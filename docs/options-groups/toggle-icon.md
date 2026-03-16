---
title: "Toggle Icon Options"
category: options-groups
tags: ["options-groups", "toggle-icon"]
related: ["accordion-icon", "toggle"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10101671"
---

# Toggle Icon Options

Lets you select which icon is displayed for accordion items in their closed state.

## Overview

The Toggle Icon options group provides an icon picker for choosing the visual indicator shown when an accordion item is collapsed. By default, Divi uses a standard icon (such as a plus symbol or arrow) to indicate that content can be expanded. This options group lets you replace that default with any icon from the available Divi icon library.

This setting is located in the Content tab of the Accordion module settings panel. It controls only the icon selection itself; for icon color and size styling, see the separate Accordion Icon options group in the Design tab.

Choosing an appropriate icon is important for usability. Icons like a plus sign, downward arrow, or chevron are universally recognized as expand/collapse indicators. The icon should clearly communicate that the content can be toggled, and it should visually align with the overall style of your site.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10101671).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Icon | Icon picker | Selects the icon displayed on accordion items in the closed state. Choose from the Divi icon library. |

## Which Elements Use This

The Toggle Icon options group is used by the Accordion module in Divi 5. It determines which icon appears next to the title of collapsed accordion items, serving as a visual cue for expandable content.

## Code Examples

```css
/* Override the toggle icon with a custom font icon */
.et_pb_accordion .et_pb_toggle_close .et-pb-icon::before {
  content: "\e050"; /* Divi icon code */
}
```

## Related

- [Accordion Icon Options](accordion-icon.md) -- Color and size controls for the accordion toggle icon
- [Toggle Options](toggle.md) -- Background colors for open and closed toggle states
