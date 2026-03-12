---
title: "Slider"
category: modules
tags: ["modules", "slider"]
related: ["post-slider", "video-slider", "fullwidth-slider"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/slider/"
---

# Slider

The Slider module is a Divi 5 content element used in the Visual Builder.

## Overview

How to add, configure and customize the Divi slider module.

The Divi Slider Module can be placed anywhere on your website. Sliders can be large, small, fixed-width, or full-width. You can add a parallax background image as well as full-width video backgrounds.

View A Live Demo Of This Module

![Slider module overview](../assets/screenshots/modules/slider/overview.png){ loading=lazy }
*The Slider module as it appears in the Divi 5 Visual Builder.*

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Slider module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Content settings --> | | | |

![Slider Content tab settings](../assets/screenshots/modules/slider/settings-content.png){ loading=lazy }

### Design Tab

<!-- TODO: Verify all Design tab settings for Slider module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

![Slider Design tab settings](../assets/screenshots/modules/slider/settings-design.png){ loading=lazy }

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Slider module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| CSS ID | text | — | Assign a unique CSS ID to the module |
| CSS Class | text | — | Assign CSS classes to the module |
| Custom CSS | code | — | Add custom CSS directly to the module's elements |
| Visibility | toggle | Show on all devices | Control device visibility (desktop, tablet, phone) |
| Transition | select | Default | Animation transition style for hover effects |

## Code Examples

### Custom CSS

```css
/* Style the Slider module */
.et_pb_slider {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_slider {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Slider module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_slider' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Slider module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Slider module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

- [Post Slider](post-slider.md)
- [Video Slider](video-slider.md)
- [Fullwidth Slider](fullwidth-slider.md)
