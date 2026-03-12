#!/usr/bin/env python3
"""
Divi 5 Docs — Content Monitor

Checks for updates to source documentation, new Divi releases,
community contributions, and content gaps. Generates a report
of what needs attention.

Designed to be run on a schedule (weekly or biweekly) via Claude Code
or a cron job.

Usage:
    python scripts/monitor_updates.py --all
    python scripts/monitor_updates.py --sources
    python scripts/monitor_updates.py --gaps
    python scripts/monitor_updates.py --releases

Output:
    Writes a report to reports/update-report-YYYY-MM-DD.md
"""

import argparse
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Install dependencies: pip install requests beautifulsoup4")
    sys.exit(1)

try:
    import yaml
except ImportError:
    yaml = None


REPORT_DIR = "reports"
DOCS_DIR = "docs"
ELEGANT_THEMES_BASE = "https://www.elegantthemes.com"


def check_source_updates(docs_dir: str) -> list:
    """Check if source URLs have been updated since our last_updated date."""
    findings = []

    for md_file in Path(docs_dir).rglob("*.md"):
        content = md_file.read_text()

        # Extract frontmatter
        fm_match = re.match(r'^---\n(.+?)\n---', content, re.DOTALL)
        if not fm_match:
            continue

        fm_text = fm_match.group(1)

        # Extract source_url and last_updated
        source_match = re.search(r'source_url:\s*["\'](.+?)["\']', fm_text)
        date_match = re.search(r'last_updated:\s*(\S+)', fm_text)

        if not source_match:
            continue

        source_url = source_match.group(1)
        our_date = date_match.group(1) if date_match else "unknown"

        try:
            resp = requests.head(source_url, timeout=10, allow_redirects=True,
                                 headers={'User-Agent': 'Divi5Docs Monitor'})

            # Check Last-Modified header
            last_modified = resp.headers.get('Last-Modified', '')
            status = resp.status_code

            if status == 404:
                findings.append({
                    'file': str(md_file),
                    'source_url': source_url,
                    'issue': 'SOURCE_GONE',
                    'detail': f'Source URL returns 404 — page may have been moved or removed',
                    'our_date': our_date,
                })
            elif status == 301 or status == 302:
                findings.append({
                    'file': str(md_file),
                    'source_url': source_url,
                    'issue': 'SOURCE_REDIRECTED',
                    'detail': f'Source URL redirects to {resp.headers.get("Location", "unknown")}',
                    'our_date': our_date,
                })
            elif last_modified:
                findings.append({
                    'file': str(md_file),
                    'source_url': source_url,
                    'issue': 'CHECK_CONTENT',
                    'detail': f'Source last modified: {last_modified}. Our page: {our_date}',
                    'our_date': our_date,
                })

        except Exception as e:
            findings.append({
                'file': str(md_file),
                'source_url': source_url,
                'issue': 'FETCH_ERROR',
                'detail': str(e),
                'our_date': our_date,
            })

    return findings


def check_content_gaps(docs_dir: str) -> list:
    """Identify pages that are placeholders or have TODO markers."""
    gaps = []

    for md_file in Path(docs_dir).rglob("*.md"):
        if md_file.name == 'index.md':
            continue

        content = md_file.read_text()

        todo_count = content.count('<!-- TODO')
        is_placeholder = 'Placeholder' in content and 'needs community contributions' in content
        has_no_settings = '## Settings & Options' not in content and 'modules/' in str(md_file)
        word_count = len(content.split())

        if is_placeholder:
            gaps.append({
                'file': str(md_file),
                'issue': 'PLACEHOLDER',
                'detail': 'Page is a stub placeholder with no real content',
                'word_count': word_count,
            })
        elif todo_count > 3:
            gaps.append({
                'file': str(md_file),
                'issue': 'MANY_TODOS',
                'detail': f'{todo_count} TODO markers — needs enrichment',
                'word_count': word_count,
            })
        elif has_no_settings:
            gaps.append({
                'file': str(md_file),
                'issue': 'MISSING_SETTINGS',
                'detail': 'Module page has no Settings section',
                'word_count': word_count,
            })

    return gaps


