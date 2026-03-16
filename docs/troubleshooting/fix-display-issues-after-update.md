---
title: "Fix Display Issues After Updating"
category: troubleshooting
tags: ["troubleshooting", "update", "display-issues", "cache"]
related: ["fix-custom-css", "support-center"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13627727"
---

# Fix Display Issues After Updating

After a Divi 5 update, pages may show misaligned sections, outdated styles, incorrect fonts, or layouts that do not match the Visual Builder.

## Overview

Display issues after an update are typically caused by stale cached files, incompatible custom CSS, third-party plugin conflicts, or invalid HTML in custom wrappers. Work through the steps below in order -- most problems resolve at step 1 or 2.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13627727).

## Step 1: Clear All Caches

Cached files are the most common culprit. Clear them in this order:

### Divi CSS Cache

Go to **Divi > Theme Options** and click **Clear CSS Cache**. This forces Divi to regenerate its static CSS files with the latest settings.

### Plugin Cache

If you use a caching plugin (WP Rocket, W3 Total Cache, LiteSpeed Cache, etc.), open its settings and purge all caches. Look for separate CSS/JS purge options and use those as well.

### Server-Level Cache

Log into your hosting control panel and look for a Cache or Performance section. Use the Flush or Purge controls. If you cannot find them, contact your host.

### Browser Cache

Clear your browser cache through its settings, or test in a private/incognito window to rule out local caching.

## Step 2: Test Custom CSS

Custom CSS written for a previous version may conflict with updated markup or class names.

1. Go to **Divi > Theme Options > Custom CSS**.
2. Copy all CSS to a text file as a backup.
3. Remove the CSS and click Save.
4. Clear the Divi CSS cache.
5. Check the front end -- if the issue disappears, your CSS needs updating.

Also check these locations for custom code:

- Page Settings > Advanced > Custom CSS
- Module Settings > Advanced > CSS
- Code Modules with `<style>` blocks
- Child theme `style.css`

Re-add your CSS incrementally, testing after each addition, to isolate the problematic rules. Use the browser DevTools or the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to identify syntax errors.

## Step 3: Validate Custom HTML Wrappers

If you use the HTML option group on any module (Advanced > HTML), verify that:

- Every tag opened in **HTML Before** is closed in **HTML After**.
- No experimental or incomplete markup is present.

Remove custom HTML wrappers temporarily and test to see if they are causing the issue.

## Step 4: Check for Plugin Conflicts

1. Deactivate all non-essential plugins.
2. Clear all caches.
3. Test the front end.
4. Reactivate plugins one at a time, clearing caches between each activation, until the issue reappears.

The last activated plugin before the issue returns is the conflict source.

!!! tip "Safe Mode"
    Use **Divi > Support Center > Safe Mode** to disable plugins, child themes, and custom code for your user only -- without affecting other visitors.

## Step 5: Verify Divi Is Up to Date

Confirm you are running the latest version at **Divi > Theme Options**. Check that no pending update tasks or incomplete migration processes exist.

## Step 6: Contact Support

If none of the above steps resolve the issue, contact Elegant Themes support with:

- A description of the problem and when it started
- Links to affected pages
- Screenshots or screen recordings
- Confirmation of which troubleshooting steps you completed

## Related

- [Fix Custom CSS Not Working](fix-custom-css.md)
- [Support Center](../builder/support-center.md)
- [Troubleshooting Decision Tree](../playbooks/troubleshooting-tree.md)
