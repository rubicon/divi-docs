---
title: "Position Options"
description: "Divi 5 Position options group — relative, absolute, and fixed positioning with vertical/horizontal offsets and z-index stacking."
category: options-groups
tags: ["options-groups", "position", "advanced"]
related: ["scroll-effects", "sizing", "spacing"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102783"
---

# Position Options

The Position options group determines how an element is placed within the page layout, enabling precise control over positioning, offsets, and stacking order.

!!! abstract "Quick Reference"
    **What it controls:** CSS position method (relative, absolute, fixed), directional offsets, and z-index stacking
    **Where to find it:** Advanced Tab → Position
    **Available on:** All modules, sections, rows, and columns
    **Responsive:** Yes — position values can be configured per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102783)

## Overview

Every module in Divi 5 includes a Position options group under the Advanced tab. These settings let you override the default document flow so that elements can be pinned to a specific spot on the page, layered on top of one another, or anchored to the viewport while the user scrolls.

By default, every element uses relative positioning, meaning it stays in the normal document flow and any offset values shift it visually without affecting surrounding elements. Switching to absolute positioning removes the element from the flow entirely, positioning it relative to its nearest positioned ancestor (or the viewport if none exists). Fixed positioning also removes the element from the flow but locks it to the viewport so it remains visible regardless of scrolling.

These settings are essential for creating overlapping layouts, sticky navigation bars, floating call-to-action buttons, and any design that requires elements to break out of the standard top-to-bottom flow.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102783).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Position | Dropdown | Defines the positioning method for the element. Options are Relative (default, stays in document flow), Absolute (removed from flow, positioned relative to nearest positioned ancestor), and Fixed (removed from flow, locked to the viewport). |
| Vertical Offset | Numeric input | Shifts the element up or down from its natural position. Positive values move it downward; negative values move it upward. |
| Horizontal Offset | Numeric input | Shifts the element left or right from its natural position. Positive values move it to the right; negative values move it to the left. |
| Z-Index | Numeric input | Controls the stacking order of the element. Higher values place the element in front of elements with lower values, which is useful for layered or overlapping designs. |

## Which Elements Use This

All modules, columns, rows, and sections in the Divi 5 Visual Builder include the Position options group. The settings are located under the **Advanced** tab of any element's settings panel.

## Code Examples

Use a CSS ID or class to target a positioned element with additional custom styles:

```css
/* Make a module stick to the top of its container */
.floating-cta {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 999;
}
```

```css
/* Overlap two elements using absolute positioning */
.overlap-badge {
  position: absolute;
  top: -10px;
  right: -10px;
  z-index: 10;
}
```

## Related

- [Scroll Effects Options](scroll-effects.md)
- [Sizing Options](sizing.md)
- [Spacing Options](spacing.md)
- [Transform Options](transform.md) — Combine position with translate for precise element placement
- [Flexbox Layout](../builder/flexbox.md) — Use flex positioning as an alternative to absolute position
- [CSS Grid](../builder/css-grid.md) — Grid placement as a layout-driven positioning approach
