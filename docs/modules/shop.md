---
title: "Shop"
category: modules
tags: ["modules", "woocommerce", "ecommerce", "products", "store", "product-grid", "shopping"]
related: ["portfolio", "blog", "gallery"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://www.elegantthemes.com/documentation/divi/ecommerce-divi/"
---

# Shop

The Shop module displays WooCommerce products in a customizable grid layout with images, titles, prices, and add-to-cart functionality.

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

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose between grid layout options. Flexbox and CSS Grid configurations are available for advanced column/row control. |
| Image | image styling | Configure product image appearance including border radius, object fit, hover effects, and overlay behavior. |
| Star Rating | color/size controls | Customize the color and size of the star rating icons displayed on product cards. |
| Sale Badge | styling controls | Customize the appearance of the sale badge including background color, text color, font, and positioning. |
| Text | text styling | Set general text properties for the module including font family, weight, style, alignment, and line height. |
| Title Text | text styling | Style the product title specifically with independent font, size, color, letter spacing, and text shadow controls. |
| Price Text | text styling | Customize the price display including font, size, regular price color, sale price color, and strikethrough styling for original prices. |
| Meta Text | text styling | Style supplementary metadata text such as category labels or descriptions if displayed. |
| Button | button styling | Customize the add-to-cart button appearance including font, text color, background color, border, border radius, padding, and hover effects. |
| Sizing | dimension controls | Set the module's width, height, min/max dimensions, and alignment within its container. |
| Spacing | margin/padding | Adjust the internal padding and external margins of the module and individual product cards. Supports responsive values. |
| Border | border controls | Apply borders to the module container and individual product cards with independent side control. |
| Box Shadow | shadow controls | Add a shadow behind the module or individual product cards with adjustable offset, blur, spread, and color. |
| Filters | filter controls | Apply CSS filter effects including hue rotation, saturation, brightness, contrast, invert, sepia, opacity, and blend mode. |
| Transform | transform controls | Apply CSS transforms including scale, rotate, skew, and translate on the X, Y, and Z axes. |
| Animation | animation controls | Set an entrance animation style with configurable duration, delay, and intensity. |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

| Setting | Type | Description |
|---------|------|-------------|
| CSS ID | text | Assign a unique CSS ID to the module's outermost wrapper for targeted styling or JavaScript hooks. |
| CSS Class | text | Add one or more CSS classes to the module for shared styling rules. |
| Custom Attributes | text | Add custom HTML data attributes to the module element. |
| Custom CSS | code editor | Write CSS rules targeting specific internal elements of the module (e.g., product card, image, title, price, button, sale badge). |
| HTML Tag | select | Choose the semantic HTML element used for the module wrapper (div, section, article, etc.). |
| Conditions | logic builder | Set display conditions based on user role, device, date, or other dynamic criteria. |
| Interactions | event builder | Configure custom interactions triggered by click, hover, or scroll events. |
| Visibility | device toggles | Control whether the module renders on desktop, tablet, and phone screen sizes. |
| Transitions | transition controls | Set the duration, delay, and easing curve for CSS transitions on hover and state changes. |
| Position | position controls | Switch between static, relative, absolute, or fixed positioning with configurable offsets. |
| Scroll Effects | scroll controls | Apply scroll-driven transformations such as vertical/horizontal motion, fade, scale, rotate, and blur. |

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
