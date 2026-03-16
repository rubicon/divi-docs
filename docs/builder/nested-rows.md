---
title: "Nested Rows"
category: builder
tags: ["builder", "nested-rows", "layout", "columns", "hierarchy"]
related: ["nested-modules", "flexbox", "css-grid"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11009228"
---

# Nested Rows

Insert rows inside columns to create sub-layouts with their own column structures, adding a second level of row-based organization to your pages.

## Overview

Divi 5 introduces nested rows, allowing you to place a Row inside a Column. This creates a hierarchy of **Section > Row > Column > Nested Row > Column**, enabling more granular layout control without resorting to workarounds. Nested rows behave identically to top-level rows: they support all the same column structures, Flex and Grid layout settings, and responsive configurations.

This is particularly useful for designs that require a sub-grid within a single column, such as a sidebar with multiple content blocks arranged in their own columns, or a hero section where one column contains a complex multi-column layout.

For the official Elegant Themes documentation, see [Nested Rows](https://help.elegantthemes.com/en/articles/11009228).

## How Nested Rows Work

### Page Hierarchy

The standard Divi hierarchy extends by one level when nested rows are used:

```
Page > Section > Row > Column > Nested Row > Column > Module
```

The breadcrumb path displayed in the settings panel reflects this full hierarchy. If the path is long, it truncates to fit the available display space.

### Nesting Depth Limit

Nested rows support **one level of nesting only**. You cannot place a row inside a column that is itself inside a nested row. This constraint keeps the layout predictable and prevents performance issues from excessive nesting depth.

## Adding Nested Rows

### Method 1: Drag and Drop

Drag a row directly into a column using either the Visual Builder canvas or the [Layers View](layers-view.md). The placement works identically to how you would place a module.

### Method 2: Insert Modal

1. Click the insert (+) icon within an existing column.
2. Select the **New Row** tab in the insert modal.
3. Choose a column layout preset for the nested row.

The nested row appears as a sibling to any modules already in that column, and you can reorder it relative to those modules.

## Column Layout Options

Nested rows support all standard column structure presets:

| Structure | Description |
|-----------|-------------|
| 1 Column (1/1) | Full-width single column within the nested row |
| 2 Columns (1/2 + 1/2) | Two equal columns |
| 3 Columns (1/3 + 1/3 + 1/3) | Three equal columns |
| 4 Columns (1/4 x 4) | Four equal columns |
| 6 Columns (1/6 x 6) | Six equal columns |
| Custom | Any combination using Column Class settings |

You can also add or remove columns after creation and use **Column Class** (under **Design Tab > Sizing**) to define custom width fractions.

## Default Styling

Nested rows ship with intentional default CSS to prevent layout conflicts:

| Property | Default Value | Description |
|----------|---------------|-------------|
| Width | 100% | Nested row fills its parent column completely |
| Max-width | none | No upper width constraint applied by default |

These defaults ensure nested rows adapt to their container without inheriting restrictive sizing from the parent row.

## Responsive Behavior

Nested rows inherit Divi's standard responsive column behavior. Columns within a nested row collapse and stack according to the same breakpoint rules as top-level columns. Grid-based modules inside nested rows (such as Blog or Portfolio) also adapt: for example, a three-column masonry grid in a 1/3-width nested column will automatically switch to a single-column layout.

You can configure column widths independently per breakpoint. A common pattern is setting columns to 1/4 width on desktop and 1/2 on tablet, causing the nested row to wrap into a 2x2 grid on smaller screens.

## Layers View Display

Nested rows appear as indented entries in the Layers View, clearly showing the parent-child relationship. The full hierarchy is visible:

```
Section
  └── Row
      └── Column
          └── Row (nested)
              └── Column
                  └── Module
```

You can manage nested rows from the Layers View using all the same actions available for top-level rows: drag to reorder, right-click for context menu, and click to open settings.

## Common Patterns

### Sidebar Sub-Grid

Place a nested row inside a narrow column (e.g., 1/4 width) to create a two-column sub-layout within the sidebar area. This is useful for displaying related content blocks side by side in a space that would otherwise be a single column.

### Hero Section with Complex Layout

In a full-width hero section, use one column for a headline and another column containing a nested row with its own multi-column layout for features, stats, or testimonials.

### Footer Widget Areas

Use nested rows within footer columns to create widget-like arrangements where each footer column contains its own sub-grid of content.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 did not support placing rows inside columns.

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Nested rows are represented as block entries within the parent column's `innerBlocks` array in the `post_content` JSON. A nested row has the same `blockName` as a top-level row but appears at a deeper nesting level in the block tree.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Parse `post_content` block JSON; nested rows appear as row blocks inside column `innerBlocks` | Needs Testing | The row block contains its own `innerBlocks` array of column blocks |
| Modify | Locate the nested row block in the hierarchy and update its `attrs` or child `innerBlocks` | Needs Testing | Must preserve the parent column's other children (sibling modules) |
| Create | Insert a row block object into a column's `innerBlocks` array | Needs Testing | The row block must contain at least one column block in its own `innerBlocks` |

## Troubleshooting

!!! warning "Cannot Nest Deeper Than One Level"
    If the insert modal does not offer a Row option inside a column, check whether that column is already inside a nested row. Divi 5 enforces a single level of row nesting.

!!! warning "Column Width Issues in Nested Rows"
    If columns inside a nested row do not display at the expected width, verify that **Layout Wrapping** is set to **Wrap** on the nested row and that Column Class values are properly assigned under **Design Tab > Sizing**.

## Related

- [Nested Modules](nested-modules.md)
- [Flexbox Layout System](flexbox.md)
- [CSS Grid Layout System](css-grid.md)
- [Layers View](layers-view.md)
