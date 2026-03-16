---
title: "Woo Checkout Payment"
description: "Divi 5 Woo Checkout Payment module — WooCommerce payment method selection with radio buttons, gateway descriptions, terms acceptance, and place order button."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "checkout", "payment", "gateway"]
related: ["woo-checkout-billing", "woo-checkout-shipping"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12095382"
---

# Woo Checkout Payment

The Woo Checkout Payment module displays payment method selection, gateway descriptions, terms acceptance, and the "Place Order" button on the WooCommerce checkout page.

!!! abstract "Quick Reference"
    **What it does:** Renders payment gateway radio buttons, gateway-specific descriptions/tooltips, terms and conditions acceptance, and the Place Order submission button.
    **When to use it:** Custom checkout page templates in the Theme Builder
    **Key settings:** Radio Buttons styling, Selected Radio Buttons styling, Tooltip styling, Form Notice styling, Button styling
    **Block identifier:** `divi/woo-checkout-payment`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12095382)

!!! tip "When to Use This Module"
    - Building a custom WooCommerce checkout page template in the Theme Builder
    - Displaying available payment gateways (Stripe, PayPal, bank transfer, etc.)
    - Providing the final place-order action in a custom checkout flow

!!! warning "When NOT to Use This Module"
    - On non-checkout pages — this module requires the WooCommerce checkout context
    - For product add-to-cart buttons — use [Shop](shop.md) or Woo Product modules
    - For general button elements — use [Button](button.md)

## Overview

The Woo Checkout Payment module is the final and most critical component of the WooCommerce checkout flow. It renders all payment gateways configured in WooCommerce as selectable radio buttons, displays descriptive text for the selected payment method, optionally shows a terms and conditions checkbox, and provides the "Place Order" button that submits the order.

The payment methods displayed are pulled directly from your WooCommerce payment settings (WooCommerce > Settings > Payments). When a customer selects a different payment method, the tooltip area updates to show that gateway's description. For gateways that require additional input (such as credit card fields for Stripe), the input form appears within the tooltip area as well. The Form Notice styling option lets you customize how error messages appear when payment fails or when terms are not accepted.

This module must be present on the checkout page for customers to complete their purchase. Without it, there is no mechanism for payment selection or order submission. It pairs with the [Woo Checkout Billing](woo-checkout-billing.md), [Woo Checkout Shipping](woo-checkout-shipping.md), [Woo Checkout Details](woo-checkout-details.md), and [Woo Checkout Information](woo-checkout-information.md) modules to create a complete checkout experience. For the official Elegant Themes documentation, see the [Woo Checkout Payment help article](https://help.elegantthemes.com/en/articles/12095382).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active. It will not appear in the module picker without WooCommerce.

## Use Cases

1. **Two-Column Checkout with Sidebar Payment** — Place the payment module in a sidebar column alongside the billing and shipping forms. This keeps the payment options visible while customers fill out their details, creating a balanced layout that emphasizes the final action step.

2. **Sticky Payment Section** — Use Position settings to make the payment module sticky in a sidebar column. As customers scroll through long checkout forms, the payment options and Place Order button remain accessible, reducing the effort needed to complete the purchase.

3. **Branded Place Order Button** — Style the Place Order button with your brand's primary color, generous padding, and full width. Make it the most visually prominent element on the checkout page to direct attention toward completing the purchase. Apply hover effects that reinforce interactivity.

## How to Add the Woo Checkout Payment Module

1. Ensure WooCommerce is installed and activated with at least one payment gateway enabled (WooCommerce > Settings > Payments). Navigate to the Theme Builder and create or edit the template assigned to the WooCommerce checkout page.
2. Open the Visual Builder on your checkout page template. Click the gray **+** icon to add a new module to a row.
3. Search for "Woo Checkout Payment" in the module picker or find it in the WooCommerce category, then click to insert it. The module will display your configured payment gateways automatically.

## Settings & Options

The Woo Checkout Payment module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the module's background and layout positioning. Payment gateways are configured in WooCommerce settings, not within this module.

| Setting | Type | Description |
|---------|------|-------------|
| Background | background controls | Set a background color, gradient, image, or video behind the payment module. |
| Loop | toggle | Enable the loop builder to use this module within a loop context. |
| Order | select | Set the Flexbox order of the module within its parent row. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |

### Design Tab

The Design tab provides controls for styling the payment gateway radio buttons, their descriptions, error notices, and the Place Order button.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Body Text | text styling | Style the general body text content within the payment section. |
| Radio Buttons | styling controls | Customize the appearance of each payment method radio button including size, color, and spacing in their unselected state. |
| Selected Radio Buttons | styling controls | Style the active/selected state of payment method radio buttons, allowing you to differentiate the chosen payment method visually. |
| Tooltip | styling controls | Style the payment method description area that appears when a gateway is selected. This includes the background, text color, borders, and padding of the descriptive text panel. |
| Form Notice | styling controls | Style validation error messages that appear when payment fails or terms are not accepted. Customize background color, text color, border, and padding. |
| Button | styling controls | Customize the "Place Order" button including font, text color, background color, border, border radius, padding, and hover effects. This is the most important interactive element on the checkout page. |

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
| [CSS](../options-groups/css.md) | Custom CSS per element target (radio buttons, tooltip, button, form notices) |
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
/* Style the payment methods container */
.et_pb_wc_checkout_payment_info .wc_payment_methods {
    background: #fff;
    border-radius: 8px;
    border: 1px solid #e5e5e5;
    overflow: hidden;
    list-style: none;
    padding: 0;
    margin: 0;
}

/* Style individual payment method items */
.et_pb_wc_checkout_payment_info .wc_payment_methods li {
    padding: 16px 20px;
    border-bottom: 1px solid #f0f0f0;
}

.et_pb_wc_checkout_payment_info .wc_payment_methods li:last-child {
    border-bottom: none;
}

/* Style the selected payment method */
.et_pb_wc_checkout_payment_info .wc_payment_methods li.wc_payment_method input[type="radio"]:checked + label {
    font-weight: 600;
    color: #333;
}

/* Style the payment method description/tooltip area */
.et_pb_wc_checkout_payment_info .payment_box {
    background-color: #f8f9fa;
    padding: 16px 20px;
    margin-top: 12px;
    border-radius: 4px;
    font-size: 14px;
    color: #666;
}

/* Style the Place Order button */
.et_pb_wc_checkout_payment_info #place_order {
    background-color: #27ae60;
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 18px 32px;
    font-size: 18px;
    font-weight: 700;
    width: 100%;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.et_pb_wc_checkout_payment_info #place_order:hover {
    background-color: #219a52;
    transform: translateY(-2px);
}

