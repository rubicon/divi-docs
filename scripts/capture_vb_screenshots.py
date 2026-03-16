#!/usr/bin/env python3
"""
Capture Visual Builder settings panel screenshots from the Divi 5 Visual Builder.

Logs into WordPress at $DIVI_SITE_URL, opens the Visual Builder, and for each module:
  1. Opens the module settings panel
  2. Captures screenshots of the Content, Design, and Advanced tabs
  3. Saves optimized PNGs to docs/assets/screenshots/modules/{slug}/

Environment variables required:
  DIVI_SITE_URL  — e.g. https://www.16wells.dev
  DIVI_WP_USER   — WordPress admin username
  DIVI_WP_PASS   — WordPress admin password

Usage:
  python scripts/capture_vb_screenshots.py                    # All modules
  python scripts/capture_vb_screenshots.py --modules blurb,text
  python scripts/capture_vb_screenshots.py --debug            # Save debug screenshots
  python scripts/capture_vb_screenshots.py --skip-existing    # Skip modules with existing screenshots
"""

import argparse
import asyncio
import os
import sys
from pathlib import Path

from PIL import Image
from playwright.async_api import async_playwright

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCREENSHOTS_DIR = Path("docs/assets/screenshots/modules")

# Map from doc slug → Divi module slug used in the VB module picker.
# The VB module picker uses internal slugs like "et_pb_accordion".
MODULE_VB_SLUGS = {
    "accordion": "et_pb_accordion",
    "audio": "et_pb_audio",
    "bar-counter": "et_pb_counters",
    "blog": "et_pb_blog",
    "blurb": "et_pb_blurb",
    "button": "et_pb_button",
    "call-to-action": "et_pb_cta",
    "circle-counter": "et_pb_circle_counter",
    "code": "et_pb_code",
    "comments": "et_pb_comments",
    "contact-form": "et_pb_contact_form",
    "countdown-timer": "et_pb_countdown_timer",
    "divider": "et_pb_divider",
    "email-optin": "et_pb_signup",
    "filterable-portfolio": "et_pb_filterable_portfolio",
    "fullwidth-header": "et_pb_fullwidth_header",
    "fullwidth-map": "et_pb_fullwidth_map",
    "fullwidth-menu": "et_pb_fullwidth_menu",
    "fullwidth-portfolio": "et_pb_fullwidth_portfolio",
    "fullwidth-slider": "et_pb_fullwidth_slider",
    "gallery": "et_pb_gallery",
    "group": "et_pb_group",
    "group-carousel": "et_pb_group_carousel",
    "heading": "et_pb_heading",
    "hero": "et_pb_hero",
    "icon": "et_pb_icon",
    "icon-list": "et_pb_icon_list",
    "image": "et_pb_image",
    "login": "et_pb_login",
    "lottie": "et_pb_lottie",
    "map": "et_pb_map",
    "menu": "et_pb_menu",
    "number-counter": "et_pb_number_counter",
    "pagination": "et_pb_pagination",
    "person": "et_pb_team_member",
    "portfolio": "et_pb_portfolio",
    "post-navigation": "et_pb_post_nav",
    "post-slider": "et_pb_post_slider",
    "post-title": "et_pb_post_title",
    "pricing-table": "et_pb_pricing_tables",
    "search": "et_pb_search",
    "shop": "et_pb_shop",
    "sidebar": "et_pb_sidebar",
    "slider": "et_pb_slider",
    "social-media-follow": "et_pb_social_media_follow",
    "tabs": "et_pb_tabs",
    "testimonial": "et_pb_testimonial",
    "text": "et_pb_text",
    "toggle": "et_pb_toggle",
    "video": "et_pb_video",
    "video-slider": "et_pb_video_slider",
}

