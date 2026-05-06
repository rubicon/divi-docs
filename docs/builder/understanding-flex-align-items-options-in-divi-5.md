---
title: "Understanding Flex Align Items Options in Divi 5"
category: builder
tags: ["builder", "flexbox", "layout", "align-items", "vertical-alignment"]
related: ["understanding-divi-s-new-flexbox-layout.md", "understanding-flex-justify-content-in-divi-5.md", "understanding-flex-order-option-in-divi-5.md", "understanding-flex-direction-in-divi-5.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11882896-understanding-flex-align-items-options-in-divi-5"
---

# Understanding Flex Align Items Options in Divi 5

The Align Items setting controls how child elements align along the cross axis (vertically in a row, horizontally in a column) within a flex container.

## Overview

In Divi 5's flexbox system, **Align Items** determines the vertical (or cross-axis) alignment of flex items. This is different from **Justify Content**, which aligns items along the main axis (typically horizontal).

**Align Items** is particularly useful for:
- Vertically centering content within rows or columns
- Creating consistent alignment of elements of different heights
- Stretching items to fill the height of their parent container
- Aligning elements to the top, middle, or bottom of their flex container

When you set Align Items on a Row or Column, all child elements within that container will align according to the chosen option. This works independently of element heights, making it ideal for creating balanced layouts without manual sizing.

## Settings & Options

### How to Access

1. Select a **Row** or **Column** (the flex container)
2. Go to the **Design tab** → **Layout** section
3. Find the **Align Items** setting
4. Choose from the available alignment options

### Align Items Options

| Option | Description |
|--------|-------------|
| **Flex Start** | Aligns items to the start of the cross axis (top of a row, left of a column) |
| **Center** | Centers items on the cross axis |
| **Flex End** | Aligns items to the end of the cross axis (bottom of a row, right of a column) |
| **Stretch** | Stretches items to fill the full height/width of the container (default in many cases) |
| **Baseline** | Aligns items along their text baseline |

### Visual Examples

**Flex Start (Top Alignment)**
```
┌─────────────────────┐
│ Item1  Item2  Item3 │
│                     │
└─────────────────────┘
```

**Center (Vertical Center)**
```
┌─────────────────────┐
│                     │
│ Item1  Item2  Item3 │
│                     │
└─────────────────────┘
```

**Flex End (Bottom Alignment)**
```
┌─────────────────────┐
│                     │
│ Item1  Item2  Item3 │
└─────────────────────┘
```

**Stretch (Full Height)**
```
┌─────────────────────┐
│ Item1 │ Item2 │Item3│
│       │       │     │
└─────────────────────┘
```

## Code Examples

Align Items translates to the CSS flexbox property:

```css
/* Center alignment (most common use case) */
.et_pb_row {
  display: flex;
  align-items: center;
}

/* Align to top */
.et_pb_row {
  display: flex;
  align-items: flex-start;
}

/* Align to bottom */
.et_pb_row {
  display: flex;
  align-items: flex-end;
}

/* Stretch to fill height */
.et_pb_row {
  display: flex;
  align-items: stretch;
}
```

## Common Patterns

1. **Centered vertical alignment**: Use **Center** to vertically center all columns in a row, regardless of their individual heights. This creates a polished, balanced appearance without manual height adjustments.

2. **Hero section alignment**: Combine Align Items: Center with Justify Content: Center to create a perfect center-aligned hero section or call-to-action area.

3. **Mixed-height columns**: When columns contain different amounts of content, Align Items: Stretch ensures all columns extend to the same height, creating a uniform container appearance.

4. **Top-aligned content**: Use Align Items: Flex Start to align content to the top of a row, useful for headers or navigation elements.

## Troubleshooting

!!! warning "Align Items only works in flex containers"
    This setting only affects child elements within a flex-enabled Row or Column. Ensure the parent container has flexbox layout enabled in its Layout settings.

!!! warning "Stretch may be limited by content width"
    When using Align Items: Stretch on columns, ensure child elements don't have fixed heights that prevent stretching. Remove any explicit height constraints on modules if you want full stretching behavior.

!!! warning "Different from text alignment"
    Align Items aligns the entire element/module within its space. To align text or content *within* a module, use text alignment settings on the module itself, not Align Items on the row.

!!! warning "Horizontal Gap with Center alignment"
    If spacing between columns looks uneven when using Align Items: Center, check the Horizontal Gap setting in the Layout section. Set it to 0 if you want no spacing, or adjust to your preferred value.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 uses a different layout engine.

## Related

- [Understanding Divi 5's New Flexbox Layout](understanding-divi-s-new-flexbox-layout.md)
- [Understanding Flex Justify Content in Divi 5](understanding-flex-justify-content-in-divi-5.md)
- [Understanding Flex Order Option in Divi 5](understanding-flex-order-option-in-divi-5.md)
- [Understanding Flex Direction in Divi 5](understanding-flex-layout-direction-in-divi-5.md)