/* Style error notices */
.et_pb_wc_checkout_payment_info .woocommerce-error {
    background-color: #fdf0f0;
    border-left: 4px solid #e74c3c;
    color: #c0392b;
    padding: 12px 16px;
    border-radius: 4px;
    margin-bottom: 16px;
}

/* Style the terms and conditions checkbox */
.et_pb_wc_checkout_payment_info .woocommerce-terms-and-conditions-wrapper {
    padding: 12px 0;
    font-size: 14px;
}

/* Responsive adjustments */
@media (max-width: 767px) {
    .et_pb_wc_checkout_payment_info #place_order {
        font-size: 16px;
        padding: 16px 24px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Checkout Payment module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_checkout_payment_info' !== $render_slug) {
        return $output;
    }
    return $output;
}, 10, 2);

/* Change the Place Order button text */
add_filter('woocommerce_order_button_text', function() {
    return 'Complete Purchase';
});

/* Add a security notice above the Place Order button */
add_action('woocommerce_review_order_before_submit', function() {
    echo '<div class="payment-security-notice">';
    echo '<span class="dashicons dashicons-lock"></span> ';
    echo 'Your payment information is encrypted and secure.';
    echo '</div>';
});

/* Add trust badges below the Place Order button */
add_action('woocommerce_review_order_after_submit', function() {
    echo '<div class="trust-badges" style="text-align:center; margin-top:16px;">';
    echo '<p style="font-size:12px; color:#999;">Secure checkout powered by SSL encryption</p>';
    echo '</div>';
});
```

## Common Patterns

1. **Card-Style Payment Options** — Style each payment method as a card by applying borders, padding, and a background color change on the selected state. This makes the payment selection feel more intentional and interactive than plain radio buttons. Use the Selected Radio Buttons option to apply a highlight color when a method is chosen.

2. **Prominent Place Order Button** — Make the Place Order button the most visually dominant element in the checkout flow. Use a high-contrast background color (green or your brand's primary color), generous padding, full width, uppercase text, and a subtle hover lift effect. Add a security message above the button using PHP hooks to increase customer confidence.

3. **Payment Below Order Summary** — Position the payment module directly below the Woo Checkout Details module so customers see exactly what they are paying for immediately before selecting a payment method and clicking Place Order. This creates a logical top-to-bottom flow: review items, choose payment, and submit.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API** produces content that
    renders on the front end but may not appear in the Visual Builder layer view.
    Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/woo-checkout-payment` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

## Saving Your Work

After configuring the Woo Checkout Payment module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple checkout templates, or added to your Divi Library for reuse by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Woo Checkout Payment module in Divi 5 supports Conditions, Interactions, Scroll Effects, and enhanced layout controls not available in Divi 4.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active.

## Troubleshooting

!!! warning "No Payment Methods Displaying"
    If the module renders but shows no payment options, verify that at least one payment gateway is enabled in WooCommerce > Settings > Payments. Check that the enabled gateways are available for your store's currency and the customer's billing country. Some gateways (like Stripe) require API keys to be configured before they appear.

!!! warning "Place Order Button Not Working"
    If clicking Place Order does nothing or shows a spinning indicator indefinitely, check the browser console for JavaScript errors. Common causes include conflicts with other plugins, expired nonces (try refreshing the page), or improperly configured payment gateways. Also verify that required billing and shipping fields are filled in correctly — incomplete form validation can silently block submission.

!!! tip "Terms and Conditions Checkbox Missing"
    The terms and conditions checkbox only appears if you have set a Terms and Conditions page in WooCommerce > Settings > Advanced > Page Setup. Create a page with your store's terms, then select it in the WooCommerce settings. The checkbox will then appear above the Place Order button.

## Related

- [Woo Checkout Billing](woo-checkout-billing.md)
- [Woo Checkout Shipping](woo-checkout-shipping.md)
