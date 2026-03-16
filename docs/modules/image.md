---
title: "Image"
category: modules
tags: ["modules", "media", "image", "lightbox", "visual", "content"]
related: ["gallery", "blurb", "icon"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10315772-the-image-module-in-divi-5"
---

# Image

The Image module displays a single image with optional linking, lightbox functionality, and extensive styling controls.

## Overview

The Image module is one of the most fundamental building blocks in Divi 5. It allows you to place a single image anywhere within your page layout and provides full control over how that image is presented, sized, aligned, and animated. Whether you need a simple photo in a blog post, a clickable banner linking to another page, or a lightbox-enabled portfolio piece, the Image module handles all of these scenarios without requiring any custom code.

Divi 5 gives the Image module a complete set of responsive design controls, so you can fine-tune the appearance on desktop, tablet, and phone independently. The built-in CSS filter controls let you adjust properties like brightness, contrast, saturation, and blur directly within the Visual Builder, eliminating the need to edit images in an external application. You can also apply overlay effects, box shadows, border radius adjustments, and entrance animations to create polished, interactive image presentations.

The module integrates seamlessly with other Divi 5 elements. Pair it with a [Blurb](blurb.md) module for image-and-text cards, arrange several Image modules in a multi-column row for a custom [Gallery](gallery.md)-style grid, or use the [Icon](icon.md) module alongside it for decorative accents. The Image module supports linking to any URL or opening the full-resolution version in a built-in lightbox overlay, making it versatile enough for hero sections, product showcases, team photos, and more.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10315772-the-image-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/image/)

![Image module](../assets/screenshots/modules/image/element.png){ loading=lazy }
*The Image module as it appears in the Divi 5 Visual Builder.*

## Use Cases

1. **Hero and Banner Images** — Place a full-width image at the top of a page or section to create a striking visual introduction. Combine with entrance animations and responsive sizing to ensure the hero looks great across all devices.

2. **Linked Product or Portfolio Images** — Use the link setting to make images clickable, directing visitors to product detail pages, case studies, or external resources. Enable the lightbox for portfolio galleries where visitors can view full-resolution versions.

3. **Decorative Section Accents** — Insert styled images with border radius, box shadows, and CSS filters to create visually distinct section dividers, background accents, or testimonial photos that match your brand aesthetic.

## How to Add the Image Module

1. **Open the Visual Builder** — Navigate to the page you want to edit and activate the Divi 5 Visual Builder. Click the plus icon in the section and row where you want the image to appear.

2. **Select the Image Module** — In the module picker, search for "Image" or find it in the module list. Click to insert it into your chosen column.

3. **Upload or Select an Image** — In the Content tab, click the image upload area to choose an image from your WordPress Media Library or upload a new file. Configure any link, lightbox, or alignment settings, then adjust the Design and Advanced tabs as needed.

## Settings & Options

### Content Tab

The Content tab holds the core settings for selecting your image and configuring how it behaves when clicked.

| Setting | Type | Description |
|---------|------|-------------|
| Image | upload | Upload or select an image from the WordPress Media Library. Supports JPG, PNG, GIF, WebP, and SVG formats. This is the primary content of the module. |
| Link | group | Contains settings for linking the image to a URL. Includes the destination URL, whether it opens in the same window or a new tab, and whether the lightbox is enabled. When lightbox is active, clicking the image opens the full-size version in an overlay. |
| Background | group | Apply a background color, gradient, or image behind the module container. Useful for adding padding around the image with a colored backdrop. |
| Loop | toggle | When used inside a dynamic layout such as a Theme Builder template, this setting controls whether the module repeats for each item in a post loop. |
| Order | select | Determines the display order of the module when multiple modules exist within the same container. Useful for reordering elements without dragging in the builder. |
| Meta | group | Contains the admin label field, which lets you assign a custom name to the module for easier identification in the Visual Builder layers panel. |

### Design Tab

The Design tab provides visual customization options for the image and the module container.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Alignment | select | Controls the horizontal alignment of the image within its column — left, center, or right. Supports responsive values for different device breakpoints. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Overlay](../options-groups/overlay.md) | Hover overlay icon, color, and opacity |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding per side, responsive breakpoints |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Color, offsets, blur radius, spread |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue, blur, invert, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (main element, image tag, overlay) |
| HTML | Custom HTML attributes for module wrapper (data attributes, ARIA labels) |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

