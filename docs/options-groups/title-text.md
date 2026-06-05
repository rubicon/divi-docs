---
title: "Title Text Options"
description: "Divi 5 Title Text options group — font, weight, size, color, alignment, heading level, and shadow controls for module titles."
category: options-groups
tags: ["options-groups", "title-text"]
related: ["body-text", "text", "closed-title-text"]
divi_version: "5.x"
last_updated: 2026-06-05
source_url: "https://help.elegantthemes.com/en/articles/10066965"
---

# Title Text Options

Controls the typography and visual appearance of module title elements throughout Divi 5.

!!! abstract "Quick Reference"
    **What it controls:** Font, weight, size, color, alignment, heading level (H1-H6), letter spacing, line height, and text shadow for titles
    **Where to find it:** Design Tab → Title Text
    **Available on:** Modules with headings (Accordion, Toggle, Blurb, CTA, Pricing Table, Slider, Tabs, and others)
    **Responsive:** Yes — all typography values can be set per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10066965)

## Overview

The Title Text options group provides a comprehensive set of typographic controls for styling module headings. Whenever a Divi 5 module displays a title, whether it is an Accordion header, a Blurb heading, or a Call to Action title, the Title Text settings determine how that heading looks.

These settings are found in the Design tab of the module settings panel. They allow you to adjust the font family, weight, size, color, alignment, spacing, and shadow of the title. You can also set the HTML heading level (H1 through H6), which affects both visual hierarchy and semantic markup for accessibility and SEO.

Title Text options integrate with Divi 5's responsive controls, so you can configure different values for desktop, tablet, and phone breakpoints independently. If you need distinct styling for open versus closed states in Accordion or Toggle modules, see the separate Closed Title Text options group.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10066965).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Title Text Color | Color picker | Sets the color of the title text. Supports site palette selection and custom color values. |
| Title Gradient Fill | Gradient picker | Fills title text with a gradient via the [Gradient Picker](../builder/gradient-builder.md); supports gradient variables (Divi 5.7+). |
| Title Image Fill | Image selector | Fills title glyphs with a background image (Divi 5.7+). |
| Title Text Stroke | Composite | Outlines title letterforms for contrast on busy backgrounds (Divi 5.7+). |
| Text Heading Level | Dropdown | Assigns the HTML heading tag (H1 through H6) for semantic structure and visual hierarchy. |
| Title Font | Font selector | Chooses the typeface for the title. Supports theme defaults and custom uploaded fonts. |
| Title Font Weight | Selector | Adjusts the boldness of the title text, ranging from light to extra-bold. |
| Title Font Style | Toggle options | Applies stylistic treatments including italics, capitalization, small caps, underline, and strikethrough. |
| Title Text Alignment | Alignment selector | Positions the title text as left-aligned, centered, right-aligned, or justified. |
| Title Text Size | Range slider / input | Sets the font size of the title using a slider or direct numeric entry. |
| Title Letter Spacing | Range slider / input | Controls the spacing between individual characters in the title. |
| Title Line Height | Range slider / input | Defines the vertical distance between lines of title text. |
| Title Text Shadow | Shadow editor | Adds a drop shadow to the title with controls for direction, blur radius, and shadow color. |

## Which Elements Use This

The Title Text options group appears in modules that display a heading or title element. Common examples include Accordion, Toggle, Blurb, Call to Action, Pricing Table, Slider, Post Title, Tabs, and many others. Any module with a configurable title will expose these settings in the Design tab.

## Code Examples

```css
/* Override title text styling for a specific module */
.my-custom-class .et_pb_module_header {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: 1px;
  color: #2d3436;
}
```

## Related

- [Body Text Options](body-text.md) -- Typography controls for body content areas
- [Closed Title Text Options](closed-title-text.md) -- Title styling for closed accordion/toggle states
- [Text Options](text.md) -- General text alignment and shadow for all module text
