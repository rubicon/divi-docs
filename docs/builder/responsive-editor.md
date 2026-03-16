---
title: "Responsive Editor"
description: "Divi 5 Responsive Editor — view and edit per-breakpoint, hover, and sticky values for any setting from a single unified modal."
category: builder
tags: ["builder", "responsive", "breakpoints", "editor", "device"]
related: ["custom-breakpoints", "responsive-preview"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12105366"
---

# Responsive Editor

Edit per-breakpoint values for any setting from a single modal without switching device views.

!!! abstract "Quick Reference"
    **What it does:** Opens a per-setting panel showing values for every breakpoint, hover state, and sticky state in one view.
    **Where to find it:** Click the Responsive Editor icon next to any responsive-capable setting in element settings.
    **Key features:**

    - Rows for each enabled breakpoint (up to 7) plus hover and sticky states
    - Blue icon indicator flags settings with non-desktop overrides
    - Reset button to clear individual breakpoint overrides
    - Modified Settings filter to audit all responsive customizations

    **ET Docs:** [Responsive Editor](https://help.elegantthemes.com/en/articles/12105366){:target="_blank"}

## Overview

The Responsive Editor is a per-setting panel that displays the current value of an option across every enabled breakpoint, hover state, and sticky state in one unified view. Instead of switching between device previews to tweak a font size or padding value, you open the Responsive Editor next to that specific setting and make all adjustments in place.

A blue icon indicator appears whenever a setting has been customized for at least one non-desktop state, acting as a visual map of all responsive overrides on the page. You can also filter the settings sidebar to show only modified settings, making it easy to audit responsive changes.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12105366) and the [responsive editing details article](https://help.elegantthemes.com/en/articles/13002269).

## Inheritance Model

Desktop is the base layer. All other breakpoints inherit the desktop value until you provide an explicit override.

| Scenario | Behavior |
|----------|----------|
| Only desktop value set | All devices display the desktop value |
| Tablet value overridden | Tablet uses the override; other devices still inherit desktop |
| Override cleared (reset) | That breakpoint reverts to inheriting from desktop |
| Display hint | Inherited values appear in gray text; custom overrides in standard text |

## How to Access

1. Open element settings (click the gear icon or the element itself).
2. Locate the setting you want to adjust (e.g., Font Size, Padding, Background).
3. Click the **Responsive Editor icon** next to that setting.
4. The modal opens, showing rows for every enabled breakpoint plus hover and sticky states.

The icon is available on any setting that supports responsive values, across sections, rows, columns, and modules.

## Settings and Controls

| Control | Type | Description |
|---------|------|-------------|
| Device rows | Value fields | One row per enabled breakpoint showing the current value |
| Hover state row | Value field | The value applied on mouse hover (where supported) |
| Sticky state row | Value field | The value applied when the element is in a sticky position |
| Reset button | Action | Clears the override for a specific state, returning it to inheritance |
| Blue icon indicator | Visual flag | Appears on the parent setting when any non-desktop state has a custom value |
| Modified Settings filter | Toggle | Filters the settings sidebar to show only settings with responsive overrides |

## Workflow

1. Open element settings and find the target option.
2. Click the Responsive Editor icon to open the panel.
3. Locate the breakpoint row you want to customize (e.g., Tablet).
4. Enter or adjust the value.
5. Repeat for additional breakpoints or states as needed.
6. Use the **Reset** button to clear any unintended overrides.
7. Close the panel and save your changes.

## Supported Breakpoints

The Responsive Editor displays rows for every breakpoint enabled in your [Custom Breakpoints](custom-breakpoints.md) configuration -- up to seven:

| Breakpoint | Notes |
|------------|-------|
| Phone | Smallest viewport |
| Phone Wide | Only visible if enabled in breakpoint settings |
| Tablet | Mid-range viewport |
| Tablet Wide | Only visible if enabled in breakpoint settings |
| Desktop | Always present; base values live here |
| Widescreen | Only visible if enabled in breakpoint settings |
| Ultra Wide | Only visible if enabled in breakpoint settings |

## Common Use Cases

| Task | Approach |
|------|----------|
| Reduce heading size on mobile | Open Responsive Editor on Font Size; set smaller values for Phone and Tablet |
| Tighten spacing on small screens | Open Responsive Editor on Padding/Margin; reduce values for phone breakpoints |
| Audit all responsive overrides | Toggle the Modified Settings filter in the sidebar to surface every customized setting |
| Remove a stale override | Look for the blue icon indicator, open the Responsive Editor, and click Reset on the unwanted state |

## Tips and Best Practices

- **Start with desktop.** Set your base values on the Desktop row first, then override only where genuinely needed.
- **Minimize overrides.** Every device-specific value is another thing to maintain. Override only when the design actually breaks.
- **Watch the blue icons.** They are your map to every responsive customization. If a design looks unexpected on a device, check blue-flagged settings first.
- **Combine with device preview.** Use the Responsive Editor for precision edits and the [Responsive Preview](responsive-preview.md) for full-page context.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If the Responsive Editor icon is not visible, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.

- **Setting shows a value but the device preview looks different.** Check whether a parent element (section or row) has an override that is cascading down.
- **Blue icon present but no obvious override.** Open the Responsive Editor and check hover and sticky state rows -- the override may be on a non-breakpoint state.
- **Modified Settings filter shows nothing.** Confirm you have actually saved responsive overrides; unsaved edits may not appear in the filter.

## Related

- [Custom Breakpoints](custom-breakpoints.md)
- [Responsive Preview](responsive-preview.md)
