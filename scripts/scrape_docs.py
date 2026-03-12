#!/usr/bin/env python3
"""
Divi 5 Docs — Content Scraper

Crawls elegantthemes.com documentation pages, extracts content,
and converts it to structured Markdown matching our doc template.

This produces DRAFT pages that need human review and enrichment
(adding tested code examples, screenshots, troubleshooting tips).

Usage:
    # Scrape a single page
    python scrape_docs.py --url "https://www.elegantthemes.com/documentation/divi/blurb/"

    # Scrape all module pages
    python scrape_docs.py --index "https://www.elegantthemes.com/documentation/divi/modules/" --category modules

    # Scrape with screenshots
    python scrape_docs.py --url "https://example.com/docs/blurb/" --screenshots

Requirements:
    pip install requests beautifulsoup4 markdownify pyyaml
"""

import argparse
import os
import re
import sys
from datetime import date
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
except ImportError:
    print("Install dependencies: pip install requests beautifulsoup4 markdownify")
    sys.exit(1)


TEMPLATE = """---
title: "{title}"
category: {category}
tags: [{tags}]
related: []
divi_version: "5.x"
last_updated: {date}
source_url: "{source_url}"
---

# {title}

{summary}

## Overview

{overview}

## Settings & Options

{settings}

## Code Examples

<!-- TODO: Add tested code examples -->

```css
/* TODO: Add CSS customization examples */
```

```php
// TODO: Add PHP hook/filter examples
```

## Common Patterns

<!-- TODO: Add 2-3 real-world use cases -->

## Version Notes

!!! note "Divi 5"
    This page documents Divi 5 behavior. Some settings or markup may differ from Divi 4.

## Troubleshooting

<!-- TODO: Add common issues and solutions -->

## Related

<!-- TODO: Add links to related pages -->
"""


def slugify(text: str) -> str:
    """Convert text to a filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text


def extract_page_content(url: str) -> dict:
    """Fetch a URL and extract the main documentation content."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Divi5Docs Scraper; +https://github.com/16wells/divi-docs)'
    }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    # Try common content selectors for Elegant Themes docs
    content_selectors = [
        '.entry-content',
        '.et_pb_text_inner',
        'article .content',
        '#content-area',
        'main article',
        'article',
    ]

    content_el = None
    for selector in content_selectors:
        content_el = soup.select_one(selector)
        if content_el:
            break

    if not content_el:
        content_el = soup.find('body')

    # Extract title
    title = ''
    title_el = soup.find('h1')
    if title_el:
        title = title_el.get_text(strip=True)
    elif soup.find('title'):
        title = soup.find('title').get_text(strip=True).split('|')[0].strip()

    # Remove navigation, sidebars, footers from content
    for tag in content_el.select('nav, .sidebar, footer, .comments, script, style, .social-share'):
        tag.decompose()

    # Extract images with their context
    images = []
    for img in content_el.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt', '')
        if src and not src.startswith('data:'):
            src = urljoin(url, src)
            images.append({'src': src, 'alt': alt})

    # Convert to markdown
    content_md = md(
        str(content_el),
        heading_style='ATX',
        bullets='-',
        strip=['script', 'style'],
    )

    # Clean up the markdown
    content_md = re.sub(r'\n{3,}', '\n\n', content_md)
    content_md = content_md.strip()

    # Try to split into summary and body
    paragraphs = [p.strip() for p in content_md.split('\n\n') if p.strip()]
    summary = paragraphs[0] if paragraphs else ''
    overview = '\n\n'.join(paragraphs[1:4]) if len(paragraphs) > 1 else ''
    settings = '\n\n'.join(paragraphs[4:]) if len(paragraphs) > 4 else '<!-- TODO: Document all settings -->'

    return {
        'title': title,
        'summary': summary,
        'overview': overview,
        'settings': settings,
        'images': images,
        'full_content': content_md,
        'url': url,
    }


