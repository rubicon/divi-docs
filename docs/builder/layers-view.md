---
title: "Layers View"
description: "Divi 5 Layers View — collapsible tree panel for navigating, reordering, renaming, locking, and managing every element on your page."
category: builder
tags: ["builder", "layers", "navigation", "workflow"]
related: ["visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/using-the-divi-layers-view"
---

# Layers View

Divi’s Layer View provides an efficient way to navigate your page’s elements while designing.

!!! abstract "Quick Reference"
    **What it does:** Displays all page elements in a collapsible hierarchical tree for navigation and management.
    **Where to find it:** Left sidebar → Layers icon, or bottom toolbar → Layers icon.
    **Key features:**

    - Click any layer to select and open its settings
    - Drag-and-drop reordering within and across containers
    - Double-click to rename elements for clarity
    - Lock, hide, and right-click context menu on every layer

    **ET Docs:** [Layers View](https://www.elegantthemes.com/documentation/divi/using-the-divi-layers-view){:target="_blank"}

The Divi layers view adds a very quick and easy way to view, rearrange, edit, and rename your elements. This is especially true when you have elements that have transition effects or negative margins on them that would normally be tricky to click on the traditional way.

Divi’s layers view gives you easy access to any element within your page. It’s small, so you can keep it open in a corner or wherever is convenient for you during the design process. Additionally, the layers view works well to help you access elements in complex designs with overlapping elements or altered transform controls. When the layers view is active, you can click on any section, row, column, or module to edit it with ease.

<!-- ![Layers View overview](../assets/screenshots/builder/layers-view/overview.png){ loading=lazy }
*The Layers View interface in Divi 5.* -->

## The Power of Divi’s Layers View

The Layers View panel is indispensable when working with complex page designs. In the standard visual canvas, overlapping elements, negative margins, and transform effects can make it difficult to click the right element. Layers View eliminates this friction by presenting every element in a clean, hierarchical tree where any item is one click away.

Key capabilities:

- **Navigate** directly to any element regardless of visual overlap.
- **Reorder** elements by dragging them within the tree.
- **Rename** elements for clarity on long pages.
- **Lock** or **hide** elements to protect them from accidental changes.
- **Access settings** with a single click on the layer entry.
- **Right-click** any layer for the full [context menu](right-click-menus.md) (copy, paste, extend, delete, etc.).

## Accessing the Layers View Panel

There are two ways to open Layers View:

1. **Left Sidebar**: Click the **Layers** icon in the [left sidebar](left-sidebar.md).
2. **Bottom Toolbar**: Click the **Layers** icon in the right section of the bottom toolbar.

The panel can remain open alongside the visual canvas or [Wireframe View](wireframe-view.md).

## How To Use Layers View Panel

### Selecting Elements

Click any layer in the tree to select the corresponding element on the canvas. Its settings panel opens automatically.

### Drag-and-Drop Reordering

Drag a layer to a new position in the tree to move the element on the page. You can move elements within the same container or drag them into a different container (e.g., move a module from one column to another).

### Renaming Elements

Double-click a layer’s name to enter edit mode. Type a custom name (e.g., "Hero CTA Button", "Pricing Row") and press Enter. Custom names persist across editing sessions and also appear in [Wireframe View](wireframe-view.md).

### Locking Elements

Click the **lock icon** on a layer to prevent it from being edited or moved. Locked elements display a lock indicator on both the layer and the canvas. Click the lock icon again (or right-click and select **Unlock**) to restore editing.

### Hiding Elements

Click the **eye icon** on a layer to temporarily hide the element from the canvas. Hidden elements are still part of the page -- they are just not rendered during the current editing session. Click the eye icon again to restore visibility.

### Collapsing and Expanding

Click the arrow next to any container element (section, row, column) to collapse or expand its children. This is helpful for focusing on a specific area of a long page.

### Right-Click Context Menu

Right-click any layer to access the full [right-click menu](right-click-menus.md), including:

- **Add Element Above / Inside / Below** -- insert new elements at precise positions.
- **Copy / Paste / Duplicate / Delete** -- standard element operations.
- **Copy Attributes / Paste Design Attributes** -- transfer styles between elements.
- **Lock / Disable / Save to Library** -- element management.

### Keyboard Shortcuts in Layers View

Several [keyboard shortcuts](keyboard-shortcuts.md) work while the Layers panel is focused:

| Shortcut | Action |
|----------|--------|
| Cmd/Ctrl + C | Copy selected layer |
| Cmd/Ctrl + V | Paste |
| Cmd/Ctrl + Shift + D | Duplicate |
| Cmd/Ctrl + Backspace | Delete |
| Cmd/Ctrl + Z | Undo |

## Tips & Best Practices for Using Layers View

- **Rename everything on complex pages.** Default names like "Text Module" and "Row" are unhelpful when a page has dozens of elements. Invest a few seconds in descriptive names to save minutes of hunting later.
- **Lock finished sections.** Once a section is finalized, lock it to prevent accidental edits while you work on other parts of the page.
- **Combine with Wireframe View.** Open Layers View while in [Wireframe View](wireframe-view.md) for maximum structural control -- Wireframe shows the spatial layout while Layers shows the hierarchy.
- **Use Layers for drag operations.** Dragging in the Layers tree is more precise than dragging on the canvas, especially for moving elements between containers.
- **Collapse irrelevant sections.** On long pages, collapse the sections you are not working on to reduce visual clutter in the panel.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If this feature is not visible, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.

<!-- TODO: Add feature-specific troubleshooting items -->

## Related

- [Visual Builder](visual-builder.md)
- [Visual Builder Interface](vb-interface.md) -- Overview of the full editor workspace
- [Wireframe View](wireframe-view.md) -- Structural editing mode as an alternative to layers
- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Shortcut to toggle the layers panel
- [Right-Click Menus](right-click-menus.md) -- Context menu actions available from the layers panel
