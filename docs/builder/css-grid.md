---
title: "CSS Grid Layout System"
category: builder
tags: ["builder", "layout", "css-grid", "responsive"]
related: ["flexbox"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/collections/15495410-css-grid-layout-system"
---

# CSS Grid Layout System

Divi 5 includes a full CSS Grid layout mode that enables two-dimensional control over both rows and columns simultaneously, complementing the default Flexbox system.

## Overview

While Flexbox handles one-dimensional flow (either horizontal or vertical), CSS Grid provides two-dimensional layout control, allowing you to define both column and row structures at the same time. In Divi 5, Grid layout is available on Sections, Rows, Columns, and Module Groups as an alternative to the default Flex mode.

Grid is particularly well suited for complex, asymmetrical layouts where items need to span multiple rows or columns, or where you want precise placement of elements within a defined grid structure. For simpler linear arrangements, Flexbox remains the better choice.

To activate Grid mode, navigate to **Design Tab > Layout** and change the **Layout Style** dropdown from Flex to Grid. This reveals the full set of Grid-specific settings.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/collections/15495410-css-grid-layout-system).

## Grid vs. Flexbox

| Aspect | CSS Grid | Flexbox |
|--------|----------|---------|
| Dimensions | Two-dimensional (rows and columns simultaneously) | One-dimensional (single axis at a time) |
| Structure | You define the grid template explicitly | Content-driven flow determines layout |
| Best for | Complex asymmetrical layouts, magazine-style grids, dashboard panels | Linear arrangements, navigation bars, card rows |
| Item positioning | Precise placement via offset rules and span values | Sequential flow with alignment controls |

## Grid Structure Settings

These settings define the fundamental grid template: how many columns and rows exist, and how they are sized.

| Setting | Type | Description |
|---------|------|-------------|
| Layout Style | Dropdown | Select **Grid** to enable CSS Grid mode. Located under **Design Tab > Layout**. Available on Sections, Rows, Columns, and Module Groups. |
| Number of Columns | Input | Specifies how many columns the grid contains. Child elements are distributed across these columns. |
| Column Width | Input | Defines the width of individual grid columns. Accepts any CSS unit value (px, %, fr, auto). |
| Number of Rows | Input | Specifies how many rows the grid contains. Required when Grid Direction is set to Column. |
| Row Heights | Dropdown | Controls how grid rows adjust to their content. Options include **Auto** height (rows size to content), **Equal** height (all rows match the tallest), **Minimum** height, and **Fixed** height. |
| Collapse Empty Columns | Toggle | When enabled, empty grid columns are removed from rendering rather than occupying blank space. |

## Gap Settings

| Setting | Type | Description |
|---------|------|-------------|
| Horizontal Gap | Input (supports all unit values) | Controls the space between grid columns. Maps to the CSS `column-gap` property. |
| Vertical Gap | Input (supports all unit values) | Controls the space between grid rows. Maps to the CSS `row-gap` property. |

## Flow and Density Settings

These settings control how items are automatically placed into the grid when no explicit positioning is defined.

| Setting | Type | Description |
|---------|------|-------------|
| Grid Direction | Dropdown | Determines the auto-placement direction. **Row** (default) fills cells left to right, row by row. **Column** fills cells top to bottom, column by column. Column mode requires a Number of Rows value. |
| Grid Density | Dropdown | Controls how the auto-placement algorithm handles gaps in the grid. **Dense** (default) attempts to fill earlier empty cells with smaller items. **Auto** maintains the natural document order, which may leave gaps. |
| Grid Auto Columns | Input | Defines the size of implicitly created columns when items exceed the explicit grid boundaries. Accepts CSS unit values. |
| Grid Auto Rows | Input | Defines the size of implicitly created rows when items overflow the explicit grid. Accepts CSS unit values. |

## Alignment Settings

Grid provides four alignment controls that position items within the grid cells and distribute the grid within its container.

| Setting | Type | Description |
|---------|------|-------------|
| Justify Content | Dropdown | Distributes the grid columns within the container along the horizontal axis. Options: **Start**, **Center**, **End**, **Space Between**, **Space Around**, **Space Evenly**. |
| Align Content | Dropdown | Distributes the grid rows within the container along the vertical axis. Only takes effect when the container is taller than the grid content. Options: **Stretch** (default), **Start**, **Center**, **End**, **Space Between**, **Space Around**, **Space Evenly**. |
| Justify Items | Dropdown | Aligns item content horizontally within their individual grid cells. Options: **Stretch** (default), **Start**, **Center**, **End**. |
| Align Items | Dropdown | Aligns item content vertically within their individual grid cells. Requires the container to have a defined height or min-height. Options: **Stretch** (default), **Start**, **Center**, **End**. |

