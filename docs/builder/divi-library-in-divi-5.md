---
title: "Divi Library in Divi 5"
category: builder
tags: ["builder", "library", "layouts", "templates", "presets"]
related: ["create-a-new-website-using-a-pre-made-starter-site.md", "element-presets.md", "divi-builder-basics.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/13616078-divi-library-in-divi-5"
---

# Divi Library in Divi 5

Save and reuse sections, rows, modules, and entire page layouts in the Divi Library—a central storage system for all your design components.

## Overview

The Divi Library is a powerful time-saving feature that lets you create once and use many times. Instead of rebuilding the same header, pricing section, or testimonial block across multiple pages, you save it to the library and insert it wherever needed. The library also supports global elements, which automatically update across all pages when edited. You can organize library items with custom categories and tags, and easily import or export your library for backup or sharing with team members.

The Divi 5 Library is accessible from the WordPress dashboard and integrates seamlessly with the Visual Builder, making it simple to maintain a consistent design system across your entire site.

![Divi Library Overview](../assets/screenshots/builder/divi-library-in-divi-5/overview.png){ loading=lazy }
*The Divi Library dashboard provides a centralized location to manage all saved layouts, sections, rows, and modules.*

## Saving Items to the Library

### Save from the Visual Builder

1. Open any page in the Divi Visual Builder
2. Select the **Section**, **Row**, or **Module** you want to save
3. Click the **Add to Library** icon (located in the element's toolbar)
4. A modal will appear with save options:
   - Enter a name for your library item
   - (Optional) Check **Save as Global** if you want the element to update everywhere it's used
   - (Optional) Select or create a category
   - (Optional) Add tags for easier searching
5. Click **Submit** to save

### Save Individual Items from a Layout

To break down a page into individual reusable components:

1. Open a page in the Visual Builder
2. Select a **Section**, **Row**, or **Module**
3. Right-click or click the menu icon and choose **Save To Library**
4. In the **Save Individual Items** section, select which parts to save:
   - The entire section
   - Individual rows within the section
   - Individual modules within rows
5. Configure naming, categories, and tags for each item
6. Click **Submit**

### Save Entire Page Layouts

1. In the Visual Builder, click the **Add Layout** icon (located in the top left corner)
2. Click **Saved Layout** option
3. Enter a name for the layout
4. (Optional) Add categories and tags
5. Click **Submit** to save the full page layout to the library

## Accessing and Using Library Items

### Insert from the Visual Builder

1. While editing a page, click **Add From Library** tab in the left sidebar
2. Browse available library items or use the search function
3. Click on an item to preview it
4. Click **Use This Section/Row/Module** to insert it into your page
5. The item will be added to your page—if it's marked as global, any changes you make will affect all instances

### Edit Library Items

1. Navigate to **Dashboard → Divi → Divi Library**
2. Browse your saved items
3. Click the **Edit With The Divi Builder** button to open an item for editing
4. Make your changes in the Visual Builder
5. Click the **Save** button (top right corner) to save your changes
6. Click the **Exit** button to return to the Dashboard

If the item is marked as global, your changes will automatically apply to all pages using that item.

## Managing Your Library

### View and Organize Library Items

1. Go to **Dashboard → Divi → Divi Library**
2. Here you can:
   - **Create** new library items (page layouts, sections, rows, modules)
   - **Edit** existing elements
   - **Delete** existing elements
3. Use the search and filter functions to find items by name, category, or tag

### Organize with Categories and Tags

1. In the Library management page, click **Create** or edit an existing item
2. Assign it to a category (e.g., "Headers", "Footers", "Blog Sections")
3. Add tags for additional organization (e.g., "homepage", "landing-page", "seasonal")
4. Click **Submit** to save

This organization system helps you quickly locate components when building new pages.

## Import and Export

### Export Your Library

Export your library to create backups or share with team members:

1. Go to **Dashboard → Divi → Divi Library**
2. Click the **Import & Export** button at the top
3. Select the **Export** tab
4. Choose which items to export (all items or specific selections)
5. Click **Download Export** to download a JSON file

### Import Library Items

Add previously exported items to your site:

1. Go to **Dashboard → Divi → Divi Library**
2. Click the **Import & Export** button at the top
3. Select the **Import** tab
4. Click **Import Divi Builder Layouts** and select your exported JSON file
5. Choose which items to import
6. Click **Submit** to complete the import

This is useful for:
- Restoring library items from a backup
- Moving your design system to a new site
- Sharing components with other team members

## Global Elements vs. Regular Library Items

**Global Elements** (marked with **Save as Global**):
- Any edits made to a global element update everywhere it's used across all pages
- Useful for headers, footers, and recurring design patterns
- Saves time if you need consistent updates site-wide
- Cannot be individually customized per page

**Regular Library Items**:
- Each instance is independent
- You can customize each copy differently
- Good for reusable templates that need minor variations
- Changes to the library item don't affect already-placed instances

## Best Practices

**Create a naming convention:**
Use clear, descriptive names like "Hero / Dark Blue" or "Team Section / 3-Column" to make items easy to identify at a glance.

**Use categories strategically:**
Organize by section type (Headers, Footers, Hero sections, Testimonials) or by page type (Homepage, Blog, Services, Contact) depending on your site structure.

**Tag for discoverability:**
Add tags for design themes, color schemes, or use cases (e.g., "light-mode", "dark-mode", "seasonal", "mobile-optimized").

**Keep global items focused:**
Use global elements for truly universal components. Overusing globals can make it difficult to customize pages when needed.

**Maintain version clarity:**
If you have multiple versions of a component (e.g., "CTA Button v1" vs. "CTA Button v2"), explicitly version your library items to avoid confusion.

## Troubleshooting

**Library items don't appear after saving:**
- Refresh the page or clear your browser cache
- Verify that the save operation completed successfully (check for a success notification)
- Ensure you have appropriate user permissions to add library items

**Global element changes aren't propagating:**
- Confirm that the item was saved with **Save as Global** enabled
- Check that you're editing the library item itself (in Divi Library), not an instance on a page
- Clear your WordPress cache if using a caching plugin

**Cannot delete library items:**
- Verify you have admin or editor permissions
- Check if the item is still being used on any pages (some themes prevent deletion of in-use globals)
- Try again after clearing your browser cache

**Import fails or doesn't find items:**
- Ensure the JSON export file is valid and hasn't been corrupted
- Check that the export file is from a compatible Divi version
- Try importing a smaller subset of items first to identify which item is causing issues

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 Library behavior. The library interface and functionality differ significantly from Divi 4 and earlier versions.

## Related

- [Create a New Website Using a Pre-Made Starter Site](create-a-new-website-using-a-pre-made-starter-site.md)
- [Element Presets](element-presets.md)
- [Divi Builder Basics](getting-started-with-divi-5-theme-builder.md)
- [Theme Builder](getting-started-with-divi-5-theme-builder.md)
