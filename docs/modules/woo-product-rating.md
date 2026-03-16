---
title: "Woo Product Rating"
description: "Complete Divi 5 Woo Product Rating module reference — settings, design options, code examples, and troubleshooting for WooCommerce product star ratings."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product", "reviews", "rating"]
related: ["woo-product-reviews", "woo-product-title"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12040851"
---

# Woo Product Rating

The Woo Product Rating module displays the average star rating for a WooCommerce product based on customer reviews, with optional review count text.

!!! abstract "Quick Reference"
    **What it does:** Renders the average product star rating derived from WooCommerce customer reviews, with customizable star appearance and optional review count display.
    **When to use it:** Product page templates, custom product layouts in the Theme Builder
    **Key settings:** Product selector, Show Star Review, Show Customer Reviews Count, Layout (Inline/Stacked), Star Rating styling
    **Block identifier:** `divi/wc-product-rating`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12040851)

!!! tip "When to Use This Module"
    - Displaying the average review rating on custom product page templates as social proof
    - Positioning the star rating near the product title or price for quick trust signals
    - Styling the rating display to match your store's visual design

!!! warning "When NOT to Use This Module"
    - On non-WooCommerce pages — this module requires a product context
    - For full review listings with text — use [Woo Product Reviews](woo-product-reviews.md)
    - For product grids with ratings — use [Shop](shop.md) (ratings are built in)

## Overview

The Woo Product Rating module displays the average star rating calculated from all customer reviews submitted for a WooCommerce product. It provides two distinct visual elements: the star rating visualization (filled and unfilled stars representing the average score) and a text-based review count that shows how many customer reviews contribute to the rating.

Both elements can be independently toggled on or off, and the layout can be set to either inline (stars and count side by side) or stacked (stars above count). The star appearance is fully customizable, including color, size, alignment, and letter spacing between individual stars.

This module serves as a powerful social proof element that helps build customer trust and confidence in purchasing decisions.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12040851).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. Products must have customer reviews with ratings for this module to display content.

<!-- ![Woo Product Rating module](../assets/screenshots/modules/woo-product-rating/element.png){ loading=lazy } -->
<!-- *The Woo Product Rating module displaying stars and review count in the Visual Builder.* -->

## Use Cases

1. **Social Proof Near Title** — Place the rating module directly below the product title and above the price, providing immediate trust signals that influence purchasing decisions.
2. **Compact Inline Rating** — Use the inline layout with a small star size next to the product price, creating a compact rating display that reinforces value without dominating the layout.
3. **Prominent Review Callout** — Use the stacked layout with large, colored stars and a prominent review count to create an attention-grabbing rating display on products with many positive reviews.

## How to Add the Woo Product Rating Module

1. Navigate to **Divi > Theme Builder** and create or edit a product page template.
2. Open the Visual Builder on the product template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Product Rating" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12040851).

## Settings & Options

The Woo Product Rating module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which product is referenced and what rating elements are displayed.

| Setting | Type | Description |
|---------|------|-------------|
| Content (Product) | select | Choose which product supplies the rating data. On a dynamic product template, this defaults to the current product. |
| Show Star Review | toggle | Display or hide the star rating visualization. Enabled by default. |
| Show Customer Reviews Count | toggle | Display or hide the text showing the number of customer reviews (e.g., "(12 customer reviews)"). Enabled by default. |
| Link | url | Optionally make the entire module clickable, directing users to a specific page, section, or external URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the rating module. |
| Loop | toggle | Enable the Loop Builder feature for dynamic template contexts. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Woo Product Rating Content tab settings](../assets/screenshots/modules/woo-product-rating/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the visual styling of the star rating and review count text.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose between **Inline** (stars and review count side by side) or **Stacked** (stars above review count) orientation. |
| Star Rating | star styling | Customize the star alignment, color (filled and unfilled), size, and letter spacing between individual stars. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height for the review count text |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, hue, saturation, blending) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Woo Product Rating Design tab settings](../assets/screenshots/modules/woo-product-rating/settings-design.png){ loading=lazy } -->

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

