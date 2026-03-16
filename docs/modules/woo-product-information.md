---
title: "Woo Product Information"
description: "Complete Divi 5 Woo Product Information module reference — settings, design options, code examples, and troubleshooting for WooCommerce product attributes and specifications."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product", "attributes"]
related: ["woo-product-title", "woo-product-price", "woo-product-stock"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12042030"
---

# Woo Product Information

The Woo Product Information module displays additional product attributes, dimensions, weight, and specification details from WooCommerce in a formatted table.

!!! abstract "Quick Reference"
    **What it does:** Renders product attributes and shipping specifications (weight, dimensions, colors, sizes, materials) pulled from the WooCommerce product data fields in a structured table layout.
    **When to use it:** Product page templates, custom product layouts in the Theme Builder
    **Key settings:** Product selector, Elements (title toggle), Table styling, Attribute Text, Title Text
    **Block identifier:** `divi/wc-product-information`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12042030)

!!! tip "When to Use This Module"
    - Displaying product specifications (dimensions, weight, custom attributes) on product pages
    - Building detailed product layouts that separate attribute data from descriptions
    - Showing shipping-related product details in a custom template

!!! warning "When NOT to Use This Module"
    - On non-WooCommerce pages — this module requires a product context
    - For product descriptions — use [Woo Product Description](woo-product-description.md)
    - For tabbed product info (description + reviews + attributes) — use [Woo Product Tabs](woo-product-tabs.md)

## Overview

The Woo Product Information module integrates with WooCommerce to display additional product details in a structured table format. It pulls data from two sources within the WooCommerce product editor: the **Attributes** section (custom attributes like color, size, material) and the **Shipping** section (weight and dimensions).

The output is rendered as a simple two-column table with attribute names on the left and values on the right. Each row in the table represents a single product attribute or specification. The module also includes an optional title element that can be toggled on or off.

This module is particularly valuable for products that have detailed specifications — such as electronics, furniture, or clothing — where customers need structured data to make purchasing decisions.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12042030).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. Product attributes and shipping data must be configured in the WooCommerce product editor for this module to display content.

<!-- ![Woo Product Information module](../assets/screenshots/modules/woo-product-information/element.png){ loading=lazy } -->
<!-- *The Woo Product Information module displaying product attributes in a table format.* -->

## Use Cases

1. **Product Specifications Table** — Display a structured table of product dimensions, weight, material, and custom attributes below the product description, giving customers easy access to technical details.
2. **Sidebar Attribute Summary** — Place the module in a narrow sidebar column next to the main product content, providing a quick-reference specification panel.
3. **Comparison-Ready Layout** — Use consistent attributes across products so customers can compare specifications between similar items on your store.

## How to Add the Woo Product Information Module

1. Navigate to **Divi > Theme Builder** and create or edit a product page template.
2. Open the Visual Builder on the product template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Product Information" in the module picker, then click to insert it.

<!-- TODO: Add animated GIF demonstrating module insertion -->

## Settings & Options

The Woo Product Information module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which product is referenced and what elements are displayed.

