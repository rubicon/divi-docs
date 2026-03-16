---
title: "Post Carousel"
description: "Complete Divi 5 Post Carousel module reference — settings, design options, code examples, and troubleshooting for dynamic post carousels with category filtering and overlay effects."
category: modules
tags: ["modules", "content-modules", "carousel", "posts", "blog", "dynamic-content", "slider"]
related: ["post-slider", "blog", "slider"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10373482"
---

# Post Carousel

The Post Carousel module displays WordPress posts in a horizontal carousel or grid format, with featured images, titles, dates, and hover overlay effects.

!!! abstract "Quick Reference"
    **What it does:** Generates a browsable carousel or grid of WordPress posts with featured images, titles, and publish dates.
    **When to use it:** Homepage featured content sections, category spotlights, blog archive enhancements
    **Key settings:** Post Type, Categories, Layout (Carousel/Grid), Carousel Columns, Overlay
    **Block identifier:** `divi/post-carousel`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10373482)

!!! tip "When to Use This Module"
    - Creating a visually engaging featured posts section that scrolls horizontally
    - Building a homepage content spotlight that highlights recent articles from specific categories
    - Displaying portfolio or project items in a compact, browsable format

!!! warning "When NOT to Use This Module"
    - For a fullscreen post slideshow with text overlays — use [Post Slider](post-slider.md)
    - For a traditional blog feed with excerpts — use [Blog](blog.md)
    - For a manual image/content slider — use [Slider](slider.md)

## Overview

The Post Carousel module creates a dynamic, visually compact display of WordPress posts that customers can browse by scrolling or swiping horizontally. Unlike the Post Slider, which presents one post at a time in a fullscreen format, the Post Carousel shows multiple posts simultaneously in a card-based layout, making it efficient for surfacing a larger number of items in a smaller space.

The module queries posts based on the selected post type and optional category filters, then renders each post as a card showing its featured image with configurable overlay effects, the post title, and optionally the publish date. Users can browse the carousel by swiping on touch devices or using the built-in navigation.

Two layout modes are available: **Carousel**, which creates the traditional horizontal scrolling strip, and **Grid**, which arranges posts in a static CSS Grid or Flexbox layout with configurable columns and column spacing. The Grid layout transforms the module into a static post grid, which is useful when you want the card-based visual style of the carousel without the scrolling behavior.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10373482).

<!-- ![Post Carousel module](../assets/screenshots/modules/post-carousel/element.png){ loading=lazy } -->
<!-- *The Post Carousel module displaying recent blog posts in a three-column carousel with hover overlays.* -->

## Use Cases

1. **Homepage Featured Posts** — Place the carousel in a prominent section on the homepage to highlight recent or featured blog posts with their images, drawing visitors into your content with a visually engaging browsable format.
2. **Category Spotlight** — Filter the carousel to a specific post category to create a focused content section within a landing page, such as "Latest News" or "Featured Projects," without displaying the entire blog feed.
3. **Portfolio Grid** — Use the Grid layout mode with custom post types to display portfolio projects, case studies, or team members in a card-based grid with hover overlay effects for a modern, interactive presentation.

## How to Add the Post Carousel Module

1. Open the Visual Builder on the page where you want the carousel to appear.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Post Carousel" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10373482).

## Settings & Options

The Post Carousel module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which posts appear in the carousel, what elements are shown on each card, and the module's link and background options.

