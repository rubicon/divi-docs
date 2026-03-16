---
title: "Woo Product Reviews"
description: "Divi 5 Woo Product Reviews module — WooCommerce customer review list and review submission form with customizable styling."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product"]
related: []
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-reviews-module/"
---

# Woo Product Reviews

The Woo Product Reviews module displays customer reviews and a review submission form for WooCommerce products.

!!! abstract "Quick Reference"
    **What it does:** Renders the WooCommerce product review list and the leave-a-review form.
    **When to use it:** Product page templates, custom product layouts in the Theme Builder
    **Key settings:** Text color, Text styling, CSS customization, Visibility
    **Block identifier:** `divi/woo-product-reviews`
    **ET Docs:** [Official documentation](https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-reviews-module/)

!!! tip "When to Use This Module"
    - Building custom WooCommerce product pages with a dedicated reviews section
    - Displaying customer reviews and star ratings to build buyer trust
    - Positioning the reviews section independently in your product template layout

!!! warning "When NOT to Use This Module"
    - On non-WooCommerce pages → this module requires a product context
    - For average star rating only → use [Woo Product Rating](woo-product-rating.md)
    - For blog post comments → use [Comments](comments.md)

## Overview

How to add, configure and customize the Divi Woo Product Reviews module.

The Divi Woo Product Reviews Module integrates with WooCommerce and can display product reviews anywhere on your website. This is handy to use on product page templates, or anywhere on your website.

Before you can add the Divi Woo Product Reviews Module to your website, you’ll need to have the Divi theme and WooCommerce installed on your WordPress website. Learn how to install the Divi theme on your WordPress websitehereand how to install WooCommercehere. For additional information on the Divi Builder itself, its interface, usage philosophy and best practices, please refer to ourGetting Started With The Divi Builderguide.

<!-- TODO: Replace with proper screenshot -->
<!-- ![Woo Product Reviews module overview](../assets/screenshots/modules/woo-product-reviews/overview.png){ loading=lazy } -->
<!-- *The Woo Product Reviews module as it appears in the Divi 5 Visual Builder.* -->

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Woo Product Reviews module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Text Color– Choose the text color | text | — | light or dark. |
| WooCommerce Performance Optimization | text | — | 14 Tips & Best Practices |
| Updating WooCommerce | text | — | Best Practices to Follow Every Time |

<!-- TODO: Replace with proper screenshot -->
<!-- ![Woo Product Reviews Content tab settings](../assets/screenshots/modules/woo-product-reviews/settings-content.png){ loading=lazy } -->

### Design Tab

<!-- TODO: Verify all Design tab settings for Woo Product Reviews module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

<!-- TODO: Replace with proper screenshot -->
<!-- ![Woo Product Reviews Design tab settings](../assets/screenshots/modules/woo-product-reviews/settings-design.png){ loading=lazy } -->

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Woo Product Reviews module -->

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
/* Style the Woo Product Reviews module */
.et_pb_wc_product_reviews {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_product_reviews {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Product Reviews module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_wc_product_reviews' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Woo Product Reviews module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Product Reviews module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

<!-- TODO: Add related module links -->
