---
title: "Woo Products"
description: "Divi 5 Woo Products module — WooCommerce product gallery grid for featured, sale, and custom product collections with styling."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product"]
related: []
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/the-divi-woo-products-module/"
---

# Woo Products

The Woo Products module displays a gallery of WooCommerce products with options for featured, sale, and custom product collections.

!!! abstract "Quick Reference"
    **What it does:** Shows a grid of WooCommerce products with images, titles, prices, and filtering options.
    **When to use it:** Product page templates, homepage product showcases, custom shop layouts
    **Key settings:** Product type, Category filter, Columns, CSS customization, Visibility
    **Block identifier:** `divi/woo-products`
    **ET Docs:** [Official documentation](https://www.elegantthemes.com/documentation/divi/the-divi-woo-products-module/)

!!! tip "When to Use This Module"
    - Displaying curated product collections on homepage or landing pages
    - Showing featured or on-sale products in a product page template
    - Building custom shop layouts with filtered product grids

!!! warning "When NOT to Use This Module"
    - On non-WooCommerce sites → this module requires WooCommerce
    - For the main shop page with full sorting/filtering → use the [Shop](shop.md) module
    - For non-product content grids → use [Blog](blog.md) or [Portfolio](portfolio.md)

## Overview

How to add, configure and customize the Divi Woo Products module.

The Divi Woo Products Module displays a gallery of products on your website. It’s an easy way to add a collection of products anywhere on your website. Use the module to display featured products, on-sale products, limited-edition products, and customer favorites. In this doc, we’ll go over how to use the Woo Products module and all of the content and design settings available within the module.

View A Live Demo Of This Module

<!-- TODO: Replace with proper screenshot -->
<!-- ![Woo Products module overview](../assets/screenshots/modules/woo-products/overview.png){ loading=lazy } -->
<!-- *The Woo Products module as it appears in the Divi 5 Visual Builder.* -->

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Woo Products module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| WooCommerce Performance Optimization | text | — | 14 Tips & Best Practices |

<!-- ![Woo Products Content tab settings](../assets/screenshots/modules/woo-products/settings-content.png){ loading=lazy } -->

### Design Tab

<!-- TODO: Verify all Design tab settings for Woo Products module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

<!-- ![Woo Products Design tab settings](../assets/screenshots/modules/woo-products/settings-design.png){ loading=lazy } -->

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Woo Products module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| CSS ID | text | — | Assign a unique CSS ID to the module |
| CSS Class | text | — | Assign CSS classes to the module |
| Custom CSS | code | — | Add custom CSS directly to the module's elements |
| Visibility | toggle | Show on all devices | Control device visibility (desktop, tablet, phone) |
| Transition | select | Default | Animation transition style for hover effects |

## Code Examples

### Custom CSS

```css
/* Style the Woo Products module */
.et_pb_wc_products {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_products {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Products module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_wc_products' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Woo Products module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Products module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

<!-- TODO: Add related module links -->
