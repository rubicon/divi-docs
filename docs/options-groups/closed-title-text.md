---
title: "Closed Title Text Options"
category: options-groups
tags: ["options-groups", "closed-title-text"]
related: ["title-text", "toggle"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102283"
---

# Closed Title Text Options

Styles the title text of accordion and toggle items when they are in the closed (collapsed) state.

## Overview

The Closed Title Text options group provides a dedicated set of typography controls specifically for the closed state of collapsible content elements. When an Accordion or Toggle item is collapsed, its title can be styled differently from the open state, allowing for clear visual distinction between active and inactive items.

These settings are found in the Design tab of the Accordion module settings panel. If no custom closed title styles are applied, the titles inherit their appearance from the standard Title Text options group. By configuring Closed Title Text separately, you can use color, weight, or size changes to signal interactivity and guide users toward expandable content.

All settings in this group support Divi 5's responsive breakpoints, so you can fine-tune the closed title appearance independently for desktop, tablet, and mobile devices.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102283).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Closed Title Text Color | Color picker | Sets the text color for titles in the closed state. |
| Closed Text Heading Level | Dropdown | Defines the HTML heading tag (H1 through H6) for semantic hierarchy. |
| Closed Title Font | Font selector | Selects the typeface for closed titles, supporting default and custom fonts. |
| Closed Title Font Weight | Selector | Adjusts the boldness of the closed title, from light to extra-bold. |
| Closed Title Font Style | Toggle options | Applies italics, capitalization, small caps, underline, or strikethrough to closed titles. |
| Closed Title Text Alignment | Alignment selector | Positions the closed title as left, center, right, or justified. |
| Closed Title Text Size | Range slider / input | Sets the font size of the closed title text. |
| Closed Title Letter Spacing | Range slider / input | Controls the spacing between characters in the closed title. |
| Closed Title Line Height | Range slider / input | Defines the vertical distance between lines of closed title text. |
| Closed Title Text Shadow | Shadow editor | Adds a shadow effect to closed titles with direction, blur, and color controls. |

## Which Elements Use This

The Closed Title Text options group is used exclusively by the Accordion module in Divi 5. It controls the title appearance for toggle items that are in the collapsed state, complementing the standard Title Text group which handles the open state styling.

## Code Examples

```css
/* Style closed accordion titles differently */
.et_pb_accordion .et_pb_toggle_close h5 {
  color: #636e72;
  font-weight: 400;
}

.et_pb_accordion .et_pb_toggle_open h5 {
  color: #2d3436;
  font-weight: 700;
}
```

## Related

- [Title Text Options](title-text.md) -- Typography controls for open-state titles
- [Toggle Options](toggle.md) -- Background color settings for open and closed toggle states
