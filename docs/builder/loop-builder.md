---
title: "Loop Builder"
description: "Divi 5 Loop Builder — display repeating posts, products, terms, users, or ACF repeaters in fully custom layouts with query controls and pagination."
category: builder
tags: ["builder", "loop-builder", "queries", "dynamic-content", "posts", "woocommerce", "acf"]
related: ["dynamic-content", "theme-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11863867"
---

# Loop Builder

Display repeating content from your WordPress database (posts, products, terms, users) in fully customizable layouts controlled by query parameters.

!!! abstract "Quick Reference"
    **What it does:** Transforms any container into a repeating template that iterates over database records (posts, products, terms, users, ACF repeaters).
    **Where to find it:** Any container element's settings → Content Tab → Loop → enable Loop toggle.
    **Key features:**

    - Query types: Posts, Terms, Users, WordPress Menus, ACF Repeater Fields
    - Full query configuration: post type, taxonomy filters, meta queries, ordering, offset
    - Loop-specific dynamic content fields (Loop Post Title, Loop Featured Image, etc.)
    - Separate Pagination module for splitting results across pages

    **ET Docs:** [Loop Builder](https://help.elegantthemes.com/en/articles/11863867){:target="_blank"}

## Overview

The Loop Builder transforms any Divi container element into a repeating template that iterates over a set of database records. You design the layout for a single item, configure a query to select which records to display, and insert dynamic content fields to populate each iteration with the correct data. The result is a fully custom content loop: blog feeds, product grids, team directories, portfolio displays, event listings, and more.

Unlike the pre-built Blog or Portfolio modules, the Loop Builder gives you complete control over the item template. Every module, layout property, and design setting inside the loop container is used as the repeating template for each item in the query results.

For the official Elegant Themes documentation, see [Loop Builder](https://help.elegantthemes.com/en/articles/11863867) and [Loop Builder Deep Dive](https://help.elegantthemes.com/en/articles/13644757).

## Core Components

| Component | Description |
|-----------|-------------|
| Loop Container | The element you convert into a loop (Section, Row, Column, Group, or Module) |
| Loop Item Template | The layout inside the container that repeats for each query result |
| Loop Query | The rules that define which items appear (post type, taxonomy, sort order, count, meta filters) |
| Dynamic Content Fields | Loop-specific fields that resolve to each item's data (title, image, excerpt, price, etc.) |
| Pagination Module | An optional separate module placed outside the loop container to split results across pages |

## Enabling the Loop

1. Select any container element (Section, Row, Column, Group, or individual module).
2. Open the element's settings.
3. Navigate to **Content Tab > Loop**.
4. Enable the **Loop** toggle.
5. Configure the query settings.

Once enabled, every child element inside the container becomes part of the repeating template.

## Query Settings

### Query Type

| Query Type | Description |
|------------|-------------|
| Posts | Query blog posts, pages, custom post types, or WooCommerce products |
| Terms | Query categories, tags, or custom taxonomy terms |
| Users | Query WordPress users (authors, contributors, team members) |
| WordPress Menus | Query published navigation menus |
| ACF Repeater Fields | Query rows from ACF Repeater field data |

### Post Query Configuration

When the query type is set to Posts, the following settings are available:

| Setting | Type | Description |
|---------|------|-------------|
| Post Type | Dropdown | Select which post type to query (Posts, Pages, Products, Projects, custom post types) |
| Posts Per Page | Number input | How many items to display per page. Required for pagination to work. |
| Order By | Dropdown | Sort criteria: Publish Date, Title, Menu Order, Modified Date, Random, or custom field |
| Order | Toggle | Ascending or Descending sort direction |
| Post Offset | Number input | Skip the first N items. Useful for creating secondary loops that pick up where a primary loop left off. |
| Include Posts With Specific Term | Multi-select | Filter to only show posts in selected categories, tags, or taxonomy terms |
| Exclude Posts With Specific Term | Multi-select | Remove posts in selected categories, tags, or taxonomy terms from results |
| Include Specific Posts | Multi-select | Show only specified posts by name or ID |
| Exclude Specific Posts | Multi-select | Remove specified posts from results |

### Meta Query

Meta queries let you filter results based on custom field values stored in the `wp_postmeta` table:

| Setting | Type | Description |
|---------|------|-------------|
| Meta Key | Text input | The post meta key to filter on |
| Meta Value | Text input | The value to compare against |
| Compare | Dropdown | Comparison operator (equals, not equals, greater than, less than, LIKE, etc.) |
| Type | Dropdown | Data type for comparison (string, number, date, time) |

Multiple meta queries can be combined for complex filtering scenarios.

## Loop-Specific Dynamic Content Fields

When working inside a loop container, the dynamic content picker offers loop-specific sources that resolve to each item's data:

| Field | Description |
|-------|-------------|
| Loop Featured Image | The featured image of the current loop item |
| Loop Post Title | The title of the current loop item |
| Loop Excerpt | The excerpt of the current loop item |
| Loop Product Price | The WooCommerce price of the current product (product loops only) |
| Loop Author | The author of the current loop item |
| Loop Post Date | The publish date of the current loop item |
| Loop Link | The permalink of the current loop item |
| Post URL | The URL of the current loop item (for link fields) |

These fields are distinct from the standard dynamic content sources and are specifically designed to resolve within the loop context.

## Layout Configuration

The loop container and its children control the visual layout:

| Element | Recommended Settings | Purpose |
|---------|---------------------|---------|
| Row (loop container) | Layout Wrapping: **Wrap** | Enables grid-like display where items flow to new lines |
| Column (inside loop) | Column Class: **1/3** or desired fraction | Controls item width; responsive per breakpoint |
| Module Group | Flex Direction: **Column** | Stacks inner modules vertically within each item |

### Creating a Grid Layout

1. Use a Row as the loop container.
2. Set Layout Wrapping to **Wrap** on the Row.
3. Place a single Column inside the Row.
4. Set the Column Class to your desired grid fraction (e.g., 1/3 for a three-column grid).
5. Design the column content as your item template.
6. The loop duplicates the column for each query result, wrapping to new rows as needed.

## Pagination

Pagination is handled by a separate **Pagination** module placed outside the loop container:

1. Add a Pagination module below (or above) the looped element.
2. In the Pagination module settings, select the **Target Loop** (the looped element identified by its Admin Label).
3. The Pagination module automatically generates page navigation based on the loop's Posts Per Page and total result count.

!!! tip "Admin Labels"
    Assign descriptive Admin Labels to loop containers, especially when a page has multiple loops. The Pagination module uses the Admin Label to identify which loop it controls.

## Common Use Cases

### Custom Blog Feed

Loop a Row over Posts, insert a Column with an Image module (Loop Featured Image), Heading module (Loop Post Title), Text module (Loop Excerpt), and Button module (Loop Link). Set Column Class to 1/3 for a three-column grid.

### WooCommerce Product Grid

Loop a Row over Products, use loop-specific fields for product title, price, and featured image. Add filtering with taxonomy terms for product categories.

### Team Directory

Loop over Users query type. Use dynamic content for user display name, bio, and avatar. Arrange in a grid with Column Class settings.

### Portfolio with Custom Filtering

Loop over a custom post type (Projects). Use meta queries to filter by project category or status. Combine with taxonomy term filtering for faceted results.

## Best Practices

- Use **Admin Labels** on all loop containers for clear identification in Pagination and Layers View.
- Insert **Dynamic Content** for all variable data inside loop templates; avoid hardcoding text that should change per item.
- Control query size with **Posts Per Page** and **Offset** settings to manage performance.
- Keep static elements (section headings, CTAs, introductory text) outside the loop container.
- Position the **Pagination** module outside the loop container, not inside it.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    The loop configuration is stored as attributes on the loop container block in `post_content`. The query parameters (post type, taxonomy filters, meta queries, ordering, pagination) are stored in the block's `attrs`. The loop item template is the container's `innerBlocks` content, which gets repeated at render time for each query result. The template itself is stored once; repetition happens during server-side rendering.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Parse the loop container block's `attrs` for query configuration keys (post_type, posts_per_page, meta_query, etc.) | Needs Testing | The innerBlocks define the template layout; the attrs define the query |
| Modify | Update query parameters in the block's `attrs` (e.g., change post_type, adjust posts_per_page, add taxonomy filters) | Needs Testing | Modifying the template layout requires editing the innerBlocks structure |
| Create | Add a loop-enabled block to `post_content` with appropriate query attrs and template innerBlocks | Needs Testing | Must include both the loop query configuration in attrs and a valid template structure in innerBlocks |

!!! warning "Template vs. Query Data"
    The loop container stores the **template** (how to display each item) in its `innerBlocks` and the **query** (which items to display) in its `attrs`. These are independent: changing the query does not affect the template layout, and vice versa. Dynamic content tokens inside the template resolve at render time based on the current loop item.

## Troubleshooting

!!! warning "Loop Shows No Items"
    Verify that the query settings match existing content. Check that the selected post type has published posts, taxonomy filters are not excluding all results, and meta query values match actual post meta data.

!!! warning "Pagination Not Working"
    Ensure the Pagination module is placed **outside** the loop container and its Target Loop setting references the correct Admin Label. Also verify that Posts Per Page is set to a finite number (not "all").

!!! warning "Dynamic Content Showing Same Data for All Items"
    If all loop items display the same content, you may be using standard dynamic content sources instead of loop-specific sources. Use the **Loop Featured Image**, **Loop Post Title**, etc. fields rather than the generic post title/image fields.

## Related

- [Dynamic Content](dynamic-content.md)
- [Theme Builder](theme-builder.md)
- [Blog Module](../modules/blog.md)
- [Portfolio Module](../modules/portfolio.md)
- [Pagination Module](../modules/pagination.md)
- [Flexbox Layout](flexbox.md) — Control loop item layout direction and alignment
- [CSS Grid](css-grid.md) — Arrange loop items in precise grid layouts
