---
title: "Understanding Flex Column Structure Changes in Divi 5"
category: builder
tags: ["builder", "flexbox", "columns", "layout", "responsive", "structure"]
related: ["understanding-flex-layout-direction-in-divi-5.md", "understanding-divi-s-new-flexbox-layout.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11892376-understanding-flex-column-structure-changes-in-divi-5"
---

# Understanding Flex Column Structure Changes in Divi 5

Column Structure in Divi 5 has been completely redesigned to leverage the new flexbox layout system, making it easier to create multi-column layouts and adjust column widths on the fly.

## Overview

In Divi 4, changing the number of columns in a row was a destructive operation—you had to delete or create new modules and manually adjust settings. Divi 5 introduces a dynamic Column Structure editor that lets you:

- Add or remove columns without losing existing modules
- Set individual column widths using intuitive Column Class values (1/12 to 12/12)
- Adjust column counts per breakpoint for responsive layouts
- Duplicate columns to speed up setup
- Visually preview your column configuration in real-time

The Column Structure panel is accessed directly from the Row's **Content** tab, making it a core part of layout design rather than a hidden setting.

![Column Structure Interface](../assets/screenshots/builder/flex-column-structure/overview.png){ loading=lazy }
*The Column Structure dialog showing a 3-column layout with individual column width controls.*

## How to Access

1. Select a **Row** in the Visual Builder
2. Open the **Content** tab (not Design)
3. Look for the **Change Column Structure** button or icon
4. Click to open the Column Structure panel
5. Adjust the number of columns and their widths as needed

## Managing Column Structure

### Add Columns

- Click the **+ Add New Column** button in the Column Structure panel
- The new column inherits default width (1/12 if no preset is selected)
- Existing modules remain intact; the new column is empty

### Remove Columns

- Click the **Trash** icon next to any column in the Column Structure panel
- Modules in that column are deleted—confirm the action
- Other columns and their modules are not affected

### Change Column Count

Use the **Column Structure presets** (1, 2, 3, 4, 6, or 12 columns) to quickly set up common layouts:

| Preset | Columns | Typical Use |
|--------|---------|------------|
| 1 | 1 | Full-width single column |
| 2 | 2 | Two-column layout (sidebar + content) |
| 3 | 3 | Three-column grid |
| 4 | 4 | Four-column card grid |
| 6 | 6 | Narrow six-column (uncommon) |
| 12 | 12 | Max granularity (rarely used) |

When you switch from one preset to another:
- If the new structure has *more* columns, click **+ Add New Column** to add the remaining columns
- If the new structure has *fewer* columns, click **Trash** to remove the extras

### Set Individual Column Widths

Each column can be assigned a **Column Class** value that determines its width:

| Class | Width | Notes |
|-------|-------|-------|
| 1 | 8.33% (1/12) | Narrow column |
| 2 | 16.67% (2/12) | — |
| 3 | 25% (3/12) | Quarter width |
| 4 | 33.33% (4/12) | Third width |
| 5 | 41.67% (5/12) | — |
| 6 | 50% (6/12) | Half width |
| 7 | 58.33% (7/12) | — |
| 8 | 66.67% (8/12) | Two-thirds width |
| 9 | 75% (9/12) | Three-quarter width |
| 10 | 83.33% (10/12) | — |
| 11 | 91.67% (11/12) | Nearly full width |
| 12 | 100% | Full width |

To set a custom width manually:
1. Select a column in the Column Structure panel
2. Go to the **Design** tab
3. Under **Sizing**, find the **Column Class** option
4. Enter a custom class name or use the dropdown to select a preset

### Duplicate Columns

- Click the **Duplicate** icon next to any column
- A new column is created with the same width and any shared settings
- Modules are *not* duplicated—the new column is empty

![Column Structure Controls](../assets/screenshots/builder/flex-column-structure/controls.png){ loading=lazy }
*Column Structure panel showing add, remove, and duplicate controls.*

## Responsive Column Structure

You can set different column structures per breakpoint:

1. Select a Row and open the **Content** tab
2. Use the **Responsive Editor** button (if available) or switch to a different device breakpoint via the top toolbar
3. Click **Change Column Structure** again
4. Set a different number of columns for that breakpoint
5. Save

For example:
- **Desktop**: 3 columns
- **Tablet**: 2 columns
- **Phone**: 1 column

This creates a fully responsive layout without duplicating content.

## Code Examples

Here's how Column Class translates to CSS flex basis:

```css
/* Example: 3-column layout with equal widths */
.et_pb_row {
  display: flex;
  flex-wrap: wrap;
  gap: 30px; /* Spacing between columns */
}

.et_pb_column.et_pb_column_4 {
  /* Column Class "4" = 33.33% width */
  flex: 0 0 calc(33.33% - 20px);
}

/* Example: 2-column layout with sidebar */
.et_pb_column.et_pb_column_8 {
  /* Main content: 66.67% */
  flex: 0 0 calc(66.67% - 20px);
}

.et_pb_column.et_pb_column_4 {
  /* Sidebar: 33.33% */
  flex: 0 0 calc(33.33% - 20px);
}
```

## Common Patterns

1. **Responsive Grid**  
   Desktop: 3 columns → Tablet: 2 columns → Phone: 1 column. Use equal Column Class values (4, 6, 12 respectively) for automatic equal widths.

2. **Sidebar Layout**  
   Desktop: Column 1 = 8 (66.67% main), Column 2 = 4 (33.33% sidebar). On phone, switch to 2 equal columns or 1 full-width.

3. **Feature Comparison**  
   Create a 4-column layout on desktop (each 3 wide) for a feature comparison table. Collapse to 2 columns on tablet, 1 on phone.

4. **Card Grid**  
   Desktop: 4 columns (3 wide each) for card grids. Tablet: 2 columns (6 wide each). Phone: 1 column (12 wide).

## Troubleshooting

!!! warning "Columns appear stacked instead of side-by-side"
    Check the Row's **Display** setting in the Design tab. It should be set to **Flex**. If set to Block or Grid, columns will stack vertically regardless of Column Class.

!!! warning "Column widths don't match my settings"
    1. Verify the Column Class values are correct (go to Design tab → Sizing → Column Class)
    2. Check for conflicting CSS in your theme's custom CSS file
    3. Clear your browser cache and rebuild in WordPress (Divi Dashboard → Cache → Clear Cache)

!!! note "Adding many columns (9+)"
    While technically possible, column structures with 9 or more columns require manual Column Class adjustments. The preset buttons max out at 6 or 12 columns. For a custom 5-column layout, use the preset to add 6 columns, then manually adjust widths (e.g., 2.4 width each, or custom CSS).

!!! tip "Duplicate columns to speed up setup"
    Instead of manually creating and sizing columns, create one column with the exact width you want, then click Duplicate to create copies. All duplicates inherit the parent's Column Class.

## Version Notes

!!! note "Divi 5 Only"
    Column Structure in Divi 5 is fundamentally different from Divi 4's approach. Divi 4 used a fixed column grid (1, 2, 3, or 4 columns), while Divi 5 offers unlimited flexibility with custom Column Class values.

## Related

- [Understanding Flex Layout Direction in Divi 5](understanding-flex-layout-direction-in-divi-5.md)
- [Understanding Divi's New Flexbox Layout](understanding-divi-s-new-flexbox-layout.md)
- [Responsive Editor in Divi 5 Visual Builder](responsive-editor-in-divi-5-visual-builder.md)
