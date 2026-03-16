---
title: "Right-Click Menus"
description: "Divi 5 right-click context menus — copy, paste, extend, lock, reset, and manage element attributes directly from the canvas."
category: builder
tags: ["builder", "right-click", "context-menu", "workflow"]
related: ["keyboard-shortcuts", "vb-interface"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12992238"
---

# Right-Click Menus

Context-sensitive menus that appear when you right-click any element in the Divi 5 Visual Builder.

!!! abstract "Quick Reference"
    **What it does:** Provides contextual access to copy, paste, extend, reset, lock, disable, and save operations on any element.
    **Where to find it:** Right-click any element on the Visual Builder canvas or in Layers View.
    **Key features:**

    - Granular paste options (All, Design, Content, Presets, Select)
    - Extend and Find & Replace attribute operations
    - Reset options at element, tab, group, or field level
    - Lock, disable, and save-to-library actions

    **ET Docs:** [Divi Right-Click Menus](https://help.elegantthemes.com/en/articles/12992238){:target="_blank"}

## Overview

Right-click menus provide fast, contextual access to the most common operations you perform on sections, rows, columns, and modules. Instead of opening the settings panel or navigating toolbars, you can right-click any element and immediately copy, paste, extend, lock, duplicate, or delete it. For the official Elegant Themes reference, see [Divi Right-Click Menus](https://help.elegantthemes.com/en/articles/12992238){:target="_blank"}.

The menu adapts its options based on the type of element you clicked and what you have on your clipboard, so the available actions are always relevant to your current context.

## How to Access

Right-click any element (section, row, column, or module) directly on the canvas while the Visual Builder is active. The context menu appears at your cursor position.

You can also right-click within the [Layers View](layers-view.md) panel to access the same menu for any element in the tree.

## Available Actions

### Core Operations

| Action | Description |
|--------|-------------|
| **Undo** | Reverse the most recent action. |
| **Redo** | Restore a previously undone action. |
| **Copy** | Copy the entire element to the clipboard. |
| **Cut** | Remove the element and place it on the clipboard. |
| **Paste** | Insert a previously copied element. |
| **Duplicate** | Create an identical copy of the element directly below (or beside) the original. |
| **Delete** | Remove the element from the page. |

### Attribute Operations

These options let you transfer specific design properties between elements without cloning content. See [Copy & Paste Attributes](copy-paste-attributes.md) for a deeper explanation.

| Action | Description |
|--------|-------------|
| **Copy Attributes** | Copy the element's content, styles, and presets to the clipboard. |
| **Paste All Attributes** | Apply all copied attributes (content, styles, presets) to the target element. |
| **Paste Design Attributes** | Apply only styles and presets, leaving the target element's content unchanged. |
| **Paste Content Attributes** | Apply only content (text, images, links), leaving styles untouched. |
| **Paste Presets** | Apply only the preset assignments from the source element. |
| **Paste Select Design Attributes** | Choose specific modified styles and presets to paste. |
| **Paste Select Style Attributes** | Paste only modified styles without presets or content. |
| **Paste Select Content Attributes** | Selectively paste content fields. |

### Extend & Replace

| Action | Description |
|--------|-------------|
| **Extend Attributes** | Apply the element's styles to other matching elements across a chosen scope (section, row, column, or page). |
| **Find & Replace** | Open the [Find & Replace Attributes](find-replace-attributes.md) dialog for the selected field or element. |

### Reset Options

| Action | Description |
|--------|-------------|
| **Reset All Attributes** | Remove all customizations and revert to defaults. |
| **Reset Design Attributes** | Reset styles and presets only. |
| **Reset Style Attributes** | Reset styles only, keeping presets. |
| **Reset Content Attributes** | Reset content to defaults. |
| **Reset Presets** | Remove preset assignments. |

### Element Management

| Action | Description |
|--------|-------------|
| **Save to Library** | Store the element in the Divi Library for reuse. |
| **Save to Divi Cloud** | Upload the element to your Divi Cloud account. |
| **Lock / Unlock** | Prevent (or allow) editing of the element. Locked elements display a lock indicator. |
| **Disable** | Temporarily hide the element from the front end without deleting it. |

## Applicable Elements

Right-click menus work on every element type in the builder, though the available options vary slightly:

| Element Type | Available Operations |
|-------------|---------------------|
| **Sections** | All core, attribute, extend, lock, disable, save, and delete operations. |
| **Rows** | All core, attribute, extend, lock, disable, save, and delete operations. |
| **Columns** | Attribute copy/paste, extend, reset, and style operations. |
| **Modules** | Full menu including all attribute operations, presets, lock, disable, and save. |
| **Module Groups** | Same as modules, plus group-specific nesting operations. |
| **Fields / Option Groups** | Scoped copy/paste and reset for individual settings or setting groups. |

## Typical Workflows

### Copying a Button Style to Multiple Buttons

1. Design your first button with the desired colors, fonts, and spacing.
2. Right-click the button and select **Copy Attributes**.
3. Right-click each target button and select **Paste Design Attributes**.
4. Each target button inherits the styling while keeping its own text and link.

### Extending a Section Background Across the Page

1. Right-click the section with the background you want to reuse.
2. Select **Extend Attributes**.
3. Choose the scope (e.g., "All Sections on Page").
4. The background settings propagate to every matching section.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 right-click menus. The attribute paste variants (Paste Design, Paste Content, Paste Select, etc.) are new to Divi 5.

## Related

- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Hotkey alternatives for many right-click actions
- [Visual Builder Interface](vb-interface.md) -- Overview of the editor workspace
- [Copy & Paste Attributes](copy-paste-attributes.md) -- Full attribute transfer documentation
- [Find & Replace Attributes](find-replace-attributes.md) -- Bulk value replacement
