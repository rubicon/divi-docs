---
title: "Hero"
description: "Complete Divi 5 Hero module reference — full-screen landing sections with title, subtitle, dual buttons, images, and overlay settings."
category: modules
tags: ["modules", "hero", "header", "banner", "landing-page", "cta", "fullwidth"]
related: ["fullwidth-header", "slider", "call-to-action"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10369762-the-hero-module-in-divi-5"
---

# Hero

The Hero module displays a prominent content block with a title, subtitle, body text, dual buttons, images, and an icon for impactful landing sections.

!!! abstract "Quick Reference"
    **What it does:** Creates a high-visibility landing section with title, subtitle, body text, logo, background image, icon, and two CTA buttons.
    **When to use it:** Homepage hero sections, promotional banners, section introductions, landing pages
    **Key settings:** Title, Subtitle, Body text, Button One/Two, Images (logo and header), Full-screen toggle, Overlay, Scroll Down Icon
    **Block identifier:** `divi/hero`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10369762-the-hero-module-in-divi-5)

!!! tip "When to Use This Module"
    - You need a self-contained hero section with title, subtitle, body text, and dual CTA buttons
    - Full-screen landing areas with background images and overlays
    - Section introductions that need a prominent visual treatment with multiple content elements

!!! warning "When NOT to Use This Module"
    - You need an edge-to-edge fullwidth hero → use [Fullwidth Header](fullwidth-header.md)
    - You need rotating hero slides → use [Slider](slider.md)
    - You need only a heading and button (no subtitle or body) → use [Call to Action](call-to-action.md)

## Overview

The Hero module is built for high-visibility page sections that need to make an immediate impression. It bundles several content elements into one cohesive unit: a main title, subtitle, body text, a logo image, a header background image, an icon, and two side-by-side call-to-action buttons. This makes it a self-contained landing section that does not require assembling multiple modules manually.

The module supports full-screen display mode, which stretches the hero to fill the entire viewport height. A scroll-down indicator icon can be enabled to signal that more content exists below the fold. Layout controls allow you to adjust text and logo alignment, and an overlay option adds a semi-transparent color layer over the background image to improve text readability.

In template contexts, the Hero module can pull dynamic post titles, making it useful for single post or project templates where the hero headline should match the current content. It works equally well as a static promotional banner on landing pages, homepages, and section introductions.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10369762-the-hero-module-in-divi-5).

![Hero module](../assets/screenshots/modules/hero/element.png){ loading=lazy }
*The Hero module with title, subtitle, buttons, and background image.*

## Use Cases

1. **Homepage Landing Section** — Create a full-screen hero area with a headline, subheadline, background image with overlay, and dual CTA buttons for primary and secondary actions like "Get Started" and "Learn More."
2. **Promotional Banner** — Highlight special offers, product launches, or time-sensitive deals with prominent title text, a brief description, and a visually striking background that draws attention above the fold.
3. **Section Introduction** — Mark the beginning of key content areas (About, Services, Portfolio) with a hero block that includes a section title, supporting subtitle, and an icon that reinforces the section's theme.

## How to Add the Hero Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Hero" in the module picker or find it in the Content Elements category, then click to insert it.

<!-- TODO: Add animated GIF demonstrating module insertion -->

## Settings & Options

The Hero module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the hero's text elements, images, link behavior, background, and module metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Text | text fields | Configure the title, subtitle, body text, and button labels. Each text element supports dynamic content for use in templates. |
| Images | image upload | Select a logo image and a header background image. The logo displays within the content area; the header image serves as the background visual. |
| Link | url/link settings | Makes the entire Hero module clickable, directing users to a page or external URL. Includes target and relationship options. |
| Background | background controls | Apply a background color, gradient, image, or video behind the entire module. This is separate from the header image and can be layered with it. |
| Loop | toggle | Enables the loop builder for repeating the Hero dynamically within query-driven layouts. |
| Order | number | Controls the display order when the parent container uses Flexbox or Grid layout. |
| Meta | admin label | Set an admin label and control Visual Builder visibility. |

<!-- ![Hero Content tab settings](../assets/screenshots/modules/hero/settings-content.png){ loading=lazy } -->
<!-- TODO: Capture Content tab screenshot -->

### Design Tab

The Design tab controls layout, visual appearance of individual text elements, buttons, images, overlay, and effects.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | alignment/toggle | Adjust text and logo alignment within the hero. Enable full-screen display to stretch the module to viewport height. |
| Scroll Down Icon | toggle/styling | Show or hide a scroll-down indicator icon. Configure icon type, color, and size. |
| Image | image styling | Control the appearance of the logo and header images, including sizing and effects. |
| Overlay | color/opacity | Apply a semi-transparent color layer over the background image to improve text contrast and readability. |
| Title Text | typography controls | Font family, weight, style, size, color, letter spacing, line height, and text shadow for the main title. |
| Body Text | typography controls | Typography settings for the descriptive body content below the title and subtitle. |
| Subtitle Text | typography controls | Font family, weight, size, color, and spacing for the subtitle element. |
| Button One | button styling | Appearance controls for the first CTA button: text size, colors, border, radius, font, icon, and hover states. |
| Button Two | button styling | Appearance controls for the second CTA button, configured independently from Button One. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | General text styling — font, alignment, color |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (hue, saturation, brightness, blend mode) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Hero Design tab settings](../assets/screenshots/modules/hero/settings-design.png){ loading=lazy } -->
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

