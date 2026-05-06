---
title: "Getting Started with Divi 5 Theme Builder"
category: builder
tags: ["builder", "theme-builder", "templates", "headers", "footers", "getting-started"]
related: ["building-templates-for-your-website-with-theme-builder-in-divi-5", "managing-theme-builder-templates-in-divi-5"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/10374023-getting-started-with-divi-5-theme-builder"
---

# Getting Started with Divi 5 Theme Builder

The Divi 5 Theme Builder is a powerful tool for creating and managing custom templates for your WordPress website. It extends Divi Builder's capabilities to site-wide elements like headers, footers, and post templates, so you can design them visually without manually editing theme files.

## Overview

While the Divi Visual Builder lets you design individual pages, the Theme Builder lets you design the structural elements that appear across your entire site. Think of it as the foundation template system that wraps around your page content.

With Theme Builder, you can:

- Create global headers that apply site-wide
- Design custom footers for your entire site
- Build default templates for posts, pages, archives, and custom post types
- Override the default template with custom designs for specific pages, categories, or post types
- Manage all templates from a single, organized interface

## How to Access the Divi 5 Theme Builder

### Step 1: Ensure Divi 5 Is Installed

Log into your WordPress dashboard and verify that Divi 5 is installed and activated as your active theme.

### Step 2: Navigate to Theme Builder

In the WordPress dashboard, go to **Divi → Theme Builder**.

You'll see the main Theme Builder screen where all templates are managed.

### Step 3: Explore the Interface

The Theme Builder interface displays available templates as a list of cards. Each card represents a template and shows:

- Template name
- Template type (Global Header, Global Footer, Post, Page, etc.)
- Current status
- Action buttons for editing, duplicating, and more

## Understanding the Theme Builder Interface

### Default Website Template

The **Default Website Template** is the main template that affects all pages unless overridden by a more specific template.

!!! note
    The Default Website Template cannot be deleted. It serves as the fallback template for any page without a custom template assigned.

### Global Sections

The Theme Builder organizes site-wide design elements into three main areas:

| Section | Purpose | Scope |
|---------|---------|-------|
| **Header** | Logo, navigation menu, contact info, search bar | Appears at the top of every page |
| **Body** | Post/page content container | Wraps the main content area |
| **Footer** | Site footer info, copyright, additional navigation | Appears at the bottom of every page |

!!! note
    Global sections can also be configured as non-global and attached to different templates for custom variations.

### Custom Templates

Beyond the global header/body/footer, you can create custom templates for:

- Specific pages or posts
- Post categories
- Custom post types
- Archives
- Search results

Custom templates override the default template for their assigned content.

### Template Management Tools

The Theme Builder provides action buttons to:

- **Add** new templates
- **Edit** existing templates in the Visual Builder
- **Duplicate** templates to save time
- **Delete** templates (except the Default Website Template)

## Creating Your First Global Header

### Quick Start

1. From the Theme Builder screen, click the **Header** card or the **+** button in the Header section
2. In the modal that appears, click **Add Global Header**
3. The Visual Builder opens—design your header with logo, navigation, and other elements
4. Click **Save** to apply changes globally

### What to Include

A typical global header might contain:

- **Logo**: Your site's logo or brand name
- **Navigation Menu**: Primary menu for site navigation
- **Search Bar**: Optional search functionality
- **Call-to-Action Button**: Optional button linking to a key page
- **Contact Info**: Phone number, email, or hours (optional)

## Creating a Global Footer

### Quick Start

1. From the Theme Builder screen, click the **Footer** card or the **+** button in the Footer section
2. Click **Add Global Footer**
3. Design your footer in the Visual Builder
4. Click **Save** to apply globally

### What to Include

A typical global footer might contain:

- **Copyright Notice**: Copyright year and owner
- **Footer Navigation**: Secondary menu or sitemap
- **Social Links**: Links to your social media profiles
- **Contact Info**: Business address, phone, email
- **Newsletter Signup**: Optional email capture form
- **Payment Methods**: Optional payment icons if applicable

## Creating Custom Page Templates

### When to Use Custom Templates

Create a custom template when a specific page or group of pages needs a different layout than the default template. Examples:

- Landing pages with no sidebar
- Product pages with custom layout
- Blog archive pages with grid or card layout
- Contact pages with specific sidebar elements

### Quick Start

1. From the Theme Builder screen, click **Add New Template**
2. Name your template (e.g., "Landing Page", "Product Page")
3. Choose what the template applies to:
   - **All Posts**: Applies to all blog posts
   - **Specific Categories**: Applies to posts in selected categories
   - **All Pages**: Applies to all pages
   - **Specific Pages**: Choose individual pages from a list
4. Click **Create Template**
5. Design in the Visual Builder and click **Save**

## Assigning Templates to Content

### For Posts & Pages

After creating a template, assign it to content:

1. Edit the post or page in WordPress
2. Look for the **Divi Theme Template** dropdown in the page editor
3. Select your custom template from the list
4. Save the post or page

### For Archives & Custom Post Types

Archive and custom post type templates are assigned automatically based on your template settings. Refer to [Managing Theme Builder Templates](managing-theme-builder-templates-in-divi-5.md) for advanced assignment options.

## Common Patterns

### Pattern 1: Minimal Landing Page

Create a landing page template with:
- Minimal header (just logo, no full navigation)
- No sidebar
- Full-width content area
- Simple footer with just essentials

This works well for lead generation or product launches.

### Pattern 2: Blog Post Template

Create a post template with:
- Standard header (logo + full navigation)
- Main content area with featured image
- Sidebar with recent posts, categories, and search
- Standard footer

### Pattern 3: Service Page Template

Create a template for service pages with:
- Standard header
- Hero section for the service name/description
- Multi-section content area
- Call-to-action section before footer
- Standard footer

## Troubleshooting

!!! warning "Template Not Appearing"
    If a custom template isn't appearing on your page, check:
    1. Is the template correctly assigned in the page/post editor?
    2. Is the template published (not in draft)?
    3. Do you have the correct post type or category selected?
    4. Clear your browser cache and your site's cache plugin

!!! warning "Global Header/Footer Not Showing"
    If your global header or footer isn't displaying:
    1. Verify it's been published (not in draft)
    2. Check that no custom template is overriding it
    3. Ensure your theme layout includes header and footer sections
    4. Clear all caches (browser, WordPress, caching plugins)

!!! warning "Changes Not Saving"
    If changes in the Visual Builder aren't saving:
    1. Check for JavaScript errors in the browser console
    2. Verify your user role has permission to edit theme options
    3. Ensure the hosting environment's file permissions allow writing
    4. Try saving from a different browser or in incognito mode

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 Theme Builder behavior exclusively. Divi 4 had a different Theme Builder interface and workflow.

## Related

- [Building Templates for Your Website with Theme Builder in Divi 5](building-templates-for-your-website-with-theme-builder-in-divi-5.md)
- [Managing Theme Builder Templates in Divi 5](managing-theme-builder-templates-in-divi-5.md)
- [Exploring Divi 5's New Features](exploring-divi-5-s-new-features.md)
