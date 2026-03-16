---
title: "Number Counter"
category: modules
tags: ["modules", "animation", "counter", "statistics", "numbers", "percentage", "data-visualization"]
related: ["circle-counter", "bar-counter", "countdown-timer"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10353752-the-number-counter-module-in-divi-5"
---

# Number Counter

The Number Counter module displays an animated number that counts up from zero to a specified value, ideal for showcasing statistics and key figures.

## Overview

The Number Counter module provides an engaging way to present numerical data on your Divi 5 pages. When a visitor scrolls the module into view, it animates from zero up to the target number you have defined, creating an eye-catching counting effect that draws attention to important figures. You can display whole numbers or percentages, making it suitable for everything from project completion rates to company milestones.

This module works well in data-driven sections where you want to communicate achievements, capabilities, or metrics at a glance. Common applications include displaying years of experience, number of clients served, projects completed, or satisfaction percentages. The animation triggers on scroll, so visitors experience the counting effect as they reach that part of the page.

Each Number Counter module displays a single number with an optional title label above it and an optional percentage sign. To present multiple statistics side by side, place several Number Counter modules in adjacent columns within a row. The Design tab gives you independent typography controls for both the title and the number, so you can create strong visual hierarchy between the label and the figure.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10353752-the-number-counter-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/number-counter/)

![Number Counter module](../assets/screenshots/modules/number-counter/element.png){ loading=lazy }
*The Number Counter module as it appears on the live demo.*

## Use Cases

1. **Company Statistics Section** — Arrange three or four Number Counter modules in a row to highlight key business metrics such as total customers, years in business, team members, and countries served. The animated counting draws attention as visitors scroll into the section.

2. **Skill or Progress Indicators** — Use the percentage sign option to display proficiency levels for different skills on a portfolio or resume page. Pair each counter with a descriptive title like "WordPress Development" or "UI Design" to communicate expertise areas.

3. **Fundraising or Campaign Progress** — Display the current dollar amount raised, number of donors, or percentage of goal reached on a nonprofit or crowdfunding landing page. Update the number field periodically to keep the figure current.

## How to Add the Number Counter Module

1. **Open the Visual Builder** on your target page. Click the gray plus icon inside a row to open the module picker, then search for "Number Counter" and click to insert it.

2. **Set the title and number** in the Content tab's Text group. Enter a descriptive title (such as "Projects Completed") and the target number value. Toggle the percentage sign on or off depending on whether your figure represents a percentage.

3. **Style the output** using the Design tab. Customize the title and number typography independently, adjust sizing and spacing, and choose an entrance animation. Save your page when finished.

## Settings & Options

### Content Tab

The Content tab is where you define the number to display, the title text, and whether a percentage symbol appears alongside the figure.

| Setting | Type | Description |
|---------|------|-------------|
| **Text — Title** | text | Enter the label that appears above the animated number, such as "Happy Clients" or "Years Experience" |
| **Text — Number** | number | Set the target value the counter animates up to when it enters the viewport |
| **Elements — Percent Sign** | toggle | Show or hide a percentage symbol (%) next to the animated number |
| **Link** | URL / toggle | Make the entire module a clickable link and configure the destination URL, target, and rel attributes |
| **Background** | composite | Set background color, gradient, image, or video behind the module |
| **Loop** | toggle | Enable the Loop Builder to render this module dynamically within loop templates |
| **Order** | number | Set the display order of the module inside a Flexbox or CSS Grid layout |
| **Meta — Label** | text | Assign a label for identification in the Visual Builder layer panel |
| **Meta — Force Visibility** | toggle | Keep the module visible in the Visual Builder even when conditions would normally hide it |

### Design Tab

The Design tab provides separate typography controls for the title and number, along with all standard visual styling options.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Number Text | text styling | Font, weight, style, color, size, letter spacing, line height, and text shadow for the animated number display. Typically set larger than the title. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Title Text](../options-groups/title-text.md) | Font, size, color, letter spacing, line height, text shadow for the title label |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding per side, responsive breakpoints |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Color, offsets, blur radius, spread |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue, blur, invert, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, scroll-driven effects, and positioning.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Semantic HTML tag for the module wrapper (div, section) |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

## Code Examples

### Custom CSS

```css
/* Make the number large and bold with a brand color */
.et_pb_number_counter .percent p {
    font-size: 72px;
    font-weight: 800;
    color: #2563eb;
}

/* Style the title beneath the number */
.et_pb_number_counter h3 {
    font-size: 16px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #6b7280;
    margin-top: 10px;
}

/* Add a circular background behind each counter */
.et_pb_number_counter {
    background: #f0f9ff;
    border-radius: 50%;
    width: 200px;
    height: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
}

/* Responsive sizing for smaller screens */
@media (max-width: 980px) {
    .et_pb_number_counter {
        width: 150px;
        height: 150px;
    }

    .et_pb_number_counter .percent p {
        font-size: 48px;
    }
}
```

### PHP Hooks

```php
/* Filter the Number Counter module to append a custom suffix */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_number_counter' !== $render_slug) {
        return $output;
    }
    // Add a "+" symbol after counters that represent growth metrics
    $output = str_replace('</span>', '+</span>', $output);
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Statistics Row with Icons** — Place three or four Number Counter modules in equal-width columns within a single row. Give each column a background color or icon above the counter using a Blurb module, creating a visually balanced statistics bar that communicates key metrics at a glance.

2. **Before-and-After Comparison** — Use two adjacent Number Counter modules to show a past value and a current value side by side, such as "2020 Revenue" at 500 and "2025 Revenue" at 1200. Add distinct colors to each number to emphasize the growth between the two periods.

3. **Percentage-Based Skill Bars** — Enable the percent sign toggle and set values between 0 and 100 to represent proficiency or completion rates. Stack several counters vertically on a resume or portfolio page, each with a different title like "HTML/CSS" or "Project Management," to create a dynamic skills showcase.

## Saving Your Work

After configuring the Number Counter module, click the green **Save** button at the bottom of the Visual Builder page settings bar. To reuse a particular counter configuration across multiple pages, right-click the module and select **Save to Library**. You can also save the entire row of counters as a library item to maintain consistent styling.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Number Counter module in Divi 5 includes the updated options framework with Flexbox and Grid ordering, conditions, interactions, and scroll effects that are not present in Divi 4. If you are still using Divi 4, consult the legacy Elegant Themes documentation.

## Troubleshooting

!!! warning "Counter Not Animating"
    If the number appears instantly at its final value without the counting animation, check whether a caching plugin is serving a static version of the page that bypasses JavaScript execution. Clear your site cache and any CDN cache layers. Also verify that no JavaScript errors appear in the browser console, as script conflicts can prevent the animation from initializing.

!!! warning "Number Displays as Zero"
    If the counter stays at zero and never counts up, confirm that you have entered a numeric value in the Number field under the Content tab's Text group. Non-numeric characters or empty fields will cause the counter to remain at zero. Also check that the module is not hidden by Visibility settings on the device you are testing.

!!! warning "Percentage Sign Missing"
    If you expect a percent symbol next to the number but it does not appear, open the Content tab and expand the Elements group. Make sure the Percent Sign toggle is enabled. This setting is off by default, so it must be explicitly turned on for percentage-based counters.

## Related

- [Circle Counter](circle-counter.md)
- [Bar Counter](bar-counter.md)
- [Countdown Timer](countdown-timer.md)
