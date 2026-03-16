---
title: "Group Carousel"
category: modules
tags: ["modules", "group-carousel", "carousel", "slider", "slideshow", "navigation", "interactive"]
related: ["group", "slider", "gallery"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11982051"
---

# Group Carousel

The Group Carousel module displays multiple grouped modules in a horizontal, scrollable carousel with configurable navigation and animation.

## Overview

The Group Carousel module extends the concept of the Group module by arranging multiple slide groups in a horizontal carousel that visitors can navigate via arrows, dots, or touch swipe. Each slide within the carousel is its own group container capable of holding any combination of child modules such as images, text, buttons, or blurbs.

Carousel behavior is highly configurable. You can set how many slides are visible at once, how many advance per navigation click, whether slides rotate automatically, and whether the active slide stays centered. Arrow and dot navigation can each be toggled independently, and their positioning, sizing, and color are adjustable through the Design tab.

This module is well suited for content that benefits from horizontal browsing without consuming excessive vertical page space. Testimonial sliders, portfolio previews, product highlights, and team member showcases all work naturally in this format. The carousel is touch-responsive on mobile devices, providing a native swipe experience.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11982051).

![Group Carousel module](../assets/screenshots/modules/group-carousel/element.png){ loading=lazy }
*The Group Carousel module displaying multiple slide groups with navigation controls.*

## Use Cases

1. **Portfolio Showcase** — Present project previews in grouped slides, each containing a thumbnail image, project title, and short description, allowing visitors to browse work samples without overwhelming the page layout.
2. **Testimonial Slider** — Display client testimonials with photos, quotes, and attribution in a compact swipeable carousel that cycles automatically or on user interaction.
3. **Product Collection Display** — Highlight related products in interactive groups showing product images, names, and prices, encouraging quick exploration across a catalog.

## How to Add the Group Carousel Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Group Carousel" in the module picker or locate it in the Layout Elements category, then click to insert it.

<!-- TODO: Add animated GIF demonstrating module insertion -->

## Settings & Options

The Group Carousel module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the carousel slides, rotation behavior, navigation toggles, and module metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Slides | item list | Add, edit, reorder, or remove individual carousel slide groups. Each slide is a container that can hold multiple child modules. |
| Automatic Rotation | toggle | Enables automatic slide advancement at a set interval. When disabled, slides only change via manual navigation. |
| Center Mode | toggle | Keeps the active slide centered in the viewport with adjacent slides partially visible on either side. |
| Transition Speed | slider/number | Controls how quickly slides animate between positions, measured in milliseconds. |
| Slides to Show | number | Determines how many slide groups are visible simultaneously in the carousel viewport. |
| Slides to Scroll | number | Sets how many slides advance per navigation click or swipe gesture. |
| Show Dot Navigation | toggle | Displays indicator dots below or above the carousel for direct slide selection. |
| Show Arrows | toggle | Displays left and right arrow buttons for manual slide navigation. |
| Left Arrow Icon | icon picker | Choose a custom icon for the left navigation arrow. |
| Right Arrow Icon | icon picker | Choose a custom icon for the right navigation arrow. |
| Link | url/link settings | Makes the entire carousel module clickable, directing users to a URL. |
| Background | background controls | Apply a background color, gradient, image, or video behind the carousel container. |
| Loop | toggle | Enables the loop builder for dynamic content repetition based on a data source. |
| Meta | admin label | Set an admin label and control Visual Builder visibility. |

<!-- ![Group Carousel Content tab settings](../assets/screenshots/modules/group-carousel/settings-content.png){ loading=lazy } -->
<!-- TODO: Capture Content tab screenshot -->

### Design Tab

The Design tab controls the visual appearance of navigation elements, individual slide groups, and overall module styling.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Arrows Position | dropdown | Place arrow controls inside, outside, or centered relative to the carousel container. |
| Arrow Color | color picker | Set the color of the navigation arrow icons. |
| Arrow Font Size | slider | Adjust the size of the arrow icons in pixels. |
| Dot Position | dropdown | Position dot indicators below, above, or overlaid on the carousel. |
| Dot Alignment | dropdown | Align dots to the left, center, or right of the carousel. |
| Dot Size | slider | Control the diameter of individual dot indicators. |
| Dot Color | color picker | Set the color of the navigation dots. |
| Groups | styling controls | Apply background, padding, border, and shadow styles uniformly to all carousel slide groups. |
| Active Groups | styling controls | Override styling for the currently active slide group, allowing it to stand out visually. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (hue, saturation, brightness, blend mode) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Group Carousel Design tab settings](../assets/screenshots/modules/group-carousel/settings-design.png){ loading=lazy } -->
<!-- TODO: Capture Design tab screenshot -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, interactions, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

