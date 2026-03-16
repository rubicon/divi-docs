---
title: "Transform Options"
description: "Divi 5 Transform options group — scale, translate, rotate, and skew controls with transform origin for 2D and 3D element effects."
category: options-groups
tags: ["options-groups", "transform", "design", "styling"]
related: ["filters", "animation", "position"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102613"
---

# Transform Options

The Transform options group applies scaling, rotation, translation, and skewing effects to any Divi 5 element for dynamic layout designs.

!!! abstract "Quick Reference"
    **What it controls:** Scale, translate, rotate, skew values and transform origin for 2D/3D effects
    **Where to find it:** Design Tab → Transform
    **Available on:** All modules, sections, rows, and columns
    **Responsive:** Yes — transform values can be configured per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102613)

## Overview

The Transform options group gives you access to CSS transform properties directly within the Divi 5 visual builder. These controls let you scale, rotate, move, and skew elements in both 2D and 3D space, enabling creative layouts and visual effects that go beyond standard positioning.

These settings are located in the Design tab of any element's settings panel under the Transform group. Each transform type (scale, translate, rotate, and skew) provides separate horizontal and vertical controls, and a transform origin setting lets you define the anchor point from which all transformations are calculated.

Transforms are particularly powerful when combined with hover states and transitions, as they enable smooth interactive effects like growing buttons, tilting cards, and sliding content. Because transforms do not affect the document flow, the surrounding layout remains stable while the transformed element changes its visual position and shape.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102613).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Scale (Horizontal) | Range slider / numeric input | Resizes the element's width. A value of 1 is the default size; values above 1 enlarge, below 1 shrink. |
| Scale (Vertical) | Range slider / numeric input | Resizes the element's height independently from width. |
| Scale Link Toggle | Toggle (chainlink icon) | Locks horizontal and vertical scale values together to maintain proportional resizing. |
| Translate (Horizontal) | Numeric input | Moves the element left or right from its original position. Positive values move right, negative values move left. |
| Translate (Vertical) | Numeric input | Moves the element up or down from its original position. Positive values move down, negative values move up. |
| Rotate (X-axis) | Numeric input / range slider | Rotates the element around the horizontal axis, creating a 3D tilting effect. |
| Rotate (Y-axis) | Numeric input / range slider | Rotates the element around the vertical axis, creating a 3D turning effect. |
| Rotate (Z-axis) | Numeric input / range slider | Rotates the element on the flat plane, spinning it clockwise (positive) or counter-clockwise (negative). |
| Skew (Horizontal) | Numeric input | Slants the element along the horizontal axis, tilting it to the left or right. |
| Skew (Vertical) | Numeric input | Slants the element along the vertical axis, tilting it up or down. |
| Transform Origin | Grid selector / drag control | Sets the anchor point from which all transform effects are calculated. Common options include center, top-left, top-right, bottom-left, and bottom-right. |

## Which Elements Use This

The Transform options group is available on all Divi 5 modules and structural elements. It is especially popular for creating interactive hover effects on buttons, images, and cards, as well as for building angled or rotated section designs.

## Code Examples

Create a hover zoom effect on an image module:

```css
.image-module {
  transform: scale(1);
  transition: transform 0.3s ease;
}

.image-module:hover {
  transform: scale(1.05);
}
```

Tilt a card element in 3D space:

```css
.tilted-card {
  transform: perspective(800px) rotateY(-5deg);
  transform-origin: left center;
}
```

Skew a decorative background element:

```css
.skewed-bg {
  transform: skewY(-3deg);
  transform-origin: top left;
}
```

## Related

- [Filters Options](filters.md)
- [Animation Options](animation.md)
- [Position Options](position.md)
- [Transitions Options](transitions.md) — Animate transform changes on hover with duration and easing
- [Scroll Effects Options](scroll-effects.md) — Drive transforms based on scroll position
- [Interactions](../builder/interactions.md) — Trigger transforms on hover, click, or scroll events
