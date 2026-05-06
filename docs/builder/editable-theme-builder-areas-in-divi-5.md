---
title: "Editable Theme Builder Areas in Divi 5"
category: builder
tags: ["builder", "theme-builder", "templates", "editable-areas", "workflow"]
related: ["build-custom-templates-using-the-theme-builder-in-divi-5.md", "getting-started-with-divi-5-theme-builder.md", "divi-5-role-editor.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14014566-editable-theme-builder-areas-in-divi-5"
---

# Editable Theme Builder Areas in Divi 5

In Divi 5, you can edit Theme Builder templates directly from any page on your site. Rather than jumping between pages and templates, you open the builder on a regular page, click into the header or footer template, make changes, and save—all in one session.

## Overview

Editable Theme Builder areas allow you to view and edit global template regions while designing a page in context. This feature improves workflow by eliminating the need to navigate away from a page, open the Theme Builder separately, load a template, make changes, and return.

### Key Benefits

**Spot design conflicts in real time**
When building a new page, you see your real header and footer surrounding it. Font sizes that clash, colors that don't match, or spacing that looks off become immediately visible.

**Update site navigation without leaving**
Your navigation menu lives in the header template. Previously, updating it meant going to the Theme Builder, loading the header, making changes, and coming back. In Divi 5, open any page's builder, click into the header, update the menu, and save—all in one session.

**Fix footer issues on the spot**
Footer layouts (contact details, social links, copyright text) apply to every page. If you spot an error while reviewing a blog post, fix it without leaving the builder. No need to open a separate editing session.

**Design pages in full context**
When building a new page, you see it surrounded by your real header and footer by default. You design the page in context rather than in isolation, catching alignment and spacing issues early.

## Enabling Editable Theme Builder Areas

By default, Divi 5 displays your header and footer as you edit pages. If they're hidden, you can re-enable them:

1. Open any page in the Visual Builder
2. In the builder toolbar, look for **Builder Settings** (usually a gear icon)
3. Find the **Show Theme Builder Layouts** option
4. Ensure it's **checked/enabled**
5. Your header and footer now appear in the builder view

## Editing Header and Footer Templates

### From a Page in the Builder

1. Open any page in the Visual Builder (Pages, Posts, or Archive pages)
2. The header and footer appear above and below your page content
3. Hover over the **header area** or **footer area**
4. Click **Edit** (or double-click the region)
5. The Template Builder opens, allowing you to edit that template
6. Make your changes (add/remove modules, update content, adjust styling)
7. Click **Save** (or **Ctrl+S** / **Cmd+S**)
8. Click **Exit** to return to the page builder
9. Your header/footer updates are now live across the entire site

### What's Editable in Theme Builder Areas?

You can modify:

- **Header templates**: Logo, navigation menu, search bar, CTA buttons, tagline
- **Footer templates**: Contact details, copyright text, social links, payment methods, logo
- **Sidebar templates** (on sites with custom sidebars): Widgets, menus, recent posts
- **Any custom template area** you've created in Theme Builder

You cannot directly edit:

- Individual post/page content from within the header/footer editor
- Global theme settings from the header/footer template view (use Divi → Theme Options for that)

## Controlling Access with Role Editor

If you want to restrict editing of templates to certain user roles:

1. In your WordPress dashboard, navigate to **Divi** → **Role Editor**
2. Find the role you want to manage (Editor, Contributor, etc.)
3. Under **General Functionality**, locate the **Theme Builder** option
4. **Check** the box to allow this role to edit Theme Builder templates
5. **Uncheck** to prevent this role from editing templates (they can still edit page content)
6. Click **Save** (if applicable)

This is useful if you want editors to build pages but not modify site-wide header/footer layouts.

## Workflow Improvements in Divi 5

### Before Divi 5

1. Open a page for editing
2. Realize the header menu is wrong
3. Close the page builder
4. Open Theme Builder
5. Find and open the Header template
6. Edit the menu
7. Save and close the template
8. Go back to your page
9. Continue editing (disruption, context loss)

### With Editable Theme Builder Areas (Divi 5)

1. Open a page for editing
2. Click into the header to edit
3. Update the menu
4. Save
5. Exit to the page
6. Continue editing (seamless workflow, full context)

## Common Tasks with Editable Areas

### Update Navigation Menu

1. Open any page in the builder
2. Click the **Edit** button on the header area
3. Find the **Menu** module
4. Click to open its settings
5. Change menu items, links, or styling
6. Save and exit

### Modify Footer Copyright Text

1. Open any page in the builder
2. Click the **Edit** button on the footer area
3. Locate the text module containing copyright information
4. Update the year, company name, or legal text
5. Save and exit
6. Changes apply site-wide

### Add a New Section to Header

1. Open the builder on any page
2. Click **Edit** on the header area
3. Use **Add Row** to insert a new section
4. Add modules (text, image, button, etc.)
5. Style and save
6. Exit to the page builder

### Test Responsive Design

1. Open a page in the builder
2. View the header/footer in the visual preview
3. Test how navigation, menus, and footer links respond to different screen sizes
4. Adjust responsive settings directly from the template
5. Save and exit

## Troubleshooting

!!! warning "Header/Footer Not Showing in Builder"
    **Cause:** Theme Builder Layouts display is disabled.
    
    **Solution:** Click the **Builder Settings** icon (gear) in the toolbar and enable **Show Theme Builder Layouts**.

!!! warning "Cannot Edit Header/Footer — Edit Button Not Appearing"
    **Cause:** Visual Builder is not enabled for your post type, or you lack permission.
    
    **Solution:** 
    - Check **Divi** → **Theme Options** → **Builder** → **Post Type Integration** to ensure Visual Builder is enabled for your post type
    - Check **Divi** → **Role Editor** to confirm your user role has Theme Builder editing permissions

!!! warning "Edit With Divi Button Not Available on Archive Pages"
    **Cause:** Your site may not have a Theme Builder Header or Footer created yet.
    
    **Solution:** 
    - Create a Theme Builder Header template first: **Divi** → **Theme Builder** → **Add New Template** → Select **Header**
    - Or create a Theme Builder Footer template
    - Once at least one template exists, the **Edit with Divi** option becomes available on archive pages

!!! warning "Changes to Template Not Showing on Pages"
    **Cause:** Page cache or browser cache may be showing an outdated version.
    
    **Solution:** 
    - Clear your site's cache (if using a cache plugin like WP Super Cache)
    - Clear your browser cache
    - Hard refresh the page (Ctrl+Shift+R or Cmd+Shift+R)

## Version Notes

!!! note "Divi 5 Feature"
    Editable Theme Builder areas are exclusive to Divi 5. This workflow improvement does not exist in Divi 4. This page documents Divi 5 behavior only.

## Related

- [Build Custom Templates Using the Theme Builder in Divi 5](../builder/build-custom-templates-using-the-theme-builder-in-divi-5.md)
- [Getting Started with Divi 5 Theme Builder](../builder/getting-started-with-divi-5-theme-builder.md)
- [Divi 5 Role Editor](../builder/role-editor.md)
- [Theme Options Guide](../builder/divi-5-theme-options.md)
