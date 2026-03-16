---
title: "Woo Product Meta"
description: "Complete Divi 5 Woo Product Meta module reference — settings, design options, code examples, and troubleshooting for displaying WooCommerce product SKU, categories, and tags."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product", "meta", "sku", "categories", "tags"]
related: ["woo-product-information", "woo-product-title"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12034567"
---

# Woo Product Meta

The Woo Product Meta module displays a WooCommerce product's metadata — including SKU, categories, and tags — on custom single product page templates.

!!! abstract "Quick Reference"
    **What it does:** Renders the product SKU, category links, and tag links with configurable layout and visibility toggles.
    **When to use it:** Custom single product page templates built in the Divi Theme Builder
    **Key settings:** Separator, Show SKU, Show Categories, Show Tags, Layout (Inline/Stacked)
    **Block identifier:** `divi/wc-meta`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12034567)

!!! tip "When to Use This Module"
    - Building a custom single product page that needs to display SKU, category, and tag metadata
    - Creating a product page layout where customers can navigate to related products via category or tag links
    - Displaying inventory identifiers (SKU) for products where customers reference part numbers

!!! warning "When NOT to Use This Module"
    - For general product details like weight and dimensions — use [Woo Product Information](woo-product-information.md)
    - For the product title — use [Woo Product Title](woo-product-title.md)
    - For product descriptions — use [Woo Product Description](woo-product-description.md)

## Overview

The Woo Product Meta module provides a structured way to display the organizational and identification metadata associated with a WooCommerce product. This metadata typically includes the product SKU (Stock Keeping Unit), the categories the product belongs to, and any tags assigned to it. Each metadata element is rendered as a labeled line — for example, "SKU: WC-SHIRT-001" or "Categories: Clothing, Summer Collection" — with categories and tags rendered as clickable links that navigate to their respective archive pages.

The module includes individual toggles for each metadata element, so you can display any combination of SKU, categories, and tags depending on what is relevant to your store. A Separator setting controls the visual delimiter between multiple categories or tags on the same line (such as commas, pipes, or other characters).

The Design tab offers a Layout option to arrange the metadata items either inline (side by side on one line) or stacked (each on its own line). This flexibility lets you integrate the module into compact product cards or expanded detail sections equally well.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12034567).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. Products must have metadata (SKU, categories, or tags) assigned for the module to display content.

<!-- ![Woo Product Meta module](../assets/screenshots/modules/woo-product-meta/element.png){ loading=lazy } -->
<!-- *The Woo Product Meta module displaying SKU, categories, and tags in a stacked layout.* -->

## Use Cases

1. **Product Detail Footer** — Place the meta module below the product description and add-to-cart area to provide supplementary identification and classification information, following the conventional e-commerce product page structure.
2. **Category Navigation Aid** — Display category and tag links so customers can browse related products by clicking through to category or tag archive pages, improving product discoverability across your catalog.
3. **B2B Product Identification** — For wholesale or B2B stores, enable only the SKU display to give purchasing managers the part number reference they need for reordering, while hiding categories and tags that are less relevant in a business context.

## How to Add the Woo Product Meta Module

1. Navigate to **Divi > Theme Builder** and create or edit a template assigned to WooCommerce product pages.
2. Open the Visual Builder on the product template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Product Meta" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12034567).

## Settings & Options

The Woo Product Meta module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which product's metadata is displayed, which metadata elements are visible, and how they are separated.

