---
title: "Building Templates for Your Website with Theme Builder in Divi 5"
category: builder
tags: ["builder", "theme-builder", "templates", "visual-builder", "workflow"]
related: ["getting-started-with-divi-5-theme-builder", "managing-theme-builder-templates-in-divi-5"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/10586867-building-templates-for-your-website-with-theme-builder-in-divi-5"
---

# Building Templates for Your Website with Theme Builder in Divi 5

This guide walks you through the process of building custom templates using Divi 5's Theme Builder. Whether you're creating global headers and footers or custom templates for specific content types, the workflow is visual, intuitive, and powerful.

## Overview

The Theme Builder uses the same Visual Builder you use for pages and posts, so if you're familiar with Divi's page builder, you already know how to build templates. The main difference is that templates apply to site-wide elements or entire content categories instead of individual pages.

## How to Access the Theme Builder

1. In the WordPress dashboard, click **Divi → Theme Builder**
2. You'll see the main Theme Builder screen with cards for each template type
3. Click any card or the **+** button to create or edit a template

## Building a Global Header

### Step 1: Add a Global Header

From the Theme Builder screen:

1. Click the **Header** card or the **+** button in the **Header** section
2. Select **Add Global Header**
3. The Visual Builder opens with a blank canvas

### Step 2: Design Your Header

Use the Divi Visual Builder to add elements:

- **Logo/Brand**: Add a text module with your logo or an image module with your logo file
- **Navigation**: Add a navigation menu module and select your primary menu
- **Search**: Add a search module for site-wide search functionality
- **Call-to-Action**: Add a button module linking to a key page (e.g., "Get Started", "Contact")
- **Contact Info**: Add text modules with phone, hours, or email (optional)
- **Social Links**: Add a social icons module (optional)

All elements are placed in a layout structure (rows and sections) just like a regular page.

### Step 3: Style Your Header

- Use the Divi Variable system for colors, fonts, and spacing to maintain consistency
- Apply responsive settings so your header looks good on mobile, tablet, and desktop
- Use the Style Inspector to manage colors and fonts across all elements
- Set breakpoint-specific overrides for mobile responsiveness

### Step 4: Save Your Header

Click **Save** in the top-right corner of the builder. Your global header is now live across your entire site.

## Building a Global Footer

### Step 1: Add a Global Footer

From the Theme Builder screen:

1. Click the **Footer** card or the **+** button in the **Footer** section
2. Select **Add Global Footer**
3. The Visual Builder opens

### Step 2: Design Your Footer

Typical footer content includes:

- **Copyright Notice**: A text module with copyright text (e.g., "© 2026 Your Company Name")
- **Footer Navigation**: A navigation module with secondary menu
- **Contact Info**: Text modules with address, phone, email
- **Newsletter Signup**: A newsletter signup form module
- **Social Links**: Social icons module
- **Widget Area**: Column dedicated to WordPress widgets (optional)
- **Payment Icons**: Images showing accepted payment methods (optional)

### Step 3: Create a Multi-Column Layout

Footers typically use multiple columns:

1. Add a section with 3 or 4 columns
2. In the first column, place copyright and company info
3. In the second column, place footer navigation
4. In the third column, place social links or newsletter signup
5. (Optional) Fourth column for additional links or widgets

### Step 4: Save Your Footer

Click **Save** to apply your footer globally across the entire site.

## Building Custom Templates for Content

### Step 1: Create a New Template

From the Theme Builder screen:

1. Click **Add New Template**
2. Give your template a descriptive name (e.g., "Landing Page", "Product", "Blog Post")
3. Choose what content type this template applies to:
   - **All Posts**: Applies to all blog posts
   - **Specific Categories**: Select one or more categories
   - **All Pages**: Applies to all pages
   - **Specific Pages**: Select individual pages from a list
   - **Archives**: Applies to post type archives (if applicable)

### Step 2: Add Content Containers

Every custom template needs a content area that displays the actual post or page content.

For post templates, you **must** include the **Post Content module**:

1. In the Visual Builder, create a layout section for your main content
2. Add a **Post Content** module to this section
3. The Post Content module automatically displays the post's content, title, featured image, etc.

!!! note "Important"
    Custom post/page templates must contain a Post Content module, or the page content won't display.

### Step 3: Add Supporting Sections

Beyond the Post Content module, add sections for:

- **Header Area**: Breadcrumbs, post meta (author, date, categories)
- **Sidebar**: Related posts, recent posts, category listing, search
- **Before Content**: Hero section, featured image, intro text
- **After Content**: Call-to-action, related posts, author bio
- **Comments Section**: (Optional) Comment form if not built into Post Content module

### Step 4: Style for Responsiveness

1. Design for desktop first
2. Use the responsive breakpoint tools to adjust layout for tablet (768px)
3. Adjust again for mobile (480px)
4. Test on actual devices to ensure readability and functionality

### Step 5: Use Divi Variables

Keep your design system consistent:

- Use global color variables for all text, backgrounds, and borders
- Use global font variables for headings, body text, and accents
- Use spacing variables for consistent padding and margins
- Update a variable once to change it everywhere

### Step 6: Save Your Template

Click **Save** in the builder. Your template is now available for assignment to content.

## Common Design Patterns

### Pattern 1: Blog Post Template

Structure:

```
[Global Header]
[Breadcrumbs + Post Meta]
[Featured Image]
[Post Title]
[Post Content] [Sidebar: Recent Posts, Categories, Search]
[Related Posts Section]
[Comment Section]
[Call-to-Action]
[Global Footer]
```

Use this for blog posts across your site.

### Pattern 2: Landing Page Template

Structure:

```
[Minimal Header - Logo Only]
[Hero Section with Title & CTA]
[Main Content Sections]
[Social Proof / Testimonials]
[Final Call-to-Action]
[Minimal Footer]
```

No navigation, no sidebar—designed to focus attention on conversion.

### Pattern 3: Service Page Template

Structure:

```
[Standard Header]
[Hero Section - Service Name & Image]
[Service Overview]
[Features/Benefits Section - 3 Columns]
[Process/Steps Section]
[Testimonials/Case Studies]
[Pricing or CTA Section]
[Related Services / Sidebar]
[Standard Footer]
```

Used for pages describing individual services.

### Pattern 4: Product Page Template

Structure:

```
[Standard Header]
[Hero Section - Product Image + Title]
[Product Overview + Key Details]
[Detailed Specifications Table]
[Feature Breakdown - Multiple Sections]
[Pricing & Add to Cart]
[Customer Reviews]
[Related Products / Sidebar]
[Standard Footer]
```

Designed for WooCommerce product pages.

## Best Practices for Template Building

### Plan Before Building

- Sketch your template layout on paper before opening the Visual Builder
- Identify which sections need responsive adjustments
- Plan your color and typography hierarchy
- List all dynamic elements (post title, featured image, author, etc.)

### Use the Post Content Module Correctly

- The Post Content module displays the actual page/post content
- Configure it to show/hide featured image based on your needs
- Configure title display (usually hidden since you add it separately for better styling)
- Adjust module styling for consistent appearance across templates

### Organize with Sections and Rows

- Use sections to group related content
- Use rows within sections to create column layouts
- Name your sections descriptively for easier management
- Use the Layers Panel to find and select elements quickly

### Test Across Devices

- Preview your template on desktop, tablet, and mobile
- Use Divi's responsive preview tools to test specific breakpoints
- Check that text remains readable and images scale properly
- Test navigation, forms, and interactive elements on mobile

### Maintain Backups

- Export your templates regularly to create backups
- Save exported templates in version control or cloud storage
- Before making major changes, export the current version
- Refer to [Managing Theme Builder Templates](managing-theme-builder-templates-in-divi-5.md) for export instructions

### Use a Style Guide

- Keep color, typography, and spacing consistent across all templates
- Document your design system decisions
- Use Divi Variables to enforce consistency
- Train other team members on the design system

## Troubleshooting

!!! warning "Post Content Not Showing"
    If the post/page content isn't displaying:
    1. Verify the Post Content module is in your template
    2. Check that the module settings allow content to display
    3. Ensure the template is actually assigned to the post/page
    4. Clear all caches (browser, WordPress, caching plugins)

!!! warning "Template Not Applying to Content"
    If a custom template isn't appearing on assigned pages:
    1. Verify the template is published (not draft)
    2. Check the template assignment in the page/post editor
    3. Confirm the assignment criteria match your content
    4. Clear site and browser caches
    5. Try assigning the template again

!!! warning "Elements Overlapping on Mobile"
    If elements overlap on mobile devices:
    1. Use the responsive preview tool to test mobile view
    2. Reduce font sizes at the mobile breakpoint
    3. Adjust padding/margins for smaller screens
    4. Change multi-column layouts to single-column on mobile
    5. Test on actual mobile devices to confirm

!!! warning "Performance Issues with Complex Templates"
    If templates feel slow to load or edit:
    1. Reduce the number of heavy modules (videos, images) in one section
    2. Lazy-load images using Divi's image settings
    3. Simplify complex nested layouts
    4. Remove unused CSS and JavaScript from global styles
    5. Consider splitting very complex layouts into multiple sections

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 Theme Builder workflow exclusively. Divi 4's Theme Builder had a different interface and design process.

## Related

- [Getting Started with Divi 5 Theme Builder](getting-started-with-divi-5-theme-builder.md)
- [Managing Theme Builder Templates in Divi 5](managing-theme-builder-templates-in-divi-5.md)
- [Exploring Divi 5's New Features](exploring-divi-5-s-new-features.md)
