---
title: "Meta Text Options"
category: options-groups
tags: ["options-groups", "meta-text"]
related: ["title-text", "body-text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10248762"
---

# Meta Text Options

Controls the typography and appearance of post metadata elements such as author name, date, categories, and comment count.

## Overview

The Meta Text options group provides typographic styling for metadata displayed alongside blog posts and similar content. Metadata includes the author name, publication date, assigned categories, and comment count that typically appear near the post title or below the excerpt.

These settings are located in the Design tab. They let you choose a font, weight, size, color, and alignment for all metadata text, ensuring it visually complements your title and body typography without competing for attention. Letter spacing, line height, and text shadow settings offer additional refinement.

Meta text styling is especially important for blog layouts where metadata helps readers quickly scan content attributes. By styling meta text distinctly from body and title text, you can establish a clear visual hierarchy that makes your content easier to navigate.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10248762).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Meta Font | Font selector | Selects the typeface for metadata text, supporting default and custom fonts. |
| Meta Font Weight | Selector | Adjusts the boldness of metadata text from light to extra-bold. |
| Meta Font Style | Toggle options | Applies italics, capitalization, small caps, underline, or strikethrough to metadata text. |
| Meta Text Alignment | Alignment selector | Positions metadata text as left, center, right, or justified. |
| Meta Text Color | Color picker | Sets the color of metadata text from the site palette or a custom value. |
| Meta Text Size | Range slider / input | Defines the font size of the metadata text. |
| Meta Letter Spacing | Range slider / input | Controls the spacing between characters in metadata text. |
| Meta Line Height | Range slider / input | Sets the vertical distance between lines of metadata text. |
| Meta Text Shadow | Shadow editor | Adds a shadow effect with controls for horizontal/vertical position, blur strength, and shadow color. |

## Which Elements Use This

The Meta Text options group is used by modules that display post metadata. This primarily includes the Blog module, Portfolio module, and Post Title module, where author, date, category, and comment count information accompanies the post content.

## Code Examples

```css
/* Style post meta text */
.et_pb_post_meta {
  font-size: 13px;
  color: #999;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
```

## Related

- [Title Text Options](title-text.md) -- Typography controls for post titles
- [Body Text Options](body-text.md) -- Typography controls for post body content
