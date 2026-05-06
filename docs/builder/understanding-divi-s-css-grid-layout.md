---
title: "Understanding Divi's CSS Grid Layout"
category: builder
tags: [builder, layout, css-grid, grid-layout, alignment]
related: [css-grid, flexbox]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12350654-understanding-divi-s-css-grid-layout"
---

# Understanding Divi's CSS Grid Layout

A comprehensive guide to Divi 5's CSS Grid layout system, covering structure, alignment, auto-placement, and advanced offset rules.

## Overview

CSS Grid is a powerful two-dimensional layout system that allows you to simultaneously control both rows and columns within a container. In Divi 5, Grid mode complements the default Flexbox system and is available for Sections, Rows, Columns, and Module Groups.

Unlike Flexbox, which handles one-dimensional flow (either horizontal or vertical), Grid provides explicit control over a defined grid structure. This makes it ideal for complex, asymmetrical layouts where items need to span multiple rows or columns, magazine-style grids, dashboard panels, or any situation requiring precise item placement.

To activate Grid mode, open any container's settings, navigate to **Design Tab > Layout**, and change the **Layout Style** dropdown from Flex to Grid. This reveals a comprehensive set of Grid-specific settings for structure, gaps, flow, alignment, and advanced offset rules.

![CSS Grid Layout panel](../assets/screenshots/builder/css-grid-layout/overview.png){ loading=lazy }
*Divi 5's CSS Grid layout system enables two-dimensional control over container structure and alignment.*

## Getting Started with CSS Grid

### Enabling Grid Layout

1. Open the settings of a Section, Row, Column, or Module Group
2. Navigate to the **Design Tab > Layout**
3. Open the **Layout Style** dropdown
4. Select **Grid** (default is Flex)

Once Grid is selected, all Grid-specific settings become available in the Layout section.

## Grid Structure Settings

These foundational settings define the grid template: how many columns and rows exist, how they are sized, and how they handle overflow content.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Number of Columns | Input | 3 | Specifies how many columns the grid contains. Child elements are distributed across these columns. |
| Column Width | Input | auto | Defines the width of individual grid columns. Accepts any CSS unit value (px, %, fr, auto, or minmax expressions). |
| Collapse Empty Columns | Toggle | Off | When enabled, empty grid columns are removed from rendering rather than occupying blank space. Useful for responsive layouts where some columns may become unused. |
| Grid Auto Columns | Input | auto | Defines the size of implicitly created columns when grid items are placed outside the explicitly defined grid boundaries. Controls the width of overflow columns that appear beyond the specified column count. |
| Number of Rows | Input | auto | Specifies how many rows the grid contains. Required when Grid Direction is set to Column. Works alongside Row Heights to define the grid's vertical structure. |
| Row Heights | Dropdown | Auto | Controls how grid rows adjust to their content. **Auto** (default): rows size to content. **Equal**: all rows match the tallest. **Minimum**: sets a baseline minimum height. **Fixed**: maintains consistent row dimensions. |
| Grid Auto Rows | Input | auto | Defines the size of implicitly created rows when grid items overflow the explicit grid. Controls the height of overflow rows that appear beyond the specified row count. |

## Gap Settings

Gaps define the space between grid columns and rows, creating breathing room between items.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Horizontal Gap | Input | 0 | Controls the space between grid columns. Maps to CSS `column-gap` property. Accepts any CSS unit value (px, em, %, rem). |
| Vertical Gap | Input | 0 | Controls the space between grid rows. Maps to CSS `row-gap` property. Accepts any CSS unit value (px, em, %, rem). |

![Grid with gaps applied](../assets/screenshots/builder/css-grid-layout/settings-gaps.png){ loading=lazy }
*Horizontal and Vertical Gap settings control spacing between grid tracks.*

## Flow and Auto-Placement Settings

