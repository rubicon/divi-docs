---
title: "Fullwidth Slider"
category: modules
tags: ["modules", "fullwidth", "slider", "slideshow", "carousel", "hero", "call-to-action", "parallax"]
related: ["slider", "post-slider", "video-slider", "fullwidth-header"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://www.elegantthemes.com/documentation/divi/slider-fullwidth/"
---

# Fullwidth Slider

The Fullwidth Slider module displays a full-width slideshow with customizable slides that can include titles, body text, buttons, images, and video backgrounds.

## Overview

The Fullwidth Slider module creates an edge-to-edge slideshow that spans the entire browser width. Each slide can contain a heading, descriptive text, a call-to-action button, and a background image or video, making it one of the most versatile modules for hero sections, promotional banners, and feature highlights. The module supports parallax background effects and full-width video backgrounds for cinematic presentations.

Slides are managed individually within the module, so each one can have its own unique content, background, and styling. Navigation arrows and dot indicators let visitors move between slides manually, while auto-advancement can cycle through slides on a timer. The fullwidth format ensures maximum visual impact regardless of the visitor's screen resolution.

The Fullwidth Slider differs from the standard [Slider](slider.md) module only in that it must be placed inside a fullwidth section and stretches to fill the entire viewport width. It shares the same slide-level content structure and most design controls. For sliders that automatically pull from blog posts, see the [Post Slider](post-slider.md) module. For video-focused slideshows, see the [Video Slider](video-slider.md) module.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10364612-the-slider-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/fullwidth-slider/)

![Fullwidth Slider module](../assets/screenshots/modules/fullwidth-slider/element.png){ loading=lazy }
*The Fullwidth Slider module displaying a hero-style slide with title, text, and call-to-action button.*

## Use Cases

1. **Homepage Hero Banner** — Create an attention-grabbing first impression with a fullwidth slideshow cycling through your key offerings. Each slide can feature a different product, service, or value proposition with a unique background image and CTA button.

2. **Promotional Campaign Rotator** — Display time-sensitive promotions, seasonal offers, or event announcements in a rotating slideshow. Update individual slides without rebuilding the entire section, and use the button on each slide to link directly to the relevant landing page.

3. **Visual Storytelling Section** — Use the slider mid-page to break up text-heavy content with a sequence of full-bleed images and captions. Parallax backgrounds and video slides add depth and movement that keeps visitors engaged as they scroll.

## How to Add the Fullwidth Slider Module

1. Open the Visual Builder on the page you want to edit. Add a **Fullwidth Section** if one does not already exist, since this module requires a fullwidth section.
2. Click the gray **+** icon inside the fullwidth section to add a new module.
3. Search for "Fullwidth Slider" in the module picker or locate it in the Fullwidth Modules category, then click to insert it. The module will appear with one default slide ready for editing.

## Settings & Options

The Fullwidth Slider module settings are organized across three tabs at the module level. Each individual slide also has its own settings panel.

### Content Tab

The Content tab manages the collection of slides, navigation elements, and module-level metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Slides | item list | Manage individual slides within the slider. Click **+** to add a new slide, the pencil icon to edit, the trash icon to delete, and drag to reorder. Each slide opens its own settings panel. |
| Elements — Show Arrows | toggle | Display or hide the left/right navigation arrows that allow visitors to move between slides manually. |
| Elements — Show Dot Navigation | toggle | Display or hide the dot indicators below the slider that show the current slide position and allow direct navigation. |
| Link | url | Optionally make the entire slider module clickable, directing visitors to a specified URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the slider module itself (visible if slides do not fully cover the area). |
| Loop | toggle | When enabled, activates the Loop Builder functionality for repeating the module in dynamic layouts. |
| Order | select | Control the module's placement order within Flexbox and Grid parent layouts. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |

#### Individual Slide Settings

Each slide within the Fullwidth Slider has its own settings panel with the following options:

| Setting | Type | Description |
|---------|------|-------------|
| Heading | text | The main title displayed prominently on the slide. |
| Button | text | The call-to-action button label. Leave empty to hide the button. |
| Body | rich text editor | Descriptive content displayed below the heading. Supports formatted text, links, and inline media. |
| Image | image upload | An optional image displayed alongside the slide content, typically positioned to the left or right of the text. |
| Link — Button Link URL | url | The destination URL when a visitor clicks the slide button. |
| Link — URL Opens | select | Choose whether the button link opens in the same window or a new tab. |
| Background | background controls | Set the slide's background color, gradient, image, or video. Supports parallax scrolling for images. |

### Design Tab

The Design tab controls the visual presentation of the slider, its slides, and all typographic elements.

| Setting | Type | Description |
|---------|------|-------------|
| Overlay | overlay controls | Apply a color overlay on top of slide backgrounds with adjustable opacity. Also configure text overlay styling. |
| Navigation | color picker | Set the color of the navigation arrows and dot indicators for both default and hover states. |
| Image | image styling | Configure the appearance of slide images including border radius, shadow, and object-fit behavior. |
| Text | text styling | Set general text properties for the module including font family, weight, style, alignment, and line height. |
| Title Text | text styling | Customize the slide heading typography including font, size, color, letter spacing, line height, and text shadow. |
| Body Text | text styling | Style the slide body content text with independent font, size, color, and spacing controls. |
| Button | button styling | Customize the CTA button appearance including font, colors, border, border radius, padding, and hover state effects. |
| Sizing | dimension controls | Set the module's width, height, min/max dimensions, and alignment. |
| Spacing | margin/padding | Adjust the internal padding and external margins of the module. Supports per-device responsive values. |
| Border | border controls | Apply borders to the module container with independent control over each side's width, style, and color. |
| Box Shadow | shadow controls | Add a shadow behind the module with adjustable offset, blur, spread, and color. |
| Filters | filter controls | Apply CSS filter effects including hue rotation, saturation, brightness, contrast, invert, sepia, opacity, and blend mode. |
| Transform | transform controls | Apply CSS transforms including scale, rotate, skew, and translate on the X, Y, and Z axes. |
| Animation | animation controls | Set an entrance animation style with configurable duration, delay, and intensity. |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

