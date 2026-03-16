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

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose text and logo alignment (left, center, right) and whether the module should display in full-screen mode, expanding to fill the entire viewport height. |
| Scroll Down Icon | toggle + options | Enable a scroll-down indicator icon below the header content. When enabled, configure the icon style, color, and size to guide visitors to scroll. |
| Subtitle Text | text styling | Style the subtitle line with its own font, size, color, and spacing settings. |
| Button One | button styling | Customize the first button's appearance: text color, background color, border, border radius, font, icon, and hover state styles. |
| Button Two | button styling | Customize the second button independently with the same options as Button One, allowing for contrasting primary/secondary button designs. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Title Text](../options-groups/title-text.md) | Font, size, color, letter spacing, line height, text shadow for the main title |
| [Body Text](../options-groups/body-text.md) | Font, size, color, line height for body content |
| [Image](../options-groups/image.md) | Border radius, shadows, and filters for the header image |
| [Overlay](../options-groups/overlay.md) | Color overlay on background for text readability |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding per side, responsive breakpoints |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Color, offsets, blur radius, spread |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue, blur, invert, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, and interaction behavior.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (title, subtitle, buttons, images, container) |
| HTML | Semantic HTML tag for the module wrapper (div, header, section, article) |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

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

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/fullwidth-header` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Title | `attrs.title` | Main hero heading text |
| Subhead | `attrs.subhead` | Subtitle text below the title |
| Body | `attrs.content` | Body text content |
| Button One Text | `attrs.button_one_text` | Primary CTA button label |
| Button Two Text | `attrs.button_two_text` | Secondary CTA button label |

!!! tip "Module Selection Guidance"
    For full-width hero banners use Fullwidth Header; for content-width heroes consider Hero module; for rotating banners use Fullwidth Slider.

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
