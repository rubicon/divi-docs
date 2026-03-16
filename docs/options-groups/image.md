---
title: "Image Options"
description: "Divi 5 Image options group — border, rounded corners, box shadow, CSS filters, and blend mode controls for featured images."
category: options-groups
tags: ["options-groups", "image"]
related: ["image-icon", "overlay", "filters"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10248754"
---

# Image Options

Controls the border, shadow, and filter effects applied to featured images within Divi 5 modules.

!!! abstract "Quick Reference"
    **What it controls:** Image border, rounded corners, box shadow, CSS filters (hue, saturation, brightness, etc.), and blend mode
    **Where to find it:** Design Tab → Image
    **Available on:** Modules with featured images (Image, Blurb, Blog, Person, Testimonial, Portfolio, Gallery)
    **Responsive:** Yes — image styling values can be set per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10248754)

## Overview

The Image options group provides a comprehensive set of visual controls for featured images displayed by modules. It covers three key areas: border styling (rounded corners, width, color, style), box shadow effects (position, blur, spread, color), and CSS image filters (hue, saturation, brightness, contrast, and more).

These settings are found in the Design tab of the module settings panel. The border controls let you add rounded corners for a softer look, or apply distinct border styles to frame the image. Box shadow settings add depth with configurable offsets, blur, spread, and inner/outer positioning. The filter controls provide non-destructive color adjustments similar to photo editing tools.

The blend mode setting at the end of the filter controls determines how the image composites with elements behind it, offering creative options like multiply, screen, overlay, and more. Combined, these settings give you extensive creative control over image presentation without leaving the Visual Builder.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10248754).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Image Rounded Corners | Input / linked toggle | Sets corner radius values. Can apply uniformly or per-corner when unlinked. |
| Border Width | Input | Defines the thickness of the image border in pixels (minimum 1px). |
| Border Color | Color picker | Selects the color of the image border. |
| Border Style | Dropdown | Chooses the border style: solid, dashed, dotted, double, groove, ridge, inset, outset, or none. |
| Horizontal Position (Shadow) | Range slider | Moves the box shadow left or right relative to the image. |
| Vertical Position (Shadow) | Range slider | Moves the box shadow up or down relative to the image. |
| Blur Strength (Shadow) | Range slider | Controls how soft or sharp the shadow edge appears. |
| Spread Strength (Shadow) | Range slider | Expands or contracts the shadow area beyond the image edges. |
| Shadow Color | Color picker | Sets the color of the box shadow. |
| Box Shadow Position | Toggle | Switches the shadow between outer (outside the image) and inner (inset) placement. |
| Hue | Range slider | Shifts the overall color tone of the image. |
| Saturation | Range slider | Adjusts the vibrancy of image colors. |
| Brightness | Range slider | Makes the image lighter or darker. |
| Contrast | Range slider | Increases or decreases the difference between light and dark areas. |
| Invert | Toggle / slider | Reverses the image colors for a negative effect. |
| Sepia | Range slider | Applies a warm, vintage yellow-brown tone to the image. |
| Opacity | Range slider | Controls the transparency of the image. |
| Blur (Filter) | Range slider | Applies a Gaussian blur for a soft-focus effect. |
| Blend Mode | Dropdown | Determines how the image blends with underlying elements (normal, multiply, screen, overlay, etc.). |

## Which Elements Use This

The Image options group appears in modules that display featured images or visual content. Common examples include the Image module, Blurb, Blog, Person, Testimonial, Portfolio, Gallery, and Post Slider modules.

## Code Examples

```css
/* Apply image styling with CSS */
.et_pb_image img {
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  filter: brightness(1.05) contrast(1.1);
}
```

## Related

- [Image & Icon Options](image-icon.md) -- Placement, alignment, and styling for combined image/icon elements
- [Overlay Options](overlay.md) -- Hover overlay effects for featured images
- [Filters Options](filters.md) -- CSS filter controls available across all elements
