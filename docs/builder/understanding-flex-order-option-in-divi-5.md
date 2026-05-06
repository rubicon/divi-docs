---
title: "Understanding Flex Order Option in Divi 5"
category: builder
tags: ["builder", "flexbox", "layout", "flex-order", "element-positioning"]
related: ["understanding-divi-s-new-flexbox-layout.md", "understanding-flex-justify-content-in-divi-5.md", "understanding-flex-align-items-options-in-divi-5.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11893079-understanding-flex-order-option-in-divi-5"
---

# Understanding Flex Order Option in Divi 5

The Flex Order option lets you reorder child elements within a flex container without changing their HTML source order, providing flexible layout control for responsive designs.

## Overview

Divi 5 leverages CSS Flexbox to manage layout behavior, and the Order property is a core flexbox feature that controls the visual sequence of flex items. By default, child elements (rows, modules, or columns) display in their natural HTML order. However, the **Flex Order** option allows you to override this visually by assigning numeric order values.

This is particularly useful when you want to:
- Rearrange elements for different screen sizes without duplicating content
- Create responsive layouts where the visual order differs from the source order
- Reorganize navigation, content sections, or grid-like layouts dynamically
- Maintain semantic HTML while achieving flexible presentation

The Order property accepts integer values (positive or negative). Elements are sorted from smallest to largest order value, and elements with the same order value appear in their original source order.

## Settings & Options

### How to Access

1. Select a **Row, Column, or Module** within a flex container (Section or Row)
2. Navigate to the **Content tab** (or **Design tab** depending on element type)
3. Look for the **Layout** section → **Order** field
4. Enter a numeric value

### Order Property Values

| Value | Behavior |
|-------|----------|
| `0` (default) | Element appears in its natural source order |
| Positive integers (1, 2, 3...) | Elements reorder from smallest to largest value |
| Negative integers (-1, -2, -3...) | Elements appear before those with 0 or positive values |

### Order Display Behavior

When multiple elements have Order values:
- **Order -2** appears first
- **Order -1** appears second  
- **Order 0** appears in its natural position among other 0-value items
- **Order 1** appears next
- **Order 2** appears last

## Code Examples

In Divi's front-end, this translates to CSS flexbox order:

```css
/* Divi internally applies this CSS */
.et_pb_column {
  display: flex;
  order: 2; /* If Order is set to 2 */
}

/* Example: Reordering three columns */
.et_pb_column:nth-child(1) {
  order: 3; /* Appears last */
}

.et_pb_column:nth-child(2) {
  order: 1; /* Appears first */
}

.et_pb_column:nth-child(3) {
  order: 2; /* Appears second */
}
```

## Common Patterns

1. **Mobile-first content reordering**: Place the most important content first on mobile by assigning lower order values, then adjust for desktop layouts using responsive settings.

2. **Navigation reordering**: Move navigation elements to different positions across breakpoints without duplicating HTML or using workarounds.

3. **Grid-like layouts**: Create multi-column grids where items visually rearrange in response to screen size changes while maintaining proper source order for accessibility.

4. **Sidebar repositioning**: Move a sidebar from the right (desktop) to below content (mobile) purely through CSS flexbox order values.

## Troubleshooting

!!! warning "Order only works within flex containers"
    The Order option has no effect on elements inside non-flex containers. Ensure the parent (Row or Section) has flexbox layout enabled. In Divi 5, most containers default to flexbox, but verify this in the parent's Layout settings.

!!! warning "Source order matters for accessibility"
    While visual order can be rearranged via CSS, screen readers follow the HTML source order. Ensure your visual reordering does not create confusing or inaccessible experiences. Use order strategically for presentation, not for critical information flow.

!!! warning "Same order values use source order as tiebreaker"
    If two elements have the same order value (e.g., both are 0), they will appear in their natural HTML order. There is no secondary sort—source order wins.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 uses a different layout system.

## Related

- [Understanding Divi 5's New Flexbox Layout](understanding-divi-s-new-flexbox-layout.md)
- [Understanding Flex Justify Content in Divi 5](understanding-flex-justify-content-in-divi-5.md)
- [Understanding Flex Align Items Options in Divi 5](understanding-flex-align-items-options-in-divi-5.md)
- [Flex Direction: Arranging Items Horizontally or Vertically](understanding-flex-direction-in-divi-5.md)
