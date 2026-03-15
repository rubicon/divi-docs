#!/usr/bin/env python3
"""Add a sidebar with navigation links to all module demo subpages."""

import re
import time
import requests

WP_URL = "https://www.16wells.dev/wp-json/wp/v2/pages"
AUTH = ("sshean", "KjGF bJG7 CInC aCJp U0BV nOTt")
BV = "5.0.3"


def get_child_pages(retries=5):
    for attempt in range(retries):
        try:
            resp = requests.get(WP_URL, auth=AUTH,
                                params={"parent": 10, "per_page": 100, "status": "publish"},
                                timeout=60)
            return sorted(resp.json(), key=lambda x: x["title"]["rendered"])
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            wait = 15 * (attempt + 1)
            print(f"  ⏳ Fetch failed: {type(e).__name__}, retry in {wait}s ({attempt+2}/{retries})")
            time.sleep(wait)
    raise RuntimeError("Could not fetch child pages after retries")


def build_sidebar_html(pages):
    links = []
    for p in pages:
        title = p["title"]["rendered"]
        slug = p["slug"]
        links.append(f'<li><a href="/module-demos/{slug}/">{title}</a></li>')
    return '<h4>Module Demos</h4><ul>' + "".join(links) + "</ul>"


def extract_module_content(raw):
    """Extract the module content from inside the first column."""
    col_match = re.search(
        r'<!-- wp:divi/column[^>]*-->\s*\n?(.*?)\n?\s*<!-- /wp:divi/column -->',
        raw, re.DOTALL
    )
    if col_match:
        return col_match.group(1).strip()
    return raw


def build_two_column_content(module_content, sidebar_escaped):
    return f'''<!-- wp:divi/placeholder --><!-- wp:divi/section {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/row {{"module":{{"advanced":{{"flexColumnStructure":{{"desktop":{{"value":"equal-columns_2"}}}}}},"decoration":{{"layout":{{"desktop":{{"value":{{"flexWrap":"nowrap"}}}}}}}}}},"builderVersion":"{BV}"}} -->
<!-- wp:divi/column {{"module":{{"decoration":{{"sizing":{{"desktop":{{"value":{{"flexType":"18_24"}}}}}}}}}},"builderVersion":"{BV}"}} -->
{module_content}
<!-- /wp:divi/column -->
<!-- wp:divi/column {{"module":{{"decoration":{{"sizing":{{"desktop":{{"value":{{"flexType":"6_24"}}}}}}}}}},"builderVersion":"{BV}"}} -->
<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"{sidebar_escaped}"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/column -->
<!-- /wp:divi/row -->
<!-- /wp:divi/section --><!-- /wp:divi/placeholder -->'''


def update_page(page_id, new_content, title, retries=3):
    for attempt in range(retries):
        try:
            resp = requests.post(
                f"{WP_URL}/{page_id}", auth=AUTH,
                json={"content": new_content}, timeout=90
            )
            if resp.status_code == 200:
                return True
            else:
                print(f"  ❌ {title}: HTTP {resp.status_code}")
                return False
        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError) as e:
            wait = 10 * (attempt + 1)
            print(f"  ⏳ {title}: {type(e).__name__}, retry in {wait}s ({attempt+2}/{retries})")
            time.sleep(wait)
    print(f"  ❌ {title}: failed after {retries} attempts")
    return False


def main():
    print("Fetching child pages...")
    pages = get_child_pages()
    print(f"Found {len(pages)} pages\n")

    sidebar_html = build_sidebar_html(pages)
    sidebar_escaped = sidebar_html.replace('"', '\\"')

    # Check which pages already have the sidebar (have 2 columns)
    success = 0
    skipped = 0
    failed = 0

    for p in pages:
        page_id = p["id"]
        title = p["title"]["rendered"]
        slug = p["slug"]

        # Fetch raw content
        try:
            resp = requests.get(f"{WP_URL}/{page_id}?context=edit", auth=AUTH, timeout=30)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            time.sleep(10)
            try:
                resp = requests.get(f"{WP_URL}/{page_id}?context=edit", auth=AUTH, timeout=30)
            except:
                print(f"  ❌ {title}: could not fetch")
                failed += 1
                continue

        raw = resp.json()["content"]["raw"]

        # Check if sidebar already added (has Module Demos heading in content)
        if "Module Demos</h4>" in raw:
            print(f"  ⏭  {title} (already has sidebar)")
            skipped += 1
            continue

        module_content = extract_module_content(raw)
        new_content = build_two_column_content(module_content, sidebar_escaped)

        if update_page(page_id, new_content, title):
            print(f"  ✅ {title}")
            success += 1
        else:
            failed += 1

        time.sleep(2)

    print(f"\n{'='*50}")
    print(f"DONE: {success} updated, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
