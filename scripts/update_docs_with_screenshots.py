#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update module doc pages with screenshot references.

For each module that has settings screenshots captured:
- Uncomments screenshot image references
- Replaces animated GIF TODO markers with ET walkthrough links
- Only touches lines that reference screenshots - preserves all other content

Usage:
    python3 scripts/update_docs_with_screenshots.py
    python3 scripts/update_docs_with_screenshots.py --dry-run
"""

import argparse
import re
import sys
from pathlib import Path


DOCS_DIR = Path("docs/modules")
SCREENSHOTS_DIR = Path("docs/assets/screenshots/modules")
MIN_FILE_SIZE = 1024  # 1KB - skip tiny/corrupt images


def get_source_url(content: str) -> str:
    """Extract source_url from frontmatter."""
    match = re.search(r'source_url:\s*["\'](.+?)["\']', content)
    return match.group(1) if match else ""


def update_module_doc(md_path: Path, dry_run: bool = False) -> dict:
    """Update a single module doc with screenshot references.

    Returns dict with counts of changes made.
    """
    slug = md_path.stem
    screenshot_dir = SCREENSHOTS_DIR / slug
    changes = {"uncommented": 0, "gif_replaced": 0}

    if not md_path.exists():
        return changes

    content = md_path.read_text()
    original = content
    source_url = get_source_url(content)

    # Check which settings screenshots exist and are valid
    has_content = (screenshot_dir / "settings-content.png").exists() and \
                  (screenshot_dir / "settings-content.png").stat().st_size > MIN_FILE_SIZE
    has_design = (screenshot_dir / "settings-design.png").exists() and \
                 (screenshot_dir / "settings-design.png").stat().st_size > MIN_FILE_SIZE
    has_advanced = (screenshot_dir / "settings-advanced.png").exists() and \
                   (screenshot_dir / "settings-advanced.png").stat().st_size > MIN_FILE_SIZE

    # Uncomment screenshot references where the file exists
    screenshot_map = {
        "settings-content.png": has_content,
        "settings-design.png": has_design,
        "settings-advanced.png": has_advanced,
    }

    for filename, exists in screenshot_map.items():
        if not exists:
            continue

        # Pattern: <!-- ![Alt text](../path/to/settings-content.png){ loading=lazy } -->
        pattern = rf'<!-- (!\[.*?\]\(.*?{re.escape(filename)}.*?\).*?) -->'
        matches = re.findall(pattern, content)
        if matches:
            for match in matches:
                content = content.replace(f"<!-- {match} -->", match)
                changes["uncommented"] += 1

    # Replace animated GIF TODO markers with ET walkthrough link
    if source_url:
        gif_patterns = [
            r'<!-- TODO: Add animated GIF demonstrating.*?-->',
            r'<!-- TODO: Add animated GIF.*?-->',
        ]
        replacement = f"For an animated walkthrough of this module, see the [official Elegant Themes documentation]({source_url})."

        for pattern in gif_patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                changes["gif_replaced"] += 1
                content = new_content

    # Write if changed
    if content != original:
        if not dry_run:
            md_path.write_text(content)
        return changes

    return changes


def main():
    parser = argparse.ArgumentParser(description="Update module docs with screenshot references")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    parser.add_argument("--module", help="Update one specific module")
    args = parser.parse_args()

    if args.module:
        files = [DOCS_DIR / f"{args.module}.md"]
    else:
        files = sorted(DOCS_DIR.glob("*.md"))

    total_uncommented = 0
    total_gif = 0
    updated_files = 0

    for md_path in files:
        if md_path.name == "index.md":
            continue

        changes = update_module_doc(md_path, dry_run=args.dry_run)

        if changes["uncommented"] or changes["gif_replaced"]:
            updated_files += 1
            total_uncommented += changes["uncommented"]
            total_gif += changes["gif_replaced"]
            action = "Would update" if args.dry_run else "Updated"
            print(f"  {action}: {md_path.name} "
                  f"(+{changes['uncommented']} screenshots, "
                  f"+{changes['gif_replaced']} GIF replacements)")

    print(f"\n=== Summary ===")
    print(f"  Files {'checked' if args.dry_run else 'updated'}: {updated_files}")
    print(f"  Screenshots uncommented: {total_uncommented}")
    print(f"  GIF TODOs replaced: {total_gif}")
    if args.dry_run:
        print(f"  (Dry run - no files were modified)")


if __name__ == "__main__":
    main()
