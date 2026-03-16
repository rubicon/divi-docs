---
title: "Countdown Timer"
category: modules
tags: ["modules", "countdown", "timer", "date", "event", "urgency", "interactive"]
related: ["number-counter", "circle-counter"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10273123-the-countdown-timer-module-in-divi-5"
---

# Countdown Timer

The Countdown Timer module displays a real-time countdown to a specific date and time, showing the remaining days, hours, minutes, and seconds.

## Overview

The Countdown Timer module lets you place an animated, live-updating timer on any page or post. You set a target date and time, and the module automatically calculates and displays the remaining duration broken into days, hours, minutes, and seconds. Each unit updates in real time without requiring a page refresh, giving visitors an immediate sense of urgency or anticipation.

This module is particularly effective for time-sensitive marketing. Whether you are promoting a product launch, building excitement for a live event, running a limited-time sale, or creating a "coming soon" landing page, the countdown timer draws attention and encourages visitors to act before time runs out.

The timer supports full visual customization through the Design tab, where you can style the number displays, separator characters, labels, and surrounding text independently. You can also set a title above the timer to provide context for what visitors are counting down to.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10273123-the-countdown-timer-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/countdown-timer/)

![Countdown Timer module](../assets/screenshots/modules/countdown-timer/element.png){ loading=lazy }
*The Countdown Timer module displaying a live countdown with days, hours, minutes, and seconds.*

## Use Cases

1. **Product Launch Countdown** — Place a countdown timer on a landing page to build anticipation for a new product or service release, paired with a pre-order button or email signup form.
2. **Limited-Time Sale Banner** — Add a timer to a promotional section to show exactly how much time remains in a flash sale or seasonal discount, creating urgency that drives conversions.
3. **Event Countdown** — Display a countdown to a webinar, conference, or live stream start time so visitors know precisely when to tune in or show up.

## How to Add the Countdown Timer Module

1. Open the Visual Builder on the page where you want to place the countdown timer.
2. Click the gray **+** icon inside any row to add a new module.
3. Search for "Countdown Timer" in the module picker or browse the Content Elements category, then click to insert it.

## Settings & Options

The Countdown Timer module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab is where you set the countdown target date, title text, link behavior, and background styling.

| Setting | Type | Description |
|---------|------|-------------|
| Title | text | The heading displayed above the countdown timer. Use this to tell visitors what they are counting down to, such as "Sale Ends In" or "Event Starts In." |
| Date | date/time picker | The target date and time the countdown is counting toward. When this date is reached, the timer displays all zeros. |
| Link | url | Optionally wrap the entire module in a link so clicking anywhere on it navigates to a specified URL. Useful for linking to an event page or product listing. |
| Background | background controls | Set a background color, gradient, image, or video behind the entire countdown timer module. |
| Loop | toggle | Enable the loop builder to use this module as a repeating element within dynamic content layouts. |
| Order | select | Control the module's display order when its parent row uses Flexbox or CSS Grid layout. |
| Meta | admin label | Assign a custom label to identify this module in the Visual Builder's layer panel. Helpful when a page has multiple countdown timers. |

### Design Tab

The Design tab provides granular control over the typography and visual appearance of every element within the countdown timer.

| Setting | Type | Description |
|---------|------|-------------|
| Text | text styling | Set the default font family, weight, style, alignment, and color for general text within the module. |
| Title Text | text styling | Style the title heading independently — font, size, color, letter spacing, line height, and text shadow. |
| Numbers | text styling | Control the appearance of the countdown digits (days, hours, minutes, seconds). Set the font family, size, weight, color, and spacing for the numerical display. |
| Separator Text | text styling | Style the separator characters between the countdown units (typically colons or other dividers). Adjust font, size, and color. |
| Label Text | text styling | Customize the labels beneath each number group (e.g., "Days," "Hours," "Minutes," "Seconds"). Control font, size, color, and letter spacing. |
| Sizing | dimensions | Set the module's width, max-width, min-height, and overall dimensions. Supports responsive values for each device breakpoint. |
| Spacing | margin/padding | Configure margin and padding values around and within the module. Supports individual values per side and per device. |
| Border | border controls | Add borders around the module with configurable width, color, style, and border radius for rounded corners. |
| Box Shadow | shadow controls | Apply a box shadow effect with adjustable horizontal and vertical offset, blur radius, spread, and shadow color. |
| Filters | image filters | Apply CSS filter effects including brightness, contrast, saturation, hue rotation, invert, sepia, opacity, and blur. |
| Transform | transform controls | Apply CSS transforms such as scale, translate, rotate, and skew. Set the transform origin point for precise control. |
| Animation | animation select | Choose an entrance animation (fade, slide, bounce, zoom, flip, fold, roll) with configurable duration, delay, intensity, and starting opacity. |

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display logic, and scroll-driven effects.

