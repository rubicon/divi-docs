---
title: "Build Custom Templates Using the Theme Builder in Divi 5"
category: builder
tags: [theme-builder, templates, header, footer, custom-templates, assignment]
related: [divi-5-visual-builder-overview, dynamic-content-reference]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/13644980-build-custom-templates-using-the-theme-builder-in-divi-5"
---

# Build Custom Templates Using the Theme Builder in Divi 5

Create and manage custom headers, footers, and page templates for different sections of your site without manually editing each page.

## Overview

The Theme Builder is Divi 5's system for creating reusable page templates that apply to specific page types or conditions. Instead of building a header on every single page, you build it once in the Theme Builder and assign it to all pages—or to specific categories, post types, or custom rules.

The Theme Builder consists of three main parts:

- **Header** — Global or custom headers displayed at the top of pages
- **Body** — The main content area, including post content, custom layouts, and dynamic elements
- **Footer** — Global or custom footers displayed at the bottom of pages

You can create global templates that apply site-wide, or override them with specific templates for posts, pages, product pages, archives, and more. Templates use Dynamic Content (like Post Title, Post Content, Featured Image) so they work for every item they're assigned to, not just one page.

![Theme Builder overview in Divi 5](../assets/screenshots/builder/build-custom-templates/overview.png){ loading=lazy }
*The Theme Builder dashboard showing available templates and assignment controls.*

## Creating Your First Template

### Step 1: Access the Theme Builder

1. Log in to your WordPress dashboard
2. Click **Divi** in the sidebar
3. Click **Theme Builder**

You'll see the **Default Website Template** box with options to add a Global Header, Custom Body, and Global Footer.

### Step 2: Build a Global Header

1. In the **Default Website Template** box, click **Add Global Header**
2. Divi opens the Visual Builder with a blank header template
3. Design your header: add a Section, insert your logo, create a navigation menu, add a CTA button, or include contact information
4. Click **Save** to save your changes
5. Click **Exit** to return to the Theme Builder dashboard

Your Global Header is now assigned to all pages on your site automatically.

### Step 3: Build a Custom Body (Optional)

1. Click **Add Custom Body** in the **Default Website Template** box
2. Click **Build Custom Body**
3. In the Visual Builder, add a Section and Row
4. Insert a **Post Title** module at the top to display the current page/post title dynamically
5. Insert a **Post Content** module where you want the main content to appear
6. Add any additional modules (sidebars, related posts, author boxes, newsletter signups)
7. Click **Save** and **Exit**

A custom body ensures consistent layout across all pages using this template.

### Step 4: Build a Global Footer

1. Click **Add Global Footer** in the **Default Website Template** box
2. Click **Build Global Footer**
3. Design your footer: add links, copyright info, newsletter signup, social media icons, or contact details
4. Click **Save** and **Exit**

Your Global Footer is now assigned to all pages automatically.

## Working with Template Assignments

### Create a Template for Specific Post Types

You can create separate templates for specific categories, post types (Blog Posts, Products), or archives.

1. In the Theme Builder dashboard, click **Add New Template**
2. Choose your target:
   - **All Posts** — applies to every blog post
   - **Posts in Category: [Name]** — applies to posts in a specific category
   - **All Pages** — applies to all pages
   - **All Product Category Pages** (WooCommerce) — applies to product category archives
   - **Specific Product Category Pages** (WooCommerce) — applies only to selected product categories

3. Click **Create Template**
4. Build the template's body using the Visual Builder
5. Add a Post Title and Post Content module for single items, or use the Loop Builder for archives/categories
6. Click **Save** and **Exit**

### Manage Template Assignments

To view or change which pages a template applies to:

1. Right-click on a template in the Theme Builder dashboard
2. Click **Manage Template Assignments**
3. Adjust the page, post, or category rules
4. Click **Save**

### Override Global Header/Footer for Specific Templates

If you've created a Global Header and Global Footer but want a specific template (like "All Posts") to use a different header:

