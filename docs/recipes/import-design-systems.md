---
title: "Import a Design System into Divi 5"
description: "Step-by-step guide to importing Divi 5 design systems (JSON presets, global variables, layouts, Theme Builder templates, and Customizer settings) into a clean site."
category: recipes
tags: [recipes, design-system, presets, global-variables, import, theme-builder]
related: [import-library-elements, upload-svg-json, block-format, json-attribute-map]
divi_version: "5.x"
last_updated: 2026-03-17
source_url: "https://www.elegantthemes.com/blog/divi-resources/divi-5-launch-gift-design-system"
---

# Import a Design System into Divi 5

How to import a Divi 5 “design system” (presets, design variables, layouts, Theme Builder templates, and optional Customizer settings) into a clean Divi 5 installation.

## Overview

Most Divi 5 design system downloads ship as a ZIP containing multiple JSON files. Each JSON file targets a different importer:

- **Presets**: module presets + option group presets
- **Design Variables**: global colors + variables (numbers, strings, fonts, images, links)
- **Layouts**: pages, section layouts, premade layouts
- **Theme Builder**: headers/footers/templates (often references layouts)
- **Theme Customizer (optional)**: baseline typography + colors as WP theme mods

The key to successful imports is **order**: presets + variables first, then layouts, then Theme Builder, then Customizer.

!!! note "Start on a clean site"
    Imports are safest on a fresh Divi 5 install. Importing into an existing site can overwrite presets, add lots of library items, and change Theme Builder assignments.

## What’s in a typical ZIP

Using the Divi 5 Launch Design System as an example, the ZIP contains files like:

- `Divi-5-Launch-Freebie_Presets.json`
- `Divi-5-Launch-Freebie_Global-Variables.json`
- `Divi-5-Launch-Freebie_All-Sections_Layouts.json` (or `..._All-Individual-Sections.json`)
- `Divi-5-Launch-Freebie_Pages.json` (and sometimes additional layout packs)
- `Divi-5-Launch-Freebie_Theme-Builder-Templates.json`
- `Divi-5-Launch-Freebie_Theme-Customizer.json` (optional)

If you see `__MACOSX/` folders, you can ignore them.

## Import order (recommended)

1. **Import Presets**
2. **Import Global Variables**
3. **Import Section Layouts**
4. **Import Page / Premade Layouts**
5. **Import Theme Builder Templates**
6. **(Optional) Import Theme Customizer settings**

This order avoids missing references like a layout that points to a preset id or a variable that doesn’t exist yet.

## How to tell which JSON file goes where (by `context`)

If you’re importing a different design system and the filenames aren’t obvious, open the JSON file and check the first field: **`context`**. It determines which Divi importer will accept the file.

| `context` value | What it contains | Where to import |
|---|---|---|
| `et_builder` | Presets and/or Global Variables | **Divi → Divi Library → Import & Export** |
| `et_builder_layouts` | Layouts (pages, sections, premades) | **Divi → Divi Library → Import & Export** |
| `et_theme_builder` | Theme Builder templates + referenced layouts | **Divi → Theme Builder → ↑↓** |
| `et_divi_mods` | Theme Customizer settings (theme mods) | **Divi → Theme Customizer → ↑↓** |

For the deeper JSON structure and how presets/variables are referenced, see [Library Import JSON Structure](../internals/library-import-json.md).

## Step-by-step import (Divi 5 Launch Design System)

### 1) Import Presets (Divi Library)

1. Go to **Divi → Divi Library → Import & Export**
2. Choose `Divi-5-Launch-Freebie_Presets.json`
3. Ensure **Import Presets** is enabled
4. Import

### 2) Import Global Variables (Divi Library)

1. In the same **Import & Export** dialog, choose `Divi-5-Launch-Freebie_Global-Variables.json`
2. Ensure **Import Global Variables** is enabled
3. Import

### 3) Import Section Layouts (Divi Library)

Choose one:

- **Grouped section layouts**: import `Divi-5-Launch-Freebie_All-Sections_Layouts.json`
- **Individual sections**: import `Divi-5-Launch-Freebie_All-Individual-Sections.json`

Import via **Divi → Divi Library → Import & Export**.

### 4) Import Pages and Premade Layouts (Divi Library)

Import any of the following (as desired):

- `Divi-5-Launch-Freebie_Pages.json`
- `Divi-5-Launch-Freebie_Premade-Layouts.json`
- `Divi-5-Launch-Freebie_Preset-Pages.json`

These create many Divi Library items and/or pages depending on how the pack is structured.

### 5) Import Theme Builder templates (Theme Builder)

1. Go to **Divi → Theme Builder**
2. Use the **↑↓ Import/Export** control
3. Import `Divi-5-Launch-Freebie_Theme-Builder-Templates.json`
4. If prompted, enable importing presets with the templates

!!! warning "Template assignments can override your site"
    Theme Builder imports can replace existing header/footer/template assignments. On a non-clean site, export your current Theme Builder state first.

### 6) Optional: Import Theme Customizer settings (Customizer)

1. Go to **Divi → Theme Customizer**
2. Use the **↑↓ Import/Export** control
3. Import `Divi-5-Launch-Freebie_Theme-Customizer.json`

This typically affects global typography and baseline colors.

## After import: how to customize safely

1. **Start with Design Variables** (colors, fonts, spacing, type scale).
2. Then adjust key **presets** (buttons, headings, sections, etc.).
3. Only then tweak specific **layouts**.

This preserves the “single source of truth” workflow where variables feed presets, and presets feed layouts.

## Troubleshooting

!!! warning "JSON import fails or file is blocked"
    Some hosts/security plugins block JSON uploads. See [Upload SVG and JSON Files](../troubleshooting/upload-svg-json.md).

!!! warning "Imported layouts look wrong (missing styles)"
    You likely imported layouts **before** presets/variables. Re-import in the recommended order.

!!! warning "Theme Builder import changed my header/footer"
    Theme Builder templates include assignment rules. Export your Theme Builder first on non-clean sites, then re-import selectively.

## Related

- [Library Import JSON Structure](../internals/library-import-json.md)
- [Import Elements from Divi Library](../troubleshooting/import-library-elements.md)
- [Upload SVG and JSON Files](../troubleshooting/upload-svg-json.md)
- [Block Comment Format](../internals/block-format.md)
