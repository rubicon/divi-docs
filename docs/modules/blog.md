---
title: "Blog Module"
category: modules
tags: [blog, content-modules, posts, grid, list]
related: [text, blurb]
divi_version: "5.x"
last_updated: 2026-03-12
---

# Blog Module

The Blog module displays WordPress posts in either a grid or fullwidth (list) layout, with controls for filtering by category, limiting post count, and toggling meta elements.

## Overview

The Blog module is Divi's primary way to display dynamic post content. It queries your WordPress posts and renders them with featured images, excerpts, meta information, and read-more links. It supports two layout modes — a masonry-style grid and a traditional fullwidth list — and includes built-in pagination.

This module is commonly used on blog index pages, homepage "latest posts" sections, and category landing pages.

## Settings & Options

### Content Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Post Count | number | 10 | Number of posts to display |
| Include Categories | multi-select | All | Filter posts by category |
| Date Format | text | `M j, Y` | PHP date format string |
| Show Featured Image | toggle | Yes | Display post thumbnails |
| Show Content | select | Show Excerpt | `Show Excerpt` or `Show Content` |
| Excerpt Length | number | 270 | Character count for excerpts |
| Show Author | toggle | Yes | Display post author |
| Show Date | toggle | Yes | Display post date |
| Show Categories | toggle | Yes | Display post categories |
| Show Comments Count | toggle | Yes | Display comment count |
| Show Pagination | toggle | Yes | Display page navigation |
| Offset | number | 0 | Skip this many posts from the beginning |

### Design Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Layout | select | Fullwidth | `Fullwidth` (list) or `Grid` |
| Grid Columns | select | 3 | Number of columns in grid mode (1–4) |
| Overlay | toggle | Off | Show overlay on featured image hover |
| Overlay Color | color | theme accent | Color of the image overlay |
| Masonry | toggle | On | Enable masonry layout in grid mode |
| Title Font | typography | default | Post title typography |
| Body Font | typography | default | Excerpt typography |
| Meta Font | typography | default | Author, date, category typography |
| Read More Font | typography | default | Read more link typography |

## Code Examples

### Custom blog grid styling

```css
/* Card-style blog grid */
.et_pb_blog_grid .et_pb_post {
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: box-shadow 0.3s ease;
}
.et_pb_blog_grid .et_pb_post:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Add padding to the text portion */
.et_pb_blog_grid .et_pb_post .post-content-inner {
    padding: 1.5rem;
}

/* Style the read more link as a button */
.et_pb_blog_grid .et_pb_post a.more-link {
    display: inline-block;
    padding: 0.5rem 1rem;
    background: #7c3aed;
    color: #ffffff;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.875rem;
}
```

### Filtering blog posts with hooks

```php
/**
 * Exclude a specific category from all Blog modules.
 */
function my_exclude_category_from_blog( $args, $props ) {
    // Category ID to exclude
    $exclude_cat = 42;

    if ( isset( $args['cat'] ) ) {
        $args['category__not_in'] = array( $exclude_cat );
    }

    return $args;
}
add_filter( 'et_pb_blog_query_args', 'my_exclude_category_from_blog', 10, 2 );
```

### Custom excerpt length per module

```php
/**
 * Override excerpt length for Blog modules with a specific CSS class.
 */
function my_custom_excerpt_length( $length ) {
    if ( is_singular() ) {
        return 40; // word count
    }
    return $length;
}
add_filter( 'excerpt_length', 'my_custom_excerpt_length', 999 );
```

## Common Patterns

### Homepage latest posts

A 3-column grid with 3 posts, no pagination, and a "View All Posts" button below. Set Post Count to 3, Layout to Grid, and Show Pagination to No.

### Category landing page

Use Include Categories to filter to a single category. Set layout to Fullwidth for a traditional blog feel, or Grid for a magazine-style layout.

### Related posts section

Place a Blog module at the bottom of single post templates (via Theme Builder). Use the Include Categories setting dynamically or apply a custom query filter to show posts from the same category as the current post.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Blog module in Divi 5 uses updated markup for the grid layout, and the masonry implementation may use CSS Grid instead of JavaScript columns.

## Troubleshooting

!!! warning "Posts not showing"
    If the Blog module displays no posts, check: (1) you have published posts in the selected categories, (2) the Offset value isn't skipping past all available posts, (3) no conflicting query modifications from plugins.

!!! warning "Grid columns uneven"
    When Masonry is enabled, grid items can appear uneven if featured images have varying aspect ratios. Either crop all featured images to the same ratio or disable Masonry for a uniform grid.

!!! warning "Pagination conflicts"
    On static front pages, Blog module pagination can conflict with WordPress's built-in pagination. If page 2 shows the same posts as page 1, add this to your theme's `functions.php`:

    ```php
    function my_fix_blog_pagination( $query ) {
        if ( is_front_page() && $query->is_main_query() ) {
            $query->set( 'paged', get_query_var( 'page' ) );
        }
    }
    add_action( 'pre_get_posts', 'my_fix_blog_pagination' );
    ```

## Related

- [Text Module](text.md) — for static content blocks
- [Blurb Module](blurb.md) — for feature/service highlights
