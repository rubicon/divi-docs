---
title: "Woo Checkout Details"
description: "Divi 5 Woo Checkout Details module — WooCommerce order summary table showing cart products, quantities, subtotals, and total at checkout with customizable table styling."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "checkout", "order-summary"]
related: ["woo-checkout-billing", "woo-checkout-information"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12095369"
---

# Woo Checkout Details

The Woo Checkout Details module displays the order summary table on the WooCommerce checkout page, showing products, quantities, subtotals, and the total amount due.

!!! abstract "Quick Reference"
    **What it does:** Shows the list of products in the cart with individual subtotals, shipping, taxes, and the grand total on the checkout page.
    **When to use it:** Custom checkout page templates in the Theme Builder
    **Key settings:** Title Text, Column Label, Body Text, Table/Row/Cell styling
    **Block identifier:** `divi/woo-checkout-details`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12095369)

!!! tip "When to Use This Module"
    - Building a custom WooCommerce checkout page template in the Theme Builder
    - Displaying the order summary so customers can review items before completing purchase
    - Pairing with billing, shipping, and payment modules for a complete checkout flow

!!! warning "When NOT to Use This Module"
    - On non-checkout pages — this module requires the WooCommerce checkout context
    - For cart page product listings — use [Woo Cart Products](woo-cart-products.md)
    - For displaying a product catalog — use [Shop](shop.md)

## Overview

The Woo Checkout Details module provides the order review section of the WooCommerce checkout page. It renders a table listing every product in the customer's cart along with its quantity and line total, followed by the subtotal, applicable shipping costs, taxes, and the final total amount. This gives customers one last opportunity to verify their order before clicking "Place Order."

Unlike the Woo Cart Products module (which allows quantity editing and item removal), the Checkout Details module is read-only. It serves as a confirmation summary, not an editing interface. If a customer needs to change their order, they must return to the cart page. The table structure mirrors the standard WooCommerce order review table, with the same columns and row organization that WooCommerce plugins and payment gateways expect.

The design options focus on table presentation with controls for styling the title, column labels, body text, and individual table rows and cells. This allows you to create everything from a minimal, text-focused summary to a richly styled order review card with colored backgrounds and custom borders. For the official Elegant Themes documentation, see the [Woo Checkout Details help article](https://help.elegantthemes.com/en/articles/12095369).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active. It will not appear in the module picker without WooCommerce.

## Use Cases

1. **Clean Order Review Card** — Style the module with a white background, subtle box shadow, and rounded border radius to create a floating card that clearly separates the order summary from surrounding form fields. Use the Title Text options to make "Your Order" prominent and easily scannable.

2. **Two-Column Checkout Layout** — Place the Checkout Details module in a sidebar column alongside the billing and payment forms. This keeps the order summary visible at all times while the customer fills in their information, reducing anxiety about what they are purchasing.

3. **Highlighted Promotional Checkout** — During sales events, style the order summary with a themed background color and prominent total row styling. This reinforces the savings customers are getting and creates visual urgency to complete the purchase.

## How to Add the Woo Checkout Details Module

1. Ensure WooCommerce is installed and activated. Navigate to the Theme Builder and create or edit the template assigned to the WooCommerce checkout page.
2. Open the Visual Builder on your checkout page template. Click the gray **+** icon to add a new module to a row.
3. Search for "Woo Checkout Details" in the module picker or find it in the WooCommerce category, then click to insert it. The module will display the order summary based on the current cart contents.

## Settings & Options

The Woo Checkout Details module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the module's background and layout positioning. The order summary data is pulled automatically from WooCommerce cart contents.

| Setting | Type | Description |
|---------|------|-------------|
| Background | background controls | Set a background color, gradient, image, or video behind the order summary module. |
| Loop | toggle | Enable the loop builder to use this module within a loop context. |
| Order | select | Set the Flexbox order of the module within its parent row. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |

### Design Tab

The Design tab provides controls for styling the order summary table, including typography for headings and data, and row/cell appearance.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Title Text | text styling | Customize the font, size, weight, and color of the "Your Order" heading above the summary table. |
| Column Label | text styling | Style the column header text (Product, Total) including font, size, weight, and color. |
| Body Text | text styling | Style the product names, quantities, and price text within the table body. |
| Table | styling controls | Configure the overall table appearance including background color, borders, and spacing. |
| Table Row | styling controls | Style individual rows including alternating backgrounds, padding, and border separators. |
| Table Cell | styling controls | Control individual cell appearance including padding, alignment, and borders. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
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
| [CSS](../options-groups/css.md) | Custom CSS per element target (table, rows, cells, headings) |
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
/* Style the order review as a card */
.et_pb_wc_checkout_order_details .woocommerce-checkout-review-order-table {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
    overflow: hidden;
}

/* Style the "Your Order" heading */
.et_pb_wc_checkout_order_details h3 {
    font-size: 20px;
    font-weight: 700;
    padding: 20px 24px;
    margin: 0;
    background-color: #f8f9fa;
    border-bottom: 1px solid #e5e5e5;
}

/* Style table header row */
.et_pb_wc_checkout_order_details table thead th {
    padding: 14px 24px;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 12px;
    letter-spacing: 0.5px;
    background-color: #fafafa;
}

/* Style product rows */
.et_pb_wc_checkout_order_details table tbody td {
    padding: 14px 24px;
    border-bottom: 1px solid #f0f0f0;
}

/* Emphasize the total row */
.et_pb_wc_checkout_order_details table tfoot .order-total td,
.et_pb_wc_checkout_order_details table tfoot .order-total th {
    font-size: 18px;
    font-weight: 700;
    padding: 18px 24px;
    background-color: #f0f7ff;
}

/* Responsive adjustments */
@media (max-width: 767px) {
    .et_pb_wc_checkout_order_details table thead th,
    .et_pb_wc_checkout_order_details table tbody td {
        padding: 10px 16px;
        font-size: 14px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Checkout Details module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_checkout_order_details' !== $render_slug) {
        return $output;
    }
    return $output;
}, 10, 2);

