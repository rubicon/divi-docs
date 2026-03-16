---
title: "Filters Options"
description: "Divi 5 Filters options group — CSS filters for hue, saturation, brightness, contrast, blur, opacity, and blend mode on any element."
category: options-groups
tags: ["options-groups", "filters", "design", "styling"]
related: ["transform", "animation"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102602"
---

# Filters Options

The Filters options group applies visual effects such as color shifts, blur, and blending modes to any Divi 5 element.

!!! abstract "Quick Reference"
    **What it controls:** Hue, saturation, brightness, contrast, invert, sepia, opacity, blur, and blend mode
    **Where to find it:** Design Tab → Filters
    **Available on:** All modules, sections, rows, and columns
    **Responsive:** Yes — filter values can be configured per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102602)

## Overview

The Filters options group provides a set of CSS filter-based visual effects that can alter the appearance of any element without modifying its actual content. These effects include color adjustments like hue rotation, saturation, and brightness, as well as creative effects like blur, invert, and sepia toning.

These controls are found in the Design tab of any element's settings panel under the Filters group. Each filter is controlled by a range slider, making it easy to dial in the exact intensity you want. Filters are applied cumulatively, so you can combine multiple effects together to achieve complex visual treatments.

The Blend Mode setting at the bottom of the group determines how the filtered element visually interacts with elements behind it. This is especially powerful when layering elements on top of background images or colored sections, enabling effects similar to those found in image editing software.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102602).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Hue | Range slider | Rotates the color hue of the entire element by the specified angle in degrees. Shifts all colors uniformly around the color wheel. |
| Saturation | Range slider | Controls color intensity. Values above the default increase vibrancy, while lower values desaturate toward grayscale. |
| Brightness | Range slider | Adjusts overall lightness of the element. Higher values brighten; lower values darken. |
| Contrast | Range slider | Increases or decreases the distinction between light and dark areas within the element. |
| Invert | Range slider | Reverses the element's colors to their opposites. Partial values produce a mixed effect. |
| Sepia | Range slider | Applies a warm, brownish-yellow tone reminiscent of vintage photography. Intensity is adjustable. |
| Opacity | Range slider | Controls the transparency of the entire element. Lower values make the element more transparent. |
| Blur | Range slider | Applies a Gaussian blur effect to soften the element's visual output. Measured in pixels. |
| Blend Mode | Dropdown select | Determines how the element blends visually with elements behind it. Options include Normal, Multiply, Screen, Overlay, Darken, Lighten, Color Dodge, Color Burn, Hard Light, Soft Light, Difference, Exclusion, Hue, Saturation, Color, and Luminosity. |

## Which Elements Use This

The Filters options group is available on all Divi 5 modules and structural elements. It is commonly used on image-based modules for photo effects, on overlapping elements for blending, and on any module where you want to adjust visual appearance without modifying the underlying content.

## Code Examples

Create a grayscale effect that transitions to full color on hover:

```css
.my-module {
  filter: saturate(0%);
  transition: filter 0.3s ease;
}

.my-module:hover {
  filter: saturate(100%);
}
```

Apply a frosted glass effect using blur and opacity:

```css
.frosted-overlay {
  filter: blur(8px) brightness(110%);
  opacity: 0.9;
}
```

Use blend mode to create a duotone effect:

```css
.duotone-module {
  mix-blend-mode: multiply;
  background-color: #2ea3f2;
}
```

## Related

- [Transform Options](transform.md)
- [Animation Options](animation.md)
- [Transitions Options](transitions.md) — Animate filter changes on hover for interactive effects
- [Image Module](../modules/image.md) — Images commonly use brightness, contrast, and saturation filters
- [Gallery Module](../modules/gallery.md) — Apply filters to gallery images for visual consistency
