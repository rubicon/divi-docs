---
title: "Body Text Options"
description: "Divi 5 Body Text options group — text alignment and text shadow controls for paragraph and body content in modules."
category: options-groups
tags: ["options-groups", "body-text"]
related: ["title-text", "text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10101904"
---

# Body Text Options

Manages the typography and alignment of body content text within Divi 5 modules.

!!! abstract "Quick Reference"
    **What it controls:** Text alignment and text shadow for body/paragraph content areas
    **Where to find it:** Design Tab → Text (Body Text section)
    **Available on:** Modules with body content (Text, Blurb, CTA, Toggle, Accordion, Testimonial, and others)
    **Responsive:** Yes — alignment and shadow values can be set per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10101904)

## Overview

The Body Text options group (referred to as "Text" in some module panels) provides design controls that apply to the main content text area of a module. This includes paragraph text, list items, and any non-title text content rendered by the module.

These settings are located in the Design tab. They allow you to set a global text alignment for all text in the module, as well as apply a text shadow effect. While the general Text options group handles broad alignment and shadow, the Body Text group may provide additional font-level controls depending on the module context.

Body Text settings work alongside Title Text and Closed Title Text options. The general text settings act as a baseline, and the more specific typography groups (Title Text, Body Text) allow you to override individual aspects for their respective content areas.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10101904).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Text Alignment | Alignment selector | Sets horizontal alignment for all text in the module. Options include left, center, right, and justify. |
| Text Shadow | Toggle / shadow editor | Enables a drop shadow on all module text. When active, reveals sub-controls for customization. |
| Shadow Direction | Offset controls | Adjusts the horizontal and vertical offset of the text shadow. |
| Blur Strength | Range slider / input | Controls how sharp or soft the text shadow appears. Higher values create a more diffuse effect. |
| Shadow Color | Color picker | Sets the color of the text shadow. Supports site palette and custom color values. |

## Which Elements Use This

The Body Text options group applies to modules that contain body or paragraph content. It is commonly found in the Text module, Blurb, Call to Action, Toggle, Accordion, Testimonial, and other modules with descriptive text areas. The settings affect all non-title text within the module.

## Code Examples

```css
/* Customize body text appearance */
.my-module .et_pb_text_inner p {
  text-align: left;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.15);
}
```

## Related

- [Title Text Options](title-text.md) -- Typography controls for module titles
- [Text Options](text.md) -- General text alignment and shadow settings
