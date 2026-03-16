---
title: "Woo Checkout Information"
description: "Divi 5 Woo Checkout Information module — WooCommerce order notes textarea for customers to add special instructions and delivery notes at checkout."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "checkout", "forms", "order-notes"]
related: ["woo-checkout-billing", "woo-checkout-details"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12095378"
---

# Woo Checkout Information

The Woo Checkout Information module provides a text field for customers to add order notes and special instructions during WooCommerce checkout.

!!! abstract "Quick Reference"
    **What it does:** Renders the WooCommerce "Additional Information" section with an order notes textarea on the checkout page.
    **When to use it:** Custom checkout page templates in the Theme Builder
    **Key settings:** Elements (Show/Hide Title), Title Text styling, Field Labels styling, Fields styling
    **Block identifier:** `divi/woo-checkout-information`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12095378)

!!! tip "When to Use This Module"
    - Building a custom WooCommerce checkout page that accepts order notes
    - Allowing customers to provide delivery instructions or special requests
    - Completing a checkout layout alongside billing, shipping, and payment modules

!!! warning "When NOT to Use This Module"
    - On non-checkout pages — this module requires the WooCommerce checkout context
    - For general contact or feedback forms — use [Contact Form](contact-form.md)
    - For product-level notes — use WooCommerce product custom fields instead

## Overview

The Woo Checkout Information module renders the "Additional Information" section of the WooCommerce checkout page. By default, this section contains a single textarea field labeled "Order Notes" where customers can type special instructions, delivery preferences, gift messages, or any other communication they want to include with their order. The notes are saved to the order and visible to the store administrator in the WooCommerce order details.

The module includes an Elements toggle that lets you show or hide the section title ("Additional Information"). This is useful when you want to integrate the notes field seamlessly into a custom layout without a heading, or when you prefer to add your own heading above the module using a Text or Heading module for more design control.

While the default WooCommerce configuration includes only the order notes field, developers can add additional fields to this section using WooCommerce's `woocommerce_checkout_fields` filter. Any fields added to the "order" field group will appear within this module. For the official Elegant Themes documentation, see the [Woo Checkout Information help article](https://help.elegantthemes.com/en/articles/12095378).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active. It will not appear in the module picker without WooCommerce.

## Use Cases

1. **Delivery Instructions** — Allow customers to specify delivery details like gate codes, preferred delivery times, or instructions for leaving packages. This is especially valuable for food delivery, florist, or any business where delivery specifics directly affect service quality.

2. **Gift Message Capture** — For gift-oriented stores, the order notes field serves as a natural place for customers to include personalized messages. Style the field with a larger height and inviting placeholder text like "Add a gift message (optional)" to encourage use.

3. **Streamlined Checkout Placement** — Place this module between the shipping and payment modules in your checkout flow. Hide the title for a cleaner look and add a custom heading module above with text like "Anything we should know?" to create a more conversational checkout tone.

## How to Add the Woo Checkout Information Module

1. Ensure WooCommerce is installed and activated. Navigate to the Theme Builder and create or edit the template assigned to the WooCommerce checkout page.
2. Open the Visual Builder on your checkout page template. Click the gray **+** icon to add a new module to a row.
3. Search for "Woo Checkout Information" in the module picker or find it in the WooCommerce category, then click to insert it. The module will display the order notes field automatically.

## Settings & Options

The Woo Checkout Information module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the visibility of the section title and the module's background.

| Setting | Type | Description |
|---------|------|-------------|
| Elements — Show Title | toggle | Display or hide the "Additional Information" heading above the order notes field. Disable this to create a cleaner layout when using a separate heading module. |
| Background | background controls | Set a background color, gradient, image, or video behind the module. |
| Loop | toggle | Enable the loop builder to use this module within a loop context. |
| Order | select | Set the Flexbox order of the module within its parent row. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |

### Design Tab

The Design tab provides controls for styling the section title, field labels, and the textarea input.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Title Text | text styling | Customize the font, size, weight, and color of the "Additional Information" heading. |
| Field Labels | text styling | Style the "Order Notes" label text including font, size, weight, and color. |
| Fields | styling controls | Style the textarea input including border, background color, text color, padding, border radius, and focus states. Controls the visual appearance of the notes input area. |

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
| [CSS](../options-groups/css.md) | Custom CSS per element target (heading, label, textarea) |
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
/* Style the order notes textarea */
.et_pb_wc_checkout_additional_info textarea {
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    padding: 14px 16px;
    font-size: 15px;
    min-height: 120px;
    resize: vertical;
    transition: border-color 0.3s ease;
}

