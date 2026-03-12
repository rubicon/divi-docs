---
title: "Fullwidth Header"
category: modules
tags: ["modules", "fullwidth"]
related: ["image", "call-to-action", "slider"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/fullwidth-header-new/"
---

# Fullwidth Header

The Fullwidth Header module is a Divi 5 content element used in the Visual Builder.

## Overview

How to add, configure and customize the Divi fullwidth header module.

The Divi Fullwidth Header Module is a versatile module that can be used all throughout your website design in many different ways. For example, you can use this module in a page template for posts, projects, and pages to display a dynamic post title. Or you can use it as a promotional design element to highlight an important page on your website, a downloadable freebie, promote a podcast, and more.

This module has the ability to display a title, subtitle, body text, two images, an icon and two in-line (side by side) buttons. In order to use the Fullwidth Header Module, you’ll need to add a fullwidth section first. In this doc, we’ll demonstrate how to use the Fullwidth Header Module on a homepage design to promote a tea subscription service for a Tea Shop.

![Fullwidth Header module overview](../assets/screenshots/modules/fullwidth-header/overview.png){ loading=lazy }
*The Fullwidth Header module as it appears in the Divi 5 Visual Builder.*

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Fullwidth Header module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Content settings --> | | | |

![Fullwidth Header Content tab settings](../assets/screenshots/modules/fullwidth-header/settings-content.png){ loading=lazy }

### Design Tab

<!-- TODO: Verify all Design tab settings for Fullwidth Header module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

![Fullwidth Header Design tab settings](../assets/screenshots/modules/fullwidth-header/settings-design.png){ loading=lazy }

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Fullwidth Header module -->

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
/* Style the Fullwidth Header module */
.et_pb_fullwidth_header {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_fullwidth_header {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Fullwidth Header module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_fullwidth_header' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Fullwidth Header module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Fullwidth Header module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

- [Image](image.md)
- [Call To Action](call-to-action.md)
- [Slider](slider.md)
