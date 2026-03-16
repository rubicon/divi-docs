---
title: "Shop"
description: "Divi 5 Shop module — WooCommerce product grid with category filtering, sort options, sale badges, ratings, and add-to-cart buttons."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "products", "store", "product-grid", "shopping"]
related: ["portfolio", "blog", "gallery"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://www.elegantthemes.com/documentation/divi/ecommerce-divi/"
---

# Shop

The Shop module displays WooCommerce products in a customizable grid layout with images, titles, prices, and add-to-cart functionality.

!!! abstract "Quick Reference"
    **What it does:** Displays WooCommerce products in a styled grid with images, titles, prices, ratings, and add-to-cart buttons.
    **When to use it:** Homepage featured products, category landing pages, sale/clearance sections
    **Key settings:** Type (Recent/Featured/Sale/Best Selling), Posts Number, Include Categories, Columns, Orderby, Show elements
    **Block identifier:** `divi/shop`
    **ET Docs:** [Official documentation](https://www.elegantthemes.com/documentation/divi/ecommerce-divi/)

!!! tip "When to Use This Module"
    - Showcasing featured, sale, or best-selling WooCommerce products on any page
    - Building category-specific landing pages with filtered product grids
    - Adding a curated product section to non-shop pages like the homepage or blog

!!! warning "When NOT to Use This Module"
    - For displaying products on a product page template → use individual Woo Product modules
    - For non-WooCommerce content grids → use [Blog](blog.md) or [Portfolio](portfolio.md)
    - For a fullwidth product display → combine with a fullwidth section layout

## Overview

The Shop module bridges Divi's Visual Builder with WooCommerce, allowing you to showcase products anywhere on your site without relying on default WooCommerce templates. It pulls product data directly from your WooCommerce catalog and renders it in a styled grid that matches your Divi design system. Each product card displays the featured image, product title, price, star rating, and an add-to-cart button.

The module provides fine-grained control over which products appear and how they are sorted. You can display recent products, featured products, sale items, or best sellers. Category and tag filters let you curate product selections for specific pages, such as showing only accessories on an accessories landing page or highlighting seasonal items on the homepage. The column count adjusts from one to six, and the grid responds to screen size automatically.

Because the Shop module requires WooCommerce to be installed and activated, it will not appear in the module picker if the plugin is absent. Once WooCommerce is running and at least one product is published, the module becomes available in any standard section row. It works well alongside the [Portfolio](portfolio.md) module for service-based businesses that also sell products, the [Blog](blog.md) module for content-driven commerce pages, and the [Gallery](gallery.md) module for visual product showcases.

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/shop/)

![Shop module](../assets/screenshots/modules/shop/element.png){ loading=lazy }
*The Shop module displaying WooCommerce products in a grid layout with images, titles, and prices.*

## Use Cases

1. **Homepage Featured Products** — Display a curated selection of featured or best-selling products on the homepage to drive immediate purchasing interest. Set the product type to "Featured" and limit the count to four or six for a clean, balanced grid.

2. **Category Landing Page** — Build dedicated landing pages for product categories using the Include Categories filter. Pair the Shop module with a heading, descriptive text, and a banner image to create a fully branded category experience within Divi.

3. **Sale or Clearance Section** — Filter the module to show only products on sale. Place it in a colored section with a "Sale" heading above to create an attention-grabbing clearance area that updates automatically as you mark products on sale in WooCommerce.

## How to Add the Shop Module

1. Ensure WooCommerce is installed, activated, and that at least one product is published in your WordPress dashboard under Products.
2. Open the Visual Builder on the page you want to edit. Click the gray **+** icon to add a new module to a row.
3. Search for "Shop" in the module picker or find it in the WooCommerce category, then click to insert it.

## Settings & Options

The Shop module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which products display, how they are sourced and sorted, and what elements are visible on each product card.

| Setting | Type | Description |
|---------|------|-------------|
| Type | select | Choose the product query type: Recent Products, Featured Products, Sale Products, Best Selling Products, or Top Rated Products. This determines the base set of products the module pulls from. |
| Posts Number | number input | Set the maximum number of products to display. Controls how many product cards appear in the grid. |
| Include Categories | multi-select | Filter products by one or more WooCommerce product categories. Leave empty to show all categories. |
| Columns | select | Set the number of columns in the product grid (1 through 6). Affects how many products appear per row on desktop. |
| Orderby | select | Control the sort order of products: Date, Title, Price, Popularity, Rating, or Random. Works in combination with the Type filter. |
| Order | select | Choose ascending or descending sort direction for the selected Orderby field. |
| Elements — Show Title | toggle | Display or hide the product title on each card. |
| Elements — Show Price | toggle | Display or hide the product price, including sale pricing when applicable. |
| Elements — Show Rating | toggle | Display or hide the star rating on each product card. Ratings come from WooCommerce product reviews. |
| Elements — Show Add to Cart | toggle | Display or hide the add-to-cart button on each product card. |
| Elements — Show Sale Badge | toggle | Display or hide the "Sale" badge overlay on products that are currently on sale. |
| Elements — Show Pagination | toggle | Enable or disable pagination controls below the product grid when the total product count exceeds the Posts Number setting. |
| Link | url | Optionally make the entire module clickable, directing visitors to a specified URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the module. |
| Module Order | select | Control the module's placement order within Flexbox and Grid parent layouts. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |

### Design Tab

The Design tab provides controls for the visual presentation of the product grid, including layout, typography, image styling, and effects.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose between grid layout options. Flexbox and CSS Grid configurations are available for advanced column/row control. |
| Star Rating | color/size controls | Customize the color and size of the star rating icons displayed on product cards. |
| Sale Badge | styling controls | Customize the appearance of the sale badge including background color, text color, font, and positioning. |
| Price Text | text styling | Customize the price display including font, size, regular price color, sale price color, and strikethrough styling for original prices. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Title Text](../options-groups/title-text.md) | Font, size, color, letter spacing, text shadow for product titles |
| [Meta Text](../options-groups/meta-text.md) | Font, size, color, spacing for category labels or descriptions |
| [Button](../options-groups/button.md) | Font, text color, background color, border, border radius, padding, hover effects for add-to-cart button |
| [Image](../options-groups/image.md) | Border radius, object fit, hover effects, overlay behavior for product images |
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
| [CSS](../options-groups/css.md) | Custom CSS per element target (product card, image, title, price, button, sale badge) |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

