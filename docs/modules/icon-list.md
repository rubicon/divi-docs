---
title: "Icon List"
description: "Complete Divi 5 Icon List module reference — styled lists with custom icons per item, Flex and Block layouts, and per-item overrides."
category: modules
tags: ["modules", "icon-list", "icons", "list", "features", "checklist", "bullets"]
related: ["icon", "blurb", "text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11982062-the-icon-list-module-in-divi-5"
---

# Icon List

The Icon List module displays a styled list of items, each paired with a custom icon from the Divi icon library or an uploaded image.

!!! abstract "Quick Reference"
    **What it does:** Creates a styled list where each item has a custom icon, title, and optional body text with per-item design overrides.
    **When to use it:** Feature checklists, process/step guides, contact information blocks, pricing plan inclusions
    **Key settings:** Items (add/edit/remove), Layout (Block/Flex), Icon styling, per-item icon and text overrides
    **Block identifier:** `divi/icon-list`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/11982062-the-icon-list-module-in-divi-5)

!!! tip "When to Use This Module"
    - You need a list where each item has its own custom icon
    - Feature comparison checklists with checkmark/X icons per item
    - Contact details blocks with phone, email, address, and hours icons

!!! warning "When NOT to Use This Module"
    - You need a single standalone icon → use [Icon](icon.md)
    - You need icons with longer descriptions in a card layout → use [Blurb](blurb.md) modules in columns
    - You need a simple bullet or numbered list → use [Text](text.md) with HTML list markup

## Overview

The Icon List module creates visually engaging lists by combining text entries with icons. Each list item consists of a title, optional body text, and an icon that can be selected from the built-in Divi icon library or uploaded as a custom image. This makes the module suitable for feature lists, service breakdowns, contact information displays, step-by-step processes, and any content that benefits from icon-paired text entries.

The module supports both Block and Flexbox layout modes. Block mode stacks items vertically in a traditional list format, while Flex mode arranges items horizontally with wrapping, which is useful for multi-column feature grids. Each individual list item can be styled independently, allowing you to override the module-wide icon size, color, and text settings for specific entries.

Items are managed through an add/edit/remove interface in the Content tab. Each item opens its own settings panel where you configure the icon, title, body content, and item-specific design overrides. The module-level Design tab controls shared styling that applies uniformly unless overridden at the item level.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11982062-the-icon-list-module-in-divi-5).

![Icon List module](../assets/screenshots/modules/icon-list/element.png){ loading=lazy }
*The Icon List module displaying items with custom icons and text.*

## Use Cases

1. **Product Feature Highlights** — Display a product's key benefits with each feature paired to a relevant icon, creating a scannable list that communicates value quickly without lengthy paragraphs.
2. **Process or Step Guide** — Show sequential steps using numbered or symbolic icons alongside brief descriptions, guiding users through a workflow, onboarding process, or setup procedure.
3. **Contact Information Block** — List phone numbers, email addresses, physical locations, and business hours with matching icons (phone, envelope, map pin, clock) for a clean, professional contact section.

## How to Add the Icon List Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Icon List" in the module picker or find it in the Content Elements category, then click to insert it.

<!-- TODO: Add animated GIF demonstrating module insertion -->

## Settings & Options

The Icon List module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the list items, link behavior, background, and module metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Items | item list | Add, edit, reorder, or remove individual icon list items. Each item has its own icon, title, body text, and design overrides. Click **+** to add, the pencil icon to edit, the trash icon to delete, and drag to reorder. |
| Link | url/link settings | Makes the entire Icon List module clickable, directing users to a page, section, or external URL. |
| Background | background controls | Apply a background color, gradient, image, or video behind the Icon List module container. |
| Loop | toggle | Enables the loop builder to repeat the module dynamically based on a data source query. |
| Order | number | Controls the display order when the parent container uses Flexbox or Grid layout. |
| Meta | admin label | Set an admin label for identification in the Visual Builder. Controls builder-only visibility. |

<!-- ![Icon List Content tab settings](../assets/screenshots/modules/icon-list/settings-content.png){ loading=lazy } -->
<!-- TODO: Capture Content tab screenshot -->

#### Individual Item Settings

Each item within the Icon List has its own configurable settings:

| Setting | Type | Description |
|---------|------|-------------|
| Title | text | The heading text for this list item. |
| Body | rich text | Optional descriptive text displayed below the item title. |
| Icon | icon picker/upload | Select an icon from the Divi icon library or upload a custom icon image. |
| Design Overrides | styling controls | Item-specific icon size, color, and text styling that overrides the module-wide defaults for this entry only. |

