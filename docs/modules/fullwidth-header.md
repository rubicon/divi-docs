---
title: "Fullwidth Header"
category: modules
tags: ["modules", "fullwidth", "header", "hero", "landing-page", "call-to-action", "buttons"]
related: ["slider", "call-to-action", "image"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://www.elegantthemes.com/documentation/divi/fullwidth-header-new/"
---

# Fullwidth Header

The Fullwidth Header module creates a prominent, full-width hero section with customizable text, images, icons, and dual call-to-action buttons.

## Overview

The Fullwidth Header module is one of the most versatile layout elements in Divi 5. It occupies the entire width of its parent fullwidth section and is designed to make a strong visual impression at the top of a page or within any fullwidth area. The module supports a rich combination of content elements including a title, subtitle, body text, two images, a decorative icon, and two inline buttons arranged side by side.

Because of its flexible content slots and full-width presentation, this module is commonly used as a hero banner on landing pages, a promotional header for product launches, or a dynamic post title area in page templates. You can pair it with background images, gradients, or videos to create immersive visual experiences without any custom code.

The Fullwidth Header module must be placed inside a fullwidth section. It cannot be inserted into a standard section or specialty section. When building templates for posts, projects, or custom post types, you can use dynamic content fields within the title and subtitle to pull data automatically from the current post.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10369762-the-hero-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/fullwidth-header/)

![Fullwidth Header module](../assets/screenshots/modules/fullwidth-header/element.png){ loading=lazy }
*The Fullwidth Header module displaying a hero section with title, subtitle, buttons, and background image.*

## Use Cases

1. **Landing Page Hero** — Place the Fullwidth Header at the top of a marketing page with a bold headline, supporting body text, a background image or video, and two call-to-action buttons that link to a signup form and a product demo.

2. **Dynamic Post Title Section** — Use the module in a Divi 5 template with dynamic content fields for the title and subtitle, creating a consistent branded header that automatically displays the current post or project title, author, and featured image.

3. **Promotional Banner** — Feature a limited-time offer or free resource download by combining eye-catching header text with a logo image on one side, a product mockup on the other, and a prominent download button.

## How to Add the Fullwidth Header Module

1. Open the Visual Builder on the page you want to edit and ensure you have a fullwidth section on the page. If not, click the blue **+** icon and choose **Fullwidth** as the section type.

2. Click the gray **+** icon inside the fullwidth section to open the module picker.

3. Search for "Fullwidth Header" or browse the Fullwidth Modules category, then click to insert it into the section.

## Settings & Options

The Fullwidth Header module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the text, images, links, and background elements displayed by the module.

| Setting | Type | Description |
|---------|------|-------------|
| Text | text fields | Configure the module's primary content: Title, Subtitle, Button One text, Button Two text, and Body text. Each field accepts static text or dynamic content. |
| Images | image upload | Select a Logo Image and a Header Image. The logo appears above or beside the title area, while the header image displays in the designated image slot based on the chosen layout. |
| Link | url | Make the entire module clickable, directing users to another page, section, or external URL. Includes options for link URL, target, and rel attributes. |
| Background | background controls | Set a background color, gradient, image, or video behind the module. Supports multiple layers and parallax effects for images. |
| Loop | toggle | Enable the Loop Builder to display dynamic content from posts, custom post types, or other data sources. |
| Order | select | Control the display order of the module when placed inside a Flexbox or CSS Grid layout container. |
| Meta | admin label | Assign a custom label to identify the module in the Visual Builder's layer panel. Also includes a toggle to force visibility in the builder. |

### Design Tab

The Design tab controls layout, typography, button styling, and all visual presentation options.

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose text and logo alignment (left, center, right) and whether the module should display in full-screen mode, expanding to fill the entire viewport height. |
| Scroll Down Icon | toggle + options | Enable a scroll-down indicator icon below the header content. When enabled, configure the icon style, color, and size to guide visitors to scroll. |
| Image | image styling | Adjust styling for the header image including border radius, shadows, and filters. |
| Overlay | overlay controls | Apply a color overlay on top of the background to improve text readability. Configure overlay color and opacity. |
| Text | text styling | Set general text properties like font family, weight, style, alignment, and line height that apply to all text elements in the module. |
| Title Text | text styling | Style the main title independently with font family, size, color, letter spacing, line height, and text shadow. Supports responsive values per breakpoint. |
| Body Text | text styling | Configure body text appearance including font, size, color, and line height, separate from title and subtitle styling. |
| Subtitle Text | text styling | Style the subtitle line with its own font, size, color, and spacing settings. |
| Button One | button styling | Customize the first button's appearance: text color, background color, border, border radius, font, icon, and hover state styles. |
| Button Two | button styling | Customize the second button independently with the same options as Button One, allowing for contrasting primary/secondary button designs. |
| Sizing | dimensions | Control the module's width, max-width, height, and min-height. Full-screen mode overrides height settings. |
| Spacing | margin/padding | Set margin and padding values for the module container. Supports responsive values per device breakpoint. |
| Border | border controls | Add borders around the module with customizable width, color, style, and border radius for rounded corners. |
| Box Shadow | shadow controls | Apply a box shadow with configurable color, horizontal/vertical offset, blur radius, and spread. |
| Filters | CSS filters | Apply visual filter effects such as brightness, contrast, saturation, hue rotation, blur, and invert. Includes blend mode selection. |
| Transform | transform controls | Apply CSS transforms including scale, translate, rotate, skew, and transform origin for advanced positioning effects. |
| Animation | animation select | Choose an entrance animation (fade, slide, bounce, zoom, flip, fold, roll) with configurable duration, delay, intensity, and starting opacity. |

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, and interaction behavior.

