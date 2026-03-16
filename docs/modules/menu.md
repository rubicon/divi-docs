---
title: "Menu"
description: "Complete Divi 5 Menu module reference — WordPress nav menus, logo, search, cart icon, dropdown styling, and mobile menu setup."
category: modules
tags: ["modules", "navigation", "menu", "header", "logo", "dropdown", "mobile-menu", "search", "cart"]
related: ["fullwidth-menu", "sidebar"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10353582-the-menu-module-in-divi-5"
---

# Menu

The Menu module displays a WordPress navigation menu with optional logo, search icon, and shopping cart icon within Divi 5 layouts.

!!! abstract "Quick Reference"
    **What it does:** Renders a WordPress navigation menu with optional logo, search, and WooCommerce cart icons.
    **When to use it:** Custom landing page headers, secondary in-page navigation, sidebar menus
    **Key settings:** Content (menu select), Logo, Search Icon, Shopping Cart Icon, Dropdown Direction
    **Block identifier:** `divi/menu`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10353582-the-menu-module-in-divi-5)

!!! tip "When to Use This Module"
    - Building a page-specific navigation bar that differs from the global header
    - Adding secondary or sidebar navigation within content areas
    - Creating a navigation bar with integrated logo, search, and cart icons

!!! warning "When NOT to Use This Module"
    - Building a full-width site-wide header navigation → use [Fullwidth Menu](fullwidth-menu.md)
    - Displaying a WordPress widget area with nav widgets → use [Sidebar](sidebar.md)

## Overview

The Menu module brings your WordPress navigation menus directly into any Divi 5 layout. Unlike the header-specific [Fullwidth Menu](fullwidth-menu.md), this standard-width module can be placed inside any section, row, or column, giving you the flexibility to add navigation wherever it is needed on a page. It pulls from menus you have already created in WordPress under Appearance > Menus, so any changes to your menu structure are reflected automatically.

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

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout — Style | select | Choose the overall menu layout style, such as horizontal or vertical orientation |
| Layout — Dropdown Direction | select | Set whether dropdown submenus open downward, upward, or to the side |
| Menu Text | text styling | Font, weight, style, color, size, letter spacing, line height, and text shadow for top-level menu links |
| Dropdown Menu | color/style controls | Line color, text color, active link color, and mobile background color for dropdown submenus |
| Icons | color/size controls | Shopping Cart, Search, and Hamburger menu icon color and size |
| Logo | image styling | Border radius, border styles, box shadow, and image filters for the logo image |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding per side, responsive breakpoints |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Color, offsets, blur radius, spread |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue, blur, invert, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, scroll-driven effects, and positioning.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Semantic HTML tag for the module wrapper (div, nav, section) |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

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

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/menu` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Menu ID | `attrs.menu_id` | WordPress menu ID to display |
| Style | `attrs.menu_style` | Menu layout style variant |

!!! tip "Module Selection Guidance"
    For navigation within content areas use Menu; for full-width site navigation use Fullwidth Menu; for widget-based nav use Sidebar.

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

- [Fullwidth Menu](fullwidth-menu.md) — Full-browser-width menu variant for fullwidth sections
- [Sidebar](sidebar.md) — Display WordPress widget areas including navigation menus
- [Menu Text Options](../options-groups/menu-text.md) — Typography settings for menu link text
- [Theme Builder](../builder/theme-builder.md) — Build custom header templates with menus and logos
- [Responsive Options](../builder/responsive-options.md) — Control menu behavior across desktop, tablet, and phone
