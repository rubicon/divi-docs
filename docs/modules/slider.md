---
title: "Slider"
category: modules
tags: ["modules", "slider", "carousel", "hero", "slideshow", "rotating-content", "banner"]
related: ["post-slider", "video-slider", "fullwidth-slider"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10364612-the-slider-module-in-divi-5"
---

# Slider

The Slider module displays rotating slides with images, text, and buttons in an animated carousel format.

## Overview

The Slider module is one of the most prominent content elements in Divi 5, designed to present multiple pieces of content in a single, space-efficient container that cycles through slides. Each slide can include its own heading, body text, call-to-action button, and background image or video, making it suitable for hero banners, promotional rotators, testimonial carousels, and feature showcases.

The module manages all transition animations internally and provides built-in navigation controls, including directional arrows and dot-style pagination indicators. Visitors can browse slides manually or let them advance automatically on a configurable timer. Every slide operates as an independent content unit with its own background and text configuration, while the parent module controls shared behavior like animation speed, overlay styling, and navigation appearance.

Responsive behavior is handled automatically. The slider adapts to its container width and provides per-breakpoint controls for typography, spacing, and visibility. Whether placed in a narrow sidebar column or spanning a fullwidth section, the module adjusts its layout to maintain readability and visual balance across devices.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10364612-the-slider-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/slider/)

![Slider module](../assets/screenshots/modules/slider/element.png){ loading=lazy }
*The Slider module as it appears on the live demo.*

## Use Cases

1. **Hero Banner** — Place a full-width slider at the top of a landing page to cycle through key messages, promotions, or brand imagery with call-to-action buttons that drive visitors deeper into the site.
2. **Testimonial Carousel** — Rotate through customer quotes by using each slide for a different testimonial, with the client name as the heading and the quote as the body text, omitting the button for a clean look.
3. **Product or Service Showcase** — Dedicate each slide to a different product or service offering, combining a relevant background image with a brief description and a link to the full details page.

## How to Add the Slider Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Slider" in the module picker or find it in the Content Elements category, then click to insert it.

## Settings & Options

The Slider module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab manages the individual slides and the module-level content configuration including elements, links, backgrounds, and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Slides (Repeater) | item list | Manage individual slides. Click **+** to add a new slide, the pencil icon to edit, the trash icon to delete, and drag to reorder. Each slide has its own settings detailed below. |
| Elements | toggle group | Control the visibility of navigation elements such as arrows and dot pagination controls. |
| Link | url | Optionally wrap the entire slider module in a link to a specified URL. |
| Background | background controls | Set a module-level background color, gradient, image, or video that appears behind all slides. Individual slide backgrounds take precedence over this setting. |
| Loop | toggle | When enabled, the slider continuously cycles through slides, returning to the first slide after the last one completes. |
| Order | select | Control the display order of slides within the module. |
| Meta | admin label | Set an internal label for the module visible only in the Visual Builder layer panel, useful when a page contains multiple slider instances. |

#### Individual Slide Settings

Each slide within the slider has its own configuration panel:

| Setting | Type | Description |
|---------|------|-------------|
| Heading | text | The primary title displayed on the slide. Supports dynamic content tokens. |
| Button Text | text | Label for the slide's call-to-action button. Leave empty to hide the button entirely. |
| Button URL | url | Destination link for the slide button. Both text and URL must be set for the button to render. |
| Body | rich text | Descriptive content displayed below the heading. Supports HTML formatting, lists, and inline styling through the text editor. |
| Background Image | image upload | Image displayed behind the slide content. For full-width sliders, a minimum width of 1920px is recommended to avoid pixelation. |
| Background Color | color picker | Solid color behind the slide. Visible when no background image is assigned or as a loading fallback. |
| Background Video MP4 | url | Path to an MP4 video file used as the slide background when video backgrounds are enabled. |
| Background Video WebM | url | Path to a WebM video file used as an alternative format for browsers that do not support MP4. |

### Design Tab

The Design tab controls the visual presentation of the slider, including overlay appearance, navigation styling, typography, button design, and layout properties.

