---
title: "Understanding Flex Wrapping Alignment Options in Divi 5"
category: builder
tags: ["builder", "flexbox", "layout", "flex-wrap", "align-content"]
related: ["understanding-divi-s-new-flexbox-layout.md", "understanding-flex-justify-content-in-divi-5.md", "understanding-flex-align-items-options-in-divi-5.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11884457-understanding-flex-wrapping-alignment-options-in-divi-5"
---

# Understanding Flex Wrapping Alignment Options in Divi 5

Flex Wrap controls whether flex items wrap to multiple lines when they exceed container width. Align Content controls how wrapped lines are distributed along the cross axis.

## Overview

Flex Wrap and Align Content work together to manage multi-line layouts in Divi 5. By default, flex items shrink to fit in a single line. When Flex Wrap is enabled, items that don't fit will wrap to the next line, creating a responsive grid-like behavior without needing explicit grid settings.

Align Content is the multi-line equivalent of Justify Content. While Justify Content controls spacing of items along the main axis within a single line, Align Content controls how multiple wrapped lines are distributed along the cross axis (vertically in Row layouts, horizontally in Column layouts). Together, these properties give you precise control over responsive, wrapped layouts.

## Settings & Options

### How to Access

Open a Section or Row in the Visual Builder → Design tab → Layout group.

### Flex Wrap Options

**Flex Wrap** controls whether items wrap to new lines.

| Value | Description |
|-------|-------------|
| **No Wrap** | Default. All flex items stay on a single line, shrinking if necessary to fit. |
| **Wrap** | Items wrap to the next line when they exceed container width. Each line wraps independently. |

### Align Content Options

**Align Content** controls vertical distribution of wrapped lines (available when Flex Wrap is enabled).

| Value | Description |
|-------|-------------|
| **Start** | Wrapped lines are aligned to the start of the container (top in Row layouts, left in Column layouts). No spacing between lines. |
| **Center** | Wrapped lines are centered vertically with equal space above and below the group. |
| **End** | Wrapped lines are aligned to the end of the container (bottom in Row layouts, right in Column layouts). |
| **Space Between** | Wrapped lines are distributed evenly. The first line is flush with the start, the last line is flush with the end, and remaining lines are equally spaced. |
| **Space Around** | Wrapped lines have equal space around each line. Space before the first line and after the last line is half the space between lines. |
| **Space Evenly** | Wrapped lines are distributed with equal space before, between, and after each line. Creates uniform vertical spacing. |
| **Stretch** | Wrapped lines are stretched to fill the available vertical space equally. |

### Layout Direction

**Layout Direction** determines the primary axis for wrapping.

| Value | Description |
|-------|-------------|
| **Row** | Items flow left-to-right (LTR) and wrap vertically. Primary axis is horizontal. |
| **Column** | Items flow top-to-bottom and wrap horizontally. Primary axis is vertical. |

## Common Patterns

1. **Responsive Product Grid** — Set Flex Wrap to Wrap with Align Content to Space Evenly. Products automatically wrap to the next row and maintain consistent vertical spacing without media queries.

2. **Masonry-Style Layout** — Use Flex Wrap with Align Content set to Start or Center for a Pinterest-like layout where cards wrap naturally based on container width.

3. **Multi-Line Navigation** — Enable Flex Wrap to allow navigation items to wrap on smaller screens, maintaining readability without custom breakpoints.

## Code Examples

```css
/* Enable wrapping with items flowing left-to-right */
.et_pb_row {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
}

/* Distribute wrapped lines with equal vertical spacing */
.et_pb_section {
  display: flex;
  flex-wrap: wrap;
  align-content: space-evenly;
}

/* Column layout with items wrapping horizontally */
.et_pb_column {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  align-content: center;
}

/* Stretch wrapped lines to fill available height */
.et_pb_row {
  display: flex;
  flex-wrap: wrap;
  align-content: stretch;
  height: 400px;
}
```

## Troubleshooting

!!! warning "Flex Wrap Not Working"
    Flex Wrap only wraps items when they exceed container width. If items are still shrinking instead of wrapping, check that the total width of wrapped items exceeds the parent container width. You may need to set minimum widths on child modules.

!!! warning "Align Content Has No Effect"
    Align Content only works when Flex Wrap is enabled and items actually wrap to multiple lines. With a single line of items, use Justify Content instead. Also ensure the parent container has sufficient height for Align Content spacing to be visible.

!!! warning "Uneven Line Heights with Wrap"
    Items on the same wrapped line inherit their height from the tallest item (default behavior). If you need uniform heights across all items regardless of content, set explicit height values on child modules or enable Align Items: Stretch.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 flexbox behavior exclusively. Divi 4 does not include the same flexbox layout system.

## Related

- [Understanding Divi's New Flexbox Layout](understanding-divi-s-new-flexbox-layout.md)
- [Understanding Flex Justify Content in Divi 5](understanding-flex-justify-content-in-divi-5.md)
- [Understanding Flex Align Items Options in Divi 5](understanding-flex-align-items-options-in-divi-5.md)
- [Understanding Flex Horizontal and Vertical Gap in Divi 5](understanding-flex-horizontal-and-vertical-gap-in-divi-5.md)