## Code Examples

### Custom CSS — Hover Zoom Effect

```css
/* Smooth zoom on hover with overflow hidden */
.et_pb_image {
    overflow: hidden;
    border-radius: 8px;
}

.et_pb_image img {
    transition: transform 0.4s ease;
}

.et_pb_image:hover img {
    transform: scale(1.08);
}
```

### Custom CSS — Fixed Aspect Ratio

```css
/* Force a 16:9 aspect ratio on all images */
.et_pb_image {
    aspect-ratio: 16 / 9;
    overflow: hidden;
}

.et_pb_image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

### Custom CSS — Color Overlay on Hover

```css
/* Dark overlay that fades in on hover */
.et_pb_image {
    position: relative;
}

.et_pb_image::after {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
}

.et_pb_image:hover::after {
    opacity: 1;
}
```

### Custom CSS — Responsive Image Sizing

```css
/* Constrain images on desktop, full-width on mobile */
.et_pb_image {
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

@media (max-width: 980px) {
    .et_pb_image {
        max-width: 100%;
        padding: 0 15px;
    }
}
```

### PHP — Add a Wrapper Around Image Modules

```php
/* Wrap every Image module in a custom div */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_image' !== $render_slug) {
        return $output;
    }

    return '<div class="custom-image-wrapper">' . $output . '</div>';
}, 10, 2);
```

## Common Patterns

### 1. Full-Width Hero Image

Place the Image module inside a fullwidth section at the top of a page. Set the max-width to 100% and remove all margin and padding for edge-to-edge display. Apply a fade or slide-up entrance animation for visual impact when the page loads. This pattern works well for landing pages, portfolio headers, and campaign pages.

### 2. Image Card Grid

Arrange multiple Image modules in a three- or four-column row. Apply a consistent border radius of 8-12px and a subtle box shadow to each image to create a card-like appearance. Use the fixed aspect ratio CSS snippet above with a shared CSS class to ensure all images maintain the same proportions regardless of their original dimensions.

### 3. Lightbox Portfolio Gallery

Enable the lightbox setting on multiple Image modules within the same section. Divi groups lightbox-enabled images together, allowing visitors to click any image and navigate through all of them in a slideshow overlay. Add a hover zoom effect and an overlay icon for clear visual feedback that the images are interactive.

## Saving Your Work

After configuring the Image module, click the green checkmark button at the bottom of the settings panel to apply your changes. Then save the page using the save button in the Visual Builder toolbar, or use the keyboard shortcut Ctrl+S (Cmd+S on Mac). Changes are not published until you explicitly save the page.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Image Not Displaying"
    If the Image module appears empty on the front end:

    - Verify an image is selected in the Content tab — the upload field should show a thumbnail preview.
    - Check that the image file still exists in the WordPress Media Library and has not been deleted.
    - Confirm the image URL is accessible and not returning a 404 error. Migrated sites may have broken media paths.
    - Inspect the Visibility settings in the Advanced tab to ensure the module is not hidden on the current device type.
    - Clear any page caching plugin or CDN cache after uploading or replacing an image.

!!! warning "Lightbox Not Opening"
    If clicking the image does not open the lightbox overlay:

    - Confirm the lightbox option is enabled in the Content tab link settings.
    - Open the browser developer console (F12) and check for JavaScript errors that may be blocking the lightbox script.
    - Disable other lightbox or gallery plugins temporarily to rule out conflicts.
    - Ensure Divi's JavaScript files are loading correctly — minification or script deferral plugins can sometimes break the lightbox initialization order.

!!! warning "Image Appears Blurry or Stretched"
    If the displayed image looks low-quality or distorted:

    - Check the source image resolution — it should be at least as large as the display size to avoid upscaling.
    - Verify that the sizing settings in the Design tab are not forcing the image to stretch beyond its native dimensions.
    - If WordPress is serving a smaller thumbnail size, navigate to Settings > Media in the WordPress admin and adjust the image size defaults, or re-upload the image at a higher resolution.

## Related

- [Gallery](gallery.md) — Display multiple images in a grid or slider layout
- [Blurb](blurb.md) — Combine an image or icon with a title and text block
- [Icon](icon.md) — Display a standalone icon with optional linking and styling
