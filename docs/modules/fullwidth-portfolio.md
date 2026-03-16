---
title: "Fullwidth Portfolio"
category: modules
tags: ["modules", "fullwidth", "portfolio", "projects", "grid", "carousel", "gallery"]
related: ["portfolio", "filterable-portfolio", "gallery"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://www.elegantthemes.com/documentation/divi/fullwidth-portfolio/"
---

# Fullwidth Portfolio

The Fullwidth Portfolio module displays WordPress Projects in an edge-to-edge grid or carousel layout that spans the full width of the page.

## Overview

The Fullwidth Portfolio module is built to showcase your WordPress Projects at maximum visual impact. Unlike the standard [Portfolio](portfolio.md) module, the fullwidth variant stretches across the entire browser window, giving each project thumbnail more room to breathe and creating a cinematic, gallery-like presentation. It pulls directly from the native WordPress Projects custom post type, so any project you publish is automatically available for display.

The module supports two primary layout modes: a grid that tiles project thumbnails in even columns across the page, and a carousel that presents projects in a horizontally scrollable strip. Both modes display featured images as the visual anchor, with optional overlays showing the project title and category on hover. Pagination controls let visitors browse through larger collections without leaving the page.

Because the Fullwidth Portfolio occupies a fullwidth section, it works best at the top of a page, between content sections, or as a dedicated portfolio archive. It pairs naturally with the [Filterable Portfolio](filterable-portfolio.md) module for category-based browsing and the [Gallery](gallery.md) module for non-project image collections.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10358290-the-portfolio-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/fullwidth-portfolio/)

![Fullwidth Portfolio module](../assets/screenshots/modules/fullwidth-portfolio/element.png){ loading=lazy }
*The Fullwidth Portfolio module displaying project thumbnails in a fullwidth layout.*

## Use Cases

1. **Agency or Freelancer Portfolio Page** — Showcase completed client projects in a dramatic, edge-to-edge grid that lets the work speak for itself. Visitors see large thumbnails and can click through to individual project pages for details.

2. **Homepage Featured Work Section** — Place the module in a fullwidth section near the top of a homepage to immediately highlight your best projects. The carousel mode keeps the section compact while still exposing multiple pieces.

3. **Photography or Design Gallery** — Use the grid layout with project categories to organize shoots or design collections. Visitors hover over thumbnails to see titles and categories, then click to view full project details.

## How to Add the Fullwidth Portfolio Module

1. Open the Visual Builder on the page you want to edit. Add a **Fullwidth Section** if one is not already present, since this module requires a fullwidth section to function.
2. Click the gray **+** icon inside the fullwidth section to add a new module.
3. Search for "Fullwidth Portfolio" in the module picker or locate it in the Fullwidth Modules category, then click to insert it.

## Settings & Options

The Fullwidth Portfolio module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which projects are displayed, how they are ordered, and what metadata appears alongside each item.

| Setting | Type | Description |
|---------|------|-------------|
| Posts Number | number input | Set the maximum number of projects to display at once. Controls how many thumbnails appear before pagination takes over. |
| Include Categories | multi-select | Choose specific project categories to display. Leave empty to show all categories. |
| Elements — Show Title | toggle | Display or hide the project title overlay on each thumbnail. |
| Elements — Show Categories | toggle | Display or hide the project category labels on each thumbnail. |
| Elements — Show Pagination | toggle | Enable or disable pagination controls below the portfolio grid. |
| Link | url | Optionally make the entire module clickable, directing visitors to a specified URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the entire module. |
| Order | select | Control the module's placement order within Flexbox and Grid parent layouts. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel for easier identification. |
| Meta — Disable On | device toggles | Control which devices the module appears on in the builder interface. |

### Design Tab

The Design tab provides controls for the visual presentation of the portfolio grid, including layout, typography, and effects.

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose between Fullwidth (carousel-style) or Grid layout. Grid mode offers additional Flexbox and CSS Grid configuration options. |
| Image | image styling | Configure featured image appearance including border radius, object fit, and hover effects for project thumbnails. |
| Text | text styling | Set general text properties like font family, weight, style, alignment, and line height for the module. |
| Title Text | text styling | Customize the project title typography including font, size, color, letter spacing, and text shadow. |
| Meta Text | text styling | Style the category labels and other metadata text that appears on project overlays. |
| Pagination Text | text styling | Control the appearance of pagination links including font, size, color, and hover states. |
| Sizing | dimension controls | Set the module's width, height, min/max dimensions, and alignment within its container. |
| Spacing | margin/padding | Adjust the internal padding and external margins of the module. Supports responsive values. |
| Border | border controls | Apply borders to the module container with independent control over each side's width, style, and color. |
| Box Shadow | shadow controls | Add a shadow effect behind the module with adjustable horizontal/vertical offset, blur, spread, and color. |
| Filters | filter controls | Apply CSS filter effects including hue rotation, saturation, brightness, contrast, invert, sepia, opacity, and blend mode. |
| Transform | transform controls | Apply CSS transforms including scale, rotate, skew, and translate on the X, Y, and Z axes. |
| Animation | animation controls | Set an entrance animation style (fade, slide, bounce, zoom, flip, fold, roll) with configurable duration, delay, and intensity. |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

