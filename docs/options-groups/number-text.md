---
title: "Number Text Options"
category: options-groups
tags: ["options-groups", "number-text"]
related: ["percentage-text", "title-text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10260390"
---

# Number Text Options

Controls the typography and styling of numeric text elements displayed by Divi 5 modules.

## Overview

The Number Text options group provides design controls for styling the numeric values that appear in counter and statistic modules. When a module displays a prominent number, such as a count-up animation target or a statistical figure, this options group determines how that number is rendered.

These settings are located in the Design tab of the module settings panel. You can select a font, adjust weight and size, set alignment, control letter and line spacing, and apply text shadow effects. These controls allow you to make numbers visually prominent and distinct from surrounding title or body text.

Numeric text often serves as a focal point in layouts that highlight achievements, statistics, or key metrics. Styling numbers with larger sizes, bolder weights, or contrasting colors helps draw attention and communicate importance effectively.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10260390).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Number Font | Font selector | Chooses the typeface for numeric text, supporting default and custom fonts. |
| Number Font Weight | Selector | Adjusts the boldness of the number text from light to extra-bold. |
| Number Font Style | Toggle options | Applies italics, capitalization, small caps, underline, or strikethrough to numeric text. |
| Number Text Alignment | Alignment selector | Positions the number text as left, center, right, or justified. |
| Number Text Color | Color picker | Sets the color of the numeric text from the site palette or a custom value. |
| Number Text Size | Range slider / input | Defines the font size of the numeric text. |
| Number Letter Spacing | Range slider / input | Controls the spacing between characters in the number. |
| Number Line Height | Range slider / input | Sets the vertical distance between lines of numeric text. |
| Number Text Shadow | Shadow editor | Adds a shadow effect with controls for horizontal/vertical position, blur strength, and shadow color. |

## Which Elements Use This

The Number Text options group is primarily used by the Number Counter module in Divi 5. It controls the appearance of the animated counter value that the module displays.

## Code Examples

```css
/* Style the number counter value */
.et_pb_number_counter .percent p {
  font-size: 48px;
  font-weight: 800;
  color: #0984e3;
}
```

## Related

- [Percentage Text Options](percentage-text.md) -- Typography controls for percentage values in bar counters
- [Title Text Options](title-text.md) -- Typography controls for module titles
