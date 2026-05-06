---
title: "Create a New Website Using a Pre-Made Starter Site"
category: builder
tags: ["builder", "starter-sites", "layouts", "quick-start"]
related: ["divi-library-in-divi-5.md", "install-and-activate-divi-5.md", "theme-builder-basics.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12985041-create-a-new-website-using-a-pre-made-starter-site"
---

# Create a New Website Using a Pre-Made Starter Site

Launch a professional website in minutes using Divi 5's pre-made starter site templates.

## Overview

Divi 5 includes a collection of professionally designed starter sites that cover a wide range of industries and use cases—from blogs and portfolios to e-commerce stores and service-based businesses. Instead of building from a blank canvas, you can select a starter site that matches your vision, customize the content and colors to match your brand, and publish your website in hours instead of weeks.

Each starter site comes complete with pre-built pages (home, about, services, contact, blog), theme layouts via the Theme Builder, and a global design system using Divi's Global Variables and Option Group Presets. This makes it easy to maintain a consistent look and feel while customizing every aspect to fit your needs.

![Starter Sites Dashboard](../assets/screenshots/builder/create-a-new-website-using-a-pre-made-starter-site/overview.png){ loading=lazy }
*Browse and preview professionally designed starter sites from the Divi Quick Sites dashboard.*

## Finding and Selecting a Starter Site

### Access Quick Sites

1. Log in to the WordPress dashboard
2. Navigate to **Divi → Dashboard**
3. Look for the **Divi Quick Sites** card
4. Click **Select a Website Template** button

### Browse and Preview Starter Sites

1. A modal will open displaying available starter sites, organized by category (e.g., Business, Blog, Portfolio, E-commerce)
2. Scroll through the available templates to find one that matches your vision
3. Click the **Preview** button to see a full-screen preview of the starter site
4. Review the design, layout, and content structure
5. When you find a starter site you like, click the **Start With** button to select it

## Setting Up Your Starter Site

### Configure Basic Settings

After selecting a starter site:

1. Enter your **Site Name** (this is the name of your website)
2. Enter a **Site Slogan** (optional tagline or description)
3. Upload or select your **Logo Image** to replace the placeholder
4. Choose which **Pages to include** from the starter site. For example:
   - Home
   - About
   - Services
   - Contact
   - Blog
   
   Uncheck any pages you don't need; you can always add more later.

5. Click **Generate & Publish My Website** button

Divi will now generate your site with all selected pages, theme layouts, and design system in place.

## Editing Your Starter Site Pages

### Access Your New Pages

After generation completes:

1. Navigate to **Pages → All Pages** in the WordPress dashboard
2. Your new pages will appear in the list with the starter site content
3. Each page shows action icons:
   - **Pencil icon**: Used to edit the page
   - **Eye icon**: Used to view it on the front end
   - **Trash icon**: Used to delete it if you don't need it

### Edit Page Content

1. Click the **pencil icon** on any page
2. Click **Edit with Divi** to open the page in the Divi Visual Builder
3. Modify text, images, and layouts to match your content
4. Save your changes by clicking **Save** in the Visual Builder
5. Click **Exit** to return to the page editor

## Customizing Your Design

### Customize the Global Header and Footer

1. Navigate to **Divi → Theme Builder**
2. Click the **pencil icon** on the global header or footer to edit it
3. Make your changes in the Visual Builder (e.g., change company name, update contact info, revise footer links)
4. Click **Save Changes** in Theme Builder to apply updates site-wide

### Update Typography

1. Go to **Divi → Theme Customizer → General Settings → Typography**
2. Click on **Header Font** and **Body Font** to match your brand
3. Select new typefaces from the available options
4. Click **Publish** to save your changes

### Adjust Colors

1. Navigate to the **Theme Customizer** and find color settings
2. Use the **Global Variable Manager** to access color presets
3. Click on the **Colors** tab
4. Edit existing color variables to match your brand palette
5. Save your changes

### Modify Element Presets

1. When editing any page, click the **Element Preset** dropdown at the top
2. Browse pre-configured styling options for common elements
3. Click the **Gear icon** next to the preset's name to customize it
4. Apply the preset to elements on your page for consistent styling

## Pre-Population and Customization

### What Gets Pre-Populated

The starter site generates:
- Complete page layouts for all selected pages
- Global header and footer templates
- Theme Builder templates for archives and single posts
- Global Variables and colors configured to the starter site's design
- Element Presets for typography, buttons, spacing, and effects

### Customization Recommendations

**Start with a fresh or lightly used site:**
Use Divi Quick Sites on fresh or lightly used sites so Quick Sites can safely set up your homepage, menus, and Theme Builder templates without conflicts.

**Back up first:**
If the site already has content or custom templates, back up first if the site already has content or custom templates. You can always restore from backup if needed.

**Adjust gradually:**
After generation, take time to:
- Review all pages and update placeholder content
- Test on mobile and desktop to ensure responsive design
- Update the navigation menu to match your site structure
- Add any additional pages or sections you need

## Working with Generated Content

### Modify Generated Pages

Once pages are created, you have full control:

1. Edit text and images directly in the Visual Builder
2. Change the page layout using different rows and sections
3. Add or remove modules as needed
4. Customize styling through Design Tab options or presets

### Reorder Pages

1. Go to **Pages → All Pages**
2. Drag pages to reorder them in your site hierarchy
3. Update your navigation menu to reflect the new order

### Delete Unnecessary Pages

1. If you don't need a generated page, go to **Pages → All Pages**
2. Hover over the page and click **Trash**
3. The page will move to trash and won't appear on your site

## Common Patterns

**Multi-page site with consistent design:**
Use the global header/footer and color system from the starter site across all pages. Changes made in Theme Builder automatically apply everywhere.

**Portfolio or case study sites:**
Take advantage of the pre-built layout structures and customize them with your own images and project details.

**Blog with professional design:**
The blog pages come with featured images, post metadata, and archive layouts already configured and styled.

**Services or pricing pages:**
Use the pre-built pricing tables and service section layouts as starting points, then customize with your own offerings and descriptions.

## Troubleshooting

**Pages don't generate or appear incomplete:**
- Refresh the WordPress dashboard and check Pages again
- Clear your browser cache
- Verify you selected at least one page to generate
- Check that your site has sufficient available storage space

**Design elements look broken or misaligned:**
- Clear WordPress object caching if you use a caching plugin
- Check that all active plugins are compatible with Divi 5
- Try switching to a default WordPress theme temporarily to isolate theme conflicts
- Verify your theme settings are correctly configured in Theme Customizer

**Logo doesn't display:**
- Ensure the logo file is in a supported format (PNG, JPG, GIF, SVG)
- Check that the logo file size isn't too large
- Verify the image was uploaded correctly by checking the Media library
- Try re-uploading the logo

**Colors or fonts not updating site-wide:**
- Confirm you saved your changes in Theme Customizer (look for a success message)
- Clear your site's cache if using a caching plugin
- Check that Global Variables are being used (not overridden by element-specific styles)
- Visit the front end to verify changes are live

**Theme Builder templates don't apply to generated pages:**
- Ensure the template is assigned to the correct page type (single pages, archives, etc.)
- Refresh the front-end pages to clear cached versions
- Check that the template priority is set correctly if multiple templates exist

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5's Quick Sites feature. Starter site functionality is not available in Divi 4 or earlier versions.

## Related

- [Divi Library in Divi 5](divi-library-in-divi-5.md)
- [Install and Activate Divi 5](install-and-activate-divi-5.md)
- [Theme Builder Basics](getting-started-with-divi-5-theme-builder.md)
- [Global Variables in Divi 5](global-variables.md)
