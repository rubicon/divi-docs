---
title: "Add, Duplicate & Remove Elements"
category: builder
tags: ["builder", "add-elements", "duplicate", "delete", "workflow"]
related: ["copy-paste-attributes", "right-click-menus"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12992617"
---

# Add, Duplicate & Remove Elements

How to add new elements, duplicate existing ones, and remove elements from your page in the Divi 5 Visual Builder.

## Overview

Building a page in Divi is fundamentally about adding, rearranging, and removing sections, rows, and modules. The Visual Builder provides multiple methods for each of these operations so you can choose whichever fits your workflow -- on-canvas clicks, right-click menus, keyboard shortcuts, the Layers panel, or Wireframe View. For the official Elegant Themes reference, see [Add, Duplicate & Remove Elements](https://help.elegantthemes.com/en/articles/12992617){:target="_blank"}.

## Adding Elements

### On-Canvas Method

The builder uses color-coded plus icons to indicate where you can insert new elements:

| Icon Color | Adds |
|-----------|------|
| **Blue** | A new **Section** at the bottom of the page or between existing sections. |
| **Green** | A new **Row** inside a section. Clicking it prompts you to select a column layout. |
| **Black** | A new **Module** inside a column. Clicking it opens the module picker. |

Hover over the area where you want to add content and click the appropriate plus icon.

### From the Layers View

Open the [Layers View](layers-view.md) panel from the left sidebar. Right-click any existing element in the layer tree and choose:

- **Add Element Above** -- inserts a new element before the selected one.
- **Add Element Inside** -- nests a new element within the selected container.
- **Add Element Below** -- inserts a new element after the selected one.

This approach is especially useful when the element you want to add next to is difficult to target on the canvas (e.g., zero-height rows, overlapping modules).

### From Wireframe View

Switch to [Wireframe View](wireframe-view.md) where the page is displayed as labeled blocks. Plus icons appear between every pair of sibling elements, allowing you to insert new sections, rows, or modules at precise positions without visual interference.

### Using Structure Shortcuts

For a keyboard-driven workflow, use the [structure shortcuts](keyboard-shortcuts.md):

| Shortcut | Action |
|----------|--------|
| R + 1 | Add a row with 1 column |
| R + 2 | Add a row with 2 columns |
| R + 3 | Add a row with 3 columns |
| R + 4 | Add a row with 4 columns |
| R + F | Add a fullwidth row |
| S + 1 | Add a section with 1 row |

## Duplicating Elements

Duplication creates an identical copy of any element -- including all its content, design settings, and child elements -- and places it immediately after the original. Three methods are available:

### Hover Toolbar

Hover over any module, row, or section on the canvas until the action toolbar appears. Click the **duplicate** icon (overlapping squares).

### Right-Click Menu

Right-click the element and select **Duplicate** from the context menu.

### Keyboard Shortcut

Select the element, then press **Cmd + Shift + D** (Mac) or **Ctrl + Shift + D** (Windows).

!!! tip "Duplication vs. Copy & Paste"
    Duplication places the copy immediately after the original. If you need to place the copy elsewhere on the page (or on a different page), use **Copy** (Cmd/Ctrl + C) and **Paste** (Cmd/Ctrl + V) instead.

## Removing Elements

### Hover Toolbar

Hover over the element and click the **trash can** icon in the action toolbar. The element and all its child content are removed immediately.

### Right-Click Menu

Right-click the element and select **Delete**.

### Keyboard Shortcut

Select the element, then press **Cmd + Backspace** (Mac) or **Ctrl + Backspace** (Windows).

!!! warning "Deleting Containers"
    Deleting a section removes all rows and modules inside it. Deleting a row removes all columns and modules inside it. There is no confirmation dialog, but you can immediately undo with **Cmd/Ctrl + Z**.

## Best Practices

- **Duplicate first, customize second.** When building a series of similar sections or modules (e.g., pricing cards, team member blocks), design one, duplicate it, then change the content. This is faster than building each from scratch.
- **Use Layers View for precision.** When the canvas has overlapping or hard-to-click elements, add and reorder from the Layers panel instead.
- **Name your elements.** After duplicating, rename the copy (double-click the label in Wireframe or Layers View) so you can tell duplicates apart.
- **Undo mistakes immediately.** Cmd/Ctrl + Z reverts the last action, including deletions.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior. The Layers View insertion options (Add Above, Add Inside, Add Below) are new to Divi 5.

## Related

- [Copy & Paste Attributes](copy-paste-attributes.md) -- Transfer styles between elements
- [Right-Click Menus](right-click-menus.md) -- Context menu operations
- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Full shortcut reference
- [Layers View](layers-view.md) -- Tree-based element management
- [Wireframe View](wireframe-view.md) -- Structural editing mode