| Setting | Type | Description |
|---------|------|-------------|
| Attributes | text fields | Assign a CSS ID and CSS classes to the module for targeting with custom styles or JavaScript. Also supports custom HTML data attributes. |
| CSS | code editor | Write custom CSS that applies directly to specific internal elements of the module (title, subtitle, buttons, images, container, etc.). |
| HTML | tag select | Choose the semantic HTML tag used for the module's wrapper element (div, header, section, article, etc.). |
| Conditions | condition builder | Set display conditions so the module only renders when specific rules are met, such as user role, page type, date range, or custom logic. |
| Interactions | interaction builder | Define hover, click, or scroll-triggered interactions that affect this module or other elements on the page. |
| Visibility | device toggles | Show or hide the module on desktop, tablet, and/or phone. Hidden modules are not rendered in the page source for that breakpoint. |
| Transitions | transition controls | Configure CSS transition duration and easing function for smooth hover state changes on the module and its child elements. |
| Position | position controls | Set the CSS position property (relative, absolute, fixed, sticky) and offset values (top, right, bottom, left, z-index). |
| Scroll Effects | scroll controls | Apply scroll-driven effects like parallax, fade, scale, rotate, blur, or horizontal movement as the user scrolls past the module. |

## Code Examples

### Custom CSS

```css
/* Center the Fullwidth Header content and add breathing room */
.et_pb_fullwidth_header {
    text-align: center;
    padding: 80px 40px;
}

/* Style the title for stronger visual impact */
.et_pb_fullwidth_header .et_pb_fullwidth_header_title {
    font-size: 48px;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin-bottom: 16px;
}

/* Style the subtitle */
.et_pb_fullwidth_header .et_pb_fullwidth_header_subtitle {
    font-size: 20px;
    opacity: 0.85;
    margin-bottom: 24px;
}

/* Create contrasting primary and secondary buttons */
.et_pb_fullwidth_header .et_pb_button_one {
    background-color: #ffffff;
    color: #333333;
    border: 2px solid #ffffff;
}

.et_pb_fullwidth_header .et_pb_button_two {
    background-color: transparent;
    color: #ffffff;
    border: 2px solid #ffffff;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_fullwidth_header {
        padding: 50px 20px;
    }
    .et_pb_fullwidth_header .et_pb_fullwidth_header_title {
        font-size: 32px;
    }
}
```

### PHP Hooks

```php
/* Filter the Fullwidth Header module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_fullwidth_header' !== $render_slug) {
        return $output;
    }
    // Example: Add a wrapper div for additional styling control
    $output = '<div class="custom-header-wrap">' . $output . '</div>';
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Split Layout with Image** — Set the layout alignment to left or right so the text content occupies one side while the header image fills the other. Apply a subtle background gradient and use Button One as the primary CTA with a filled style, and Button Two as a secondary link with a transparent/outlined style.

2. **Full-Screen Video Background** — Enable full-screen mode in the Layout settings and add a background video in the Content tab. Apply a dark color overlay in the Design tab to ensure white text remains readable on top of the video. Add a scroll-down icon to prompt visitors to continue.

3. **Branded Template Header** — In a Divi 5 theme builder template, insert the Fullwidth Header with the title and subtitle set to dynamic content (post title and excerpt). Upload the site logo as the Logo Image and set a consistent brand-color background gradient, creating a unified header across all posts or pages that use the template.

## Saving Your Work

After configuring the Fullwidth Header:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Appearing in Module Picker"
    The Fullwidth Header module only appears when adding modules to a fullwidth section. If you are working inside a standard section or specialty section, it will not be listed. Add a fullwidth section first, then insert the module.

!!! warning "Buttons Not Displaying"
    If one or both buttons are missing from the front end, make sure you have entered text in the corresponding Button One Text or Button Two Text fields in the Content tab. Buttons without text are hidden automatically.

!!! tip "Background Image Not Covering Full Width"
    If the background image appears cropped or does not span the full module width, check that the image resolution is at least 1920px wide. Also verify that the background size is set to "Cover" and the position is set to "Center" in the Background settings.

## Related

- [Slider](slider.md) — Full-width rotating slides with similar visual impact
- [Call To Action](call-to-action.md) — Focused conversion element with heading, text, and button
- [Image](image.md) — Standalone image display for simpler visual sections
