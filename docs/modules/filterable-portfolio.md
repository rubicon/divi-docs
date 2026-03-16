---
title: "Filterable Portfolio"
category: modules
tags: ["modules", "portfolio", "projects", "filterable", "grid", "categories", "dynamic-content"]
related: ["portfolio", "gallery", "blog"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10315331-the-filterable-portfolio-module-in-divi-5"
---

# Filterable Portfolio

The Filterable Portfolio module displays WordPress project posts in a sortable, category-based grid or fullwidth layout.

## Overview

The Filterable Portfolio module builds on the standard Portfolio module by adding interactive category filtering. Visitors can click category labels displayed above the portfolio grid to dynamically show or hide projects based on their assigned project categories. This makes it straightforward for users to browse large collections of work without navigating away from the page.

This module pulls content directly from the WordPress Projects custom post type that ships with Divi. Each project's featured image, title, and category metadata are rendered automatically, so there is no need to manually configure individual items. When you publish or update a project post, the Filterable Portfolio reflects those changes on the front end.

The Filterable Portfolio is well-suited for creative agencies, freelancers, and businesses that want to showcase categorized work samples, case studies, or product lines. It pairs naturally with dedicated project pages and can be combined with other layout modules to build full portfolio sections.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10315331-the-filterable-portfolio-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/filterable-portfolio/)

![Filterable Portfolio module](../assets/screenshots/modules/filterable-portfolio/element.png){ loading=lazy }
*The Filterable Portfolio module displaying project posts with category filter buttons.*

## Use Cases

1. **Agency Portfolio Page** — Display client work organized by service type (branding, web design, print) so visitors can filter to the category most relevant to their needs.

2. **Product Showcase** — Present a product catalog where customers can sort items by category, making it easy to browse specific product lines without leaving the page.

3. **Case Study Library** — Showcase business case studies filtered by industry or solution type, helping prospects quickly find examples relevant to their situation.

## How to Add the Filterable Portfolio Module

1. **Insert the module.** Open the Visual Builder, click the gray plus icon inside any row, and search for "Filterable Portfolio" in the module picker. Click it to add it to your layout.

2. **Configure your content.** In the Content tab, set the number of projects to display and select which project categories to include. Enable or disable the title, category labels, and pagination elements as needed.

3. **Style and publish.** Switch to the Design tab to choose between grid and fullwidth layouts, adjust overlay colors, customize typography for titles and filter labels, and fine-tune spacing. Save your layout when finished.

## Settings & Options

### Content Tab

The Content tab controls which project data appears and how the module links to other content.

| Setting | Type | Description |
|---------|------|-------------|
| **Content** | | |
| Number of Projects | number | Sets how many project posts are displayed in the portfolio grid. Accepts any positive integer. |
| Project Categories | multi-select | Filters which project categories are included. Leave empty to show all categories, or select specific ones to narrow the display. |
| **Elements** | | |
| Show Title | toggle | Controls whether the project title appears below each portfolio thumbnail. |
| Show Categories | toggle | Controls whether the category filter buttons appear above the portfolio grid. |
| Show Pagination | toggle | Enables or disables numbered pagination below the portfolio when the project count exceeds the per-page limit. |
| **Link** | | |
| Module Link URL | url | Wraps the entire module in a link to a specified URL, page, or section. |
| Module Link Target | select | Sets whether the module link opens in the same window or a new tab. |
| **Background** | | |
| Background Color | color | Applies a solid background color to the module container. |
| Background Gradient | gradient | Applies a gradient background with configurable direction, stops, and colors. |
| Background Image | image | Sets a background image behind the module content. |
| Background Video | video | Embeds a background video behind the module content. |
| Background Pattern | pattern | Adds a repeating pattern overlay to the module background. |
| Background Mask | mask | Applies a decorative mask shape to the module background. |
| **Meta** | | |
| Admin Label | text | Custom label displayed in the Visual Builder layers panel to help identify the module. |
| Disable On | toggle | Forces the module to remain visible in the Visual Builder even when front-end visibility is restricted. |

### Design Tab

The Design tab provides layout, typography, color, and visual effect controls for the portfolio display.