| Setting | Type | Description |
|---------|------|-------------|
| Product | product selector | Choose which published WooCommerce product's metadata to display. In Theme Builder templates, this defaults to the current product dynamically. |
| Separator | select | Choose the character or delimiter used to separate multiple categories or tags on the same line (e.g., comma, pipe, slash). |
| Show SKU | toggle | Display or hide the product's SKU (Stock Keeping Unit) identifier. |
| Show Categories | toggle | Display or hide the product's category assignments as clickable links to category archive pages. |
| Show Tags | toggle | Display or hide the product's tag assignments as clickable links to tag archive pages. |
| Link | url | Optionally make the entire module clickable, directing users to a different page or URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the product meta module container. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Woo Product Meta Content tab settings](../assets/screenshots/modules/woo-product-meta/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the layout arrangement and typography of the metadata display.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose between Inline (metadata items displayed side by side on one line) or Stacked (each metadata item on its own line) arrangement. |

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

<!-- ![Woo Product Meta Design tab settings](../assets/screenshots/modules/woo-product-meta/settings-design.png){ loading=lazy } -->

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

<!-- ![Woo Product Meta Advanced tab settings](../assets/screenshots/modules/woo-product-meta/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the product meta container */
.et_pb_wc_meta {
    padding: 15px 0;
    border-top: 1px solid #eee;
    border-bottom: 1px solid #eee;
    margin: 15px 0;
}

/* Style meta labels (SKU:, Categories:, Tags:) */
.et_pb_wc_meta .product_meta > span {
    display: block;
    font-size: 14px;
    color: #666;
    margin-bottom: 6px;
}

/* Bold the label text */
.et_pb_wc_meta .product_meta > span > span:first-child {
    font-weight: 600;
    color: #333;
}

/* Style category and tag links */
.et_pb_wc_meta .product_meta a {
    color: #2ea3f2;
    text-decoration: none;
    transition: color 0.2s ease;
}

.et_pb_wc_meta .product_meta a:hover {
    color: #1a8cd8;
    text-decoration: underline;
}

/* Style the SKU value */
.et_pb_wc_meta .sku_wrapper .sku {
    font-family: 'Fira Code', monospace;
    background: #f5f5f5;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 13px;
}

/* Inline layout spacing */
.et_pb_wc_meta .product_meta > span + span {
    margin-left: 20px;
}
```

### PHP Hooks

```php
/* Filter the Woo Product Meta module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_meta' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Change the category separator */
add_filter('woocommerce_product_meta_separator', function($separator) {
    return ' | '; // Use pipe instead of comma
});

/* Add custom meta fields to the product meta area */
add_action('woocommerce_product_meta_end', function() {
    global $product;
    $brand = get_post_meta($product->get_id(), '_brand', true);
    if ($brand) {
        echo '<span class="brand_wrapper">Brand: <span>' . esc_html($brand) . '</span></span>';
    }
});
```

## Common Patterns

1. **Standard Product Footer Metadata** — Position the module below the add-to-cart button and above the product reviews using the Stacked layout. Apply a subtle top border and muted text color to visually separate the metadata from the primary product content, following conventional e-commerce page structure.

2. **Compact Inline Meta Strip** — Use the Inline layout with a pipe separator and reduced font size to create a single-line metadata strip. This works well in space-constrained product card layouts or sidebar product detail widgets.

3. **Category-Only Navigation** — Enable only the Show Categories toggle and hide SKU and tags. Style the category links as pill-shaped badges using custom CSS for a tag-cloud visual that invites browsing through related product categories.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-meta` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For product SKU, categories, and tags use Woo Product Meta; for product attributes and specifications use Woo Product Information; for the product title alone use Woo Product Title.

## Saving Your Work

After configuring the product meta module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. Products must have a SKU, categories, or tags assigned in the WooCommerce product editor for the corresponding metadata to display.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Product Meta module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The module is placed on a product page template (not a regular page)
    - A valid, published product is assigned to the module
    - At least one metadata toggle (Show SKU, Show Categories, or Show Tags) is enabled

!!! warning "SKU Not Displaying"
    If the SKU line does not appear even with Show SKU enabled, check that:

    - The product has a SKU value entered in the **Product Data > Inventory** section of the WooCommerce product editor
    - The SKU field is not empty or set to a whitespace-only value

!!! tip "Categories or Tags Showing as Empty"
    If the category or tag line renders its label but shows no values, verify that the product has been assigned to at least one product category or tag in the WooCommerce product editor sidebar panels.

## Related

- [Woo Product Information](woo-product-information.md) — Displays product attributes, weight, and dimensions
- [Woo Product Title](woo-product-title.md) — Displays the product title
- [Woo Product Price](woo-product-price.md) — Displays the product price
- [Woo Add to Cart](woo-add-to-cart.md) — Add-to-cart button and quantity field
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