### Design Tab

The Design tab controls the visual appearance of icons, text, layout mode, and overall module styling.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | dropdown | Choose between Block (vertical stack) or Flex (horizontal arrangement with wrapping) layout for list items. |
| Icon | icon styling | Configure default icon size, color, and appearance applied to all list items. Individual items can override these values. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | General text styling — font, alignment, color |
| [Body Text](../options-groups/body-text.md) | Font, size, color, weight for item body content |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (hue, saturation, brightness, blend mode) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Icon List Design tab settings](../assets/screenshots/modules/icon-list/settings-design.png){ loading=lazy } -->
<!-- TODO: Capture Design tab screenshot -->

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

<!-- ![Icon List Advanced tab settings](../assets/screenshots/modules/icon-list/settings-advanced.png){ loading=lazy } -->
<!-- TODO: Capture Advanced tab screenshot -->

## Code Examples

### Custom CSS

```css
/* Style the Icon List container */
.et_pb_icon_list {
    list-style: none;
    padding: 0;
}

/* Style individual list items */
.et_pb_icon_list .et_pb_icon_list_item {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 12px 0;
    border-bottom: 1px solid #eeeeee;
}

.et_pb_icon_list .et_pb_icon_list_item:last-child {
    border-bottom: none;
}

/* Icon circle background */
.et_pb_icon_list .et_pb_icon_list_icon {
    background: #f0f4ff;
    border-radius: 50%;
    padding: 12px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Hover effect on items */
.et_pb_icon_list .et_pb_icon_list_item:hover {
    background: #f9f9f9;
    border-radius: 8px;
    padding-left: 12px;
    transition: all 0.3s ease;
}

/* Responsive adjustments */
@media (max-width: 767px) {
    .et_pb_icon_list .et_pb_icon_list_item {
        gap: 12px;
    }
}
```

### PHP Hooks

```php
/* Add schema markup to Icon List items for SEO */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_icon_list' !== $render_slug) {
        return $output;
    }
    $output = str_replace(
        'class="et_pb_icon_list_item',
        'itemscope itemprop="itemListElement" class="et_pb_icon_list_item',
        $output
    );
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Feature Comparison Checklist** — Use checkmark icons for included features and X icons for excluded features. Apply green color to checkmark items and red to X items using item-level design overrides. This pattern works well alongside pricing tables to clarify what each plan includes.

2. **Two-Column Feature Grid** — Set the layout to Flex and place the Icon List in a single-column row. With appropriate sizing and spacing, items wrap into two columns on desktop and collapse to a single column on mobile. Each item highlights a product feature with an icon and short description.

3. **Contact Details Sidebar** — Create a compact vertical Icon List in a sidebar column with items for phone, email, address, and business hours. Use small, consistent icons and minimal body text. Link each item appropriately (tel: for phone, mailto: for email) at the item level for click-to-contact functionality.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/icon-list` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Child items | Nested blocks | Each item is a nested block with its own icon and text |

!!! tip "Module Selection Guidance"
    For lists with custom icons per item use Icon List; for simple bullet lists use Text; for feature grids use Blurb modules in columns.

## Saving Your Work

After configuring the Icon List module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Icons Not Displaying"
    If icons appear as blank spaces or broken images:

    - Verify that an icon is selected for each item by opening the item settings and checking the icon picker field.
    - If using custom uploaded icons, ensure the image files are accessible at their URLs and have not been deleted from the media library.
    - Check whether a CSS conflict is hiding the icon element. Inspect the element in browser DevTools to confirm the icon markup is present.

!!! warning "Items Not Wrapping in Flex Layout"
    If items overflow horizontally instead of wrapping to the next row:

    - Confirm that the Layout is set to **Flex** in the Design tab, not Block.
    - Check whether individual items have fixed widths that exceed the container. Adjust item sizing to use percentage-based or auto widths.
    - Ensure the parent column is wide enough to accommodate at least one item. Very narrow columns may cause unexpected overflow.

!!! tip "Consistent Icon Sizing Across Items"
    If some icons appear larger or smaller than others, it is usually because individual item overrides are set. To enforce uniform icon sizing, set the icon size at the module level in the Design tab and remove any item-specific size overrides.

## Related

- [Icon](icon.md) — Single icon display module for standalone icon elements
- [Blurb](blurb.md) — Icon or image combined with a heading and text for feature blocks
- [Text](text.md) — Rich text module for body content and formatted lists
