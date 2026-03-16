---
title: "Accordion"
category: modules
tags: ["modules", "content-toggle", "faq", "collapsible"]
related: ["toggle", "tabs"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10063343-the-accordion-module-in-divi-5"
---

# Accordion

The Accordion module displays collapsible content sections where only one item is open at a time.

## Overview

The Accordion module organizes content into a vertically stacked group of expandable/collapsible panels. When a visitor clicks on a panel header, its content is revealed and any previously open panel collapses automatically. By default, the first panel is open when the page loads.

This behavior distinguishes it from the [Toggle](toggle.md) module, where multiple items can be open simultaneously. The accordion enforces a one-at-a-time pattern, which keeps the layout compact and focused.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10063343-the-accordion-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/accordion/)

![Accordion module](../assets/screenshots/modules/accordion/element.png){ loading=lazy }
*The Accordion module showing collapsible FAQ-style content panels.*

## Use Cases

1. **FAQ Sections** — Present frequently asked questions with answers that expand on click, keeping the page scannable without overwhelming visitors with a wall of text.
2. **Product or Service Details** — Break down features, specifications, or plan tiers into expandable sections so visitors can drill into what interests them.
3. **Step-by-Step Instructions** — Organize multi-step processes where each step expands to reveal detailed instructions, keeping the overall flow visible.

## How to Add the Accordion Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Accordion" in the module picker or find it in the Content Elements category, then click to insert it.

<!-- TODO: Add animated GIF demonstrating module insertion -->

## Settings & Options

The Accordion module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the accordion's items, icon, link behavior, background, and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Add, Edit, and Remove | item list | Manage individual accordion items. Each item has its own title and body content. Click **+** to add, the pencil icon to edit, the trash icon to delete, and drag to reorder. |
| Toggle Icon | icon picker | Choose the icon displayed next to each accordion item header that indicates expand/collapse state. |
| Link | url | Optionally link the entire accordion module to a URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the entire accordion module. |
| Loop | toggle | When enabled, collapsing the last item automatically opens the first item, creating a circular navigation pattern. |
| Order | select | Control the display order of accordion items (e.g., default order or reversed). |
| Meta | admin label | Set an admin label for the module to help identify it in the Visual Builder's layer panel. |

<!-- ![Accordion Content tab settings](../assets/screenshots/modules/accordion/settings-content.png){ loading=lazy } -->
<!-- TODO: Capture Content tab screenshot -->

#### Individual Accordion Item Settings

Each accordion item within the module has its own settings:

| Setting | Type | Description |
|---------|------|-------------|
| Title | text | The heading text displayed in the clickable panel header. |
| Content | rich text editor | The body content revealed when the item is expanded. Supports text, images, and other media. |

### Design Tab

The Design tab controls the visual styling of the accordion and its contents.

| Setting | Type | Description |
|---------|------|-------------|
| Icon | icon styling | Customize the toggle icon's color, size, and placement. |
| Toggle | toggle styling | Style the overall toggle container including open/closed state appearance. |
| Text | text styling | Set general text properties like font family, weight, style, and line height. |
| Title Text | text styling | Style the accordion item titles specifically — font, size, color, letter spacing, etc. Separate settings for open and closed states. |
| Closed Title Text | text styling | Override title styling specifically for items in their closed state. |
| Body Text | text styling | Style the expanded content area text independently from titles. |
| Sizing | dimensions | Control the module's width, max-width, and height. |
| Spacing | margin/padding | Set margin and padding values for the module and its internal elements. Supports responsive values per device. |
| Border | border controls | Add and style borders around the module or individual elements (width, color, style, radius). |
| Box Shadow | shadow controls | Apply box shadow effects with customizable color, blur, spread, and position. |
| Filters | image filters | Apply CSS filter effects like brightness, contrast, saturation, blur, and hue rotation. |
| Transform | transform controls | Apply CSS transforms — scale, translate, rotate, skew, and transform origin. |
| Animation | animation select | Choose an entrance animation style (fade, slide, bounce, zoom, flip, fold, roll) with configurable duration, delay, and intensity. |

<!-- ![Accordion Design tab settings](../assets/screenshots/modules/accordion/settings-design.png){ loading=lazy } -->
<!-- TODO: Capture Design tab screenshot -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for IDs, classes, conditional display, and interactions.

