---
title: "Settings Search"
description: "Divi 5 Settings Search — find any element setting instantly with keyword search and category filters across Content, Design, and Advanced tabs."
category: builder
tags: ["builder", "search", "settings", "filters", "workflow"]
related: ["visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11483918"
---

# Settings Search

Instantly locate any setting within an element's Content, Design, or Advanced tabs using keyword search and category filters.

!!! abstract "Quick Reference"
    **What it does:** Filters element settings by keyword or category so you can jump directly to any option.
    **Where to find it:** Search bar at the top of every element's settings panel.
    **Key features:**

    - Free-text keyword search across all three tabs simultaneously
    - Category filter buttons: Modified, Variables, Colors, Sizes, Fonts, Background, Code, URLs, and more
    - Modified filter for auditing all changed settings on an element
    - Variables filter for identifying design variable usage

    **ET Docs:** [Settings Search](https://help.elegantthemes.com/en/articles/11483918){:target="_blank"}

## Overview

Every Divi element can have dozens of settings spread across three tabs and many option groups. The Settings Search feature adds a search bar and a bank of filter buttons to the top of every element's settings panel, letting you jump directly to the option you need instead of scrolling through tabs.

Type a keyword -- like "radius", "padding", or "font size" -- and the panel collapses to show only matching settings from all three tabs at once. Alternatively, use one of the built-in category filters to narrow the view to a specific type of option such as colors, sizes, or backgrounds.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11483918).

## How to Use Settings Search

1. Click any element (section, row, column, or module) to open its settings panel.
2. Locate the **search bar** at the top of the settings modal.
3. Type a keyword (e.g., "margin", "color", "border").
4. The panel filters down to display only matching settings across all tabs.
5. Edit the setting directly in the filtered view.
6. Clear the search to return to the full settings panel.

## Filter Categories

In addition to free-text search, the settings panel provides filter buttons that isolate settings by type.

| Filter | Shows |
|--------|-------|
| Modified | Only settings that have been changed from their defaults |
| Variables | Settings that reference a Design Variable |
| Static | Static content fields (text, labels) |
| Colors | Text Color, Link Color, Heading colors, background colors |
| Sizes | Font sizes, Width, Height, Border Radius, Border Width |
| Effects | Hue, Saturate, Brightness, Scale, Translate, Rotate |
| Font Families | Text Font, Link Font, Heading Font selections |
| Font Weights | Font weight options across text elements |
| Text | Title, Body, Admin Label, and other text-based options |
| Background | Background Image, Video, Pattern, Mask settings |
| Icons | Icon selection fields |
| Code | Before, Main Element, After, and CSS option fields |
| URLs | Module Link, Button Link, and other URL fields |

## Key Workflows

### Find a Specific Setting Quickly

Type the setting name or a related keyword. For example, entering "radius" immediately surfaces the Border Radius controls without navigating to the Design tab and expanding the Border group.

### Review All Changes on a Layout Pack Page

After importing a premade layout and making customizations, click **Modified** to see every setting you have changed. This is useful before saving or handing off to a client.

### Locate an Unfamiliar Setting

When you know what you want to change but not where Divi stores it, search for it. Typing "padding" or "font" reveals every instance of that setting type on the current element.

### Audit Design Variable Usage

Click the **Variables** filter to see which settings on the element are linked to a Design Variable and which are using static values.

## Tips and Best Practices

- **Use short, specific keywords.** Searching for "size" returns many results; "font size" or "border radius" is more precise.
- **The Modified filter is your audit tool.** Use it before saving to confirm you have only changed what you intended.
- **Filters work across all tabs.** You do not need to be on the Design tab to find design settings -- the filter pulls from Content, Design, and Advanced simultaneously.
- **Combine with the Responsive Editor.** After finding a setting via search, click its Responsive Editor icon to adjust it across breakpoints.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If the search bar is not visible at the top of element settings, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.

- **Search returns no results.** Double-check spelling. Try a broader keyword or use a category filter instead.
- **Modified filter is empty.** No settings have been changed from their defaults on this element.
- **Filter shows settings from a tab I did not expect.** This is expected behavior -- filters span all three tabs (Content, Design, Advanced).

## Related

- [Visual Builder](visual-builder.md)
