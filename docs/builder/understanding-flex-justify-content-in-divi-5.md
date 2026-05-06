---
title: "Understanding Flex Justify Content in Divi 5"
category: builder
tags: ["builder", "flexbox", "layout", "justify-content", "alignment"]
related: ["understanding-divi-s-new-flexbox-layout.md", "understanding-flex-align-items-options-in-divi-5.md", "understanding-flex-order-option-in-divi-5.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11866965-understanding-flex-justify-content-in-divi-5"
---

# Understanding Flex Justify Content in Divi 5

Justify Content controls how flex items are distributed along the main axis (horizontally in row layouts, vertically in column layouts).

## Overview

The Justify Content property is a core flexbox control that determines the alignment and spacing of child elements along the main axis. This is essential for controlling how modules distribute across a Section or Row, creating balanced layouts, centered designs, and evenly spaced content without manual margins.

Justify Content works in combination with Layout Direction: when Layout Direction is set to Row, Justify Content controls horizontal alignment; when set to Column, it controls vertical alignment. This property is one of the most commonly used flexbox tools for centering, spacing, and distributing modules within containers.

## Settings & Options

### How to Access

Open a Section or Row in the Visual Builder → Design tab → Layout group → Justify Content dropdown.

### Justify Content Options

| Value | Description |
|-------|-------------|
| **Start** | Aligns all flex items to the start of the container (left in Row layouts, top in Column layouts). No spacing between items. |
| **Center** | Centers all flex items along the main axis. Equal space on both sides of the group. |
| **End** | Aligns all flex items to the end of the container (right in Row layouts, bottom in Column layouts). No spacing between items. |
| **Space Between** | Distributes flex items evenly across the available space. The first item is flush with the start, the last item is flush with the end, and remaining items are equally spaced between them. |
| **Space Around** | Distributes flex items evenly with equal space around each item. The space before the first item and after the last item is half the space between items. |
| **Space Evenly** | Distributes flex items evenly with equal space before, between, and after each item. Creates perfectly uniform spacing across all items. |

## Common Patterns

1. **Centered CTA Section** — Set Justify Content to Center to create a symmetrical call-to-action with buttons centered horizontally in a Row.

2. **Navigation Bar** — Use Space Between to position a logo on the left and navigation links on the right with maximum separation, filling the entire width.

3. **Equal Spacing Grid** — Use Space Evenly to distribute product cards, testimonials, or feature modules with consistent, equal gaps throughout the layout.

## Code Examples

```css
/* Justify items to the start (left/top) */
.et_pb_section {
  display: flex;
  justify-content: flex-start;
}

/* Center items along the main axis */
.et_pb_row {
  display: flex;
  justify-content: center;
}

/* Distribute with equal space around each item */
.et_pb_section {
  display: flex;
  justify-content: space-around;
}

/* Maximum spacing: equal gaps between and around all items */
.et_pb_row {
  display: flex;
  justify-content: space-evenly;
}
```

## Troubleshooting

!!! warning "Items Not Distributing Evenly"
    If Justify Content doesn't appear to work, check that your parent container (Section/Row) has sufficient width and that Layout Direction is set to Row. If Layout Direction is Column, Justify Content will align items vertically. Also verify that child modules do not have fixed widths that prevent flex distribution.

!!! warning "Space Between Not Creating Visible Gap"
    Space Between only works with 2 or more items. With a single item, it behaves like Start. To create spacing with a single item, consider using margin or spacing controls on the item itself.

!!! warning "Justify Content Ignored with Flex Wrap"
    When Flex Wrap is enabled and items wrap to multiple lines, Justify Content only controls alignment within each line. Use Align Content instead to control spacing between wrapped lines.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 flexbox behavior exclusively. Divi 4 does not include the same flexbox layout system.

## Related

- [Understanding Divi's New Flexbox Layout](understanding-divi-s-new-flexbox-layout.md)
- [Understanding Flex Align Items Options in Divi 5](understanding-flex-align-items-options-in-divi-5.md)
- [Understanding Flex Order Option in Divi 5](understanding-flex-order-option-in-divi-5.md)
- [Understanding Flex Wrapping Alignment Options in Divi 5](understanding-flex-wrapping-alignment-options-in-divi-5.md)
