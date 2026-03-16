---
title: "Post Navigation"
category: modules
tags: ["modules", "blog", "navigation", "post-links", "previous-next", "theme-builder", "pagination"]
related: ["post-title", "blog", "post-slider"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://www.elegantthemes.com/documentation/divi/post-navigation/"
---

# Post Navigation

The Post Navigation module displays previous and next links that guide visitors between individual blog posts or projects.

## Overview

The Post Navigation module provides directional links at the bottom of a single post or project page, allowing readers to move sequentially through your content. It outputs a "Previous" link pointing to the older adjacent post and a "Next" link pointing to the newer one. This sequential browsing pattern keeps visitors engaged by encouraging them to explore related content without returning to the blog archive.

This module is designed specifically for use in Divi Theme Builder templates and the full-site Visual Editor. When placed on a single post template, it automatically detects the current post and calculates the adjacent entries based on publish date. You can optionally restrict navigation to posts within the same category, which is useful for sites with distinct content sections that should not cross-pollinate navigation links.

The Post Navigation module is functionally distinct from a pagination module, which handles page-level navigation within archive listings and looped elements. Post Navigation operates at the individual post level, linking to specific neighboring entries rather than paginating a list. It pairs well with the [Post Title](post-title.md) module for complete single-post template layouts and the [Blog](blog.md) module for archive pages.

For additional reference on similar navigation concepts, see the [official Elegant Themes Pagination documentation](https://help.elegantthemes.com/en/articles/10358759-the-pagination-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/post-navigation/)

![Post Navigation module](../assets/screenshots/modules/post-navigation/element.png){ loading=lazy }
*The Post Navigation module showing previous and next post links on a single post page.*

## Use Cases

1. **Blog Post Template Footer** — Place the module at the bottom of a single post Theme Builder template so readers can continue to the next article after finishing the current one. This reduces bounce rate by providing an obvious next step.

2. **Portfolio Project Walkthrough** — Add the module to a single project template with same-category navigation enabled. Visitors viewing one case study can move directly to the next project in the same category without returning to the portfolio archive.

3. **Sequential Tutorial Series** — For multi-part tutorials published as individual posts, the previous/next links create a natural reading order. Readers can progress through the series step by step, similar to chapter navigation in an online course.

## How to Add the Post Navigation Module

1. Open the Theme Builder (Divi > Theme Builder) and edit the template assigned to single posts, or open a single post page in the full-site Visual Editor.
2. Click the gray **+** icon to add a new module to a row, typically positioned below the post content area.
3. Search for "Post Navigation" in the module picker or find it in the Theme Builder Modules category, then click to insert it.

## Settings & Options

The Post Navigation module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which posts are linked, what text labels appear, and how the module behaves within the page layout.

| Setting | Type | Description |
|---------|------|-------------|
| Previous Text | text | Customize the label displayed for the previous post link. Defaults to "Previous". |
| Next Text | text | Customize the label displayed for the next post link. Defaults to "Next". |
| In Same Category | toggle | When enabled, restricts navigation to posts that share a category with the current post. When disabled, navigation spans all published posts regardless of category. |
| Show Previous Link | toggle | Enable or disable the previous post link. Useful if you only want forward navigation. |
| Show Next Link | toggle | Enable or disable the next post link. Useful if you only want backward navigation. |
| Link | url | Optionally make the entire module clickable, directing visitors to a specified URL (overrides individual post links). |
| Background | background controls | Set a background color, gradient, image, or video behind the module. |
| Order | select | Control the module's placement order within Flexbox and Grid parent layouts. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |

### Design Tab

The Design tab controls the visual styling of the navigation links and the module container.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Links Text | text styling | Customize the typography of the previous/next link text including font family, weight, size, color, letter spacing, line height, and text shadow. Supports separate hover state styling. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding per side, responsive breakpoints |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Color, offsets, blur radius, spread |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue, blur, invert, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (previous link, next link, link containers) |
| HTML | Semantic HTML tag for the module wrapper (nav, div, section) |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

## Code Examples

### Custom CSS

```css
/* Style the post navigation as a two-column layout */
.et_pb_post_navigation {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
    border-top: 1px solid #e0e0e0;
    border-bottom: 1px solid #e0e0e0;
}

/* Style the previous link */
.et_pb_post_navigation .et_pb_prev_postlink a {
    color: #333;
    font-weight: 600;
    text-decoration: none;
    transition: color 0.3s ease;
}

.et_pb_post_navigation .et_pb_prev_postlink a:hover {
    color: #2ea3f2;
}

/* Style the next link */
.et_pb_post_navigation .et_pb_next_postlink a {
    color: #333;
    font-weight: 600;
    text-decoration: none;
    text-align: right;
    transition: color 0.3s ease;
}

/* Add directional arrows */
.et_pb_post_navigation .et_pb_prev_postlink a::before {
    content: "\2190 ";
}

.et_pb_post_navigation .et_pb_next_postlink a::after {
    content: " \2192";
}

/* Stack links vertically on mobile */
@media (max-width: 767px) {
    .et_pb_post_navigation {
        flex-direction: column;
        gap: 15px;
    }
    .et_pb_post_navigation .et_pb_next_postlink a {
        text-align: left;
    }
}
```

### PHP Hooks

```php
/* Filter the Post Navigation module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_post_nav' !== $render_slug) {
        return $output;
    }
    // Example: Wrap navigation in a semantic nav element
    return '<nav aria-label="Post navigation">' . $output . '</nav>';
}, 10, 2);

/* Customize the adjacent post query to exclude specific categories */
add_filter('get_previous_post_excluded_terms', function($excluded_terms) {
    $excluded_terms[] = 42; // Exclude category ID 42
    return $excluded_terms;
});

add_filter('get_next_post_excluded_terms', function($excluded_terms) {
    $excluded_terms[] = 42;
    return $excluded_terms;
});
```

## Common Patterns

1. **Bordered Separator Navigation** — Add a top border and generous vertical padding to the module to visually separate it from the post content above. Use the Design tab to style the link text in a muted color with a bold hover state, creating a subtle but clear navigational element.

2. **Card-Style Navigation with Post Titles** — Apply a background color, border radius, and box shadow to create a card-like container. The previous and next post titles display inside the card, giving readers a preview of what comes next. This works well on editorial blogs where content discovery is a priority.

3. **Same-Category Navigation for Tutorials** — Enable the In Same Category toggle so readers of a multi-part tutorial series only see links to other parts in that series. Customize the Previous and Next labels to read "Previous Lesson" and "Next Lesson" to reinforce the sequential structure.

## Saving Your Work

After configuring the Post Navigation module, save the Theme Builder template by clicking the green **Save** button. If you are editing in the full-site Visual Editor, save the page normally. The module can also be saved to your Divi Library for reuse across multiple templates by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Post Navigation module in Divi 5 benefits from the updated options framework including Conditions, Interactions, Scroll Effects, and enhanced typography controls not available in Divi 4.

## Troubleshooting

!!! warning "Links Not Appearing"
    If the previous or next link is missing, the current post may be the first or last published post, leaving no adjacent entry to link to. Also verify that the Show Previous Link and Show Next Link toggles are both enabled in the Content tab. If In Same Category is on, confirm other posts exist in the same category.

!!! warning "Module Not Displaying on Frontend"
    The Post Navigation module is designed for single post or project templates. If placed on a static page or archive template, it will not have adjacent post data to display and may render empty. Ensure the module is used in a Theme Builder template assigned to single posts.

!!! tip "Navigation Links Showing Unrelated Posts"
    If links point to posts from unrelated topics, enable the **In Same Category** toggle. This restricts navigation to posts sharing at least one category with the current post, keeping the browsing experience contextually relevant.

## Related

- [Post Title](post-title.md)
- [Blog](blog.md)
- [Post Slider](post-slider.md)