.et_pb_wc_checkout_additional_info textarea:focus {
    border-color: #2ea3f2;
    box-shadow: 0 0 0 3px rgba(46, 163, 242, 0.15);
    outline: none;
}

/* Style the section heading */
.et_pb_wc_checkout_additional_info h3 {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 12px;
}

/* Style the field label */
.et_pb_wc_checkout_additional_info label {
    font-weight: 500;
    font-size: 14px;
    margin-bottom: 6px;
    display: block;
    color: #555;
}

/* Add a placeholder icon indicator */
.et_pb_wc_checkout_additional_info textarea::placeholder {
    color: #aaa;
    font-style: italic;
}

/* Responsive: larger touch target on mobile */
@media (max-width: 767px) {
    .et_pb_wc_checkout_additional_info textarea {
        min-height: 100px;
        font-size: 16px; /* Prevents iOS zoom */
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Checkout Information module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_checkout_additional_info' !== $render_slug) {
        return $output;
    }
    return $output;
}, 10, 2);

/* Customize the order notes field placeholder and label */
add_filter('woocommerce_checkout_fields', function($fields) {
    $fields['order']['order_comments']['placeholder'] = 'Special delivery instructions, gift messages, etc.';
    $fields['order']['order_comments']['label'] = 'Special Instructions';
    return $fields;
});

/* Add a character counter to the order notes field */
add_action('woocommerce_after_order_notes', function() {
    echo '<p class="order-notes-counter"><span id="notes-count">0</span>/500 characters</p>';
    echo '<script>
        document.getElementById("order_comments").addEventListener("input", function() {
            document.getElementById("notes-count").textContent = this.value.length;
            if (this.value.length > 500) this.value = this.value.substring(0, 500);
        });
    </script>';
});

/* Remove the order notes field entirely if not needed */
add_filter('woocommerce_checkout_fields', function($fields) {
    unset($fields['order']['order_comments']);
    return $fields;
});
```

## Common Patterns

1. **Optional Notes Below Shipping** — Place the Woo Checkout Information module between the shipping form and the payment module. Hide the title and use a Text module above it with text like "Any special instructions?" in a softer color. This positions the notes as a secondary, optional step that does not interrupt the checkout flow.

2. **Gift Message Field** — Change the field label and placeholder via PHP hooks to "Gift Message" with placeholder text like "Write your message here (we'll include it with the gift)." Style the textarea with a slightly larger minimum height and a warmer border color to create an inviting writing space that feels separate from the transactional parts of checkout.

3. **Full-Width Notes in Single-Column Checkout** — In a single-column checkout layout, place this module at full width with generous top and bottom margin via the Spacing options. The wide textarea gives customers ample room to type longer notes. Style the border to match the billing and shipping field styling for visual consistency.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API** produces content that
    renders on the front end but may not appear in the Visual Builder layer view.
    Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/woo-checkout-information` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

## Saving Your Work

After configuring the Woo Checkout Information module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple checkout templates, or added to your Divi Library for reuse by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Woo Checkout Information module in Divi 5 supports Conditions, Interactions, Scroll Effects, and enhanced layout controls not available in Divi 4.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active.

## Troubleshooting

!!! warning "Order Notes Field Not Appearing"
    If the module renders but shows no textarea, a plugin or custom code may be removing the order notes field via the `woocommerce_checkout_fields` filter. Check your theme's functions.php and active plugins for code that unsets `$fields['order']['order_comments']`. Also verify the template is assigned to the WooCommerce checkout page.

!!! warning "Notes Not Saved to Order"
    If customers report that their notes are not appearing in the order, verify that the field name is `order_comments` (the WooCommerce default). Custom implementations that change the field name may not save correctly. Check WooCommerce > Orders and click into a specific order to view the "Customer provided note" section.

!!! tip "Hiding This Module When Not Needed"
    If your store does not need order notes, you can either remove this module from the checkout template entirely or use the PHP hook to unset the order comments field. Removing unnecessary form fields simplifies the checkout process and can improve conversion rates.

## Related

- [Woo Checkout Billing](woo-checkout-billing.md)
- [Woo Checkout Details](woo-checkout-details.md)