| Setting | Type | Description |
|---------|------|-------------|
| Overlay | color/opacity | Configure the semi-transparent overlay placed on top of slide background images. Adjusting overlay color and opacity improves text readability against varied or busy images. |
| Navigation | styling group | Customize the appearance of the slider's directional arrows and dot pagination controls, including color, size, and positioning. |
| Image | image styling | Apply treatments to slide background images such as alignment adjustments and display behavior. |
| Text | text styling | Set general text properties including font family, weight, style, color, and alignment that apply broadly across the module's text elements. |
| Title Text | text styling | Style the slide heading specifically with independent font family, size, color, weight, letter spacing, line height, and text shadow settings. Responsive controls available per breakpoint. |
| Body Text | text styling | Style the slide description text with its own font, size, color, weight, letter spacing, line height, and shadow settings independent of the title. |
| Button | button styling | Customize the slide button appearance including text size, text color, background color, border width, border color, border radius, font family, icon selection, icon placement, and hover behavior. Enable custom styles to expose the full set of button controls. |
| Sizing | dimension controls | Set the module width, max width, min height, and horizontal alignment. Min height prevents the slider from collapsing when content is short. |
| Spacing | margin/padding | Configure external margin and internal padding for the slider. The default vertical padding controls perceived slide height. Responsive values can be set independently for each breakpoint. |
| Border | border styling | Add and customize borders around the slider module including width, color, style, and per-corner radius values. |
| Box Shadow | shadow controls | Apply a box shadow effect to the slider module with configurable horizontal offset, vertical offset, blur, spread, and color. |
| Filters | image filters | Apply CSS filter effects to the module including hue rotation, saturation, brightness, contrast, inversion, sepia, and blur. |
| Transform | transform controls | Apply CSS transforms to the module including scale, translate, rotate, skew, and transform origin adjustments. |
| Animation | animation controls | Configure both the slide transition effect (slide or fade between slides) and the module entrance animation triggered when scrolling into view, with style, direction, duration, delay, and intensity settings. |

### Advanced Tab

The Advanced tab provides low-level controls for custom attributes, CSS targeting, conditional display logic, and scroll-driven effects.

| Setting | Type | Description |
|---------|------|-------------|
| Attributes | id/class inputs | Assign a unique CSS ID and one or more CSS classes to the module for targeting with custom CSS or JavaScript. |
| CSS | custom CSS editor | Add custom CSS rules targeting specific internal elements of the slider such as the slide container, title, description, button, image, arrows, and pagination controls. |
| HTML | html attributes | Configure additional HTML attributes on the module wrapper element. |
| Conditions | display logic | Set conditions that determine when the module is displayed, such as user role, page type, or custom logic rules. |
| Interactions | event handlers | Define interactive behaviors triggered by user actions like click or hover events on the module. |
| Visibility | device toggles | Control which devices display this module by toggling visibility independently for desktop, tablet, and phone. |
| Transitions | transition controls | Set the duration and timing of hover transition effects on interactive elements within the module. |
| Position | positioning controls | Configure the CSS positioning scheme (static, relative, absolute, fixed, or sticky), along with z-index and offset values. |
| Scroll Effects | scroll transforms | Enable transform effects like rotation, scaling, fading, and blur that are driven by the visitor's scroll position relative to the module. |

## Code Examples

### Custom CSS: Styled Navigation Arrows

```css
/* Circular background arrows with hover effect */
.et_pb_slider .et-pb-arrow-prev,
.et_pb_slider .et-pb-arrow-next {
    font-size: 22px;
    color: #ffffff;
    background: rgba(0, 0, 0, 0.4);
    padding: 14px 18px;
    border-radius: 50%;
    transition: background 0.3s ease;
}

.et_pb_slider .et-pb-arrow-prev:hover,
.et_pb_slider .et-pb-arrow-next:hover {
    background: rgba(0, 0, 0, 0.75);
}

.et_pb_slider .et-pb-arrow-prev {
    left: 24px;
}

.et_pb_slider .et-pb-arrow-next {
    right: 24px;
}
```

### Custom CSS: Full-Viewport Hero Slider

