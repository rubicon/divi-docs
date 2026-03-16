---
title: "Global Elements"
description: "Divi 5 Global Elements — reusable modules, rows, and sections that sync content and design changes across every page where they appear."
category: builder
tags: [builder, global-elements, global-modules, sync, reusable]
related: [visual-builder, library, presets]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: ""
---

# Global Elements

Global Elements are reusable Divi builder elements (modules, rows, or sections) that sync changes across every page where they appear.

!!! abstract "Quick Reference"
    **What it does:** Creates a single shared instance of a module, row, or section that syncs edits across all pages.
    **Where to find it:** Right-click any element → Save To Library → check "Make This A Global Item" (green border indicates global).
    **Key features:**

    - Edit any instance and changes propagate to all pages site-wide
    - Green border and globe icon distinguish global elements in the builder
    - Selective Sync: choose which settings sync globally vs. remain independent per instance
    - Detach from global to convert back to a regular independent element

    **ET Docs:** N/A

## Overview

When you save a module, row, or section as a Global Element, it becomes a single shared instance. Edit the element on one page, and the changes automatically propagate to every other page where that global element is used. This eliminates the need to manually update the same content in multiple places.

Global Elements are ideal for content blocks that appear on multiple pages and need to stay identical, such as call-to-action banners, newsletter signup forms, contact information sections, or promotional notices. They are visually distinguished in the Visual Builder by a green border, making them easy to identify.

Global Elements differ from [Presets](presets.md) in a fundamental way: presets share only design settings while each element keeps its own content, whereas global elements share both content and design as a single synchronized instance.

<!-- ![Global Elements overview](../assets/screenshots/builder/global-elements/overview.png){ loading=lazy }
*A global element (green border) in the Visual Builder showing it is synced across pages.* -->

## How Global Elements Work

When you create a global element:

1. The element is saved to the [Divi Library](library.md) with a "global" flag
2. Every instance on your site references the same saved element
3. Editing any instance opens the shared element for editing
4. Saving changes updates all instances across all pages simultaneously
5. The element appears with a distinctive **green border** in the Visual Builder

| Aspect | Regular Element | Global Element |
|--------|----------------|----------------|
| **Instances** | Independent copies | Single shared instance |
| **Editing** | Affects only that element | Affects all instances site-wide |
| **Visual indicator** | Standard gray/blue border | Green border |
| **Content** | Unique per element | Shared across all instances |
| **Design** | Unique per element | Shared across all instances |
| **Stored in** | Page content | Divi Library |

## Creating a Global Element

### Method 1: Save as Global from the Settings Window

1. Open the element's settings in the Visual Builder
2. Click the **three-dot menu** (vertical ellipsis)
3. Select **Save To Library**
4. In the save dialog, check **Make This A Global Item**
5. Name the element and assign categories/tags
6. Click **Save To Library**

### Method 2: Right-Click and Save

1. Right-click on the element in the Visual Builder
2. Select **Save To Library**
3. Check **Make This A Global Item**
4. Name and save

### Method 3: Convert an Existing Library Item

1. Navigate to **Divi > Divi Library** in the WordPress admin
2. Find the library item you want to make global
3. Click **Quick Edit**
4. Check the **Global** option
5. Click **Update**

## Using Global Elements

### Adding a Global Element to a Page

1. In the Visual Builder, click the **plus (+)** icon to add a new element
2. Select **Add From Library**
3. Filter to show global items (look for the green globe icon)
4. Click the global element to insert it into your page

### Identifying Global Elements

Global elements are easy to spot in the Visual Builder:

- **Green border** surrounds the element
- **Green globe icon** appears in the element's toolbar
- Hovering shows a tooltip indicating it is a global element

## Editing Global Elements

!!! warning "Global Edits Affect All Pages"
    When you edit a global element, the changes apply everywhere that element appears on your website. Be certain you want a site-wide change before saving.

### Editing in the Visual Builder

1. Click on the global element (green-bordered) on any page
2. Open its settings (gear icon or double-click)
3. Make your changes to content, design, or advanced settings
4. Click **Save**
5. All instances of this element across your site are now updated

### Editing from the Library

1. Navigate to **Divi > Divi Library** in the WordPress admin
2. Click on the global element
3. Edit it using the Visual Builder
4. Save your changes

## Selective Sync

Selective Sync gives you granular control over which parts of a global element are synchronized across instances. This allows you to keep certain settings synced (like design styling) while letting other settings (like content) vary per instance.

### How Selective Sync Works

When Selective Sync is enabled on a global element, you can choose which specific settings are global and which are local:

| Sync Status | Behavior |
|-------------|----------|
| **Synced** (green) | This setting is shared across all instances. Changing it on one instance changes it everywhere. |
| **Unsynced** (gray) | This setting is independent per instance. Each placement can have a different value. |

