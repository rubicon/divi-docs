---
title: "Pagination"
description: "Complete Divi 5 Pagination module reference — main query and loop element targeting, link text, category filtering, and styling."
category: modules
tags: ["modules", "pagination", "navigation", "blog", "posts", "loop", "previous", "next"]
related: ["blog", "portfolio", "post-navigation"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10358759-the-pagination-module-in-divi-5"
---

# Pagination

The Pagination module provides previous and next navigation links for browsing between posts, pages, or loop-driven content.

!!! abstract "Quick Reference"
    **What it does:** Adds previous/next navigation links for browsing posts or paginating loop-driven content.
    **When to use it:** Blog post footers, portfolio browsing, loop-powered archive pagination
    **Key settings:** Target (Main Query / Looped Element), Text labels, Categories, Navigation direction
    **Block identifier:** `divi/pagination`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10358759-the-pagination-module-in-divi-5)

!!! tip "When to Use This Module"
    - Adding page-level navigation to loop-powered archive or listing pages
    - Providing previous/next links within the main WordPress query on single posts
    - Connecting pagination controls to a specific looped section, row, or module

!!! warning "When NOT to Use This Module"
    - Linking to specific adjacent posts with title previews → use [Post Navigation](post-navigation.md)
    - Displaying a paginated grid of blog posts with built-in controls → use [Blog](blog.md)

## Overview

The Pagination module adds directional navigation links that let visitors move sequentially through content. It supports two primary modes: Main Query targeting, which navigates between individual posts or pages in the standard WordPress query, and Looped Element targeting, which paginates through content sections powered by the Divi loop builder.

In Main Query mode, the module generates previous and next links based on the published post order. You can restrict navigation to posts within the same category or allow it across all published content. Custom text labels for the previous and next links can replace the default wording to match your site's voice and design.

In Looped Element mode, the module connects to a loop-powered section, row, column, or module and provides pagination controls for that specific looped content. This is useful for archive pages, custom post type listings, or any layout where content is generated dynamically through the loop builder.

The module is typically placed at the bottom of single post templates or archive layouts. It renders as simple text links by default, but the Design tab provides full typography and styling controls to match your theme's navigation patterns.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10358759-the-pagination-module-in-divi-5).

![Pagination module](../assets/screenshots/modules/pagination/element.png){ loading=lazy }
*The Pagination module displaying previous and next navigation links.*

## Use Cases

1. **Blog Post Navigation** — Place at the bottom of single blog post templates so readers can move to the previous or next article without returning to the blog index page.
2. **Portfolio Case Study Browsing** — Add to single project templates to guide visitors through related portfolio pieces sequentially, encouraging deeper engagement with your work.
3. **Loop Content Pagination** — Connect to a looped element on an archive or listing page to provide page-by-page navigation through dynamically generated content sets.

## How to Add the Pagination Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Pagination" in the module picker or find it in the Content Elements category, then click to insert it.


## Settings & Options

The Pagination module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the pagination target, link text, category filtering, navigation direction, and module metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Target | dropdown | Choose **Main Query** to navigate between posts/pages in the WordPress query, or **Looped Element** to paginate through loop builder content targeting a specific section, row, column, or module. |
| Text | text fields | Customize the labels for the Previous and Next navigation links. Default values can be replaced with any text. |
| Categories | dropdown | When using Main Query mode, choose whether navigation stays within the same category as the current post or spans all published posts regardless of category. |
| Navigation | dropdown | Select which links to display: previous only, next only, or both previous and next. |
| Background | background controls | Apply a background color, gradient, image, or video behind the Pagination module container. |
| Order | number | Controls the display order when the parent container uses Flexbox or Grid layout. |
| Meta | admin label | Set an admin label for identification in the Visual Builder layer panel. Controls builder-only visibility. |

<!-- ![Pagination Content tab settings](../assets/screenshots/modules/pagination/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the visual appearance of navigation link text and overall module styling.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Links Text | typography controls | Font family, weight, style, size, color, letter spacing, line height, and text shadow for the previous and next navigation links. |

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

<!-- ![Pagination Design tab settings](../assets/screenshots/modules/pagination/settings-design.png){ loading=lazy } -->

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

<!-- ![Pagination Advanced tab settings](../assets/screenshots/modules/pagination/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the pagination container as a flexbox row */
.et_pb_pagination {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
    border-top: 1px solid #eeeeee;
    margin-top: 40px;
}

/* Style navigation links as pill buttons */
.et_pb_pagination a {
    display: inline-block;
    padding: 10px 24px;
    background: #f4f4f4;
    border-radius: 24px;
    color: #333333;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
}

.et_pb_pagination a:hover {
    background: #2ea3f2;
    color: #ffffff;
}

/* Add directional arrows before/after link text */
.et_pb_pagination .et_pb_prev::before {
    content: '\2190 ';
}

.et_pb_pagination .et_pb_next::after {
    content: ' \2192';
}

/* Responsive stacking */
@media (max-width: 767px) {
    .et_pb_pagination {
        flex-direction: column;
        gap: 12px;
    }
}
```

### PHP Hooks

```php
/* Filter the Pagination module output to add ARIA labels */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_pagination' !== $render_slug) {
        return $output;
    }
    $output = str_replace(
        'class="et_pb_pagination',
        'role="navigation" aria-label="Post navigation" class="et_pb_pagination',
        $output
    );
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Minimal Post Footer Navigation** — Place the Pagination module in the last row of a single post template. Set Navigation to "Both" and use short labels like "Previous" and "Next." Add a top border via the module's Border settings to visually separate the navigation from the post content above.

2. **Category-Restricted Article Flow** — Enable same-category navigation in the Categories setting so readers stay within the topic they are currently reading. This is especially effective for tutorial series, news categories, or product lines where sequential browsing within a topic improves the user experience.

3. **Loop-Powered Archive Pagination** — On a blog archive or custom post type listing template, connect the Pagination module to a looped section that displays posts in a grid. The pagination controls handle page transitions for the loop, loading the next set of posts without requiring a separate archive navigation system.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/pagination` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| (Minimal) | Inherits from WP query context | Pagination behavior derived from the active WordPress query |

!!! tip "Module Selection Guidance"
    For post list pagination use Pagination with Blog or Portfolio modules; for prev/next post links use Post Navigation.

## Saving Your Work

After configuring the Pagination module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Pagination Links Not Appearing"
    If the module renders but no links are visible:

    - In Main Query mode, pagination only works on single post or page views. It does not generate links on static homepage layouts or non-singular contexts.
    - Verify that other published posts exist in the same category (if category filtering is enabled) or in the overall post type.
    - Check the Navigation setting to ensure you have not restricted it to only "Previous" or only "Next" when both are expected.

!!! warning "Looped Element Pagination Not Working"
    If the module does not paginate loop builder content:

    - Confirm that the Target is set to **Looped Element** and that the correct section, row, column, or module is selected as the loop target.
    - The loop builder must be properly configured on the target element with a data source that returns multiple pages of results.
    - Test that the loop itself is generating content by checking the target element independently before adding pagination.

!!! tip "Hiding Pagination on First or Last Post"
    When viewing the first post in a sequence, the "Previous" link has no destination. Divi hides the link automatically, but the empty space may affect layout alignment. Use the CSS flexbox pattern from the code examples with `justify-content: space-between` so the remaining link stays anchored to its side of the container.

## Related

- [Blog](blog.md) — Blog post listing module with built-in pagination for archive views
- [Portfolio](portfolio.md) — Portfolio project grid module with filterable categories
- [Post Navigation](post-navigation.md) — Alternative post navigation module for previous/next browsing
