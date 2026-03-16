---
title: "Theme Builder"
description: "Divi 5 Theme Builder — design custom headers, footers, post templates, and archive layouts with dynamic content and flexible template assignments."
category: builder
tags: [builder, theme-builder, templates, headers, footers, dynamic-content]
related: [visual-builder, library, global-elements]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: ""
---

# Theme Builder

The Divi Theme Builder is a template system that lets you design custom headers, footers, body layouts, and post templates using the Visual Builder.

!!! abstract "Quick Reference"
    **What it does:** Lets you design custom headers, footers, and body templates for any page, post type, archive, or taxonomy.
    **Where to find it:** WordPress admin → Divi → Theme Builder.
    **Key features:**

    - Three template areas: Header, Body, Footer (each optional)
    - Assign templates globally, by post type, category, tag, or specific page
    - Dynamic content fields for post title, featured image, author, date, and custom fields
    - Import/export templates as JSON for cross-site portability

    **ET Docs:** N/A

## Overview

The Theme Builder extends Divi's Visual Builder beyond individual pages to control the overall structure of your entire website. Instead of relying on a fixed theme layout, you can design every part of your site -- headers, footers, blog post templates, product pages, category archives, 404 pages, and more -- using the same drag-and-drop interface you use for page design.

Templates created in the Theme Builder are applied globally or to specific pages, posts, categories, or custom post types. This means you can have one header for your homepage and a different header for your blog, or a unique product page template for WooCommerce.

The Theme Builder uses [dynamic content](dynamic-content.md) to pull in data like post titles, featured images, author information, and more, so your templates automatically populate with the correct content for each page they are applied to.

<!-- ![Theme Builder overview](../assets/screenshots/builder/theme-builder/overview.png){ loading=lazy }
*The Theme Builder interface showing template assignments and header/footer/body areas.* -->

## Accessing the Theme Builder

1. In the WordPress admin, navigate to **Divi > Theme Builder**
2. The Theme Builder dashboard displays all your templates and their assignments
3. Click on any template area (Header, Body, Footer) to open it in the Visual Builder for editing

## Template Structure

Each Theme Builder template consists of up to three areas:

| Area | Purpose | Description |
|------|---------|-------------|
| **Header** | Site header | Appears at the top of every page the template is assigned to. Typically contains the logo, navigation menu, and top bar. |
| **Body** | Page content | The main content area. For post templates, this is where dynamic post content is displayed. For archive templates, this is where the post list appears. |
| **Footer** | Site footer | Appears at the bottom of every page the template is assigned to. Typically contains copyright info, links, contact details, and secondary navigation. |

Each area is optional. You can create a template with only a custom header, only a custom footer, or any combination.

<!-- ![Template structure](../assets/screenshots/builder/theme-builder/template-structure.png){ loading=lazy }
*A Theme Builder template showing the three template areas: Header, Body, and Footer.* -->

## Template Types

### Default Website Template

The Default Website Template applies to all pages on your site unless overridden by a more specific template. This is where you set your site-wide header and footer.

### Specific Templates

You can create templates that target specific content:

| Assignment Type | Examples |
|----------------|----------|
| **All Pages** | Every static page on the site |
| **All Posts** | Every blog post |
| **Specific Page/Post** | A single named page or post |
| **Category Archives** | All posts in a specific category |
| **Tag Archives** | All posts with a specific tag |
| **Author Archives** | Posts by a specific author |
| **Search Results** | The search results page |
| **404 Page** | The "page not found" error page |
| **WooCommerce Products** | Product pages, shop page, cart, checkout |
| **Custom Post Types** | Any registered custom post type |

### Template Priority

When multiple templates could apply to a page, Divi uses specificity to determine which template wins:

1. **Specific page/post assignment** (highest priority)
2. **Category/tag/taxonomy assignment**
3. **Post type assignment** (All Posts, All Pages)
4. **Default Website Template** (lowest priority)

## Creating a Template

### Creating a New Template

1. Navigate to **Divi > Theme Builder**
2. Click **Add New Template**
3. Choose what content this template should apply to (assignment)
4. Click **Create Template**
5. The template appears in the dashboard with empty Header, Body, and Footer areas

### Designing a Template Area

1. Click on the template area you want to design (e.g., **Add Custom Header**)
2. Choose to **Build Custom Header** (or Body/Footer)
3. The Visual Builder opens with the template area ready to edit
4. Design the template using sections, rows, and modules just like a regular page
5. Use Dynamic Content modules to pull in post-specific data
6. Save the template and return to the Theme Builder dashboard

### Assigning Templates

1. In the Theme Builder dashboard, click the gear icon on a template
2. Select **Template Settings**
3. Use the assignment options to choose where this template applies
4. You can include or exclude specific pages, posts, categories, etc.

