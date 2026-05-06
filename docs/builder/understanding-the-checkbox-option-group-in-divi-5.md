---
title: "Understanding the Checkbox Option Group in Divi 5"
category: builder
tags: ["builder", "options-groups", "checkbox", "form-fields", "design"]
related: ["composable-settings", "understanding-the-fields-option-group-in-divi-5", "understanding-the-radio-option-group-in-divi-5"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14717695-understanding-the-checkbox-option-group-in-divi-5"
---

# Understanding the Checkbox Option Group in Divi 5

The **Checkbox** design options control how checkbox inputs look inside Divi 5 modules that include them. These settings cover the typography of the checkbox option text, the check icon itself, spacing, background, border, and box shadow for the checkbox container.

## Overview

![Checkbox Option Group overview](../assets/screenshots/builder/checkbox-option-group/overview.png){ loading=lazy }

## Where to Find the Checkbox Options

1. **Open the Module Settings**: Click the gear icon or the module itself to access its settings.
2. **Navigate to the Design Tab**: Locate the **Checkbox** option group.

## Settings & Options

### Input Text

Controls the typography of the text that appears next to each checkbox option.

| Setting | Type | Description |
|---------|------|-------------|
| Fields Font | Font selection | Choose a font from the Google Fonts library or upload a custom font. |
| Fields Font Weight | Weight selector | Set the weight from thin, light, regular, bold, and every weight in between. |
| Fields Font Style | Style options | Apply italic, uppercase, capitalize, underline, or strikethrough. |
| Fields Text Alignment | Alignment | Align text left, center, right, or justify. |
| Fields Text Color | Color picker | Pick a static color or assign a global color variable for sitewide consistency. |
| Fields Text Size | Unit input | Set the font size using any supported unit (px, em, rem, %, vw, vh, and more). |
| Fields Letter Spacing | Slider | Increase or decrease the space between characters. |
| Fields Line Height | Slider | Adjust vertical spacing between lines of text. |
| Fields Text Shadow | Shadow controls | Add a shadow behind the option text with control over horizontal position, vertical position, blur strength, and color. |

### Spacing

Controls the space around and inside each checkbox.

| Setting | Type | Description |
|---------|------|-------------|
| Fields Margin | Spacing control | Add space outside the checkbox on the top, right, bottom, and left. Click the chainlink icon to lock opposing sides together for uniform spacing. |
| Fields Padding | Spacing control | Add space inside the checkbox (between the icon and the checkbox edges) on the top, right, bottom, and left. Click the chainlink icon to lock opposing sides together for uniform spacing. |

### Icon

Controls the check indicator that appears inside a ticked checkbox.

| Setting | Type | Description |
|---------|------|-------------|
| Fields Icon Color | Color picker | Set the color of the check icon. Pick a static color or assign a global color variable. |
| Field Icon | Icon selector | Choose the icon shown when a checkbox is ticked. Select from the ET icon library or the Font Awesome library. |
| Use Custom Field Icon Size | Toggle | Toggle on to override the default icon size. When enabled, a size slider appears so you can set a custom value using any supported unit. |

### Background

Controls the appearance of the checkbox background. Divi 5 offers six background types, each available as its own tab. You can combine them (for example, a color base with a pattern on top).

| Setting | Type | Description |
|---------|------|-------------|
| Background Color | Color fill | Apply a solid color fill. |
| Background Gradient | Gradient | Apply a multi-stop gradient with control over direction, type (linear or radial), and color stops. |
| Background Image | Image upload | Upload or link an image and adjust size, position, repeat, and blend mode. |
| Background Video | Video embed | Embed an MP4 or WebM video as a looping background. |
| Background Mask | Mask shape | Apply a pre-built mask shape over the background for layered visual effects. |
| Background Pattern | Pattern overlay | Overlay a repeating pattern on top of the background. |

### Border

Controls the shape and edge of the checkbox container.

| Setting | Type | Description |
|---------|------|-------------|
| Fields Rounded Corners | Corner radius | Set the corner radius. Keep the chainlink icon locked for uniform corners or unlink it to round each corner independently. |
| Border Width | Pixel input | Define the border thickness (minimum `1px`). |
| Border Color | Color picker | Pick a static color or assign a global color variable. |
| Border Style | Dropdown | Choose solid, dashed, dotted, double, groove, ridge, inset, outset, or none. |

### Box Shadow

Adds a drop shadow around the checkbox container to create depth. Pick from a library of preset shadow styles, or customize each property manually.

| Setting | Type | Description |
|---------|------|-------------|
| Horizontal Position | Slider | Move the shadow left or right of the checkbox. |
| Vertical Position | Slider | Move the shadow up or down from the checkbox. |
| Blur Strength | Slider | Soften or sharpen the shadow edges. |
| Spread Strength | Slider | Expand or contract the shadow's reach. |
| Shadow Color | Color picker | Pick a static color or assign a global color variable. |

## Tips for Using Checkbox Options

- **Match Form Typography**: Keep **Input Text** font, weight, and size consistent with the rest of your form fields so checkboxes read as part of the same group.
- **Use Global Colors**: Assign global color variables to **Fields Icon Color** and **Border Color** so sitewide palette changes update checkboxes automatically.
- **Size Icons Proportionally**: When enabling **Use Custom Field Icon Size**, keep the icon smaller than the checkbox container so it sits cleanly inside the box.
- **Pick a Clear Check Icon**: Choose a simple, recognizable icon from the ET or Font Awesome libraries. Complex icons can feel cluttered at small sizes.
- **Keep Tap Targets Generous**: Use **Fields Padding** and **Fields Margin** to give checkboxes enough space for easy tapping on mobile devices.
- **Ensure Contrast**: Check that the icon color contrasts clearly with the checkbox background so the ticked state is obvious at a glance.

## Related

- [Composable Settings in Divi 5](composable-settings-in-divi-5.md)
- [Understanding the Fields Option Group in Divi 5](understanding-the-fields-option-group-in-divi-5.md)
- [Understanding the Radio Option Group in Divi 5](understanding-the-radio-option-group-in-divi-5.md)

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.
