---
title: "Audio"
category: modules
tags: ["modules", "media", "audio", "music", "podcast", "mp3", "player"]
related: ["video", "video-slider"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10125708-the-audio-module-in-divi-5"
---

# Audio

The Audio module embeds an audio player with optional album artwork, title, and artist metadata.

## Overview

The Audio module provides a fully styled, browser-native audio player that you can drop into any page layout. It wraps the standard HTML5 `<audio>` element with Divi's design controls, letting you present music tracks, podcast episodes, voice recordings, or any other audio file with a polished, on-brand appearance.

Beyond basic playback, the module supports an accompanying cover image, making it well suited for album art, podcast artwork, or episode thumbnails. You can also display a title and artist/caption alongside the player, giving visitors the context they need without leaving the page.

Because the module relies on the browser's native audio capabilities, it supports common formats such as MP3, OGG, and WAV. Upload files to the WordPress Media Library and select them from within the module settings, or paste an external URL to a hosted audio file.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10125708-the-audio-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/audio/)

![Audio module](../assets/screenshots/modules/audio/element.png){ loading=lazy }
*The Audio module displaying a track with cover artwork and playback controls.*

## Use Cases

1. **Podcast Episode Player** — Embed individual episodes directly on a show notes page so visitors can listen without navigating to a third-party platform.
2. **Music Portfolio** — Showcase original compositions or production samples with album artwork, giving prospective clients or fans an inline listening experience.
3. **Guided Meditation or Course Audio** — Offer audio lessons, meditations, or training recordings alongside written content for a multimedia learning experience.

## How to Add the Audio Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Audio" in the module picker or locate it in the Media category, then click to insert it.

<!-- TODO: Add animated GIF demonstrating module insertion -->

## Settings & Options

The Audio module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the audio source, accompanying text and image, link behavior, background, and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Text | text fields | Enter the track title and artist or description that display above the audio player. |
| Audio | file upload / URL | Select or upload an audio file (MP3, OGG, WAV) from the Media Library, or paste an external audio URL. This is the file the player will stream. |
| Image | image upload | Upload or select a cover image displayed alongside the player. Commonly used for album art, podcast artwork, or a branded thumbnail. |
| Link | URL | Optionally wrap the module in a link so clicking navigates to another page or resource. |
| Background | background controls | Apply a background color, gradient, image, or video behind the entire Audio module container. |
| Loop | toggle | When enabled, the module output can be repeated in loop-based layouts such as post type archives or custom queries. |
| Order | select | Control the display order when the module is used inside a loop or dynamic layout context. |
| Meta | admin label | Set an internal admin label to identify this module in the Visual Builder's layer panel and search. |

<!-- ![Audio Content tab settings](../assets/screenshots/modules/audio/settings-content.png){ loading=lazy } -->
<!-- TODO: Capture Content tab screenshot -->

### Design Tab

The Design tab controls all visual styling for the audio player and its surrounding elements.

| Setting | Type | Description |
|---------|------|-------------|
| Image | image styling | Adjust the cover image dimensions, alignment, and how it is displayed relative to the player. |
| Text | text styling | Set general text properties like font family, weight, style, color, and line height for all text in the module. |
| Title Text | text styling | Style the track title independently — font family, size, color, letter spacing, line height, and text shadow. |
| Caption Text | text styling | Style the artist or caption text below the title with its own font, size, color, and spacing values. |
| Sizing | dimensions | Control the module's width, max-width, min-height, and height. |
| Spacing | margin / padding | Set margin and padding values around and within the module. Supports responsive values per device breakpoint. |
| Border | border controls | Add borders around the module or specific internal elements — configure width, color, style, and border radius. |
| Box Shadow | shadow controls | Apply a box shadow with customizable horizontal/vertical offset, blur, spread, color, and position (outer or inner). |
| Filters | CSS filters | Apply visual filter effects such as brightness, contrast, saturation, blur, hue rotation, and inversion. |
| Transform | transform controls | Apply CSS transforms including scale, translate, rotate, skew, and set the transform origin point. |
| Animation | animation select | Choose an entrance animation (fade, slide, bounce, zoom, flip, fold, roll) with configurable speed, delay, intensity, and starting opacity. |

<!-- ![Audio Design tab settings](../assets/screenshots/modules/audio/settings-design.png){ loading=lazy } -->
<!-- TODO: Capture Design tab screenshot -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, and scroll-driven effects.

| Setting | Type | Description |
|---------|------|-------------|
| Attributes | text fields | Assign a CSS ID and CSS classes to the module for precise targeting with custom styles or JavaScript. |
| CSS | code editor | Write custom CSS scoped to specific internal elements of the module (container, image, title, player, etc.). |
| HTML | code fields | Add custom HTML attributes to the module's wrapper element for accessibility or integration needs. |
| Conditions | condition builder | Define display conditions so the module only renders based on rules such as user role, page type, date range, or custom logic. |
| Interactions | interaction builder | Configure hover, click, or scroll-triggered interactions that affect this module or other page elements. |
| Visibility | device toggles | Show or hide the module on desktop, tablet, and/or phone. Hidden modules are excluded from the page source for that device. |
| Transitions | transition controls | Set CSS transition duration, easing function, and delay for smooth hover-state changes. |
| Position | position controls | Set the CSS position property (relative, absolute, fixed, sticky) along with offset values and z-index. |
| Scroll Effects | scroll controls | Apply scroll-driven effects like parallax, fade, scale, rotate, blur, or horizontal movement triggered as the user scrolls. |

<!-- ![Audio Advanced tab settings](../assets/screenshots/modules/audio/settings-advanced.png){ loading=lazy } -->
<!-- TODO: Capture Advanced tab screenshot -->

## Code Examples

### Custom CSS

```css
/* Style the Audio module container */
.et_pb_audio_module {
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 30px;
}

/* Style the cover image area */
.et_pb_audio_module .et_pb_audio_cover_art {
    max-width: 200px;
    border-radius: 8px;
}

/* Style the track title */
.et_pb_audio_module h2 {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 4px;
}

/* Customize the playback controls bar */
.et_pb_audio_module .mejs-container {
    background: transparent;
}

.et_pb_audio_module .mejs-controls .mejs-time-rail .mejs-time-total {
    border-radius: 4px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_audio_module .et_pb_audio_cover_art {
        max-width: 150px;
    }
    .et_pb_audio_module h2 {
        font-size: 18px;
    }
}
```

### PHP Hooks

```php
/* Filter the Audio module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_audio' !== $render_slug) {
        return $output;
    }
    // Example: add a download link after the player
    $output .= '<a href="#" class="audio-download-link">Download Episode</a>';
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Podcast Show Notes Layout** — Place the Audio module at the top of a blog post, followed by a text module with episode show notes and timestamps. Set a branded cover image and use the title field for the episode name.

2. **Music Portfolio Grid** — Arrange multiple Audio modules in a multi-column row to create a grid of playable tracks. Give each a unique cover image and keep titles short so the layout stays compact and scannable.

3. **Background Ambience Player** — Use a single Audio module in a sticky footer or sidebar section to provide ambient background audio. Style it with a minimal design, reduced spacing, and subtle colors so it does not compete with primary content.

## Saving Your Work

After configuring the Audio module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Audio File Not Playing"
    If the player appears but no audio plays, verify that:

    - The audio file URL is accessible and not behind authentication
    - The file format is supported by browsers (MP3 is the most widely compatible)
    - Your hosting server allows direct file access and has not blocked the MIME type

!!! warning "Cover Image Not Displaying"
    If the uploaded image does not appear beside the player:

    - Confirm the image was uploaded to the Media Library and the URL is valid
    - Check that Design tab image sizing settings are not collapsing the image to zero dimensions
    - Verify no custom CSS is hiding the `.et_pb_audio_cover_art` element

!!! tip "Player Looks Unstyled or Broken"
    The Audio module relies on the MediaElement.js library bundled with WordPress. If the player appears as a plain HTML5 control, check that no optimization plugin is deferring or combining the mediaelement scripts incorrectly. Exclude `wp-mediaelement` from script optimization to restore styling.

## Related

- [Video](video.md) — Embed video content with a similar media-focused layout
- [Video Slider](video-slider.md) — Present multiple videos in a sliding carousel format
