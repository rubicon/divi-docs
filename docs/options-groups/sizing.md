---
title: "Sizing Options"
description: "Divi 5 Sizing options group — width, max-width, height, min-height, and module alignment controls with multiple CSS unit support."
category: options-groups
tags: ["options-groups", "sizing", "design", "styling"]
related: ["spacing", "position"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102469"
---

# Sizing Options

The Sizing options group controls the dimensions and alignment of any Divi 5 element.

!!! abstract "Quick Reference"
    **What it controls:** Width, max-width, height, min-height, max-height, and horizontal module alignment
    **Where to find it:** Design Tab → Sizing
    **Available on:** All modules, rows, and columns
    **Responsive:** Yes — dimension values can be set independently per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102469)

## Overview

The Sizing options group gives you precise control over how wide and tall an element renders on the page. By setting explicit width, height, and their minimum and maximum constraints, you can override the default content-driven sizing behavior and build pixel-perfect layouts.

These settings are located in the Design tab of any element's settings panel under the Sizing group. All dimension fields accept a wide range of CSS units including px, %, em, rem, vw, vh, in, mm, cm, pt, and pc, so you can use whichever unit best suits your layout approach.

When you set a specific Width or Max Width that is narrower than the element's container, the Module Alignment setting becomes available, letting you position the element to the left, center, or right within its parent. This is particularly useful for creating centered content blocks or asymmetric layouts.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102469).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Width | Text input (with unit selector) | Defines the horizontal dimension of the element. Accepts values in px, %, vw, em, rem, vh, and other CSS units. |
| Max Width | Text input (with unit selector) | Sets an upper limit on the element's width, preventing it from exceeding this value regardless of its container size. |
| Module Alignment | Select (left / center / right) | Controls horizontal alignment of the element within its parent container. Only available when Width or Max Width is set to less than 100%. |
| Min Height | Text input (with unit selector) | Establishes a minimum vertical dimension, ensuring the element is at least this tall even if its content is shorter. |
| Height | Text input (with unit selector) | Sets a fixed vertical dimension, overriding the default content-driven height. |
| Max Height | Text input (with unit selector) | Restricts the maximum vertical dimension the element can reach, useful for preventing content overflow in dynamic layouts. |

## Which Elements Use This

The Sizing options group is available on all Divi 5 modules, as well as on rows and columns. Sections typically have their own width behavior governed by the layout settings, but most content-level elements expose the full set of sizing controls.

## Code Examples

Set a module to fill half its container width and center it:

```css
.my-module {
  width: 50%;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}
```

Establish a minimum height for a hero section element:

```css
.hero-module {
  min-height: 80vh;
}
```

## Related

- [Spacing Options](spacing.md)
- [Position Options](position.md)
- [Flexbox Layout](../builder/flexbox.md) — Control how elements size and distribute within flex containers
- [CSS Grid](../builder/css-grid.md) — Define explicit column and row sizing for grid layouts
- [Responsive Options](../builder/responsive-options.md) — Set different sizing values per breakpoint
- [Advanced Units](../builder/advanced-units.md) — Use calc(), clamp(), and custom units in sizing fields
