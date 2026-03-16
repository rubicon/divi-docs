---
title: "Fix Custom CSS Not Working"
category: troubleshooting
tags: ["troubleshooting", "css", "debugging", "troubleshooting"]
related: ["where-to-add-css", "css"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13479939"
---

# Fix Custom CSS Not Working

Custom CSS added to Divi 5 may fail to apply due to syntax errors, caching issues, or missing selectors.

## Overview

When your custom CSS does not produce the expected result, the cause is almost always one of three things: invalid syntax, a cached version of the page being served, or selectors that do not match any elements on the page. This guide helps you diagnose and fix each scenario.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13479939).

## Problem 1: Syntax Errors

**Symptoms:** CSS has no effect at all, or only some rules apply.

**Solution:** Validate your CSS using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) or your browser's DevTools. Common mistakes include:

- Missing semicolons or closing braces
- Typos in property names or values
- Incorrect use of shorthand properties

## Problem 2: Caching

**Symptoms:** CSS changes do not appear even though the code is correct.

**Solution:**

1. **Clear the Divi CSS cache** -- go to **Divi > Theme Options** and click **Clear CSS Cache**.
2. **Clear your caching plugin** -- if you use WP Rocket, W3 Total Cache, or similar, purge all caches.
3. **Clear your browser cache** -- or test in a private/incognito window.
4. **Clear server-level cache** -- if your host uses Varnish, Nginx caching, or a CDN, purge from your hosting control panel.

!!! tip
    During active development, disable caching plugins entirely to avoid confusion. Enable them only when the design is finalized.

## Problem 3: Missing Selectors

**Symptoms:** CSS rule is valid but does not match any element.

**Solution:**

1. Open your browser's DevTools (right-click > Inspect).
2. Find the element you are trying to style.
3. Verify the class name or ID matches what your CSS targets.
4. Check whether Divi has generated different class names than expected.

## Where Custom CSS Can Be Added

Make sure your CSS is in the right location for the scope you need:

| Location | Scope | Notes |
|----------|-------|-------|
| **Divi > Theme Options > Custom CSS** | Site-wide | Applies to every page |
| **Page Settings > Advanced > Custom CSS** | Single page | Only affects the current page |
| **Element > Advanced > Free Form CSS** | Single element | Use `selector.` prefix for custom selectors |
| **Element > Advanced > Module Elements** | Single element | CSS rules only (no selectors) |

!!! info "Module Elements syntax"
    In the Module Elements CSS area, enter only CSS property-value pairs (e.g., `background-color: red;`), not full selectors.

## Related

- [Where to Add Custom CSS](where-to-add-css.md)
- [CSS Options Group](../options-groups/css.md)
- [CSS in Divi 5 Playbook](../playbooks/css-in-divi.md)