| Setting | Type | Description |
|---------|------|-------------|
| **Layout** | | |
| Layout | select | Switches between Grid (multi-column) and Fullwidth (single-column, full-width images) display modes. |
| **Overlay** | | |
| Overlay Icon | icon-picker | Selects the icon displayed when hovering over a portfolio thumbnail. |
| Overlay Icon Color | color | Sets the color of the hover overlay icon. |
| Hover Overlay Color | color | Sets the background color of the overlay that appears on thumbnail hover. |
| Hover Icon Picker | toggle | Enables or disables the icon displayed on hover. |
| **Image** | | |
| Image Rounded Corners | border-radius | Applies rounded corners to portfolio thumbnail images. |
| Image Border | border | Adds a border around each portfolio thumbnail image. |
| Image Box Shadow | box-shadow | Applies a shadow effect to portfolio thumbnail images. |
| Image CSS Filters | filters | Adjusts hue, saturation, brightness, contrast, invert, and sepia on images. |
| **Text** | | |
| Text Alignment | alignment | Sets the horizontal alignment of all text content within the module. |
| Text Color Scheme | select | Switches between dark and light text color presets for readability on different backgrounds. |
| **Title Text** | | |
| Title Font | font | Sets the font family for project titles. |
| Title Font Weight | select | Controls the boldness of project title text. |
| Title Font Style | toggle | Applies italic, uppercase, underline, or strikethrough to title text. |
| Title Text Color | color | Sets the color of project title text. |
| Title Text Size | range | Controls the font size of project titles. |
| Title Letter Spacing | range | Adjusts the spacing between characters in project titles. |
| Title Line Height | range | Sets the vertical spacing between lines in project titles. |
| Title Text Shadow | shadow | Applies a shadow effect to project title text. |
| **Filter Criteria Text** | | |
| Filter Font | font | Sets the font family for the category filter buttons. |
| Filter Font Weight | select | Controls the boldness of filter button text. |
| Filter Font Style | toggle | Applies italic, uppercase, underline, or strikethrough to filter text. |
| Filter Text Color | color | Sets the color of the category filter button labels. |
| Filter Text Size | range | Controls the font size of filter button labels. |
| Filter Letter Spacing | range | Adjusts character spacing in filter button labels. |
| Filter Line Height | range | Sets vertical spacing between lines in filter button text. |
| Filter Text Shadow | shadow | Applies a shadow effect to filter button text. |
| **Meta Text** | | |
| Meta Font | font | Sets the font family for project metadata text. |
| Meta Font Weight | select | Controls the boldness of metadata text. |
| Meta Font Style | toggle | Applies italic, uppercase, underline, or strikethrough to metadata. |
| Meta Text Color | color | Sets the color of project metadata text. |
| Meta Text Size | range | Controls the font size of metadata text. |
| Meta Letter Spacing | range | Adjusts character spacing in metadata text. |
| Meta Line Height | range | Sets vertical spacing between lines in metadata text. |
| Meta Text Shadow | shadow | Applies a shadow effect to metadata text. |
| **Pagination Text** | | |
| Pagination Font | font | Sets the font family for pagination links. |
| Pagination Font Weight | select | Controls the boldness of pagination text. |
| Pagination Font Style | toggle | Applies italic, uppercase, underline, or strikethrough to pagination text. |
| Pagination Text Color | color | Sets the color of pagination link text. |
| Pagination Text Size | range | Controls the font size of pagination links. |
| Pagination Letter Spacing | range | Adjusts character spacing in pagination links. |
| Pagination Line Height | range | Sets vertical spacing between lines in pagination text. |
| Pagination Text Shadow | shadow | Applies a shadow effect to pagination text. |
| **Sizing** | | |
| Width | range | Sets the horizontal width of the module. |
| Max Width | range | Sets the maximum horizontal width the module can reach. |
| Module Alignment | alignment | Controls the horizontal alignment of the module when its width is less than the column width. |
| Min Height | range | Sets the minimum height of the module container. |
| Height | range | Sets the exact height of the module container. |
| Max Height | range | Sets the maximum height the module container can reach. |
| **Spacing** | | |
| Margin | spacing | Controls the outer spacing around the module on all four sides. |
| Padding | spacing | Controls the inner spacing within the module on all four sides. |
| **Border** | | |
| Border Width | range | Sets the thickness of the module border. |
| Border Color | color | Sets the color of the module border. |
| Border Style | select | Chooses the border style (solid, dashed, dotted, double, groove, ridge, inset, outset). |
| Border Radius | border-radius | Rounds the corners of the module container. |
| **Box Shadow** | | |
| Box Shadow | box-shadow | Adds a shadow effect around the module with configurable blur, spread, color, and position. |
| **Filters** | | |
| Hue | range | Shifts the hue of the entire module. |
| Saturation | range | Adjusts the color saturation of the entire module. |
| Brightness | range | Controls the brightness level of the entire module. |
| Contrast | range | Adjusts the contrast of the entire module. |
| Invert | range | Inverts the colors of the entire module. |
| Sepia | range | Applies a sepia tone to the entire module. |
| Opacity | range | Controls the transparency of the entire module. |
| Blend Mode | select | Sets how the module blends with elements behind it. |
| **Transform** | | |
| Transform Scale | range | Scales the module up or down from its original size. |
| Transform Translate | range | Moves the module horizontally or vertically from its original position. |
| Transform Rotate | range | Rotates the module by a specified degree. |
| Transform Skew | range | Skews the module along the horizontal or vertical axis. |
| Transform Origin | select | Sets the reference point for all transform operations. |
| **Animation** | | |
| Animation Style | select | Chooses the entrance animation type (fade, slide, bounce, zoom, flip, fold, roll). |
| Animation Direction | select | Sets the direction from which the animation originates. |
| Animation Duration | range | Controls how long the entrance animation takes to complete. |
| Animation Delay | range | Sets a delay before the entrance animation begins. |
| Animation Intensity | range | Controls the intensity or distance of the animation effect. |
| Animation Starting Opacity | range | Sets the opacity at the beginning of the animation. |
| Animation Speed Curve | select | Defines the acceleration curve of the animation (ease, linear, ease-in, ease-out, ease-in-out). |
| Animation Repeat | toggle | Sets whether the animation plays once or loops continuously. |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

