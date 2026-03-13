#!/usr/bin/env python3
"""Capture module screenshots from Elegant Themes documentation pages."""

import asyncio
import os
import re
from pathlib import Path

from PIL import Image
from playwright.async_api import async_playwright


DOCS_DIR = Path('docs/modules')
SCREENSHOTS_DIR = Path('docs/assets/screenshots/modules')


def get_module_urls():
    """Scan docs/modules/ for source URLs."""
    modules = []
    for md_file in DOCS_DIR.glob('*.md'):
        if md_file.name == 'index.md':
            continue
        content = md_file.read_text()
        fm_match = re.match(r'^---\n(.+?)\n---', content, re.DOTALL)
        if not fm_match:
            continue

        slug = md_file.stem
        source_url = None
        for line in fm_match.group(1).split('\n'):
            if 'source_url' in line:
                url_match = re.search(r'["\'](.+?)["\']', line)
                if url_match:
                    source_url = url_match.group(1)

        if not source_url:
            source_url = f'https://www.elegantthemes.com/documentation/divi/{slug}/'

        modules.append({'slug': slug, 'url': source_url})

    return sorted(modules, key=lambda m: m['slug'])


async def capture_module_screenshots():
    modules = get_module_urls()
    print(f"Found {len(modules)} modules to capture")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 800},
            device_scale_factor=2,
        )

        captured_count = 0
        error_count = 0

        for i, mod in enumerate(modules, 1):
            slug = mod['slug']
            url = mod['url']
            out_dir = SCREENSHOTS_DIR / slug
            out_dir.mkdir(parents=True, exist_ok=True)

            # Skip if overview already captured
            if (out_dir / 'overview.png').exists() and (out_dir / 'overview.png').stat().st_size > 1000:
                print(f'[{i}/{len(modules)}] SKIP {slug} (already captured)')
                continue

            print(f'[{i}/{len(modules)}] Capturing: {slug}')

            try:
                page = await context.new_page()
                resp = await page.goto(url, wait_until='networkidle', timeout=30000)

                if resp and resp.status == 404:
                    print(f'  ⚠ 404 - skipping')
                    await page.close()
                    error_count += 1
                    continue

                await page.wait_for_timeout(2000)

                # Dismiss popups/cookie banners
                for selector in [
                    '[class*="close"]', '[class*="dismiss"]',
                    '.cookie-notice .button', '#cookie-notice .button',
                    '[aria-label="Close"]', '.modal-close',
                ]:
                    try:
                        btns = await page.query_selector_all(selector)
                        for btn in btns[:2]:
                            if await btn.is_visible():
                                await btn.click()
                                await page.wait_for_timeout(300)
                    except:
                        pass

                # --- Overview screenshot ---
                content_area = await page.query_selector('.entry-content, .post-content, article, main')
                captured_overview = False

                if content_area:
                    # Try to find the first significant image in content
                    images = await content_area.query_selector_all('img')
                    for img in images:
                        try:
                            box = await img.bounding_box()
                            if box and box['width'] > 300 and box['height'] > 150:
                                await img.screenshot(path=str(out_dir / 'overview.png'))
                                captured_overview = True
                                print(f'  ✅ overview.png (content image)')
                                break
                        except:
                            continue

                    if not captured_overview:
                        # Viewport screenshot of the content area
                        try:
                            await content_area.screenshot(
                                path=str(out_dir / 'overview.png'),
                                clip={'x': 0, 'y': 0, 'width': 1280, 'height': 800}
                            )
                            captured_overview = True
                            print(f'  ✅ overview.png (content area)')
                        except:
                            pass

                if not captured_overview:
                    await page.screenshot(path=str(out_dir / 'overview.png'))
                    print(f'  ✅ overview.png (viewport)')
                    captured_overview = True

                # --- Settings panel images ---
                all_images = await page.query_selector_all('img')
                for img in all_images:
                    try:
                        alt = (await img.get_attribute('alt') or '').lower()
                        src = (await img.get_attribute('src') or '').lower()
                        box = await img.bounding_box()

                        if not box or box['width'] < 200:
                            continue

                        combined = alt + ' ' + src
                        if any(kw in combined for kw in ['content tab', 'content settings']):
                            await img.screenshot(path=str(out_dir / 'settings-content.png'))
                            print(f'  ✅ settings-content.png')
                        elif any(kw in combined for kw in ['design tab', 'design settings']):
                            await img.screenshot(path=str(out_dir / 'settings-design.png'))
                            print(f'  ✅ settings-design.png')
                    except:
                        continue

                captured_count += 1
                await page.close()

                # Rate limiting
                await asyncio.sleep(2)

            except Exception as e:
                print(f'  ❌ Error: {e}')
                error_count += 1
                try:
                    await page.close()
                except:
                    pass

        await browser.close()

    print(f'\n=== CAPTURE COMPLETE ===')
    print(f'Captured: {captured_count}')
    print(f'Errors: {error_count}')

    # --- Post-process: optimize all screenshots ---
    print('\nOptimizing screenshots...')
    optimized = 0
    for png in SCREENSHOTS_DIR.rglob('*.png'):
        if png.name == '.gitkeep':
            continue
        if png.stat().st_size < 100:
            continue
        try:
            img = Image.open(png)
            if img.width > 2400:
                ratio = 2400 / img.width
                img = img.resize((2400, int(img.height * ratio)), Image.LANCZOS)
            img.save(png, 'PNG', optimize=True)
            size_kb = os.path.getsize(png) / 1024
            optimized += 1
        except Exception as e:
            print(f'  Warning: Could not optimize {png}: {e}')

    print(f'Optimized {optimized} images')


if __name__ == '__main__':
    asyncio.run(capture_module_screenshots())
