---
title: "Use Theme Builder to Customize Your Website's Header and Footer"
category: builder
tags: [theme-builder, builder, header, footer, customization]
related: [getting-started-with-the-divi-5-visual-builder, divi-visual-builder-overview]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12984638-use-theme-builder-to-customize-your-website-s-header-and-footer"
---

# Use Theme Builder to Customize Your Website's Header and Footer

Divi's Theme Builder lets you design global and page-specific headers and footers without touching code. Create reusable header and footer layouts that apply across your entire site, or override them with custom designs for specific pages or post types.

## Overview

The Theme Builder is a site-wide template system that controls the structural elements of your site — headers, footers, and page templates. Unlike the Visual Builder (which edits individual page content), Theme Builder creates wrapper layouts that appear on every page unless overridden.

Headers and footers are the most common Theme Builder templates. A **Global Header** appears at the top of every page on your site. A **Global Footer** appears at the bottom. You can build these once and they automatically render everywhere, or you can create **Custom Headers/Footers** that override the global versions for specific pages, posts, categories, or custom post types.

Common use cases include:
- Creating a navigation menu with logo that appears site-wide
- Building a standardized footer with contact info, social links, and copyright
- Designing different headers for different sections (shop vs. blog, for example)
- Maintaining consistent branding across all pages without manually editing each one

## Setting Up Theme Builder

### Enable Theme Builder

Before you can create global headers and footers, ensure Divi is installed and activated. Then:

1. In the WordPress dashboard, navigate to **Divi → Theme Builder**
2. You'll see the Template Library with options for creating new templates
3. If you plan to use a Menu module in your header, create at least one menu in **Appearance → Menus** first

### Create a Default Website Template

The **Default Website Template** is the master template that controls the default header, body, and footer for your entire site.

1. In **Divi → Theme Builder**, click **Add New Template**
2. Choose **Default Website Template**
3. Click **Create Template**

This creates a template that wraps around every page's content. Now you can add a global header and footer to it.

## Building a Global Header

### Step 1: Add a Global Header

1. From **Divi → Theme Builder**, select your **Default Website Template**
2. Click **Add Global Header**
3. You'll enter the Theme Builder editor showing a blank header area

### Step 2: Design the Header Layout

Create a basic header structure:

1. Click **Add Section** to create a section
2. Add a **Row** inside (for example, one row with one or two columns)
3. Drag modules into the columns:
   - **Menu Module** — Display your site's navigation and logo
   - **Search Module** — Add a search bar
   - **Text Module** — Add a tagline or description

### Step 3: Configure the Menu Module

The Menu module is the most important part of a header. To set it up:

1. Click the **Menu module** to open its settings
2. Go to the **Content tab**
3. Under **Menu**, select the WordPress menu you created earlier
4. Under **Logo**, upload your website's logo image
5. Go to the **Design tab**
6. Under **Menu Text → Text Alignment**, choose **Right** to right-align menu items (optional)
7. Adjust colors, spacing, and font sizes to match your branding

### Step 4: Save and Publish

1. Click the **Save** button in the top toolbar
2. Click **Exit** to return to Theme Builder
3. Click **Save Changes** in the top right to publish the header

Your global header now appears on every page of your site.

## Building a Global Footer

### Step 1: Add a Global Footer

1. From **Divi → Theme Builder**, select your **Default Website Template**
2. Click **Add Global Footer**
3. You'll enter the Theme Builder editor showing a blank footer area

### Step 2: Design the Footer Layout

A typical footer contains multiple sections:

1. Click **Add Section** to create a section
2. Add a **Row** and divide it into columns (for example, three columns for content, social, and contact)
3. Add modules to each column:
   - **Text Module** — Add an about blurb or company description
   - **Social Follow Module** — Display social media icons
   - **Email Optin Module** — Add an email signup form
   - **Text Module** — Add copyright notice and footer credits

### Step 3: Configure Each Module

Configure modules to display your footer content:

- **About section:** Use a Text module with your company description
- **Social section:** Use a Social Follow module to link to your social profiles
- **Contact section:** Use an Email Optin module or additional Text module
- **Copyright section:** Use a Text module with `&copy; 2026 Your Company. All rights reserved.`

Adjust colors, spacing, and alignment in the Design tab to create a cohesive look.

### Step 4: Save and Publish

1. Click the **Save** button in the top toolbar
2. Click **Exit** to return to Theme Builder
3. Click **Save Changes** in the top right to publish the footer

Your global footer now appears on every page of your site.

## Creating Custom Headers and Footers for Specific Pages

You can override the global header and footer for specific pages, posts, categories, or post types.

### Step 1: Create a New Template

1. From **Divi → Theme Builder**, click **Add New Template**
2. Choose what this template should apply to:
   - **Specific Page** → Select a page (e.g., About, Contact)
   - **All Posts** — applies to all blog posts
   - **Product Category X** — applies to a specific WooCommerce category
   - **Custom Post Type** — applies to custom post types
3. Click **Create Template**

