#!/usr/bin/env python3
"""
Capture screenshots from all module demo pages on 16wells.dev.
Saves both full-page and element-specific screenshots.
After capture, runs update_module_docs_screenshots.py to insert element
screenshots and demo links into the corresponding module docs.
"""

import asyncio
import os
import subprocess
import sys
from pathlib import Path

from playwright.async_api import async_playwright
from PIL import Image

BASE_URL = "https://www.16wells.dev/module-demos"
SCREENSHOTS_DIR = Path("docs/assets/screenshots/modules")

# Module slug -> CSS selector for the Divi module element
MODULE_SELECTORS = {
    "accordion": ".et_pb_accordion",
    "audio": ".et_pb_audio_module",
    "bar-counter": ".et_pb_bar_counters",
    "blog": ".et_pb_blog",
    "blurb": ".et_pb_blurb",
    "button": ".et_pb_button_module_wrapper",
    "call-to-action": ".et_pb_promo",
    "circle-counter": ".et_pb_circle_counter",
    "code": ".et_pb_code",
    "comments": ".et_pb_comments_module",
    "contact-form": ".et_pb_contact_form_container",
    "countdown-timer": ".et_pb_countdown_timer",
    "divider": ".et_pb_divider",
    "email-optin": ".et_pb_signup",
    "filterable-portfolio": ".et_pb_filterable_portfolio",
    "fullwidth-header": ".et_pb_fullwidth_header",
    "fullwidth-map": ".et_pb_map",
    "fullwidth-menu": ".et_pb_fullwidth_menu",
    "fullwidth-portfolio": ".et_pb_fullwidth_portfolio",
    "fullwidth-slider": ".et_pb_fullwidth_slider",
    "gallery": ".et_pb_gallery",
    "icon": ".et_pb_icon",
    "image": ".et_pb_image",
    "login": ".et_pb_login",
    "map": ".et_pb_map",
    "menu": ".et_pb_menu",
    "number-counter": ".et_pb_number_counter",
    "person": ".et_pb_team_member",
    "portfolio": ".et_pb_portfolio",
    "post-navigation": ".et_pb_post_nav",
    "post-slider": ".et_pb_slider",
    "post-title": ".et_pb_post_title",
    "pricing-table": ".et_pb_pricing",
    "search": ".et_pb_search",
    "shop": ".et_pb_shop",
    "sidebar": ".et_pb_widget_area",
    "slider": ".et_pb_slider",
    "social-media-follow": ".et_pb_social_media_follow",
    "tabs": ".et_pb_tabs",
    "testimonial": ".et_pb_testimonial",
    "text": ".et_pb_text",
    "toggle": ".et_pb_toggle",
    "video": ".et_pb_video",
    "video-slider": ".et_pb_video_slider",
}


def optimize_image(filepath, max_width=1200):
    """Resize and compress a screenshot for web use."""
    try:
        img = Image.open(filepath)
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.LANCZOS)
        img.save(filepath, 'PNG', optimize=True)
    except Exception as e:
        print(f"    Warning: Could not optimize {filepath}: {e}")


async def capture_all():
    slugs = sorted(MODULE_SELECTORS.keys())
    print(f"Capturing screenshots for {len(slugs)} modules...\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 800},
            device_scale_factor=2,
        )

        captured = 0
        failed = 0

        for i, slug in enumerate(slugs, 1):
            url = f"{BASE_URL}/{slug}/"
            out_dir = SCREENSHOTS_DIR / slug
            out_dir.mkdir(parents=True, exist_ok=True)

            print(f"[{i}/{len(slugs)}] {slug}")

            try:
                page = await context.new_page()
                resp = await page.goto(url, wait_until='load', timeout=60000)

                if resp and resp.status >= 400:
                    print(f"  ⚠ HTTP {resp.status} — skipping")
                    await page.close()
                    failed += 1
                    continue

                await page.wait_for_timeout(3000)

                # Dismiss cookie banners / popups
                for sel in [
                    '[class*="close"]', '[class*="dismiss"]',
                    '.cookie-notice .button', '[aria-label="Close"]',
                ]:
                    try:
                        btns = await page.query_selector_all(sel)
                        for btn in btns[:2]:
                            if await btn.is_visible():
                                await btn.click()
                                await page.wait_for_timeout(300)
                    except:
                        pass

                # Full page screenshot
                fp_path = str(out_dir / "overview.png")
                await page.screenshot(path=fp_path, full_page=True)
                optimize_image(fp_path)
                size_kb = os.path.getsize(fp_path) / 1024
                print(f"  ✅ overview.png ({size_kb:.0f} KB)")

                # Element-specific screenshot
                selector = MODULE_SELECTORS[slug]
                element = await page.query_selector(selector)
                if element:
                    box = await element.bounding_box()
                    if box and box['width'] > 10 and box['height'] > 10:
                        elem_path = str(out_dir / "element.png")
                        await element.screenshot(path=elem_path)
                        optimize_image(elem_path)
                        size_kb = os.path.getsize(elem_path) / 1024
                        print(f"  ✅ element.png ({size_kb:.0f} KB)")
                    else:
                        print(f"  ⚠ Element too small or hidden for {selector}")
                else:
                    # Try broader selector
                    section = await page.query_selector('.et_pb_section')
                    if section:
                        elem_path = str(out_dir / "element.png")
                        await section.screenshot(path=elem_path)
                        optimize_image(elem_path)
                        size_kb = os.path.getsize(elem_path) / 1024
                        print(f"  ✅ element.png (section fallback, {size_kb:.0f} KB)")
                    else:
                        print(f"  ⚠ No element found for {selector}")

                captured += 1
                await page.close()
                await asyncio.sleep(2)

            except Exception as e:
                print(f"  ❌ Error: {e}")
                failed += 1
                try:
                    await page.close()
                except:
                    pass

        await browser.close()

    print(f"\n{'='*50}")
    print(f"DONE: {captured} captured, {failed} failed")

    # Update module docs: insert element screenshots and link "View A Live Demo"
    script_dir = Path(__file__).resolve().parent
    update_script = script_dir / "update_module_docs_screenshots.py"
    if update_script.exists():
        print("\nUpdating module documentation with new screenshots and demo links...")
        subprocess.run([sys.executable, str(update_script)], cwd=script_dir.parent, check=False)


if __name__ == "__main__":
    asyncio.run(capture_all())