| Setting | Type | Description |
|---------|------|-------------|
| Post Type | select | Choose which WordPress post type to query for the carousel (e.g., Posts, Pages, or custom post types). |
| Carousel Title | text | Set an optional heading displayed above the carousel, such as "Featured Articles" or "Recent Projects." |
| Categories | multi-select | Filter the carousel to display posts from specific categories. When no categories are selected, all published posts of the chosen type are included. |
| Show Post Title | toggle | Display or hide the post title text on each carousel card. |
| Show Publish Date | toggle | Display or hide the post's publish date on each carousel card. |
| Link | url | Make the entire Post Carousel module clickable, directing users to a specific page or URL rather than the default per-post linking. |
| Background | background controls | Set a background color, gradient, image, or video behind the carousel module container. |
| Order | select | Set the flexbox order of the module within Flexbox and CSS Grid parent layouts. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Post Carousel Content tab settings](../assets/screenshots/modules/post-carousel/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the carousel layout mode, columns, image overlays, and all text styling.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose between Carousel (horizontal scrolling) or Grid (static CSS Grid/Flexbox) display mode. |
| Carousel Columns | number | Set the number of columns displayed in the grid layout. Only active when Layout is set to Grid. |
| Column Spacing | range | Adjust the horizontal gap between columns in the grid layout. Only active when Layout is set to Grid. |
| Overlay | overlay styling | Configure the image hover overlay appearance, including background color, icon, and opacity. |
| Image | image styling | Style the featured image on each card, including border, shadow, and spacing. |
| Title Text | text styling | Customize the carousel title heading, including font family, weight, size, color, and alignment. |
| Carousel Item Title Text | text styling | Style the individual post title text on each card, including heading level, font, weight, alignment, color, and size. |
| Meta Text | text styling | Customize the body text styles for the publish date and other metadata displayed on each card. |

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

<!-- ![Post Carousel Design tab settings](../assets/screenshots/modules/post-carousel/settings-design.png){ loading=lazy } -->

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

<!-- ![Post Carousel Advanced tab settings](../assets/screenshots/modules/post-carousel/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the carousel container */
.et_pb_post_carousel {
    padding: 20px 0;
}

/* Style the carousel title */
.et_pb_post_carousel .et_pb_module_header {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #333;
}

/* Style individual carousel cards */
.et_pb_post_carousel .et_pb_carousel_item {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    transition: box-shadow 0.3s ease, transform 0.2s ease;
}

.et_pb_post_carousel .et_pb_carousel_item:hover {
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
    transform: translateY(-2px);
}

/* Style post images */
.et_pb_post_carousel .et_pb_carousel_item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

/* Style the overlay on hover */
.et_pb_post_carousel .et_overlay {
    background: rgba(0, 0, 0, 0.5);
    transition: opacity 0.3s ease;
}

/* Style post titles within cards */
.et_pb_post_carousel .et_pb_carousel_item h3 {
    font-size: 16px;
    font-weight: 600;
    padding: 12px 15px 5px;
    color: #333;
}

/* Style the publish date */
.et_pb_post_carousel .et_pb_carousel_item .post-meta {
    font-size: 13px;
    color: #888;
    padding: 0 15px 12px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_post_carousel .et_pb_carousel_item img {
        height: 160px;
    }
}
```

### PHP Hooks

```php
/* Filter the Post Carousel module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_post_carousel' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Filter the post query used by the carousel */
add_filter('pre_get_posts', function($query) {
    if (!is_admin() && $query->get('post_type') === 'post') {
        // Exclude sticky posts from carousel queries
        $query->set('ignore_sticky_posts', true);
    }
    return $query;
});
```

## Common Patterns

1. **Homepage Content Strip** — Place the Post Carousel in a full-width section on the homepage using the Carousel layout with 3-4 visible items. Add a descriptive carousel title like "Latest From The Blog" and enable both title and date elements on each card for a complete content preview strip.

2. **Category Feature Grid** — Use the Grid layout filtered to a single category with 3 columns and generous column spacing. This creates a static featured posts grid that works well as a content section within longer landing pages.

3. **Image-Only Portfolio Browse** — Hide post titles and dates to create a pure image carousel with hover overlays. Apply custom overlay styling with a zoom icon to create an interactive portfolio browsing experience where images are the sole focus.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/post-carousel` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For a compact multi-post carousel use Post Carousel; for a fullscreen single-post slideshow use Post Slider; for a traditional blog feed with excerpts use Blog; for a manual content slider use Slider.

## Saving Your Work

After configuring the post carousel module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Post Carousel module does not appear on the front end, verify that:

    - The module is placed inside a valid section and row
    - There are published posts matching the selected post type and category filters
    - Visibility settings are not hiding the module on the current device

!!! warning "No Posts Displaying"
    If the module renders but shows no post cards, check that:

    - The selected post type has published posts
    - The selected categories have posts assigned to them
    - Posts have featured images set (the carousel relies on featured images for its visual display)

!!! tip "Carousel Not Scrolling"
    If the carousel appears as a static grid instead of scrolling, verify that the Layout setting in the Design tab is set to Carousel rather than Grid. If the Layout is correctly set to Carousel but there are fewer posts than visible columns, the carousel will not scroll because there is nothing to scroll to.

## Related

- [Post Slider](post-slider.md) — Full-width post slideshow with text overlays and navigation
- [Blog](blog.md) — Traditional blog feed with excerpts and pagination
- [Slider](slider.md) — Manual content slider with custom slides
- [Gallery](gallery.md) — Image gallery with grid and slider options
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
