---
title: "Person"
category: modules
tags: ["modules"]
related: ["testimonial", "blurb"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/person/"
---

# Person

The Person module is a Divi 5 content element used in the Visual Builder.

## Overview

How to add, configure and customize the Divi person module.

The Person Module is the best way to create a personal profile for someone on your Divi website. It’s an easy way to highlight team members, featured vendors, company leadership, staff, and more. This is a great module to use on About Me or Team Member pages. It combines text, imagery, and social media links into a single, cohesive module.

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/person/)

![Person module](../assets/screenshots/modules/person/element.png){ loading=lazy }
*The Person module as it appears on the live demo.*


## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Person module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Content settings --> | | | |

<!-- TODO: Replace with proper screenshot -->
<!-- ![Person Content tab settings](../assets/screenshots/modules/person/settings-content.png){ loading=lazy } -->

### Design Tab

<!-- TODO: Verify all Design tab settings for Person module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

<!-- TODO: Replace with proper screenshot -->
<!-- ![Person Design tab settings](../assets/screenshots/modules/person/settings-design.png){ loading=lazy } -->

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Person module -->

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
/* Style the Person module */
.et_pb_person {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_person {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Person module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_person' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Person module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Person module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

- [Testimonial](testimonial.md)
- [Blurb](blurb.md)
