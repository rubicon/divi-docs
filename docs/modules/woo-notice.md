---
title: "Woo Notice"
description: "Complete Divi 5 Woo Notice module reference — settings, design options, code examples, and troubleshooting for WooCommerce notice messages on product, cart, and checkout pages."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "notices", "alerts", "cart", "checkout"]
related: ["woo-cart-products", "woo-checkout-billing"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12032822"
---

# Woo Notice

The Woo Notice module displays WooCommerce notification messages — such as success confirmations, error alerts, and informational notices — on product, cart, and checkout pages.

!!! abstract "Quick Reference"
    **What it does:** Renders WooCommerce notice messages (success, error, info) for the selected page context.
    **When to use it:** Custom WooCommerce page templates built in the Divi Theme Builder
    **Key settings:** Page Type, Product, Background, Text
    **Block identifier:** `divi/wc-notice`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12032822)

!!! tip "When to Use This Module"
    - Building a custom product page template that needs to show add-to-cart confirmation messages
    - Creating a custom cart page where notice banners should appear after quantity changes or coupon applications
    - Designing a checkout page template that must display validation errors and payment status messages

!!! warning "When NOT to Use This Module"
    - On pages without WooCommerce context — notices require WooCommerce page data to render
    - For custom alert banners unrelated to WooCommerce — use a [Text](text.md) module with styled admonitions instead
    - For static promotional banners — use [Call to Action](call-to-action.md)

## Overview

The Woo Notice module serves as the designated area for WooCommerce system messages within custom Theme Builder templates. WooCommerce generates notices in three categories: success messages (such as "Product added to cart"), error messages (such as validation failures during checkout), and informational notices (such as coupon details or shipping threshold alerts). Without this module placed in your template, these critical messages would have nowhere to render, leaving customers without feedback on their actions.

The module adapts its output based on the **Page Type** setting, which determines whether it pulls notices relevant to a single product page, the cart, or the checkout flow. On product pages, it typically displays add-to-cart confirmations with a "View Cart" button. On cart pages, it shows messages related to coupon applications, quantity updates, or stock issues. On checkout pages, it handles form validation errors and payment processing feedback.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12032822).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. Notices will only appear when WooCommerce triggers them through user actions.

<!-- ![Woo Notice module](../assets/screenshots/modules/woo-notice/element.png){ loading=lazy } -->
<!-- *The Woo Notice module displaying a success message after adding a product to the cart.* -->

## Use Cases

1. **Product Page Confirmation** — Place the module at the top of a custom single product template so that "Product added to cart" messages appear prominently with a link to the cart, giving customers immediate feedback after clicking the add-to-cart button.
2. **Cart Page Alerts** — Position the module above the cart table on a custom cart template to display coupon success/error messages, stock warnings, and shipping threshold notifications as customers modify their cart.
3. **Checkout Validation Feedback** — Include the module at the top of a custom checkout template so that form validation errors (missing fields, invalid payment details) appear clearly, guiding customers to correct issues before resubmitting.

## How to Add the Woo Notice Module

1. Navigate to **Divi > Theme Builder** and create or edit a template assigned to a WooCommerce page (product, cart, or checkout).
2. Open the Visual Builder on the template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Notice" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12032822).

## Settings & Options

The Woo Notice module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which page context the module targets, the product selection for preview, and the module's background and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Page Type | select | Choose which WooCommerce page context the notices apply to: Product, Cart, or Checkout. This determines which set of WooCommerce notices the module renders. |
| Product | product selector | Select a specific published product to preview notice output in the Visual Builder. This setting helps you see what the notice will look like during editing. |
| Background | background controls | Set a background color, gradient, image, or video behind the notice module container. |
| Meta | admin label | Assign an admin label for the module and control its visibility inside the Visual Builder. |

