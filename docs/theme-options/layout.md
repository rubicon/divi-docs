---
title: "Layout Settings"
description: "Divi 5 Layout theme options — single post and page layout controls for thumbnails, comments, post info sections, and index page display settings."
category: theme-options
tags: [theme-options, layout, posts, pages, thumbnails, comments]
related: [general, navigation, builder-settings]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/theme-options/"
---

# Layout Settings

The Layout Settings tab controls how posts and pages display content such as post info sections, comments, and thumbnail images.

!!! abstract "Quick Reference"
    **What it controls:** How posts and pages display thumbnails, comments, and post info sections on single and index pages.
    **Where to find it:** Divi → Theme Options → Layout
    **Key settings:** Place Thumbs on Posts/Pages, Show comments on posts/pages, Post info section items
    **ET Docs:** [https://www.elegantthemes.com/documentation/divi/theme-options/](https://www.elegantthemes.com/documentation/divi/theme-options/)

## Overview

In the Layout Settings tab there are three sub-tabs: **Single Post Layout**, **Single Page Layout**, and **General Settings**.

The **Single Post Layout** sub-tab controls what information is displayed in the post info section on single post pages, whether comments are shown, and whether thumbnails appear on posts. The **Single Page Layout** sub-tab provides controls for thumbnails and comments on pages specifically.

The **General Settings** sub-tab contains options for the post info section on index pages and whether thumbnails are shown on index pages.

<!-- ![Layout Settings overview](../assets/screenshots/theme-options/layout/overview.png){ loading=lazy }
*The Layout Settings panel in Divi Theme Options.* -->

## Settings & Options

### Single Post Layout

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Choose which items to display in the post info section | select | All | Choose which items appear in the post info section on single post pages. This is the area, usually below the post title, which displays basic information about your post. The highlighted items will appear. |
| Show comments on posts | toggle | Enabled | Controls whether comments and the comment form are displayed on single post pages. Disable to remove comments from posts. |
| Place Thumbs on Posts | toggle | Enabled | By default, thumbnails are placed at the beginning of your post on single post pages. Disable this to remove the initial thumbnail image and avoid repetition. |

### Single Page Layout

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Place Thumbs on Pages | toggle | Disabled | By default, thumbnails are not placed on pages (only on posts). Enable this option to use thumbnails on pages. |
| Show comments on pages | toggle | Disabled | By default, comments are not placed on pages. Enable this option to allow people to comment on your pages. |

### General Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Post info section | select | All | Choose which items appear in the post info section on index pages. This is the area, usually below the post title, which displays basic information about your post. |
| Show Thumbs on Index pages | toggle | Enabled | Enable this option to show thumbnails on Index Pages. |

## Code Examples

```php
// Check if comments are enabled on posts
$show_comments = et_get_option('divi_show_postcomments', 'on');

// Check if thumbnails are placed on posts
$show_thumbs = et_get_option('divi_thumbnails', 'on');

// Check if page comments are enabled
$page_comments = et_get_option('divi_show_pagescomments', 'off');
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Thumbnails Not Appearing"
    If thumbnails are enabled but not appearing, ensure your posts have a Featured Image set. The "Grab the first post image" option in General Settings must also be enabled if you want to use the first image in the post content as the thumbnail instead of a Featured Image.

## Related

- [General Settings](general.md)
- [Navigation Settings](navigation.md)
- [Builder Settings](builder-settings.md)
