---
title: "Content Options"
description: "Divi 5 Content options group — post type, count, category filters, date format, excerpt length, and offset for blog feeds."
category: options-groups
tags: ["options-groups", "content"]
related: ["elements", "meta"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10248683"
---

# Content Options

Configures the data source and display settings for blog feed modules, including post type, count, categories, and excerpt formatting.

!!! abstract "Quick Reference"
    **What it controls:** Post type, count, category filters, date format, excerpt length, and post offset
    **Where to find it:** Content Tab → Content
    **Available on:** Blog module
    **Responsive:** No — content query settings apply across all breakpoints
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10248683)

## Overview

The Content options group controls what content is pulled into a blog feed module and how that content is formatted. It determines which post type to display, how many posts to show, which categories to include, the date format, and how excerpts are generated and truncated.

These settings are found in the Content tab of the module settings panel. They work at the data level, determining what gets queried and how it is prepared for display. The Elements options group then controls which of these content components are visible on the front end, while the various typography groups handle their visual styling.

The post offset setting is particularly useful for layouts that feature a hero post separately from the main feed. By setting an offset, you can skip posts that are already displayed elsewhere on the page, avoiding duplicate content in your layouts.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10248683).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Post Type | Dropdown | Selects the content type to display: posts, pages, media, projects, products, or other registered types. |
| Post Count | Number input | Sets the number of posts to display per page in the feed. |
| Included Categories | Multi-select | Filters the feed to show posts from specific categories. All categories are included by default. |
| Date Format | Text input | Customizes the date display using PHP date format codes (e.g., "F j, Y" for "March 16, 2026"). |
| Content Length | Toggle | Switches between showing the post excerpt or the full post content in the feed. |
| Use Post Excerpts | Toggle | When enabled, uses manually written excerpts. When disabled, auto-generates excerpts from content. |
| Excerpt Length | Number input | Sets the character limit for auto-generated excerpts. Defaults to 270 characters. |
| Post Offset Number | Number input | Skips the specified number of posts before the feed begins (e.g., 3 means the feed starts with the 4th post). |

## Which Elements Use This

The Content options group is used by the Blog module in Divi 5. It provides the core data configuration for any module that displays a feed of posts or other content types.

## Code Examples

```php
// Example: Blog module with content settings configured
[et_pb_blog posts_number="6" include_categories="5,12" content_length="excerpt" use_manual_excerpt="on" excerpt_length="200" offset_number="1"]
```

## Related

- [Elements Options](elements.md) -- Visibility toggles for individual feed components
- [Meta Options](meta.md) -- Admin label and module metadata settings