# Display name for search in the module picker
MODULE_DISPLAY_NAMES = {
    "accordion": "Accordion",
    "audio": "Audio",
    "bar-counter": "Bar Counters",
    "blog": "Blog",
    "blurb": "Blurb",
    "button": "Button",
    "call-to-action": "Call To Action",
    "circle-counter": "Circle Counter",
    "code": "Code",
    "comments": "Comments",
    "contact-form": "Contact Form",
    "countdown-timer": "Countdown Timer",
    "divider": "Divider",
    "email-optin": "Email Optin",
    "filterable-portfolio": "Filterable Portfolio",
    "fullwidth-header": "Fullwidth Header",
    "fullwidth-map": "Fullwidth Map",
    "fullwidth-menu": "Fullwidth Menu",
    "fullwidth-portfolio": "Fullwidth Portfolio",
    "fullwidth-slider": "Fullwidth Slider",
    "gallery": "Gallery",
    "group": "Group",
    "group-carousel": "Group Carousel",
    "heading": "Heading",
    "hero": "Hero",
    "icon": "Icon",
    "icon-list": "Icon List",
    "image": "Image",
    "login": "Login",
    "lottie": "Lottie",
    "map": "Map",
    "menu": "Menu",
    "number-counter": "Number Counter",
    "pagination": "Pagination",
    "person": "Person",
    "portfolio": "Portfolio",
    "post-navigation": "Post Navigation",
    "post-slider": "Post Slider",
    "post-title": "Post Title",
    "pricing-table": "Pricing Tables",
    "search": "Search",
    "shop": "Shop",
    "sidebar": "Sidebar",
    "slider": "Slider",
    "social-media-follow": "Social Media Follow",
    "tabs": "Tabs",
    "testimonial": "Testimonial",
    "text": "Text",
    "toggle": "Toggle",
    "video": "Video",
    "video-slider": "Video Slider",
}

# ---------------------------------------------------------------------------
# Selectors — these are best guesses for Divi 5 VB and WILL need adjustment.
# The script logs every selector it tries and takes debug screenshots on failure.
# ---------------------------------------------------------------------------

