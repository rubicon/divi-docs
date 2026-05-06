---
title: "Build Custom Loops Using Loop Builder in Divi 5"
category: builder
tags: ["builder", "loop-builder", "dynamic-content", "posts", "custom-fields", "pagination", "query"]
related: ["advanced-content-management-using-dynamic-content-in-divi-5", "build-custom-templates-using-the-theme-builder-in-divi-5", "use-global-variables-with-dynamic-content"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/13644757-build-custom-loops-using-loop-builder-in-divi-5"
---

# Build Custom Loops Using Loop Builder in Divi 5

The Loop Builder in Divi 5 lets you create dynamic, repeating content blocks powered by WordPress queries. Instead of manually duplicating module layouts, you define a loop container, set query rules (what posts to fetch, how many, in what order), and populate it with dynamic content fields. Divi repeats your design for every matching item.

!!! abstract "Quick Reference"
    **What it does:** Repeats a template design for multiple items (posts, terms, users, custom fields); replaces manual duplication with database-driven content.
    
    **Query types:** Posts (default), Terms, Users, Comments, Custom Data
    
    **Data sources:** Blog posts, custom post types, product listings, team members, testimonials, custom field values
    
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/13644757-build-custom-loops-using-loop-builder-in-divi-5)

## Overview

Loop Builder transforms static designs into dynamic content feeds. Instead of hardcoding ten product cards or testimonials, you create one card template and tell Divi to repeat it for every post that matches your query.

The Loop Builder has three core parts:

1. **Loop Container** — the element you turn into a loop (Section, Row, Column, or specific modules like a Card). Divi repeats this element for every item in your query.

2. **Loop Query** — the rules that define which items show (post type, category, order, count, filters, meta queries, etc.).

3. **Dynamic Content** — special "Loop" fields that pull the correct data into each repeated card: Loop Featured Image, Loop Post Title, Loop Excerpt, Loop Author, etc.

When combined, these create posts or products feeds, team rosters, case study galleries, customer testimonial carousels, and more—all pulling live data from your WordPress database.

![Loop Builder example](../assets/screenshots/builder/loop-builder/overview.png){ loading=lazy }
*A single row template repeated for six blog posts, each with its own featured image, title, and excerpt.*

## Loop Query Basics

### Supported Data Sources

| Source | Query Type | Common Use |
|--------|-----------|-----------|
| **Posts** | Blog posts, pages, custom post types | Blog feeds, case studies, portfolios |
| **Terms** | Categories, tags, taxonomies | Category listings, skill tags |
| **Users** | WordPress users | Team rosters, author listings |
| **Comments** | Post comments | Comment threads, testimonials |
| **Custom Data** | Advanced custom fields, repeater fields | Flexible data sources |

### Query Settings

When you enable the loop on a container, you define:

| Setting | Description |
|---------|-------------|
| **Loop Element** | Choose which element to repeat (column, section, or module). |
| **Query Type** | Select the data source: Posts (default), Terms, Users, Comments, or Custom. |
| **Post Type** | If querying posts, choose Posts, Pages, or custom post types (Products, Events, etc.). |
| **Posts Per Page** | Number of items to display per page (e.g., 6, 9, 12). Set to finite number for pagination. |
| **Order By** | Sort items by publish date (default), title, menu order, comment count, custom fields, etc. |
| **Order** | Direction: Ascending (oldest first) or Descending (newest first). |
| **Post Offset** | Skip N items (useful for showing different sets of posts on different pages/templates). |
| **Include Posts with Specific Term** | Filter to show only posts from certain categories, tags, or custom taxonomy terms. |
| **Include by Custom Field Value** | Filter by custom field (Meta Query): show only posts where a custom field equals a specific value. |

## Building a Loop

### Step 1: Choose Your Container

Select the element to repeat. Common choices:

- **Column:** for card-based layouts (products, testimonials, team members)
- **Row:** for complex repeating sections (featured articles with alternating images)
- **Section:** for full-width repeating blocks (customer case studies)

### Step 2: Enable Loop

Open the container's settings → **Content tab** → find the **Loop** option group.

Toggle **Loop Element** to ON.

### Step 3: Configure Query

Set the query rules:

```
Query Type: Posts (default)
Post Type: Posts (or your custom post type)
Posts Per Page: 6
Order By: Publish Date
Order: Descending (newest first)
Include Posts with Specific Term: Blog (category)
```

### Step 4: Build the Card Template

Inside the loop container, build your repeating design:

- Add an **Image module** for the featured image
- Add a **Heading module** for the post title
- Add a **Text module** for author / date info
- Add another **Text module** for the excerpt
- Add a **Button module** for a "Read More" link

Keep layouts simple: each element inside the loop repeats for every item.

### Step 5: Populate with Dynamic Content

For each module inside the loop, connect it to the correct dynamic field:

| Module | Dynamic Field |
|--------|---------------|
| **Image** | Loop Featured Image |
| **Heading** | Loop Post Title |
| **Text (meta)** | Loop Author, Loop Post Date, Loop Post Category |
| **Text (excerpt)** | Loop Excerpt (set word count if needed) |
| **Button** | Loop Link or Post URL (links the button to the post) |

To add dynamic content: hover over the field → click the **Dynamic Content icon** → select the **Loop** field.

### Step 6: (Optional) Add Pagination

If you want to split results into multiple pages:

1. Add a **Pagination module** *outside* your loop container.
2. Open the Pagination settings → **Content tab** → **Target Loop**
3. Select the loop column/row you created
4. The pagination will control which page of results shows

**Important:** Your loop query must have **Posts Per Page** set to a finite number (not "All"). Otherwise, pagination has nothing to split.

