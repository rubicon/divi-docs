---
title: "Custom Breakpoints"
description: "Divi 5 Custom Breakpoints — enable up to seven responsive breakpoints (Phone through Ultra Wide) and adjust their pixel widths site-wide."
category: builder
tags: ["builder", "responsive", "breakpoints", "mobile", "media-queries"]
related: ["responsive-editor", "responsive-preview"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10511806"
---

# Custom Breakpoints

Configure up to seven responsive breakpoints to control how your Divi layouts adapt across phone, tablet, desktop, and ultrawide screens.

!!! abstract "Quick Reference"
    **What it does:** Lets you enable/disable breakpoints and set custom pixel widths for site-wide responsive behavior.
    **Where to find it:** Top bar → three-dot menu next to device icons → Sitewide Responsive Breakpoints.
    **Key features:**

    - Seven breakpoints: Phone, Phone Wide, Tablet, Tablet Wide, Desktop, Widescreen, Ultra Wide
    - Three enabled by default (Phone, Tablet, Desktop); four optional
    - Adjustable pixel widths with ascending-order enforcement
    - Disabling a breakpoint preserves its styles for later re-enabling

    **ET Docs:** [Custom Breakpoints](https://help.elegantthemes.com/en/articles/10511806){:target="_blank"}

## Overview

Divi 5 ships with a customizable breakpoint system that replaces the fixed phone/tablet/desktop tiers from earlier versions. You can enable or disable individual breakpoints and adjust their pixel widths, giving you granular control over how designs respond at every viewport size. Changes are applied site-wide, so every page shares the same responsive grid.

Under the hood, Divi generates CSS media queries for each enabled breakpoint. Desktop serves as the base layer with no media query. Smaller breakpoints use `min-width` queries, while larger breakpoints (Widescreen, Ultra Wide) use `max-width` queries. Enabling additional breakpoints does not add performance overhead on the front end.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10511806) and the [breakpoint details article](https://help.elegantthemes.com/en/articles/13001900).

## Default Breakpoints

Divi 5 provides seven breakpoints. Three are enabled by default; four are available but disabled until you turn them on.

| Breakpoint | Default State | Editable Width | Can Disable | Media Query Type |
|------------|---------------|----------------|-------------|------------------|
| Phone | Enabled | Yes | Yes | `min-width` |
| Phone Wide | Disabled | Yes | Yes | `min-width` |
| Tablet | Enabled | Yes | Yes | `min-width` |
| Tablet Wide | Disabled | Yes | Yes | `min-width` |
| Desktop | Enabled | No | No | Base (none) |
| Widescreen | Disabled | Yes | Yes | `max-width` |
| Ultra Wide | Disabled | Yes | Yes | `max-width` |

Desktop is always enabled and its width cannot be changed -- it is the foundational layer from which all other breakpoints inherit.

## Accessing Breakpoint Settings

1. Open any page in the Divi 5 Visual Builder.
2. Locate the device icons in the top bar.
3. Click the **three-dot overflow menu** icon next to the device icons.
4. Select **Sitewide Responsive Breakpoints**.

You can also reach the breakpoint picker from the Settings Modal or from the device selector dropdown inside any element's settings panel.

## Configuring Breakpoints

### Enabling and Disabling

Toggle a breakpoint on or off with its switch. Key behaviors:

| Action | Result |
|--------|--------|
| Disable a breakpoint | Styles are preserved but not applied; the media query is removed |
| Re-enable a breakpoint | Previously saved styles are restored automatically |
| Save | Changes only take effect after clicking Save and confirming |

### Adjusting Widths

Click an enabled breakpoint to edit its pixel value. All widths must maintain ascending order -- Divi enforces this constraint and will not let you set a value that overlaps an adjacent breakpoint, even if that adjacent breakpoint is currently disabled.

| Rule | Detail |
|------|--------|
| Units | Pixels only |
| Ordering | Each breakpoint must be wider than the one below it |
| Validation | Divi checks constraints before saving |
| Scope | Site-wide; not configurable per-page |

## Workflow Summary

1. Open the Sitewide Responsive Breakpoints panel (three-dot menu in the top bar).
2. Toggle on any additional breakpoints you need (e.g., Phone Wide, Widescreen).
3. Click each enabled breakpoint to adjust its pixel width if the defaults do not suit your design.
4. Verify that widths remain in ascending order.
5. Click **Save** and confirm the change.

After saving, the new breakpoints appear in the device switcher and in every element's responsive editor.

## Tips and Best Practices

- **Start with the defaults.** Phone, Tablet, and Desktop cover most projects. Only add breakpoints when a design genuinely needs them.
- **Plan breakpoints around content, not devices.** Set widths where your layout actually breaks rather than targeting specific phone models.
- **Disabling is non-destructive.** If you experiment with Widescreen styles and later disable the breakpoint, those styles are kept in storage and will return if you re-enable it.
- **Performance is unaffected.** Enabling all seven breakpoints does not slow down page rendering.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 used fixed, non-configurable breakpoints.

## Troubleshooting

!!! warning "Feature Not Available"
    If the breakpoint settings are not visible, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.

- **Cannot set a breakpoint width.** The value likely conflicts with an adjacent breakpoint. Adjust surrounding widths first to make room.
- **Styles disappear after disabling a breakpoint.** The styles are still stored; they are simply not applied. Re-enable the breakpoint to restore them.
- **Breakpoint changes not reflecting on the front end.** Confirm you clicked Save and received the confirmation message. Clear any page caches.

## Related

- [Responsive Editor](responsive-editor.md)
- [Responsive Preview](responsive-preview.md)