# Selectors to try for different VB UI elements (tried in order)
SELECTORS = {
    # The VB top bar / builder chrome that indicates the builder is loaded
    "builder_loaded": [
        ".et-fb-page-settings-bar",
        "#et-fb-app",
        ".et-fb-root-ancestor",
        "[data-et-fb]",
        ".et_fb_desktop_mode",
    ],
    # Settings panel container
    "settings_panel": [
        ".et-fb-settings-panel",
        ".et-fb-panel--settings",
        ".et-fb-option-container",
        "[class*='settings-panel']",
        "[class*='SettingsPanel']",
    ],
    # Tab buttons within the settings panel
    "tab_content": [
        ".et-fb-settings-tab-content",
        "[data-tab='content']",
        "button:has-text('Content')",
        ".et-fb-tabs button:first-child",
    ],
    "tab_design": [
        ".et-fb-settings-tab-design",
        "[data-tab='design']",
        "button:has-text('Design')",
        ".et-fb-tabs button:nth-child(2)",
    ],
    "tab_advanced": [
        ".et-fb-settings-tab-advanced",
        "[data-tab='advanced']",
        "button:has-text('Advanced')",
        ".et-fb-tabs button:nth-child(3)",
    ],
    # Add module button (the "+" button in a row)
    "add_module": [
        ".et-fb-button--add-module",
        ".et-fb-insert-module",
        "[class*='add-module']",
        "[class*='insert-module']",
    ],
    # Module search input in the module picker
    "module_search": [
        ".et-fb-module-search input",
        ".et-fb-modules-list input[type='search']",
        "[class*='module-search'] input",
        "input[placeholder*='Search']",
    ],
    # Close button for settings panel
    "close_settings": [
        ".et-fb-settings-panel .et-fb-close",
        ".et-fb-panel--settings .et-fb-close",
        "[class*='settings'] [class*='close']",
        ".et-fb-settings-heading button",
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def optimize_image(filepath: str, max_width: int = 1200) -> None:
    """Resize to max_width and optimize PNG."""
    try:
        img = Image.open(filepath)
        if img.width > max_width:
            ratio = max_width / img.width
            new_size = (max_width, int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)
        img.save(filepath, "PNG", optimize=True)
    except Exception as e:
        print(f"    Warning: Could not optimize {filepath}: {e}")


async def try_selectors(page, selector_list: list[str], action: str = "locate",
                        timeout: int = 5000, debug: bool = False) -> object | None:
    """Try a list of selectors in order, return the first match or None."""
    for sel in selector_list:
        try:
            if debug:
                print(f"    Trying selector: {sel}")
            locator = page.locator(sel).first
            await locator.wait_for(state="visible", timeout=timeout)
            if debug:
                print(f"    ✓ Found: {sel}")
            return locator
        except Exception:
            continue
    return None


async def debug_screenshot(page, name: str, debug_dir: Path) -> None:
    """Save a full-page debug screenshot."""
    debug_dir.mkdir(parents=True, exist_ok=True)
    path = debug_dir / f"debug-{name}.png"
    await page.screenshot(path=str(path), full_page=False)
    print(f"    📸 Debug screenshot: {path}")


# ---------------------------------------------------------------------------
# Core capture logic
# ---------------------------------------------------------------------------

async def login_to_wordpress(page, site_url: str, username: str, password: str,
                             debug: bool = False, debug_dir: Path | None = None) -> bool:
    """Log into WordPress. Returns True on success."""
    print("Logging into WordPress...")
    try:
        await page.goto(f"{site_url}/wp-login.php", wait_until="networkidle", timeout=30000)
        await page.fill("#user_login", username)
        await page.fill("#user_pass", password)
        await page.click("#wp-submit")
        await page.wait_for_url("**/wp-admin/**", timeout=15000)
        print("  ✅ Logged in successfully")
        return True
    except Exception as e:
        print(f"  ❌ Login failed: {e}")
        if debug and debug_dir:
            await debug_screenshot(page, "login-failed", debug_dir)
        return False


async def wait_for_vb(page, debug: bool = False, debug_dir: Path | None = None) -> bool:
    """Wait for the Visual Builder to fully load. Returns True on success."""
    print("  Waiting for Visual Builder to load...")
    loaded = await try_selectors(page, SELECTORS["builder_loaded"], timeout=45000, debug=debug)
    if loaded:
        # Give it extra time for React to finish rendering
        await page.wait_for_timeout(3000)
        print("  ✅ Visual Builder loaded")
        return True
    else:
        print("  ❌ Visual Builder did not load")
        if debug and debug_dir:
            await debug_screenshot(page, "vb-not-loaded", debug_dir)
        return False


async def open_module_settings(page, slug: str, debug: bool = False,
                               debug_dir: Path | None = None) -> bool:
    """
    Open the settings panel for a module. Tries two approaches:
    1. Click on an existing module instance on the page
    2. Use the module picker to add a new instance

    Returns True if settings panel is open.
    """
    vb_slug = MODULE_VB_SLUGS.get(slug, f"et_pb_{slug.replace('-', '_')}")
    display_name = MODULE_DISPLAY_NAMES.get(slug, slug.replace("-", " ").title())

    # Approach 1: Try clicking an existing module on the page
    # Divi 5 modules in VB often have data attributes or class names
    existing_selectors = [
        f"[data-type='{vb_slug}']",
        f".{vb_slug}",
        f"[class*='{vb_slug}']",
    ]

    for sel in existing_selectors:
        try:
            if debug:
                print(f"    Trying to click existing module: {sel}")
            el = page.locator(sel).first
            await el.wait_for(state="visible", timeout=3000)
            await el.dblclick()
            await page.wait_for_timeout(1000)

            # Check if settings panel opened
            panel = await try_selectors(page, SELECTORS["settings_panel"], timeout=5000, debug=debug)
            if panel:
                print(f"    ✓ Opened existing {slug} module settings")
                return True
        except Exception:
            continue

    # Approach 2: Use the module picker to add a new instance
    print(f"    No existing instance found, trying module picker...")

    # Find and click the add-module button
    add_btn = await try_selectors(page, SELECTORS["add_module"], timeout=5000, debug=debug)
    if not add_btn:
        print(f"    ❌ Could not find add-module button")
        if debug and debug_dir:
            await debug_screenshot(page, f"{slug}-no-add-btn", debug_dir)
        return False

    await add_btn.click()
    await page.wait_for_timeout(1000)

    # Search for the module
    search_input = await try_selectors(page, SELECTORS["module_search"], timeout=5000, debug=debug)
    if not search_input:
        print(f"    ❌ Could not find module search input")
        if debug and debug_dir:
            await debug_screenshot(page, f"{slug}-no-search", debug_dir)
        return False

    await search_input.fill(display_name)
    await page.wait_for_timeout(1000)

    # Click the module in search results
    module_item_selectors = [
        f"[data-slug='{vb_slug}']",
        f".et-fb-module-item:has-text('{display_name}')",
        f"[class*='module-item']:has-text('{display_name}')",
        f"li:has-text('{display_name}')",
    ]

    for sel in module_item_selectors:
        try:
            if debug:
                print(f"    Trying module item selector: {sel}")
            item = page.locator(sel).first
            await item.wait_for(state="visible", timeout=3000)
            await item.click()
            await page.wait_for_timeout(1500)

            # Check if settings panel opened
            panel = await try_selectors(page, SELECTORS["settings_panel"], timeout=5000, debug=debug)
            if panel:
                print(f"    ✓ Added {slug} via module picker, settings open")
                return True
        except Exception:
            continue

    print(f"    ❌ Could not open settings for {slug}")
    if debug and debug_dir:
        await debug_screenshot(page, f"{slug}-failed-open", debug_dir)
    return False


async def capture_tab(page, slug: str, tab_name: str, tab_selectors: list[str],
                      out_dir: Path, debug: bool = False,
                      debug_dir: Path | None = None) -> bool:
    """Click a settings tab and capture the panel screenshot. Returns True on success."""
    filename = f"settings-{tab_name}.png"
    filepath = out_dir / filename

    # For content tab, it's usually already selected
    if tab_name != "content":
        tab_btn = await try_selectors(page, tab_selectors, timeout=5000, debug=debug)
        if not tab_btn:
            print(f"    ❌ Could not find {tab_name} tab button")
            if debug and debug_dir:
                await debug_screenshot(page, f"{slug}-no-{tab_name}-tab", debug_dir)
            return False
        await tab_btn.click()
        await page.wait_for_timeout(800)

    # Find the settings panel and screenshot it
    panel = await try_selectors(page, SELECTORS["settings_panel"], timeout=5000, debug=debug)
    if not panel:
        print(f"    ❌ Settings panel not visible for {tab_name} tab")
        if debug and debug_dir:
            await debug_screenshot(page, f"{slug}-no-panel-{tab_name}", debug_dir)
        return False

    await panel.screenshot(path=str(filepath))
    optimize_image(str(filepath))
    size_kb = os.path.getsize(filepath) / 1024
    print(f"    ✅ {filename} ({size_kb:.0f} KB)")
    return True


async def close_settings(page, debug: bool = False) -> None:
    """Close the settings panel."""
    close_btn = await try_selectors(page, SELECTORS["close_settings"], timeout=3000, debug=debug)
    if close_btn:
        await close_btn.click()
        await page.wait_for_timeout(500)
    else:
        # Try pressing Escape as fallback
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(500)


async def capture_module(page, slug: str, skip_existing: bool = False,
                         debug: bool = False, debug_dir: Path | None = None) -> dict:
    """
    Capture all three tab screenshots for a single module.
    Returns dict with results: {"content": bool, "design": bool, "advanced": bool}
    """
    out_dir = SCREENSHOTS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    results = {"content": False, "design": False, "advanced": False}

    # Check if all screenshots already exist
    if skip_existing:
        all_exist = all(
            (out_dir / f"settings-{tab}.png").exists()
            and (out_dir / f"settings-{tab}.png").stat().st_size > 1024
            for tab in results
        )
        if all_exist:
            print(f"  ⏭ {slug} (all settings screenshots exist)")
            return {"content": True, "design": True, "advanced": True}

    # Open settings panel
    if not await open_module_settings(page, slug, debug=debug, debug_dir=debug_dir):
        return results

    # Capture each tab
    tabs = [
        ("content", SELECTORS["tab_content"]),
        ("design", SELECTORS["tab_design"]),
        ("advanced", SELECTORS["tab_advanced"]),
    ]

    for tab_name, tab_selectors in tabs:
        # Skip if this specific screenshot already exists
        if skip_existing:
            existing = out_dir / f"settings-{tab_name}.png"
            if existing.exists() and existing.stat().st_size > 1024:
                print(f"    ⏭ settings-{tab_name}.png (exists)")
                results[tab_name] = True
                continue

        results[tab_name] = await capture_tab(
            page, slug, tab_name, tab_selectors, out_dir,
            debug=debug, debug_dir=debug_dir,
        )

    # Close settings panel before moving to next module
    await close_settings(page, debug=debug)
    await page.wait_for_timeout(500)

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main(modules: list[str] | None = None, skip_existing: bool = False,
               debug: bool = False, page_path: str = "/sample-page/") -> None:
    """Main capture routine."""
    site_url = os.environ.get("DIVI_SITE_URL", "").rstrip("/")
    wp_user = os.environ.get("DIVI_WP_USER", "")
    wp_pass = os.environ.get("DIVI_WP_PASS", "")

    if not all([site_url, wp_user, wp_pass]):
        print("ERROR: Set environment variables before running:")
        print("  export DIVI_SITE_URL='https://www.16wells.dev'")
        print("  export DIVI_WP_USER='your-username'")
        print("  export DIVI_WP_PASS='your-password'")
        sys.exit(1)

    # Determine which modules to process
    if modules:
        slugs = modules
    else:
        # All modules with doc pages
        docs_dir = Path("docs/modules")
        slugs = sorted(
            f.stem for f in docs_dir.glob("*.md")
            if f.name != "index.md"
        )

    debug_dir = Path("docs/assets/screenshots/debug") if debug else None
    if debug and debug_dir:
        debug_dir.mkdir(parents=True, exist_ok=True)

    print(f"Capturing VB settings screenshots for {len(slugs)} modules")
    print(f"Site: {site_url}")
    print(f"Skip existing: {skip_existing}")
    print(f"Debug mode: {debug}")
    print()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=2,
        )
        page = await context.new_page()

        # Step 1: Log into WordPress
        if not await login_to_wordpress(page, site_url, wp_user, wp_pass,
                                        debug=debug, debug_dir=debug_dir):
            await browser.close()
            sys.exit(1)

        # Step 2: Navigate to a page with VB enabled
        vb_url = f"{site_url}{page_path}?et_fb=1"
        print(f"\nOpening Visual Builder at {vb_url}")
        try:
            await page.goto(vb_url, wait_until="load", timeout=60000)
        except Exception as e:
            print(f"  ❌ Failed to navigate to VB page: {e}")
            if debug and debug_dir:
                await debug_screenshot(page, "vb-navigate-failed", debug_dir)
            await browser.close()
            sys.exit(1)

        if not await wait_for_vb(page, debug=debug, debug_dir=debug_dir):
            await browser.close()
            sys.exit(1)

        # Step 3: Capture each module
        report = {"captured": [], "partial": [], "failed": []}

        for i, slug in enumerate(slugs, 1):
            print(f"\n[{i}/{len(slugs)}] {slug}")

            try:
                results = await capture_module(
                    page, slug,
                    skip_existing=skip_existing,
                    debug=debug,
                    debug_dir=debug_dir,
                )

                success_count = sum(results.values())
                if success_count == 3:
                    report["captured"].append(slug)
                elif success_count > 0:
                    report["partial"].append((slug, results))
                else:
                    report["failed"].append(slug)

            except Exception as e:
                print(f"  ❌ Unexpected error: {e}")
                report["failed"].append(slug)
                if debug and debug_dir:
                    await debug_screenshot(page, f"{slug}-crash", debug_dir)

        await browser.close()

    # Print report
    print("\n" + "=" * 60)
    print("CAPTURE REPORT")
    print("=" * 60)
    print(f"\n✅ Fully captured: {len(report['captured'])}")
    for slug in report["captured"]:
        print(f"   {slug}")

    if report["partial"]:
        print(f"\n⚠ Partially captured: {len(report['partial'])}")
        for slug, results in report["partial"]:
            tabs = ", ".join(t for t, ok in results.items() if ok)
            print(f"   {slug} (got: {tabs})")

    print(f"\n❌ Failed: {len(report['failed'])}")
    for slug in report["failed"]:
        print(f"   {slug}")

    total = len(slugs)
    full = len(report["captured"])
    print(f"\nTotal: {full}/{total} fully captured")

    # Save report to file
    report_path = Path("reports/vb-screenshot-report.txt")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w") as f:
        f.write(f"VB Screenshot Capture Report\n")
        f.write(f"{'=' * 40}\n\n")
        f.write(f"Fully captured ({len(report['captured'])}):\n")
        for slug in report["captured"]:
            f.write(f"  {slug}\n")
        f.write(f"\nPartially captured ({len(report['partial'])}):\n")
        for slug, results in report["partial"]:
            tabs = ", ".join(t for t, ok in results.items() if ok)
            f.write(f"  {slug} (got: {tabs})\n")
        f.write(f"\nFailed ({len(report['failed'])}):\n")
        for slug in report["failed"]:
            f.write(f"  {slug}\n")
        f.write(f"\nTotal: {full}/{total} fully captured\n")
    print(f"\nReport saved to {report_path}")


def parse_args():
    parser = argparse.ArgumentParser(description="Capture VB settings panel screenshots")
    parser.add_argument(
        "--modules", type=str, default=None,
        help="Comma-separated list of module slugs to capture (default: all)",
    )
    parser.add_argument(
        "--skip-existing", action="store_true",
        help="Skip modules that already have settings screenshots",
    )
    parser.add_argument(
        "--debug", action="store_true",
        help="Save debug screenshots at each step for troubleshooting",
    )
    parser.add_argument(
        "--page", type=str, default="/sample-page/",
        help="Page path to open in the VB (default: /sample-page/)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    module_list = args.modules.split(",") if args.modules else None
    asyncio.run(main(
        modules=module_list,
        skip_existing=args.skip_existing,
        debug=args.debug,
        page_path=args.page,
    ))
