---
title: "Video Slider"
category: modules
tags: ["modules", "slider", "media", "video", "carousel", "gallery", "youtube", "vimeo"]
related: ["video", "slider", "gallery"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10368157-the-video-slider-module-in-divi-5"
---

# Video Slider

The Video Slider module displays a collection of videos in a navigable carousel with thumbnail controls.

## Overview

The Video Slider module lets you present multiple videos in a single, space-efficient component. Instead of stacking several individual video players down the page, the slider consolidates them into a carousel that visitors can browse using navigation arrows and a thumbnail strip. Each video in the collection can be sourced from a self-hosted file upload, YouTube, or Vimeo.

The module renders a main video area at the top with a row of clickable thumbnails below it. Clicking a thumbnail loads that video into the main player. Each video can have its own custom overlay image, and the slider-level controls let you toggle navigation arrow visibility and customize the overall appearance of the playback interface. This layout is well suited for portfolios, course catalogs, product showcases, and any context where multiple videos belong together as a set.

When you only need to embed a single video, use the [Video](video.md) module instead. For image-based slideshows, see the [Slider](slider.md) or [Gallery](gallery.md) modules.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10368157-the-video-slider-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/video-slider/)

![Video Slider module](../assets/screenshots/modules/video-slider/element.png){ loading=lazy }
*The Video Slider module displaying a carousel of videos with thumbnail navigation.*

## Use Cases

1. **Video Portfolio** — Showcase a collection of project highlights, client testimonials, or creative work in a compact carousel that lets visitors browse without leaving the page.
2. **Course or Training Library** — Organize a series of instructional videos into a single slider so students can navigate lessons sequentially through the thumbnail strip.
3. **Product Feature Tours** — Present multiple short videos, each covering a different feature or angle of a product, giving prospective customers a thorough visual overview in one module.

## How to Add the Video Slider Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Video Slider" in the module picker or locate it in the Media category, then click to insert it.

<!-- TODO: Add animated GIF demonstrating module insertion -->

## Settings & Options

The Video Slider module settings are organized across three tabs: Content, Design, and Advanced. The module also contains individual video item settings for each slide.

### Content Tab

The Content tab is where you manage the video collection and configure overlay and background options.

| Setting | Type | Description |
|---------|------|-------------|
| Content (Video Items) | item list | Manage the individual videos in the slider. Click **+** to add a new video, the pencil icon to edit an existing one, the trash icon to delete, and drag to reorder. Each item has its own settings panel (see below). |
| Elements | toggles | Control interface elements such as navigation arrows. Toggle arrows on or off to determine how visitors move between videos in the slider. |
| Overlay | image picker | Set a default overlay image for the main video display area. Individual video items can override this with their own overlays. |
| Background | background controls | Apply a background color, gradient, image, or video behind the entire Video Slider module container. |
| Order | number / select | Control the module's display order when placed inside a Flexbox or CSS Grid container. Useful for reordering elements without moving them in the layer tree. |
| Meta | admin label / visibility | Assign a custom label to identify this module in the Visual Builder's layer panel and optionally force its visibility during editing. |

<!-- ![Video Slider Content tab settings](../assets/screenshots/modules/video-slider/settings-content.png){ loading=lazy } -->
<!-- TODO: Capture Content tab screenshot -->

#### Individual Video Item Settings

Each video within the slider has its own settings panel:

| Setting | Type | Description |
|---------|------|-------------|
| Video | url / upload | Provide the video source for this item. Upload an MP4 file through the media library or paste a YouTube or Vimeo URL. |
| Overlay | image picker | Assign a custom thumbnail image for this specific video. This image appears in the thumbnail strip and as the overlay on the main player when this item is selected. |

### Design Tab

The Design tab controls the visual styling of the slider controls, player area, and overall module appearance.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Controls | control styling | Customize the appearance of the slider's navigation elements, including the play icon styling, thumbnail overlay effects, and slider arrow controls. Adjust colors and sizes to match your brand. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, min-height, height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding with responsive breakpoint controls |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Horizontal/vertical offset, blur, spread, color, position |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue rotation, blur, invert, sepia, opacity, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, direction, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional logic, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (slider container, thumbnails, play icon, arrows) |
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
/* Add rounded corners and depth to the video slider */
.et_pb_video_slider {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

/* Style the thumbnail strip */
.et_pb_video_slider .et_pb_slider_controls_container {
    background: #1a1a2e;
    padding: 10px;
}

/* Highlight the active thumbnail */
.et_pb_video_slider .et_pb_slider_controls .et_pb_slide_active {
    border: 2px solid #2ea3f2;
    border-radius: 4px;
}

/* Hide navigation arrows on mobile for a cleaner look */
@media (max-width: 767px) {
    .et_pb_video_slider .et-pb-slider-arrows {
        display: none;
    }
}

/* Responsive spacing */
@media (max-width: 980px) {
    .et_pb_video_slider {
        margin-bottom: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Video Slider module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_video_slider' !== $render_slug) {
        return $output;
    }

    // Add a custom wrapper for tracking or styling
    $output = '<div class="custom-video-slider-wrapper">' . $output . '</div>';

    return $output;
}, 10, 2);
```

## Common Patterns

1. **Portfolio Video Reel** — Add 4-8 project highlight videos with custom overlay thumbnails that show a branded frame from each video. Use a dark background behind the slider and light-colored navigation controls for a cinematic presentation style.

2. **Tutorial Series Navigator** — Create an ordered series of instructional videos with descriptive overlay images. Keep navigation arrows enabled so learners can step forward and backward through the sequence, and use the thumbnail strip as a visual table of contents.

3. **Testimonial Video Collection** — Compile customer testimonial recordings into a single slider. Use consistent overlay images (e.g., each featuring the customer's name and company) to give visitors a quick sense of who is speaking before they click play.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/video-slider` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Child video items | Nested blocks | Each item has video URL and overlay image |

!!! tip "Module Selection Guidance"
    For video collections use Video Slider; for single videos use Video; for image slideshows use Slider or Gallery.

## Saving Your Work

After configuring your Video Slider module, save your changes using one of these methods:

- Click the **green checkmark** at the bottom of the module settings to apply changes.
- Click the **Save** button in the Visual Builder toolbar to persist all page changes.
- Use the keyboard shortcut **Ctrl+S** (Windows) or **Cmd+S** (Mac) to quick-save.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Video Slider module in Divi 5 uses the updated settings panel structure with Content, Design, and Advanced tabs. Some setting names and locations differ from previous versions of Divi.

## Troubleshooting

!!! warning "Videos Not Loading in Slider"
    If one or more videos in the slider fail to play or display:

    - Verify each video URL is correct and publicly accessible. Private YouTube or Vimeo videos may not embed.
    - For self-hosted files, confirm the video format is browser-compatible (MP4 with H.264 encoding is the safest choice).
    - Check that you have not accidentally left a video item with an empty source field.

!!! warning "Thumbnails Not Appearing"
    If the thumbnail strip is missing or shows blank frames:

    - Ensure each video item has an overlay image assigned. Without an overlay, the thumbnail may render as a blank or dark frame.
    - If using **Generate From Video**, the video source must be accessible at build time for the frame to be extracted.
    - Verify that overlay images have not been deleted from the media library.

!!! tip "Performance with Many Videos"
    Video sliders with a large number of items (10+) can impact page load performance. Videos are loaded on demand when selected, but the thumbnail images all load upfront. Use optimized, appropriately sized thumbnail images and consider limiting the slider to 6-8 videos for the best user experience.

## Related

- [Video](video.md)
- [Slider](slider.md)
- [Gallery](gallery.md)
