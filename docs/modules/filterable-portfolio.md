---
title: "Filterable Portfolio"
category: modules
tags: ["modules", "portfolio"]
related: ["portfolio", "gallery", "fullwidth-portfolio"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/filterable-portfolio/"
---

# Filterable Portfolio

The Filterable Portfolio module is a Divi 5 content element used in the Visual Builder.

## Overview

How to add, configure and customize the Divi filterable portfolio module.

The Divi Filterable Portfolio Module is similar to the Divi Portfolio Module but has additional sorting functionality. Users can click the categories at the top to dynamically sort and view the projects they’d like to see. This module integrates seamlessly with the native WordPress projects functionality and is great to display your work or demonstrate case studies.

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/filterable-portfolio/)

![Filterable Portfolio module](../assets/screenshots/modules/filterable-portfolio/element.png){ loading=lazy }
*The Filterable Portfolio module as it appears on the live demo.*


## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Filterable Portfolio module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Content settings --> | | | |

<!-- TODO: Replace with proper screenshot -->
<!-- ![Filterable Portfolio Content tab settings](../assets/screenshots/modules/filterable-portfolio/settings-content.png){ loading=lazy } -->

### Design Tab

<!-- TODO: Verify all Design tab settings for Filterable Portfolio module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

<!-- TODO: Replace with proper screenshot -->
<!-- ![Filterable Portfolio Design tab settings](../assets/screenshots/modules/filterable-portfolio/settings-design.png){ loading=lazy } -->

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Filterable Portfolio module -->

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
/* Style the Filterable Portfolio module */
.et_pb_filterable_portfolio {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_filterable_portfolio {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Filterable Portfolio module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_filterable_portfolio' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Filterable Portfolio module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Filterable Portfolio module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

- [Portfolio](portfolio.md)
- [Gallery](gallery.md)
- [Fullwidth Portfolio](fullwidth-portfolio.md)
