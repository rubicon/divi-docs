---
title: "Background Options"
category: options-groups
tags: ["options-groups", "background", "design", "styling"]
related: ["link", "meta"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10063358"
---

# Background Options

The Background options group provides fully responsive and customizable background styling for any Divi 5 element.

## Overview

The Background options group lets you apply rich visual backgrounds to sections, rows, columns, and modules throughout your Divi 5 layouts. It supports six distinct background types that can be combined and layered together using opacity and blending controls, giving you tremendous creative flexibility without writing any code.

You will find the Background options within the Design tab of any element's settings panel. Each background type has its own sub-tab, and you can switch between them to configure colors, gradients, images, videos, patterns, and masks independently. All background settings support responsive device toggling, so you can tailor the appearance for desktop, tablet, and mobile views separately.

One of the most powerful aspects of the Background options group is the ability to layer multiple background types simultaneously. For example, you can set a background color, overlay a semi-transparent gradient, and add a pattern on top, all on the same element. Blending modes and opacity controls on images and patterns enable sophisticated visual compositions.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10063358).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Background Color | Color picker | Applies a solid color fill to the element background. Supports opacity adjustment and can be layered beneath other background types. |
| Background Gradient | Gradient editor | Creates a custom gradient background with configurable direction, type (linear or radial), color stops, and positioning. |
| Background Image | File upload / image selector | Lets you upload or select an image for the background. Includes controls for position, size, repeat behavior, blend mode, and parallax scrolling. |
| Background Video | File upload / URL input | Embeds a video as the element background by uploading a file or providing a URL. |
| Background Pattern | Pattern selector | Applies a decorative repeating pattern from a library of built-in options. Includes controls for color, opacity, size, and blend mode. |
| Background Mask | Shape selector | Adds a custom shape or overlay mask to the background. Provides controls for color, size, aspect ratio, and orientation. |

## Which Elements Use This

The Background options group is available on every structural and content element in Divi 5, including sections, rows, columns, and all modules. Any element that occupies space on the page can have a customized background applied through this options group.

## Code Examples

Apply a semi-transparent gradient overlay on top of a background image using custom CSS:

```css
.my-element {
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.2)),
              url('image.jpg') center/cover no-repeat;
}
```

Force a parallax-style fixed background on a section:

```css
.et-db .my-section {
  background-attachment: fixed;
  background-size: cover;
}
```

## Related

- [Link Options](link.md)
- [Meta Options](meta.md)
