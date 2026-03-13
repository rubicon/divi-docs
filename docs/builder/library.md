---
title: "Divi Library"
category: builder
tags: [builder, library, layouts, templates, import, export]
related: [visual-builder, global-elements, presets]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: ""
---

# Divi Library

The Divi Library is a built-in system for saving, organizing, and reusing layouts, sections, rows, and modules across your website.

## Overview

Every Divi installation includes access to the Divi Library, where you can save design elements for reuse. Whether you have crafted a perfect hero section, a contact form layout, or an entire page design, you can save it to the library and load it onto any page with a few clicks.

The library supports saving individual modules, rows, sections, or complete page layouts. Items can be organized with categories and tags, and can be exported as JSON files for use on other Divi websites. The library also integrates with Divi Cloud, giving you access to your saved designs across all websites connected to your Elegant Themes account.

Divi also ships with hundreds of professionally designed premade layouts organized into layout packs. These provide ready-to-use page designs that you can load and customize.

<!-- ![Divi Library overview](../assets/screenshots/builder/library/overview.png){ loading=lazy }
*The Divi Library interface showing saved layouts, premade layouts, and organization options.* -->

## Accessing the Library

There are multiple ways to access the Divi Library:

| Method | How |
|--------|-----|
| **Visual Builder Toolbar** | Click the **plus (+)** icon in the middle of the bottom toolbar |
| **WordPress Admin** | Navigate to **Divi > Divi Library** in the admin sidebar |
| **New Page Prompt** | Select **Choose A Premade Layout** when creating a new page |
| **Element Save** | Click the **down arrow** icon in the toolbar to save the current layout |

## Saving to the Library

### Saving a Full Page Layout

1. With your page design complete in the Visual Builder, click the **down arrow** icon in the bottom toolbar
2. Give your layout a name
3. Optionally assign categories and tags for organization
4. Choose whether to save to the local library, Divi Cloud, or both
5. Click **Save To Library**

### Saving Individual Elements

You can save any section, row, or module individually:

1. Open the element's settings (click the gear icon)
2. Click the **three-dot menu** (vertical ellipsis)
3. Select **Save To Library** or **Save To Divi Cloud**
4. Name the element and assign categories/tags
5. Click **Save To Library**

### Save Options

| Option | Description |
|--------|-------------|
| **Save To Library** | Saves to the local WordPress installation. Available only on this website. |
| **Save To Divi Cloud** | Saves to your Elegant Themes cloud account. Available on any Divi website signed in with your account. |
| **Save As Global** | Saves the element as a [Global Element](global-elements.md) that syncs changes across all instances. |

## Loading from the Library

### Loading a Layout onto a Page

1. Open the Divi Library (click the **+** icon in the toolbar)
2. Browse the available tabs:
   - **Premade Layouts** -- Hundreds of professionally designed layout packs
   - **Your Saved Layouts** -- Layouts you have saved, including Divi Cloud items
   - **Clone Existing Page** -- Copy a design from another page on your site
3. Click on a layout to preview it
4. Click **Use This Layout** to load it onto your page

!!! warning "Loading a Layout Replaces Content"
    Loading a full layout will replace the current page content. If you want to add a saved element to an existing design rather than replace it, load individual sections, rows, or modules instead.

### Loading Individual Elements

1. When adding a new section, row, or module, click **Add From Library**
2. Browse or search your saved elements
3. Click to insert the element into your page

## Premade Layouts

Divi includes hundreds of free layout packs designed by the Elegant Themes team. Each pack typically includes multiple page designs (homepage, about, services, contact, blog, etc.) that share a cohesive visual style.

### Browsing Premade Layouts

1. Open the Divi Library in the Visual Builder
2. Click the **Premade Layouts** tab
3. Use the left sidebar to filter by category
4. Use the search bar to find specific designs
5. Click a layout pack to view all pages in the pack
6. Select and load the page design you want

## Organizing Library Items

### Categories and Tags

When saving items to the library, assign categories and tags for easy organization:

