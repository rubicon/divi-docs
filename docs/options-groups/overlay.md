---
title: "Overlay Options"
category: options-groups
tags: ["options-groups", "overlay"]
related: ["image", "filters"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10248734"
---

# Overlay Options

Controls the hover overlay effect on featured images, including background color and icon display.

## Overview

The Overlay options group lets you add an interactive hover effect to featured images in your modules. When enabled, hovering over an image reveals a colored overlay with an optional icon, providing a visual cue that the image is clickable or interactive.

These settings are found in the Design tab of the module settings panel. The master toggle enables or disables the overlay effect entirely. Once enabled, you can customize the overlay background color, the icon that appears, and the icon color. Setting the icon color to fully transparent effectively hides the icon while keeping the background overlay visible.

Overlay effects are a common design pattern for portfolio grids, blog post thumbnails, and gallery layouts. They signal interactivity, draw attention to linked content, and add a layer of polish to image-heavy designs. The Divi icon library provides a wide range of choices for the overlay icon, from arrows and links to search and zoom symbols.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10248734).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Featured Image Overlay | Toggle | Enables or disables the hover overlay effect on the featured image. |
| Overlay Icon Color | Color picker | Sets the color of the icon displayed on hover. Setting to transparent hides the icon. |
| Overlay Background Color | Color picker | Sets the background color of the overlay that appears on hover. |
| Overlay Icon | Icon picker | Selects which icon from the Divi library is displayed during the hover state. |

## Which Elements Use This

The Overlay options group is used by modules that display featured images with hover interactions. Common examples include the Blog module, Portfolio module, Filterable Portfolio, and Gallery module in Divi 5.

## Code Examples

```css
/* Custom overlay styling */
.et_overlay {
  background-color: rgba(108, 92, 231, 0.8);
}

.et_overlay::before {
  color: #ffffff;
  font-size: 32px;
}
```

## Related

- [Image Options](image.md) -- Border, shadow, and filter settings for featured images
- [Filters Options](filters.md) -- CSS filter controls for visual adjustments