| Setting | Type | Description |
|---------|------|-------------|
| Content (Product) | select | Choose which product supplies the attribute data. On a dynamic product template, this defaults to the current product. |
| Elements | toggle | Display or hide the module's title heading above the attribute table. |
| Link | url | Optionally make the entire module clickable, directing users to a specific page or URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the product information module. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Woo Product Information Content tab settings](../assets/screenshots/modules/woo-product-information/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the visual styling of the attribute table and its text.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Title Text | text styling | Customize the font, size, color, weight, and letter spacing of the module's title heading ("Additional information"). |
| Attribute Text | text styling | Style the attribute name and value text within the table, including font family, weight, size, and color. |
| Table | table styling | Style the table element itself, including background, overall table appearance, and alignment. |
| Table Row | row styling | Customize the appearance of individual table rows, including alternating row colors and spacing. |
| Table Cell | cell styling | Style individual table cells, including padding, borders between cells, and text alignment. |

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

<!-- ![Woo Product Information Design tab settings](../assets/screenshots/modules/woo-product-information/settings-design.png){ loading=lazy } -->

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

<!-- ![Woo Product Information Advanced tab settings](../assets/screenshots/modules/woo-product-information/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the product information container */
.et_pb_wc_additional_info {
    margin-bottom: 30px;
}

/* Style the section heading */
.et_pb_wc_additional_info h2 {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 15px;
    color: #222;
}

/* Style the attributes table */
.et_pb_wc_additional_info table.shop_attributes {
    width: 100%;
    border-collapse: collapse;
}

/* Style table rows with alternating backgrounds */
.et_pb_wc_additional_info table.shop_attributes tr:nth-child(even) {
    background: #f8f8f8;
}

/* Style attribute name cells */
.et_pb_wc_additional_info table.shop_attributes th {
    font-weight: 600;
    color: #333;
    padding: 12px 15px;
    text-align: left;
    width: 35%;
    border-bottom: 1px solid #eee;
}

/* Style attribute value cells */
.et_pb_wc_additional_info table.shop_attributes td {
    padding: 12px 15px;
    color: #555;
    border-bottom: 1px solid #eee;
}

/* Style attribute value links */
.et_pb_wc_additional_info table.shop_attributes td a {
    color: #2ea3f2;
    text-decoration: none;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_additional_info table.shop_attributes th,
    .et_pb_wc_additional_info table.shop_attributes td {
        padding: 10px;
        font-size: 14px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Product Information module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_additional_info' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Reorder product attributes display */
add_filter('woocommerce_display_product_attributes', function($attributes, $product) {
    // Custom sorting or filtering of attributes
    return $attributes;
}, 10, 2);
```

## Common Patterns

1. **Below-Description Specs** — Place the product information module in a full-width row directly beneath the product description. Use alternating row colors and clear cell padding for a clean, scannable specifications table.

2. **Sidebar Specifications** — Position the module in a narrow sidebar column alongside the product images and description. Hide the title element to save vertical space and let the table data speak for itself.

3. **Styled Specification Card** — Apply a subtle background color, border-radius, and box shadow to the module to present product attributes as a self-contained specification card within the product page layout.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-product-information` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Product | `attrs.product` | Product ID reference |
| Show Title | `attrs.show_title` | Toggle for section title visibility |

!!! tip "Module Selection Guidance"
    For structured product attributes and specs use Woo Product Information; for the product description text use Woo Product Description; for tabbed display combining description, attributes, and reviews use Woo Product Tabs.

## Saving Your Work

After configuring the product information module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. Product attributes and shipping specifications must be configured in the WooCommerce product editor for this module to display content.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Product Information module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The module is placed on a product page template or a page with a valid product context
    - The module is not inside a disabled section or row
    - Visibility settings are not hiding it on the current device

!!! warning "No Attributes Showing"
    If the module renders but the table is empty, check that:

    - The product has attributes configured under **Product Data > Attributes** in the WooCommerce product editor
    - The attributes are set to be visible on the product page (check the "Visible on the product page" checkbox)
    - Weight and dimensions are entered under **Product Data > Shipping** if you expect those to appear

!!! tip "Table Styling Looks Off"
    If the attribute table appears unstyled or misaligned, check for CSS conflicts from your theme or other plugins. The module outputs a standard WooCommerce `table.shop_attributes` element, which may inherit global table styles. Use the module's Design tab Table, Table Row, and Table Cell settings to override conflicting styles.

## Related

- [Woo Product Title](woo-product-title.md) — Displays the product title with customizable typography
- [Woo Product Price](woo-product-price.md) — Shows the product price with sale price formatting
- [Woo Product Tabs](woo-product-tabs.md) — Tabbed display of description, additional information, and reviews
- [Woo Product Description](woo-product-description.md) — Displays the full or short product description
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