- **Categories** -- Broad groupings (e.g., "Headers", "Hero Sections", "Contact Forms")
- **Tags** -- Specific labels (e.g., "dark-theme", "minimal", "client-abc")

### Managing Library Items

In the WordPress admin under **Divi > Divi Library**:

| Action | How |
|--------|-----|
| **Edit** | Click on any library item to open it in the Visual Builder for editing |
| **Delete** | Hover over an item and click **Trash** |
| **Rename** | Click **Quick Edit** to change the title, category, or tags |
| **Bulk Actions** | Select multiple items and use the Bulk Actions dropdown to delete or move |

## Importing and Exporting

### Exporting Layouts

1. Navigate to **Divi > Divi Library** in the WordPress admin
2. Click the **Import & Export** button at the top
3. Select the **Export** tab
4. Choose to export all library items or select specific items
5. Click **Export Divi Builder Layouts**
6. A JSON file will download to your computer

### Importing Layouts

1. Navigate to **Divi > Divi Library**
2. Click the **Import & Export** button
3. Select the **Import** tab
4. Click **Choose File** and select a Divi JSON export file
5. Choose import options:

| Option | Description |
|--------|-------------|
| **Override Existing Defaults** | Replace existing default templates with imported ones |
| **Import Presets** | Include any presets saved with the layouts |
6. Click **Import Divi Builder Layouts**

### Portability (Page-Level)

You can also import/export individual page designs directly from the Visual Builder:

1. Click the **Import/Export** icon in the bottom toolbar (two arrows)
2. Choose **Export** to download the current page layout as JSON
3. On another page or site, use **Import** to upload and load the layout

!!! tip "Sharing Designs Between Sites"
    Use Divi Cloud for seamless sharing between sites, or export/import JSON files for one-time transfers. Divi Cloud is the better option for designs you use regularly across multiple projects.

## Divi Cloud

Divi Cloud is a cloud-based extension of the Divi Library that stores your designs on Elegant Themes' servers, making them accessible across all your Divi websites.

| Feature | Local Library | Divi Cloud |
|---------|--------------|------------|
| **Storage** | WordPress database | Elegant Themes servers |
| **Access** | This website only | Any Divi website with your account |
| **Sync** | Manual export/import | Automatic |
| **Included with** | All Divi licenses | All Divi licenses |

## Code Examples

### Programmatically Adding a Library Layout via PHP

```php
// Load a Divi Library layout by ID onto a page
function load_divi_library_layout($layout_id) {
    $layout = get_post($layout_id);
    if ($layout && $layout->post_type === 'et_pb_layout') {
        return $layout->post_content;
    }
    return '';
}
```

### Querying Library Items

```php
// Get all Divi Library items in a specific category
$library_items = get_posts(array(
    'post_type'      => 'et_pb_layout',
    'posts_per_page' => -1,
    'tax_query'      => array(
        array(
            'taxonomy' => 'layout_category',
            'field'    => 'slug',
            'terms'    => 'headers',
        ),
    ),
));
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Divi Library interface has been refined in Divi 5 with improved browsing and search capabilities.

## Troubleshooting

!!! warning "Library Items Not Appearing"
    If saved library items do not appear when browsing:

    1. Check that you are looking in the correct tab (Your Saved Layouts vs. Premade Layouts)
    2. Clear any active filters or search terms
    3. Verify the items were saved to the local library and not only to Divi Cloud (or vice versa)
    4. Check that the library item's post status is "Published" in the WordPress admin

!!! warning "Import Fails or Timeout"
    If importing a large library file fails:

    1. Increase the PHP `max_execution_time` in your server configuration
    2. Increase the `upload_max_filesize` and `post_max_size` PHP settings
    3. Try importing smaller batches of layouts instead of the full collection
    4. Check your hosting provider's file upload limits

## Related

- [Visual Builder](visual-builder.md) -- The editor where you create and load library layouts
- [Theme Builder](theme-builder.md) -- Template system that can use library elements
- [Presets](presets.md) -- Saved styling configurations for elements
- [Global Elements](global-elements.md) -- Synced elements saved to the library
