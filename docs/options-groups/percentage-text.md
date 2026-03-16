---
title: "Percentage Text Options"
description: "Divi 5 Percentage Text options group — font, size, weight, color, and spacing for percentage values in bar counter modules."
category: options-groups
tags: ["options-groups", "percentage-text"]
related: ["number-text", "title-text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10200244"
---

# Percentage Text Options

Controls the typography and styling of percentage values displayed by Divi 5 counter modules.

!!! abstract "Quick Reference"
    **What it controls:** Font, weight, size, color, alignment, letter spacing, line height, and text shadow for percentage labels
    **Where to find it:** Design Tab → Percentage Text
    **Available on:** Bar Counter module
    **Responsive:** Yes — all typography values can be set per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10200244)

## Overview

The Percentage Text options group provides design settings for the percentage value shown in bar counter and similar progress indicator modules. This numeric label typically animates to its target value and sits alongside or within the progress bar element.

These settings are found in the Design tab of the module settings panel. They offer the same set of typographic controls available in other text option groups: font selection, weight, style, color, alignment, size, letter spacing, line height, and text shadow. This consistency makes it easy to style percentage values in harmony with other text on the page.

Because the percentage value is a key visual element in any progress or achievement display, thoughtful styling helps communicate the intended emphasis. A large, bold percentage value can serve as the primary focal point, while a subtler treatment can let the bar graphic take center stage.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10200244).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Percentage Font | Font selector | Chooses the typeface for the percentage value, supporting default and custom fonts. |
| Percentage Font Weight | Selector | Adjusts the boldness of the percentage text from light to extra-bold. |
| Percentage Font Style | Toggle options | Applies italics, capitalization, small caps, underline, or strikethrough to the percentage value. |
| Percentage Text Alignment | Alignment selector | Positions the percentage text as left, center, right, or justified. |
| Percentage Text Color | Color picker | Sets the color of the percentage value from the site palette or a custom value. |
| Percentage Text Size | Range slider / input | Defines the font size of the percentage text. |
| Percentage Letter Spacing | Range slider / input | Controls the spacing between characters in the percentage value. |
| Percentage Line Height | Range slider / input | Sets the vertical distance between lines of percentage text. |
| Percentage Text Shadow | Shadow editor | Adds a shadow effect with controls for horizontal/vertical position, blur strength, and shadow color. |

## Which Elements Use This

The Percentage Text options group is primarily used by the Bar Counter module in Divi 5. It styles the percentage label that appears on or adjacent to the animated progress bar.

## Code Examples

```css
/* Style the bar counter percentage label */
.et_pb_counter_amount .et_pb_counter_amount_number {
  font-size: 14px;
  font-weight: 700;
  color: #ffffff;
}
```

## Related

- [Number Text Options](number-text.md) -- Typography controls for numeric counter values
- [Title Text Options](title-text.md) -- Typography controls for module titles