### Step 2: Add Custom Header/Footer (Optional)

1. In the template editor, you can click **Add Custom Header** or **Add Custom Footer**
2. Build them just like you did for the global versions
3. If you **do not** add a custom header, the page uses the **Global Header**
4. If you **do** add a custom header, it overrides the global header for that template's pages

### Step 3: Build the Page Body

1. Add sections and modules to build the page content
2. This is the main area between the header and footer

### Step 4: Save

1. Click **Save** in the top toolbar
2. Click **Save Changes** to publish the template

## Managing Theme Builder Templates

### View All Templates

In **Divi → Theme Builder**, you'll see a list of all your templates. Each shows:
- The template name and type (Default Website, Specific Page, etc.)
- An **Edit** button to modify the template
- An **Eye icon** to activate/deactivate the template
- Status (active or inactive)

### Disable a Template

Click the **Eye icon** next to a template to deactivate its header and/or footer. When disabled, the template reverts to using the global header and footer.

## Exporting and Importing Theme Builder Templates

### Export Templates

You can export your Theme Builder templates as a JSON file for backup or sharing:

1. In **Divi → Theme Builder**, click the **Portability icon** (double arrow in the top right)
2. Click the **Export tab**
3. Check **Export All Templates** to export all templates, or uncheck and select specific ones
4. Click **Export Theme Builder Template** to download a JSON file

### Import Templates

To import previously exported templates:

1. In **Divi → Theme Builder**, click the **Portability icon** (double arrow)
2. Click the **Import tab**
3. Upload the JSON file you exported
4. The imported templates are added to your site

This is useful for migrating templates between sites or restoring from backups.

## Building a 404 Error Page

You can use Theme Builder to create a custom 404 page:

1. From **Divi → Theme Builder**, click **Add New Template**
2. In the assignment modal, choose **404 page**
3. Click **Create Template**
4. Design the 404 page content (headline, description, link back to home)
5. Click **Save** and **Save Changes**

Your custom 404 page now appears when visitors land on a non-existent URL.

## Key Differences: Global vs. Custom

| Aspect | Global Header/Footer | Custom Header/Footer |
|--------|----------------------|----------------------|
| **Applies to** | All pages by default | Specific pages/posts/categories |
| **Override behavior** | Used unless a custom version exists | Overrides the global version for selected pages |
| **Setup location** | Default Website Template | Page/Post/Category-specific template |
| **When to use** | Standard site-wide design | Different header/footer for specific sections |

## Common Header Patterns

### Header with Logo + Centered Menu

1. Create a section with one row and three columns
2. Left column: Logo image in an Image module
3. Center column: Menu module (choose "Center" alignment)
4. Right column: Social icons or search in a custom module

### Header with Sticky Navigation

1. Build your header in a section
2. In the **Section settings → Design tab**, check **Sticky** to make it stick to the top while scrolling
3. Adjust z-index if needed to keep it above other content

### Header with Dropdown Menus

1. Use the Menu module
2. In the Menu module settings, enable **Dropdown Menus** (if available in your WordPress menu structure)
3. Ensure submenus are created in **Appearance → Menus**

## Common Footer Patterns

### Multi-Column Footer with Widgets

1. Create a section with multiple columns
2. Add different content to each column (about, contact, recent posts, etc.)
3. Add a final row below with copyright text

### Footer with Newsletter Signup

1. Add an **Email Optin module** in your footer
2. Connect it to your email service (Mailchimp, ConvertKit, etc.)
3. Style the form to match your footer design

### Dark Footer with Light Text

1. In the **Section settings → Design tab → Background Color**, choose a dark color
2. In each module, set text color to white or light gray
3. Ensure sufficient contrast for accessibility

## Troubleshooting

### Header/Footer Not Showing

- Verify the template is assigned correctly in **Divi → Theme Builder**
- Check that the template is **active** (eye icon visible)
- Clear your browser cache and WordPress cache
- Temporarily disable custom CSS/plugins that might hide the header

### Menu Not Appearing in Header

- Ensure you created a menu in **Appearance → Menus**
- In the Menu module settings, confirm the correct menu is selected
- Check that menu items are assigned to the correct location

### Custom Header/Footer Not Overriding Global

- Verify the custom template is set to apply to the correct page/post/category
- Check that the custom template is **active** (eye icon visible)
- Ensure there are no conflicting CSS rules hiding the custom header/footer

### Styling Not Applied

- Check that you've clicked **Save** in the template editor
- Verify you've clicked **Save Changes** in Theme Builder to publish
- Clear all caches (browser, server, WordPress)
- Check for conflicting custom CSS in **Divi → Theme Options → Custom CSS**

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 Theme Builder behavior exclusively. Divi 4 used a different theme builder interface.

## Related

- [Getting Started with the Divi 5 Visual Builder](../builder/visual-builder.md)
- [Divi Visual Builder Overview](../builder/visual-builder.md)
- [Menu Module](../modules/menu.md)
- [Text Module](../modules/text.md)
- [Social Follow Module](../modules/social-media-follow.md)
