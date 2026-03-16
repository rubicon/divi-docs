---
title: "Heading Text Options"
category: options-groups
tags: ["options-groups", "heading-text"]
related: ["title-text", "text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10365216"
---

# Heading Text Options

Provides full typographic control over heading elements within Divi 5 modules.

## Overview

The Heading Text options group lets you customize the styling of heading elements in your designs. It controls the typeface, weight, size, color, alignment, spacing, and shadow of headings, and allows you to assign an appropriate HTML heading level (H1 through H6) for proper document structure.

These settings appear in the Design tab of the module settings panel. They give you granular control over how headings render on the page, ensuring that your typographic choices align with your overall site design and branding. Heading levels also play an important role in accessibility and search engine optimization by establishing content hierarchy.

All heading text settings are responsive, meaning you can configure unique values for each device breakpoint. This ensures your headings look appropriate at every screen size without needing custom CSS.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10365216).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Heading Level | Dropdown | Assigns an HTML heading tag (H1 through H6) for semantic structure. |
| Heading Font | Font selector | Chooses the typeface for the heading, supporting theme defaults and custom fonts. |
| Heading Font Weight | Selector | Adjusts the heading boldness from light to extra-bold. |
| Heading Font Style | Toggle options | Applies stylistic treatments including italics, capitalization, small caps, underline, and strikethrough. |
| Heading Text Alignment | Alignment selector | Sets the horizontal position of the heading: left, center, right, or justified. |
| Heading Text Color | Color picker | Selects the color for the heading text from the site palette or a custom value. |
| Heading Text Size | Range slider / input | Defines the font size of the heading. |
| Heading Letter Spacing | Range slider / input | Controls the spacing between characters in the heading. |
| Heading Line Height | Range slider / input | Sets the vertical spacing between lines of heading text. |
| Heading Text Shadow | Shadow editor | Adds a drop shadow effect with configurable direction, blur radius, and color. |

## Which Elements Use This

The Heading Text options group appears in modules that render configurable heading content. It functions as a reusable typography component across Divi 5 design modules wherever dedicated heading styling is required.

## Code Examples

```css
/* Custom heading text overrides */
.my-section h2 {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  letter-spacing: -0.5px;
  color: #1a1a2e;
}
```

## Related

- [Title Text Options](title-text.md) -- Typography controls for module title elements
- [Text Options](text.md) -- General text alignment and shadow settings