def check_divi_releases() -> list:
    """Check for new Divi releases and changelog entries."""
    findings = []
    urls_to_check = [
        "https://www.elegantthemes.com/blog/theme-releases/divi-release-notes",
        "https://www.elegantthemes.com/api/changelog/divi",
    ]

    for url in urls_to_check:
        try:
            resp = requests.get(url, timeout=15,
                                headers={'User-Agent': 'Divi5Docs Monitor'})
            if resp.status_code == 200:
                findings.append({
                    'url': url,
                    'status': 'ACCESSIBLE',
                    'detail': f'Check for new release notes. Response size: {len(resp.text)} bytes',
                })
        except Exception as e:
            findings.append({
                'url': url,
                'status': 'ERROR',
                'detail': str(e),
            })

    return findings


def check_new_elegant_themes_docs() -> list:
    """Scan the ET documentation index for pages we haven't scraped yet."""
    findings = []

    # Get our known source URLs
    known_urls = set()
    for md_file in Path(DOCS_DIR).rglob("*.md"):
        content = md_file.read_text()
        source_match = re.search(r'source_url:\s*["\'](.+?)["\']', content)
        if source_match:
            known_urls.add(source_match.group(1).rstrip('/'))

    # Check ET documentation index
    index_urls = [
        "https://www.elegantthemes.com/documentation/divi/",
        "https://www.elegantthemes.com/documentation/divi/modules/",
    ]

    for index_url in index_urls:
        try:
            resp = requests.get(index_url, timeout=15,
                                headers={'User-Agent': 'Divi5Docs Monitor'})
            soup = BeautifulSoup(resp.text, 'html.parser')

            for a in soup.find_all('a', href=True):
                href = a['href']
                if '/documentation/divi/' in href:
                    full_url = href if href.startswith('http') else ELEGANT_THEMES_BASE + href
                    full_url = full_url.rstrip('/')

                    if full_url not in known_urls and '/documentation/divi/' in full_url:
                        title = a.get_text(strip=True)
                        if title and len(title) > 2:
                            findings.append({
                                'url': full_url,
                                'title': title,
                                'issue': 'NEW_PAGE',
                                'detail': f'Documentation page exists at ET but not in our repo',
                            })

        except Exception as e:
            findings.append({
                'url': index_url,
                'issue': 'SCAN_ERROR',
                'detail': str(e),
            })

    # Deduplicate
    seen = set()
    unique = []
    for f in findings:
        if f.get('url') not in seen:
            seen.add(f.get('url'))
            unique.append(f)

    return unique


def check_community_resources() -> list:
    """Search for community Divi 5 resources we might want to reference or incorporate."""
    findings = []

    search_terms = [
        "Divi 5 documentation",
        "Divi 5 tutorial 2026",
        "Divi 5 developer guide",
        "Divi 5 CSS class reference",
        "Divi 5 hooks filters",
    ]

    # This would use a search API in production.
    # For now, just flag that these searches should be done manually or via web_search.
    for term in search_terms:
        findings.append({
            'search_term': term,
            'action': 'MANUAL_SEARCH',
            'detail': f'Search for "{term}" and check for new resources',
        })

    return findings


