---
title: "Box Shadow Options"
description: "Divi 5 Box Shadow options group — shadow position, blur, spread, color, and inner/outer placement for depth effects on any element."
category: options-groups
tags: ["options-groups", "box-shadow", "design", "styling"]
related: ["border", "filters"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102594"
---

# Box Shadow Options

The Box Shadow options group adds and customizes shadow effects around Divi 5 elements to create depth and visual emphasis.

!!! abstract "Quick Reference"
    **What it controls:** Shadow horizontal/vertical position, blur, spread, color, and inner/outer placement
    **Where to find it:** Design Tab → Box Shadow
    **Available on:** All modules, sections, rows, and columns
    **Responsive:** Yes — shadow values can be configured per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102594)

## Overview

The Box Shadow options group lets you apply shadow effects to any element, simulating depth and elevation in your layouts. Shadows are one of the most effective ways to draw attention to specific content areas and create a sense of layering between elements on the page.

These controls are located in the Design tab of any element's settings panel under the Box Shadow group. You can configure the shadow's position, softness, spread, color, and whether it appears outside or inside the element's boundaries. Each property can be fine-tuned independently to achieve exactly the look you want.

For best results, use subtle shadow values with colors that complement your element's background. Overly dark or large shadows can feel heavy, while carefully calibrated shadows create a natural, professional sense of depth. Inside shadows (inset) produce a recessed effect, as if the element is pressed into the page, while outside shadows suggest the element is elevated above it.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102594).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Box Shadow Horizontal Position | Range slider | Controls the horizontal offset of the shadow. Positive values shift the shadow to the right, negative values shift it to the left. |
| Box Shadow Vertical Position | Range slider | Controls the vertical offset of the shadow. Positive values shift the shadow downward, negative values shift it upward. |
| Box Shadow Blur Strength | Range slider | Adjusts how soft or sharp the shadow edge appears. Higher values produce a wider, more diffused shadow. |
| Box Shadow Spread Strength | Range slider | Controls the size and density of the shadow. Positive values expand the shadow, negative values shrink it. |
| Shadow Color | Color picker | Sets the color of the shadow using the site palette or a custom color picker. |
| Box Shadow Position | Select toggle | Switches the shadow between an outer (outside) and inner (inset) position relative to the element. |

## Which Elements Use This

The Box Shadow options group is available on all Divi 5 modules and structural elements. Any element that renders as a visible box, including sections, rows, columns, and modules, can have box shadow effects applied.

## Code Examples

Apply a subtle elevation shadow to a card element:

```css
.card-module {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}
```

Create an inset shadow for a recessed appearance:

```css
.inset-module {
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.15);
}
```

Combine multiple shadows for a more natural depth effect:

```css
.elevated-module {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06),
              0 8px 24px rgba(0, 0, 0, 0.1);
}
```

## Related

- [Border Options](border.md)
- [Filters Options](filters.md)
- [Transform Options](transform.md) — Combine shadows with scale and translate for depth effects
- [Transitions Options](transitions.md) — Animate shadow changes on hover for interactive feedback
- [Blurb Module](../modules/blurb.md) — Feature cards commonly use box shadows for visual lift
