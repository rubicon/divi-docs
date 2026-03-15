#!/usr/bin/env python3
"""
Update module documentation pages to:
1. Insert or replace the element screenshot (element.png) in the Overview section.
2. Link "View A Live Demo Of This Module" to the 16wells.dev demo page.

Run after capture_demo_screenshots.py, or let the capture script invoke this at the end.
Only processes modules that have docs/assets/screenshots/modules/{slug}/element.png.
"""

import re
import sys
from pathlib import Path

DOCS_MODULES = Path("docs/modules")
SCREENSHOTS_BASE = Path("docs/assets/screenshots/modules")
DEMO_BASE_URL = "https://www.16wells.dev/module-demos"


def get_module_title(content: str, slug: str) -> str:
    """Extract module display name from frontmatter or first heading."""
    # Frontmatter: title: "Button" or title: 'Button'
    m = re.search(r'^title:\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    # First # Heading
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    # Fallback: slug to title (e.g. bar-counter -> Bar Counter)
    return slug.replace("-", " ").title()


def ensure_demo_link(content: str, slug: str) -> str:
    """Replace plain 'View A Live Demo Of This Module' with link to 16wells.dev."""
    link = f"[View A Live Demo Of This Module]({DEMO_BASE_URL}/{slug}/)"
    # Only replace if not already a link
    if re.search(r'\[View A Live Demo Of This Module\]\s*\(http', content):
        return content
    return content.replace("View A Live Demo Of This Module", link, 1)


def build_element_block(title: str, slug: str) -> str:
    """Markdown block for element screenshot and caption."""
    # Avoid "Blog Module module" when title is "Blog Module"
    short_title = title.replace(" Module", "").strip() or title
    return (
        f"![{short_title} module](../assets/screenshots/modules/{slug}/element.png){{ loading=lazy }}\n"
        f"*The {short_title} module as it appears on the live demo.*"
    )


def ensure_element_screenshot_in_overview(content: str, slug: str, title: str) -> str:
    """
    In the Overview section, ensure the element screenshot is present:
    - If there's already an image for this module (any filename), replace it with element.png block.
    - If there's only commented placeholder(s), replace with live element block.
    - If no image, insert element block after the demo line.
    """
    element_block = build_element_block(title, slug)

    # Find Overview section: from "## Overview" to next "## " or "### Content Tab" or "### Design Tab"
    overview_start = content.find("## Overview")
    if overview_start == -1:
        return content

    # End of overview: next ## or ### (Content Tab / Design Tab)
    rest = content[overview_start:]
    end_match = re.search(r'\n(## |### Content Tab|### Design Tab)', rest)
    overview_end = overview_start + (end_match.start() if end_match else len(rest))
    overview = content[overview_start:overview_end]
    before_overview = content[:overview_start]
    after_overview = content[overview_end:]

    # Pattern: optional TODO line, optional image line (active or commented), optional caption line (active or commented)
    # Image line: ![...](.../modules/slug/anything.png){ loading=lazy } or commented
    slug_escaped = re.escape(slug)
    image_pattern = (
        r'(?:\s*<!-- TODO:[^>]*-->)?\s*'
        r'(?:<!--\s*)?'
        r'!\[[^\]]*\]\s*\(\s*\.\./assets/screenshots/modules/' + slug_escaped + r'/[^)]+\)\s*\{\s*loading=lazy\s*\}(?:\s*-->)?'
        r'\s*'
        r'(?:\*\s*[^*]+\s*\*|<!--\s*\*\s*[^*]+\s*\*\s*-->)?\s*'
    )

    if re.search(r'\.\./assets/screenshots/modules/' + slug_escaped + r'/', overview):
        # Replace existing image block (any filename) with element.png block
        new_overview = re.sub(image_pattern, "\n\n" + element_block + "\n\n", overview, count=1)
        # Collapse multiple newlines
        new_overview = re.sub(r'\n{3,}', '\n\n', new_overview)
    else:
        # No image for this module yet: insert after "View A Live Demo" link or at end of Overview
        demo_link = "[View A Live Demo Of This Module](" + DEMO_BASE_URL + "/" + slug + "/)"
        if f"modules/{slug}/element.png" in overview:
            new_overview = overview
        elif demo_link in overview:
            new_overview = overview.replace(demo_link, demo_link + "\n\n" + element_block, 1)
        elif "View A Live Demo Of This Module" in overview:
            new_overview = overview.replace(
                "View A Live Demo Of This Module",
                demo_link + "\n\n" + element_block,
                1,
            )
        else:
            # No demo line (e.g. blog, text): add demo link + element block before end of Overview
            new_overview = overview.rstrip() + "\n\n" + demo_link + "\n\n" + element_block + "\n"
    return before_overview + new_overview + after_overview


def process_module(slug: str) -> bool:
    """Update one module doc. Returns True if file was modified."""
    md_path = DOCS_MODULES / f"{slug}.md"
    element_path = SCREENSHOTS_BASE / slug / "element.png"

    if not element_path.exists():
        return False
    if not md_path.exists():
        print(f"  ⚠ No doc for {slug} at {md_path}")
        return False

    content = md_path.read_text(encoding="utf-8")
    title = get_module_title(content, slug)

    new_content = content
    new_content = ensure_demo_link(new_content, slug)
    new_content = ensure_element_screenshot_in_overview(new_content, slug, title)

    if new_content != content:
        md_path.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    if not DOCS_MODULES.is_dir() or not SCREENSHOTS_BASE.is_dir():
        print("Run this script from the repo root.")
        sys.exit(1)

    # All slugs that have element.png
    slugs = sorted(
        d.name for d in SCREENSHOTS_BASE.iterdir()
        if d.is_dir() and (d / "element.png").exists()
    )
    if not slugs:
        print("No module screenshots found (docs/assets/screenshots/modules/*/element.png).")
        print("Run capture_demo_screenshots.py first.")
        sys.exit(0)

    print(f"Updating module docs for {len(slugs)} modules with element screenshots...\n")
    updated = 0
    for slug in slugs:
        if process_module(slug):
            print(f"  ✅ {slug}")
            updated += 1
        else:
            print(f"  ⏭ {slug} (no changes)")
    print(f"\n{'='*50}")
    print(f"DONE: {updated} doc(s) updated.")


if __name__ == "__main__":
    main()
