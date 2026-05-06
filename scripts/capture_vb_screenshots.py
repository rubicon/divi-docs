#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Capture Visual Builder settings panel screenshots from 16wells.dev.

Logs into WordPress, opens each module's demo page in the Visual Builder,
clicks through Content/Design/Advanced tabs, and captures the settings panel.

Usage:
    python3 scripts/capture_vb_screenshots.py                  # All modules
    python3 scripts/capture_vb_screenshots.py --module blurb   # One module
    python3 scripts/capture_vb_screenshots.py --discover        # Debug VB selectors
    python3 scripts/capture_vb_screenshots.py --debug           # Extra debug screenshots

Prerequisites:
    - .env file with DIVI_SITE_URL, DIVI_WP_USER, DIVI_WP_PASS
    - pip install playwright Pillow python-dotenv
    - playwright install chromium
"""

import argparse
import os
import re
import sys
import time
from pathlib import Path

try:
    from dotenv import load_dotenv
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    from PIL import Image
except ImportError:
    print("Install dependencies: pip install playwright Pillow python-dotenv")
    print("Then: playwright install chromium")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

load_dotenv()

SITE_URL = os.getenv("DIVI_SITE_URL", "https://www.16wells.dev")
WP_USER = os.getenv("DIVI_WP_USER", "")
WP_PASS = os.getenv("DIVI_WP_PASS", "")

SCREENSHOT_DIR = Path("docs/assets/screenshots/modules")
DEBUG_DIR = Path("debug-screenshots")
MAX_WIDTH = 1200

# Selectors - discovered via --discover on 2026-03-16
VB_SELECTORS = {
    # Indicates VB has fully loaded
    "vb_ready": "#et-fb-app",
    # The settings panel container (right sidebar modal)
    "settings_panel": ".et-vb-modal-panel",
    # The full right sidebar
    "sidebar": ".et-vb-sidebar--right",
    # Tab buttons within the settings panel
    "tab_content": "button.et-vb-modal-tab:has-text('Content')",
    "tab_design": "button.et-vb-modal-tab:has-text('Design')",
    "tab_advanced": "button.et-vb-modal-tab:has-text('Advanced')",
    # Tabs container
    "tabs_container": ".et-vb-modal-tabs",
    # Module element on the page
    "module_element": "[class*='et_pb_'], [class*='divi_'], [data-type]",
    # Close button for settings panel
    "close_panel": "button[aria-label='Close']",
}

# Modules with demo pages at /module-demos/{slug}/
DEMO_MODULES = [
    "accordion", "audio", "bar-counter", "blog", "blurb", "button",
    "call-to-action", "circle-counter", "code", "comments", "contact-form",
    "countdown-timer", "divider", "email-optin", "filterable-portfolio",
    "fullwidth-header", "fullwidth-map", "fullwidth-menu", "fullwidth-portfolio",
    "fullwidth-slider", "gallery", "icon", "image", "login", "map", "menu",
    "number-counter", "person", "portfolio", "post-navigation", "post-slider",
    "post-title", "pricing-table", "search", "shop", "sidebar", "slider",
    "social-media-follow", "tabs", "testimonial", "text", "toggle", "video",
    "video-slider",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def optimize_image(path: Path, max_width: int = MAX_WIDTH):
    """Resize image to max width and optimize PNG."""
    try:
        img = Image.open(path)
        if img.width > max_width:
            ratio = max_width / img.width
            new_size = (max_width, int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)
        img.save(path, "PNG", optimize=True)
    except Exception as e:
        print(f"    Warning: Could not optimize {path}: {e}")


def ensure_dir(path: Path):
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def login_to_wordpress(page):
    """Log into WordPress admin."""
    login_url = f"{SITE_URL}/wp-login.php"
    print(f"  Logging into {login_url}...")

    page.goto(login_url, wait_until="networkidle", timeout=30000)
    time.sleep(1)

    page.fill("#user_login", WP_USER)
    page.fill("#user_pass", WP_PASS)
    page.click("#wp-submit")

    # Wait for redirect to dashboard
    page.wait_for_url("**/wp-admin/**", timeout=30000)
    print("  Logged in successfully.")


def wait_for_vb(page, timeout: int = 120000):
    """Wait for the Visual Builder to fully load.

    If the VB doesn't auto-launch, tries clicking 'Edit With Divi' in the
    admin bar as a fallback.
    """
    try:
        page.wait_for_selector(VB_SELECTORS["vb_ready"], timeout=timeout)
    except PlaywrightTimeout:
        # VB didn't auto-launch — try clicking "Edit With Divi" in admin bar
        print("    VB not auto-launched, clicking Edit With Divi...")
        try:
            # Look for the admin bar link
            edit_link = page.query_selector(
                "a:has-text('Edit With Divi'), "
                "a:has-text('Enable Visual Builder'), "
                "#wp-admin-bar-et-use-visual-builder a, "
                "#wp-admin-bar-et_fb_admin_bar_toggle a"
            )
            if edit_link:
                edit_link.click()
                page.wait_for_selector(VB_SELECTORS["vb_ready"], timeout=timeout)
            else:
                print("    Warning: Could not find Edit With Divi link")
                return False
        except PlaywrightTimeout:
            print("    Warning: VB did not load after clicking Edit With Divi")
            return False

    # Wait for the modal tabs to appear (indicates VB is interactive)
    try:
        page.wait_for_selector(VB_SELECTORS["tabs_container"], timeout=15000)
    except PlaywrightTimeout:
        pass  # Tabs may not be visible until a module is clicked

    # Extra wait for React to render
    time.sleep(5)
    print("    VB ready")
    return True


def find_and_click_module(page, slug: str, debug: bool = False):
    """Find the first module instance on the page and click to open settings."""
    # Give VB time to render modules
    time.sleep(3)

    if debug:
        ensure_dir(DEBUG_DIR)
        page.screenshot(path=str(DEBUG_DIR / f"{slug}-before-click.png"), full_page=True)

    # Try clicking the module element on canvas
    try:
        module_selectors = [
            f".et_pb_{slug.replace('-', '_')}",
            f"[class*='{slug.replace('-', '_')}']",
            ".et_pb_module",
            ".et_pb_section .et_pb_row .et_pb_column > div",
        ]

        for selector in module_selectors:
            elements = page.query_selector_all(selector)
            if elements:
                elements[0].click(force=True)
                print(f"    Clicked module (selector: {selector})")
                time.sleep(2)

                if debug:
                    page.screenshot(path=str(DEBUG_DIR / f"{slug}-after-click.png"), full_page=True)
                return True

    except Exception as e:
        print(f"    Warning: Click failed: {e}")

    # Fallback: try double-clicking anywhere in the content area
    try:
        content_area = page.query_selector(".et-fb-page-content, .et_builder_inner_content, #et-fb-app")
        if content_area:
            content_area.dblclick()
            time.sleep(2)
            return True
    except Exception:
        pass

    return False


def capture_settings_tab(page, tab_selector: str, output_path: Path, debug: bool = False):
    """Click a settings tab and capture the panel."""
    # Click the tab using Playwright's built-in selector engine
    try:
        page.click(tab_selector, timeout=5000)
        time.sleep(1.5)
    except Exception as e:
        print(f"    Warning: Could not click tab ({tab_selector}): {e}")

    # Try to capture the settings panel
    try:
        panel = page.query_selector(VB_SELECTORS["settings_panel"])
        if panel:
            panel.screenshot(path=str(output_path))
            optimize_image(output_path)
            return True
    except Exception:
        pass

    # Fallback: capture the right sidebar
    try:
        sidebar = page.query_selector(VB_SELECTORS["sidebar"])
        if sidebar:
            sidebar.screenshot(path=str(output_path))
            optimize_image(output_path)
            return True
    except Exception:
        pass

    # Last fallback: clip the right portion of viewport
    try:
        page.screenshot(path=str(output_path), clip={
            "x": 1100, "y": 0, "width": 340, "height": 900
        })
        optimize_image(output_path)
        return True
    except Exception as e:
        print(f"    Warning: Could not capture tab: {e}")
        return False


# ---------------------------------------------------------------------------
# Main capture functions
# ---------------------------------------------------------------------------

def discover_vb(page, slug: str = "accordion"):
    """Discovery mode: log into VB, dump DOM info, take debug screenshots."""
    ensure_dir(DEBUG_DIR)

    demo_url = f"{SITE_URL}/module-demos/{slug}/?et_fb=1&PageSpeed=off"
    print(f"\n  Navigating to: {demo_url}")
    page.goto(demo_url, wait_until="domcontentloaded", timeout=60000)

    print("  Waiting for VB to load...")
    wait_for_vb(page, timeout=90000)
    time.sleep(5)

    # Full page screenshot
    page.screenshot(path=str(DEBUG_DIR / "discover-full.png"), full_page=True)
    print(f"  Saved: {DEBUG_DIR}/discover-full.png")

    # Viewport screenshot
    page.screenshot(path=str(DEBUG_DIR / "discover-viewport.png"))
    print(f"  Saved: {DEBUG_DIR}/discover-viewport.png")

    # Dump relevant DOM structure
    print("\n  === DOM Discovery ===")

    discovery_selectors = [
        "[class*='settings']",
        "[class*='panel']",
        "[class*='modal']",
        "[class*='sidebar']",
        "[data-tab]",
        "[role='tab']",
        "[class*='tab']",
        "[class*='et_pb_']",
        "[class*='divi_']",
        "#et-fb-app",
        "[id*='et-fb']",
    ]

    for selector in discovery_selectors:
        try:
            elements = page.query_selector_all(selector)
            if elements and len(elements) < 20:
                print(f"\n  Selector: {selector} ({len(elements)} matches)")
                for i, el in enumerate(elements[:5]):
                    tag = el.evaluate("e => e.tagName")
                    classes = el.evaluate("e => e.className")
                    el_id = el.evaluate("e => e.id")
                    text = el.evaluate("e => e.textContent?.substring(0, 50)")
                    print(f"    [{i}] <{tag}> id='{el_id}' class='{str(classes)[:80]}' text='{text}'")
            elif elements:
                print(f"\n  Selector: {selector} ({len(elements)} matches - too many to list)")
        except Exception:
            pass

    # Try clicking the first module to open settings
    print("\n  === Attempting to open module settings ===")
    find_and_click_module(page, slug, debug=True)
    time.sleep(3)

    # Take screenshot after click
    page.screenshot(path=str(DEBUG_DIR / "discover-after-click.png"), full_page=True)
    print(f"  Saved: {DEBUG_DIR}/discover-after-click.png")

    # Look for settings panel now
    for selector in ["[class*='settings']", "[class*='panel']", "[class*='modal']"]:
        try:
            elements = page.query_selector_all(selector)
            if elements:
                print(f"\n  After click - {selector}: {len(elements)} matches")
                for i, el in enumerate(elements[:5]):
                    tag = el.evaluate("e => e.tagName")
                    classes = el.evaluate("e => e.className")
                    visible = el.evaluate("e => e.offsetParent !== null")
                    bbox = el.bounding_box()
                    print(f"    [{i}] <{tag}> class='{str(classes)[:80]}' visible={visible} bbox={bbox}")
        except Exception:
            pass

    print("\n  Discovery complete. Review debug-screenshots/ directory.")
    print("  Update VB_SELECTORS in the script based on what you find.")


def capture_module(page, slug: str, debug: bool = False, skip_existing: bool = True):
    """Capture Content/Design/Advanced tab screenshots for one module."""
    output_dir = SCREENSHOT_DIR / slug
    ensure_dir(output_dir)

    # Check if already captured
    if skip_existing:
        existing = [
            (output_dir / "settings-content.png").exists(),
            (output_dir / "settings-design.png").exists(),
            (output_dir / "settings-advanced.png").exists(),
        ]
        if all(existing):
            print(f"  [{slug}] All settings screenshots exist, skipping")
            return "skipped"

    demo_url = f"{SITE_URL}/module-demos/{slug}/?et_fb=1&PageSpeed=off"
    print(f"  [{slug}] Navigating to VB...")

    try:
        page.goto(demo_url, wait_until="domcontentloaded", timeout=60000)
    except PlaywrightTimeout:
        print(f"  [{slug}] FAILED: Page load timeout")
        return "failed"

    # Wait for VB — if it fails, try re-login and retry once
    if not wait_for_vb(page):
        if debug:
            ensure_dir(DEBUG_DIR)
            page.screenshot(path=str(DEBUG_DIR / f"{slug}-vb-initial-fail.png"))
        print(f"  [{slug}] VB failed to load, re-logging in...")
        try:
            login_to_wordpress(page)
            page.goto(demo_url, wait_until="domcontentloaded", timeout=60000)
            if not wait_for_vb(page):
                print(f"  [{slug}] FAILED: VB did not load after re-login")
                if debug:
                    ensure_dir(DEBUG_DIR)
                    page.screenshot(path=str(DEBUG_DIR / f"{slug}-vb-fail.png"))
                return "failed"
        except Exception as e:
            print(f"  [{slug}] FAILED: Re-login failed: {e}")
            return "failed"

    # Click module to open settings
    if not find_and_click_module(page, slug, debug=debug):
        print(f"  [{slug}] FAILED: Could not open module settings")
        if debug:
            ensure_dir(DEBUG_DIR)
            page.screenshot(path=str(DEBUG_DIR / f"{slug}-click-fail.png"))
        return "failed"

    # Capture each tab
    tabs = [
        ("Content", VB_SELECTORS["tab_content"], output_dir / "settings-content.png"),
        ("Design", VB_SELECTORS["tab_design"], output_dir / "settings-design.png"),
        ("Advanced", VB_SELECTORS["tab_advanced"], output_dir / "settings-advanced.png"),
    ]

    captured = 0
    for tab_name, tab_selector, output_path in tabs:
        print(f"    Capturing {tab_name} tab...")
        if capture_settings_tab(page, tab_selector, output_path, debug=debug):
            size = output_path.stat().st_size
            print(f"    Saved: {output_path} ({size:,} bytes)")
            captured += 1
        else:
            print(f"    FAILED: Could not capture {tab_name} tab")

    if captured == 3:
        return "captured"
    elif captured > 0:
        return "partial"
    else:
        return "failed"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Capture VB settings panel screenshots",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/capture_vb_screenshots.py --discover         Debug VB selectors
  python3 scripts/capture_vb_screenshots.py --module accordion Capture one module
  python3 scripts/capture_vb_screenshots.py                    Capture all modules
  python3 scripts/capture_vb_screenshots.py --debug            Extra debug output
        """,
    )
    parser.add_argument("--module", help="Capture one specific module by slug")
    parser.add_argument("--discover", action="store_true", help="Discovery mode: dump VB DOM info")
    parser.add_argument("--debug", action="store_true", help="Save extra debug screenshots")
    parser.add_argument("--skip-existing", action="store_true", default=True,
                        help="Skip modules with existing screenshots (default)")
    parser.add_argument("--force", action="store_true", help="Re-capture even if screenshots exist")

    args = parser.parse_args()

    if not WP_USER or not WP_PASS:
        print("Error: DIVI_WP_USER and DIVI_WP_PASS must be set in .env")
        sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=2,
        )
        page = context.new_page()

        # Log in
        try:
            login_to_wordpress(page)
        except Exception as e:
            print(f"Error: Login failed: {e}")
            browser.close()
            sys.exit(1)

        if args.discover:
            slug = args.module or "accordion"
            discover_vb(page, slug)
            browser.close()
            return

        # Determine which modules to capture
        if args.module:
            modules = [args.module]
        else:
            modules = DEMO_MODULES

        # Capture
        results = {"captured": 0, "partial": 0, "skipped": 0, "failed": 0}
        print(f"\nCapturing settings screenshots for {len(modules)} modules...\n")

        consecutive_failures = 0
        for i, slug in enumerate(modules, 1):
            print(f"[{i}/{len(modules)}] {slug}")

            # Preventive re-login every 10 modules
            if i > 1 and (i - 1) % 10 == 0:
                print("  (Preventive re-login)")
                try:
                    login_to_wordpress(page)
                except Exception:
                    pass

            # Re-login after 3 consecutive failures
            if consecutive_failures >= 3:
                print("  (Re-login after consecutive failures)")
                try:
                    login_to_wordpress(page)
                    consecutive_failures = 0
                except Exception:
                    pass

            try:
                result = capture_module(page, slug, debug=args.debug, skip_existing=not args.force)
                results[result] += 1
                if result == "failed":
                    consecutive_failures += 1
                else:
                    consecutive_failures = 0
            except Exception as e:
                print(f"  [{slug}] ERROR: {e}")
                results["failed"] += 1
                consecutive_failures += 1
                if args.debug:
                    ensure_dir(DEBUG_DIR)
                    try:
                        page.screenshot(path=str(DEBUG_DIR / f"{slug}-error.png"))
                    except Exception:
                        pass

        browser.close()

        # Summary
        print(f"\n=== Screenshot Capture Summary ===")
        print(f"  Captured (all 3 tabs): {results['captured']}")
        print(f"  Partial (some tabs):   {results['partial']}")
        print(f"  Skipped (existing):    {results['skipped']}")
        print(f"  Failed:                {results['failed']}")
        print(f"  Total:                 {sum(results.values())}")


if __name__ == "__main__":
    main()