## Dynamic Content Reference

These fields are available inside any loop container:

### Post-Specific Fields

| Field | Returns |
|-------|---------|
| Loop Post Title | The post's title |
| Loop Post Excerpt | The post's excerpt (you can set word count and "Read more" text) |
| Loop Post Content | The full post content |
| Loop Featured Image | The post's featured image; hover the image field → Dynamic Content → Loop Featured Image |
| Loop Post Date | Publication date (format: date settings from WordPress) |
| Loop Author | The post author's display name |
| Loop Post URL / Loop Link | The permalink to the post; use this to link buttons or the whole card |
| Loop Post Category | Primary category name |
| Loop Post Tags | Comma-separated list of post tags |

### Custom Field Values

If your posts have custom fields (ACF, Metabox, etc.):

- Use the **Dynamic Content icon** and search for the field name
- The field will auto-populate with the current loop item's value

### Meta Information

| Field | Returns |
|-------|---------|
| Loop Post ID | The post's ID (useful for custom queries or CSS targeting) |
| Loop Post Type | The post's type (post, page, product, etc.) |
| Loop Post Status | Current status (published, draft, etc.) |

## Common Patterns

### Blog Feed with Pagination

```
Section
  └─ Row
      └─ Column (Loop Container)
          ├─ Image module (Dynamic Content: Loop Featured Image)
          ├─ Heading module (Dynamic Content: Loop Post Title)
          ├─ Text module (Dynamic Content: Loop Excerpt)
          └─ Button module (Link to: Loop Link)

Pagination Module (outside loop)
  └─ Target: Column (loop container above)
```

### Product Grid (E-commerce)

```
Section
  └─ Row
      └─ Column (Loop Container, Query: Products, Posts Per Page: 9)
          ├─ Image module (Loop Featured Image)
          ├─ Heading module (Loop Product Title)
          ├─ Text module (Loop Product Price via custom field)
          └─ Button module (Add to Cart, linked to Loop Link)
```

### Team Roster with Alternating Images

```
Section
  └─ Row (Layout: Grid or Flex)
      ├─ Column (Loop Container, Query: Posts with category="Team")
      │   ├─ Image module (Loop Featured Image)
      │   ├─ Heading module (Loop Post Title)
      │   └─ Text module (Loop Post Excerpt)
      │
      ... (repeats for each team member)
```

### Testimonials with Author Meta

```
Section
  └─ Row
      └─ Column (Loop Container, Query: Posts with category="Testimonials")
          ├─ Text module (Loop Post Excerpt)
          ├─ Text module (Loop Author + Loop Post Date: "By [author] on [date]")
          └─ Image module (Loop Featured Image - author photo)
```

## Performance Optimization

When building loops, follow these guidelines:

| Practice | Benefit |
|----------|---------|
| **Use Posts Per Page:** Limit items shown at once (e.g., 6, 9, 12) | Faster page load; easier pagination |
| **Filter by category/term:** Show only relevant posts | Reduce query complexity |
| **Use Meta Queries judiciously:** Filter by custom field only if necessary | Large meta queries can slow queries |
| **Avoid nested loops:** Don't loop inside a loop | Exponential query complexity |
| **Cache dynamic content:** Use Divi's caching for frequently queried loops | Reduces database hits |
| **Order by publish date, not by custom field:** Default ordering is faster | Custom field ordering requires extra database work |

## Conditional Display in Loops

You can show/hide modules inside a loop based on field values:

1. Open the module settings → **Advanced tab** → **Conditions**
2. Set a condition like "Show if Loop Post Category equals News"
3. The module will only render for matching items

## Troubleshooting

**No items showing in the loop:**
- Verify the query settings: is the Post Type correct? Does the category/term exist?
- Check if "Include Posts with Specific Term" is filtering too aggressively.
- Verify the Post Type/Posts Per Page are set to finite values (not blank or 0).
- Check console for PHP errors (may indicate query failure).

**Wrong data in dynamic fields:**
- Ensure you've selected the correct Dynamic Content field (e.g., Loop Post Title, not Loop Post Author).
- For custom fields, verify the field name matches exactly (case-sensitive in some systems).
- Check if the custom field value is empty for some items.

**Loop container too wide or too narrow:**
- Verify the parent row's column structure.
- Check if the loop element's sizing (via Column settings) is constraining width.
- Inspect CSS for conflicting width rules.

**Pagination not working:**
- Ensure the Pagination module's **Target** is set to the correct loop container.
- Verify loop query has **Posts Per Page** set to a finite number (not "All" or blank).
- Check if CSS or custom layout is hiding pagination buttons.

**Performance issues (slow page load):**
- Reduce Posts Per Page (fewer items per load).
- Use post offset to paginate results.
- Add category/term filters to reduce query scope.
- Check database for missing indexes on custom field columns (if using Meta Query heavily).

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 Loop Builder behavior exclusively. Divi 4 did not have loop builder; instead, content was often duplicated manually.

## Elegant Themes Tutorials

- [Using the Loop Builder (Elegant Themes Blog)](https://www.elegantthemes.com) — Official walkthrough with video

## Related

- [Advanced Content Management Using Dynamic Content in Divi 5](../builder/advanced-content-management-using-dynamic-content-in-divi-5.md) — Full dynamic content field reference
- [Build Custom Templates Using the Theme Builder in Divi 5](../builder/build-custom-templates-using-the-theme-builder-in-divi-5.md) — Use loops in templates (archive pages, single post pages)
- [Use Global Variables with Dynamic Content](../builder/global-variables.md) — Combine loops with global variables