| Setting | Type | Description |
|---------|------|-------------|
| CSS ID | text | Assign a unique CSS ID to the module's outermost wrapper for targeted styling or JavaScript hooks. |
| CSS Class | text | Add one or more CSS classes to the module for shared styling rules. |
| Custom Attributes | text | Add custom HTML data attributes to the module element. |
| Custom CSS | code editor | Write CSS rules targeting specific internal elements of the module (e.g., slide content, title, button, image, arrows, dots). |
| HTML Tag | select | Choose the semantic HTML element used for the module wrapper (div, section, article, etc.). |
| Conditions | logic builder | Set display conditions based on user role, device, date, or other dynamic criteria. |
| Interactions | event builder | Configure custom interactions triggered by click, hover, or scroll events. |
| Visibility | device toggles | Control whether the module renders on desktop, tablet, and phone screen sizes. |
| Transitions | transition controls | Set the duration, delay, and easing curve for CSS transitions on hover and state changes. |
| Position | position controls | Switch between static, relative, absolute, or fixed positioning with configurable offsets. |
| Scroll Effects | scroll controls | Apply scroll-driven transformations such as vertical/horizontal motion, fade, scale, rotate, and blur. |

## Code Examples

### Custom CSS

```css
/* Darken slide backgrounds for better text contrast */
.et_pb_fullwidth_slider .et_pb_slide_overlay_container {
    background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.6));
}

/* Style the slide heading */
.et_pb_fullwidth_slider .et_pb_slide_description h2 {
    font-size: 48px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
}

/* Customize the CTA button */
.et_pb_fullwidth_slider .et_pb_button {
    border-radius: 30px;
    padding: 12px 32px;
    font-weight: 600;
    text-transform: uppercase;
}

/* Center slide content vertically */
.et_pb_fullwidth_slider .et_pb_slide_description {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

/* Responsive: reduce heading size on mobile */
@media (max-width: 767px) {
    .et_pb_fullwidth_slider .et_pb_slide_description h2 {
        font-size: 28px;
    }
}
```

### PHP Hooks

```php
/* Filter the Fullwidth Slider module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_fullwidth_slider' !== $render_slug) {
        return $output;
    }
    // Example: Add a scroll-down indicator after the slider
    $output .= '<div class="scroll-indicator"><span>&#8595;</span></div>';
    return $output;
}, 10, 2);

/* Add custom class to the slider based on slide count */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_fullwidth_slider' !== $render_slug) {
        return $output;
    }
    $slide_count = substr_count($output, 'et_pb_slide ');
    if ($slide_count === 1) {
        $output = str_replace('et_pb_fullwidth_slider', 'et_pb_fullwidth_slider single-slide', $output);
    }
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Parallax Hero with Video Fallback** — Set a high-resolution image as the slide background with parallax enabled. For modern browsers, add a video background that autoplays silently. The image serves as a fallback for devices that do not support autoplay. Add a centered heading and CTA button with the overlay darkened to ensure text readability.

2. **Multi-Slide Feature Tour** — Create three to five slides, each spotlighting a different feature or benefit of your product. Use a consistent background style across all slides and position a product image on the right side of each slide with descriptive text on the left. Enable dot navigation so visitors can jump between features.

3. **Minimal Announcement Banner** — Use a single slide with a solid background color or subtle gradient. Set a short heading, a one-line description, and a button linking to the announcement page. Disable navigation arrows and dots since there is only one slide, keeping the layout clean and focused.

## Saving Your Work

After configuring the Fullwidth Slider module, click the green **Save** button at the bottom of the Visual Builder interface. You can also save the entire slider (with all its slides) to your Divi Library for reuse across pages by right-clicking the module and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Fullwidth Slider in Divi 5 uses the updated rendering engine and supports Conditions, Interactions, Scroll Effects, and enhanced Flexbox/Grid layout controls that are not available in Divi 4.

## Troubleshooting

!!! warning "Slides Not Advancing Automatically"
    If you expect slides to auto-rotate but they remain static, check that the auto-advance setting is enabled and that a timing interval is configured. Also verify that the slider contains more than one slide, as single-slide sliders will not animate.

!!! warning "Video Background Not Playing"
    Video backgrounds require an MP4 or WebM URL. If the video does not play, verify the file URL is publicly accessible and that no browser autoplay restrictions are blocking it. Most mobile browsers block autoplay video unless it is muted. Ensure the video is served over HTTPS.

!!! tip "Content Overflowing on Mobile"
    If slide text or buttons are being cut off on smaller screens, reduce the heading font size and body text length for tablet and phone breakpoints using the responsive toggle in the Design tab. You can also increase the module's minimum height to give content more vertical room.

## Related

- [Slider](slider.md)
- [Post Slider](post-slider.md)
- [Video Slider](video-slider.md)
- [Fullwidth Header](fullwidth-header.md)
