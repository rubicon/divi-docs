---
title: "Theme & Module Customizer"
description: "Divi 5 Theme and Module Customizer — site-wide styling controls for header, navigation, body text, headings, and per-module size and font customization."
category: theme-options
tags: ["theme-options", "customizer", "styling", "typography", "global-styles", "header", "navigation", "footer"]
related: ["general", "navigation", "layout"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://www.elegantthemes.com/documentation/divi/customizer"
---

# Theme & Module Customizer

The Theme Customizer and Module Customizer provide live-preview controls for site-wide styling and per-module defaults in Divi 5.

!!! abstract "Quick Reference"
    **What it controls:** Site-wide theme element styling (header, navigation, logo, body/heading text) and per-module size, font, and color defaults.
    **Where to find it:** WordPress admin > Divi > Theme Customizer and Divi > Module Customizer
    **Key features:** Live preview of all changes, hundreds of global style settings, per-module default overrides
    **ET Docs:** [Official documentation](https://www.elegantthemes.com/documentation/divi/customizer)

## Overview

Divi 5 provides two customizer interfaces that control the default visual appearance of your entire site. The **Theme Customizer** handles site-wide structural elements such as the header, navigation menus, logo placement, body text, heading typography, footer layout, and general color schemes. The **Module Customizer** controls the default size, font, color, and spacing values for each individual module type, so changes propagate across every instance of that module site-wide.

Both customizers use the WordPress Customizer framework, which means every change you make is previewed live before you publish. This makes it safe to experiment with global style adjustments without affecting the live site until you click **Save & Publish**.

The customizers complement the Visual Builder's per-element styling. Settings made in the customizer act as defaults — they apply everywhere unless overridden at the individual module, row, or section level in the builder. This hierarchy means you can establish a consistent baseline in the customizer and then fine-tune specific instances in the builder as needed.

<!-- ![Theme & Module Customizer overview](../assets/screenshots/theme-options/customizer/overview.png){ loading=lazy } -->
<!-- *The Theme & Module Customizer interface in Divi 5.* -->

## Accessing the Customizers

### Theme Customizer

1. Log in to WordPress as an Administrator.
2. Navigate to **Divi > Theme Customizer** in the WordPress admin sidebar.
3. The WordPress Customizer interface opens with Divi's theme panels in the left sidebar and a live preview of your site on the right.

### Module Customizer

1. Log in to WordPress as an Administrator.
2. Navigate to **Divi > Module Customizer** in the WordPress admin sidebar.
3. The Customizer opens with a panel for each Divi module type.

!!! tip "Access via the Admin Bar"
    When logged in and viewing the front end of your site, you can also access the Theme Customizer from the WordPress admin bar under **Customize**.

## Theme Customizer Panels

The Theme Customizer organizes settings into several top-level panels, each containing sub-panels for specific site elements.

### Header & Navigation

Controls the appearance and behavior of the site header, logo, and navigation menus.

| Sub-Panel | Settings |
|-----------|----------|
| **Header Format** | Header style (default, centered, slide-in, fullscreen), header height, hide navigation until scroll toggle |
| **Primary Menu Bar** | Background color, menu link color, active link color, menu height, dropdown menu animation, text size, font weight, letter spacing, text transform |
| **Secondary Menu Bar** | Background color, text color, text size, font, icon size, dropdown styling |
| **Fixed Navigation** | Fixed header background color, fixed header link color, fixed header height, transition effects |
| **Header Elements** | Show/hide search icon, show/hide social icons, social icon URLs, show/hide cart icon (WooCommerce) |
| **Logo** | Logo max height, logo positioning, hide logo image toggle |

### General Settings

Controls fundamental site-wide styling properties.

| Sub-Panel | Settings |
|-----------|----------|
| **Layout** | Website content width (px), sidebar width, use boxed layout toggle, section height, row width, gutter width |
| **Typography** | Body text size, body line height, body font, header text size (H1-H6), header font, header font weight, header text color, header letter spacing, header line height |
| **Background** | Default page background color, default page background image, background image position, background size |
| **Color Scheme** | Accent color (site-wide highlight color used for links, buttons, and active states) |

### Buttons

Controls the default appearance of button elements across the site.

| Setting | Description |
|---------|-------------|
| Button Text Size | Default font size for all buttons |
| Button Text Color | Default text color for all buttons |
| Button Background Color | Default fill color |
| Button Border Width | Default border thickness |
| Button Border Color | Default border color |
| Button Border Radius | Corner rounding value |
| Button Font | Font family for button text |
| Button Text Transform | Uppercase, lowercase, capitalize, or none |
| Button Letter Spacing | Spacing between characters |
| Button Hover Text Color | Text color on hover |
| Button Hover Background Color | Fill color on hover |
| Button Hover Border Color | Border color on hover |
| Button Hover Letter Spacing | Letter spacing on hover |
| Button Icon | Default icon displayed next to button text |
| Button Icon Color | Icon color |
| Button Icon Placement | Left or right of button text |
| Button Show Icon on Hover | Toggle whether icon appears only on hover |

### Footer

Controls the bottom-of-page footer area.

| Sub-Panel | Settings |
|-----------|----------|
| **Footer Layout** | Number of footer columns, show/hide bottom bar, footer background color |
| **Footer Elements** | Show/hide social icons, show/hide footer menu |
| **Footer Typography** | Footer widget heading font, size, color; footer widget body text font, size, color |
| **Bottom Bar** | Background color, text color, text alignment |

### Mobile Styles

Controls how the site adapts to tablet and phone screen sizes.

| Sub-Panel | Settings |
|-----------|----------|
| **Mobile Menu** | Mobile menu background color, link color, link size, breakpoint |
| **Tablet** | Section height, row width, body text size, header text sizes |
| **Phone** | Section height, row width, body text size, header text sizes |

## Module Customizer Panels

The Module Customizer provides a panel for each Divi module type. Within each panel, you can set default values for that module's key visual properties. These defaults apply to every instance of the module across the site unless overridden in the individual module's settings.

Common settings available per module include:

| Setting Category | Controls |
|-----------------|----------|
| **Header Font Size** | Default heading text size for the module |
| **Header Font Style** | Bold, italic, uppercase, underline |
| **Header Font Color** | Default heading color |
| **Header Letter Spacing** | Character spacing for headings |
| **Header Line Height** | Line height for headings |
| **Body Font Size** | Default body text size |
| **Body Font Style** | Bold, italic, uppercase, underline |
| **Body Font Color** | Default body text color |
| **Body Letter Spacing** | Character spacing for body text |
| **Body Line Height** | Line height for body text |
| **Padding** | Top, bottom, left, right internal spacing |

Modules with unique visual elements have additional settings. For example:

- **Slider** — Slide height, slide padding, arrow size, dot navigation size
- **Blog** — Grid column count, meta font settings, read-more link styling
- **Bar Counter** — Bar height, bar background color, bar fill color
- **Blurb** — Icon size, icon color, image max width
- **Testimonial** — Quote icon color, portrait border radius
- **Pricing Table** — Header background color, price font size, bullet icon color

## Theme Customizer vs. Module Customizer

| Aspect | Theme Customizer | Module Customizer |
|--------|-----------------|-------------------|
| **Scope** | Site-wide structural elements (header, footer, typography, colors) | Per-module-type default values |
| **Access** | Divi > Theme Customizer | Divi > Module Customizer |
| **What it controls** | Header layout, navigation styles, global typography, button defaults, footer | Font sizes, colors, spacing, and module-specific dimensions for each module type |
| **Override behavior** | Builder page-level and element-level settings override these | Individual module settings in the builder override these |
| **Best for** | Establishing the site's foundational design system | Ensuring consistent module styling without configuring each instance |

## Settings Hierarchy

Divi applies styles in a cascading hierarchy. Settings at higher levels act as defaults that lower levels can override:

1. **Theme Customizer** — Broadest defaults (site-wide typography, colors, header/footer)
2. **Module Customizer** — Per-module-type defaults
3. **Global Presets** — Saved style configurations applied to specific module instances
4. **Individual Module Settings** — Per-instance overrides in the Visual Builder

This means you can set a site-wide heading font in the Theme Customizer, override it for all Blurb modules in the Module Customizer, and then further override it for a single Blurb instance in the Visual Builder.

## Best Practices

1. **Configure the Theme Customizer first** — Establish your global typography, colors, and header/footer styles before building pages. This reduces the amount of per-module styling you need to do in the builder.

2. **Use the Module Customizer for consistency** — If you find yourself applying the same font size or padding to every instance of a module, set it once in the Module Customizer instead. This keeps your styling DRY and easier to update later.

3. **Preview before publishing** — Both customizers show live previews. Test changes across different page types (homepage, blog posts, archives) by navigating within the preview pane before clicking Save & Publish.

4. **Document your customizer settings** — Use the Divi Portability feature to export your Theme Options (which include customizer values) as a backup. Store the export alongside your site documentation for disaster recovery or site migration.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Customizer interface and available settings may differ from Divi 4.

## Troubleshooting

!!! warning "Customizer Changes Not Appearing"
    If changes made in the customizer do not reflect on the live site:

    - Confirm you clicked **Save & Publish** in the Customizer, not just the preview close button.
    - Clear all caching layers: browser cache, WordPress page cache, server-level cache (Cloudflare, Varnish, etc.).
    - Check whether per-module settings in the Visual Builder are overriding your customizer values. Builder-level settings take precedence over customizer defaults.

!!! warning "Theme Customizer Panel Missing"
    If the Divi > Theme Customizer link is not visible in the admin menu:

    - Verify your user role has Theme Customizer access in the [Role Editor](../builder/role-editor.md).
    - Ensure Divi 5 is the active theme (not a child theme that fails to load properly).
    - Deactivate other plugins temporarily to check for conflicts that may remove customizer panels.

!!! tip "Resetting Customizer Values"
    There is no single "reset all" button in the customizer. To restore defaults, either import a saved Divi options backup via the Portability feature, or manually clear individual fields. For the Module Customizer, emptying a field reverts it to the theme's built-in default.

## Related

- [General Settings](general.md) — Divi theme general options panel
- [Navigation Settings](navigation.md) — Navigation-specific theme options
- [Layout Settings](layout.md) — Layout-specific theme options
- [Role Editor](../builder/role-editor.md) — Control which roles can access the Theme Customizer
