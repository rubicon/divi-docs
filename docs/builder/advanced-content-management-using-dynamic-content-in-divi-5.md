---
title: "Advanced Content Management using Dynamic Content in Divi 5"
category: builder
tags: ["builder", "dynamic-content", "custom-fields", "advanced"]
related: ["build-custom-loops-using-loop-builder-in-divi-5.md", "divi-library-in-divi-5.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/13627810-advanced-content-management-using-dynamic-content-in-divi-5"
---

# Advanced Content Management using Dynamic Content in Divi 5

Link content fields to dynamic data sources so modules pull information automatically from posts, custom fields, WooCommerce products, and more.

## Overview

Dynamic content lets you connect text, image, link, and other module fields to posts, custom fields, WooCommerce data, ACF (Advanced Custom Fields) variables, and global Divi variables. Instead of manually entering content into every page, you create a template once—modules pull their own data automatically.

This approach is essential for building scalable sites: create one product page template that automatically displays each product's price, image, and description; create one blog post template that displays post titles, featured images, and published dates.

## What is Dynamic Content?

Dynamic content uses a system where:

1. **Template** – A reusable layout (using Theme Builder or component instances)
2. **Data Source** – Where the content comes from (post title, custom field, WooCommerce product price, etc.)
3. **Field Connection** – The link between a module field and the data source

### Supported Field Types

Most Divi modules support dynamic content on these fields:

- Text content (headings, paragraphs, button text)
- Image sources
- Link URLs
- Colors
- Spacing and sizing variables
- Custom styling values

## Accessing Dynamic Content

### The Dynamic Content Icon

Most text, image, and link fields display a **Dynamic Content icon** (lightning bolt or link symbol). Click it to open the dynamic content selector.

### Where to Find It

1. **Text Modules** – Open the module settings, go to the **Content** tab
2. **Image Modules** – Open the module settings, find the image field
3. **Link Fields** – Any button or link field
4. **Design Values** – Colors, fonts, spacing in the **Design** tab

## Data Sources

### Post/Archive Data

When using Theme Builder templates:

- `Post Title` / `Archive Title` – The page or archive heading
- `Post Content` – The full post body (displays automatically in the Post Content module)
- `Featured Image` – The post's featured image
- `Post Excerpt` – The post summary
- `Published Date` – When the post was published
- `Author` – Post author name
- `Categories` – Categories assigned to the post
- `Tags` – Tags assigned to the post
- `Comments Count` – Number of comments

### Custom Post Types

Dynamic content works with any custom post type (portfolios, testimonials, projects, etc.).

### Custom Fields (ACF Integration)

Advanced Custom Fields (ACF) plugin creates custom fields that you can link via dynamic content:

1. Install and configure Advanced Custom Fields
2. Create custom field groups (text, image, repeater, etc.)
3. In any module field, click the **Dynamic Content icon**
4. Select the custom field to connect

### WooCommerce Product Data

If you use WooCommerce, dynamic content can pull:

- Product name/title
- Product description
- Product image
- Product price
- Product SKU
- Stock status
- Product attributes

### Global Divi Variables

Divi 5 includes global variables for:

- Text content (store phone numbers, addresses, company names)
- Colors (brand colors, accent colors)
- Typography (fonts, sizes, line-height)
- Spacing (padding, margins, gap values)
- Numbers (any numeric value)

When you update a global variable, every module using it updates automatically.

## Using Dynamic Content: Step-by-Step Examples

### Example 1: Basic Post Template

Create a template that displays every post's title, featured image, date, categories, and content automatically.

1. In Theme Builder, create a template for **All Posts**
2. Add a **Heading module** and click the Dynamic Content icon
3. Select `Post/Archive Title` to display the post title automatically
4. Add an **Image module** and use the Dynamic Content icon to select `Featured Image`
5. Add a **Text module** and link it to `Published Date`
6. Add another **Text module** and link it to `Categories`
7. Add a **Post Content module** (which is dynamic by default)
8. Save the template

Now every post automatically uses this layout and displays its own data.

### Example 2: Custom Portfolio/Project Template

Use Advanced Custom Fields for custom project details like client name, project date, and tools used.

1. Use ACF to create custom fields: Client Name (text), Project Date (date), Tools Used (repeater)
2. In Theme Builder, create a portfolio item template
3. Add **Text modules** for each field
4. Click the Dynamic Content icon on each field
5. Link to the corresponding ACF custom field
6. Save as a template for your portfolio

### Example 3: WooCommerce Product Page Template

Create a custom product layout with dynamic price, stock status, and images.

1. In Theme Builder, create a template for **WooCommerce Product**
2. Add modules for:
   - Product title (dynamic)
   - Product image (dynamic)
   - Product price (dynamic)
   - Product description (dynamic)
   - Stock status (dynamic)
   - Product attributes (dynamic)
3. Style the layout
4. Save the template

Every product now uses this layout with its own data.

### Example 4: Global Contact Information Strip

Create a reusable section with your contact details that updates everywhere when you change the phone number or address.

1. Create **Global Text variables** for:
   - Phone Number
   - Email Address
   - Physical Address
2. Create a section with **Text modules** for each contact detail
3. Link each field to the corresponding global variable using the Dynamic Content icon
4. Save the section as a **library item** (reusable layout)
5. Use this section in your header, footer, and contact page
6. When you change the phone number in global variables, it updates everywhere

### Example 5: Consistent Button Styling with Variables

Create buttons that use your brand style consistently everywhere.

1. Create **global Divi variables** for:
   - Button Color
   - Button Hover Color
   - Button Border Radius
   - Button Padding
2. Add a **Button module**
3. In the Design tab, link the background color to the Button Color variable
4. Link border radius to the Button Border Radius variable
5. Link padding to the Button Padding variable
6. Save the button as a **preset**
7. Reuse the preset on every page
8. Update the global variable once, and all buttons update

## Before and After Dynamic Content

### Without Dynamic Content

You manually create a page for each post:
- Home page template
- Blog post 1 (manual title, image, date entry)
- Blog post 2 (manual title, image, date entry)
- Blog post 3 (manual title, image, date entry)
- ... repeat for every post

### With Dynamic Content

You create one post template:
- Post template (title links to Post Title variable, image links to Featured Image variable, etc.)
- Every post automatically uses this template and pulls its own data

## Combining Static and Dynamic Content

### The Before/After Fields

In text/image modules, you can add static content around dynamic values:

1. Enter static text in the **Before** field
2. Link dynamic content
3. Enter static text in the **After** field

Example: Before="Posted on " + Dynamic(Published Date) + After=" by " + Dynamic(Author Name)

Result: "Posted on May 6, 2026 by John Smith"

### HTML in Before/After

You can use HTML tags in Before and After fields:

- Opening tag in Before: `<strong>`
- Closing tag in After: `</strong>`

Example wraps the dynamic content in bold.

## Performance Considerations

### Template Approach

Using Theme Builder templates with dynamic content is the most efficient:

- One template definition
- Database queries are optimized
- Less code on the page

### Custom Field Queries

If you use many custom fields on one page:

- Divi optimizes queries automatically
- ACF caches field queries
- WooCommerce uses built-in query optimization

### Global Variables

Global variables are stored in the database but:

- Divi caches them on page load
- Changes apply instantly
- No performance impact even with many variables

## Common Patterns

### Pattern 1: Single Post Template

Used for blog posts, case studies, testimonials, reviews. One template displays every post with its own content.

### Pattern 2: Portfolio/Project Showcase

Used for portfolio sites, service providers, creative agencies. Display project details, client info, and images automatically.

### Pattern 3: Product Catalog

Used for WooCommerce stores. Display product price, description, images, stock status automatically.

### Pattern 4: Team Member Directory

Use custom fields (ACF) to display team member info: name, title, bio, photo, social links.

### Pattern 5: Global Design System

Create global variables for all colors, fonts, and spacing. Link modules to these variables so brand changes update everywhere.

## Troubleshooting

### Dynamic Content Doesn't Appear

- Verify the template is assigned correctly in Theme Builder
- Check that the data source exists (post has a featured image, custom field is filled, etc.)
- Ensure you clicked the Dynamic Content icon and selected a source
- Check the browser console for errors (F12)

### Wrong Data Displaying

- Verify you selected the correct data source
- Check that the post/item has content in that field
- Ensure the template is assigned to the right post type

### Global Variable Changes Don't Apply

- Clear your site's cache
- Ensure you saved the variable changes
- Check that modules are actually linked to the variable (not just using a static value)
- Verify the variable is used consistently across modules

### Custom Field Not Appearing in Dynamic Content Selector

- Verify Advanced Custom Fields is installed and activated
- Confirm the custom field is assigned to the correct post type
- Check that the field is set to show in the REST API (if using advanced ACF settings)
- Save and refresh the page

## Advanced Techniques

### Conditional Display with Dynamic Content

Some themes/plugins support conditional rules based on dynamic content values. Check if your plugin supports: "Display this module only if product price is greater than $100."

### Looping with Dynamic Content

Use the Loop Builder with dynamic content to create galleries that pull featured images, portfolios that pull project details, product grids that pull prices and descriptions.

### Combining Multiple Data Sources

Some modules support multiple dynamic content fields:

- Heading module: link title AND subtitle to different sources
- Image module: link image source and link URL
- Button module: link text AND URL

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 dynamic content exclusively. Divi 4 uses a different system.

## Related

- [Build Custom Loops using Loop Builder in Divi 5](../builder/build-custom-loops-using-loop-builder-in-divi-5.md)
- [Divi Library in Divi 5](../builder/divi-library-in-divi-5.md)
- [Theme Builder: Creating Custom Templates](../builder/build-custom-templates-using-the-theme-builder-in-divi-5.md)
