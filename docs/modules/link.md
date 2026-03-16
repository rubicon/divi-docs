---
title: "Link"
description: "Complete Divi 5 Link module reference — settings, design options, code examples, and troubleshooting for styled link elements with icons and nested child modules."
category: modules
tags: ["modules", "content-modules", "link", "navigation", "icon", "nested-modules"]
related: ["button", "text", "menu"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13713821"
---

# Link

The Link module creates a styled, clickable link element with optional icon and support for nested child modules, providing flexible linking capabilities beyond what a standard text link or button offers.

!!! abstract "Quick Reference"
    **What it does:** Renders a configurable link element with text, optional icon, and the ability to contain nested child modules.
    **When to use it:** Navigation menus, styled link lists, icon+text link combinations, container links wrapping child elements
    **Key settings:** Text, Icon, Link URL, Layout (Block/Flex/Grid), Elements (nested modules)
    **Block identifier:** `divi/link`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/13713821)

!!! tip "When to Use This Module"
    - Creating styled navigation links with icons that go beyond basic text hyperlinks
    - Building link lists or navigation components with consistent visual styling
    - Wrapping multiple child elements in a single clickable link container using nested modules

!!! warning "When NOT to Use This Module"
    - For a prominent call-to-action button — use [Button](button.md)
    - For inline text links within paragraphs — use [Text](text.md) with HTML links
    - For a full site navigation menu — use [Menu](menu.md)

## Overview

The Link module is a versatile element in Divi 5 that creates a styled, clickable link with more structural flexibility than a simple text hyperlink. At its core, it renders an anchor element (`<a>`) with configurable text, an optional icon displayed alongside the text, and a destination URL. However, what distinguishes the Link module from a basic link is its ability to function as a container that accepts nested child modules through the Elements setting.

This nesting capability means you can create compound link elements — for example, a card-like link that wraps an icon, a heading, and a description paragraph, all of which become part of the same clickable area. The Design tab's Layout option (Block, Flex, or Grid) controls how these nested child modules are arranged within the link container, giving you the same layout control over the link's internal structure that you have over sections and rows.

The module also supports the Loop Builder, enabling dynamic link generation from WordPress data sources. Combined with the icon selector and text styling options, the Link module serves as a building block for navigation components, feature link lists, icon menus, and other interactive elements that need more structure than a button but more styling than a plain hyperlink.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13713821).

<!-- ![Link module](../assets/screenshots/modules/link/element.png){ loading=lazy } -->
<!-- *The Link module displaying a text link with an icon, styled with custom font and color settings.* -->

## Use Cases

1. **Icon Link Navigation** — Create a row of styled links, each with a descriptive icon and text label, forming a visual navigation component for sections like "Our Services" or "Quick Links" that is more engaging than a plain text list.
2. **Container Link Cards** — Use nested child modules to build card-like link elements that wrap an image, title, and description in a single clickable area, directing users to detailed pages without needing a separate button.
3. **Loop-Driven Link Lists** — Enable the Loop Builder to dynamically generate links from WordPress data (categories, pages, custom post types), creating auto-updating navigation or content index sections.

## How to Add the Link Module

1. Open the Visual Builder on the page where you want the link to appear.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Link" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13713821).

## Settings & Options

The Link module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the link's text, icon, destination URL, nested elements, and the Loop Builder toggle.

| Setting | Type | Description |
|---------|------|-------------|
| Text | text | Define the visible text label for the link. This is the primary clickable text displayed to users. |
| Icon | icon selector | Choose an icon from the Divi icon library to display alongside the link text. The icon appears before or after the text depending on layout settings. |
| Link | url | Set the destination URL for the link. Supports internal pages, external URLs, sections, and anchors. |
| Elements | nested modules | Insert nested child modules within the link container, such as images, text, icons, or other modules that become part of the clickable area. |
| Background | background controls | Set a background color, gradient, image, or video behind the link module container. |
| Loop | toggle | Enable the Loop Builder to dynamically generate link instances from WordPress data sources. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Link Content tab settings](../assets/screenshots/modules/link/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the layout of nested child elements, icon styling, and text appearance.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose how nested child modules are arranged inside the link container: Block (stacked), Flex (flexible alignment), or Grid (CSS Grid layout). |
| Icon | icon styling | Customize the icon color, font size, and background styling. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, hue, saturation, blending) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Link Design tab settings](../assets/screenshots/modules/link/settings-design.png){ loading=lazy } -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Choose the semantic HTML tag for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

<!-- ![Link Advanced tab settings](../assets/screenshots/modules/link/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the link module as a pill-shaped link */
.et_pb_link_module {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    background: #f0f4ff;
    border-radius: 24px;
    color: #2ea3f2;
    text-decoration: none;
    font-weight: 500;
    transition: background 0.3s ease, color 0.2s ease;
}

.et_pb_link_module:hover {
    background: #2ea3f2;
    color: #fff;
}

/* Style the icon */
.et_pb_link_module .et-pb-icon {
    font-size: 18px;
    transition: transform 0.2s ease;
}

.et_pb_link_module:hover .et-pb-icon {
    transform: translateX(3px);
}

/* Style link as a card container */
.et_pb_link_module.link-card {
    display: block;
    padding: 24px;
    background: #fff;
    border: 1px solid #eee;
    border-radius: 8px;
    text-decoration: none;
    color: inherit;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.et_pb_link_module.link-card:hover {
    border-color: #2ea3f2;
    box-shadow: 0 4px 12px rgba(46, 163, 242, 0.15);
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_link_module {
        padding: 8px 16px;
        font-size: 14px;
    }
}
```

### PHP Hooks

```php
/* Filter the Link module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_link' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Icon + Text Navigation Row** — Place multiple Link modules in a Flex row, each with a different icon and text label pointing to key pages. This creates a visual quick-navigation bar that is more engaging than a plain text menu and more compact than a set of full buttons.

2. **Clickable Card Grid** — Use the Link module with nested child elements (image + heading + description) arranged in a Grid or Flex layout. Place multiple cards in a row to create a feature grid where each entire card is a single clickable link to a detail page.

3. **Loop-Generated Breadcrumb Trail** — Enable the Loop Builder with a page hierarchy data source to dynamically generate a breadcrumb-style navigation trail, with each Link module instance representing one level in the hierarchy.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/link` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For styled links with icons and nested elements use Link; for prominent call-to-action buttons use Button; for inline text links use Text; for full navigation menus use Menu.

## Saving Your Work

After configuring the link module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Link module does not appear on the front end, verify that:

    - The module is placed inside a valid section and row
    - The Text or Elements setting has content defined
    - Visibility settings are not hiding the module on the current device

!!! warning "Link Not Clickable"
    If the module renders but is not clickable, check that:

    - A valid URL is entered in the Link setting
    - The URL format is correct (include `https://` for external URLs)
    - No parent element is intercepting the click event with its own link or interaction

!!! tip "Nested Modules Not Aligning Properly"
    If child modules within the Link container are not arranged as expected, verify the Layout setting in the Design tab. Use Flex for horizontal alignment with flexible spacing, Grid for structured column/row placement, or Block for simple vertical stacking.

## Related

- [Button](button.md) — Prominent call-to-action button module
- [Text](text.md) — Rich text module for paragraphs and inline content
- [Menu](menu.md) — Full site navigation menu module
- [Icon](icon.md) — Standalone icon display module
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