## Grid Offset Rules

Grid Offset Rules provide advanced item positioning by targeting specific child elements using `nth-child` selectors and applying custom span or placement values. This enables complex layouts where individual items occupy multiple rows or columns.

To add an offset rule, open the container settings and navigate to the Grid Offset Rules section. Each rule consists of three components:

| Setting | Type | Description |
|---------|------|-------------|
| Admin Label | Text input | An optional label to identify the offset rule in the builder interface. |
| Target Offset | Dropdown | Selects which grid item(s) the rule applies to. Predefined options include **First Item**, **Last Item**, **Even Items**, **Odd Items**, and **Every Nth Item** (3rd through 10th). A **Custom** option allows entering any valid `nth-child` expression. |
| Offset Rule | Dropdown | The CSS Grid property to apply. Options: **Column Span**, **Column Start**, **Column End**, **Row Span**, **Row Start**, **Row End**, **Grid Template Columns**. |
| Offset Value | Numeric input | The value for the selected offset rule (e.g., a span of 2 makes the item occupy two columns). |

### Custom nth-child expressions

The Custom target offset accepts standard CSS `nth-child` syntax:

| Expression | Targets |
|-----------|---------|
| `5` | The fifth item only |
| `3n` | Every third item (3, 6, 9, ...) |
| `3n+1` | Items 1, 4, 7, 10, ... |
| `-n+3` | The first three items only |
| `2n` | Even items (same as the Even preset) |

### Available offset rules explained

| Rule | CSS Property | Purpose |
|------|-------------|---------|
| Column Span | `grid-column: span N` | Makes the targeted item span across N columns. |
| Column Start | `grid-column-start` | Sets the starting column line for the targeted item. |
| Column End | `grid-column-end` | Sets the ending column line for the targeted item. |
| Row Span | `grid-row: span N` | Makes the targeted item span across N rows. |
| Row Start | `grid-row-start` | Sets the starting row line for the targeted item. |
| Row End | `grid-row-end` | Sets the ending row line for the targeted item. |
| Grid Template Columns | `grid-template-columns` | Overrides the column template for the targeted item's context. |

## Common Layout Patterns

### Featured item with spanning

Create a 3-column grid and add an offset rule targeting the **First Item** with **Column Span** set to **2**. The first item spans two columns while the remaining items fill single cells, creating a featured-item layout.

### Magazine-style grid

Use a 4-column grid with multiple offset rules: target the first item with Column Span 2 and Row Span 2 for a large hero area, then let the remaining items auto-fill into the surrounding cells. Set Grid Density to Dense so smaller items fill any gaps.

### Dashboard panel layout

Set Number of Columns to 3 and Row Heights to Equal. Use offset rules to make specific panels span 2 columns or 2 rows as needed. The equal row height ensures a clean, structured appearance.

## Code Examples

### Basic grid override via CSS

```css
/* Define a custom 3-column grid with specific track sizes */
.my-grid-row {
    display: grid !important;
    grid-template-columns: 1fr 2fr 1fr !important;
    gap: 20px !important;
}
```

### Make a specific item span the full width

```css
/* First child spans all columns */
.my-grid-row > *:first-child {
    grid-column: 1 / -1;
}
```

### Responsive grid column adjustment

```css
/* 3 columns on desktop, 2 on tablet, 1 on mobile */
.my-grid-row {
    grid-template-columns: repeat(3, 1fr) !important;
}

@media (max-width: 980px) {
    .my-grid-row {
        grid-template-columns: repeat(2, 1fr) !important;
    }
}

@media (max-width: 767px) {
    .my-grid-row {
        grid-template-columns: 1fr !important;
    }
}
```

### Named grid areas for complex layouts

```css
/* Create a named-area layout */
.my-complex-grid {
    display: grid !important;
    grid-template-columns: 1fr 1fr 1fr !important;
    grid-template-rows: auto auto !important;
    grid-template-areas:
        "hero hero sidebar"
        "content content sidebar" !important;
    gap: 20px !important;
}

.my-complex-grid > *:nth-child(1) { grid-area: hero; }
.my-complex-grid > *:nth-child(2) { grid-area: content; }
.my-complex-grid > *:nth-child(3) { grid-area: sidebar; }
```

## Related

- [Flexbox Layout System](flexbox.md)
- [Responsive Preview](responsive-preview.md)
- [Visual Builder](visual-builder.md)
