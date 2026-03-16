#!/usr/bin/env python3
"""
Update module documentation pages with screenshot references and ET walkthrough links.

For each module doc:
1. Uncomments commented-out screenshot references where the file actually exists
2. Replaces "<!-- TODO: Add animated GIF -->" with a link to the ET Help Center article
3. Reports what was updated

Usage:
  python scripts/update_docs_with_screenshots.py            # Process all modules
  python scripts/update_docs_with_screenshots.py --dry-run   # Preview changes
"""

import argparse
import re
import sys
from pathlib import Path

DOCS_DIR = Path("docs/modules")
SCREENSHOTS_DIR = Path("docs/assets/screenshots/modules")


def get_source_url(content: str) -> str | None:
    """Extract source_url from frontmatter."""
    fm_match = re.match(r"^---\n(.+?)\n---", content, re.DOTALL)
    if not fm_match:
        return None
    for line in fm_match.group(1).split("\n"):
        if "source_url" in line:
            m = re.search(r'["\']([^"\']+)["\']', line)
            if m:
                return m.group(1)
    return None


def get_module_title(content: str, slug: str) -> str:
    """Extract module title from frontmatter or heading."""
    m = re.search(r'^title:\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return slug.replace("-", " ").title()


def uncomment_screenshot(content: str, slug: str) -> tuple[str, list[str]]:
    """
    Uncomment screenshot references where the actual file exists.
    Returns (new_content, list_of_uncommented_files).
    """
    uncommented = []

    for tab in ["content", "design", "advanced"]:
        filename = f"settings-{tab}.png"
        filepath = SCREENSHOTS_DIR / slug / filename

        if not filepath.exists() or filepath.stat().st_size < 1024:
            continue

        # Pattern: <!-- ![Alt text](../assets/screenshots/modules/{slug}/settings-{tab}.png){ loading=lazy } -->
        # Possibly followed by a TODO comment on the next line
        pattern = (
            r"<!-- (!\[[^\]]*\]\(\.\.\/assets\/screenshots\/modules\/"
            + re.escape(slug)
            + r"\/"
            + re.escape(filename)
            + r"\)\s*\{\s*loading=lazy\s*\}) -->"
        )

        match = re.search(pattern, content)
        if match:
            # Get the module title for the caption
            title = get_module_title(content, slug)
            short_title = title.replace(" Module", "").strip()
            tab_display = tab.capitalize()

            # Build replacement: uncommented image + caption
            replacement = (
                match.group(1)
                + f"\n*The {tab_display} tab settings panel for the {short_title} module.*"
            )
            content = content[:match.start()] + replacement + content[match.end():]
            uncommented.append(filename)

            # Remove the TODO comment that follows (if present)
            todo_pattern = r"\n<!-- TODO: Capture " + tab_display + r" tab screenshot -->"
            content = re.sub(todo_pattern, "", content, count=1)

    return content, uncommented


def replace_gif_todo(content: str, slug: str) -> tuple[str, bool]:
    """
    Replace <!-- TODO: Add animated GIF --> with a link to the ET article.
    Returns (new_content, was_replaced).
    """
    todo_pattern = r"<!-- TODO: Add animated GIF demonstrating module insertion -->"

    if not re.search(todo_pattern, content):
        return content, False

    source_url = get_source_url(content)
    if not source_url:
        # Can't link without a source URL
        return content, False

    replacement = (
        "For an animated walkthrough of adding and configuring this module, see the\n"
        f"[official Elegant Themes documentation]({source_url})."
    )

    content = re.sub(todo_pattern, replacement, content, count=1)
    return content, True


def process_module(slug: str, dry_run: bool = False) -> dict:
    """Process a single module doc. Returns report dict."""
    md_path = DOCS_DIR / f"{slug}.md"
    if not md_path.exists():
        return {"slug": slug, "status": "no_doc"}

    content = md_path.read_text(encoding="utf-8")
    original = content

    # Uncomment screenshot references
    content, uncommented = uncomment_screenshot(content, slug)

    # Replace GIF TODO with ET link
    content, gif_replaced = replace_gif_todo(content, slug)

    report = {
        "slug": slug,
        "uncommented": uncommented,
        "gif_replaced": gif_replaced,
        "changed": content != original,
    }

    if content != original and not dry_run:
        md_path.write_text(content, encoding="utf-8")
        report["status"] = "updated"
    elif content != original:
        report["status"] = "would_update"
    else:
        report["status"] = "no_changes"

    return report


def main():
    parser = argparse.ArgumentParser(description="Update module docs with screenshots and ET links")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--modules", type=str, default=None, help="Comma-separated module slugs")
    args = parser.parse_args()

    if not DOCS_DIR.is_dir():
        print("Run this script from the repo root.")
        sys.exit(1)

    if args.modules:
        slugs = args.modules.split(",")
    else:
        slugs = sorted(f.stem for f in DOCS_DIR.glob("*.md") if f.name != "index.md")

    print(f"Processing {len(slugs)} module docs...")
    if args.dry_run:
        print("(DRY RUN — no files will be modified)\n")
    else:
        print()

    updated = 0
    screenshots_added = 0
    gifs_replaced = 0

    for slug in slugs:
        report = process_module(slug, dry_run=args.dry_run)

        if report.get("changed"):
            status = "WOULD UPDATE" if args.dry_run else "UPDATED"
            details = []
            if report["uncommented"]:
                details.append(f"screenshots: {', '.join(report['uncommented'])}")
                screenshots_added += len(report["uncommented"])
            if report["gif_replaced"]:
                details.append("GIF TODO → ET link")
                gifs_replaced += 1
            print(f"  ✅ {slug} — {status} ({'; '.join(details)})")
            updated += 1
        elif report.get("status") == "no_doc":
            pass  # Silent skip
        else:
            pass  # No changes needed, silent

    print(f"\n{'=' * 50}")
    action = "Would update" if args.dry_run else "Updated"
    print(f"{action}: {updated} docs")
    print(f"Screenshots uncommented: {screenshots_added}")
    print(f"GIF TODOs replaced: {gifs_replaced}")


if __name__ == "__main__":
    main()
