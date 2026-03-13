---
title: "Toggle"
category: modules
tags: ["modules"]
related: ["accordion", "tabs"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/toggle/"
---

# Toggle

The Toggle module is a Divi 5 content element used in the Visual Builder.

## Overview

How to add, configure and customize the Divi toggle module.

The Divi Toggle Module allows you to show or hide content with the click of a button. It’s an easy way to share a lot of information without cluttering your design by consolidating your content and improving user experience. The toggle module can be put in any sized column and you can add as many toggles as you’d like.

You can use the toggle module to build aFAQs section, arestaurant menu, aservices section, sharepricing info, and more!

<!-- TODO: Replace with proper screenshot -->
<!-- ![Toggle module overview](../assets/screenshots/modules/toggle/overview.png){ loading=lazy } -->
<!-- *The Toggle module as it appears in the Divi 5 Visual Builder.* -->

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for Toggle module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Content settings --> | | | |

<!-- ![Toggle Content tab settings](../assets/screenshots/modules/toggle/settings-content.png){ loading=lazy } -->

### Design Tab

<!-- TODO: Verify all Design tab settings for Toggle module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

<!-- ![Toggle Design tab settings](../assets/screenshots/modules/toggle/settings-design.png){ loading=lazy } -->

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for Toggle module -->

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
/* Style the Toggle module */
.et_pb_toggle {
    /* Add your custom styles */
    margin-bottom: 30px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_toggle {
        padding: 20px;
    }
}
```

### PHP Hooks

```php
/* Filter the Toggle module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_et_pb_toggle' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the Toggle module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Toggle module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

- [Accordion](accordion.md)
- [Tabs](tabs.md)