1. In the template, click **Add Custom Header**
2. Click **Build Custom Header**
3. Design the custom header in the Visual Builder
4. Click **Save** and **Exit**

The custom header now applies only to that template, overriding the global one. Repeat the same process for custom footers.

### Disable a Global Header/Footer

If you've created a Global Header or Footer but want to remove it from a specific template:

1. In the template, click the **Eye icon** next to the Global Header/Footer
2. Toggle to hide it, or click **Disable Global** to convert it to a static local header/footer
3. You can now customize the local version without affecting the global one

## Template Options

### Right-Click Template Menu

Right-click on any template to access these options:

| Action | Description |
|--------|-------------|
| **Manage Template Assignments** | Change the page/post/category rules this template applies to |
| **Reset Template Assignments** | Revert all assignments to their defaults |
| **Duplicate Template** | Create a copy of this template (useful as a starting point for variations) |
| **Disable the Template** | Temporarily disable this template without deleting it; assignments are ignored |
| **Delete Template** | Permanently remove this template |
| **Rename Template** | Change the template's display name |
| **Export Template** | Save this template as a JSON file for backup or sharing |

### Import and Export Templates

Click the **Portability icon** (top right) to bulk-export or import templates:

- **Export** — Save all templates or select specific ones to export as a JSON file
- **Import** — Load a JSON file containing one or more templates into your site

This is useful for moving templates between sites, backing up your work, or sharing templates with other Divi users.

## Common Template Patterns

### Single Global Template (Minimal Site)

Use one global template with a consistent header, footer, and content width for the entire site:

- Create a Global Header with logo and main menu
- Create a Global Footer with links and copyright
- All pages use the same basic layout with dynamic content areas

Best for: Small sites, blogs, portfolios with uniform design.

### Blog System with Category Overrides

Create a main "All Posts" template, then override specific categories:

- **All Posts** template with post title, content, author box, and related posts
- **Category: Tutorials** template with a custom layout, sidebar, or tag cloud
- **Category: News** template with a different header or featured section

Best for: Blogs with distinct content types or sections.

### WooCommerce Store

Create separate templates for products and categories:

- **Single Product** template showing product gallery, details, variations, and related products
- **Product Category** template using Loop Builder to display product grids with filters
- **All Product Pages** with a consistent header and footer

Best for: WooCommerce shops with consistent styling across products and archives.

### Marketing Landing Pages

Create custom templates without the standard header and footer:

- **Landing Page Template** with a minimal header (no navigation) and no footer
- **Thank You Page** with a specific CTA and conversion message
- **Download Page** with custom styling and limited navigation

Best for: Conversion-focused pages that need different design from the rest of the site.

### Multi-Section Site

Combine global templates with page-specific overrides:

- Global Header and Footer applied site-wide
- **Blog Body** template for the /blog/ section
- **Support** template for help/documentation pages
- **Team** template for about/team pages

Best for: Larger sites with distinct sections.

## Settings Reference

### Global Header/Footer Settings

| Setting | Type | Description |
|---------|------|-------------|
| **Add Global Header** | Action | Creates a header template applied to all pages using the Default Website Template |
| **Add Global Footer** | Action | Creates a footer template applied to all pages using the Default Website Template |
| **Build Global Header/Footer** | Action | Opens the Visual Builder to design the selected template |
| **Disable Global** | Action | Converts a global header/footer to a local one, allowing template-specific customization |
| **Eye icon** | Toggle | Shows/hides the template part on the front end (editing still allowed) |
| **Pencil icon** | Action | Opens the Visual Builder to edit the selected template part |
| **Trash icon** | Action | Deletes the selected template part |

### Template Assignment Rules

