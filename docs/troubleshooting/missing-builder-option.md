---
title: "Missing Enable Divi Builder Option"
category: troubleshooting
tags: ["troubleshooting", "builder", "enable", "post-type"]
related: ["visual-builder", "builder-settings", "support-center"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13904114"
---

# Missing Enable Divi Builder Option

The "Enable Divi Builder" button does not appear on posts, pages, or custom post types.

## Overview

If the button to launch the Divi Visual Builder is missing, the most common cause is that the builder has not been enabled for that post type. Less common causes include plugin conflicts, child theme issues, or server-side problems.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13904114).

## Fix 1: Enable the Builder for the Post Type

This is the most common cause, especially for custom post types.

1. Go to **Divi > Theme Options > Builder** tab.
2. Open the **Post Type Integration** sub-tab.
3. Toggle on the post types where you want the Divi Builder available.
4. Save changes.

The "Enable Divi Builder" button should now appear on new and existing posts of that type.

## Fix 2: Use Safe Mode

If the builder button is missing on post types that are already enabled, a plugin or child theme may be interfering.

1. Go to **Divi > Support Center**.
2. Toggle **Safe Mode** on.
3. Check whether the builder button appears.

Safe Mode temporarily disables all plugins, your child theme, and any custom CSS/JavaScript -- but only for your user session. Other visitors are not affected.

### If Safe Mode Resolves the Issue

The conflict is caused by a plugin, child theme, or custom code. Narrow it down:

1. **Disable custom code:** Go to Divi > Theme Options > Integration and disable any custom header/body scripts.
2. **Deactivate your child theme:** Switch to the parent Divi theme temporarily.
3. **Deactivate all plugins**, then reactivate them one at a time to identify the conflicting plugin.

### If Safe Mode Does Not Help

The issue may be server-side:

1. Check the **System Status** report in **Divi > Support Center** for warnings.
2. Try resetting permalinks: go to **Settings > Permalinks**, switch to **Plain**, save, then switch back to your preferred structure and save again.
3. Install the **Really Simple SSL** plugin if you see mixed-content or SSL errors.
4. Open the browser console (right-click > Inspect > Console tab) and look for JavaScript errors that might prevent the builder from loading.

## Fix 3: Contact Support

If none of the above resolves the issue:

1. Enable **Remote Access** in **Divi > Support Center** so the support team can inspect your setup directly.
2. Contact Elegant Themes support with details about the problem and the troubleshooting steps you have already completed.

## Related

- [Visual Builder](../builder/visual-builder.md)
- [Builder Settings](../theme-options/builder-settings.md)
- [Support Center](../builder/support-center.md)
