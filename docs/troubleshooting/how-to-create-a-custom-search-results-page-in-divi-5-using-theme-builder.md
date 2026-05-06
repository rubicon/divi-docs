---
title: "How to Create a Custom Search Results Page in Divi 5 Using Theme Builder"
category: troubleshooting
tags: ["troubleshooting", "theme-builder", "search", "templates", "dynamic-content"]
related: ["build-custom-templates-using-the-theme-builder-in-divi-5.md", "getting-started-with-divi-5-theme-builder.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14085106-how-to-create-a-custom-search-results-page-in-divi-5-using-theme-builder"
---

# How to Create a Custom Search Results Page in Divi 5 Using Theme Builder

By default, WordPress displays search results in a plain, unstyled list. With Divi 5's Theme Builder, you can create a custom search results page that matches your site's design and improves the user experience.

## Overview

Divi 5 lets you design search results pages using the Theme Builder's dynamic content features. You can add a custom heading, control result layout with the Blog module, and apply your site's styling to create a cohesive experience.

## Prerequisites

- Divi 5 installed and activated
- Access to **Divi** → **Theme Builder** in the WordPress dashboard
- Visual Builder enabled for your site's post types
- Basic familiarity with modules (Heading, Blog, etc.)

## Step 1: Create a Search Results Template

1. In your WordPress dashboard, go to **Divi** → **Theme Builder**
2. Click **Add New Template** button at the top
3. A new template creation dialog appears
4. Select **Search Results** from the template type list
5. Give your template a name (e.g., "Custom Search Results") — this is for internal reference only
6. Click **Build New Template** or **Create** to proceed to the builder

The Theme Builder now opens with a blank canvas for your search results template.

## Step 2: Add a Heading Module

1. In the builder, add a new **Row** at the top of the template (if not already present)
2. Add a **Heading** module to the first section
3. Click on the **Heading** module settings
4. In the **Content** tab, locate the **Heading text** field
5. Click the **Dynamic Content** icon (lightning bolt or dynamic data symbol) next to the heading input
6. From the dropdown menu, select **Post/Archive Title** (this dynamically displays "Search Results for [term]")
7. Style the heading as desired (font, size, color) in the **Design** tab
8. Click **Save** on the module

## Step 3: Add a Blog Module to Display Results

1. Below the heading, add another **Row** (if needed)
2. Add a **Blog** module to this row
3. Click on the **Blog** module settings
4. In the **Content** tab:
   - Locate the **Posts For Current Page** option
   - **Enable** this option (toggle it on)
   - This tells the module to display the search results instead of a hardcoded post list
5. Configure the Blog module layout:
   - Choose a layout style (Grid, List, Carousel, Masonry, etc.)
   - Set the **Number of Posts Per Page** (typically 10-20)
   - Decide whether to show featured image, excerpt, date, author, etc.
6. In the **Design** tab, style the blog module to match your site:
   - Set column width and spacing
   - Adjust card styling, borders, shadows
   - Configure hover effects (if desired)
7. Click **Save** on the module

## Step 4: Add Additional Elements (Optional)

You can customize further by adding:

### Search Filter/Refinement

- Add a **Search** module above the Blog module to let users refine their search
- Style it to match your site's design

### Sidebar

- Add modules to a sidebar column (Categories, Recent Posts, Search widget)
- This is common on search results pages

### Custom Message for No Results

- Some themes allow conditional display of "No results found" messages
- Use text modules to provide helpful guidance when search returns nothing

### Call-to-Action

- Add a CTA section below results offering further navigation options
- Example: "Didn't find what you're looking for? Browse our knowledge base" with a link

## Step 5: Save Your Template

1. In the Visual Builder toolbar, click **Save** (or press **Ctrl+S** / **Cmd+S**)
2. A confirmation appears: "Template saved successfully"
3. Click **Exit** to close the Visual Builder

Your custom search results template is now active. Any search on your site will display using this template.

## Testing Your Search Results Page

1. Visit your website's homepage
2. Use the search function (search bar in header/footer)
3. Search for a common term that exists on your site (e.g., a post category name or word from a post title)
4. The search results should display using your custom template
5. Verify:
   - The heading displays "Search Results for [term]"
   - The Blog module shows relevant posts
   - Styling matches the rest of your site
   - Click links work correctly

## Example: Blog-Style Search Results Template

Here's a typical structure for a blog-focused search results page:

```
┌─────────────────────────┐
│   Site Header           │ (Editable Theme Builder area)
├─────────────────────────┤
│  Search Results for     │ (Heading with dynamic content)
│  "WordPress Design"     │
├─────────────────────────┤
│ [Search Box]            │ (Optional refinement)
├─────────────────────────┤
│  Result 1  │  Result 2  │ (Blog module in 2-column grid)
│  [Image]   │  [Image]   │
│  Title     │  Title     │
│  Excerpt   │  Excerpt   │
│  Read More │  Read More │
├─────────────────────────┤
│  Result 3  │  Result 4  │
│  ...       │  ...       │
├─────────────────────────┤
│   Pagination (1 2 3 >)  │
├─────────────────────────┤
│   Site Footer           │ (Editable Theme Builder area)
└─────────────────────────┘
```

## Troubleshooting

!!! warning "Search Results Show Default WordPress Style, Not Custom Template"
    **Cause:** The search results template is not assigned or the post type integration is disabled.
    
    **Solution:** 
    - Verify the Search Results template is created in Theme Builder
    - Check **Divi** → **Theme Options** → **Builder** → **Post Type Integration**
    - Ensure Visual Builder is enabled for your site
    - Clear your browser cache and perform a fresh search

!!! warning "Dynamic Content Icon Not Appearing for Post/Archive Title"
    **Cause:** Your Divi version may not support dynamic content, or the module type doesn't support it.
    
    **Solution:** 
    - Ensure you're on Divi 5.0 or later
    - Try using the Heading module instead of Text module
    - Clear the browser cache and reload the builder

!!! warning "Blog Module Shows All Posts Instead of Search Results"
    **Cause:** The **Posts For Current Page** option is not enabled.
    
    **Solution:** 
    - Open the Blog module settings
    - Go to **Content** tab
    - Find **Posts For Current Page** and **enable** it
    - Save the module

!!! warning "Pagination Not Working on Search Results"
    **Cause:** The Blog module's pagination setting may be disabled.
    
    **Solution:** 
    - Open the Blog module settings
    - Ensure **Show Pagination** is enabled in the Content tab
    - Set pagination type (standard, load more, infinite scroll) as desired
    - Save and test

!!! warning "Search Results Template Not Triggering for Certain Searches"
    **Cause:** Empty searches or special characters may bypass the template.
    
    **Solution:** 
    - WordPress may not trigger search template for very broad or empty queries
    - Test with a clear search term
    - Check WordPress search settings in **Settings** → **Reading** if needed

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior. The specific template type and dynamic content features described here are exclusive to Divi 5. Divi 4 search results customization works differently.

## Related

- [Build Custom Templates Using the Theme Builder in Divi 5](../builder/build-custom-templates-using-the-theme-builder-in-divi-5.md)
- [Getting Started with Divi 5 Theme Builder](../builder/getting-started-with-divi-5-theme-builder.md)
- [Dynamic Content in Divi 5](../builder/advanced-content-management-using-dynamic-content-in-divi-5.md)
- [Blog Module Guide](../modules/blog.md)
