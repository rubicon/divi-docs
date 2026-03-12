---
title: "Shop"
category: modules
tags: ["modules", "woocommerce", "ecommerce"]
related: ["woo-products", "woo-product-price"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/ecommerce-divi/"
---

# Shop

The Shop module is a Divi 5 content element used in the Visual Builder.

## Overview

How to add, configure and customize the Divi shop module.

Divi has been designed to be WooCommerce compatible. To integrate WooCommerce you will need to install the latest version ofWooCommerce.

WooCommerce is the plugin that we recommend, as it has the nicest feature set, interface and follows the best coding practices. After you enabled the plugin, you will see a new “WooCommerce” and “Products” section has been added to your WordPress Dashboard. You can use these areas to adjust your eCommerce settings and publish new products. You can find fulldocumentation on WooCommerce here.

![Shop module overview](../assets/screenshots/modules/shop/overview.png){ loading=lazy }
*The Shop module as it appears in the Divi 5 Visual Builder.*

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Shop module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Content settings --> | | | |

![Shop Content tab settings](../assets/screenshots/modules/shop/settings-content.png){ loading=lazy }

### Design Tab

<!-- TODO: Verify all Design tab settings for Shop module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

![Shop Design tab settings](../assets/screenshots/modules/shop/settings-design.png){ loading=lazy }

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Shop module -->

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
/* Style the Shop module */
.et_pb_shop {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_shop {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Shop module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_shop' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Shop module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Shop module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

- [Woo Products](woo-products.md)
- [Woo Product Price](woo-product-price.md)