<!-- ![Group Carousel Advanced tab settings](../assets/screenshots/modules/group-carousel/settings-advanced.png){ loading=lazy } -->
<!-- TODO: Capture Advanced tab screenshot -->

## Code Examples

### Custom CSS

```css
/* Style the carousel container */
.et_pb_group_carousel {
    overflow: hidden;
    border-radius: 12px;
}

/* Highlight the active slide with a subtle scale effect */
.et_pb_group_carousel .slick-slide.slick-active {
    transform: scale(1.02);
    transition: transform 0.3s ease;
}

/* Custom arrow styling */
.et_pb_group_carousel .slick-arrow {
    background: rgba(0, 0, 0, 0.5);
    border-radius: 50%;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
}

.et_pb_group_carousel .slick-arrow:hover {
    background: rgba(0, 0, 0, 0.8);
}

/* Custom dot styling */
.et_pb_group_carousel .slick-dots li button {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #cccccc;
    transition: background 0.3s ease;
}

.et_pb_group_carousel .slick-dots li.slick-active button {
    background: #2ea3f2;
}

/* Responsive: show fewer slides on mobile */
@media (max-width: 767px) {
    .et_pb_group_carousel .slick-slide {
        padding: 0 8px;
    }
}
```

### PHP Hooks

```php
/* Add a custom wrapper around the Group Carousel output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_group_carousel' !== $render_slug) {
        return $output;
    }
    $output = '<div class="custom-carousel-wrapper">' . $output . '</div>';
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Testimonial Carousel** — Create a Group Carousel with three visible slides. Each slide group contains an image module (client photo), a text module (quote), and a heading (client name). Enable automatic rotation with a 5-second interval and dot navigation for manual browsing.

2. **Product Highlight Slider** — Set slides to show at 3 with 1 slide to scroll. Each group holds a product image, name heading, price text, and "View Details" button. Use the Active Groups styling to add a subtle border or shadow to the currently focused product.

3. **Team Member Carousel** — Use center mode to spotlight the active team member while showing adjacent members at reduced opacity. Each slide group contains a circular profile image, name heading, title text, and social media icon links.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/group-carousel` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Child groups | Nested blocks | Each carousel slide is a nested group block |
| Autoplay | `attrs.autoplay` | Automatic slide rotation toggle |

!!! tip "Module Selection Guidance"
    For rotating groups of modules use Group Carousel; for image slideshows use Slider or Gallery; for static grouping use Group.

## Saving Your Work

After configuring the Group Carousel module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Slides Not Advancing Automatically"
    If automatic rotation is not working:

    - Confirm that **Automatic Rotation** is toggled on in the Content tab.
    - Check whether the transition speed is set to an extremely high value, causing very slow movement.
    - JavaScript errors on the page can prevent the carousel script from initializing. Inspect the browser console for errors.

!!! warning "Navigation Arrows or Dots Not Visible"
    If navigation controls are missing:

    - Verify that **Show Arrows** and **Show Dot Navigation** are enabled in the Content tab.
    - If arrows are positioned outside the carousel, ensure the parent column has enough horizontal space to display them.
    - Check whether the arrow or dot color matches the background, rendering them invisible.

!!! tip "Carousel Looks Cramped on Mobile"
    Reduce the **Slides to Show** value for tablet and phone breakpoints using the responsive toggle. A single visible slide per viewport often works best on narrow screens. Also reduce horizontal padding on individual slide groups to maximize usable content area.

## Related

- [Group](group.md) — Static container module for wrapping child elements without carousel behavior
- [Slider](slider.md) — Full-width sliding content with text overlays and call-to-action buttons
- [Gallery](gallery.md) — Image gallery with grid and slider display modes
