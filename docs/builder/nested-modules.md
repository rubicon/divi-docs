---
title: "Nested Modules"
description: "Divi 5 nested modules — place any module inside another module with full Flex and Grid layout controls for deeply layered compositions."
category: builder
tags: ["builder", "nested-modules", "layout", "innerblocks", "flex", "grid"]
related: ["nested-rows", "canvases", "flexbox", "css-grid"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12672584"
---

# Nested Modules

Place modules inside other modules to build complex, deeply layered layouts without custom code.

!!! abstract "Quick Reference"
    **What it does:** Allows any Divi module to contain child modules, enabling multi-level nesting with layout controls.
    **Where to find it:** Content Tab → Elements → Add Element, or right-click → Add Element Inside.
    **Key features:**

    - Every element acts as a Flex or Grid container when it holds children
    - Insert via settings panel (Content → Elements) or right-click context menu
    - Full layout controls (direction, alignment, gap, wrapping) on parent modules
    - Layers View shows nested hierarchy for deep structures

    **ET Docs:** [Nested Modules](https://help.elegantthemes.com/en/articles/12672584){:target="_blank"}

## Overview

Divi 5 fundamentally changes how modules relate to each other by allowing any module to contain child modules. In previous versions, modules were terminal elements that could only live inside columns. Now, every element in Divi 5 acts as a potential Flex or Grid container, so you can nest rows, tabs, sliders, buttons, and other modules as deeply as your design requires.

This capability removes the need for workarounds like custom HTML or third-party plugins when building layouts such as card grids with embedded buttons, tabbed interfaces with complex inner content, or slider items containing multiple sub-elements.

For the official Elegant Themes documentation, see [Nested Modules](https://help.elegantthemes.com/en/articles/12672584).

## How Nested Modules Work

Every Divi 5 element is a Flex or Grid container by default. This means that any module can hold child elements, and the same layout controls (direction, alignment, gap, wrapping) available on Sections, Rows, and Columns are also available on individual modules when they contain nested content.

### Adding Nested Modules

There are two primary methods for inserting a module inside another module.

**Method 1: Settings Panel**

1. Open the settings for any Divi element.
2. Navigate to **Content Tab > Elements**.
3. Select **Add Element**.
4. Choose the module or row you want to insert inside the parent.

**Method 2: Right-Click Context Menu**

1. Right-click an existing module on the canvas.
2. Choose an insertion position: **Above**, **Below**, or **Inside**.
3. Select the element type to insert.

The right-click method provides precise placement control without needing to locate a plus icon, and the "Inside" option is what distinguishes nested insertion from sibling insertion.

### Supported Elements

All native Divi modules support nesting. Commonly nested elements include:

- Rows (creating nested row structures)
- Buttons (inside Blurbs, CTAs, or Groups)
- Tabs and Sliders (with complex inner content)
- Groups (as intermediate containers)
- Any standard content module

## Layout Controls for Nested Content

When a module contains child elements, the parent module gains full Flex and Grid layout controls. These appear under **Design Tab > Layout** and include:

| Setting | Type | Description |
|---------|------|-------------|
| Layout Type | Dropdown | Choose Flex or Grid for the container behavior of the parent module |
| Layout Direction | Dropdown | Set child flow to Row, Row Reverse, Column, or Column Reverse |
| Justify Content | Dropdown | Distribute children along the main axis (Start, Center, End, Space Between, etc.) |
| Align Items | Dropdown | Position children along the cross axis (Start, Center, End, Stretch) |
| Gap | Input | Set horizontal and vertical spacing between nested child elements |
| Layout Wrapping | Dropdown | Control whether children wrap to new lines (No Wrap, Wrap, Wrap Reverse) |

These are the same Flex controls available on Sections, Rows, and Columns, applied consistently to any element acting as a container.

### Structure Templates

You can apply predefined column structure templates to any module that contains nested content, giving you quick access to common layout patterns (e.g., two-column, three-column) without manually configuring each Flex property.

## Managing Nested Elements

### Sortable Elements Panel

The **Elements** panel within a module's Content Tab displays all child elements in a sortable list. You can drag items within this list to reorder them, which is often easier than rearranging via the canvas for deeply nested layouts.

### Layers View Integration

Nested modules appear as indented entries in the [Layers View](layers-view.md), reflecting the full hierarchy. This makes it straightforward to select, reorder, or edit deeply nested elements that might be difficult to click on the canvas directly.

### Right-Click Management

Right-clicking any nested element provides the full set of context menu actions: Cut, Copy, Paste, Duplicate, Delete, and attribute management options.

## Nesting Depth

The documentation does not specify a maximum nesting depth. In practice, you can nest elements multiple levels deep (e.g., a Section containing a Row containing a Column containing a Group containing a Blurb containing a Button). However, deeply nested structures increase layout complexity and may impact builder performance on lower-powered devices.

## Common Patterns

### Card with Embedded Button

Place a Button module inside a Blurb module. Set the Blurb's layout direction to Column so the button appears below the blurb content. Adjust gap spacing for consistent padding.

### Tabbed Content with Complex Layouts

Nest a Row with multiple Columns inside each Tab item. Each column can contain its own modules, creating rich tabbed interfaces without leaving the Tabs module.

### Slider with Multi-Element Slides

Insert a Group module inside each Slider item, then nest multiple modules (Heading, Text, Button) within the Group. Use Flex direction and alignment to control the slide layout.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 did not support nesting modules inside other modules.

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Nested modules are stored as innerBlocks within the parent block's JSON structure in `post_content`. Each nested module becomes a child block entry with its own `blockName`, `attrs`, and potentially its own `innerBlocks` array, creating a recursive tree structure.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Parse `post_content` block JSON, traverse `innerBlocks` arrays recursively | Needs Testing | Each block object contains `blockName`, `attrs`, `innerContent`, and `innerBlocks` |
| Modify | Update the target block's `attrs` within the nested `innerBlocks` tree, then serialize back to `post_content` | Needs Testing | Must preserve the full tree structure; modifying a deeply nested block requires walking the entire hierarchy |
| Create | Insert a new block object into the parent block's `innerBlocks` array at the desired index | Needs Testing | The new block must include valid `blockName` and `attrs` matching the module type schema |

!!! warning "Structural Integrity"
    When programmatically modifying nested module structures, always validate that the resulting JSON maintains proper parent-child relationships. Malformed `innerBlocks` arrays can cause the Visual Builder to fail to parse the layout.

## Troubleshooting

!!! warning "Nested Elements Not Appearing"
    If a nested module does not render on the front end, verify that the parent module's layout type is set to Flex or Grid. Block layout mode may not properly display nested children.

!!! warning "Performance with Deep Nesting"
    Extremely deep nesting (5+ levels) may cause the Visual Builder to slow down. Consider flattening your structure using Rows and Columns where possible.

## Related

- [Nested Rows](nested-rows.md)
- [Canvases](canvases.md)
- [Flexbox Layout System](flexbox.md)
- [CSS Grid Layout System](css-grid.md)
- [Group Module](../modules/group.md)
