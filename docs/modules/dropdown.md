---
title: "Dropdown"
description: "Complete Divi 5 Dropdown module reference — settings, design options, code examples, and troubleshooting for creating hover/click-triggered dropdown containers with nested child modules."
category: modules
tags: ["modules", "content-modules", "dropdown", "navigation", "menu", "interactive", "nested-modules"]
related: ["menu", "accordion", "toggle"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13714244"
---

# Dropdown

The Dropdown module creates an interactive container that reveals nested child modules on hover or click, providing a way to build custom dropdown menus, mega menus, and reveal-on-demand content panels.

!!! abstract "Quick Reference"
    **What it does:** Renders a collapsible container that shows/hides nested child modules via hover or click triggers.
    **When to use it:** Custom dropdown menus, mega menus, content reveals, tooltip-like panels
    **Key settings:** Elements (nested modules), Dropdown Position, Layout (Block/Flex/Grid), trigger type
    **Block identifier:** `divi/dropdown`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/13714244)

!!! tip "When to Use This Module"
    - Building custom dropdown menus or mega menus with rich content beyond simple text links
    - Creating hover-triggered content reveals like expanded descriptions or preview panels
    - Designing interactive UI elements that show additional content on demand without navigating away

!!! warning "When NOT to Use This Module"
    - For the site's primary navigation menu — use [Menu](menu.md)
    - For always-visible collapsible sections — use [Accordion](accordion.md) or [Toggle](toggle.md)
    - For simple hover tooltips — consider CSS-only tooltips via the [Text](text.md) module

## Overview

The Dropdown module introduces a powerful interactive container element to Divi 5 that reveals content on hover or click. Unlike the Accordion or Toggle modules, which show content in an always-visible collapsible format, the Dropdown positions its content as a floating panel that appears relative to the trigger element — similar to how a navigation submenu works, but with the full flexibility of Divi's module system inside the dropdown panel.

The module works through a parent-child relationship: the Dropdown itself serves as the trigger element and container, while nested child modules (added through the Elements setting) form the content of the dropdown panel. You can nest any combination of modules inside — Link modules for a navigation dropdown, Image and Text modules for a mega menu with visuals, or form modules for a compact settings panel.

The Design tab provides extensive **Dropdown Position** controls that let you configure where the dropdown panel appears relative to the trigger (above, below, left, right), its direction of expansion, alignment, offset distances, and whether it opens on hover or on click. The Layout setting (Block, Flex, or Grid) controls how the nested child modules are arranged within the dropdown panel, giving you the same layout flexibility available in sections and rows.

The module also supports the Loop Builder for dynamic dropdown content generation from WordPress data sources, making it possible to create auto-updating dropdown navigation from categories, pages, or custom post types.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13714244).

<!-- ![Dropdown module](../assets/screenshots/modules/dropdown/element.png){ loading=lazy } -->
<!-- *The Dropdown module with a flyout panel containing nested Link modules, triggered on hover.* -->

## Use Cases

1. **Custom Mega Menu** — Build a rich dropdown panel with multiple columns of links, featured images, and promotional text. Nest Link modules, Image modules, and Text modules inside the dropdown, use the Grid or Flex layout to arrange them in columns, and position the dropdown below its trigger.
2. **Action Menu** — Create a click-triggered dropdown containing action links (Edit, Duplicate, Delete, etc.) for a custom admin-facing interface or user dashboard component.
3. **Content Preview Panel** — Attach a dropdown to a product or post link that reveals a preview panel on hover, showing an image thumbnail, short description, and a "Read More" link, similar to a content preview tooltip.

## How to Add the Dropdown Module

1. Open the Visual Builder on the page where you want the dropdown to appear.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Dropdown" in the module picker, then click to insert it.
4. Use the Elements setting to add nested child modules that will form the dropdown panel content.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13714244).

## Settings & Options

The Dropdown module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the dropdown's nested content elements, link behavior, and the Loop Builder toggle.

