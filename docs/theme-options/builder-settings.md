---
title: "Builder Settings"
category: theme-options
tags: [theme-options, builder, post-types, css, woocommerce, classic-editor]
related: [general, layout]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/theme-options/"
---

# Builder Settings

The Builder Settings tab controls which post types can use the Divi Builder and provides advanced options for CSS generation and editor preferences.

## Overview

In the Builder Settings tab there are two sub-tabs: **Post Type Integration** and **Advanced**.

The **Post Type Integration** sub-tab lets you enable the Divi Builder on custom post types beyond standard posts and pages, and configure WooCommerce product page layout options. The **Advanced** sub-tab contains settings for static CSS file generation, inline style output, the product tour, and editor preferences including the option to use the Classic Editor instead of Gutenberg.

<!-- ![Builder Settings overview](../assets/screenshots/theme-options/builder-settings/overview.png){ loading=lazy }
*The Builder Settings panel in Divi Theme Options.* -->

## Settings & Options

### Post Type Integration

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable Divi Builder On Post Types | select | Posts, Pages | By default, the Divi Builder is only accessible on standard post types. This option lets you enable the builder on any custom post type currently registered on your website. Note that the builder may not be compatible with all custom post types. |
| Product Layout | select | Default | Choose the Product Page Layout for WooCommerce. |
| Product Content | select | Default | "Build From Scratch" loads a pre-built WooCommerce page layout that you can build on when the Divi Builder is enabled. The "Default" option uses the default WooCommerce page layout. |

### Advanced

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Static CSS File Generation | toggle | Enabled | When enabled, the builder's inline CSS styles for all pages will be cached and served as static files. Enabling this can help improve performance. |
| Output Styles Inline | toggle | Disabled | With previous versions of the builder, CSS styles for module design settings were output inline in the footer. Enable this to restore that behavior. |
| Product Tour | toggle | Enabled | When enabled, the Product Tour will start automatically when the Visual Builder is launched for the first time. |
| Enable The Latest Divi Builder Experience | toggle | Enabled | Disabling this option loads the legacy Divi Builder interface when editing a post using the classic WordPress post editor. The legacy builder lacks many features and interface improvements. |
| Enable Classic Editor | toggle | Disabled | Enable this option to use the Classic Editor instead of Gutenberg / Block Editor. |

## Code Examples

```php
// Check which post types have the builder enabled
$builder_post_types = et_get_option('et_builder_post_types');

// Check if static CSS generation is enabled
$static_css = et_get_option('et_pb_static_css_file', 'on');

// Check if Classic Editor is enabled
$classic_editor = et_get_option('et_enable_classic_editor', 'off');
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Builder Not Available on Custom Post Types"
    If the Divi Builder doesn't appear on a custom post type after enabling it in Post Type Integration, verify that the custom post type supports the `editor` feature. Some custom post types may not be fully compatible with the Divi Builder.

## Related

- [General Settings](general.md)
- [Layout Settings](layout.md)
- [Integration Settings](integration.md)