| Setting | Type | Description |
|---------|------|-------------|
| Attributes | text fields | Assign a CSS ID and one or more CSS classes to the module for targeting with custom styles or JavaScript. |
| CSS | code editor | Write custom CSS rules that apply to specific internal elements of the module (container, title, numbers, labels, separators). |
| HTML | code fields | Add custom HTML attributes to the module's wrapper element, such as `data-*` attributes for JavaScript interaction. |
| Conditions | condition builder | Set display conditions so the module only renders when specific rules are met (user role, page type, date range, or custom logic). |
| Interactions | interaction builder | Define hover, click, or scroll-triggered interactions that affect this module or other elements on the page. |
| Visibility | device toggles | Show or hide the module on desktop, tablet, and/or phone. Hidden modules are excluded from the rendered page source on that device. |
| Transitions | transition controls | Configure CSS transition duration, easing function, and delay for hover state changes on the module. |
| Position | position controls | Set the CSS position property (relative, absolute, fixed, sticky) along with top, right, bottom, left offset values and z-index. |
| Scroll Effects | scroll controls | Apply scroll-driven effects like parallax movement, fade, scale, rotate, blur, or horizontal translation as the user scrolls past the module. |

## Code Examples

### Custom CSS

```css
/* Style the countdown timer container */
.et_pb_countdown_timer {
    text-align: center;
    padding: 40px 20px;
}

/* Style the countdown number sections */
.et_pb_countdown_timer .section {
    display: inline-block;
    margin: 0 15px;
}

/* Style the countdown digits */
.et_pb_countdown_timer .section p.value {
    font-size: 48px;
    font-weight: 700;
    color: #2ea3f2;
}

/* Style the unit labels (Days, Hours, etc.) */
.et_pb_countdown_timer .section p.label {
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #666;
}

/* Style the separator between units */
.et_pb_countdown_timer .sep {
    font-size: 36px;
    color: #ccc;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_countdown_timer .section {
        margin: 0 8px;
    }
    .et_pb_countdown_timer .section p.value {
        font-size: 32px;
    }
}
```

### PHP Hooks

```php
/* Filter the Countdown Timer module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_countdown_timer' !== $render_slug) {
        return $output;
    }
    // Example: add a wrapper div around the timer
    $output = '<div class="custom-countdown-wrapper">' . $output . '</div>';
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Hero Section Countdown** — Place the countdown timer in a full-width section with a background image or video, paired with a heading module above and a call-to-action button below. This creates a high-impact landing page for product launches or events.

2. **Sale Notification Bar** — Add the countdown timer to a narrow row at the top of the page with a bold background color and compact sizing. Pair it with short text like "Flash Sale Ends In:" to create an urgency bar that stays visible as visitors browse.

3. **Event Registration Page** — Combine the countdown timer with a blurb module listing event details and an email optin or button module for registration. Style the timer numbers in your brand colors and use the title field to display the event name.

## Saving Your Work

After configuring the countdown timer:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Timer Shows All Zeros"
    If the countdown timer displays 00:00:00:00, the target date has already passed. Open the module settings and update the date/time field to a future date. Double-check the timezone settings in your WordPress General Settings to ensure the timer is calculating against the correct timezone.

!!! warning "Numbers Not Updating in Real Time"
    If the countdown appears frozen or only updates on page refresh, JavaScript may be blocked or encountering an error. Check the browser console for JavaScript errors, and verify that no caching plugin is serving a fully static version of the page. Exclude the page from full-page caching if necessary.

!!! tip "Timer Looks Misaligned on Mobile"
    On smaller screens, the countdown units may stack awkwardly if the container is too narrow. Use the Spacing settings in the Design tab to reduce margins between units, or apply custom CSS to adjust the layout at mobile breakpoints. Consider reducing the font size of the numbers and labels for phone devices.

## Related

- [Number Counter](number-counter.md) — Animated number counting for statistics and metrics
- [Circle Counter](circle-counter.md) — Circular progress indicators with animated fill
