#!/usr/bin/env python3
"""
Divi 5 Docs — Screenshot Capture Tool

Captures, crops, and organizes screenshots from Divi sites and
elegantthemes.com documentation pages.

Usage:
    # Capture a full page screenshot
    python capture_screenshots.py --url "https://example.com/page" --output docs/assets/screenshots/modules/

    # Capture a specific element by CSS selector
    python capture_screenshots.py --url "https://example.com/page" --selector ".et_pb_blurb" --output docs/assets/screenshots/modules/blurb/

    # Batch capture from a config file
    python capture_screenshots.py --batch screenshots.yml

    # Capture with login (for wp-admin/Divi Builder pages)
    python capture_screenshots.py --url "https://example.com/wp-admin/" --login --output docs/assets/screenshots/

Requirements:
    pip install playwright pyyaml Pillow
    playwright install chromium
"""

import argparse
import asyncio
import os
import re
import sys
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Install playwright: pip install playwright && playwright install chromium")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: pip install Pillow")
    sys.exit(1)

try:
    import yaml
except ImportError:
    yaml = None


def slugify(text: str) -> str:
    """Convert text to a filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text


def optimize_image(filepath: str, max_width: int = 1200, quality: int = 85):
    """Resize and compress a screenshot for web use."""
    img = Image.open(filepath)

    # Resize if wider than max_width
    if img.width > max_width:
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((max_width, new_height), Image.LANCZOS)

    # Save as optimized PNG or WebP
    if filepath.endswith('.png'):
        img.save(filepath, 'PNG', optimize=True)
    elif filepath.endswith('.webp'):
        img.save(filepath, 'WEBP', quality=quality)
    else:
        img.save(filepath, quality=quality, optimize=True)

    return filepath


async def capture_screenshot(
    url: str,
    output_dir: str,
    filename: str = None,
    selector: str = None,
    full_page: bool = True,
    viewport_width: int = 1280,
    viewport_height: int = 800,
    wait_for: str = None,
    delay_ms: int = 2000,
    crop: dict = None,
    login_url: str = None,
    username: str = None,
    password: str = None,
    max_width: int = 1200,
):
    """Capture a screenshot of a URL or specific element."""

    os.makedirs(output_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': viewport_width, 'height': viewport_height},
            device_scale_factor=2,  # Retina-quality screenshots
        )
        page = await context.new_page()

        # Handle WordPress login if needed
        if login_url and username and password:
            await page.goto(login_url)
            await page.fill('#user_login', username)
            await page.fill('#user_pass', password)
            await page.click('#wp-submit')
            await page.wait_for_load_state('networkidle')

        # Navigate to target URL
        await page.goto(url, wait_until='networkidle')

        # Optional: wait for a specific element to appear
        if wait_for:
            await page.wait_for_selector(wait_for, timeout=10000)

        # Allow page animations/lazy-loading to complete
        await page.wait_for_timeout(delay_ms)

        # Generate filename from URL if not provided
        if not filename:
            url_path = url.split('/')[-1] or url.split('/')[-2]
            filename = slugify(url_path) or 'screenshot'

        filepath = os.path.join(output_dir, f"{filename}.png")

        if selector:
            # Capture a specific element
            element = await page.query_selector(selector)
            if element:
                await element.screenshot(path=filepath)
            else:
                print(f"  WARNING: Selector '{selector}' not found on {url}")
                await page.screenshot(path=filepath, full_page=full_page)
        else:
            # Capture full page or viewport
            await page.screenshot(path=filepath, full_page=full_page)

        await browser.close()

    # Post-process: crop if specified
    if crop and os.path.exists(filepath):
        img = Image.open(filepath)
        # crop = {top, left, right, bottom} as pixel values or percentages
        left = crop.get('left', 0)
        top = crop.get('top', 0)
        right = crop.get('right', img.width)
        bottom = crop.get('bottom', img.height)
        img = img.crop((left, top, right, bottom))
        img.save(filepath)

    # Optimize for web
    if os.path.exists(filepath):
        optimize_image(filepath, max_width=max_width)
        size_kb = os.path.getsize(filepath) / 1024
        print(f"  ✅ {filepath} ({size_kb:.0f} KB)")

    return filepath


async def batch_capture(config_path: str):
    """Process a YAML batch config file."""
    if not yaml:
        print("Install pyyaml for batch mode: pip install pyyaml")
        sys.exit(1)

    with open(config_path) as f:
        config = yaml.safe_load(f)

    defaults = config.get('defaults', {})
    captures = config.get('captures', [])

    print(f"Processing {len(captures)} screenshot captures...")

    for i, capture in enumerate(captures, 1):
        # Merge defaults with per-capture settings
        settings = {**defaults, **capture}
        url = settings.pop('url')
        print(f"\n[{i}/{len(captures)}] {url}")

        await capture_screenshot(url=url, **settings)

    print(f"\nDone! Captured {len(captures)} screenshots.")


def main():
    parser = argparse.ArgumentParser(description='Divi 5 Docs Screenshot Capture')
    parser.add_argument('--url', help='URL to capture')
    parser.add_argument('--output', default='docs/assets/screenshots/', help='Output directory')
    parser.add_argument('--filename', help='Output filename (without extension)')
    parser.add_argument('--selector', help='CSS selector for element-specific capture')
    parser.add_argument('--full-page', action='store_true', default=True, help='Capture full page')
    parser.add_argument('--viewport-only', action='store_true', help='Capture viewport only')
    parser.add_argument('--width', type=int, default=1280, help='Viewport width')
    parser.add_argument('--height', type=int, default=800, help='Viewport height')
    parser.add_argument('--wait-for', help='CSS selector to wait for before capture')
    parser.add_argument('--delay', type=int, default=2000, help='Delay in ms after page load')
    parser.add_argument('--max-width', type=int, default=1200, help='Max image width in px')
    parser.add_argument('--batch', help='YAML config file for batch captures')
    parser.add_argument('--login', action='store_true', help='Login to WordPress first')
    parser.add_argument('--login-url', help='WordPress login URL')
    parser.add_argument('--username', help='WordPress username')
    parser.add_argument('--password', help='WordPress password')

    args = parser.parse_args()

    if args.batch:
        asyncio.run(batch_capture(args.batch))
    elif args.url:
        asyncio.run(capture_screenshot(
            url=args.url,
            output_dir=args.output,
            filename=args.filename,
            selector=args.selector,
            full_page=not args.viewport_only,
            viewport_width=args.width,
            viewport_height=args.height,
            wait_for=args.wait_for,
            delay_ms=args.delay,
            max_width=args.max_width,
            login_url=args.login_url if args.login else None,
            username=args.username,
            password=args.password,
        ))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
