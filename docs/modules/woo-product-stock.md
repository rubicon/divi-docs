---
title: "Woo Product Stock"
description: "Divi 5 Woo Product Stock module — WooCommerce product stock status and inventory count display with customizable styling."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product", "inventory", "stock"]
related: ["woo-product-price", "woo-product-information"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12041304"
---

# Woo Product Stock

The Woo Product Stock module displays the stock status and inventory count for a WooCommerce product.

!!! abstract "Quick Reference"
    **What it does:** Shows the product stock quantity and availability status (in stock, out of stock, on backorder) pulled from WooCommerce inventory settings.
    **When to use it:** Product page templates, custom product layouts in the Theme Builder
    **Key settings:** In Stock Text styling, Out of Stock Text styling, On Backorder Text styling, Loop Builder
    **Block identifier:** `divi/woo-product-stock`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12041304)

!!! tip "When to Use This Module"
    - Displaying stock availability on custom product page templates
    - Creating urgency with low-stock indicators near the add-to-cart area
    - Showing distinct styling for in-stock, out-of-stock, and backorder statuses

!!! warning "When NOT to Use This Module"
    - On non-WooCommerce pages — this module requires a product context
    - When stock management is disabled in WooCommerce — the module will show no data
    - For product pricing — use [Woo Product Price](woo-product-price.md)

## Overview

The Woo Product Stock module pulls inventory data directly from the WooCommerce product listing's Inventory section and displays the stock quantity and status on the front end. It supports three stock states — in stock, out of stock, and on backorder — each of which can be styled independently through the Design tab.

This module is particularly useful for products where stock visibility drives purchasing decisions. Showing "Only 3 left in stock" creates urgency that can increase conversion rates. For products on backorder, the module communicates availability expectations so customers know what to expect before purchasing.

The stock data is fully dynamic. When you update inventory quantities in WooCommerce (either manually or through order fulfillment), the module output updates automatically on the front end. For the module to display any data, stock management must be enabled on the individual product under Product Data > Inventory, and the "Stock quantity" field must be filled in.

The module also supports the Loop Builder, allowing you to display stock information for multiple products in a dynamic loop context outside of the standard product page template.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated. It will not appear in the module picker if WooCommerce is absent.