| Assignment Type | Applies To |
|-----------------|-----------|
| **All Posts** | Every blog post on the site |
| **Posts in Category: [Name]** | Blog posts in a specific category |
| **All Pages** | Every page (non-post) on the site |
| **Specific Page** | A single page (identified by ID or slug) |
| **All Product Pages** | All WooCommerce products (requires WooCommerce) |
| **Specific Product** | A single product |
| **All Product Category Pages** | All WooCommerce product category archives |
| **Specific Product Category** | A single product category archive |
| **Archive Pages** | Author, date, or category archive pages |
| **Search Results** | The site's search results page |

## Tips for Success

### Start with a Global Template

Set a global header, body, and footer first, then add more specific templates only when you need them. This saves time and keeps your template collection manageable.

### Name Templates Clearly

Use descriptive names that explain both purpose and scope:
- Good: "Global Template", "All Posts", "Category: Tutorials", "Product: Single"
- Avoid: "Template 1", "Header v2", "Page"

### Keep Assignments Simple

Avoid too many overlapping include/exclude rules at first. Use simple, targeted assignments so you always know why a template is being applied.

### Use Dynamic Content in Body Layouts

In body templates, use Dynamic Content modules (Post Title, Post Content, Featured Image, Author Name, etc.) so templates work for every item in their scope, not just one page.

### Combine with Loop Builder for Archives

Use Loop Builder inside Theme Builder templates for archives and product grids (blog, products, directories), but keep single-item templates simple when you're starting out.

### Test Before Going Live

Before assigning a template to your entire site:
1. Build the template in the Visual Builder
2. Preview the page to see how it looks
3. Test on multiple page types (post, page, product) to ensure dynamic content displays correctly
4. Check mobile responsiveness
5. Then assign it widely

## Troubleshooting

### Template Not Appearing on Front End

**Problem:** You created a template but it's not showing on pages.

**Solution:**
1. Verify the template is not disabled (right-click and check status)
2. Check the assignment rules — click **Manage Template Assignments** to confirm the correct pages are selected
3. Clear your browser cache and WordPress cache (if using a cache plugin)
4. Verify the page/post meets the assignment criteria (correct category, post type, etc.)

### Global Header/Footer Displaying Inconsistently

**Problem:** Your global header appears on some pages but not others.

**Solution:**
1. Check if specific templates have custom headers/footers that override the global one
2. Right-click the template and click **Manage Template Assignments** to review rules
3. Use the **Eye icon** to ensure the global header/footer is visible
4. If using **Disable Global**, you may have converted it to a local version — click **Add Global Header** to restore it

### Dynamic Content Not Showing

**Problem:** Post Title, Post Content, or other dynamic modules appear blank on the front end.

**Solution:**
1. Verify you're using Dynamic Content modules (Post Title, Post Content, Featured Image), not static text
2. Check that the template is assigned to the correct post/page type
3. In the Visual Builder, open the module and verify the dynamic source is set (not hard-coded text)
4. Clear your site's cache
5. Check the browser console (F12 → Console) for JavaScript errors

### Too Many Templates (Site Becoming Slow)

**Problem:** You've created many templates and the Theme Builder is sluggish.

**Solution:**
1. Right-click unused templates and click **Delete Template** to remove them
2. Consolidate similar templates (e.g., combine "Category: News" and "Category: Updates" if they have the same design)
3. Use one global template with dynamic assignments rather than individual templates for every category
4. Use the **Disable the Template** option instead of deleting if you might reuse it

### Can't Find a Template's Assignment Rules

**Problem:** You forget which pages a template is assigned to.

**Solution:**
1. Right-click the template
2. Click **Manage Template Assignments**
3. Review the include/exclude rules
4. You can adjust them here without rebuilding the template

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 Theme Builder behavior exclusively. Divi 4 Theme Builder has different workflows and UI.

## Related

- [Divi 5 Visual Builder Overview](../builder/visual-builder.md)
- [Dynamic Content Reference](../builder/dynamic-content.md)
- [Loop Builder for Archives](../builder/build-custom-loops-using-loop-builder-in-divi-5.md)
- [WordPress Theme Development Basics](../builder/getting-started-with-divi-5-theme-builder.md)