<!-- ![Woo Notice Content tab settings](../assets/screenshots/modules/woo-notice/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the typography and visual presentation of notice text, buttons, and the module container.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Title Text | text styling | Customize the font family, weight, size, color, alignment, and letter spacing of notice title text. |
| Body Text | text styling | Style the body text and any links within the notice message, including font, color, size, and link hover behavior. |
| Button | button styling | Control the appearance of buttons within notices (such as the "View Cart" button), including background color, text color, border, padding, and hover effects. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, hue, saturation, blending) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Woo Notice Design tab settings](../assets/screenshots/modules/woo-notice/settings-design.png){ loading=lazy } -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Choose the semantic HTML tag for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

<!-- ![Woo Notice Advanced tab settings](../assets/screenshots/modules/woo-notice/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the notice container */
.et_pb_wc_notice {
    margin-bottom: 20px;
}

/* Style success notices */
.et_pb_wc_notice .woocommerce-message {
    background: #e8f5e9;
    border-left: 4px solid #4caf50;
    padding: 15px 20px;
    border-radius: 4px;
    color: #2e7d32;
}

/* Style error notices */
.et_pb_wc_notice .woocommerce-error {
    background: #fce4ec;
    border-left: 4px solid #e53935;
    padding: 15px 20px;
    border-radius: 4px;
    color: #c62828;
}

/* Style informational notices */
.et_pb_wc_notice .woocommerce-info {
    background: #e3f2fd;
    border-left: 4px solid #1e88e5;
    padding: 15px 20px;
    border-radius: 4px;
    color: #1565c0;
}

/* Style the View Cart button inside notices */
.et_pb_wc_notice .woocommerce-message .button {
    background: #4caf50;
    color: #fff;
    border-radius: 4px;
    padding: 8px 16px;
    float: right;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_notice .woocommerce-message .button {
        float: none;
        display: block;
        margin-top: 10px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Notice module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_notice' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Add a custom notice to WooCommerce */
add_action('woocommerce_before_cart', function() {
    wc_add_notice('Free shipping on orders over $50!', 'notice');
});
```

## Common Patterns

1. **Top-of-Page Notices** — Place the Woo Notice module in the first row of your template, spanning the full width, so that all system messages appear at the very top of the page where customers will see them immediately.

2. **Styled Alert Banners** — Apply custom border-left colors and background tints to differentiate success (green), error (red), and info (blue) notices visually, creating a consistent alert system that matches your store branding.

3. **Sticky Notice Bar** — Use the Position setting to make the notice module sticky at the top of the viewport, ensuring customers always see important messages like checkout validation errors even as they scroll the page.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-notice` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For WooCommerce system notices use Woo Notice; for static promotional messages use Call to Action or Text; for checkout-specific validation use Woo Notice with Page Type set to Checkout.

## Saving Your Work

After configuring the notice module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. Notices are generated dynamically by WooCommerce based on user actions — the module will appear empty until a notice-triggering event occurs.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Notice module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The Page Type setting matches the template context (Product, Cart, or Checkout)
    - The module is placed on a WooCommerce page template, not a regular page
    - Visibility settings are not hiding it on the current device

!!! warning "No Notices Displaying"
    If the module renders but shows no notices, this is expected behavior when no notice-triggering action has occurred. Notices appear only after events such as:

    - Adding a product to the cart (product page)
    - Applying or removing a coupon (cart page)
    - Submitting the checkout form with validation errors (checkout page)

!!! tip "Notices Disappearing Too Quickly"
    WooCommerce notices are session-based and typically display once per page load. If notices seem to vanish, check for AJAX-based page updates or caching plugins that may be interfering with the WooCommerce session data.

## Related

- [Woo Cart Products](woo-cart-products.md) — Displays the cart contents table on the cart page
- [Woo Checkout Billing](woo-checkout-billing.md) — Billing address form on the checkout page
- [Woo Checkout Payment](woo-checkout-payment.md) — Payment method selection on the checkout page
- [Woo Product Price](woo-product-price.md) — Product price display on single product pages
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
