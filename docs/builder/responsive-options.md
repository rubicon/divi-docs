---
title: "Responsive Options"
description: "Divi 5 Responsive Options — device-first editing workflow where selecting a breakpoint automatically scopes all design changes to that device."
category: builder
tags: ["builder", "responsive", "mobile", "breakpoints", "device"]
related: ["responsive-preview", "vb-interface"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10454950"
---

# Responsive Options

How Divi 5 handles device-specific design settings, breakpoints, and the responsive editing workflow.

!!! abstract "Quick Reference"
    **What it does:** Makes every design setting inherently responsive — select a device, edit any setting, and the change applies to that breakpoint.
    **Where to find it:** Device selector in the top bar, or the per-element device selector in settings panels.
    **Key features:**

    - Device-first workflow: no "enable responsive" toggle needed per setting
    - Desktop values cascade to Tablet and Phone unless overridden
    - Nearly every setting supports per-device values (typography, spacing, layout, visibility)
    - Module-level device selector for breakpoint-specific edits within the settings panel

    **ET Docs:** [Divi Responsive Options](https://help.elegantthemes.com/en/articles/10454950){:target="_blank"}

## Overview

Divi 5 takes a device-first approach to responsive design. Instead of requiring you to manually enable responsive toggles on each individual setting (as Divi 4 required), you simply select a device from the top bar and any edits you make are automatically scoped to that breakpoint. This dramatically reduces the number of clicks needed to build responsive layouts. For the official Elegant Themes reference, see [Divi Responsive Options](https://help.elegantthemes.com/en/articles/10454950){:target="_blank"}.

With mobile devices accounting for the majority of internet traffic, responsive design is not optional. Divi's responsive options let you tailor every design setting -- font sizes, spacing, visibility, layout direction, and more -- for each device size without writing media queries.

## Device Breakpoints

Divi 5 supports three primary device breakpoints accessible from the device selector in the top bar:

| Device | Typical Width | Use Case |
|--------|--------------|----------|
| **Desktop** | 981 px and above | Standard laptop and desktop screens. |
| **Tablet** | 768 px -- 980 px | Tablets in portrait and landscape orientation. |
| **Phone** | Below 768 px | Smartphones in portrait orientation. |

Settings cascade downward by default: a value set on Desktop applies to Tablet and Phone unless you override it at the smaller breakpoint.

For additional control over viewport widths, see [Responsive Preview](responsive-preview.md), which lets you test arbitrary pixel widths and custom breakpoints.

## How Responsive Editing Works in Divi 5

### The Device-First Workflow

1. **Select a device** from the device selector in the top bar (Desktop, Tablet, or Phone).
2. **Click any element** to open its settings.
3. **Adjust any setting** -- the change automatically applies to the selected device breakpoint.
4. **Switch devices** and adjust again if the value needs to differ.

There is no extra "enable responsive" toggle to click. Every design setting is inherently responsive.

### Divi 5 vs. Divi 4

| Step | Divi 4 | Divi 5 |
|------|--------|--------|
| Enable responsive for a setting | Click the responsive icon on each individual setting | Not needed -- all settings are responsive by default |
| Select target device | Choose from a per-setting device dropdown | Select once from the top-bar device selector |
| Adjust value | Edit the value | Edit the value |
| Repeat for next setting | Re-enable responsive, re-select device | Just edit (device is already selected) |

The result is fewer steps, faster iterations, and a more intuitive workflow.

### Module-Level Device Selector

In addition to the global device selector in the top bar, each element's settings panel includes a device selector so you can switch breakpoints without leaving the settings window.

## Responsive Setting Types

Nearly every design setting in Divi supports per-device values. Common examples include:

| Setting Category | Examples |
|-----------------|----------|
| **Typography** | Font size, line height, letter spacing |
| **Spacing** | Padding, margin, gap |
| **Sizing** | Width, height, max-width, min-height |
| **Layout** | Flex direction, alignment, column count |
| **Visibility** | Show/hide on specific devices |
| **Position** | Top, left, right, bottom offsets |
| **Transform** | Scale, rotate, translate per device |

## Best Practices

- **Design desktop first, then refine.** Start with the desktop layout, then switch to tablet and phone to adjust values that do not scale well.
- **Use relative units.** Percentages, `em`, and `vw` values often need fewer per-device overrides than fixed pixel values.
- **Leverage presets and variables.** Define responsive-friendly values in [presets](presets.md) and global variables so changes propagate site-wide.
- **Test at every breakpoint.** Use the [Responsive Preview](responsive-preview.md) system to verify your design at the exact widths your audience uses.
- **Minimize overrides.** The fewer device-specific overrides you set, the easier the layout is to maintain. Let the cascade do the work.

## Version Notes

!!! note "Divi 5 Only"
    The device-first responsive workflow described here is specific to Divi 5. Divi 4 requires manually enabling responsive controls on a per-setting basis.

## Related

- [Responsive Preview](responsive-preview.md) -- Preview your design at specific viewport widths
- [Visual Builder Interface](vb-interface.md) -- Top bar device selector and workspace overview
- [Visual Builder](visual-builder.md) -- General Visual Builder documentation
- [Custom Breakpoints](custom-breakpoints.md) -- Define custom viewport breakpoints beyond defaults
- [Visibility Options](../options-groups/visibility.md) -- Show or hide elements per device type
- [Playbook: Responsive Design](../playbooks/responsive-design.md) -- Best practices for responsive Divi layouts