<!-- ![Woo Product Rating Advanced tab settings](../assets/screenshots/modules/woo-product-rating/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the rating container */
.et_pb_wc_rating {
    margin-bottom: 10px;
}

/* Style the star rating */
.et_pb_wc_rating .star-rating {
    font-size: 16px;
    color: #f5a623;
}

/* Style filled stars */
.et_pb_wc_rating .star-rating span::before {
    color: #f5a623;
}

/* Style unfilled stars */
.et_pb_wc_rating .star-rating::before {
    color: #ddd;
}

/* Style the review count text */
.et_pb_wc_rating .woocommerce-review-link {
    font-size: 14px;
    color: #666;
    text-decoration: none;
    margin-left: 8px;
}

/* Hover effect on review count link */
.et_pb_wc_rating .woocommerce-review-link:hover {
    color: #2ea3f2;
    text-decoration: underline;
}

/* Stacked layout adjustments */
.et_pb_wc_rating .star-rating + .woocommerce-review-link {
    display: block;
    margin-top: 5px;
    margin-left: 0;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_rating .star-rating {
        font-size: 14px;
    }
    .et_pb_wc_rating .woocommerce-review-link {
        font-size: 13px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Product Rating module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_rating' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Modify the review count text */
add_filter('woocommerce_product_review_count_html', function($html) {
    // Customize the review count display
    return $html;
});
```

## Common Patterns

1. **Below-Title Social Proof** — Place the rating module directly beneath the product title and above the price. Use the inline layout with medium-sized gold stars and a subtle gray review count link that scrolls to the reviews section when clicked.

2. **Compact Rating Badge** — Position the rating module next to the product price in the same row. Hide the review count text and show only the stars at a small size, creating a compact trust signal alongside the price.

3. **Prominent Review Callout** — Use the stacked layout with large stars and a bold review count. Apply a light background color and padding to the module to create a standalone rating card that draws attention on product pages with many positive reviews.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-product-rating` — *Needs Testing*

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
| Show Star Review | `attrs.show_star_review` | Toggle for star visibility |
| Show Customer Reviews Count | `attrs.show_reviews_count` | Toggle for review count text |

!!! tip "Module Selection Guidance"
    For the average star rating display use Woo Product Rating; for the full review listing with text use Woo Product Reviews; for product grids with built-in ratings use Shop.

## Saving Your Work

After configuring the product rating module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. Products must have customer reviews with star ratings for this module to display content. Enable reviews under **WooCommerce > Settings > Products**.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Product Rating module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The module is placed on a product page template or a page with a valid product context
    - The module is not inside a disabled section or row
    - Visibility settings are not hiding it on the current device

!!! warning "No Stars Showing"
    If the module renders but no stars appear, check that:

    - The product has at least one customer review with a star rating
    - Product reviews are enabled in **WooCommerce > Settings > Products > Enable reviews**
    - The **Show Star Review** toggle is enabled in the Content tab
    - Star ratings are enabled for reviews (check "Enable star rating on reviews" in WooCommerce settings)

!!! warning "Review Count Shows Zero"
    If stars display but the review count shows "(0 customer reviews)", verify that:

    - Reviews have been submitted and approved (not pending moderation)
    - The **Show Customer Reviews Count** toggle is enabled in the Content tab

!!! tip "Stars Appear Unstyled"
    If the stars appear as plain text characters rather than styled star icons, check for CSS conflicts or a missing WooCommerce stylesheet. The stars rely on WooCommerce's font icon system, which requires the WooCommerce stylesheet to be loaded.

## Related

- [Woo Product Reviews](woo-product-reviews.md) — Displays the full customer review listing with individual review text
- [Woo Product Title](woo-product-title.md) — Displays the product title with customizable typography
- [Woo Product Tabs](woo-product-tabs.md) — Tabbed display including a reviews tab
- [Shop](shop.md) — Product grid module with built-in rating display
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
