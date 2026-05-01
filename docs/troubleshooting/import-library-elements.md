---
title: "Import Elements from Divi Library"
category: troubleshooting
tags: ["troubleshooting", "library", "import", "layouts"]
related: ["library", "visual-builder", "library-import-json"]
divi_version: "5.x"
last_updated: 2026-04-30
source_url: "https://help.elegantthemes.com/en/articles/12918951"
---

# Import Elements from Divi Library

Add pre-built layouts, sections, rows, and modules from your Divi Library into any page using the Visual Builder.

## Overview

The Divi Library stores reusable design components at four levels: full page layouts, sections, rows, and modules. You can import any of these into a page without rebuilding them from scratch. Each element type has its own import workflow and placement rules.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12918951).

If you **import JSON** into the Divi Library (portability / `et_builder_layouts`) and the item **appears in the admin library list** but **not** in the Visual Builder **Saved Layout** / **Add From Library** pickers, the file’s **`terms`** array is usually wrong — for example `layout_type` must use slug `layout` for full page layouts, not `page`. See [Library Import JSON Structure — Common pitfalls](../internals/library-import-json.md#common-pitfalls-library-json-imports).

## Import a Full Page Layout

1. Open the page in the Visual Builder.
2. Click the **Add Layout** icon in the left sidebar.
3. Select the **Saved Layout** tab.
4. Choose the layout you want to use.
5. Click **Use This Layout**.

!!! warning "Replace vs. append"
    By default, importing a layout replaces all existing page content. Uncheck **Replace Existing Content** if you want to add the layout below your current content.

## Import a Section

1. Click the **Add Section** button (the blue "+" icon between existing sections).
2. Select the **Add From Library** tab.
3. Choose the saved section.
4. Click **Use This Section**.

## Import a Row

1. Click the **Add Row** button inside any section (the green "+" icon).
2. Select the **Add From Library** tab.
3. Choose the saved row.
4. Click **Use This Row**.

!!! note
    Rows can only be imported inside an existing section.

## Import a Module

1. Click the **Add Module** button inside any row (the gray "+" icon).
2. Select the **Add From Library** tab.
3. Choose the saved module.
4. Click **Use This Module**.

!!! note
    Modules can only be imported inside an existing row.

## Hierarchy Rules

Divi enforces a strict parent-child hierarchy for imported elements:

| Element | Can Be Placed In |
|---------|-----------------|
| Layout | Replaces or appends to entire page |
| Section | Directly on the page |
| Row | Inside a section |
| Module | Inside a row |

## Related

- [Divi Library](../builder/library.md)
- [Visual Builder](../builder/visual-builder.md)
- [Global Elements](../builder/global-elements.md)
- [Library Import JSON Structure](../internals/library-import-json.md) — `et_builder_layouts` shape, `terms` taxonomies, and import pitfalls