<!-- ![Hero Advanced tab settings](../assets/screenshots/modules/hero/settings-advanced.png){ loading=lazy } -->
<!-- TODO: Capture Advanced tab screenshot -->

## Code Examples

### Custom CSS

```css
/* Darken the hero overlay for better text contrast */
.et_pb_hero_module .et_pb_hero_overlay {
    background: rgba(0, 0, 0, 0.55);
}

/* Center hero content vertically and horizontally */
.et_pb_hero_module .et_pb_hero_content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    min-height: 80vh;
    padding: 60px 30px;
}

/* Style the dual buttons with contrasting themes */
.et_pb_hero_module .et_pb_button_one {
    background: #ffffff;
    color: #333333;
    border: 2px solid #ffffff;
}

.et_pb_hero_module .et_pb_button_two {
    background: transparent;
    color: #ffffff;
    border: 2px solid #ffffff;
}

.et_pb_hero_module .et_pb_button_two:hover {
    background: #ffffff;
    color: #333333;
}

/* Responsive font scaling */
@media (max-width: 767px) {
    .et_pb_hero_module .et_pb_hero_title {
        font-size: 28px !important;
    }
    .et_pb_hero_module .et_pb_hero_subtitle {
        font-size: 16px !important;
    }
}
```

### PHP Hooks

```php
/* Add a video background fallback for the Hero module */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_hero' !== $render_slug) {
        return $output;
    }
    // Add a poster image attribute for video backgrounds
    $output = str_replace(
        'class="et_pb_hero_module',
        'data-hero="true" class="et_pb_hero_module',
        $output
    );
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Full-Screen Landing Hero** — Enable full-screen display in the Layout settings, add a high-resolution background image with a dark overlay at 50-60% opacity, and center-align white title text with a contrasting subtitle. Use Button One for the primary action ("Get Started") with a solid background and Button Two for the secondary action ("Watch Demo") with a transparent/outline style.

2. **Video Background Hero** — Set a video as the module background in the Content tab, apply a semi-transparent overlay to maintain text readability, and disable the scroll-down icon. Keep the title and subtitle concise since video backgrounds compete for visual attention. This pattern works well for agency and portfolio homepages.

3. **Template Post Hero** — Use the Hero module in a single post template with the title field set to dynamic post title content. The subtitle can pull from a custom field (such as a tagline), and the background image can map to the featured image. This creates a consistent, visually rich header for every post without manual configuration.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/hero` — *Needs verification on current build*

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
| Subtitle | `attrs.subtitle` | Secondary heading text |
| Body | `attrs.content` | Descriptive body content |
| Button One Text | `attrs.button_one_text` | Primary CTA button label |
| Button Two Text | `attrs.button_two_text` | Secondary CTA button label |
| Image | `attrs.image` | Hero background or featured image |

!!! tip "Module Selection Guidance"
    For hero sections within content columns use Hero; for edge-to-edge heroes use Fullwidth Header; for rotating heroes use Slider.

## Saving Your Work

After configuring the Hero module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Background Image Not Displaying"
    If the hero background appears blank:

    - Distinguish between the **Images > Header Image** field and the **Background** settings. The header image is a content-level image, while the background is applied via the Background controls.
    - Ensure the image URL is correct and the file exists at the specified location.
    - If using a video background, verify that the video file format is supported (MP4 is most reliable) and the file is accessible.

!!! warning "Buttons Not Appearing"
    If one or both CTA buttons are missing:

    - Both the button text and a link URL must be provided for a button to render. An empty text field hides the button entirely.
    - Check that button text color and background color are not identical, which would make the button appear invisible.
    - In the Design tab, verify that button font size is not set to 0.

!!! tip "Improving Mobile Hero Performance"
    Full-screen heroes with large background images can affect mobile load times. Use the responsive toggle to set a smaller, optimized image for phone breakpoints. Consider disabling the overlay on mobile if it adds unnecessary rendering cost, and reduce padding to prevent excessive scrolling on small screens.

## Related

- [Fullwidth Header](fullwidth-header.md) — Legacy fullwidth header module with similar hero-style layout capabilities
- [Slider](slider.md) — Sliding content panels with text overlays and navigation controls
- [Call to Action](call-to-action.md) — Focused conversion block with heading, description, and button
- [Background Options](../options-groups/background.md) — Configure background images, videos, and gradients for hero sections
- [Button Options Group](../options-groups/button.md) — Style the hero's call-to-action buttons
- [Scroll Effects Options](../options-groups/scroll-effects.md) — Add parallax and scroll-driven animations to hero content
