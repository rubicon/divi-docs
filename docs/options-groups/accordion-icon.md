---
title: "Accordion Icon Options"
description: "Divi 5 Accordion Icon options group — color and custom size controls for the expand/collapse indicator icon on accordion items."
category: options-groups
tags: ["options-groups", "accordion-icon"]
related: ["toggle-icon", "toggle"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10101739"
---

# Accordion Icon Options

Controls the color and size of the toggle indicator icon displayed in Accordion module items.

!!! abstract "Quick Reference"
    **What it controls:** Icon color and optional custom icon size for the expand/collapse indicator
    **Where to find it:** Design Tab → Icon
    **Available on:** Accordion module only
    **Responsive:** No — icon color and size apply across all breakpoints
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10101739)

## Overview

The Accordion Icon options group provides design controls for the small icon that appears on each accordion item, typically positioned on the right side of the toggle title. This icon serves as a visual indicator that the item can be expanded or collapsed, and its appearance can be customized to match your design.

These settings are found in the Design tab of the Accordion module settings panel, within the Icon option group. You can change the icon color and optionally enable a custom size to make the icon larger or smaller than the default. The icon color defaults to a light gray, but you can set it to any color to match your layout.

A well-styled toggle icon improves usability by clearly signaling interactive elements. Choosing a color that contrasts with the toggle background ensures the icon is visible, while appropriate sizing keeps it proportional to the title text.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10101739).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Icon Color | Color picker | Sets the color of the toggle indicator icon. Defaults to light gray. |
| Use Custom Icon Size | Toggle | Enables or disables custom icon sizing. When disabled, the icon uses the default size. |
| Icon Size | Range slider / input | Sets the dimensions of the icon in pixels. Only available when custom icon size is enabled. |

## Which Elements Use This

The Accordion Icon options group is used exclusively by the Accordion module in Divi 5. It controls the appearance of the expand/collapse indicator icon displayed alongside each accordion item title.

## Code Examples

```css
/* Style accordion toggle icons */
.et_pb_accordion .et_pb_toggle .et-pb-icon {
  color: #6c5ce7;
  font-size: 20px;
}
```

## Related

- [Toggle Icon Options](toggle-icon.md) -- Selects the specific icon used for the closed state
- [Toggle Options](toggle.md) -- Background colors for open and closed toggle states
