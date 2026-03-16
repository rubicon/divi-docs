---
title: "Visibility Options"
category: options-groups
tags: ["options-groups", "visibility", "advanced"]
related: ["conditions", "css"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102735"
---

# Visibility Options

The Visibility options group controls whether an element appears on specific device types and how it handles content that extends beyond its boundaries.

## Overview

Divi 5 provides Visibility settings under the Advanced tab of every module, giving you device-level display control and overflow management in a single location. These two capabilities work together to ensure your layouts look correct across all screen sizes and handle edge cases where content exceeds its container.

The device visibility toggles let you hide any element on phones, tablets, or desktops independently. This is useful when a design requires different layouts per breakpoint or when certain content is only relevant on mobile (such as a tap-to-call button) or desktop (such as a wide data table).

The overflow settings determine what happens when an element's content is larger than its container. You can allow the content to spill out visibly, clip it so it is hidden, or add scrollbars to let users navigate the overflow. Horizontal and vertical overflow are controlled separately, so you can scroll horizontally while clipping vertically, for example.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102735).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Disable On | Checkboxes | Hides the element on selected device types. Options are Phone, Tablet, and Desktop. Multiple devices can be selected simultaneously. |
| Horizontal Overflow | Dropdown | Controls how content that extends beyond the element's left or right edges is handled. Options are Visible (content spills out), Scroll (adds a horizontal scrollbar), Hidden (clips the overflow), and Auto (browser decides whether a scrollbar is needed). |
| Vertical Overflow | Dropdown | Controls how content that extends beyond the element's top or bottom edges is handled. Options are Visible (content spills out), Scroll (adds a vertical scrollbar), Hidden (clips the overflow), and Auto (browser decides whether a scrollbar is needed). |

## Which Elements Use This

All modules, columns, rows, and sections in the Divi 5 Visual Builder include the Visibility options group. The settings are found under the **Advanced** tab.

## Code Examples

```css
/* Hide overflow on a specific module to create a clipping mask effect */
.image-mask {
  overflow: hidden;
  border-radius: 50%;
}
```

```css
/* Add horizontal scrolling to a wide table within a module */
.scrollable-table-wrapper {
  overflow-x: auto;
  overflow-y: hidden;
  -webkit-overflow-scrolling: touch;
}
```

## Related

- [Conditions Options](conditions.md)
- [CSS Options](css.md)
