---
title: "Image & Icon Options"
description: "Divi 5 Image & Icon options group — placement, alignment, border, shadow, and filter controls for combined image/icon elements."
category: options-groups
tags: ["options-groups", "image-icon"]
related: ["image", "button"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10259617"
---

# Image & Icon Options

Controls the placement, alignment, border, shadow, and filter effects for combined image and icon elements within Divi 5 modules.

!!! abstract "Quick Reference"
    **What it controls:** Image/icon placement (top/left), alignment, border, box shadow, CSS filters, and blend mode
    **Where to find it:** Design Tab → Image & Icon
    **Available on:** Blurb module (primarily)
    **Responsive:** Yes — layout and styling values can be set per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10259617)

## Overview

The Image & Icon options group provides layout and styling controls for modules that display an image or icon as a key visual element alongside text content. It extends the standard image styling with placement and alignment settings that determine where the visual element appears relative to the module content.

These settings are found in the Design tab of the module settings panel. The placement control lets you position the image or icon above (Top) or beside (Left) the text content. When placement is set to Top, an additional alignment control appears for horizontal positioning. Beyond layout, the group provides the same border, shadow, and filter controls found in the standard Image options group.

The filter controls (hue, saturation, brightness, contrast, invert, sepia, opacity, blur) and blend mode options let you apply non-destructive visual adjustments directly within the builder. This is particularly useful for creating consistent visual treatments across a set of blurbs or feature boxes.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10259617).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Image/Icon Placement | Dropdown | Positions the image or icon relative to content: Top or Left. |
| Image/Icon Alignment | Dropdown | Sets horizontal alignment (Left, Center, Right) when placement is Top. |
| Image Rounded Corners | Input / linked toggle | Sets corner radius values, uniformly or per-corner when unlinked. |
| Border Width | Input | Defines border thickness in pixels (minimum 1px). |
| Border Color | Color picker | Selects the border color. |
| Border Style | Dropdown | Chooses border style: solid, dashed, dotted, double, groove, ridge, inset, outset, or none. |
| Horizontal Position (Shadow) | Input | Sets the horizontal offset of the box shadow. |
| Vertical Position (Shadow) | Input | Sets the vertical offset of the box shadow. |
| Blur Strength (Shadow) | Input | Controls shadow softness. |
| Spread Strength (Shadow) | Input | Expands or contracts the shadow area. |
| Shadow Color | Color picker | Sets the box shadow color. |
| Box Shadow Position | Dropdown | Switches between inner and outer shadow placement. |
| Hue | Range slider | Shifts the color tone of the image. |
| Saturation | Range slider | Adjusts color vibrancy. |
| Brightness | Range slider | Makes the image lighter or darker. |
| Contrast | Range slider | Controls the difference between light and dark areas. |
| Invert | Toggle / slider | Reverses image colors. |
| Sepia | Range slider | Applies a vintage warm tone. |
| Opacity | Range slider | Controls image transparency. |
| Blur (Filter) | Range slider | Applies a Gaussian blur effect. |
| Blend Mode | Dropdown | Determines how the image blends with underlying elements. |

## Which Elements Use This

The Image & Icon options group is primarily used by the Blurb module in Divi 5, which displays an image or icon alongside a title and description. It may also appear in other modules that combine visual elements with text content.

## Code Examples

```css
/* Position blurb icon to the left with custom styling */
.et_pb_blurb .et_pb_main_blurb_image {
  margin-right: 20px;
}

.et_pb_blurb .et_pb_main_blurb_image img {
  border-radius: 50%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
}
```

## Related

- [Image Options](image.md) -- Border, shadow, and filter settings for standalone images
- [Button Options](button.md) -- Styling controls for button elements
