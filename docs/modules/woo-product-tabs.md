---
title: "Woo Product Tabs"
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product"]
related: []
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/divi-woo-product-tabs-module/"
---

# Woo Product Tabs

The Woo Product Tabs module is a Divi 5 content element used in the Visual Builder.

## Overview

How to add, configure and customize the Divi Woo Product Tabs module.

The Divi Woo Product Tabs integrate seamlessly with WooCommerce and allow you to display product information in a tabbed design. This module allows you to display additional information about a product in a succinct way, such as product dimensions, description, reviews and more.

The information displayed in the Divi Woo Product Tabs Module is pulled from the product listing. Specifically, this module can display the full description, attributes, shipping, and reviews sections of the product.

![Woo Product Tabs module overview](../assets/screenshots/modules/woo-product-tabs/overview.png){ loading=lazy }
*The Woo Product Tabs module as it appears in the Divi 5 Visual Builder.*

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Woo Product Tabs module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| WooCommerce Performance Optimization | text | — | 14 Tips & Best Practices |
| Updating WooCommerce | text | — | Best Practices to Follow Every Time |

![Woo Product Tabs Content tab settings](../assets/screenshots/modules/woo-product-tabs/settings-content.png){ loading=lazy }

### Design Tab

<!-- TODO: Verify all Design tab settings for Woo Product Tabs module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

![Woo Product Tabs Design tab settings](../assets/screenshots/modules/woo-product-tabs/settings-design.png){ loading=lazy }

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Woo Product Tabs module -->

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
/* Style the Woo Product Tabs module */
.et_pb_wc_product_tabs {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_product_tabs {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Product Tabs module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_wc_product_tabs' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Woo Product Tabs module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Product Tabs module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

<!-- TODO: Add related module links -->