def extract_links_from_index(url: str) -> list:
    """Extract documentation page links from an index/category page."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Divi5Docs Scraper; +https://github.com/16wells/divi-docs)'
    }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find links that look like documentation pages
    links = []
    base_domain = urlparse(url).netloc

    for a in soup.find_all('a', href=True):
        href = urljoin(url, a['href'])
        parsed = urlparse(href)

        # Only follow links on the same domain under /documentation/
        if parsed.netloc == base_domain and '/documentation/' in parsed.path:
            text = a.get_text(strip=True)
            if text and href not in [l['url'] for l in links]:
                links.append({'url': href, 'title': text})

    return links


def download_images(images: list, output_dir: str) -> list:
    """Download images and return local paths."""
    os.makedirs(output_dir, exist_ok=True)
    local_images = []

    for i, img in enumerate(images):
        try:
            response = requests.get(img['src'], timeout=15)
            response.raise_for_status()

            # Determine extension
            content_type = response.headers.get('content-type', '')
            if 'png' in content_type:
                ext = '.png'
            elif 'webp' in content_type:
                ext = '.webp'
            elif 'gif' in content_type:
                ext = '.gif'
            else:
                ext = '.jpg'

            filename = f"img-{i:03d}{ext}"
            if img['alt']:
                filename = f"{slugify(img['alt'])[:50]}{ext}"

            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)

            local_images.append({
                'local_path': filepath,
                'alt': img['alt'],
                'original_src': img['src'],
            })
            print(f"  📷 Downloaded: {filename}")

        except Exception as e:
            print(f"  ⚠️  Failed to download {img['src']}: {e}")

    return local_images


def generate_doc_page(data: dict, category: str, output_dir: str, download_imgs: bool = False):
    """Generate a Markdown documentation page from scraped data."""
    slug = slugify(data['title'])
    filename = f"{slug}.md"
    filepath = os.path.join(output_dir, filename)

    tags = slugify(data['title']).replace('-', ', ')

    # Download images if requested
    if download_imgs and data['images']:
        img_dir = os.path.join('docs', 'assets', 'screenshots', category, slug)
        local_images = download_images(data['images'], img_dir)

        # Add image references to the overview
        img_refs = '\n\n'.join([
            f"![{img['alt'] or 'Screenshot'}](../assets/screenshots/{category}/{slug}/{os.path.basename(img['local_path'])})"
            for img in local_images
        ])
        data['overview'] = f"{data['overview']}\n\n{img_refs}" if data['overview'] else img_refs

    content = TEMPLATE.format(
        title=data['title'],
        category=category,
        tags=tags,
        date=date.today().isoformat(),
        source_url=data['url'],
        summary=data['summary'],
        overview=data['overview'],
        settings=data['settings'],
    )

    os.makedirs(output_dir, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

    print(f"  📄 Generated: {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description='Divi 5 Docs Content Scraper')
    parser.add_argument('--url', help='Single URL to scrape')
    parser.add_argument('--index', help='Index page URL to extract links from')
    parser.add_argument('--category', default='modules', help='Doc category (modules, builder, etc.)')
    parser.add_argument('--output', default=None, help='Output directory (defaults to docs/<category>/)')
    parser.add_argument('--screenshots', action='store_true', help='Download images from pages')

    args = parser.parse_args()
    output_dir = args.output or os.path.join('docs', args.category)

    if args.url:
        print(f"Scraping: {args.url}")
        data = extract_page_content(args.url)
        generate_doc_page(data, args.category, output_dir, download_imgs=args.screenshots)

    elif args.index:
        print(f"Extracting links from: {args.index}")
        links = extract_links_from_index(args.index)
        print(f"Found {len(links)} documentation links\n")

        for i, link in enumerate(links, 1):
            print(f"[{i}/{len(links)}] {link['title']}: {link['url']}")
            try:
                data = extract_page_content(link['url'])
                generate_doc_page(data, args.category, output_dir, download_imgs=args.screenshots)
            except Exception as e:
                print(f"  ❌ Error: {e}")
            print()

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