| Setting | Type | Description |
|---------|------|-------------|
| **Attributes** | | |
| CSS ID | text | Assigns a unique CSS ID to the module for targeted styling or anchor links. |
| CSS Classes | text | Adds one or more CSS class names to the module for custom styling. |
| Custom HTML Attributes | text | Adds custom `data-*` or other HTML attributes to the module wrapper element. |
| **CSS** | | |
| Main Element | code | Applies custom CSS rules directly to the module's main wrapper element. |
| Portfolio Title | code | Applies custom CSS rules to the project title elements. |
| Portfolio Post Meta | code | Applies custom CSS rules to the project metadata elements. |
| Portfolio Filters | code | Applies custom CSS rules to the category filter buttons. |
| Portfolio Pagination | code | Applies custom CSS rules to the pagination elements. |
| Portfolio Image | code | Applies custom CSS rules to the portfolio thumbnail images. |
| **HTML** | | |
| Semantic Tag | select | Sets the HTML element used for the module container (div, article, section, header, footer, aside, main). |
| **Conditions** | | |
| Display Conditions | conditions | Sets rules that determine when the module is visible, based on user role, page type, date, or custom logic. |
| **Interactions** | | |
| Module Interactions | interactions | Defines show, hide, or toggle behaviors triggered by clicks, hovers, or scroll events on other elements. |
| **Visibility** | | |
| Disable On | toggle | Hides the module on selected device types: desktop, tablet, or phone. |
| **Transitions** | | |
| Transition Duration | range | Sets how long hover-state property transitions take to complete. |
| Transition Delay | range | Sets a delay before hover-state transitions begin. |
| Transition Speed Curve | select | Defines the acceleration curve for hover transitions. |
| **Position** | | |
| Position | select | Sets the CSS position property (default/static, relative, absolute, fixed, sticky). |
| Z-Index | number | Controls the stacking order of the module relative to other positioned elements. |
| Horizontal Offset | range | Moves the module left or right from its positioned origin. |
| Vertical Offset | range | Moves the module up or down from its positioned origin. |
| **Scroll Effects** | | |
| Sticky Position | toggle | Makes the module stick to the viewport during scrolling. |
| Motion Effects - Vertical | toggle | Moves the module vertically at a different rate as the user scrolls. |
| Motion Effects - Horizontal | toggle | Moves the module horizontally as the user scrolls. |
| Motion Effects - Fade | toggle | Changes the module opacity as the user scrolls through the viewport. |
| Motion Effects - Scaling | toggle | Scales the module up or down as the user scrolls. |
| Motion Effects - Rotating | toggle | Rotates the module as the user scrolls. |
| Motion Effects - Blur | toggle | Applies or removes a blur effect as the user scrolls. |