/* Add product thumbnails to the checkout order review */
add_filter('woocommerce_cart_item_name', function($name, $cart_item, $cart_item_key) {
    if (is_checkout()) {
        $product = $cart_item['data'];
        $thumbnail = $product->get_image(array(40, 40), array('class' => 'checkout-thumb'));
        $name = $thumbnail . '<span class="checkout-product-name">' . $name . '</span>';
    }
    return $name;
}, 10, 3);

/* Add a savings summary row to the checkout order review */
add_action('woocommerce_review_order_after_order_total', function() {
    $discount = WC()->cart->get_discount_total();
    if ($discount > 0) {
        echo '<tr class="savings-row"><th>You Save</th><td>' . wc_price($discount) . '</td></tr>';
    }
});
```

## Common Patterns

1. **Sticky Order Summary Sidebar** — Place the Checkout Details module in a one-third sidebar column and use Position settings to make it sticky. As customers scroll through billing and shipping forms, the order summary remains visible, providing constant reassurance about what they are purchasing and the total cost.

2. **Compact Order Review** — Apply tight padding to table cells and use a smaller font size for body text to create a compact summary that does not dominate the checkout layout. This works well when the order details are placed above the payment section in a single-column checkout design.

3. **Order Summary with Product Images** — Use the PHP hook above to inject product thumbnails into the order review table. Combined with custom CSS to align the images with product names, this creates a visual order summary that helps customers confirm they have the right items, especially important for stores with many similar products.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API** produces content that
    renders on the front end but may not appear in the Visual Builder layer view.
    Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/woo-checkout-details` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

## Saving Your Work

After configuring the Woo Checkout Details module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple checkout templates, or added to your Divi Library for reuse by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Woo Checkout Details module in Divi 5 supports Conditions, Interactions, Scroll Effects, and enhanced layout controls not available in Divi 4.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active.

## Troubleshooting

!!! warning "Order Summary Shows Empty Table"
    If the module renders but shows no products, verify that the template is assigned to the WooCommerce checkout page in the Theme Builder. The module pulls data from the active WooCommerce cart session. Also ensure you have products in the cart when previewing — use a separate tab to add products, then navigate to the checkout page.

!!! warning "Totals Do Not Match Cart Page"
    If the order total on the checkout page differs from the cart page, check for shipping costs, taxes, or coupons that may apply differently at checkout. WooCommerce recalculates totals on the checkout page based on the entered billing/shipping address, which may change tax and shipping amounts.

!!! tip "Order Review Not Updating When Payment Method Changes"
    Some payment gateways add surcharges that should update the order total. If the order review table does not refresh when switching payment methods, this may be a gateway plugin issue. Check for JavaScript errors in the browser console and ensure the payment gateway plugin is up to date.

## Related

- [Woo Checkout Billing](woo-checkout-billing.md)
- [Woo Checkout Information](woo-checkout-information.md)
