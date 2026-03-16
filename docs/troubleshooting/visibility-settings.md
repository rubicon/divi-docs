---
title: "Visibility Settings"
category: troubleshooting
tags: ["troubleshooting", "visibility", "responsive", "device-visibility"]
related: ["visibility", "responsive-options", "custom-breakpoints"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13722487"
---

# Visibility Settings

Control which elements appear on different devices using Divi 5's per-element visibility settings.

## Overview

Divi 5 lets you selectively hide sections, rows, columns, and modules on specific device types. This is useful when you need structurally different layouts for desktop and mobile rather than just resized versions of the same design.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13722487).

## How to Configure Visibility

1. Hover over the element you want to control and click the **gear icon** to open its settings.
2. Go to the **Advanced** tab.
3. Open the **Visibility** option group.
4. Under **Disable On**, check the devices where the element should be hidden: **Phone**, **Tablet**, or **Desktop**.
5. Save your changes.

## Previewing Disabled Elements

When you switch device previews in the Visual Builder, elements disabled on the current preview breakpoint appear at **50% opacity**. They are still visible to you for editing purposes but will not render on the front end for that device.

## Available Breakpoints

| Breakpoint | Description |
|------------|-------------|
| Phone | Smallest screens (default) |
| Phone Wide | Wider phone screens (optional) |
| Tablet | Mid-range screens (default) |
| Tablet Wide | Wider tablet screens (optional) |
| Desktop | Standard screens (default) |
| Widescreen | Large monitors (optional) |
| Ultra Wide | Very large monitors (optional) |

The three default breakpoints (Phone, Tablet, Desktop) are always available. Additional breakpoints can be enabled through [Custom Breakpoints](../builder/custom-breakpoints.md).

## Overflow Settings

The Visibility option group also includes **Horizontal Overflow** and **Vertical Overflow** controls with four options:

- **Visible** -- content overflows normally
- **Hidden** -- content is clipped at the element boundary
- **Scroll** -- a scrollbar appears when content overflows
- **Auto** -- a scrollbar appears only when needed

These are useful when content clips or extends beyond its container on smaller screens.

## Best Practices

- **Limit layout versions** to one desktop and one mobile version. Creating too many device-specific alternatives makes maintenance difficult.
- **Use admin labels** to identify variants clearly (e.g., "Hero -- Desktop", "Hero -- Mobile").
- **Reserve visibility toggles for structural changes.** For minor adjustments like font sizes or spacing, use responsive styling options instead.
- **Use overflow settings** when content clips unexpectedly on small screens rather than hiding the entire element.

## Related

- [Visibility Options Group](../options-groups/visibility.md)
- [Responsive Options](../builder/responsive-options.md)
- [Custom Breakpoints](../builder/custom-breakpoints.md)
- [Missing Elements on Mobile](missing-elements-mobile.md)
