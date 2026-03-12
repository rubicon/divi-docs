---
title: "Countdown Timer"
category: modules
tags: ["modules"]
related: ["number-counter", "circle-counter"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/countdown/"
---

# Countdown Timer

The Countdown Timer module is a Divi 5 content element used in the Visual Builder.

## Overview

How to add, configure and customize the Divi Countdown Timer module.

The Divi Countdown Timer Module is a dynamic way to display a countdown timer on your website. The countdown timer can be used to count down to a product launch, an upcoming event, a seasononal sale, or even on a coming soon page announcing your website launch!

View A Live Demo Of This Module

![Countdown Timer module overview](../assets/screenshots/modules/countdown-timer/overview.png){ loading=lazy }
*The Countdown Timer module as it appears in the Divi 5 Visual Builder.*

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Countdown Timer module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Content settings --> | | | |

![Countdown Timer Content tab settings](../assets/screenshots/modules/countdown-timer/settings-content.png){ loading=lazy }

### Design Tab

<!-- TODO: Verify all Design tab settings for Countdown Timer module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

![Countdown Timer Design tab settings](../assets/screenshots/modules/countdown-timer/settings-design.png){ loading=lazy }

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Countdown Timer module -->

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
/* Style the Countdown Timer module */
.et_pb_countdown_timer {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_countdown_timer {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Countdown Timer module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_countdown_timer' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Countdown Timer module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Countdown Timer module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

- [Number Counter](number-counter.md)
- [Circle Counter](circle-counter.md)
