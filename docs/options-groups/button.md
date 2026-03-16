---
title: "Button Options"
category: options-groups
tags: ["options-groups", "button"]
related: ["text", "link"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10259854"
---

# Button Options

Provides comprehensive styling controls for button elements within Divi 5 modules, covering background, text, border, and icon settings.

## Overview

The Button options group is one of the most feature-rich options groups in Divi 5. It lets you fully customize the appearance of buttons rendered by modules, from background fills and gradients to typography, borders, and icon placement. A master toggle enables or disables custom styling, giving you the choice between global button defaults and per-module overrides.

These settings appear in the Design tab of any module that includes a button element. The group is organized into logical sub-sections: background (color, gradient, image, video, pattern, and mask), text (font, weight, style, color, size, spacing, shadow), border (radius, width, color, style), and icon (visibility, selection, color, placement, hover behavior).

The layered background system mirrors what is available in the standard Background options group, so you can create visually rich buttons with gradient overlays, image fills, or even video backgrounds. Combined with the border radius and shadow controls, this provides complete creative freedom for button design without custom CSS.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10259854).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Use Custom Styles For Button | Toggle | Enables or disables per-module button styling. When off, global defaults apply. |
| Background Color | Color picker | Applies a solid fill to the button background with opacity support. |
| Background Gradient | Gradient editor | Creates a linear or radial gradient background with configurable direction and color stops. |
| Background Image | File upload / selector | Sets an image as the button background with position, size, and repeat options. |
| Background Video | File upload / URL | Embeds a video background within the button area. |
| Background Pattern | Pattern selector | Applies a repeating decorative pattern with opacity and size controls. |
| Background Mask | Mask selector | Adds a shape overlay with color, size, and orientation settings. |
| Button Border Radius | Range slider / input | Controls the corner rounding of the button. |
| Button Border Styles | Border editor | Sets the border width, color, and style (solid, dashed, dotted, etc.). |
| Button Font | Font selector | Chooses the typeface for button text, supporting default and custom fonts. |
| Button Font Weight | Selector | Adjusts the boldness of button text from light to extra-bold. |
| Button Font Style | Toggle options | Applies italics, capitalization, small caps, underline, or strikethrough. |
| Button Text Color | Color picker | Sets the color of the button label text. |
| Button Text Size | Range slider / input | Defines the font size of the button text. |
| Button Letter Spacing | Range slider / input | Controls the spacing between characters in the button text. |
| Button Line Height | Range slider / input | Sets the vertical spacing between lines of button text. |
| Button Text Shadow | Shadow editor | Adds a shadow effect to the button text with position, blur, and color controls. |
| Show Button Icon | Toggle | Enables or disables the display of an icon within the button. |
| Button Icon | Icon picker | Selects the icon to display from the Divi icon library. |
| Button Icon Color | Color picker | Sets the color of the button icon. |
| Button Icon Placement | Selector | Positions the icon to the left or right of the button text. |
| Only Show Icon On Hover For Button | Toggle | When enabled, the icon only appears when the user hovers over the button. Enabled by default. |

## Which Elements Use This

The Button options group appears in any module that renders a clickable button. Common examples include the Button module, Call to Action, Pricing Table, Contact Form, Email Optin, Login, Slider, Fullwidth Header, and Audio module. Each module may expose one or more button groups depending on how many buttons it supports.

## Code Examples

```css
/* Custom button styling */
.et_pb_button {
  background-color: #6c5ce7;
  color: #ffffff;
  border-radius: 30px;
  padding: 12px 28px;
  font-weight: 600;
  letter-spacing: 1px;
}

.et_pb_button:hover {
  background-color: #5a4bd1;
}
```

## Related

- [Text Options](text.md) -- General text alignment and shadow settings
- [Link Options](link.md) -- URL and link target configuration
