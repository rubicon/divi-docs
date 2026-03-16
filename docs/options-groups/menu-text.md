---
title: "Menu Text Options"
description: "Divi 5 Menu Text options group — font, size, color, active link styling, and color scheme for navigation menu item text."
category: options-groups
tags: ["options-groups", "menu-text"]
related: ["text", "title-text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10353617"
---

# Menu Text Options

Provides full typographic and color control over navigation menu item text in Divi 5.

!!! abstract "Quick Reference"
    **What it controls:** Font, size, color, active link color, text color scheme, alignment, and text shadow for menu items
    **Where to find it:** Design Tab → Menu Text
    **Available on:** Menu and Fullwidth Menu modules only
    **Responsive:** Yes — all typography values can be set per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10353617)

## Overview

The Menu Text options group lets you customize every aspect of how menu item text appears within the Menu and Fullwidth Menu modules. It covers font selection, weight, size, color, alignment, spacing, and shadow effects, giving you precise control over your site navigation typography.

These settings are found in the Design tab of the Menu module settings panel. Beyond standard typography controls, the Menu Text group includes an Active Link Color setting for highlighting the current page and a Text Color Scheme toggle for switching between dark and light text modes. These features make it easy to adapt menu styling to different header backgrounds.

Because navigation menus are a prominent part of every page, consistent and readable menu text is essential. The settings in this group let you match your menu typography to your site branding while ensuring good readability at all viewport sizes through responsive controls.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10353617).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Active Link Color | Color picker | Sets the text color for the currently active page link in the menu. |
| Menu Font | Font selector | Chooses the typeface for menu item text, supporting default and custom fonts. |
| Menu Font Weight | Selector | Adjusts the boldness of menu text from light to extra-bold. |
| Menu Font Style | Toggle options | Applies italics, capitalization, small caps, underline, or strikethrough to menu text. |
| Menu Text Color | Color picker | Sets the base text color for all menu items. |
| Menu Text Size | Range slider / input | Defines the font size of menu item text. |
| Menu Letter Spacing | Range slider / input | Controls the spacing between characters in menu text. |
| Menu Line Height | Range slider / input | Sets the vertical spacing between lines of menu text. |
| Menu Text Shadow | Shadow editor | Adds a shadow effect to menu text with direction, blur, and color controls. |
| Text Alignment | Alignment selector | Positions menu text as left, center, right, or justified. |
| Text Color Scheme | Toggle | Switches between dark and light text color modes for different background contexts. |

## Which Elements Use This

The Menu Text options group is used by the Menu module and Fullwidth Menu module in Divi 5. It controls the text styling for all navigation links rendered by these modules.

## Code Examples

```css
/* Custom menu text styling */
.et_pb_menu .et-menu a {
  font-size: 15px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

/* Active link highlight */
.et_pb_menu .current-menu-item a {
  color: #6c5ce7;
}
```

## Related

- [Text Options](text.md) -- General text alignment and shadow settings
- [Title Text Options](title-text.md) -- Typography controls for module titles