!!! tip "Template Assignment Conflicts"
    If two templates are assigned to the same page, Divi will notify you of the conflict. The more specific assignment takes priority.

## Dynamic Content

Dynamic content is essential for Theme Builder templates. It allows template elements to pull in page-specific data automatically.

### Common Dynamic Content Fields

| Field | Description | Use Case |
|-------|-------------|----------|
| **Post/Page Title** | The title of the current post or page | Header areas, body templates |
| **Post Content** | The full content of the post | Blog post body templates |
| **Featured Image** | The post's featured image | Post headers, archive listings |
| **Post Excerpt** | The post excerpt | Archive/category page listings |
| **Author Name** | The post author's display name | Blog post bylines |
| **Post Date** | The publication date | Blog post metadata |
| **Post Categories** | Assigned categories | Blog post metadata |
| **Post Tags** | Assigned tags | Blog post metadata |
| **Site Title** | The WordPress site title | Headers |
| **Site Tagline** | The WordPress site tagline | Headers |
| **Site Logo** | The logo set in Divi Theme Options | Headers |
| **Custom Fields** | Any custom field / ACF field | Advanced templates |

### Using Dynamic Content

1. Add a module to your template (e.g., a Text module)
2. Click on the dynamic content icon (database icon) next to supported fields
3. Select the dynamic content source from the dropdown
4. The module will display placeholder content in the builder and real content on the front end

## Global vs. Specific Templates

| Aspect | Global (Default) Template | Specific Template |
|--------|--------------------------|-------------------|
| **Scope** | Applies to all pages by default | Applies only to assigned pages/posts |
| **Typical use** | Site-wide header and footer | Custom blog post layout, special landing page header |
| **Override behavior** | Overridden by any specific template | Overrides the global template for its assigned pages |
| **Number allowed** | One | Unlimited |

## Importing and Exporting Templates

Templates can be exported and imported between Divi websites:

1. In the Theme Builder dashboard, click the portability icon (two arrows)
2. Choose **Export** to download templates as a JSON file
3. On another site, use **Import** to upload the JSON file
4. All template designs and assignments are transferred

!!! warning "Dynamic Content After Import"
    After importing templates, verify that dynamic content fields are correctly mapped. Category assignments and custom fields may need to be reconfigured if the target site has different content.

## Code Examples

### Custom CSS for Theme Builder Header

```css
/* Target the Theme Builder header area */
.et-l--header {
    position: sticky;
    top: 0;
    z-index: 999;
    transition: background-color 0.3s ease;
}

/* Transparent header that becomes solid on scroll */
.et-l--header.et-fixed-header {
    background-color: #ffffff;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
```

### Custom CSS for Theme Builder Footer

```css
/* Target the Theme Builder footer area */
.et-l--footer {
    background-color: #1a1a2e;
    color: #ffffff;
}

.et-l--footer a {
    color: #e2e2e2;
    transition: color 0.2s ease;
}

.et-l--footer a:hover {
    color: #7c4dff;
}
```

### Custom Body Template Styling

```css
/* Style the body template area for blog posts */
.et-l--body .post-meta {
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
    font-size: 14px;
    color: #666;
}
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Theme Builder in Divi 5 features an improved interface and expanded template assignment options compared to earlier versions.

## Troubleshooting

!!! warning "Template Not Applying"
    If a template is not appearing on the expected pages:

    1. Check the template assignment in the Theme Builder dashboard
    2. Verify there is no conflicting template with a more specific assignment
    3. Clear any caching plugins (page cache, object cache)
    4. Check that the template areas (header, body, footer) are actually designed and not empty

!!! warning "Dynamic Content Showing Placeholder Text"
    If dynamic content fields display placeholder text or are empty on the front end:

    1. Verify the content exists on the page/post (e.g., the post has a featured image)
    2. Check that the correct dynamic content field is selected
    3. Ensure the template is assigned to a content type that supports the field

!!! warning "Header Not Sticky"
    If you want a sticky header but it scrolls away:

    1. In the header section's Advanced tab, enable **Position > Sticky**
    2. Set the sticky position to **Top**
    3. Adjust the z-index if the header appears behind other content

## Related

- [Visual Builder](visual-builder.md) -- The front-end editor used to design templates
- [Divi Library](library.md) -- Save and reuse template designs
- [Global Elements](global-elements.md) -- Elements that sync across all pages
- [Presets](presets.md) -- Consistent styling across template elements
- [Dynamic Content](dynamic-content.md) -- Pull post data dynamically into template elements
- [Loop Builder](loop-builder.md) -- Build custom post loops within theme templates
- [Playbook: Theme Builder Ops](../playbooks/theme-builder-ops.md) -- LLM playbook for theme builder automation
