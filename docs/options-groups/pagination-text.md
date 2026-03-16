---
title: "Pagination Text Options"
category: options-groups
tags: ["options-groups", "pagination-text"]
related: ["meta-text", "title-text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10248789"
---

# Pagination Text Options

Controls the typography and appearance of pagination navigation links at the bottom of content feed modules.

## Overview

The Pagination Text options group provides design settings for the page navigation links that appear when a content feed spans multiple pages. These pagination links let visitors move between pages of posts, portfolio items, or other paginated content.

These settings are located in the Design tab of the module settings panel. They provide the standard set of typography controls: font family, weight, style, alignment, color, size, letter spacing, line height, and text shadow. This allows you to style pagination links consistently with the rest of your design.

Pagination text is often an afterthought in page design, but well-styled pagination links contribute to a polished user experience. Matching the font and color to your meta text or body text creates visual cohesion, while sufficient sizing and spacing ensures the links are easy to click on all devices.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10248789).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Pagination Font | Font selector | Selects the typeface for pagination links, supporting default and custom fonts. |
| Pagination Font Weight | Selector | Adjusts the boldness of pagination link text from light to extra-bold. |
| Pagination Font Style | Toggle options | Applies italics, capitalization, small caps, underline, or strikethrough to pagination text. |
| Pagination Text Alignment | Alignment selector | Positions the pagination text as left, center, right, or justified. |
| Pagination Text Color | Color picker | Sets the color of pagination links from the site palette or a custom value. |
| Pagination Text Size | Range slider / input | Defines the font size of the pagination text. |
| Pagination Letter Spacing | Range slider / input | Controls the spacing between characters in pagination links. |
| Pagination Line Height | Range slider / input | Sets the vertical distance between lines of pagination text. |
| Pagination Text Shadow | Shadow editor | Adds a shadow effect with controls for horizontal/vertical position, blur strength, and shadow color. |

## Which Elements Use This

The Pagination Text options group is used by modules that display paginated content feeds, primarily the Blog module and Portfolio module in Divi 5.

## Code Examples

```css
/* Style pagination links */
.et_pb_blog_grid .wp-pagenavi a,
.et_pb_blog_grid .wp-pagenavi span {
  font-size: 14px;
  font-weight: 500;
  color: #636e72;
}
```

## Related

- [Meta Text Options](meta-text.md) -- Typography controls for post metadata
- [Title Text Options](title-text.md) -- Typography controls for module titles
