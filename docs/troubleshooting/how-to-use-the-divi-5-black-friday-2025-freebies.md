---
title: "How to Use the Divi 5 Black Friday 2025 Freebies"
category: troubleshooting
tags: [freebies, imports, layouts, presets, black friday]
related: ["divi-library-in-divi-5", "advanced-styling-using-option-group-presets-in-divi-5", "getting-started-with-divi-5-theme-builder"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12915434-how-to-use-the-divi-5-black-friday-2025-freebies"
---

# How to Use the Divi 5 Black Friday 2025 Freebies

A comprehensive guide to importing and using the Black Friday 2025 Divi 5 freebies, which include layouts, presets, Theme Builder templates, and a complete design system in JSON format.

## Overview

Elegant Themes released a set of premium Black Friday 2025 freebies for Divi 5, consisting of multiple JSON files that you can import into your site. These files contain:

- **Module Presets and Option Group Presets** — pre-configured design patterns for common elements
- **Global Variables** — a complete color, typography, and spacing system
- **Pre-built layouts** — over 40 section types with 430+ individual sections
- **Ready-made pages** — home pages and other full page layouts
- **Theme Builder templates** — headers, footers, post templates, product pages, and more

The freebies are distributed as separate JSON files that you import into different areas of Divi 5 (Divi Library, Theme Builder, Theme Customizer). This guide walks you through what each file contains and how to import them.

## Prerequisites

Before importing any freebie files, verify that you have:

- Divi 5 installed and activated on your WordPress site
- Administrator access to the WordPress dashboard
- The JSON freebie files downloaded from Elegant Themes
- (Optional) WooCommerce installed and activated if you want to use e-commerce templates and sections
- (Optional) Sample posts, projects, and products published if you want to preview all template functionality

## Freebie Files Overview

The Black Friday 2025 package includes seven main JSON files, each serving a different purpose:

### 1. Presets File (`Black-Friday-2025_Divi-5-Freebie_Presets.json`)

**What it contains:** 8 complete layouts plus every Module Preset, Option Group Preset, and Global Variable from the design system.

**What it does:** This is the backbone of the entire freebie package. It imports the core design system that all other files depend on.

**Where to import:** Divi Library (Import & Export → Import Presets)

**Recommendation:** Import this file first before importing any other freebie files.

### 2. Theme Customizer Settings File (`Black-Friday-2025_Divi-5-Freebie_Theme-Customizer.json`)

**What it contains:** Pre-selected fonts and colors chosen by the Elegant Themes design team.

**What it does:** Configures your site's global theme colors and typography via the Theme Customizer.

**Where to import:** Theme Customizer (Portability → Import)

**Note:** This file is entirely optional. You only need to import it if you want to use the recommended color and font scheme.

### 3. All Sections Layouts File (`Black-Friday-2025_Divi-5-Freebie_All-Sections_Layouts.json`)

**What it contains:** 40 layouts organized by section type (Hero, Pricing, Testimonials, CTA, etc.), with multiple pre-made sections in each layout.

**What it does:** Imports organized collections of sections grouped by their function.

**Where to import:** Divi Library (Import & Export → Import Divi Builder Layouts)

**Example:** After importing, you'll find a layout called "Pricing Sections" that contains multiple pricing section variations you can copy and reuse.

### 4. Individual Sections File (`Black-Friday-2025_Divi-5-Freebie_Individual-Sections.json`)

**What it contains:** 430 individual section layouts in a single file.

**What it does:** Provides a comprehensive library of pre-built sections ready to copy into your pages.

**Where to import:** Divi Library (Import & Export → Import Divi Builder Layouts)

**Note:** This file is comprehensive but may take longer to import than the All-Sections file. Choose based on your preference — either approach gives you access to all sections.

### 5. Individual Section Type Files (`Black-Friday-2025_Divi-5-Freebie_SECTION-NAME-Sections.json`)

**What it contains:** 40 separate JSON files, one for each section type (e.g., `Black-Friday-2025_Divi-5-Freebie_Pricing-Sections.json`, `Black-Friday-2025_Divi-5-Freebie_Hero-Sections.json`).

**What it does:** Each file imports a layout containing all sections of that type plus individual section variants. For example, the Pricing file imports "Pricing Sections All", "Pricing - Section 1", "Pricing - Section 2", etc.

**Where to import:** Divi Library (Import & Export → Import Divi Builder Layouts)

**Use case:** Import only the section types you need, rather than all 430 at once.

### 6. Pages File (`Black-Friday-2025_Divi-5-Freebie_Pages.json`)

**What it contains:** Complete pre-made page layouts (e.g., Home Page).

**What it does:** Imports page designs to your Divi Library. These become templates you can load into new pages.

**Where to import:** Divi Library (Import & Export → Import Divi Builder Layouts)

**Important:** Importing this file does NOT create pages on your site. It only adds the layouts to your library. To use them, you must create a new page and load the layout from the library.

**Recommendation:** Import the Presets file first before importing the Pages file to ensure all design tokens are available.

### 7. Theme Builder Templates File (`Black-Friday-2025_Divi-5-Freebie_Theme-Builder-Templates.json`)

**What it contains:** Pre-made templates for dynamic areas of your site: Global Header, Global Footer, Single Post templates, Product templates, 404 pages, search results, and more.

**What it does:** Imports ready-to-use templates for common page types and site-wide sections.

**Where to import:** Theme Builder (Portability → Import)

## Step-by-Step Import Instructions

### Importing Presets to Divi Library

The Presets file should be imported first since all other files depend on it.

1. Go to **WordPress Dashboard → Divi → Divi Library**
2. Click the **Import & Export** button at the top of the page
3. Click the **Import** tab
4. Click **Choose File** and select `Black-Friday-2025_Divi-5-Freebie_Presets.json`
5. After the file is selected, check the **Import Presets** option
6. Click **Import Divi Builder Layouts** to complete the import
7. Wait for the confirmation message — the import may take a moment

### Importing Layouts to Divi Library

Follow these steps for the All-Sections, Individual-Sections, section type files, or Pages file.

1. Go to **WordPress Dashboard → Divi → Divi Library**
2. Click the **Import & Export** button
3. Click the **Import** tab
4. Click **Choose File** and select the JSON file you want to import
5. Check the **Import Presets** option if importing for the first time
6. Click **Import Divi Builder Layouts**
7. Wait for confirmation

### Importing Theme Builder Templates

1. Go to **WordPress Dashboard → Divi → Theme Builder**
2. Click the **Portability** icon (usually at the top)
3. Click the **Import** tab
4. Click **No File Selected** and choose `Black-Friday-2025_Divi-5-Freebie_Theme-Builder-Templates.json`
5. Check the **Import Presets** option
6. Click **Import Divi Theme Builder Templates** to complete the import

### Importing Theme Customizer Settings (Optional)

1. Go to **WordPress Dashboard → Divi → Theme Customizer**
2. Click the **Portability** icon
3. Click the **Import** tab
4. Click **Choose File** and select `Black-Friday-2025_Divi-5-Freebie_Theme-Customizer.json`
5. Click **Import Divi Customizer Settings**

## Using the Imported Freebies

### Loading Layouts on Your Pages

After importing the layout files, you can use them on any page:

1. Create a new page or edit an existing one
2. Click **Edit With The Divi Builder**
3. In the Divi Library (left sidebar), scroll to find the layout you want
4. Click on the layout name to load it into your page
5. Alternatively, use the search bar in the library to find layouts by name

### Copying Individual Sections

If you want to use just one or two sections rather than a full layout:

1. Open any imported layout in the Divi Library
2. Click **Edit With The Divi Builder** on that layout
3. Right-click on the section you want to copy
4. Select **Copy Section** from the context menu
5. Open the page where you want to paste the section
6. Right-click on any existing section
7. Select **Paste Section**
8. Choose where to paste it:
   - **Above the current section**
   - **Below the current section**

### Using Option Group Presets

The Presets file includes pre-configured Option Group Presets for common design elements. To use them:

1. Open any module's settings in the Divi Builder
2. Look for **Option Group Presets** dropdowns in the Design tab
3. Select the preset you want from the dropdown (e.g., "Heading 2", "Small Text", "Medium Spacing", "Outlined - Dark")
4. The preset applies all grouped settings at once

Example: On a Person module, you can select:
- **Title Text:** "Heading 2" preset
- **Body:** "Small Text" preset
- **Spacing:** "Medium" preset
- **Border:** "Outlined - Dark" preset

## Using the Theme Builder Templates

After importing the Theme Builder templates:

1. Go to **Divi → Theme Builder**
2. Select a template type (Header, Footer, Single Post, etc.)
3. Click **Set Default Template** to apply it site-wide
4. Or click **Edit** to customize the template before applying it
5. You can assign specific templates to individual posts, pages, or post types as needed

## Recommended Import Order

To avoid missing dependencies, follow this order:

1. **Black-Friday-2025_Divi-5-Freebie_Presets.json** — Import first (contains all presets and global variables)
2. **Black-Friday-2025_Divi-5-Freebie_All-Sections_Layouts.json** or individual section type files — Import next
3. **Black-Friday-2025_Divi-5-Freebie_Pages.json** — Import after presets are in place
4. **Black-Friday-2025_Divi-5-Freebie_Theme-Builder-Templates.json** — Import to Theme Builder
5. **Black-Friday-2025_Divi-5-Freebie_Theme-Customizer.json** — Optional; import last if you want the recommended colors and fonts

## Tips for Success

- **Import presets first.** All layouts depend on the presets file, so always import it before layouts.
- **Don't import everything at once if you don't need it.** You can import only the section types you'll use (Pricing, Hero, Testimonials, etc.) instead of all 430 sections.
- **Test on a staging site first.** Before importing on a production site, test the files on a staging environment to ensure they work as expected.
- **Create demo content.** Publish some posts, pages, and products (if using WooCommerce) before importing to see how templates render with real content.
- **Customize after importing.** The freebies are starting points — customize colors, text, and layout to match your brand after importing.

## Troubleshooting

### Import button is disabled or not working

- Ensure you've selected a valid JSON file
- Check that the file size is not larger than your server's upload limit
- Verify that the file was downloaded completely and is not corrupted

### Presets don't appear after import

- Refresh the Divi Library page after importing
- Clear your browser cache
- Verify that the Presets import option was checked during import

### Layouts look different than expected

- Ensure the Presets file was imported before the Layouts file
- Check that all Global Variables were imported successfully
- Verify that you have the same fonts installed (the freebies use specific typefaces)

### Theme Builder templates don't show up

- Verify you imported to Theme Builder, not the Divi Library
- Check that the file was imported to the correct location (Portability → Import in Theme Builder)
- Refresh the Theme Builder page

## Related

- [Divi Library in Divi 5](../builder/divi-library-in-divi-5.md)
- [Option Group Presets](../builder/advanced-styling-using-option-group-presets-in-divi-5.md)
- [Getting Started with Theme Builder](../builder/getting-started-with-divi-5-theme-builder.md)
- [Variable Generator in Divi 5](../builder/variable-generator-in-divi-5.md)

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Black Friday 2025 freebies are designed for Divi 5 and may not work with Divi 4.
