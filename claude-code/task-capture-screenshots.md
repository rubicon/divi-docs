# Claude Code Task: Capture Module Screenshots from Elegant Themes

## Context

You are working on the `divi-docs` repo (https://github.com/16wells/divi-docs).
The module documentation pages are generated but have broken image placeholders because
no actual screenshot files exist yet. This task captures screenshots from Elegant Themes'
own documentation and demo pages to fill those gaps.

## Prerequisites

```bash
pip install playwright Pillow pyyaml requests beautifulsoup4
playwright install chromium
```

## Task

For every module that has a documentation page in `docs/modules/`, capture screenshots
from the corresponding Elegant Themes documentation page and save them to the correct
screenshot directory.

## Step-by-Step Instructions

### Step 1: Build the Module URL Map

Scan `docs/modules/` for all .md files (excluding index.md). For each one, extract the
`source_url` from the YAML frontmatter. This gives you the Elegant Themes URL to screenshot.

If a page doesn't have a `source_url`, construct one:
```
https://www.elegantthemes.com/documentation/divi/{module-slug}/
```

### Step 2: For Each Module, Capture These Screenshots

For each module, navigate to its Elegant Themes documentation page and capture:

**a) Overview screenshot (`overview.png`)**
- Navigate to the ET documentation page for the module
- Look for the first large image or demo screenshot on the page
- If the page has a hero/header image showing the module, capture that
- If no hero image, take a viewport screenshot of the top of the page content
- Target: what the module looks like in use on a real page

**b) Settings panel screenshots (if visible on the page)**
- Many ET doc pages show screenshots of the Divi settings panels
- Look for images on the page that show the Content tab, Design tab, or module settings
- If found, save as `settings-content.png`, `settings-design.png`
- If the ET page doesn't show settings panels (many don't), skip these — don't capture random content

**c) Front-end output screenshot (`frontend-default.png`)**
- If the ET page has a live demo or example of the module rendering, capture it
- Look for elements that show the module's default output

### Step 3: Screenshot Capture Approach

Use Playwright to navigate to each page and capture screenshots. Here's the approach:

```python
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image
import re, os, yaml

async def capture_module_screenshots():
    # Scan docs/modules/ for source URLs
    modules = []
    for md_file in Path('docs/modules').glob('*.md'):
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

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 800},
            device_scale_factor=2,  # Retina quality
        )

        for mod in modules:
            slug = mod['slug']
            url = mod['url']
            out_dir = f'docs/assets/screenshots/modules/{slug}'
            os.makedirs(out_dir, exist_ok=True)

            print(f'Capturing: {slug} from {url}')

            try:
                page = await context.new_page()
                await page.goto(url, wait_until='networkidle', timeout=30000)
                await page.wait_for_timeout(2000)  # Let lazy images load

                # Close any popups/modals that ET might show
                try:
                    close_btns = await page.query_selector_all('[class*="close"], [class*="dismiss"]')
                    for btn in close_btns[:3]:
                        await btn.click()
                        await page.wait_for_timeout(500)
                except:
                    pass

                # --- Overview screenshot ---
                # Try to find the main content image first
                content_area = await page.query_selector('.entry-content, .post-content, article')
                if content_area:
                    # Get the first significant image in the content
                    images = await content_area.query_selector_all('img')
                    captured_overview = False
                    for img in images:
                        box = await img.bounding_box()
                        if box and box['width'] > 300 and box['height'] > 150:
                            await img.screenshot(path=f'{out_dir}/overview.png')
                            captured_overview = True
                            print(f'  ✅ overview.png (from content image)')
                            break

                    if not captured_overview:
                        # Fall back to viewport screenshot of the content area
                        await content_area.screenshot(path=f'{out_dir}/overview.png')
                        print(f'  ✅ overview.png (content area)')
                else:
                    # Last resort: full viewport
                    await page.screenshot(path=f'{out_dir}/overview.png')
                    print(f'  ✅ overview.png (viewport)')

                # --- Find settings panel images on the page ---
                all_images = await page.query_selector_all('img')
                for img in all_images:
                    alt = (await img.get_attribute('alt') or '').lower()
                    src = (await img.get_attribute('src') or '').lower()
                    box = await img.bounding_box()

                    if not box or box['width'] < 200:
                        continue

                    # Look for images that show settings panels
                    if any(kw in alt + src for kw in ['content tab', 'settings', 'content settings',
                                                       'design tab', 'design settings']):
                        if 'content' in (alt + src):
                            await img.screenshot(path=f'{out_dir}/settings-content.png')
                            print(f'  ✅ settings-content.png')
                        elif 'design' in (alt + src):
                            await img.screenshot(path=f'{out_dir}/settings-design.png')
                            print(f'  ✅ settings-design.png')

                await page.close()

            except Exception as e:
                print(f'  ❌ Error: {e}')
                try:
                    await page.close()
                except:
                    pass

        await browser.close()

    # --- Post-process: optimize all captured screenshots ---
    for png in Path('docs/assets/screenshots/modules').rglob('*.png'):
        if png.name == '.gitkeep':
            continue
        try:
            img = Image.open(png)
            if img.width > 1200:
                ratio = 1200 / img.width
                img = img.resize((1200, int(img.height * ratio)), Image.LANCZOS)
            img.save(png, 'PNG', optimize=True)
            size_kb = os.path.getsize(png) / 1024
            print(f'  Optimized {png}: {size_kb:.0f}KB')
        except Exception as e:
            print(f'  Warning: Could not optimize {png}: {e}')

asyncio.run(capture_module_screenshots())
```

