---
title: "Menu"
category: modules
tags: ["modules", "navigation", "menu", "header", "logo", "dropdown", "mobile-menu", "search", "cart"]
related: ["fullwidth-menu", "sidebar"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10353582-the-menu-module-in-divi-5"
---

# Menu

The Menu module displays a WordPress navigation menu with optional logo, search icon, and shopping cart icon within Divi 5 layouts.

## Overview

The Menu module brings your WordPress navigation menus directly into any Divi 5 layout. Unlike the header-specific Fullwidth Menu, this standard-width module can be placed inside any section, row, or column, giving you the flexibility to add navigation wherever it is needed on a page. It pulls from menus you have already created in WordPress under Appearance > Menus, so any changes to your menu structure are reflected automatically.

Beyond simple link lists, the Menu module supports a site logo, a search icon, and a WooCommerce shopping cart icon, making it a compact yet powerful navigation hub. The dropdown system handles multi-level menus gracefully, with dedicated styling controls for submenu appearance, active link highlighting, and mobile hamburger behavior.

Because the module works at the row level rather than as a global header element, it is especially useful for building custom landing page headers, in-page navigation bars, or secondary menus within sidebar columns. Combined with Divi 5's conditions and visibility settings, you can tailor which menus appear on which pages and devices without any code.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10353582-the-menu-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/menu/)

![Menu module](../assets/screenshots/modules/menu/element.png){ loading=lazy }
*The Menu module as it appears on the live demo.*

## Use Cases

1. **Custom Landing Page Header** — Place the Menu module at the top of a landing page inside a regular section to create a page-specific navigation bar that differs from the global site header, allowing you to limit links to only the most relevant destinations.

2. **Secondary In-Page Navigation** — Add the module partway down a long page to provide anchor-link navigation that helps visitors jump between content sections without scrolling back to the top.

3. **Sidebar Navigation Menu** — Insert the Menu module into a sidebar column to give blog posts or documentation pages a persistent category or topic menu that supplements the primary site navigation.

## How to Add the Menu Module

1. **Open the Visual Builder** on the page where you want the menu. Click the gray plus icon inside a row to open the module picker, then search for "Menu" and click to insert it.

2. **Select a WordPress menu** from the Content dropdown in the Content tab. If you have not yet created a menu, go to Appearance > Menus in the WordPress dashboard and build one first.

3. **Configure appearance and behavior** using the Design tab to adjust text styling, dropdown colors, icon sizing, and logo appearance. Save or publish your page when finished.

## Settings & Options

### Content Tab

The Content tab controls which menu is displayed, whether a logo and utility icons appear, and how the module links to other content.

| Setting | Type | Description |
|---------|------|-------------|
| **Content** | select | Choose which WordPress menu to display from the list of menus registered on your site |
| **Logo** | image upload | Set a logo image that appears alongside the menu links |
| **Elements — Shopping Cart Icon** | toggle | Show or hide the WooCommerce shopping cart icon in the menu bar |
| **Elements — Search Icon** | toggle | Show or hide the search icon that opens an inline search field |
| **Link** | URL / toggle | Make the entire module a clickable link and configure the destination URL, target, and rel attributes |
| **Background** | composite | Set background color, gradient, image, or video behind the module |
| **Loop** | toggle | Enable the Loop Builder to display the module dynamically within loop templates |
| **Order** | number | Set the display order of the module when placed inside a Flexbox or CSS Grid layout |
| **Meta — Label** | text | Assign a label for identification inside the Visual Builder layer panel |
| **Meta — Force Visibility** | toggle | Keep the module visible in the Visual Builder even when conditions would otherwise hide it |

### Design Tab

The Design tab provides granular control over layout direction, typography, dropdown styling, icon appearance, logo treatment, and all standard visual properties.

| Setting | Type | Description |
|---------|------|-------------|
| **Layout — Style** | select | Choose the overall menu layout style, such as horizontal or vertical orientation |
| **Layout — Dropdown Direction** | select | Set whether dropdown submenus open downward, upward, or to the side |
| **Menu Text — Font** | font picker | Select the font family for top-level menu links |
| **Menu Text — Font Weight** | select | Set the weight (light, regular, bold, etc.) of menu link text |
| **Menu Text — Font Style** | toggles | Apply italic, uppercase, underline, or strikethrough to menu text |
| **Menu Text — Text Color** | color | Set the default color for top-level menu links |
| **Menu Text — Text Size** | range | Adjust the font size of menu link text with responsive controls |
| **Menu Text — Letter Spacing** | range | Control the spacing between individual characters in menu links |
| **Menu Text — Line Height** | range | Set the vertical line height for menu link text |
| **Menu Text — Text Shadow** | composite | Apply a shadow effect behind menu link text |
| **Dropdown Menu — Line Color** | color | Set the color of separator lines between dropdown menu items |
| **Dropdown Menu — Text Color** | color | Choose the text color for items inside dropdown submenus |
| **Dropdown Menu — Active Link Color** | color | Set the color applied to the currently active link in a dropdown |
| **Dropdown Menu — Mobile Background Color** | color | Specify the background color for the mobile hamburger menu panel |
| **Icons — Shopping Cart Color** | color | Set the color of the shopping cart icon |
| **Icons — Search Icon Color** | color | Set the color of the search icon |
| **Icons — Hamburger Menu Icon Color** | color | Set the color of the mobile hamburger menu toggle icon |
| **Icons — Font Size** | range | Adjust the size of all menu utility icons |
| **Logo — Border Radius** | range | Round the corners of the logo image |
| **Logo — Border Styles** | composite | Add border width, style, and color around the logo |
| **Logo — Box Shadow** | composite | Apply a shadow beneath or around the logo image |
| **Logo — Image Filters** | composite | Adjust hue, saturation, brightness, contrast, invert, sepia, and opacity on the logo |
| **Sizing — Width** | range | Set the width of the module |
| **Sizing — Max Width** | range | Define the maximum width the module can reach |
| **Sizing — Min Height** | range | Set a minimum height for the module container |
| **Sizing — Height** | range | Set an explicit height for the module |
| **Sizing — Alignment** | select | Align the module to the left, center, or right within its parent |
| **Spacing — Margin** | range (4 sides) | Add space outside the module on each side |
| **Spacing — Padding** | range (4 sides) | Add space inside the module on each side |
| **Border — Border Width** | range | Set the width of the module border |
| **Border — Border Color** | color | Choose the color for the module border |
| **Border — Border Style** | select | Pick a border style such as solid, dashed, or dotted |
| **Border — Border Radius** | range | Round the corners of the module container |
| **Box Shadow** | composite | Add a shadow effect beneath or around the entire module |
| **Filters — Hue** | range | Shift the hue of the module content |
| **Filters — Saturation** | range | Adjust color saturation |
| **Filters — Brightness** | range | Increase or decrease brightness |
| **Filters — Contrast** | range | Adjust contrast levels |
| **Filters — Invert** | range | Invert the colors of the module |
| **Filters — Sepia** | range | Apply a sepia tone |
| **Filters — Opacity** | range | Control overall opacity |
| **Filters — Blur** | range | Apply a blur effect |
| **Filters — Blend Mode** | select | Set how the module blends with elements behind it |
| **Transform — Scale** | range | Scale the module up or down |
| **Transform — Translate** | range | Move the module along the X and Y axes |
| **Transform — Rotate** | range | Rotate the module by a specified number of degrees |
| **Transform — Skew** | range | Skew the module along the X and Y axes |
| **Transform — Origin** | select | Set the transformation origin point |
| **Animation — Style** | select | Choose an entrance animation such as fade, slide, bounce, or zoom |
| **Animation — Direction** | select | Set the direction from which the animation enters |
| **Animation — Duration** | range | Control how long the animation takes to complete |
| **Animation — Delay** | range | Set a delay before the animation begins |
| **Animation — Intensity** | range | Adjust the strength or distance of the animation effect |
| **Animation — Starting Opacity** | range | Set the opacity at the start of the animation |
| **Animation — Speed Curve** | select | Choose an easing curve such as ease-in, ease-out, or linear |
| **Animation — Repeat** | toggle | Set whether the animation plays once or loops |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, scroll-driven effects, and positioning.

| Setting | Type | Description |
|---------|------|-------------|
| **Attributes — CSS ID** | text | Assign a unique CSS ID to the module for targeting with styles or JavaScript |
| **Attributes — CSS Classes** | text | Add one or more CSS classes, separated by spaces |
| **Attributes — Custom HTML Attributes** | repeater | Add custom data attributes or other HTML attributes to the module wrapper |
| **CSS — Custom CSS** | code editor | Write CSS rules that apply to specific internal elements of the module |
| **HTML — Semantic Tag** | select | Choose the HTML element tag (div, nav, section, etc.) used for the module wrapper |
| **Conditions** | rule builder | Define conditions under which the module is displayed, such as user role, page type, or custom field values |
| **Interactions** | action builder | Create interactions that trigger show, hide, or toggle effects on other elements |
| **Visibility — Disable On** | checkboxes | Hide the module on desktop, tablet, or phone viewports |
| **Transitions — Duration** | range | Set the duration of hover and state transition animations |
| **Transitions — Delay** | range | Add a delay before transitions begin |
| **Transitions — Speed Curve** | select | Choose the easing function for transitions |
| **Position — Position** | select | Set positioning mode: default (static), relative, absolute, or fixed |
| **Position — Offsets** | range (4 sides) | Define top, right, bottom, and left offset values for positioned modules |
| **Position — Z-Index** | number | Control the stacking order relative to other positioned elements |
| **Scroll Effects — Vertical Motion** | composite | Move the module vertically as the user scrolls |
| **Scroll Effects — Horizontal Motion** | composite | Move the module horizontally on scroll |
| **Scroll Effects — Fade In/Out** | composite | Fade the module in or out based on scroll position |
| **Scroll Effects — Scaling** | composite | Scale the module up or down as the page scrolls |
| **Scroll Effects — Rotating** | composite | Rotate the module in response to scrolling |
| **Scroll Effects — Blur** | composite | Apply or remove a blur effect based on scroll position |

## Code Examples

### Custom CSS

```css
/* Restyle the menu links for a dark navigation bar */
.et_pb_menu .et-menu-nav li a {
    color: #ffffff;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Highlight the active menu item */
.et_pb_menu .et-menu-nav li.current-menu-item a {
    color: #ff6b35;
    border-bottom: 2px solid #ff6b35;
}

/* Style the dropdown submenus */
.et_pb_menu .et-menu-nav li ul.sub-menu {
    background-color: #1a1a2e;
    border-radius: 4px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Responsive mobile hamburger menu adjustments */
@media (max-width: 980px) {
    .et_pb_menu .et_mobile_menu {
        background-color: #1a1a2e;
        padding: 20px;
    }

    .et_pb_menu .et_mobile_menu li a {
        color: #ffffff;
        padding: 10px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
}
```

### PHP Hooks

```php
/* Filter the Menu module output to add a custom wrapper */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_menu' !== $render_slug) {
        return $output;
    }
    // Wrap the menu in a sticky container
    return '<div class="custom-sticky-menu-wrapper">' . $output . '</div>';
}, 10, 2);
```

## Common Patterns

1. **Sticky Landing Page Header** — Place the Menu module inside a specialty section at the top of a page, enable the logo and search icon, then use the Advanced tab's Position setting to make it fixed. This creates a persistent navigation bar that follows the user as they scroll through long-form content.

2. **WooCommerce-Ready Navigation** — Enable both the shopping cart icon and search icon in the Elements toggle group to build a retail-friendly menu bar. Style the cart icon with a brand accent color so it draws attention, and pair the module with a sidebar filter menu on shop archive pages.

3. **Multilingual Menu Switcher** — Use Divi 5 conditions to show different Menu modules depending on the visitor's language or locale. Assign each module a different WordPress menu that contains translated page links, giving multilingual sites a seamless switching experience without plugins.

## Saving Your Work

After configuring the Menu module to your liking, click the green **Save** button at the bottom of the Visual Builder page settings bar. For layouts you plan to reuse, right-click the module and choose **Save to Library** to store it as a reusable element. You can also save the entire page layout to the Divi Library for use on other pages across your site.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Menu module in Divi 5 uses the updated options framework with Flexbox and Grid support, conditions, interactions, and scroll effects that are not available in Divi 4. If you are still running Divi 4, refer to the legacy Elegant Themes documentation.

## Troubleshooting

!!! warning "Menu Not Displaying Any Links"
    If the Menu module appears empty with no navigation links, verify that you have selected a valid WordPress menu from the Content dropdown. Go to Appearance > Menus in the WordPress dashboard and confirm that the menu exists and has items assigned to it. Also check that the menu is not restricted to a specific theme location that conflicts with the module placement.

!!! warning "Dropdown Submenus Not Appearing"
    If your multi-level menu does not show dropdown submenus on hover, ensure that the parent menu items in WordPress have child items indented beneath them. In the Design tab, check that the Dropdown Direction setting is configured correctly and that no custom CSS is setting `display: none` or `overflow: hidden` on the submenu containers.

!!! warning "Mobile Hamburger Menu Not Opening"
    If the hamburger icon appears on smaller screens but tapping it does not open the mobile menu, look for JavaScript conflicts caused by other plugins. Open your browser's developer console and check for errors. Also verify that the module's Visibility settings have not disabled it on the device you are testing, and confirm that no Interactions rules are interfering with the toggle behavior.

## Related

- [Fullwidth Menu](fullwidth-menu.md)
- [Sidebar](sidebar.md)
