---
title: "Divider"
category: modules
tags: ["modules", "divider", "separator", "line", "layout", "spacing"]
related: ["text", "image"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10273265-the-divider-module-in-divi-5"
---

# Divider

The Divider module inserts a horizontal line between content sections to create visual separation and improve page readability.

## Overview

The Divider module adds a simple horizontal rule to your page layout. Despite its simplicity, it serves an important design function: breaking up long stretches of content, separating distinct sections, and providing visual breathing room between modules. Without deliberate separation, pages can feel cluttered and difficult to scan.

You can configure the divider line's visibility, style, color, weight, and position. The line itself supports multiple CSS border styles including solid, dashed, dotted, double, groove, ridge, inset, and outset. You can also hide the line entirely and use the module purely as a transparent spacer by leveraging its margin and padding controls.

The Divider module is intentionally lightweight. It renders minimal markup and loads no additional assets, making it an efficient choice when you need spacing or separation without the overhead of more complex layout techniques.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10273265-the-divider-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/divider/)

![Divider module](../assets/screenshots/modules/divider/element.png){ loading=lazy }
*The Divider module displaying a horizontal line between content sections.*

## Use Cases

1. **Section Breaks** — Insert a styled divider between content blocks to visually separate topics, making long pages easier to scan and navigate.
2. **Decorative Accent Lines** — Use a short, colored divider beneath a heading to add a decorative underline effect that draws attention to section titles.
3. **Invisible Spacer** — Hide the divider line and use the module's margin and padding settings to create precise vertical spacing between modules without any visible element.

## How to Add the Divider Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon inside any row to add a new module.
3. Search for "Divider" in the module picker or browse the Structure Elements category, then click to insert it.

## Settings & Options

The Divider module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls whether the divider line is visible, along with link behavior, background, and metadata settings.

| Setting | Type | Description |
|---------|------|-------------|
| Show Divider | toggle | Controls whether the horizontal line is visible. When disabled, the module renders as an invisible spacer that still occupies vertical space based on its margin and padding values. |
| Link | url | Optionally wrap the entire module in a link so clicking on it navigates to a specified URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the divider module. Useful when using the divider as a decorative band or spacer with a colored background. |
| Loop | toggle | Enable the loop builder to use this module as a repeating element within dynamic content layouts. |
| Order | select | Control the module's display order when its parent row uses Flexbox or CSS Grid layout. |
| Meta | admin label | Assign a custom label to identify this module in the Visual Builder's layer panel. |

### Design Tab

The Design tab controls the line's visual properties and the module's dimensions, spacing, borders, and effects.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Line Color | color picker | Set the color of the divider line. Accepts any color value including hex, RGB, and color presets from your global color palette. |
| Line Style | select | Choose the CSS border style for the line: solid, dashed, dotted, double, groove, ridge, inset, or outset. Each creates a distinct visual effect. |
| Line Weight | range slider | Set the thickness of the divider line in pixels. Higher values create bolder, more prominent lines. |
| Line Position | select | Choose where the line sits within the module's vertical space: top, vertically centered, or bottom. This matters when the module has significant padding or height. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, etc.) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, interactions, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

## Code Examples

### Custom CSS

```css
/* Style the divider line */
.et_pb_divider .et_pb_module_inner::before {
    border-color: #2ea3f2;
    border-width: 3px;
}

/* Create a short centered accent divider */
.et_pb_divider.accent-divider {
    max-width: 80px;
    margin-left: auto;
    margin-right: auto;
}

/* Gradient divider effect using background */
.et_pb_divider.gradient-divider .et_pb_module_inner::before {
    border: none;
    height: 3px;
    background: linear-gradient(to right, #2ea3f2, #e02b20);
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_divider {
        margin-top: 15px;
        margin-bottom: 15px;
    }
}
```

### PHP Hooks

```php
/* Filter the Divider module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_divider' !== $render_slug) {
        return $output;
    }
    // Example: add an ARIA role for accessibility
    $output = str_replace('class="et_pb_divider', 'role="separator" class="et_pb_divider', $output);
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Heading Accent Underline** — Place a divider directly below a heading module with a short width (60-100px), bold weight, and a brand accent color. Center-align both modules to create a decorative underline effect commonly seen on modern landing pages.

2. **Dashed Section Break** — Use a full-width dashed divider with a muted gray color and thin weight between major content sections. This provides subtle separation without drawing too much attention away from the content itself.

3. **Invisible Vertical Spacer** — Disable the divider line and use only margin or padding to create precise vertical gaps between modules. This gives you pixel-level control over spacing without relying on row or section padding, which is useful inside complex multi-module layouts.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/divider` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Show Divider | `attrs.show_divider` | Toggle line visibility |
| Divider Style | `attrs.divider_style` | CSS border style (solid, dashed, etc.) |
| Divider Weight | `attrs.divider_weight` | Line thickness in pixels |

!!! tip "Module Selection Guidance"
    For visual separators use Divider; for invisible spacing adjust Spacing options on adjacent modules instead.

## Saving Your Work

After configuring the divider:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Divider Line Not Visible"
    If you have added a Divider module but no line appears, check the "Show Divider" toggle in the Content tab — it may be disabled. Also verify that the line color is not set to the same color as the background, and that the line weight is greater than zero.

!!! warning "Divider Takes Up Too Much Space"
    If the divider creates more vertical space than expected, check the Spacing settings in the Design tab. The module may have large top or bottom padding or margin values. Reset these to zero or your desired values.

!!! tip "Line Does Not Span Full Width"
    If the divider line appears shorter than expected, check the Sizing settings in the Design tab. The module width or max-width may be set to a value less than 100%. Also check if the parent row or column has padding that is constraining the module's available width.

## Related

- [Text](text.md) — Display formatted text content that pairs naturally with dividers for section breaks
- [Image](image.md) — Display images that can be separated from other content using dividers
