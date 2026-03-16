---
title: "Canvases"
category: builder
tags: ["builder", "canvases", "off-canvas", "popups", "global-canvas", "canvas-portal"]
related: ["nested-modules", "interactions"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13249775"
---

# Canvases

Separate workspaces within the Divi builder for organizing off-canvas content like popups, slide-in menus, and reusable global components.

## Overview

Canvases in Divi 5 are independent content areas attached to a page or template. Every page starts with a Main Canvas that holds the visible page content. You can create additional Local Canvases for page-specific off-canvas elements (menus, popups, modal dialogs) or Global Canvases that are shared across every page on the site.

Canvases keep off-canvas content organized and separate from the main page layout. The content on a non-main canvas remains hidden until triggered by an [Interaction](interactions.md), making them the foundation for dynamic UI patterns like slide-in navigation, popup announcements, and mega menus.

For the official Elegant Themes documentation, see [Canvases](https://help.elegantthemes.com/en/articles/13249775).

## Canvas Types

| Type | Scope | Description |
|------|-------|-------------|
| Main Canvas | Per page/template | The primary visible content area. Every page has exactly one Main Canvas. |
| Local Canvas | Per page/template | Additional canvases attached to a specific page or template. Content is only available on that page. Used for page-specific popups, menus, or staging areas. |
| Global Canvas | Site-wide | Canvases that are shared across all pages and templates. Used for site-wide elements like a global notification bar or mobile menu. |

## Creating and Managing Canvases

### Access Point

The Canvas dropdown is located at the top of the Divi 5 Visual Builder interface. From this dropdown you can:

- Switch between existing canvases
- Add a new canvas
- Mark a canvas as global
- Configure auto-append behavior
- Open grid view for a visual overview of all canvases
- Assign any canvas as the Main Canvas

### Canvas Actions

Right-click a canvas in the dropdown to access management options:

| Action | Description |
|--------|-------------|
| Edit | Open the canvas for editing in the builder |
| Duplicate | Create a copy of the canvas with all its content |
| Export | Export the canvas content for reuse |
| Delete | Remove the canvas and its content |
| Set as Main | Designate this canvas as the primary visible content area |
| Mark as Global | Convert a local canvas to a global canvas shared across the site |

## Working with Off-Canvas Content

### Building Off-Canvas Components

1. Create a new Local or Global Canvas from the canvas dropdown.
2. Design the off-canvas content (menu, popup, notification bar) on the new canvas.
3. Style and configure the content independently from the main page.
4. The content remains hidden from the front-end visitor until triggered.

### Connecting to Interactions

Off-canvas content is displayed to visitors through the [Interactions](interactions.md) system:

| Trigger Type | Use Case | Description |
|--------------|----------|-------------|
| Click | Toggle menus | A button click shows or hides the off-canvas menu section |
| Viewport/Scroll | Trigger popups | Content appears when the user scrolls to a certain position |
| Hover | Mega menus | Menu content appears when hovering over a navigation link |
| Load | Welcome popups | Content displays automatically when the page finishes loading |

When an interaction targets content on a separate canvas, that content is automatically appended to the main canvas on the front end and shown or hidden based on the trigger.

### Animation Support

Sections placed on canvases support animation settings for their entrance and exit:

- Slide in from left, right, top, or bottom
- Fade in and fade out
- Custom timing and easing curves

These animations are configured in the section's **Design Tab > Animation** settings on the canvas.

## Canvas Portal Module

The Canvas Portal module lets you inject content from one canvas into a specific location on another canvas (typically the Main Canvas).

### Setup Process

1. Build your content on a dedicated canvas.
2. On the Main Canvas, place a **Canvas Portal** module where you want the content to appear.
3. In the Canvas Portal settings, select the source canvas.
4. The portal renders the source canvas content at that exact position in the layout.

This is useful when you need off-canvas content to appear inline within the page layout rather than as an overlay. Canvas Portals also work with nested elements, allowing precise placement relative to parent containers.

## Staging and Experimentation

Canvases serve as safe experimentation areas beyond their off-canvas functionality:

- **Design experiments**: Duplicate the Main Canvas to test layout changes without affecting the live page.
- **A/B testing**: Create variant canvases and swap the Main Canvas designation to compare designs.
- **Preset development**: Build and refine element presets on a staging canvas before applying them to the main layout.

Changes made on non-main canvases do not affect the visible page until you explicitly connect them via interactions or canvas portals.

## Grid View

The grid view (accessible from the canvas dropdown) displays all canvases attached to the current page or template in a visual overview. This makes it easy to see how many canvases exist and quickly switch between them.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Canvases are a new concept in Divi 5 with no equivalent in Divi 4.

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Canvas content storage and its relationship to `post_content` requires investigation. Local canvases may be stored as separate block trees within the same post, or they may use a dedicated meta field or custom table. Global canvases likely use a separate post type or options entry since they span multiple pages.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Query `post_content` or associated meta for canvas block trees | Needs Testing | Main canvas content is in `post_content`; additional canvases may be in `post_meta` or a separate structure |
| Modify | Update the appropriate canvas block tree and serialize back | Needs Testing | Must identify the correct storage location for each canvas type |
| Create | Insert a new canvas block tree into the post's canvas storage | Needs Testing | Global canvases may require creating entries in a shared location (options table or custom post type) |

!!! warning "Global Canvas Scope"
    Global canvases are shared across all pages. Programmatic modifications to a global canvas will affect every page on the site. Always verify the canvas scope before making bulk changes.

## Troubleshooting

!!! warning "Off-Canvas Content Not Appearing"
    If off-canvas content does not display on the front end, verify that an Interaction is configured to target the canvas content and that the trigger condition is being met. Canvas content is hidden by default without an interaction.

!!! warning "Canvas Portal Not Rendering"
    If a Canvas Portal module shows blank content, confirm that the source canvas has been selected in the module settings and that the source canvas contains published content.

## Related

- [Nested Modules](nested-modules.md)
- [Interactions](interactions.md)
- [Visual Builder](visual-builder.md)