### Enabling Selective Sync

1. Open a global element's settings
2. Look for the **sync icon** (circular arrows) next to each setting group
3. Click the sync icon to toggle between synced and unsynced
4. Green = synced globally, Gray = independent per instance

### Common Selective Sync Patterns

| Pattern | Synced Settings | Unsynced Settings | Use Case |
|---------|----------------|-------------------|----------|
| **Style sync** | Design tab (fonts, colors, spacing) | Content tab (text, images, links) | Same look, different content per page |
| **Content sync** | Content tab | Design tab | Same content, different styling per context |
| **Full sync** | All settings | None | Identical element everywhere (default) |
| **Layout sync** | Sizing, spacing, position | Content, colors | Consistent structure, flexible appearance |

### Example: Synced CTA with Unique Text

You want a call-to-action button that looks the same everywhere but has different text on different pages:

1. Create a Button module and save it as a global element
2. Open the global element's settings
3. Toggle the **Button Text** setting to unsynced (gray)
4. Keep all Design tab settings synced (green)
5. Now each instance can have different button text while sharing the same styling

## Global Sections

Entire sections can be saved as global elements. This is commonly used for:

- **Header sections** -- A promotional banner that appears on all pages
- **CTA sections** -- A call-to-action band repeated across the site
- **Footer content sections** -- Additional content above the Theme Builder footer
- **Announcement bars** -- Site-wide notices or promotions

## Global Rows

Rows can be saved as global elements when you want to reuse a structured layout with consistent content:

- **Feature comparison rows** -- A row with columns comparing product features
- **Team member rows** -- A row displaying team member cards
- **Pricing rows** -- Pricing tier columns

## Global Modules

Individual modules can be saved as global elements for fine-grained reusability:

- **Contact forms** -- The same form on multiple pages
- **Newsletter signups** -- An email opt-in module used in various locations
- **Social media links** -- Social follow icons with the same accounts
- **Disclaimer text** -- Legal or compliance text blocks

## Converting Back to Regular Elements

If you no longer want an element to be global:

1. Right-click on the global element in the Visual Builder
2. Select **Detach From Global** (or similar option)
3. The element becomes a regular, independent element
4. Future edits to the global element will not affect this detached instance
5. Future edits to this instance will not affect other global instances

!!! tip "Detach Before Major Changes"
    If you want to use a global element as a starting point but customize it for a specific page, detach it first. This preserves the global element unchanged while giving you a local copy to modify freely.

## Code Examples

### Querying Global Library Items

```php
// Get all global elements from the Divi Library
$global_elements = get_posts(array(
    'post_type'      => 'et_pb_layout',
    'posts_per_page' => -1,
    'meta_query'     => array(
        array(
            'key'   => '_et_pb_predefined_layout',
            'value' => 'on',
        ),
    ),
));

foreach ($global_elements as $element) {
    echo $element->post_title . "\n";
}
```

<!-- TODO: Verify the exact meta key for global elements in Divi 5 -->

### Checking if an Element is Global

```php
// Check if a library item is a global element
function is_divi_global_element($post_id) {
    $is_global = get_post_meta($post_id, '_et_pb_predefined_layout', true);
    return $is_global === 'on';
}
```

<!-- TODO: Verify the meta key used for global flag in Divi 5 -->

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Global Elements and Selective Sync functionality has been refined in Divi 5 with improved visual indicators and sync controls.

## Troubleshooting

!!! warning "Global Element Not Syncing"
    If changes to a global element are not appearing on other pages:

    1. Verify the element is still global (look for the green border)
    2. Clear all caching plugins (page cache, object cache, CDN cache)
    3. Check that you saved the changes (click the green Save button)
    4. Hard-refresh the affected pages (Cmd/Ctrl + Shift + R)

!!! warning "Accidentally Edited a Global Element"
    If you accidentally changed a global element and the changes propagated:

    1. Use the **History** feature (clock icon in the toolbar) to undo
    2. Navigate to the revision where the global element had the correct state
    3. Restore that revision
    4. If the history does not go back far enough, check the Divi Library for a previous version of the element

!!! warning "Selective Sync Not Working as Expected"
    If unsynced settings are still changing across instances:

    1. Open the global element's settings
    2. Verify the sync icon status for each setting group
    3. Green = synced (changes propagate), Gray = unsynced (independent)
    4. Toggle the sync icon to the desired state and save

## Related

- [Visual Builder](visual-builder.md) -- The editor where global elements are created and managed
- [Divi Library](library.md) -- Where global elements are stored
- [Presets](presets.md) -- For sharing design settings without sharing content
- [Theme Builder](theme-builder.md) -- Templates that can incorporate global elements
- [Design Variables](design-variables.md) -- Reusable values that keep global elements consistent