## Code Examples

### Custom CSS

```css
/* Customize the category filter buttons */
.et_pb_filterable_portfolio .et_pb_portfolio_filters li a {
    background-color: #f5f5f5;
    border-radius: 4px;
    padding: 8px 16px;
    color: #333;
    transition: all 0.3s ease;
}

.et_pb_filterable_portfolio .et_pb_portfolio_filters li a:hover,
.et_pb_filterable_portfolio .et_pb_portfolio_filters li a.active {
    background-color: #2ea3f2;
    color: #fff;
}

/* Add a subtle hover effect to portfolio items */
.et_pb_filterable_portfolio .et_pb_portfolio_item {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.et_pb_filterable_portfolio .et_pb_portfolio_item:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

/* Responsive: stack to single column on mobile */
@media (max-width: 767px) {
    .et_pb_filterable_portfolio .et_pb_portfolio_item {
        width: 100% !important;
        margin-right: 0 !important;
    }
}
```

### PHP Hooks

```php
/* Modify the Filterable Portfolio module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_filterable_portfolio' !== $render_slug) {
        return $output;
    }

    // Example: Add a wrapper div with a custom class
    $output = '<div class="custom-portfolio-wrapper">' . $output . '</div>';

    return $output;
}, 10, 2);
```

```php
/* Change the number of projects per page for filterable portfolios */
add_filter('pre_get_posts', function($query) {
    if (!is_admin() && $query->get('post_type') === 'project') {
        $query->set('posts_per_page', 12);
    }
});
```

## Common Patterns

1. **Category-Filtered Services Page** — Place a Filterable Portfolio in a fullwidth row on a services page. Create project categories that match your service offerings (e.g., "Web Design", "SEO", "Branding"). Visitors can click each category to view only relevant work samples, creating an interactive browsing experience without custom code.

2. **Grid Portfolio with Custom Overlay** — Use the grid layout with a custom overlay icon and branded overlay color. Set the overlay color to match your brand palette with reduced opacity so the thumbnail remains partially visible on hover. Adjust the title and meta typography to complement your site's design system.

3. **Paginated Project Archive** — Enable pagination and set a conservative project count (6 or 9) to keep page load times fast when you have a large number of projects. Combine with a heading module above the portfolio to provide context, and style the pagination text to match your navigation design.

## Saving Your Work

After configuring the Filterable Portfolio module, save your layout by clicking the green **Save** button at the bottom of the Visual Builder panel, or use the keyboard shortcut **Ctrl+S** (Windows) / **Cmd+S** (Mac). To reuse this configured module on other pages, right-click the module in the Visual Builder and select **Save to Library**. You can also copy and paste modules between pages using **Ctrl+C** / **Ctrl+V**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Filterable Portfolio module in Divi 5 uses the updated Visual Builder interface with the accordion-style settings panel. Settings organization and naming may differ from Divi 4.

## Troubleshooting

!!! warning "No Projects Appearing"
    If the Filterable Portfolio displays nothing, verify that you have published project posts under **Projects** in the WordPress admin. The module pulls from the Projects custom post type, so standard posts and pages will not appear. Also confirm that each project has a featured image assigned and belongs to at least one project category.

!!! warning "Category Filters Not Showing"
    If the filter buttons are missing above the portfolio, check that the **Show Categories** toggle is enabled in the Content tab under Elements. Also ensure your projects are assigned to more than one category, as the filter is less useful with a single category and may not render if only one exists.

!!! tip "Slow Loading with Many Projects"
    If the portfolio is slow to load or causes layout shifts, reduce the **Number of Projects** setting and enable **Pagination**. Large project counts force the module to load all thumbnails at once, which impacts performance. Consider optimizing your project featured images to web-appropriate sizes (1200px wide maximum) before uploading.

## Related

- [Portfolio](portfolio.md)
- [Gallery](gallery.md)
- [Blog](blog.md)