```css
/* Force the slider to fill the entire viewport height */
.et_pb_slider.hero-slider {
    min-height: 100vh;
}

.et_pb_slider.hero-slider .et_pb_slide {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Gradient overlay for improved text contrast */
.et_pb_slider.hero-slider .et_pb_slide::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0.2) 0%,
        rgba(0, 0, 0, 0.6) 100%
    );
    z-index: 1;
}

.et_pb_slider.hero-slider .et_pb_slide_description {
    position: relative;
    z-index: 2;
}
```

### Custom CSS: Content-Driven Slide Height

```css
/* Let content determine slide height instead of fixed padding */
.et_pb_slider.auto-height .et_pb_slide {
    min-height: auto !important;
    padding: 60px 40px;
}

.et_pb_slider.auto-height .et_pb_slide_description {
    padding-bottom: 0;
}

@media (max-width: 980px) {
    .et_pb_slider.auto-height .et_pb_slide {
        padding: 40px 20px;
    }
}
```

### PHP: Wrap Slider Output

```php
/* Add a custom wrapper element around every slider module */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_slider' !== $render_slug) {
        return $output;
    }
    return '<div class="custom-slider-wrapper">' . $output . '</div>';
}, 10, 2);
```

## Common Patterns

### 1. Hero Banner with Gradient Overlay

Place the slider inside a fullwidth section at the top of the page. Assign high-resolution background images to each slide and enable the overlay color with a dark semi-transparent value to ensure white text remains legible. Set automatic animation to on with a 6000ms interval. Add a strong call-to-action button on each slide pointing to key conversion pages.

### 2. Minimal Testimonial Rotator

Create slides without background images, using a solid background color instead. Set each slide heading to the customer name and the body text to their quote. Leave the button fields empty to hide buttons entirely. Reduce vertical padding for a compact appearance and center-align the text. This produces a clean, typography-focused testimonial section.

### 3. Feature Highlight Carousel

Dedicate each slide to a specific feature or service. Use a relevant background image with the overlay set to a branded color at roughly 70% opacity. Keep descriptions concise at two to three sentences and include a "Learn More" button linking to the corresponding detail page. This pattern works well at two-thirds or full column width.

## Saving Your Work

After configuring your slider, save your changes by clicking the **Save** button (checkmark icon) in the Visual Builder's bottom toolbar. For reusable slider configurations, right-click the module and select **Save to Library** to store it as a preset that can be inserted on other pages.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Slider settings and class names may differ from Divi 4.

## Troubleshooting

!!! warning "Slides Not Advancing Automatically"
    If the slider stays on the first slide and does not rotate:

    - Confirm that **Loop** or automatic animation is enabled in the Content tab settings.
    - Check the animation speed value. Extremely low values can cause visual glitches, while very high values may make it seem like nothing is happening.
    - JavaScript errors from other plugins can interfere with slider scripts. Open the browser console (F12) and look for errors. Temporarily deactivate other plugins to isolate the issue.
    - A slider with only one slide has nothing to advance to. Add at least two slides.

!!! warning "Background Images Not Displaying"
    If slide backgrounds appear blank or broken:

    - Verify the image URL is correct by opening it directly in a browser tab.
    - Confirm the image has not been deleted from the WordPress Media Library.
    - If a CDN or image optimization plugin is active, ensure it is not rewriting or blocking the image path.
    - Very large images (over 5MB) may time out on slower connections. Compress images to under 500KB for reliable loading.

!!! warning "Slider Height Inconsistent or Jumping"
    If the slider changes height as it transitions between slides:

    - The default vertical padding controls perceived height. Set a fixed **Min Height** value in the Design tab's Sizing group and remove vertical padding to achieve a consistent height.
    - Slides with varying content lengths will cause height shifts unless a fixed minimum height is set.
    - On mobile devices, reduce padding using the responsive controls to prevent the slider from becoming excessively tall.

## Related

- [Post Slider](post-slider.md) — Automatically generates slides from blog posts
- [Video Slider](video-slider.md) — Slider variant with embedded video playback per slide
- [Fullwidth Slider](fullwidth-slider.md) — Full-browser-width slider for use in fullwidth sections