def generate_report(
    source_updates: list,
    content_gaps: list,
    release_checks: list,
    new_pages: list,
    community: list,
) -> str:
    """Generate a Markdown report."""
    today = date.today().isoformat()
    lines = [
        f"# Divi 5 Docs — Update Report ({today})",
        "",
        "Auto-generated by `scripts/monitor_updates.py`. Review and act on findings below.",
        "",
    ]

    # Summary
    total_items = len(source_updates) + len(content_gaps) + len(new_pages)
    lines.append(f"## Summary")
    lines.append(f"")
    lines.append(f"- **Source URL issues:** {len(source_updates)}")
    lines.append(f"- **Content gaps (placeholders/TODOs):** {len(content_gaps)}")
    lines.append(f"- **New ET doc pages we don't have:** {len(new_pages)}")
    lines.append(f"- **Total action items:** {total_items}")
    lines.append("")

    # Source Updates
    if source_updates:
        lines.append("## Source URL Issues")
        lines.append("")
        lines.append("| File | Issue | Detail |")
        lines.append("|------|-------|--------|")
        for f in source_updates:
            lines.append(f"| `{f['file']}` | {f['issue']} | {f['detail']} |")
        lines.append("")

    # Content Gaps
    if content_gaps:
        lines.append("## Content Gaps")
        lines.append("")
        lines.append("| File | Issue | Words | Detail |")
        lines.append("|------|-------|-------|--------|")
        for g in sorted(content_gaps, key=lambda x: x.get('word_count', 0)):
            lines.append(f"| `{g['file']}` | {g['issue']} | {g.get('word_count', '?')} | {g['detail']} |")
        lines.append("")

    # New Pages
    if new_pages:
        lines.append("## New Documentation Pages at Elegant Themes")
        lines.append("")
        lines.append("These pages exist at elegantthemes.com but don't have a corresponding page in our repo:")
        lines.append("")
        for p in new_pages:
            lines.append(f"- [{p.get('title', 'Unknown')}]({p['url']})")
        lines.append("")

    # Release Checks
    if release_checks:
        lines.append("## Divi Release Checks")
        lines.append("")
        for r in release_checks:
            lines.append(f"- **{r.get('url', 'Unknown')}**: {r['detail']}")
        lines.append("")

    # Community Resources
    if community:
        lines.append("## Community Resource Searches")
        lines.append("")
        lines.append("Run these searches to find new Divi 5 resources to incorporate:")
        lines.append("")
        for c in community:
            lines.append(f"- Search: `{c['search_term']}`")
        lines.append("")

    # Action Items
    lines.append("## Recommended Actions")
    lines.append("")
    lines.append("1. **Fix broken source URLs** — update or remove source_url in frontmatter")
    lines.append("2. **Fill placeholder pages** — prioritize high-traffic modules")
    lines.append("3. **Scrape new ET pages** — run `python scripts/scrape_docs.py` for new URLs")
    lines.append("4. **Check for Divi updates** — review release notes for changed behavior")
    lines.append("5. **Run community searches** — find new resources to reference or incorporate")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Divi 5 Docs Content Monitor')
    parser.add_argument('--all', action='store_true', help='Run all checks')
    parser.add_argument('--sources', action='store_true', help='Check source URL updates')
    parser.add_argument('--gaps', action='store_true', help='Check content gaps')
    parser.add_argument('--releases', action='store_true', help='Check Divi releases')
    parser.add_argument('--new-pages', action='store_true', help='Check for new ET doc pages')
    parser.add_argument('--community', action='store_true', help='Check community resources')

    args = parser.parse_args()

    if not any([args.all, args.sources, args.gaps, args.releases, args.new_pages, args.community]):
        args.all = True

    source_updates = check_source_updates(DOCS_DIR) if args.all or args.sources else []
    content_gaps = check_content_gaps(DOCS_DIR) if args.all or args.gaps else []
    release_checks = check_divi_releases() if args.all or args.releases else []
    new_pages = check_new_elegant_themes_docs() if args.all or args.new_pages else []
    community = check_community_resources() if args.all or args.community else []

    report = generate_report(source_updates, content_gaps, release_checks, new_pages, community)

    os.makedirs(REPORT_DIR, exist_ok=True)
    report_path = os.path.join(REPORT_DIR, f"update-report-{date.today().isoformat()}.md")
    with open(report_path, 'w') as f:
        f.write(report)

    print(f"Report written to {report_path}")
    print(f"  Source issues: {len(source_updates)}")
    print(f"  Content gaps: {len(content_gaps)}")
    print(f"  New ET pages: {len(new_pages)}")
    print(f"  Release checks: {len(release_checks)}")


if __name__ == '__main__':
    main()