| Setting | Type | Description |
|---------|------|-------------|
| Elements | nested modules | Add child modules that form the dropdown panel content. Supports Link modules, images, text, and any other Divi modules. |
| Link | url | Optionally make the dropdown trigger element itself clickable, directing users to a page or URL when clicked (separate from the dropdown open behavior). |
| Background | background controls | Set a background color, gradient, image, or video behind the dropdown module container. |
| Loop | toggle | Enable the Loop Builder to dynamically generate dropdown content from WordPress data sources. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Dropdown Content tab settings](../assets/screenshots/modules/dropdown/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the dropdown panel's position, trigger behavior, and the internal layout of nested elements.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose how nested child modules are arranged inside the dropdown panel: Block (stacked vertically), Flex (flexible alignment, default), or Grid (CSS Grid layout). |
| Dropdown Position | composite | A group of settings controlling the dropdown panel's behavior: position relative to the trigger, direction of expansion, alignment, horizontal and vertical offset, and trigger type (hover or click). |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, hue, saturation, blending) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Dropdown Design tab settings](../assets/screenshots/modules/dropdown/settings-design.png){ loading=lazy } -->

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

<!-- ![Dropdown Advanced tab settings](../assets/screenshots/modules/dropdown/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the dropdown trigger */
.et_pb_dropdown {
    position: relative;
    display: inline-block;
    cursor: pointer;
}

/* Style the dropdown panel */
.et_pb_dropdown .dropdown-content {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    padding: 12px;
    min-width: 220px;
}

/* Style nested links inside dropdown */
.et_pb_dropdown .dropdown-content .et_pb_link_module {
    display: block;
    padding: 10px 16px;
    color: #333;
    text-decoration: none;
    border-radius: 4px;
    transition: background 0.2s ease;
}

.et_pb_dropdown .dropdown-content .et_pb_link_module:hover {
    background: #f0f4ff;
    color: #2ea3f2;
}

/* Add a subtle entrance animation */
.et_pb_dropdown .dropdown-content {
    opacity: 0;
    transform: translateY(-8px);
    transition: opacity 0.2s ease, transform 0.2s ease;
    pointer-events: none;
}

.et_pb_dropdown:hover .dropdown-content,
.et_pb_dropdown.active .dropdown-content {
    opacity: 1;
    transform: translateY(0);
    pointer-events: auto;
}

/* Mega menu multi-column layout */
.et_pb_dropdown.mega-menu .dropdown-content {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    padding: 24px;
    min-width: 600px;
}

/* Responsive: collapse mega menu on mobile */
@media (max-width: 980px) {
    .et_pb_dropdown.mega-menu .dropdown-content {
        grid-template-columns: 1fr;
        min-width: auto;
    }
}
```

### PHP Hooks

```php
/* Filter the Dropdown module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_dropdown' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Navigation Submenu** — Place multiple Link modules inside the dropdown's Elements, each pointing to a different page. Use Flex layout with a vertical direction and minimal spacing to create a traditional navigation submenu that appears on hover below a header navigation item.

2. **Mega Menu Panel** — Use Grid layout inside the dropdown with 3 or 4 columns. Fill each column with a group of related links, and optionally add images or promotional blocks. This creates a rich mega menu experience for e-commerce or content-heavy sites.

3. **Click-to-Reveal Info Panel** — Set the trigger type to click and nest a combination of text, images, and links inside the dropdown. This creates an expandable information panel that customers can open on demand, keeping the page clean while making detailed content accessible.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/dropdown` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For custom dropdown panels with rich content use Dropdown; for the primary site navigation use Menu; for always-visible collapsible sections use Accordion or Toggle; for styled link elements use Link.

## Saving Your Work

After configuring the dropdown module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Dropdown module does not appear on the front end, verify that:

    - The module is placed inside a valid section and row
    - At least one child module is added through the Elements setting
    - Visibility settings are not hiding the module on the current device

!!! warning "Dropdown Panel Not Opening"
    If the trigger element renders but the dropdown panel does not appear, check that:

    - Child modules exist in the Elements setting (an empty dropdown has nothing to show)
    - The trigger type (hover vs. click) matches the expected user interaction
    - No CSS `overflow: hidden` on a parent element is clipping the dropdown panel
    - The dropdown Position offset values are not pushing the panel off-screen

!!! tip "Dropdown Panel Appearing in Wrong Position"
    If the dropdown panel opens but is misaligned or appears in an unexpected location, adjust the Dropdown Position settings in the Design tab. Check the position (above/below/left/right), direction, alignment, and offset values. Also verify that the parent row or section does not have `overflow: hidden` set, which can clip absolutely positioned elements.

## Related

- [Menu](menu.md) — Full site navigation menu module
- [Accordion](accordion.md) — Always-visible collapsible content sections
- [Toggle](toggle.md) — Single collapsible content section
- [Link](link.md) — Styled link element with icon support
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
