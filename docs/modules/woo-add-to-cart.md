---
title: "Woo Add to Cart"
description: "Complete Divi 5 Woo Add to Cart module reference — settings, design options, code examples, and troubleshooting for WooCommerce add-to-cart buttons and quantity fields."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product", "add-to-cart", "button", "quantity"]
related: ["woo-product-price", "woo-product-stock", "shop"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12033379"
---

# Woo Add to Cart

The Woo Add to Cart module displays the WooCommerce add-to-cart button, optional quantity field, and stock status for a selected product on custom single product page templates.

!!! abstract "Quick Reference"
    **What it does:** Renders the add-to-cart button, quantity selector, and optional stock information for a WooCommerce product.
    **When to use it:** Custom single product page templates built in the Divi Theme Builder
    **Key settings:** Product, Show Quantity Field, Show Stock, Button styling, Field Labels
    **Block identifier:** `divi/wc-add-to-cart`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12033379)

!!! tip "When to Use This Module"
    - Building a custom single product page template in the Theme Builder
    - Creating a product landing page with a prominent purchase button
    - Designing variable product layouts where customers select options before adding to cart

!!! warning "When NOT to Use This Module"
    - For general product grids with built-in add-to-cart functionality — use [Shop](shop.md)
    - For displaying only the price without a purchase button — use [Woo Product Price](woo-product-price.md)
    - For stock information without the purchase button — use [Woo Product Stock](woo-product-stock.md)

## Overview

The Woo Add to Cart module is the central purchasing element on any custom WooCommerce product page template. It renders the standard WooCommerce add-to-cart interface, which adapts its output based on the product type. For simple products, it displays a quantity field and an "Add to Cart" button. For variable products, it renders dropdown menus for each product variation (size, color, etc.), a quantity field, and the add-to-cart button. For grouped and external/affiliate products, the output adjusts accordingly to match the product type's purchasing flow.

The module includes optional toggles to show or hide the quantity input field and stock status information. When the quantity field is hidden, customers add one unit at a time. The stock display shows current availability ("In stock," "Only 3 left," or "Out of stock"), which is particularly useful for products with limited inventory where urgency messaging can drive conversions.

For variable products, the Design tab provides dedicated styling controls for field labels and dropdown menus, allowing you to customize the appearance of variation selectors to match your store's design system.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12033379).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. It will only display content when assigned to a valid WooCommerce product.

<!-- ![Woo Add to Cart module](../assets/screenshots/modules/woo-add-to-cart/element.png){ loading=lazy } -->
<!-- *The Woo Add to Cart module showing a quantity field and add-to-cart button for a simple product.* -->

## Use Cases

1. **Standard Product Page** — Place the module below the product price and above the product meta to create a conventional e-commerce purchasing flow, with the quantity field and add-to-cart button as the primary call to action.
2. **Variable Product Configurator** — For products with multiple variations, the module renders dropdown selectors for each attribute. Style these dropdowns and field labels to create a polished product configurator that guides customers through option selection.
3. **Minimal Quick-Buy Layout** — Hide the quantity field and stock display for a streamlined single-click purchase button, ideal for digital products or services where quantity selection is unnecessary.

## How to Add the Woo Add to Cart Module

1. Navigate to **Divi > Theme Builder** and create or edit a template assigned to WooCommerce product pages.
2. Open the Visual Builder on the product template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Add to Cart" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12033379).

## Settings & Options

The Woo Add to Cart module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which product the module is assigned to, which elements are visible, and the module's background and layout ordering.