[View the official Elegant Themes documentation for this module.](https://help.elegantthemes.com/en/articles/12041304)

<!-- ![Woo Product Stock module overview](../assets/screenshots/modules/woo-product-stock/overview.png){ loading=lazy } -->
<!-- *The Woo Product Stock module as it appears in the Divi 5 Visual Builder.* -->

## Use Cases

1. **Urgency-Driven Product Page** — Place the stock module directly below or beside the [Woo Product Price](woo-product-price.md) module and above the add-to-cart button. Style the in-stock text in green and use a bold font weight. When stock drops to low quantities, the visible count creates urgency that encourages immediate purchasing.

2. **Backorder Communication** — Style the on-backorder text in a distinct color (such as amber or orange) to clearly communicate that the product is available but will ship later. This sets customer expectations upfront and reduces support inquiries about delivery timelines.

3. **Inventory Dashboard Layout** — Use the Loop Builder integration to display stock status for multiple products on a single page. This can serve as an internal reference for store managers or as a public "availability" page showing which products are currently in stock.

## How to Add the Woo Product Stock Module

1. Ensure WooCommerce is installed, activated, and that the product has stock management enabled under Product Data > Inventory with a stock quantity entered.
2. Open the Visual Builder on a product page template or any page. Click the gray **+** icon to add a new module to a row.
3. Search for "Woo Product Stock" in the module picker or find it in the WooCommerce category, then click to insert it.

## Settings & Options

The Woo Product Stock module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which product's stock information is displayed and provides access to the Loop Builder for dynamic contexts.

| Setting | Type | Description |
|---------|------|-------------|
| Content | select | Choose the product for which you want to display the stock status. On Theme Builder templates, this defaults to the current product dynamically. |
| Link | url | Optionally make the entire module clickable, directing visitors to a specified URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the module. |
| Loop | toggle | Enable the Loop Builder to display stock information in a dynamic loop context for multiple products. |
| Order | select | Control the module's placement order within Flexbox and Grid parent layouts. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |

### Design Tab

The Design tab provides independent styling controls for each stock status state, allowing you to visually differentiate between in-stock, out-of-stock, and backorder products.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Text | alignment controls | Set the text alignment for the stock status display (left, center, right, justified). |
| In Stock Text | text styling | Customize the font, size, color, weight, line height, and letter spacing for the in-stock status message. Use green tones to signal availability. |
| Out of Stock Text | text styling | Style the out-of-stock status message independently. Typically styled in red or gray to indicate unavailability. |
| On Backorder Text | text styling | Style the backorder status message with distinct typography. Amber or orange tones communicate "available but delayed" effectively. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, min-height, height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding with responsive breakpoint controls |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Horizontal/vertical offset, blur, spread, color, position |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue rotation, blur, invert, sepia, opacity, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, direction, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (stock text, container) |
| HTML | Semantic HTML tag selection for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

## Code Examples

### Custom CSS

```css
/* Style the stock status display */
.et_pb_wc_stock .stock {
    font-weight: 600;
    font-size: 14px;
    padding: 8px 16px;
    border-radius: 4px;
    display: inline-block;
}

/* In-stock styling with green indicator */
.et_pb_wc_stock .stock.in-stock {
    color: #27ae60;
    background-color: #eafaf1;
    border: 1px solid #27ae60;
}

/* Out-of-stock styling with red indicator */
.et_pb_wc_stock .stock.out-of-stock {
    color: #e74c3c;
    background-color: #fdedec;
    border: 1px solid #e74c3c;
}

/* Backorder styling with amber indicator */
.et_pb_wc_stock .stock.available-on-backorder {
    color: #f39c12;
    background-color: #fef9e7;
    border: 1px solid #f39c12;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_stock .stock {
        font-size: 13px;
        text-align: center;
        width: 100%;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Product Stock module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_stock' !== $render_slug) {
        return $output;
    }
    // Example: Add an icon before stock status text
    $output = str_replace('class="stock in-stock"', 'class="stock in-stock"', $output);
    return $output;
}, 10, 2);

/* Customize WooCommerce stock display text */
add_filter('woocommerce_get_availability_text', function($availability, $product) {
    if ($product->is_in_stock()) {
        $stock_qty = $product->get_stock_quantity();
        if ($stock_qty !== null && $stock_qty <= 5) {
            return sprintf('Only %d left — order soon!', $stock_qty);
        }
    }
    return $availability;
}, 10, 2);
```

## Common Patterns

1. **Price and Stock Pairing** — Place the Woo Product Stock module directly below the [Woo Product Price](woo-product-price.md) module in the same column. This gives customers immediate visibility into both cost and availability, which are the two most important factors in a purchasing decision.

2. **Color-Coded Status Badges** — Use the independent text styling for each stock state to create badge-like displays. Green background with green text for in-stock, red for out-of-stock, and amber for backorder. This provides instant visual communication of product availability.

3. **Low-Stock Urgency** — Combine the stock module with WooCommerce's low stock threshold setting. When stock drops below the threshold, WooCommerce changes the display text to show the remaining quantity. Style this with a bold red font to create urgency and drive conversions.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API** produces content
    that renders on the front end but may not appear in the Visual Builder layer
    view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/woo-product-stock` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Product | `attrs.product` | Target product for stock display |
| Loop | `attrs.loop` | Enable Loop Builder context |

!!! tip "Module Selection Guidance"
    For stock status and quantity use Woo Product Stock; for pricing use Woo Product Price; for general product details use Woo Product Information.

## Saving Your Work

After configuring the Woo Product Stock module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple product templates, or added to your Divi Library for reuse by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Woo Product Stock module in Divi 5 benefits from the updated rendering engine and supports Conditions, Interactions, Scroll Effects, and the Loop Builder not available in Divi 4.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated. Stock management must be enabled on individual products for the module to display data. WooCommerce 7.0 or later is recommended for full Divi 5 compatibility.

## Troubleshooting

!!! warning "Module Shows No Stock Information"
    If the module appears but displays nothing, verify that stock management is enabled on the product. Go to the product editor in WooCommerce, click Product Data > Inventory, check "Manage stock," and enter a stock quantity. Products without stock management enabled will not output any stock display.

!!! warning "Stock Count Not Updating"
    If the stock count does not reflect recent orders, verify that WooCommerce is configured to reduce stock on order completion. Check WooCommerce > Settings > Products > Inventory > Manage Stock. Also clear any page caching that may be serving stale content.

!!! tip "Stock Status Shows for Some Products But Not Others"
    WooCommerce allows stock management to be enabled per-product. If stock status appears for some products but not others, check each product's Inventory tab individually. Products set to "Do not manage stock" will not provide data to this module.

## Related

- [Woo Product Price](woo-product-price.md)
- [Woo Product Information](woo-product-information.md)
