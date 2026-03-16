---
title: "Import Elements from Divi Library"
category: troubleshooting
tags: ["troubleshooting", "library", "import", "layouts"]
related: ["library", "visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12918951"
---

# Import Elements from Divi Library

Add pre-built layouts, sections, rows, and modules from your Divi Library into any page using the Visual Builder.

## Overview

The Divi Library stores reusable design components at four levels: full page layouts, sections, rows, and modules. You can import any of these into a page without rebuilding them from scratch. Each element type has its own import workflow and placement rules.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12918951).

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
