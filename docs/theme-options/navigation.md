---
title: "Navigation Settings"
category: theme-options
tags: [theme-options, navigation, menu, pages, categories, dropdown]
related: [general, layout]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/theme-options/"
---

# Navigation Settings

The Navigation Settings tab controls which pages and categories appear in your site's navigation bar, along with dropdown behavior and link ordering.

## Overview

In the Navigation settings tab, there are three sub-tabs: **Pages**, **Categories**, and **General Settings**.

The **Pages** sub-tab lets you exclude certain pages from the navigation, show or hide dropdown menus, display a home page link, and control page link sorting. The **Categories** sub-tab provides similar controls for category links, including hiding empty categories and specifying the order of categories.

The **General Settings** sub-tab contains a single but important setting for disabling top-tier dropdown menu links, which is useful when parent links serve as organizational placeholders only.

<!-- ![Navigation Settings overview](../assets/screenshots/theme-options/navigation/overview.png){ loading=lazy }
*The Navigation Settings panel in Divi Theme Options.* -->

## Settings & Options

### Pages

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Exclude pages from the navigation bar | select | — | Choose to remove certain pages from the navigation menu. All pages marked with an X will not appear in your navigation bar. |
| Show dropdown menus | toggle | Enabled | Controls whether dropdown menus are displayed in the pages navigation bar. Disable this to remove dropdown menus entirely. |
| Display Home link | toggle | Enabled | By default, the theme creates a Home link that leads back to your blog's homepage. If you are using a static homepage and have already created a page called Home, disable this to avoid a duplicate link. |
| Sort Pages Links | select | Name | Choose how to sort your pages links in the navigation. |
| Order Pages Links by Ascending/Descending | select | Ascending | Choose between ascending and descending order for page links display. |
| Number of dropdown tiers shown | number | 3 | Controls how many tiers your pages dropdown menu has. Increasing the number allows for additional menu items to be shown. |

### Categories

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Exclude categories from the navigation bar | select | — | Choose to remove certain categories from the navigation menu. All categories marked with an X will not appear in your navigation bar. |
| Show dropdown menus | toggle | Enabled | Controls whether dropdown menus are displayed in the categories navigation bar. Disable to remove dropdown menus. |
| Hide empty categories | toggle | Enabled | By default, empty categories are hidden. Disable this option to display categories in the navigation bar that don't have any posts. |
| Number of dropdown tiers shown | number | 3 | Controls how many tiers your categories dropdown menu has. Increasing the number allows for additional menu items to be shown. |
| Sort Categories Links by Name/ID/Slug/Count/Term Group | select | Name | By default, categories are sorted by name. Adjust this setting to sort by ID, Slug, Count, or Term Group instead. |
| Order Category Links by Ascending/Descending | select | Ascending | Choose between ascending and descending order for category links display. |

### General Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Disable top tier dropdown menu links | toggle | Disabled | When enabled, removes the links from all parent pages/categories so they don't lead anywhere when clicked. Useful when parent categories or links serve as placeholders to hold a list of child links or categories. |

## Code Examples

```php
// Programmatically exclude pages from navigation
$excluded_pages = et_get_option('divi_exclude_pages');

// Check if dropdown menus are enabled
$show_dropdowns = et_get_option('divi_show_dropdown', 'on');
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Navigation Not Updating"
    If changes to navigation settings don't appear on the front end, clear any page caching plugins and your browser cache. Also note that if you are using the Theme Builder with a custom header template, these navigation settings may be overridden by your Theme Builder configuration.

## Related

- [General Settings](general.md)
- [Layout Settings](layout.md)
- [Builder Settings](builder-settings.md)
