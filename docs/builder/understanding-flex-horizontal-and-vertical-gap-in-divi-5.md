---
title: "Understanding Flex Horizontal and Vertical Gap in Divi 5"
category: builder
tags: ["builder", "flexbox", "layout", "gap", "spacing"]
related: ["understanding-divi-s-new-flexbox-layout.md", "understanding-flex-justify-content-in-divi-5.md", "understanding-flex-wrapping-alignment-options-in-divi-5.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11866030-understanding-flex-horizontal-and-vertical-gap-in-divi-5"
---

# Understanding Flex Horizontal and Vertical Gap in Divi 5

Horizontal and Vertical Gap create consistent spacing between flex items without using margins, making layouts more predictable and responsive.

## Overview

The Gap property is one of the most powerful flexbox features in Divi 5. Instead of managing spacing with margins on individual items, Gap creates consistent, automatic spacing between all flex items. This approach is cleaner, more maintainable, and responsive—gaps automatically adjust when items wrap or change layout direction.

Gap works differently than Justify Content: Justify Content distributes items across available space, while Gap creates a fixed space between each item, regardless of their size. You can set Horizontal Gap (space between items left-to-right in Row layouts) and Vertical Gap (space between items top-to-bottom in Column layouts) independently, giving you precise control over both axes.

## Settings & Options

### How to Access

Open a Section or Row in the Visual Builder → Design tab → Layout group.

### Horizontal Gap

**Horizontal Gap** controls the space between items along the horizontal axis (left-to-right in Row layouts).

| Setting | Default | Unit | Description |
|---------|---------|------|-------------|
| Horizontal Gap | 5.5% | %, px, em, rem, vh, vw | Space between items on the left-to-right axis. Can be set as a percentage of container width or fixed units. |

**Percentage values** are relative to the container width, making them fluid and responsive.

**Fixed values** (px, em, rem) remain constant regardless of screen size.

### Vertical Gap

**Vertical Gap** controls the space between items along the vertical axis (top-to-bottom in Column layouts, or between wrapped lines in Row layouts).

| Setting | Default | Unit | Description |
|---------|---------|------|-------------|
| Vertical Gap | 40px | %, px, em, rem, vh, vw | Space between items on the top-to-bottom axis. Fixed units (px) are most common for vertical spacing. |

### Interaction with Layout Direction

| Layout Direction | Horizontal Gap | Vertical Gap |
|------------------|---|---|
| **Row** | Controls space between items left-to-right | Controls space between wrapped lines (top-to-bottom) |
| **Column** | Controls space between wrapped items (left-to-right) | Controls space between items top-to-bottom |

## Common Patterns

1. **Responsive Card Grid** — Set Horizontal Gap to 5% and Vertical Gap to 30px. Cards maintain consistent spacing that scales with the container, creating a professional grid without media queries.

2. **Vertical List Layout** — Use Column layout with Horizontal Gap disabled (0) and Vertical Gap set to 20px. Creates stacked items with uniform spacing regardless of screen size.

3. **Adaptive Spacing** — Combine Horizontal Gap (percentage-based) and Vertical Gap (fixed units) for layouts that scale horizontally but maintain fixed vertical spacing for readability.

## Code Examples

```css
/* Set horizontal and vertical gap for flex items */
.et_pb_row {
  display: flex;
  gap: 2rem; /* Sets both horizontal and vertical gap */
  flex-wrap: wrap;
}

/* Separate horizontal and vertical gaps */
.et_pb_section {
  display: flex;
  row-gap: 40px;      /* Space between rows */
  column-gap: 5%;     /* Space between columns */
}

/* Grid-like layout with equal gaps on both axes */
.et_pb_row {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem 3rem; /* vertical horizontal gap syntax */
}

/* Override default Divi gap spacing */
.et_pb_column {
  gap: 1.5rem !important;
}
```

## Troubleshooting

!!! warning "Gap Not Appearing Between Items"
    Gap only creates space between items, not around the outer edges of the container. If you need space around the entire group, use padding on the parent container instead of gap. Also verify that Flex Wrap is enabled if items are on different lines.

!!! warning "Percentage Gap Behaves Unexpectedly"
    Percentage-based gaps are relative to the container width. In Column layouts or on very narrow screens, percentage gaps may become very small. Consider using fixed units (px, rem) for more predictable spacing, or test at different breakpoints.

!!! warning "Gap Creates Too Much Spacing in Responsive Layouts"
    If gap spacing becomes excessive on mobile, you may need responsive settings (via CSS or Divi's custom responsive controls). Alternatively, use smaller percentage values or fixed units that scale better.

!!! warning "Items Not Spacing Evenly with Justify Content"
    Remember that Gap creates space between items, while Justify Content controls how the entire group distributes across the container. Using both together gives you control over both item spacing and overall alignment. Experiment with combinations like "Justify Content: Space Between + Gap: 2rem" for different effects.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 flexbox behavior exclusively. Divi 4 does not include the same flexbox layout system or gap properties.

## Related

- [Understanding Divi's New Flexbox Layout](understanding-divi-s-new-flexbox-layout.md)
- [Understanding Flex Justify Content in Divi 5](understanding-flex-justify-content-in-divi-5.md)
- [Understanding Flex Wrapping Alignment Options in Divi 5](understanding-flex-wrapping-alignment-options-in-divi-5.md)
- [Understanding Flex Align Items Options in Divi 5](understanding-flex-align-items-options-in-divi-5.md)