| Setting | Type | Description |
|---------|------|-------------|
| Product | product selector | Choose which published WooCommerce product the add-to-cart button is assigned to. In Theme Builder templates, this defaults to the current product dynamically. |
| Show Quantity Field | toggle | Display or hide the quantity input field next to the add-to-cart button. When hidden, clicking the button adds a single unit. |
| Show Stock | toggle | Display or hide the product's stock status text (e.g., "In stock," "Only 3 left in stock," "Out of stock") below the add-to-cart area. |
| Link | url | Optionally make the entire module clickable, directing users to a different page or URL instead of the default add-to-cart behavior. |
| Background | background controls | Set a background color, gradient, image, or video behind the add-to-cart module container. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Woo Add to Cart Content tab settings](../assets/screenshots/modules/woo-add-to-cart/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the visual appearance of the add-to-cart button, quantity field, variation dropdowns, and all text elements.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Field Labels | text styling | Style the labels displayed above variation dropdowns on variable products, including label position, font family, weight, color, and size. |
| Fields | field styling | Customize the appearance of the quantity input field, including background color, font, text color, and size. |
| Dropdown Menus | field styling | Style the variation selector dropdowns on variable products, including background, border, font, and text appearance. |
| Button | button styling | Control the add-to-cart button appearance, including background color, text color, font, border, padding, border-radius, and hover state effects. |

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

<!-- ![Woo Add to Cart Design tab settings](../assets/screenshots/modules/woo-add-to-cart/settings-design.png){ loading=lazy } -->

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

<!-- ![Woo Add to Cart Advanced tab settings](../assets/screenshots/modules/woo-add-to-cart/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the add-to-cart button */
.et_pb_wc_add_to_cart .single_add_to_cart_button {
    background: #2ea3f2;
    color: #fff;
    font-size: 16px;
    font-weight: 600;
    padding: 14px 30px;
    border-radius: 6px;
    border: none;
    transition: background 0.3s ease, transform 0.2s ease;
}

.et_pb_wc_add_to_cart .single_add_to_cart_button:hover {
    background: #1a8cd8;
    transform: translateY(-1px);
}

/* Style the quantity input field */
.et_pb_wc_add_to_cart .quantity input.qty {
    width: 60px;
    height: 48px;
    text-align: center;
    border: 2px solid #ddd;
    border-radius: 6px;
    font-size: 16px;
}

/* Style variation dropdown selectors */
.et_pb_wc_add_to_cart .variations select {
    padding: 10px 15px;
    border: 2px solid #ddd;
    border-radius: 6px;
    font-size: 14px;
    background: #fff;
}

/* Style the stock status text */
.et_pb_wc_add_to_cart .stock {
    font-size: 14px;
    font-weight: 500;
    margin-top: 10px;
}

.et_pb_wc_add_to_cart .stock.in-stock {
    color: #4caf50;
}

.et_pb_wc_add_to_cart .stock.out-of-stock {
    color: #e53935;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_add_to_cart .single_add_to_cart_button {
        width: 100%;
        text-align: center;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Add to Cart module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_add_to_cart' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Change the add-to-cart button text */
add_filter('woocommerce_product_single_add_to_cart_text', function($text) {
    return 'Buy Now';
});

/* Redirect to checkout after adding to cart */
add_filter('woocommerce_add_to_cart_redirect', function($url) {
    return wc_get_checkout_url();
});

/* Set a minimum quantity for add-to-cart */
add_filter('woocommerce_quantity_input_args', function($args, $product) {
    $args['min_value'] = 1;
    $args['max_value'] = 10;
    $args['step'] = 1;
    return $args;
}, 10, 2);
```

## Common Patterns

1. **Standard Product Purchase Block** — Position the add-to-cart module below the price module and above the product meta module, with the quantity field visible and stock status enabled. This creates the conventional e-commerce layout customers expect on product pages.

2. **Full-Width CTA Button** — Hide the quantity field and use custom CSS to make the button span the full width of its container. This creates a bold, prominent call-to-action suitable for single-purchase products like digital downloads or services.

3. **Variation-Heavy Product Layout** — For products with multiple variation attributes, give the module extra vertical space and style the dropdown menus with clear labels and adequate padding. Apply distinct styling to the field labels so customers can easily distinguish between selection options.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-add-to-cart` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For the add-to-cart button on product pages use Woo Add to Cart; for just the price display use Woo Product Price; for stock information alone use Woo Product Stock; for product grids with built-in purchase buttons use Shop.

## Saving Your Work

After configuring the add-to-cart module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. The module's output adapts based on the product type — simple, variable, grouped, or external/affiliate products each render a different add-to-cart interface.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Add to Cart module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The module is placed on a product page template (not a regular page)
    - A valid, published product is assigned to the module
    - The product is not set to a catalog-only visibility that hides the purchase button

!!! warning "Add to Cart Button Disabled or Missing"
    If the button appears grayed out or does not render, check that:

    - The product is published and not in draft or pending status
    - The product is set to "In stock" or has stock management configured correctly
    - For variable products, all variation attributes have at least one valid option defined

!!! tip "Variation Dropdowns Not Appearing"
    For variable products, the dropdown selectors only appear when the product has properly configured attributes set to "Used for variations." Verify in the WooCommerce product editor that attributes are created, assigned to variations, and that at least one variation is published.

## Related

- [Woo Product Price](woo-product-price.md) — Displays the product price on single product pages
- [Woo Product Stock](woo-product-stock.md) — Shows product stock availability status
- [Shop](shop.md) — General product grid display module with built-in add-to-cart buttons
- [Woo Product Images](woo-product-images.md) — Displays the product featured image and gallery
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
