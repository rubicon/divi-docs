---
title: "Number Counter"
category: modules
tags: ["modules", "animation"]
related: ["bar-counter", "circle-counter"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/number-counter/"
---

# Number Counter

The Number Counter module is a Divi 5 content element used in the Visual Builder.

## Overview

How to add, configure and customize the Divi number counter module.

The Divi Number Counter Module is an easy way to display numerical information about yourself or your company in an eye-catching design. The Number Counter Module can display both plain numerical numbers as well as percentages. When the Number Counter Module loads, it starts from zero and then counts up to the number or percentage you specified and then stops.

View A Live Demo Of This Module

<!-- TODO: Replace with proper screenshot -->
<!-- ![Number Counter module overview](../assets/screenshots/modules/number-counter/overview.png){ loading=lazy } -->
<!-- *The Number Counter module as it appears in the Divi 5 Visual Builder.* -->

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Number Counter module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Content settings --> | | | |

<!-- TODO: Replace with proper screenshot -->
<!-- ![Number Counter Content tab settings](../assets/screenshots/modules/number-counter/settings-content.png){ loading=lazy } -->

### Design Tab

<!-- TODO: Verify all Design tab settings for Number Counter module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

<!-- TODO: Replace with proper screenshot -->
<!-- ![Number Counter Design tab settings](../assets/screenshots/modules/number-counter/settings-design.png){ loading=lazy } -->

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Number Counter module -->

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
/* Style the Number Counter module */
.et_pb_number_counter {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_number_counter {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Number Counter module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_number_counter' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Number Counter module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Number Counter module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

- [Bar Counter](bar-counter.md)
- [Circle Counter](circle-counter.md)
