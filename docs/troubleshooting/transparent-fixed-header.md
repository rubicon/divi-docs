---
title: "Transparent Fixed Header"
category: troubleshooting
tags: ["troubleshooting", "header", "fixed", "transparent", "theme-builder"]
related: ["theme-builder", "menu", "scroll-effects"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/14003959"
---

# Transparent Fixed Header

Create a header that overlaps page content with a transparent background and stays fixed at the top while scrolling.

## Overview

A transparent fixed header is a common design pattern where the header sits on top of the hero section with no visible background, then transitions to a solid or semi-transparent background when the user scrolls. Divi 5's Theme Builder, sticky positioning, and scroll effects make this achievable without custom code.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/14003959).

## Step 1: Create a Global Header

1. Go to **Divi > Theme Builder**.
2. Click **Add Global Header** (or edit your existing one).
3. Add a **single-column Row** inside the default Section.
4. Add a **Menu** module to the row and configure it with your logo and WordPress menu.

## Step 2: Configure the Section

1. Open the Section settings.
2. Set **Background Color** to transparent (delete any existing color value).
3. Set top and bottom **Padding** to `0px`.
4. Go to the **Advanced** tab > **Scroll Effects**.
5. Enable **Sticky at the Top**.
6. Optionally, set a **Sticky Background Color** -- this is the color that appears when the user scrolls (e.g., a semi-transparent white like `rgba(255, 255, 255, 0.95)`).
7. Set a **Min Height** value (start with `90px` and adjust as needed for vertical centering).

!!! info "Why Min Height is required"
    The Row inside the Section will be positioned absolutely, which removes it from the normal document flow. The Min Height ensures the Section still occupies space on the page.

## Step 3: Configure the Row

1. Open the Row settings.
2. Set top and bottom **Padding** to `10px`.
3. Go to the **Advanced** tab > **Position**.
4. Set Position to **Absolute**.
5. Set Alignment to **Top Center**.

## Step 4: Configure the Menu Module

1. Open the Menu module settings.
2. Remove the default white background by clearing the **Background Color** field.
3. Style the menu links and logo as needed for visibility against your hero content.

## Result

- **Before scrolling:** The header overlaps the hero section with a fully transparent background, creating a seamless look.
- **After scrolling:** The header sticks to the top and displays the solid or semi-transparent background color you configured.

## Tips

- Choose menu text colors that contrast well against both your hero image and the sticky background color.
- Test on mobile devices to ensure the header height and padding work at all breakpoints.
- If your hero section content is hidden behind the header, add top padding to the hero equal to the header's Min Height.

## Related

- [Theme Builder](../builder/theme-builder.md)
- [Menu Module](../modules/menu.md)
- [Scroll Effects](../options-groups/scroll-effects.md)