These settings control how grid items automatically fill the grid when no explicit positioning is defined.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Grid Direction | Dropdown | Row | Determines the auto-placement direction for items. **Row** (default): fills cells left to right, row by row, moving to the next row when the current is full. **Column**: fills cells top to bottom, column by column, moving to the next column when the current is full. Column mode requires a Number of Rows value. |
| Grid Density | Dropdown | Dense | Controls how the auto-placement algorithm handles gaps in the grid. **Dense** (default): attempts to fill earlier empty cells with smaller items, which may reorder the visual flow compared to source order. **Auto**: maintains the natural document (source) order, which may leave gaps in the grid. |
| Grid Auto Columns | Input | auto | Defines the size of implicitly created columns beyond the explicit grid structure. Useful when you don't know how many columns you'll need, or when responsive changes may require more columns than initially specified. |
| Grid Auto Rows | Input | auto | Defines the size of implicitly created rows beyond the explicit grid structure. Useful for flexible grids that accommodate variable numbers of items. |

## Alignment Settings

Grid provides four alignment controls that position items within grid cells and distribute the entire grid within its container.

### Justify Content

Controls how grid **columns** (the entire grid's column structure) are distributed horizontally within the container.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Justify Content | Dropdown | Start | Aligns the grid's column structure along the horizontal axis. **Start** (default): flush left. **Center**: centered. **End**: flush right. **Space Between**: columns evenly spaced with no space at edges. **Space Around**: columns evenly spaced with half-size gaps at edges. **Space Evenly**: columns and all gaps (including edges) equally spaced. |

### Align Content

Controls how grid **rows** (the entire grid's row structure) are distributed vertically within the container.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Align Content | Dropdown | Stretch | Aligns the grid's row structure along the vertical axis. Only takes effect when the container is taller than the total grid content. **Stretch** (default): rows expand proportionally to fill container height. **Start**: rows pack at top. **Center**: rows center vertically. **End**: rows pack at bottom. **Space Between**: rows spread vertically with no space at edges. **Space Around**: rows spread with half-size gaps at edges. **Space Evenly**: rows and all gaps equally spaced. |

!!! note "Note"
    Align Content only takes effect when the grid container has explicit height that exceeds the total height of all rows plus gaps.

### Justify Items

Controls how **item content** is aligned horizontally within individual grid cells.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Justify Items | Dropdown | Stretch | Aligns item content along the horizontal axis within their cells. **Stretch** (default): content expands to fill cell width (unless fixed width is set). **Start**: content aligns to left edge of cell. **Center**: content centers horizontally. **End**: content aligns to right edge of cell. |

### Align Items

Controls how **item content** is aligned vertically within individual grid cells.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Align Items | Dropdown | Stretch | Aligns item content along the vertical axis within their cells. **Stretch** (default): content expands to fill cell height (unless fixed height is set). **Start**: content aligns to top edge of cell. **Center**: content centers vertically. **End**: content aligns to bottom edge of cell. |

!!! warning "Important"
    Align Items requires the grid container to have a defined height or min-height value to be visible. Without explicit container height, all items naturally expand to fill available space.

![Alignment settings](../assets/screenshots/builder/css-grid-layout/settings-alignment.png){ loading=lazy }
*Justify Content, Align Content, Justify Items, and Align Items control grid and item positioning.*

## Grid Offset Rules

Grid Offset Rules provide advanced item positioning by targeting specific child elements using `nth-child` selectors and applying custom span or placement values. This enables complex, asymmetrical layouts where individual items occupy multiple rows or columns.

### Adding an Offset Rule

Open the container settings and navigate to the **Grid Offset Rules** section. Each rule consists of three components:

| Setting | Type | Description |
|---------|------|-------------|
| Admin Label | Text Input | An optional label to identify the offset rule in the builder interface. Useful when managing multiple rules. |
| Target Offset | Dropdown | Selects which grid item(s) the rule applies to. Predefined options include **First Item**, **Last Item**, **Even Items**, **Odd Items**, and **Every Nth Item** (3rd through 10th). A **Custom** option allows entering any valid `nth-child` expression (e.g., `3n+1` for every 3rd item starting at the first). |
| Offset Rule | Dropdown | The CSS Grid property to apply. Options: **Column Span** (how many columns the item spans), **Column Start** (which column the item starts on), **Column End** (which column the item ends on), **Row Span** (how many rows the item spans), **Row Start** (which row the item starts on), **Row End** (which row the item ends on), **Grid Template Columns** (redefines the grid structure for specific items). |
| Offset Value | Numeric Input | The value for the selected offset rule (e.g., a Column Span of 2 makes the item occupy two columns). For custom nth-child expressions, provide the specific column or row number. |

### Common Offset Rule Patterns

**Example 1: Make the first item span 2 columns**
- Target Offset: First Item
- Offset Rule: Column Span
- Offset Value: 2

**Example 2: Make every 3rd item span 2 rows**
- Target Offset: Every Nth Item (3)
- Offset Rule: Row Span
- Offset Value: 2

**Example 3: Create a hero item in a masonry-style grid**
- Target Offset: First Item
- Offset Rule: Column Span
- Offset Value: 2 (and then separately Row Span: 2)

![Grid Offset Rules](../assets/screenshots/builder/css-grid-layout/offset-rules.png){ loading=lazy }
*Grid Offset Rules enable complex item positioning with nth-child targeting and custom span values.*

## Code Examples

### Basic Grid Structure

```css
/* Enable a 3-column grid with equal 20px gaps */
.et-grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

/* Make the first item span 2 columns */
.et-grid-container > :first-child {
  grid-column: span 2;
}

/* Align content to the center */
.et-grid-container {
  place-items: center;
}
```

### Advanced Grid with Auto-Flow

```css
/* Create a responsive grid that automatically wraps items */
.et-grid-responsive {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  auto-flow: dense;  /* Fill gaps with smaller items */
}
```

### Grid with Explicit Row and Column Placement

```css
/* Define explicit grid with fixed dimensions */
.et-grid-explicit {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;  /* 3 columns: narrow, wide, narrow */
  grid-template-rows: auto 200px auto;  /* 3 rows with middle row fixed height */
  gap: 15px 10px;  /* 15px vertical gap, 10px horizontal gap */
}

/* Position a specific item */
.et-grid-explicit > .hero {
  grid-column: 2;        /* Column 2 (the wide column) */
  grid-row: 2;           /* Row 2 (the fixed-height row) */
  align-self: center;    /* Center vertically in its cell */
}
```

## Common Patterns

### Magazine-Style Layout

A classic asymmetrical layout with a large featured item in the top-left and smaller items filling the remaining space.

```css
/* 4-column grid */
.et-grid-magazine {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: auto auto;
  gap: 20px;
}

/* Featured item spans 2 columns and 2 rows */
.et-grid-magazine > .featured {
  grid-column: span 2;
  grid-row: span 2;
}
```

![Magazine-style grid layout](../assets/screenshots/builder/css-grid-layout/pattern-magazine.png){ loading=lazy }
*A magazine-style layout with one large featured item and smaller surrounding items.*

### Dashboard Panel Grid

A responsive grid for dashboard-style layouts with equal-sized panels.

```css
/* 3-column equal-width grid */
.et-grid-dashboard {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
  grid-auto-rows: minmax(200px, auto);
}

/* Responsive: on smaller screens, collapse to 2 columns */
@media (max-width: 768px) {
  .et-grid-dashboard {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

![Dashboard panel grid](../assets/screenshots/builder/css-grid-layout/pattern-dashboard.png){ loading=lazy }
*Dashboard-style grid with uniform panel heights and responsive column adjustment.*

### Asymmetrical Gallery

A complex gallery where different items span different numbers of rows and columns.

```css
/* 6-column base grid */
.et-grid-gallery {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 10px;
  grid-auto-rows: 200px;
}

/* Some items span 2 columns */
.et-grid-gallery > .wide {
  grid-column: span 2;
}

/* Some items span 2 rows */
.et-grid-gallery > .tall {
  grid-row: span 2;
}

/* Some items span both */
.et-grid-gallery > .hero {
  grid-column: span 3;
  grid-row: span 2;
}
```

![Asymmetrical gallery grid](../assets/screenshots/builder/css-grid-layout/pattern-gallery.png){ loading=lazy }
*Asymmetrical gallery grid with items of varying sizes creating a complex, engaging layout.*

## Comparing Grid and Flexbox

| Aspect | CSS Grid | Flexbox |
|--------|----------|---------|
| Dimensions | Two-dimensional (rows and columns simultaneously) | One-dimensional (single axis) |
| Structure | You define the grid template explicitly | Content-driven flow determines layout |
| Best for | Complex asymmetrical layouts, precise item placement, magazine grids | Linear arrangements, navigation, card rows, flexible wrapping |
| Item positioning | Explicit placement via offset rules, spanning, and grid coordinates | Sequential flow with alignment controls |
| Container-dependent | Layout defined by container structure | Items size relative to their content |

## Tips and Best Practices

- **Grid vs. Flexbox**: Use Grid for complex, two-dimensional layouts. Use Flexbox for simpler, one-directional layouts.
- **Dense Packing**: Dense mode may reorder items visually. If source order matters, use Auto density instead.
- **Container Height**: Most vertical alignment (Align Items, Align Content) requires the container to have explicit height.
- **Offset Rules**: Use offset rules to create asymmetrical layouts without manually placing every item.
- **Responsive Grids**: Use Grid Offset Rules to adjust spanning behavior on different screen sizes, or rebuild the grid at breakpoints.
- **Auto-Flow**: Grid Auto Columns and Grid Auto Rows handle overflow items, making grids flexible when the number of items is unknown.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. CSS Grid in Divi 5 is a full implementation of the W3C CSS Grid specification with Divi-specific controls for alignment, offset rules, and auto-placement.

## Troubleshooting

### Items Not Aligning Vertically

**Cause**: Align Items requires the grid container to have a defined height or min-height.

**Solution**: Add explicit height or min-height to the container. Without it, items naturally expand to fill available vertical space.

### Grid Not Responding to Justify Content

**Cause**: Justify Content only works when there's leftover horizontal space after the grid columns are sized. If columns expand to fill 100% of container width, there's no space to justify.

**Solution**: Adjust Column Width or Number of Columns so they don't consume the full container width, creating space for Justify Content to distribute.

### Offset Rules Not Working

**Cause**: Offset Rules target specific child items using nth-child selectors. If the selector is incorrect, the rule won't match any items.

**Solution**: Double-check the Target Offset value. Use the browser's Developer Tools (Inspector) to inspect the child elements and verify their position in the DOM.

### Dense Mode Creating Unexpected Order

**Cause**: Grid Density set to Dense attempts to fill gaps by allowing items to break out of source order.

**Solution**: If source order matters, change Grid Density to Auto instead. This maintains document order but may leave gaps.

## Elegant Themes tutorials

- [Understanding CSS Grid Layout System](https://www.elegantthemes.com/blog/wordpress/css-grid-layout-system){:target="_blank"} — Comprehensive guide to CSS Grid in Divi
- [Understanding Flex Justify Content](https://www.elegantthemes.com/blog/wordpress/understand-flex-justify-content-divi){:target="_blank"} — Related alignment concepts also applicable to Grid

## Related

- [CSS Grid Layout System](css-grid.md) — Complete reference documentation
- [Flexbox Layout System](flexbox.md) — Divi's one-dimensional layout alternative
- [Understanding Flex Gaps](understanding-flex-horizontal-and-vertical-gap-in-divi-5.md) — Gap concepts apply to Grid as well
- [Theme Builder](build-custom-templates-using-the-theme-builder-in-divi-5.md) — Grid is available in Theme Builder layouts
