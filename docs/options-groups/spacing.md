---
title: "Spacing Options"
description: "Divi 5 Spacing options group — margin and padding controls with responsive breakpoints, unit selection, and linked value toggles for all elements."
category: options-groups
tags: ["options-groups", "spacing", "design", "styling"]
related: ["sizing", "position"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102490"
---

# Spacing Options

The Spacing options group controls the margin and padding of any Divi 5 element, managing the space inside and around it.

!!! abstract "Quick Reference"
    **What it controls:** Margin and padding values for all four sides with linked value toggles
    **Where to find it:** Design Tab → Spacing
    **Available on:** All modules, sections, rows, and columns
    **Responsive:** Yes — spacing values can be set independently per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102490)

## Overview

The Spacing options group provides direct control over the two fundamental CSS box model properties: margin and padding. Margin defines the external space surrounding an element, separating it from neighboring elements on the page. Padding defines the internal space between an element's content and its outer boundary.

You will find the Spacing controls in the Design tab of any element's settings panel. Each property (margin and padding) exposes four directional values: top, right, bottom, and left. You can set each side independently or use the chainlink toggle to lock paired values together for symmetrical spacing.

All spacing fields support multiple CSS units including px, %, em, rem, vw, and vh, giving you flexibility to use fixed or relative spacing as needed. Both margin and padding default to 0 when no value is specified. Responsive device toggles are available, so you can fine-tune spacing for desktop, tablet, and mobile breakpoints independently.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102490).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Margin Top | Text input (with unit selector) | Sets the external space above the element, pushing it away from the element above. |
| Margin Right | Text input (with unit selector) | Sets the external space to the right of the element. |
| Margin Bottom | Text input (with unit selector) | Sets the external space below the element, creating distance from the element beneath. |
| Margin Left | Text input (with unit selector) | Sets the external space to the left of the element. |
| Padding Top | Text input (with unit selector) | Sets the internal space between the top edge of the element and its content. |
| Padding Right | Text input (with unit selector) | Sets the internal space between the right edge and the content. |
| Padding Bottom | Text input (with unit selector) | Sets the internal space between the bottom edge and the content. |
| Padding Left | Text input (with unit selector) | Sets the internal space between the left edge and the content. |
| Link Toggle (chainlink icon) | Toggle | Locks paired directional values (top+bottom or left+right) together so they stay symmetrical when adjusted. |

## Which Elements Use This

The Spacing options group is available on every Divi 5 element, including sections, rows, columns, and all modules. It is one of the most universally used options groups since virtually every layout requires spacing adjustments.

## Code Examples

Add consistent internal padding and remove default bottom margin:

```css
.my-module {
  padding: 30px 40px;
  margin-bottom: 0;
}
```

Use responsive spacing with viewport-relative units:

```css
.my-section {
  padding-top: 8vh;
  padding-bottom: 8vh;
  margin-left: 5vw;
  margin-right: 5vw;
}
```

## Related

- [Sizing Options](sizing.md)
- [Position Options](position.md)
- [Flexbox Layout](../builder/flexbox.md) — Use gap and alignment instead of manual spacing in flex containers
- [Responsive Options](../builder/responsive-options.md) — Set different margin and padding values per breakpoint
- [Advanced Units](../builder/advanced-units.md) — Use calc(), vw, and other CSS functions in spacing fields
