---
title: "Toggle Options"
category: options-groups
tags: ["options-groups", "toggle"]
related: ["accordion-icon", "toggle-icon"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10101806"
---

# Toggle Options

Controls the background colors for open and closed states of collapsible toggle elements in Divi 5.

## Overview

The Toggle options group provides background color controls for the two states of collapsible content items. In the Accordion and Toggle modules, each item can be either open (expanded) or closed (collapsed), and this options group lets you assign a distinct background color to each state.

These settings are found in the Design tab of the module settings panel. By assigning different colors to the open and closed states, you create a clear visual cue that helps users understand which items are expanded and which can be clicked to reveal content. This is especially valuable in longer accordion lists where quick scanning is important.

Both color settings support the site color palette and custom color values. For best results, choose colors with enough contrast to be easily distinguishable while maintaining harmony with your overall design. Also ensure that the text color (configured in the Title Text and Closed Title Text groups) remains legible against both background colors.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10101806).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Open Toggle Background Color | Color picker | Sets the background color of toggle items when they are in the expanded (open) state. |
| Closed Toggle Background Color | Color picker | Sets the background color of toggle items when they are in the collapsed (closed) state. |

## Which Elements Use This

The Toggle options group is used by the Accordion module and the Toggle module in Divi 5. It controls the background appearance of individual collapsible items in both modules.

## Code Examples

```css
/* Custom toggle state backgrounds */
.et_pb_toggle_open {
  background-color: #dfe6e9;
}

.et_pb_toggle_close {
  background-color: #f5f6fa;
}
```

## Related

- [Accordion Icon Options](accordion-icon.md) -- Icon styling for accordion toggle indicators
- [Toggle Icon Options](toggle-icon.md) -- Icon selection for the closed state indicator
