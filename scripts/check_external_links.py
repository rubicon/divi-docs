#!/usr/bin/env python3
"""
Scan Markdown under docs/ for http(s) links and verify they respond.

Usage:
  python3 scripts/check_external_links.py
  python3 scripts/check_external_links.py --write-report reports/external-link-check-2026-04-22.md
  python3 scripts/check_external_links.py --strict   # exit 1 if any link fails

Weekly maintenance: run after mkdocs build; review the report and fix or remove
broken URLs in the listed files. Add patterns to scripts/external_link_allowlist.txt
to skip known false positives (one substring or full URL per line).
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date
import ssl
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
ALLOWLIST_FILE = Path(__file__).resolve().parent / "external_link_allowlist.txt"
LINK_PATTERN = re.compile(r"\]\((https?://[^)\s]+)\)")
# Also catch href="..." and bare https in angle brackets (rare in this repo)
EXTRA_PATTERNS = [
    re.compile(r'href="(https?://[^"]+)"'),
    re.compile(r"<(https?://[^>]+)>"),
]

DEFAULT_WORKERS = 8
TIMEOUT = 20
USER_AGENT = "divi-docs-link-check/1.0 (+https://github.com/16wells/divi-docs)"


def build_ssl_context() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    try:
        import certifi

        ctx.load_verify_locations(certifi.where())
    except Exception:
        pass
    return ctx


@dataclass
class CheckResult:
    url: str
    ok: bool
    status: Optional[int]
    detail: str


def load_allowlist() -> list[str]:
    if not ALLOWLIST_FILE.is_file():
        return []
    lines = []
    for line in ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            lines.append(line)
    return lines


def skip_url(url: str, allowlist: list[str]) -> bool:
    u = url.rstrip(").,;]")
    for frag in allowlist:
        if frag in u:
            return True
    parsed = urlparse(u)
    if parsed.scheme not in ("http", "https"):
        return True
    return False


def _add(found: dict[str, list[tuple[str, int]]], url: str, rel: str, lineno: int) -> None:
    key = (rel, lineno)
    if key not in found[url]:
        found[url].append(key)


def normalize_url(raw: str) -> str:
    u = raw.rstrip(").,;]")
    # Strip common Markdown / punctuation artifacts
    while u.endswith((")", "]", ">", '"', "'")):
        u = u[:-1]
    return u


def collect_links() -> dict[str, list[tuple[str, int]]]:
    """url -> list of (relative_path, line_number)."""
    found: dict[str, list[tuple[str, int]]] = defaultdict(list)
    allow = load_allowlist()

    for path in sorted(DOCS_DIR.rglob("*.md")):
        if "node_modules" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(text.splitlines(), start=1):
            for m in LINK_PATTERN.finditer(line):
                url = normalize_url(m.group(1))
                if skip_url(url, allow):
                    continue
                _add(found, url, rel, lineno)
            for pat in EXTRA_PATTERNS:
                for m in pat.finditer(line):
                    url = normalize_url(m.group(1))
                    if skip_url(url, allow):
                        continue
                    _add(found, url, rel, lineno)
    return found


def _probe_get(url: str, ctx: ssl.SSLContext) -> CheckResult:
    req = urllib.request.Request(
        url,
        method="GET",
        headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            resp.read(512)
            code = resp.getcode()
            if 200 <= code < 400:
                return CheckResult(url, True, code, "ok (GET)")
            return CheckResult(url, False, code, "error")
    except urllib.error.HTTPError as e:
        if 200 <= e.code < 400:
            return CheckResult(url, True, e.code, "ok (GET)")
        return CheckResult(url, False, e.code, (e.reason or str(e))[:120])
    except urllib.error.URLError as e:
        reason = e.reason if getattr(e, "reason", None) else str(e)
        return CheckResult(url, False, None, str(reason)[:200])
    except Exception as e:
        return CheckResult(url, False, None, str(e)[:200])


def probe(url: str) -> CheckResult:
    ctx = build_ssl_context()
    req = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            code = resp.getcode()
            if 200 <= code < 400:
                return CheckResult(url, True, code, "ok")
            return CheckResult(url, False, code, "error")
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 501):
            return _probe_get(url, ctx)
        if 200 <= e.code < 400:
            return CheckResult(url, True, e.code, "ok")
        return CheckResult(url, False, e.code, (e.reason or str(e))[:120])
    except urllib.error.URLError as e:
        reason = e.reason if getattr(e, "reason", None) else str(e)
        return CheckResult(url, False, None, str(reason)[:200])
    except Exception as e:
        return CheckResult(url, False, None, str(e)[:200])


def main() -> int:
    ap = argparse.ArgumentParser(description="Check external https links in docs/")
    ap.add_argument(
        "--write-report",
        metavar="PATH",
        help="Write Markdown report to this path (directories created as needed)",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Exit with status 1 if any URL fails",
    )
    ap.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help=f"Concurrent checks (default {DEFAULT_WORKERS})",
    )
    ap.add_argument(
        "--max-urls",
        type=int,
        default=0,
        metavar="N",
        help="Only check the first N unique URLs (sorted), for smoke tests",
    )
    args = ap.parse_args()

    url_refs = collect_links()
    urls = sorted(url_refs.keys())
    if args.max_urls and args.max_urls > 0:
        urls = urls[: args.max_urls]
        url_refs = {u: url_refs[u] for u in urls}
    if not urls:
        print("No external URLs found.", file=sys.stderr)
        return 0

    print(f"Checking {len(urls)} unique URLs ({sum(len(v) for v in url_refs.values())} occurrences)…")

    results: dict[str, CheckResult] = {}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        fut = {pool.submit(probe, u): u for u in urls}
        for i, f in enumerate(as_completed(fut), start=1):
            u = fut[f]
            results[u] = f.result()
            if i % 25 == 0 or i == len(urls):
                print(f"  … {i}/{len(urls)}")

    failed = [r for r in results.values() if not r.ok]
    ok_count = len(results) - len(failed)

    lines = [
        f"# External link check — {date.today().isoformat()}",
        "",
        f"- **Unique URLs:** {len(urls)}",
        f"- **OK:** {ok_count}",
        f"- **Failed:** {len(failed)}",
        "",
        "Allowlist: `scripts/external_link_allowlist.txt` (substring match per line).",
        "",
    ]

    if failed:
        lines.append("## Failed URLs")
        lines.append("")
        lines.append("| URL | Status | Detail | Occurrences |")
        lines.append("|-----|--------|--------|-------------|")
        for r in sorted(failed, key=lambda x: x.url):
            occ = url_refs[r.url]
            occ_str = "; ".join(f"`{p}:{n}`" for p, n in occ[:5])
            if len(occ) > 5:
                occ_str += f" … (+{len(occ) - 5} more)"
            st = str(r.status) if r.status is not None else "—"
            lines.append(f"| `{r.url}` | {st} | {r.detail.replace('|', '/')} | {occ_str} |")
        lines.append("")
        lines.append("## Follow-up")
        lines.append("")
        lines.append(
            "1. Open each file at the line shown and **update or remove** the broken link.\n"
            "2. If the target is temporarily flaky, add a **substring** of the URL to "
            "`scripts/external_link_allowlist.txt` and document why.\n"
            "3. Re-run: `python3 scripts/check_external_links.py`"
        )
    else:
        lines.append("All probed URLs returned success (2xx/3xx).")
        lines.append("")

    report = "\n".join(lines)
    print(report)

    if args.write_report:
        out = Path(args.write_report)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
        print(f"\nWrote {out}", file=sys.stderr)

    if failed and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
