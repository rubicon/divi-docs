---
title: "Lottie"
category: modules
tags: ["modules", "lottie", "animation", "svg", "json", "motion", "interactive"]
related: ["icon", "image", "video"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11982058-the-lottie-module-in-divi-5"
---

# Lottie

The Lottie module plays lightweight JSON or SVG animations anywhere in your layout with configurable triggers, looping, speed, and direction.

## Overview

The Lottie module brings vector-based motion graphics into Divi pages by rendering animations from JSON or SVG files. Lottie animations are typically created in Adobe After Effects and exported via the Bodymovin plugin, producing small, scalable files that perform well across devices. Because they are vector-based rather than raster video, Lottie files maintain crisp quality at any resolution while keeping file sizes minimal.

The module offers granular playback control. You can set the animation trigger to play on page load, on hover, or on scroll. Looping can be toggled on or off, and a bounce play mode reverses the animation after completion for a back-and-forth effect. Speed and direction settings let you slow down, speed up, or reverse the animation to match your design intent.

One important consideration is that WordPress blocks SVG and JSON file uploads by default for security reasons. You will need to allow these file types through a plugin, a functions.php snippet, or your hosting configuration before uploading Lottie files to the media library.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11982058-the-lottie-module-in-divi-5).

![Lottie module](../assets/screenshots/modules/lottie/element.png){ loading=lazy }
*The Lottie module displaying an animated illustration.*

## Use Cases

1. **Animated Hero Illustration** — Place a Lottie animation at the top of a landing page that plays on load with looping enabled, creating an eye-catching visual that draws attention without the file size overhead of a video.
2. **Interactive Hover Icons** — Use small Lottie animations as interactive icons that trigger on hover, providing micro-interactions that make feature sections or navigation elements feel responsive and polished.
3. **Scroll-Triggered Storytelling** — Configure the animation trigger to scroll mode so the animation progresses as the user scrolls. This creates a narrative effect where illustrations build as visitors move through the page content.

## How to Add the Lottie Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Lottie" in the module picker or find it in the Content Elements category, then click to insert it.

<!-- TODO: Add animated GIF demonstrating module insertion -->

## Settings & Options

The Lottie module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the animation file, playback behavior, link settings, and module metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Lottie Animation | file upload | Upload a JSON or SVG animation file from the media library. This is the primary animation asset rendered by the module. |
| Animation Trigger | dropdown | Determines when the animation plays: on page load, on hover, or on scroll. Each trigger mode changes how the user interacts with the animation. |
| Loop | toggle | When enabled, the animation repeats continuously after reaching the end. When disabled, it plays once and stops on the final frame. |
| Animation Speed | slider | Adjusts the playback rate. Values above 1 speed up the animation; values below 1 slow it down. |
| Direction | dropdown | Sets whether the animation plays forward (normal) or in reverse from the last frame to the first. |
| Play Mode | dropdown | Choose **Normal** for standard one-direction playback, or **Bounce** to reverse the animation automatically after completion, creating a ping-pong effect. |
| Link | url/link settings | Makes the entire Lottie module clickable, directing users to a page or external URL. |
| Background | background controls | Apply a background color, gradient, image, or video behind the Lottie animation container. |
| Loop Builder | toggle | Enables the loop builder for repeating the module dynamically within query-driven layouts. |
| Order | number | Controls the display order when the parent container uses Flexbox or Grid layout. |
| Meta | admin label | Set an admin label and control Visual Builder visibility. |

<!-- ![Lottie Content tab settings](../assets/screenshots/modules/lottie/settings-content.png){ loading=lazy } -->
<!-- TODO: Capture Content tab screenshot -->

### Design Tab

The Design tab controls the module's dimensions, spacing, borders, and visual effects.

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | General text styling (applies if text elements are present) |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (hue, saturation, brightness, blend mode) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles (separate from Lottie playback) |

<!-- ![Lottie Design tab settings](../assets/screenshots/modules/lottie/settings-design.png){ loading=lazy } -->
<!-- TODO: Capture Design tab screenshot -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, interactions, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

<!-- ![Lottie Advanced tab settings](../assets/screenshots/modules/lottie/settings-advanced.png){ loading=lazy } -->
<!-- TODO: Capture Advanced tab screenshot -->

## Code Examples

### Custom CSS

```css
/* Constrain the Lottie animation to a specific size */
.et_pb_lottie {
    max-width: 400px;
    margin: 0 auto;
}

/* Add a circular mask to the Lottie animation */
.et_pb_lottie.circular-lottie svg {
    border-radius: 50%;
    overflow: hidden;
}

/* Reduce animation opacity until hovered */
.et_pb_lottie.hover-reveal {
    opacity: 0.6;
    transition: opacity 0.3s ease;
}

.et_pb_lottie.hover-reveal:hover {
    opacity: 1;
}

/* Responsive sizing */
@media (max-width: 980px) {
    .et_pb_lottie {
        max-width: 300px;
    }
}

@media (max-width: 767px) {
    .et_pb_lottie {
        max-width: 200px;
    }
}
```

### PHP Hooks

```php
/* Add a loading="lazy" attribute to the Lottie module container */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_lottie' !== $render_slug) {
        return $output;
    }
    $output = str_replace(
        'class="et_pb_lottie',
        'loading="lazy" class="et_pb_lottie',
        $output
    );
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Animated Loading Indicator** — Use a small Lottie spinner animation with loop enabled and normal play mode. Place it inside a Group module alongside a "Loading..." text element. Apply conditional visibility to show this block only while content loads, or use it as a decorative element above forms.

2. **Feature Section Illustrations** — Pair Lottie animations with text content in two-column rows. Place the animation in one column and a heading plus description in the other. Set the trigger to scroll so the illustration builds as the user reaches that section, creating an engaging reveal effect.

3. **Animated Logo or Brand Mark** — Upload a Lottie version of a logo that plays once on page load with normal direction. Set the animation speed slightly below 1.0 for a smooth, deliberate reveal. Position it in the header area or hero section for memorable first impressions.

## Saving Your Work

After configuring the Lottie module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Animation File Upload Fails"
    If WordPress rejects the JSON or SVG file upload:

    - WordPress blocks SVG and JSON uploads by default for security. Install a plugin like "Safe SVG" or add a custom upload filter in your child theme's `functions.php` to allow these file types.
    - Verify that the file is a valid Lottie JSON file (not a generic JSON config file). Valid Lottie files contain animation data with properties like `v`, `fr`, `ip`, `op`, and `layers`.
    - Check your hosting provider's upload size limits if the file is large.

!!! warning "Animation Not Playing"
    If the Lottie file uploads but does not animate:

    - Check the **Animation Trigger** setting. If set to hover, the animation only plays when the cursor is over the module. If set to scroll, it progresses as the user scrolls.
    - Verify that no JavaScript errors on the page are blocking the Lottie player library from initializing.
    - Test the Lottie file on [lottiefiles.com](https://lottiefiles.com) to confirm it is valid and plays correctly outside of Divi.

!!! tip "Optimizing Lottie File Size"
    Large Lottie files with many layers or effects can impact performance. Use the LottieFiles optimizer tool to reduce file size. Remove unused layers in After Effects before exporting, and prefer shape layers over image assets. Aim to keep Lottie JSON files under 100KB for optimal load times.

## Related

- [Icon](icon.md) — Static icon display module from the Divi icon library
- [Image](image.md) — Standard image display module for static visuals
- [Video](video.md) — Video playback module for embedded or self-hosted video content
