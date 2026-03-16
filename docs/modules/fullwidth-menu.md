---
title: "Fullwidth Menu"
category: modules
tags: ["modules", "fullwidth", "menu", "navigation", "header", "links", "search", "logo"]
related: ["menu", "sidebar"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://www.elegantthemes.com/documentation/divi/fullwidth-menu/"
---

# Fullwidth Menu

The Fullwidth Menu module displays a WordPress navigation menu that spans the entire width of a fullwidth section, with optional logo, search, and cart icons.

## Overview

The Fullwidth Menu module places a complete navigation menu inside a fullwidth section, stretching the menu bar from edge to edge. It pulls from any WordPress menu you have created under Appearance > Menus, and presents the links in a horizontal bar with dropdown support for nested menu items. The module also supports an optional logo image, a search icon, and a WooCommerce shopping cart icon.

This module is the fullwidth counterpart of the standard [Menu](menu.md) module. While both share the same settings and functionality, the Fullwidth Menu is designed exclusively for fullwidth sections and takes advantage of the extra horizontal space. It is particularly useful for building custom header areas within the Divi 5 Theme Builder, creating secondary navigation bars on long-form pages, or adding persistent site-wide navigation that is visually distinct from the primary theme header.

On smaller screens, the horizontal menu items automatically collapse into a mobile-friendly hamburger menu. The dropdown menu behavior, icon styling, and mobile breakpoint are all configurable through the module's settings, giving you full control over the navigation experience across all devices.

For additional reference, see the [official Elegant Themes documentation for the Menu module](https://help.elegantthemes.com/en/articles/10353582-the-menu-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/fullwidth-menu/)

![Fullwidth Menu module](../assets/screenshots/modules/fullwidth-menu/element.png){ loading=lazy }
*The Fullwidth Menu module displaying a horizontal navigation bar with logo and menu links.*

## Use Cases

1. **Custom Theme Builder Header** — Use the Fullwidth Menu module in a Divi 5 Theme Builder header template to create a branded navigation bar with your logo, primary menu links, a search icon, and a WooCommerce cart icon, all spanning the full browser width.

2. **Secondary Page Navigation** — Add a Fullwidth Menu below the main header on long-form pages like documentation or resource centers, providing a persistent second-level navigation that links to page sections or related pages within a category.

3. **Footer Navigation Bar** — Place a Fullwidth Menu in a fullwidth section near the bottom of the page to present a streamlined set of important links (privacy policy, terms, sitemap, contact) in a compact horizontal bar that complements the main footer area.

## How to Add the Fullwidth Menu Module

1. Open the Visual Builder and ensure the page has a fullwidth section. If needed, click the blue **+** icon and select **Fullwidth** as the section type.

2. Click the gray **+** icon inside the fullwidth section to open the module picker.

3. Search for "Fullwidth Menu" or browse the Fullwidth Modules category, then click to insert it into the section.

## Settings & Options

The Fullwidth Menu module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which menu is displayed, the logo image, optional utility icons, and background styling.

| Setting | Type | Description |
|---------|------|-------------|
| Content | select | Choose which WordPress menu to display. Lists all menus created under Appearance > Menus. If no menus exist, you will need to create one in the WordPress admin first. |
| Logo | image upload | Upload or select a logo image to display alongside the menu. The logo appears on the left side of the menu bar (or centered, depending on layout). Useful for branding in secondary navigation bars or Theme Builder headers. |
| Elements | toggle checkboxes | Control visibility of optional utility icons: **Shopping Cart** (requires WooCommerce to be active) and **Search Icon** (adds a click-to-expand search field in the menu bar). |
| Link | url | Make the entire module clickable, redirecting users to another page, section, or external URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the menu module. Useful for creating a visually distinct navigation bar that stands out from the page content. |
| Loop | toggle | Enable the Loop Builder to dynamically generate menu content from posts or other data sources. |
| Order | select | Control the display order of the module when placed inside a Flexbox or CSS Grid layout container. |
| Meta | admin label | Set a custom label to identify the module in the Visual Builder's layer panel. Includes a toggle to force visibility in the builder. |

### Design Tab

The Design tab controls the menu layout, typography, dropdown styling, icon appearance, and all visual presentation options.

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose the menu bar style: **Left Aligned** (logo left, links right), **Centered** (links centered below or beside logo), or **Inline Centered Logo** (logo centered between two groups of links). Also set the dropdown menu direction (downward or upward). |
| Menu Text | text styling | Configure the typography for top-level menu items: font family, weight, size, color, letter spacing, line height, and text transform. Supports separate hover state colors. |
| Dropdown Menu | color/style controls | Customize the dropdown sub-menu appearance: line color (separator between items), text color, active link color, and mobile menu background color. |
| Icons | color/size controls | Style the optional utility icons: Shopping Cart icon color and size, Search icon color and size, and Hamburger menu icon color and size. Each icon can be styled independently. |
| Logo | image styling | Configure styling for the logo image including border radius, border styles, box shadow, and image filters (brightness, contrast, saturation, etc.). |
| Sizing | dimensions | Control the module's width, max-width, and height. |
| Spacing | margin/padding | Set margin and padding values for the module container. Supports responsive values per device breakpoint. |
| Border | border controls | Add borders around the module with customizable width, color, style, and border radius for rounded corners. |
| Box Shadow | shadow controls | Apply a box shadow with configurable color, horizontal/vertical offset, blur radius, and spread to create depth and separation from surrounding content. |
| Filters | CSS filters | Apply visual filter effects such as brightness, contrast, saturation, hue rotation, blur, and invert. Includes blend mode selection. |
| Transform | transform controls | Apply CSS transforms including scale, translate, rotate, skew, and transform origin for advanced positioning effects. |
| Animation | animation select | Choose an entrance animation (fade, slide, bounce, zoom, flip, fold, roll) with configurable duration, delay, intensity, and starting opacity. |

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, and interaction behavior.

| Setting | Type | Description |
|---------|------|-------------|
| Attributes | text fields | Assign a CSS ID and CSS classes to the module for targeting with custom styles or JavaScript. Also supports custom HTML data attributes. |
| CSS | code editor | Write custom CSS that applies directly to specific internal elements of the module (menu container, links, dropdowns, logo, icons, etc.). |
| HTML | tag select | Choose the semantic HTML tag used for the module's wrapper element (div, nav, header, etc.). Using `nav` is recommended for accessibility. |
| Conditions | condition builder | Set display conditions so the module only renders when specific rules are met, such as user role, page type, date range, or custom logic. |
| Interactions | interaction builder | Define hover, click, or scroll-triggered interactions that affect this module or other elements on the page. |
| Visibility | device toggles | Show or hide the module on desktop, tablet, and/or phone. Hidden modules are not rendered in the page source for that breakpoint. |
| Transitions | transition controls | Configure CSS transition duration and easing function for smooth hover state changes on menu items, dropdowns, and icons. |
| Position | position controls | Set the CSS position property (relative, absolute, fixed, sticky) and offset values (top, right, bottom, left, z-index). Using **sticky** keeps the menu visible as visitors scroll. |
| Scroll Effects | scroll controls | Apply scroll-driven effects like parallax, fade, scale, rotate, blur, or horizontal movement as the user scrolls past the module. |

## Code Examples

### Custom CSS

```css
/* Style the Fullwidth Menu bar background and spacing */
.et_pb_fullwidth_menu {
    background-color: #1a1a2e;
    padding: 0 30px;
}

/* Style top-level menu links */
.et_pb_fullwidth_menu .et-menu a {
    color: #ffffff;
    font-size: 15px;
    font-weight: 500;
    padding: 20px 16px;
    transition: color 0.3s ease;
}

/* Hover state for menu links */
.et_pb_fullwidth_menu .et-menu a:hover {
    color: #e94560;
}

/* Style the dropdown sub-menus */
.et_pb_fullwidth_menu .et-menu .sub-menu {
    background-color: #16213e;
    border-top: 2px solid #e94560;
    min-width: 220px;
}

.et_pb_fullwidth_menu .et-menu .sub-menu a {
    color: #cccccc;
    font-size: 14px;
    padding: 12px 20px;
}

.et_pb_fullwidth_menu .et-menu .sub-menu a:hover {
    color: #ffffff;
    background-color: #0f3460;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_fullwidth_menu {
        padding: 10px 15px;
    }
}
```

### PHP Hooks

```php
/* Filter the Fullwidth Menu module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_fullwidth_menu' !== $render_slug) {
        return $output;
    }
    // Example: Add a custom class based on the current page
    if (is_front_page()) {
        $output = str_replace(
            'et_pb_fullwidth_menu',
            'et_pb_fullwidth_menu home-menu',
            $output
        );
    }
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Sticky Secondary Navigation** — Place the Fullwidth Menu in a fullwidth section and set the Position to **sticky** with a top offset of 0 in the Advanced tab. Choose a solid background color and add a subtle box shadow so the menu bar floats above the content as visitors scroll, providing persistent access to key page sections.

2. **Branded Header with Logo and Utility Icons** — Select the **Inline Centered Logo** layout to place the logo between two groups of menu links. Enable both the Search and Shopping Cart elements for a complete e-commerce header. Style the menu text in white against a dark background and set the icon colors to match for a cohesive branded appearance.

3. **Minimal Footer Navigation** — Add a Fullwidth Menu near the bottom of the page with a centered layout, a simple WordPress menu containing legal and utility links, and no logo or icons. Use a smaller font size and muted text colors to create a clean, understated navigation bar that complements rather than competes with the primary footer content.

## Saving Your Work

After configuring the Fullwidth Menu:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Menu Shows No Links"
    If the module appears but displays no navigation links, verify that you have selected a valid WordPress menu in the Content tab's Content dropdown. If no menus appear in the dropdown, go to **Appearance > Menus** in the WordPress admin and create a menu with at least one item before returning to the builder.

!!! warning "Shopping Cart Icon Not Appearing"
    The Shopping Cart toggle in the Elements settings requires WooCommerce to be installed and active. If WooCommerce is not detected, the cart icon will not display regardless of the toggle state. Verify that WooCommerce is installed, activated, and up to date.

!!! tip "Dropdown Menus Hidden Behind Other Content"
    If dropdown sub-menus appear behind other modules or sections on the page, the issue is typically a z-index conflict. Add a higher z-index value to the Fullwidth Menu module using the Position settings in the Advanced tab, or add custom CSS: `.et_pb_fullwidth_menu { z-index: 999; }`.

## Related

- [Menu](menu.md) — Standard-width version for use within regular sections and rows
- [Sidebar](sidebar.md) — Widget-based navigation for sidebars and auxiliary content areas
