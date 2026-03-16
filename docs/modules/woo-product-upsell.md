---
title: "Woo Product Upsell"
description: "Complete Divi 5 Woo Product Upsell module reference — settings, design options, code examples, and troubleshooting for displaying WooCommerce upsell product recommendations."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product", "upsell", "recommendations", "sales"]
related: ["woo-related-products", "woo-cross-sells", "shop"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12041624"
---

# Woo Product Upsell

The Woo Product Upsell module displays upsell product recommendations linked to the current product, encouraging customers to consider higher-value alternatives or premium versions on single product pages.

!!! abstract "Quick Reference"
    **What it does:** Renders a grid of upsell products linked to the current product, with configurable columns, ordering, and element visibility.
    **When to use it:** Custom single product page templates built in the Divi Theme Builder
    **Key settings:** Product Count, Column Layout, Order, Show Name/Image/Price/Rating/Sale Badge
    **Block identifier:** `divi/wc-upsells`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12041624)

!!! tip "When to Use This Module"
    - Building a custom single product page that promotes higher-value alternatives to the viewed product
    - Creating a merchandising strategy that drives customers toward premium product options
    - Designing product pages with a dedicated recommendations section below the main product details

!!! warning "When NOT to Use This Module"
    - For related products based on category/tag similarity — use [Woo Related Products](woo-related-products.md)
    - For cross-sell suggestions on the cart page — use [Woo Cross Sells](woo-cross-sells.md)
    - For general product grids — use [Shop](shop.md)

## Overview

The Woo Product Upsell module displays products that have been configured as upsells for the currently viewed product. Upselling is a sales technique where you recommend a higher-end or more feature-rich version of the product the customer is already considering — for example, suggesting a premium laptop when the customer is viewing a standard model, or offering a larger size of a consumable product at a better per-unit price.

The products shown by this module are configured in each product's **Linked Products** section within the WooCommerce product editor under the "Upsells" field. The module then renders these linked products in a grid format with configurable columns, ordering, and element visibility. You can control how many upsell products appear, how many columns the grid uses, and which product elements (name, image, price, rating, sale badge) are displayed for each card.

Additional controls include a product offset to skip a specified number of products from the beginning of the list, and an order setting to sort the upsell products by various criteria. Overlay styling options let you customize hover effects on product images, while dedicated text styling groups allow you to fine-tune the appearance of product titles, prices, sale prices, and star ratings.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12041624).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. Products must have upsell products configured in the Linked Products section for this module to display content.

<!-- ![Woo Product Upsell module](../assets/screenshots/modules/woo-product-upsell/element.png){ loading=lazy } -->
<!-- *The Woo Product Upsell module displaying recommended premium product alternatives in a three-column grid.* -->

## Use Cases

1. **Premium Upgrade Section** — Place the upsell module below the product description to present higher-tier versions of the product. For example, on a basic plan product page, show the professional and enterprise plan options as upsells to guide customers toward higher-value purchases.
2. **Below-the-Fold Recommendations** — Position the module in a dedicated section below all primary product details, styled with a contrasting background, to create a distinct "You Might Also Like" area that catches the customer's eye as they scroll.
3. **Compact Sidebar Suggestions** — In a two-column product layout, place the upsell module in a narrower sidebar column with a single-column layout and reduced product count to provide subtle upgrade suggestions alongside the main product content.

## How to Add the Woo Product Upsell Module

1. Navigate to **Divi > Theme Builder** and create or edit a template assigned to WooCommerce product pages.
2. Open the Visual Builder on the product template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Product Upsell" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12041624).

## Settings & Options

The Woo Product Upsell module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which product's upsells are displayed, how many are shown, the grid layout, and which product card elements are visible.