| Setting | Type | Description |
|---------|------|-------------|
| Attributes | text fields | Assign a CSS ID and CSS classes to the module for targeting with custom styles or JavaScript. |
| CSS | code editor | Write custom CSS that applies directly to specific elements within the module (container, title, content, icon, etc.). |
| HTML | code fields | Add custom HTML attributes to the module's wrapper element. |
| Conditions | condition builder | Set display conditions so the module only appears based on rules (e.g., user role, page type, date range, or custom logic). |
| Interactions | interaction builder | Define hover, click, or scroll-triggered interactions that affect this module or other elements on the page. |
| Visibility | device toggles | Show or hide the module on desktop, tablet, and/or phone. Hidden modules are not rendered in the page source for that device. |
| Transitions | transition controls | Configure CSS transition properties (duration, easing, delay) for hover state changes. |
| Position | position controls | Set the CSS position property (relative, absolute, fixed, sticky) and offset values (top, right, bottom, left, z-index). |
| Scroll Effects | scroll controls | Apply scroll-driven effects like parallax, fade, scale, rotate, blur, or horizontal movement as the user scrolls. |

<!-- ![Accordion Advanced tab settings](../assets/screenshots/modules/accordion/settings-advanced.png){ loading=lazy } -->
<!-- TODO: Capture Advanced tab screenshot -->

## Managing Accordion Items

Each accordion module starts with a set of default items. You can:

1. **Add an item** — Click the **+** button at the bottom of the item list in the Content tab.
2. **Edit an item** — Click the pencil/gear icon on any existing item to open its individual settings.
3. **Delete an item** — Click the trash icon on the item you want to remove.
4. **Reorder items** — Drag items by their handle to rearrange the display order.

<!-- TODO: Add screenshot showing the add/edit/delete/reorder icons -->

## Styling Individual Items

Each accordion item can be styled independently from the parent module. Click the pencil icon on any item, then navigate to that item's **Design** tab to override the parent styles for just that item. This is useful when you want to visually distinguish a specific item — for example, highlighting a "most popular" FAQ or drawing attention to an important step.

<!-- TODO: Add animated GIF demonstrating individual item styling -->

## Code Examples

### Custom CSS

```css
/* Style the Accordion module container */
.et_pb_accordion {
    margin-bottom: 30px;
}

/* Style accordion item titles */
.et_pb_accordion .et_pb_toggle_title {
    font-weight: 600;
    font-size: 18px;
}

/* Style the open/active item differently */
.et_pb_accordion .et_pb_toggle_open .et_pb_toggle_title {
    color: #2ea3f2;
}

/* Style the content area */
.et_pb_accordion .et_pb_toggle_content {
    padding: 20px;
    line-height: 1.7;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_accordion {
        padding: 10px;
    }
    .et_pb_accordion .et_pb_toggle_title {
        font-size: 16px;
    }
}
```

### PHP Hooks

```php
/* Filter the Accordion module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_accordion' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

1. **FAQ Page** — Create a dedicated FAQ page with a single accordion module containing all questions and answers. Use descriptive titles as the questions and rich text content for the answers.

2. **Service Detail Sections** — Use multiple accordion modules on a services page, one per service category, each containing expandable details about individual offerings, pricing, and terms.

3. **Documentation Navigation** — Build a knowledge base layout where top-level topics are accordion headers and each expands to show a summary with links to full articles.

## Saving Your Work

After configuring the accordion:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Accordion module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - There is at least one accordion item with content

!!! warning "All Items Appear Open"
    If multiple items display open simultaneously, you may have accidentally inserted individual Toggle modules instead of an Accordion module. The Accordion enforces one-open-at-a-time behavior; Toggles do not.

!!! tip "Accordion Won't Collapse on Mobile"
    Check that JavaScript is not being blocked on the page. The accordion's expand/collapse behavior relies on JavaScript. Also verify no custom CSS is overriding the `display` property on toggle content elements.

## Related

- [Toggle](toggle.md) — Similar collapsible panels, but multiple items can be open at once
- [Tabs](tabs.md) — Horizontal tab-based content organization as an alternative to vertical accordions