| Setting | Type | Description |
|---------|------|-------------|
| CSS ID | text | Assign a unique CSS ID to the module's outermost wrapper for targeted styling or JavaScript hooks. |
| CSS Class | text | Add one or more CSS classes to the module for shared styling rules. |
| Custom Attributes | text | Add custom HTML data attributes to the module element. |
| Custom CSS | code editor | Write CSS rules that target specific internal elements of the module (e.g., title, image, overlay, pagination). |
| HTML Tag | select | Choose the semantic HTML element used for the module wrapper (div, section, article, etc.). |
| Conditions | logic builder | Set display conditions based on user role, device, date, or other dynamic criteria. When conditions are not met, the module is hidden. |
| Interactions | event builder | Configure custom interactions triggered by click, hover, or scroll events (show/hide elements, toggle classes, etc.). |
| Visibility | device toggles | Control whether the module renders on desktop, tablet, and phone screen sizes. |
| Transitions | transition controls | Set the duration, delay, and easing curve for CSS transitions on hover and state changes. |
| Position | position controls | Switch between default (static), relative, absolute, or fixed positioning with configurable offsets. |
| Scroll Effects | scroll controls | Apply scroll-driven transformations such as vertical/horizontal motion, fade, scale, rotate, and blur that activate as the visitor scrolls. |

## Code Examples

### Custom CSS

```css
/* Add a dark overlay to portfolio thumbnails for better title readability */
.et_pb_fullwidth_portfolio .et_pb_portfolio_image .et_overlay {
    background-color: rgba(0, 0, 0, 0.5);
}

/* Style the project title on hover */
.et_pb_fullwidth_portfolio .et_pb_portfolio_image h3 {
    font-size: 18px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Increase spacing between grid items */
.et_pb_fullwidth_portfolio .et_pb_portfolio_item {
    padding: 10px;
}

/* Responsive: stack to single column on mobile */
@media (max-width: 767px) {
    .et_pb_fullwidth_portfolio .et_pb_portfolio_item {
        width: 100% !important;
    }
}
```

### PHP Hooks

```php
/* Filter the Fullwidth Portfolio module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_fullwidth_portfolio' !== $render_slug) {
        return $output;
    }
    // Example: Add a wrapper div for custom styling
    return '<div class="custom-portfolio-wrapper">' . $output . '</div>';
}, 10, 2);

/* Modify the number of projects queried by the portfolio */
add_filter('pre_get_posts', function($query) {
    if (!is_admin() && $query->get('post_type') === 'project') {
        $query->set('posts_per_page', 12);
    }
    return $query;
});
```

## Common Patterns

1. **Fullwidth Carousel Hero** — Place the Fullwidth Portfolio module at the top of a homepage inside a fullwidth section. Use the Fullwidth layout mode to create a scrollable carousel of featured projects. Disable categories and pagination for a clean, minimal look that focuses on the imagery.

2. **Categorized Work Showcase** — Enable both title and category overlays, then use the Include Categories setting to show only projects from specific categories. Place multiple Fullwidth Portfolio modules in sequence, each filtered to a different category, to create a sectioned portfolio page.

3. **Grid with Custom Overlay Styling** — Use the Grid layout and apply custom CSS to replace the default hover overlay with a gradient fade-up effect. Combine with the Box Shadow and Border Radius design settings to create a modern card-based appearance for each project thumbnail.

## Saving Your Work

After configuring the Fullwidth Portfolio module, click the green **Save** button at the bottom of the Visual Builder interface. You can also save the module as a preset or add it to your Divi Library for reuse across pages. To save as a library item, right-click the module and select **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Fullwidth Portfolio module in Divi 5 benefits from the new rendering engine and supports the updated options framework including Flexbox/Grid layout controls, the Conditions system, and Scroll Effects — features not available in Divi 4.

## Troubleshooting

!!! warning "No Projects Displaying"
    If the Fullwidth Portfolio appears empty, verify that you have published at least one Project (under Projects > Add New in the WordPress dashboard). Check that the projects have featured images assigned, as the module relies on featured images for thumbnails. Also confirm the Include Categories filter is not set to an empty category.

!!! warning "Module Not Available in Module Picker"
    The Fullwidth Portfolio module can only be placed inside a **Fullwidth Section**. If you are working inside a standard section with rows, you will not see it in the module picker. Add a fullwidth section first, then insert the module.

!!! tip "Carousel Not Scrolling"
    If the carousel layout shows all items at once without scrolling, check that the Posts Number setting is high enough to exceed one screen of thumbnails. The carousel navigation arrows only appear when there are more items than can fit in the visible area.

## Related

- [Portfolio](portfolio.md)
- [Filterable Portfolio](filterable-portfolio.md)
- [Gallery](gallery.md)
