---
title: "How to Display Posts in a Grid Layout on Archive Pages Using Divi 5 Theme Builder"
category: troubleshooting
tags: ["troubleshooting", "theme-builder", "archive", "blog", "grid-layout"]
related: ["blog", "getting-started-with-divi-5-theme-builder", "advanced-content-management-using-dynamic-content-in-divi-5"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14085456-how-to-display-posts-in-a-grid-layout-on-archive-pages-using-divi-5-theme-builder"
---

# How to Display Posts in a Grid Layout on Archive Pages Using Divi 5 Theme Builder

Display blog posts in a responsive grid layout across your archive pages using the Divi 5 Theme Builder and Blog module.

## Overview

Archive pages (category, tag, author, date archives) often benefit from a clean grid layout that showcases multiple posts at once. Divi 5's Theme Builder allows you to create a custom archive template that displays posts in a grid, complete with featured images, titles, excerpts, and metadata. By using the Blog module with the dynamic content system, you can ensure that archive pages automatically pull and display the correct posts for each archive type.

This approach gives you full control over the layout, spacing, and styling while maintaining a consistent experience across all archive pages on your site.

## Steps

### 1. Create an Archive Template

1. Log in to the WordPress dashboard
2. Navigate to **Divi → Theme Builder**
3. Click the **Add New Template** button
4. Select **All Archive Pages** as the template type
5. Name your template (e.g., "Blog Archive Grid")
6. Click **Create Template**

The Divi Visual Builder will open.

### 2. Add a Heading Section

1. In the Visual Builder, add a new **Section** at the top
2. Add a **Heading module** to the section
3. In the Heading module's **Content Tab**, click the **Dynamic Content** icon (lightning bolt)
4. Select **Post/Archive Title** from the dropdown list
5. This will automatically display the correct title for each archive type (e.g., "Category: Web Design")

### 3. Add the Blog Module

1. In a new section below, add a **Blog module**
2. In the Blog module's **Content Tab**, enable the option **Posts For Current Page**
3. This ensures the module displays the posts that belong to the current archive page

### 4. Configure the Grid Layout

1. In the Blog module's **Design Tab**, set the following:
   - **Columns**: Set to 2 or 3 columns depending on your site width
   - **Post Count**: Choose how many posts to display per page (e.g., 12)
   - **Pagination**: Enable pagination if you want users to browse additional pages
2. Adjust spacing, shadows, and hover effects to match your design

### 5. Customize Post Display

1. In the Blog module's **Content Tab**:
   - Enable **Featured Image** to show post images
   - Enable **Title** for post titles
   - Enable **Excerpt** to show post descriptions
   - Enable **Meta** to display author, date, and category information
2. Adjust **Excerpt Length** to control how much post text is visible

### 6. Save Your Template

1. Click the **Save** button (top right) to save all changes by expanding the Visual Builder's settings and pressing **CTRL+S** (Windows/Linux) or **CMD+S** (Mac)
2. Click the **Exit** button in the top right to exit the Visual Builder
3. Click **Save Changes** in the Theme Builder interface to finalize the template

Your archive pages will now display posts in a grid layout.

## Troubleshooting

**Posts are not showing on archive pages:**
- Verify that you selected **All Archive Pages** as the template type when creating the template
- Ensure the Blog module has **Posts For Current Page** enabled in the Content Tab
- Check that your site has published posts in the relevant categories, tags, or dates

**Grid layout appears broken:**
- Check the number of columns you set for the Blog module—very high column counts on narrow screens can cause layout issues
- Verify your theme's container width settings in Theme Customizer
- Use the responsive design tools (mobile/tablet preview) to test on different screen sizes

**Pagination not working:**
- Confirm that pagination is enabled in the Blog module's Content Tab
- Check that you've set a reasonable post count per page (not showing all posts at once)
- Ensure there are enough posts on your site to create multiple pages

**Dynamic content (title) shows placeholder text:**
- Make sure you clicked the **Dynamic Content** icon (lightning bolt) and selected **Post/Archive Title**
- Verify the template type is set to archive pages
- Check that you're viewing the archive page on the front end, not editing in the builder

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Archive templates and dynamic content workflows differ significantly in earlier Divi versions.

## Related

- [Blog Module](../modules/blog.md)
- [Getting Started with Theme Builder](../builder/getting-started-with-divi-5-theme-builder.md)
- [Dynamic Content in Divi 5](../builder/advanced-content-management-using-dynamic-content-in-divi-5.md)
- [Theme Builder Templates](../builder/building-templates-for-your-website-with-theme-builder-in-divi-5.md)
