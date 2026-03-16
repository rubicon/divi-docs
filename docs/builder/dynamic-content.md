---
title: "Dynamic Content"
category: builder
tags: ["builder", "dynamic-content", "custom-fields", "acf", "templates", "variables"]
related: ["loop-builder", "theme-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11622973"
---

# Dynamic Content

Pull live data from WordPress posts, custom fields, site settings, and global variables into any module, so templates automatically adapt to the content they display.

## Overview

Dynamic content in Divi 5 lets you replace static text, images, and design values with tokens that pull data from the WordPress database at render time. Instead of hard-coding a page title, author name, or product price into a module, you insert a dynamic content reference that resolves to the current post's actual data. This is the foundation for building reusable templates in the [Theme Builder](theme-builder.md) and creating data-driven layouts with the [Loop Builder](loop-builder.md).

Divi 5 supports two categories of dynamic content: **Content Tab dynamic fields** (text, images, URLs sourced from post data and custom fields) and **Design Tab dynamic values** (spacing, colors, and fonts sourced from Global Variables). Together, these allow you to build fully dynamic templates where both content and design are driven by centralized data.

For the official Elegant Themes documentation, see [Dynamic Content](https://help.elegantthemes.com/en/articles/11622973) and [Dynamic Content in the Design Tab](https://help.elegantthemes.com/en/articles/13627810).

## Content Tab Dynamic Sources

These dynamic sources are available in text-based fields on the Content Tab (Body, Title, Image, Link URL, etc.):

### WordPress Core Data

| Source | Description |
|--------|-------------|
| Page/Archive Title | The title of the current post, page, or archive |
| Post/Page Excerpt | The excerpt field of the current post or page |
| Post/Page Publish Date | The publication date of the current content |
| Post/Page Comment Count | The number of approved comments on the current content |
| Post/Page Link | The permalink URL of the current content |
| Post/Page Author | The display name of the content author |
| Author Bio | The biographical info from the author's profile |
| Site Title | The site name from WordPress General Settings |
| Site Tagline | The site tagline from WordPress General Settings |
| Current Date | Today's date at render time |
| Featured Image | The featured image of the current post or page |

### Custom Field Sources

| Source | Description |
|--------|-------------|
| Native Custom Fields | Standard WordPress custom fields (post meta) |
| ACF Fields | Advanced Custom Fields plugin fields, including text, image, URL, and other field types |
| Toolset Fields | Toolset plugin custom fields |

### WooCommerce Data

| Source | Description |
|--------|-------------|
| Product Title | WooCommerce product name |
| Product Price | Current price (including sale price if applicable) |
| Product SKU | Stock keeping unit identifier |
| Product Stock | Current stock quantity or status |
| Other Product Fields | Various WooCommerce product data points |

## Design Tab Dynamic Sources

Design Tab fields (spacing, sizing, colors, fonts, borders) support dynamic values through **Global Variables** only. You must create Global Variables before they become available as dynamic options.

| Variable Type | Applicable Settings | Description |
|---------------|-------------------|-------------|
| Number Variables | Spacing, sizing, border radius, line height | Numeric values with units for dimensional properties |
| Color Variables | Background colors, text colors, border colors | Color values for any color-accepting field |
| Font Variables | Font family, weight, style | Typography values for text-related settings |
| Text/String Variables | Any text-accepting design field | String values for miscellaneous design properties |

Only variable types compatible with the current field appear in the dynamic content dropdown. For example, a Padding field only shows Number Variables, while a Background Color field only shows Color Variables.

A **Manage** button appears contextually in the dropdown to let you create or edit variables without leaving the settings panel.

## Inserting Dynamic Content

### In the Content Tab

1. Open the module settings (click the gear icon or double-click the module).
2. Navigate to the **Content** tab.
3. Hover over a text-based field (Body, Title, Module Link URL, Image).
4. Click the **Dynamic Content** icon that appears.
5. Select the desired data source from the dropdown.
6. Click **Apply**.

### In the Design Tab

1. Open the module settings.
2. Navigate to the **Design** tab.
3. Open the relevant option group (e.g., Spacing, Border).
4. Hover over a specific property (e.g., Padding Top).
5. Click the **Dynamic Content** icon.
6. Select a compatible Global Variable from the list.
7. Click **Apply**.

## Before/After Text

Dynamic content fields in the Content Tab support static text wrapping. You can add text before and after the dynamic value, and HTML tags are supported (matching open/close pairs required). For example, you could wrap a dynamic author name with "Written by: " before and no text after.

## Applicable Modules

Content Tab dynamic content is available in text-based modules including:

- Text, Blurb, Call to Action, Button
- Post Title, Heading
- Image (for image source fields)
- WooCommerce modules (for product-specific fields)

Design Tab dynamic content (Global Variables) is available on all modules in any Design Tab field that accepts the matching variable type.

## Common Workflows

### Blog Post Template

Build a single post template in the Theme Builder. Use dynamic content to populate:

- Post Title module with the **Page/Archive Title** source
- Text module with **Post/Page Author** and **Post/Page Publish Date**
- Image module with **Featured Image**
- Text module with the post body content

The template automatically displays the correct data for every post.

### Branded Design System with Variables

1. Create Global Variables for your brand colors, font stack, and standard spacing values.
2. Apply these variables as dynamic Design Tab values across all modules.
3. To rebrand, update the Global Variables once. All modules referencing those variables update site-wide.

### WooCommerce Product Page

Use dynamic WooCommerce sources to build a custom product page template. Pull product title, price, SKU, and stock status into individual modules, then style them with your custom layout.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Dynamic content references are stored as tokens or placeholder objects within the block's `attrs` in `post_content`. Rather than storing the resolved value, the block stores a reference to the data source (e.g., `post_title`, `custom_field:field_name`) that is resolved at render time. Design Tab dynamic values store references to Global Variable IDs.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Parse block `attrs` in `post_content` for dynamic content tokens/references | Needs Testing | Look for attribute values that contain dynamic source identifiers rather than plain text |
| Modify | Replace the dynamic token with a different source reference or a static value | Needs Testing | Token format (syntax, delimiters, source key structure) needs investigation |
| Create | Insert a dynamic content token into a block attribute value | Needs Testing | Must match the expected token format; Global Variables are likely referenced by ID |

!!! warning "Global Variable Dependencies"
    Dynamic Design Tab values reference Global Variables by ID. Deleting a Global Variable will break all dynamic references to it across the site. When programmatically managing variables, check for references before deletion.

## Troubleshooting

!!! warning "Dynamic Content Icon Not Appearing"
    The dynamic content icon only appears on compatible fields when you hover over them. If it does not appear, the field may not support dynamic content (e.g., toggle switches, dropdown selects with fixed options).

!!! warning "Design Tab Shows No Variables"
    If the Design Tab dynamic content dropdown is empty, you have not yet created Global Variables of the matching type. Use the **Manage** button or navigate to the Variables panel to create them first.

!!! warning "Dynamic Content Displays Raw Token"
    If you see a raw token string instead of resolved content on the front end, the dynamic source may be invalid or the referenced data may not exist for the current context (e.g., referencing a custom field that does not exist on the current post).

## Related

- [Loop Builder](loop-builder.md)
- [Theme Builder](theme-builder.md)
- [Presets](presets.md)
- [Visual Builder](visual-builder.md)