### Step 4: Handle Missing Screenshots

After the capture run, check which modules still don't have an overview.png.
For those modules:
1. Try alternative URLs:
   - `https://www.elegantthemes.com/documentation/divi/{slug}-module/`
   - `https://www.elegantthemes.com/documentation/divi/divi-{slug}/`
   - Search the ET site for the module name
2. If no ET page exists for a module, generate a simple placeholder image
   (solid color with the module name as text) so the page doesn't show broken images

### Step 5: Remove Broken Image References

After capturing all available screenshots, scan every module .md file. For any screenshot
reference that still points to a non-existent file, comment it out:

```python
# For each .md file in docs/modules/
# For each image reference like ![...](../assets/screenshots/...)
# Check if the referenced file exists
# If not, wrap it in an HTML comment: <!-- ![...](path) -->
# This keeps the reference for later but prevents broken images on the live site
```

This is critical — the live site should never show broken image icons.

### Step 6: Verify and Commit

```bash
# Count results
echo "Screenshots captured:"
find docs/assets/screenshots/modules -name '*.png' ! -name '.gitkeep' | wc -l

echo "Modules with screenshots:"
find docs/assets/screenshots/modules -name 'overview.png' | wc -l

# Build to verify
pip install mkdocs-material mkdocs-glightbox
mkdocs build

# Commit
git add docs/assets/screenshots/
git add docs/modules/  # For any commented-out image references
git commit -m "Add module screenshots from Elegant Themes documentation

- Captured overview screenshots for X modules
- Captured settings panel screenshots where available
- Commented out image references for modules without available screenshots
- All images optimized to max 1200px width at 2x retina quality"
git push
```

## Important Notes

- Be respectful of ET's servers — add a 2-3 second delay between page loads
- Elegant Themes may show cookie consent banners or popups — dismiss them before capturing
- Some ET documentation pages are behind a login wall — skip those modules and note them
- The goal is "good enough" screenshots that make the docs usable, not pixel-perfect captures
- If a module page at ET doesn't have good visual examples, a viewport screenshot of the documentation itself is fine — it still shows users what the module is about
- Always optimize images (max 1200px wide) to keep the site fast
- The critical step is Step 5 — no broken images should remain on the live site
