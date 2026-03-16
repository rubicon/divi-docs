---
title: "Elements Options"
description: "Divi 5 Elements options group — toggle switches for featured image, author, date, categories, excerpt, and pagination visibility."
category: options-groups
tags: ["options-groups", "elements"]
related: ["content", "meta"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10248725"
---

# Elements Options

Controls which content components are visible in blog feed and similar listing modules through a set of toggle switches.

!!! abstract "Quick Reference"
    **What it controls:** Visibility toggles for featured image, Read More button, author, date, categories, comment count, excerpt, and pagination
    **Where to find it:** Content Tab → Elements
    **Available on:** Blog module (and similar content listing modules)
    **Responsive:** No — element visibility applies across all breakpoints
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10248725)

## Overview

The Elements options group provides a collection of on/off toggles that determine which parts of a post listing are displayed. Each toggle controls the visibility of a specific content component: featured image, read more button, author name, date, categories, comment count, excerpt, and pagination.

These settings are found in the Content tab of the module settings panel. They give you quick control over what information appears for each post in a feed without affecting the underlying data. Disabling a toggle simply hides that element from the front-end display.

This options group is essential for tailoring blog feed layouts to different contexts. A minimal listing might show only the title and date, while a full-featured layout might enable all elements. The toggles work in conjunction with the Content options group (which controls data sources and formatting) and the various typography groups (which control how visible elements are styled).

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10248725).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Show Featured Image | Toggle | Controls whether the featured image is displayed for each post in the feed. |
| Show Read More Button | Toggle | Controls whether a "Read More" button appears below each post excerpt. |
| Show Author | Toggle | Controls whether the post author name is displayed in the metadata area. |
| Show Date | Toggle | Controls whether the publication date is shown in the metadata area. |
| Show Categories | Toggle | Controls whether post categories appear in the metadata area. |
| Show Comment Count | Toggle | Controls whether the comment count is displayed in the metadata area. |
| Show Excerpt | Toggle | Controls whether the post excerpt text is shown. |
| Show Pagination | Toggle | Controls whether pagination links appear at the bottom of the feed for navigating between pages. |

## Which Elements Use This

The Elements options group is used by the Blog module in Divi 5. It may also appear in similar content listing modules that display post feeds with configurable visibility options.

## Code Examples

```php
// Programmatically control blog module elements via shortcode attributes
[et_pb_blog show_author="off" show_date="on" show_categories="off" show_pagination="on"]
```

## Related

- [Content Options](content.md) -- Controls post type, count, categories, and excerpt settings
- [Meta Options](meta.md) -- Admin label and module metadata configuration
