---
title: "Text Options"
description: "Divi 5 Text options group — font selection, size, weight, color, alignment, letter spacing, line height, and text shadow controls."
category: options-groups
tags: ["options-groups", "text", "design", "styling"]
related: ["title-text", "body-text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102451"
---

# Text Options

The Text options group controls the typographic appearance of body content within text-based Divi 5 modules.

!!! abstract "Quick Reference"
    **What it controls:** Font family, weight, style, size, color, alignment, letter spacing, line height, and text shadow
    **Where to find it:** Design Tab → Text
    **Available on:** Text-based modules (Text, Accordion, Blurb, CTA, and others with body content)
    **Responsive:** Yes — all typography values can be set per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102451)

## Overview

The Text options group provides comprehensive typography controls for styling the body text content of modules. These settings affect how text renders visually, covering everything from font selection and sizing to letter spacing, line height, and text shadows.

You will find the Text controls in the Design tab of any text-based module's settings panel. The group typically includes a font selector, weight and style controls, alignment options, color picker, and fine-tuning controls for size, spacing, and line height. A text shadow sub-group is also available for adding depth to your typography.

These options control the default body text styling for the module. Many modules also expose separate typography groups for specific text elements like titles, meta text, or button labels, which override these base text settings for their respective content areas.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102451).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Font | Dropdown / custom upload | Selects the typeface for the body text. Defaults to the site's primary font if not specified. Supports uploading custom font files. |
| Font Weight | Select | Adjusts the boldness of the text, ranging from light to extra-bold weight values. |
| Font Style | Multi-select toggles | Applies stylistic treatments including italic, uppercase, underline, and strikethrough. Multiple styles can be combined. |
| Text Alignment | Button group | Sets the horizontal alignment of text content: left, center, right, or justified. |
| Text Color | Color picker | Defines the color of the body text using the site palette or a custom color value. |
| Text Size | Range slider / text input | Controls the font size of the body text. Accepts values in px, em, rem, and other CSS units. |
| Letter Spacing | Range slider / text input | Adjusts the horizontal space between individual characters. Higher values spread characters further apart. |
| Line Height | Range slider / text input | Sets the vertical distance between lines of text, affecting readability and visual density. |
| Text Shadow Horizontal Position | Range slider | Controls the horizontal offset of the text shadow effect. |
| Text Shadow Vertical Position | Range slider | Controls the vertical offset of the text shadow effect. |
| Text Shadow Blur Strength | Range slider | Adjusts the softness of the text shadow. Higher values create a more diffused shadow. |
| Text Shadow Color | Color picker | Sets the color of the text shadow effect. |

## Which Elements Use This

The Text options group appears on text-based Divi 5 modules that render body content. Common modules that include these controls are the Text module, Accordion, Audio, Blurb, Call to Action, and other modules that display descriptive body text. Modules without body text content may not expose this options group.

## Code Examples

Apply custom typography to a module's body text:

```css
.my-module p {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  line-height: 1.7;
  letter-spacing: 0.02em;
  color: #444444;
}
```

Add a subtle text shadow for visual depth:

```css
.my-module p {
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}
```

## Related

- [Title Text Options](title-text.md)
- [Body Text Options](body-text.md)
- [Heading Text Options](heading-text.md) — Typography settings specific to heading elements
- [Text Module](../modules/text.md) — The primary rich text content module
- [Heading Module](../modules/heading.md) — Standalone heading element with text styling controls
- [Design Variables](../builder/design-variables.md) — Define reusable typography values across your site