| Setting | Type | Description |
|---------|------|-------------|
| Product | product selector | Choose which published WooCommerce product's linked upsell products to display. In Theme Builder templates, this defaults to the current product dynamically. |
| Product Count | number | Set the maximum number of upsell products to display in the grid. |
| Column Layout | select | Choose the number of columns in which the upsell products are arranged (e.g., 2, 3, or 4 columns). |
| Order | select | Choose the sort order for the displayed upsell products (e.g., by date, title, price, or popularity). |
| Product Offset Number | number | Skip a specified number of products from the beginning of the upsell list. Useful for pagination-like behavior or excluding the first few results. |
| Show Name | toggle | Display or hide the product title on each upsell product card. |
| Show Image | toggle | Display or hide the product featured image on each upsell product card. |
| Show Price | toggle | Display or hide the product price on each upsell product card. |
| Show Rating | toggle | Display or hide the product star rating on each upsell product card. |
| Show Sale Badge | toggle | Display or hide the sale badge overlay on discounted upsell products. |
| Link | url | Optionally make the entire module clickable, directing users to a specific page or URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the upsell module container. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Woo Product Upsell Content tab settings](../assets/screenshots/modules/woo-product-upsell/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the visual styling of the product cards, text elements, overlays, and ratings.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Overlay | overlay styling | Configure the image overlay design, including background color, icon, and opacity on hover. |
| Image | image styling | Apply design effects to product images, including border, shadow, and spacing. |
| Star Rating | rating styling | Customize the appearance of the star rating display, including star color and size. |
| Sale Badge | badge styling | Style the sale badge overlay, including background color, text color, and position. |
| Title Text | text styling | Customize the module section title text (e.g., "You may also like..."), including font, size, weight, and color. |
| Product Title Text | text styling | Style the individual product name text on each upsell card, including font, size, weight, and color. |
| Price Text | text styling | Customize the regular price text display, including font, color, and size. |
| Sale Price Text | text styling | Style the discounted price text separately from the regular price, allowing visual emphasis on the sale amount. |

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

<!-- ![Woo Product Upsell Design tab settings](../assets/screenshots/modules/woo-product-upsell/settings-design.png){ loading=lazy } -->

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

<!-- ![Woo Product Upsell Advanced tab settings](../assets/screenshots/modules/woo-product-upsell/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the upsells container */
.et_pb_wc_upsells {
    background: #f8f9fa;
    padding: 40px 30px;
    border-radius: 8px;
}

/* Style the section heading */
.et_pb_wc_upsells h2 {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 25px;
    color: #333;
}

/* Style individual product cards */
.et_pb_wc_upsells .products li.product {
    background: #fff;
    border-radius: 8px;
    padding: 15px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    transition: box-shadow 0.3s ease, transform 0.2s ease;
}

.et_pb_wc_upsells .products li.product:hover {
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
    transform: translateY(-2px);
}

/* Style product images */
.et_pb_wc_upsells .products li.product img {
    border-radius: 6px;
    margin-bottom: 12px;
}

/* Style product titles */
.et_pb_wc_upsells .products li.product .woocommerce-loop-product__title {
    font-size: 15px;
    font-weight: 500;
    color: #333;
}

/* Style sale badge */
.et_pb_wc_upsells .products li.product .onsale {
    background: #e53935;
    color: #fff;
    border-radius: 50%;
    width: 48px;
    height: 48px;
    line-height: 48px;
    text-align: center;
    font-size: 12px;
    font-weight: 700;
}

/* Style sale price with strikethrough */
.et_pb_wc_upsells .products li.product .price del {
    color: #999;
    font-size: 13px;
}

.et_pb_wc_upsells .products li.product .price ins {
    color: #e53935;
    font-weight: 600;
    text-decoration: none;
}

/* Responsive: 2 columns on tablet */
@media (max-width: 980px) {
    .et_pb_wc_upsells .products {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Responsive: 1 column on mobile */
@media (max-width: 480px) {
    .et_pb_wc_upsells .products {
        grid-template-columns: 1fr;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Product Upsell module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_upsells' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Change the number of upsell products displayed */
add_filter('woocommerce_upsells_total', function($total) {
    return 3; // Show maximum of 3 upsell products
});

/* Change the number of upsell columns */
add_filter('woocommerce_upsells_columns', function($columns) {
    return 3; // Display in 3 columns
});

/* Customize the upsells order */
add_filter('woocommerce_upsells_orderby', function($orderby) {
    return 'rand'; // Randomize upsell order
});
```

## Common Patterns

1. **Below-Product Recommendations** — Place the upsell module in a full-width row below the product details section with a light background and clear heading. Set the column layout to 3 or 4 and enable all product card elements to create a comprehensive "You May Also Like" section.

2. **Minimal Image Grid** — Show only product images and names (disable price, rating, and sale badge) for a clean, gallery-like upsell presentation that invites exploration without overwhelming with information.

3. **Sale-Focused Upsells** — Enable the sale badge and style the sale price text with a contrasting color to draw attention to discounted premium alternatives. This is effective when upsell products are temporarily on sale, creating additional urgency for the upgrade.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-upsells` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For upsell products on single product pages use Woo Product Upsell; for related products based on category/tag similarity use Woo Related Products; for cross-sells on the cart page use Woo Cross Sells; for general product grids use Shop.

## Saving Your Work

After configuring the product upsell module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. Products must have upsell products configured in the **Linked Products** section of the WooCommerce product editor for this module to display content.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Product Upsell module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The module is placed on a product page template (not a regular page or cart template)
    - A valid, published product is assigned to the module
    - Visibility settings are not hiding it on the current device

!!! warning "No Upsell Products Showing"
    If the module renders but displays no products, check that:

    - The current product has upsell products configured under **Product Data > Linked Products > Upsells**
    - The linked upsell products are published (not draft or trashed)
    - The linked upsell products are not hidden from the catalog
    - The Product Count setting is greater than 0

!!! tip "Product Offset Hiding All Results"
    If the Product Offset Number is set higher than the number of available upsell products, no products will display. Reduce the offset value or add more upsell products to the parent product's linked products configuration.

## Related

- [Woo Related Products](woo-related-products.md) — Displays related products based on shared categories and tags
- [Woo Cross Sells](woo-cross-sells.md) — Shows cross-sell product suggestions on the cart page
- [Shop](shop.md) — General product grid display module
- [Woo Product Price](woo-product-price.md) — Displays the product price on single product pages
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
