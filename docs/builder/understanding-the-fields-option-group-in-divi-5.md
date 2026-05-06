---
title: "Understanding the Fields Option Group in Divi 5"
category: builder
tags: ["builder", "options-groups", "fields", "form-fields", "design"]
related: ["composable-settings", "contact-form", "new-form-field-options"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/10260887-understanding-the-fields-option-group-in-divi-5"
---

# Understanding the Fields Option Group in Divi 5

The **Fields** design options control how form fields look inside Divi 5 modules that include user inputs. These settings cover typography for input, label, and placeholder text, plus spacing, background, border, and box shadow controls for the field container.

## Overview

![Fields Option Group overview](../assets/screenshots/builder/fields-option-group/overview.png){ loading=lazy }

## Where to Find the Fields Options

1. **Open the Comments Module Settings**: Click the gear icon or the module itself to access the settings.
2. **Navigate to the Design Tab**: Locate the **Fields** option group.

## Settings & Options

### Input Text

Controls the typography of the text users type into form fields.

| Setting | Type | Description |
|---------|------|-------------|
| Fields Font | Font selection | Choose a font from the Google Fonts library or upload a custom font. |
| Fields Font Weight | Weight selector | Set the weight from thin, light, regular, bold, and every weight in between. |
| Fields Font Style | Style options | Apply italic, uppercase, capitalize, underline, or strikethrough. |
| Fields Text Alignment | Alignment | Align text left, center, right, or justify. |
| Fields Text Color | Color picker | Pick a static color or assign a **[global color variable](https://help.elegantthemes.com/en/articles/13348842-global-variables-in-divi-5)** for sitewide consistency. |
| Fields Text Size | Unit input | Set the font size using any **[supported unit](https://help.elegantthemes.com/en/articles/10823890-advanced-units-css-functions-and-variables-for-divi-5)** (px, em, rem, %, vw, vh, and more). |
| Fields Letter Spacing | Slider | Increase or decrease the space between characters. |
| Fields Line Height | Slider | Adjust vertical spacing between lines of text. |
| Fields Text Shadow | Shadow controls | Add a shadow behind input text with control over horizontal position, vertical position, blur strength, and color. |

### Label Text

Controls the typography of field labels (the descriptive words that identify each field, like "Name" or "Email").

| Setting | Type | Description |
|---------|------|-------------|
| Label Font | Font selection | Choose a font from Google Fonts or upload a custom font. |
| Label Font Weight | Weight selector | Set the weight from thin to bold. |
| Label Font Style | Style options | Apply italic, uppercase, capitalize, underline, or strikethrough. |
| Label Text Alignment | Alignment | Align text left, center, right, or justify. |
| Label Text Color | Color picker | Pick a static color or assign a **[global color variable](https://help.elegantthemes.com/en/articles/13348842-global-variables-in-divi-5)**. |
| Label Text Size | Unit input | Set the font size using any **[supported unit](https://help.elegantthemes.com/en/articles/10823890-advanced-units-css-functions-and-variables-for-divi-5)**. |
| Label Letter Spacing | Slider | Adjust the space between characters. |
| Label Line Height | Slider | Adjust vertical spacing between lines. |
| Label Text Shadow | Shadow controls | Add a shadow behind label text with control over position, blur, and color. |

### Placeholder Text

Controls the typography of placeholder text (the faded hint text that appears inside an empty field, like "Enter your email address").

| Setting | Type | Description |
|---------|------|-------------|
| Placeholder Font | Font selection | Choose a font from Google Fonts or upload a custom font. |
| Placeholder Font Weight | Weight selector | Set the weight from thin to bold. |
| Placeholder Font Style | Style options | Apply italic, uppercase, capitalize, underline, or strikethrough. |
| Placeholder Text Alignment | Alignment | Align text left, center, right, or justify. |
| Placeholder Text Color | Color picker | Pick a static color or assign a global color variable. |
| Placeholder Text Size | Unit input | Set the font size using any supported unit. |
| Placeholder Letter Spacing | Slider | Adjust the space between characters. |
| Placeholder Line Height | Slider | Adjust vertical spacing between lines. |
| Placeholder Text Shadow | Shadow controls | Add a shadow behind placeholder text with control over position, blur, and color. |

### Spacing

Controls the space around and inside field containers.

| Setting | Type | Description |
|---------|------|-------------|
| Fields Margin | Spacing control | Add space outside the field on the top, right, bottom, and left. Click the chainlink icon to lock opposing sides together for uniform spacing. |
| Fields Padding | Spacing control | Add space inside the field (between the text and the field edges) on the top, right, bottom, and left. Click the chainlink icon to lock opposing sides together for uniform spacing. |

### Background

Controls the appearance of the field background. Divi 5 offers six background types, each available as its own tab. You can combine them (for example, a color base with an image overlay and a pattern on top).

| Setting | Type | Description |
|---------|------|-------------|
| Background Color | Color fill | Apply a solid color fill. |
| Background Gradient | Gradient | Apply a multi-stop gradient with control over direction, type (linear or radial), and color stops. |
| Background Image | Image upload | Upload or link an image and adjust size, position, repeat, and blend mode. |
| Background Video | Video embed | Embed an MP4 or WebM video as a looping background. |
| Background Mask | Mask shape | Apply a pre-built mask shape over the background for layered visual effects. |
| Background Pattern | Pattern overlay | Overlay a repeating pattern on top of the background. |

### Border

Controls the shape and edge of the field container.

| Setting | Type | Description |
|---------|------|-------------|
| Fields Rounded Corners | Corner radius | Set the corner radius. Keep the chainlink icon locked for uniform corners or unlink it to round each corner independently. |
| Border Width | Pixel input | Define the border thickness (minimum `1px`). |
| Border Color | Color picker | Pick a static color or assign a global color variable. |
| Border Style | Dropdown | Choose solid, dashed, dotted, double, groove, ridge, inset, outset, or none. |

### Box Shadow

Adds a drop shadow around the field container to create depth. Pick from a library of preset shadow styles, or customize each property manually.

| Setting | Type | Description |
|---------|------|-------------|
| Horizontal Position | Slider | Move the shadow left or right of the field. |
| Vertical Position | Slider | Move the shadow up or down from the field. |
| Blur Strength | Slider | Soften or sharpen the shadow edges. |
| Spread Strength | Slider | Expand or contract the shadow's reach. |
| Shadow Color | Color picker | Pick a static color or assign a global color variable. |

## Tips for Using Fields Options

- **Match Site Typography**: Keep **Input Text**, **Label Text**, and **Placeholder Text** fonts consistent with the rest of your site for a cohesive look.
- **Use Global Colors**: Assign global color variables to **Text Color** and **Border Color** so sitewide palette changes update fields automatically.
- **Keep Placeholders Subtle**: Use a lighter color and reduced weight for **Placeholder Text** so it reads as a hint rather than entered content.
- **Ensure Contrast**: Check that text, placeholder, and background colors meet accessibility contrast standards for readability.
- **Add Depth Sparingly**: Use **Box Shadow** and **Text Shadow** in moderation. Subtle shadows feel polished, heavy ones feel dated.

## Related

- [Composable Settings in Divi 5](composable-settings-in-divi-5.md)
- [Contact Form Module in Divi 5](../modules/contact-form.md)
- [New Form Field Options](new-form-field-options-in-divi-5.md)

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.