## Code Examples

### Custom CSS

```css
/* Style product cards with a clean card design */
.et_pb_shop .woocommerce ul.products li.product {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    padding-bottom: 20px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.et_pb_shop .woocommerce ul.products li.product:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

/* Style the product title */
.et_pb_shop .woocommerce ul.products li.product h3 {
    font-size: 16px;
    font-weight: 600;
    padding: 0 15px;
}

/* Style the price display */
.et_pb_shop .woocommerce ul.products li.product .price {
    color: #2ea3f2;
    font-weight: 700;
    font-size: 18px;
    padding: 0 15px;
}

/* Sale badge customization */
.et_pb_shop .woocommerce span.onsale {
    background-color: #e74c3c;
    color: #fff;
    border-radius: 4px;
    padding: 4px 10px;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
}

/* Style the add-to-cart button */
.et_pb_shop .woocommerce ul.products li.product .button {
    background-color: #2ea3f2;
    color: #fff;
    border-radius: 4px;
    padding: 10px 20px;
    margin: 10px 15px 0;
    width: calc(100% - 30px);
    text-align: center;
}

/* Responsive: two columns on tablet, one on mobile */
@media (max-width: 980px) {
    .et_pb_shop .woocommerce ul.products li.product {
        width: 48% !important;
    }
}

@media (max-width: 767px) {
    .et_pb_shop .woocommerce ul.products li.product {
        width: 100% !important;
    }
}
```

### PHP Hooks

```php
/* Filter the Shop module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_shop' !== $render_slug) {
        return $output;
    }
    // Example: Add a "View All Products" link after the grid
    $shop_url = get_permalink(wc_get_page_id('shop'));
    $output .= '<div class="shop-view-all"><a href="' . esc_url($shop_url) . '">View All Products &rarr;</a></div>';
    return $output;
}, 10, 2);

/* Exclude out-of-stock products from the Shop module query */
add_filter('woocommerce_product_query_meta_query', function($meta_query) {
    $meta_query[] = array(
        'key'     => '_stock_status',
        'value'   => 'outofstock',
        'compare' => '!=',
    );
    return $meta_query;
});
```

## Common Patterns

1. **Featured Products Showcase** — Set the Type to "Featured Products" with a Posts Number of 4 and 4 columns to create a balanced grid. Apply card-style box shadows and hover lift effects through the Design tab. Place this on the homepage below a hero section to immediately surface your best products.

2. **Sale Products Banner** — Filter by "Sale Products" and place the module inside a section with a bold background color. Add a heading row above with text like "Limited Time Offers" and apply the sale badge styling to make discounted prices prominent. This creates an urgency-driven section that updates automatically.

3. **Single-Category Product Page** — Use the Include Categories filter to show products from one category. Set a higher Posts Number (12-16) with 3 or 4 columns and enable pagination. Combine with a sidebar column containing category navigation or filters to create a complete shop experience within the Divi builder.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/shop` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Type | `attrs.type` | Product query type (recent, featured, sale, etc.) |
| Posts Number | `attrs.posts_number` | Maximum products to display |
| Columns | `attrs.columns_number` | Number of grid columns |
| Orderby | `attrs.orderby` | Sort order field |

!!! tip "Module Selection Guidance"
    For WooCommerce product grids use Shop; for general post grids use Blog or Portfolio.

## Saving Your Work

After configuring the Shop module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple Shop instances, or added to your Divi Library for reuse on other pages by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Shop module in Divi 5 benefits from the updated rendering engine and supports Conditions, Interactions, Scroll Effects, and enhanced layout controls not available in Divi 4. WooCommerce compatibility in Divi 5 requires WooCommerce 7.0 or later.

## Troubleshooting

!!! warning "Module Not Appearing in Module Picker"
    The Shop module requires WooCommerce to be installed and activated. If you do not see it in the module picker, go to Plugins in your WordPress dashboard and verify WooCommerce is active. After activating WooCommerce, refresh the Visual Builder.

!!! warning "No Products Displaying"
    If the module appears but shows no products, verify that you have at least one published product in WooCommerce (Products > All Products). Check that the product has a status of "Published" (not Draft). Also verify the Include Categories filter is not set to an empty category, and that the Type filter matches your product data (e.g., "Featured Products" requires products to be marked as featured in WooCommerce).

!!! tip "Add to Cart Button Not Working"
    If clicking the add-to-cart button does not add the product to the cart, check for JavaScript conflicts with other plugins. Open the browser developer console and look for errors. Also verify that WooCommerce AJAX add-to-cart is enabled under WooCommerce > Settings > Products. For variable products, the button may redirect to the product page instead of adding directly to the cart, which is expected behavior.

## Related

- [Portfolio](portfolio.md)
- [Blog](blog.md)
- [Gallery](gallery.md)
