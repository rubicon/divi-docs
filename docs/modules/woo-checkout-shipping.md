---
title: "Woo Checkout Shipping"
description: "Complete Divi 5 Woo Checkout Shipping module reference — settings, design options, code examples, and troubleshooting for WooCommerce shipping address forms."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "checkout", "shipping"]
related: ["woo-checkout-billing", "woo-checkout-payment"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12095386"
---

# Woo Checkout Shipping

The Woo Checkout Shipping module renders the shipping address form fields on the WooCommerce checkout page.

!!! abstract "Quick Reference"
    **What it does:** Displays the WooCommerce shipping address form (name, address, city, state, zip, country) on the checkout page.
    **When to use it:** Custom checkout page templates built in the Divi Theme Builder
    **Key settings:** Layout (Default / Fullwidth / 2 Columns), Field styling, Title Text, Field Labels
    **Block identifier:** `divi/wc-checkout-shipping`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12095386)

!!! tip "When to Use This Module"
    - Building a custom WooCommerce checkout page template in the Theme Builder
    - Collecting shipping address details separate from billing information
    - Styling the shipping form fields to match your store's checkout design

!!! warning "When NOT to Use This Module"
    - On non-checkout pages — this module requires the WooCommerce checkout context
    - For billing address collection — use [Woo Checkout Billing](woo-checkout-billing.md)
    - For general address or contact forms — use [Contact Form](contact-form.md)

## Overview

The Woo Checkout Shipping module integrates with WooCommerce to capture a customer's shipping address during checkout. It outputs the standard WooCommerce shipping fields — first name, last name, company, country, street address, city, state/province, and postal code — and can be placed anywhere within a custom checkout page template.

This module is one of several checkout-specific modules designed to replace the default WooCommerce checkout layout with a fully customizable Divi design. It pairs with the [Woo Checkout Billing](woo-checkout-billing.md) and [Woo Checkout Payment](woo-checkout-payment.md) modules to form a complete checkout flow.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12095386).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. It will only render correctly on a checkout page or a Theme Builder template assigned to the checkout endpoint.

<!-- ![Woo Checkout Shipping module](../assets/screenshots/modules/woo-checkout-shipping/element.png){ loading=lazy } -->
<!-- *The Woo Checkout Shipping module displaying shipping address form fields in the Visual Builder.* -->

## Use Cases

1. **Custom Checkout Layout** — Place the shipping address form in a dedicated column alongside the billing form and order summary, giving customers a clear two-column checkout experience.
2. **Branded Checkout Flow** — Style the shipping fields with your brand fonts, colors, and spacing so the entire checkout matches the rest of your store's design.
3. **Streamlined Single-Page Checkout** — Combine the shipping module with billing, payment, and order details modules in a single-page layout for faster conversions.

## How to Add the Woo Checkout Shipping Module

1. Navigate to **Divi > Theme Builder** and create or edit a template assigned to the WooCommerce checkout page.
2. Open the Visual Builder on the checkout template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Checkout Shipping" in the module picker, then click to insert it.

<!-- TODO: Add animated GIF demonstrating module insertion -->

## Settings & Options

The Woo Checkout Shipping module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the module's background, ordering, and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Background | background controls | Set a background color, gradient, image, or video behind the shipping form module. |
| Loop | toggle | Enable the Loop Builder feature for dynamic template contexts. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Woo Checkout Shipping Content tab settings](../assets/screenshots/modules/woo-checkout-shipping/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the visual styling of the shipping form and its fields.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose the field arrangement: Default, Fullwidth, or 2 Columns. The 2 Columns option places fields side-by-side for a more compact form layout. |
| Title Text | text styling | Customize the font, size, color, weight, and letter spacing of the section heading ("Ship to a different address?"). |
| Field Labels | text styling | Style the label text above each form field, including font family, weight, size, and color. |
| Fields | field styling | Customize the appearance of the input fields themselves, including background color, text color, border, and focus states. |

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

<!-- ![Woo Checkout Shipping Design tab settings](../assets/screenshots/modules/woo-checkout-shipping/settings-design.png){ loading=lazy } -->

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

<!-- ![Woo Checkout Shipping Advanced tab settings](../assets/screenshots/modules/woo-checkout-shipping/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the shipping form container */
.et_pb_wc_checkout_shipping {
    background: #fafafa;
    padding: 30px;
    border-radius: 8px;
}

/* Style the section heading */
.et_pb_wc_checkout_shipping h3 {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 20px;
}

/* Style shipping form field labels */
.et_pb_wc_checkout_shipping .woocommerce-shipping-fields label {
    font-weight: 500;
    color: #333;
    margin-bottom: 5px;
}

/* Style shipping input fields */
.et_pb_wc_checkout_shipping .woocommerce-shipping-fields input,
.et_pb_wc_checkout_shipping .woocommerce-shipping-fields select {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px 12px;
    font-size: 15px;
}

/* Highlight focused fields */
.et_pb_wc_checkout_shipping .woocommerce-shipping-fields input:focus,
.et_pb_wc_checkout_shipping .woocommerce-shipping-fields select:focus {
    border-color: #2ea3f2;
    box-shadow: 0 0 0 2px rgba(46, 163, 242, 0.15);
    outline: none;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_checkout_shipping {
        padding: 20px 15px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Checkout Shipping module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_checkout_shipping' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Two-Column Checkout** — Place the Woo Checkout Shipping module in the left column of a two-column row alongside the Woo Checkout Billing module in the right column. Use the 2 Columns layout setting on each module for a compact, professional checkout.

2. **Shipping Below Billing** — Stack the billing and shipping modules vertically in a single column. Customers fill out billing first, then scroll to the shipping section if shipping to a different address.

3. **Branded Field Styling** — Apply your brand font to field labels, set a subtle background color on the form container, and use custom border-radius on input fields to create a cohesive, polished checkout experience.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-checkout-shipping` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Layout | `attrs.layout` | Field arrangement (default, fullwidth, 2-columns) |

!!! tip "Module Selection Guidance"
    For shipping address capture use Woo Checkout Shipping; for billing address use Woo Checkout Billing; for payment method selection use Woo Checkout Payment.

## Saving Your Work

After configuring the shipping form:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. It is only available when building checkout page templates through the Divi Theme Builder.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Checkout Shipping module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The module is placed on a checkout page template (not a regular page)
    - The module is not inside a disabled section or row
    - Visibility settings are not hiding it on the current device

!!! warning "Shipping Fields Not Showing"
    If the shipping form fields are missing or collapsed, check that:

    - WooCommerce shipping is enabled under **WooCommerce > Settings > Shipping**
    - At least one shipping zone and method are configured
    - The "Ship to a different address?" checkbox is visible and enabled in WooCommerce settings

!!! tip "Fields Not Aligning in Two Columns"
    If the 2 Columns layout is not displaying correctly, verify that the row containing the module has sufficient width. On narrow layouts or mobile devices, the fields may stack to a single column automatically for usability.

## Related

- [Woo Checkout Billing](woo-checkout-billing.md) — Captures the billing address form fields on the checkout page
- [Woo Checkout Payment](woo-checkout-payment.md) — Displays payment method options on the checkout page
- [Woo Checkout Details](woo-checkout-details.md) — Shows order review and details during checkout
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
