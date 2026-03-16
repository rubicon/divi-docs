---
title: "Slider"
description: "Complete Divi 5 Slider module reference — custom slides with images, text, buttons, overlay controls, navigation, and animations."
category: modules
tags: ["modules", "slider", "carousel", "hero", "slideshow", "rotating-content", "banner"]
related: ["post-slider", "video-slider", "fullwidth-slider"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10364612-the-slider-module-in-divi-5"
---

# Slider

The Slider module displays rotating slides with images, text, and buttons in an animated carousel format.

!!! abstract "Quick Reference"
    **What it does:** Creates a rotating slideshow with custom slides, each containing a heading, body text, button, and background image or video.
    **When to use it:** Hero banners, testimonial carousels, product/service showcases
    **Key settings:** Slides (repeater), Heading, Button Text/URL, Background Image, Overlay, Navigation
    **Block identifier:** `divi/slider`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10364612-the-slider-module-in-divi-5)

!!! tip "When to Use This Module"
    - Building hero banners with multiple rotating messages and CTAs
    - Creating testimonial or quote carousels with custom content per slide
    - Showcasing products or services with individual slide backgrounds and descriptions

!!! warning "When NOT to Use This Module"
    - Generating slides automatically from blog posts → use [Post Slider](post-slider.md)
    - Creating a video-based carousel → use [Video Slider](video-slider.md)
    - Needing a full-browser-width slider → use [Fullwidth Slider](fullwidth-slider.md)

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

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Overlay | color/opacity | Configure the semi-transparent overlay placed on top of slide background images. Adjusting overlay color and opacity improves text readability against varied or busy images. |
| Navigation | styling group | Customize the appearance of the slider's directional arrows and dot pagination controls, including color, size, and positioning. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Title Text](../options-groups/title-text.md) | Font, weight, size, color, letter spacing, line height, text shadow for slide headings |
| [Body Text](../options-groups/body-text.md) | Font, size, color, spacing for slide description text |
| [Button](../options-groups/button.md) | Text size, colors, background, border, border radius, font, icon, hover behavior |
| [Image](../options-groups/image.md) | Alignment adjustments and display behavior for slide background images |
| [Sizing](../options-groups/sizing.md) | Width, max-width, min-height, height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding with responsive breakpoint controls |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Horizontal/vertical offset, blur, spread, color, position |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue rotation, blur, invert, sepia, opacity, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, direction, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level controls for custom attributes, CSS targeting, conditional display logic, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (slide container, title, description, button, image, arrows, pagination) |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

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

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/slider` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Child slides | Nested blocks | Each slide has heading, body, button, and image attributes |

!!! tip "Module Selection Guidance"
    For static content slideshows use Slider; for post-based slideshows use Post Slider; for edge-to-edge sliders use Fullwidth Slider; for video collections use Video Slider.

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
- [Hero Module](hero.md) — Static hero section with similar heading, text, and button layout
- [Background Options](../options-groups/background.md) — Configure slide background images, gradients, and videos
- [Animation Options](../options-groups/animation.md) — Control slide entrance and transition animations
