---
title: "Missing Elements on Mobile"
category: troubleshooting
tags: ["troubleshooting", "responsive", "visibility", "mobile", "tablet"]
related: ["visibility-settings", "visibility", "responsive-options"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13924090"
---

# Missing Elements on Mobile

Sections, rows, or modules visible on desktop disappear on phones or tablets.

## Overview

If elements vanish on mobile devices but display correctly on desktop, the cause is typically one of three things: visibility settings configured to hide elements on smaller screens, display conditions that exclude mobile devices, or custom CSS/JavaScript overriding visibility.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13924090).

## Fix 1: Check Visibility Settings

This is the most common cause.

1. Open the page in the Visual Builder.
2. Select the element that is missing on mobile.
3. Go to the **Advanced** tab > **Visibility** section.
4. Check whether **Phone** or **Tablet** is checked under **Disable On**.
5. Uncheck the devices where the element should be visible.

!!! tip "Find hidden elements quickly"
    Enable **Show Disabled Elements at 50% Opacity** in the builder settings. This makes elements hidden on the current preview breakpoint appear faded rather than completely invisible, so you can identify and select them.

## Fix 2: Review Display Conditions

Divi 5's condition system can prevent elements from rendering based on various rules.

1. Open the element's settings.
2. Go to the **Advanced** tab > **Conditions** section.
3. Review any configured conditions that might block display on mobile (e.g., device-type conditions, screen-width conditions).
4. Remove or modify conditions that unintentionally exclude phone or tablet users.

## Fix 3: Test for Custom Code Conflicts

Custom CSS or JavaScript may be hiding elements on smaller screens.

1. Go to **Divi > Support Center**.
2. Enable **Safe Mode**.
3. Reload the page on a mobile device or use the browser's responsive preview.
4. If the element appears, custom code is responsible.

Check these locations for problematic code:

| Code Type | Location |
|-----------|----------|
| CSS | Divi > Theme Options > Custom CSS |
| CSS | Page Settings > Advanced |
| CSS | Code Modules with `<style>` blocks |
| JavaScript | Divi > Theme Options > Integration |
| JavaScript | Code Modules with `<script>` blocks |

Look for rules like `display: none`, `visibility: hidden`, or media queries that target mobile screen widths.

## After Fixing

Clear your site cache after making changes. Cached pages may continue to show the old (broken) version until the cache is purged.

## Related

- [Visibility Settings](visibility-settings.md)
- [Visibility Options Group](../options-groups/visibility.md)
- [Responsive Options](../builder/responsive-options.md)
- [Conditions Options Group](../options-groups/conditions.md)
