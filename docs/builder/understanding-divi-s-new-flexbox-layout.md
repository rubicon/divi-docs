---
title: "Understanding Divi's New Flexbox Layout"
category: builder
tags: [builder, flexbox, layout, layout-system]
related: [divi-visual-builder-basics, theme-builder-guide]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11754241-understanding-divi-s-new-flexbox-layout"
---

# Understanding Divi's New Flexbox Layout

Divi 5 introduces CSS Flexbox as the default layout engine for new sections and rows, replacing the block-based grid system used in Divi 4. This fundamental shift provides more control, flexibility, and responsiveness for building dynamic layouts.

## Overview

Flexbox layout represents a major architectural change in Divi 5. While existing Divi 4 pages continue to use the Block layout, all new sections and rows default to Flex layout—a modern, CSS Flexbox-based approach that gives you precise control over spacing, alignment, and flow direction.

The Flex layout system is designed to be intuitive for both beginners and advanced builders. It maintains backward compatibility with existing pages while offering superior alignment controls, gap spacing, and responsiveness options. You can switch between Flex and Block layouts at any time, allowing you to modernize existing content without affecting legacy pages.

Key advantages of Flexbox include:
- **Precise spacing control**: Define horizontal and vertical gaps independently
- **Direction flexibility**: Arrange content left-to-right, right-to-left, top-to-bottom, or bottom-to-top
- **Advanced alignment**: Justify and align items using industry-standard Flexbox properties
- **Dynamic wrapping**: Control whether items wrap to new lines and how wrapped content aligns
- **Responsive design**: Easily adjust layouts across breakpoints without complex CSS

![Flexbox layout example](../assets/screenshots/builder/flexbox-layout/overview.png){ loading=lazy }
*Divi's Flexbox layout system provides intuitive controls for modern CSS-based design.*

## Settings & Options

### General Layout Properties

| Setting | Type | Description |
|---------|------|-------------|
| Horizontal Gap (column-gap) | Select | Controls the horizontal spacing between child elements. Values range from none to custom spacing units. |
| Vertical Gap (row-gap) | Select | Controls the vertical spacing between child elements. Values range from none to custom spacing units. |

### Layout Direction (flex-direction)

Defines how items flow inside the container.

| Setting | Option | Description |
|---------|--------|-------------|
| Layout Direction | Row | Items flow left to right (default for LTR languages). |
| | Row Reverse | Items flow right to left. Useful for RTL languages or reversed visual order. |
| | Column | Items stack top to bottom, filling available height. |
| | Column Reverse | Items stack bottom to top, reversing the visual order. |

### Content Alignment (justify-content)

Controls how items are distributed along the primary axis. Note: This setting only affects layouts where a custom height, min-height, or max-height is defined.

| Setting | Option | Description |
|---------|--------|-------------|
| Justify Content | Start | Aligns items to the left or top edge (depending on flex-direction). |
| | Center | Aligns items to the center of the container. |
| | End | Aligns items to the right or bottom edge. |
| | Space Between | Aligns the first item to the start and the last item to the end, with equal space between all items. |
| | Space Around | Adds equal space around each item; outer margins are half the size of inner gaps. |
| | Space Evenly | Keeps spacing uniform between and around all items. |

### Item Alignment (align-items)

Controls how individual items are aligned along the cross-axis.

| Setting | Option | Description |
|---------|--------|-------------|
| Align Items | Start | Aligns items to the left or top edge. |
| | Center | Aligns items to the center. |
| | End | Aligns items to the right or bottom edge. |
| | Stretch | Expands items to fill the width or height of the container. |

### Layout Wrapping (flex-wrap)

Determines whether items wrap to additional lines when the container is too narrow.

| Setting | Option | Description |
|---------|--------|-------------|
| Layout Wrapping | No Wrap | Items stay on one line and shrink to fit (default behavior). |
| | Wrap | Items move to the following line if the container isn't wide enough. |
| | Wrap Reverse | Items move to the following line in reverse order if space runs out. |

### Wrapped Content Alignment (align-content)

Controls alignment of wrapped lines along the cross-axis. Only visible when Layout Wrapping is set to Wrap or Wrap Reverse.

| Setting | Option | Description |
|---------|--------|-------------|
| Wrapping Alignment | Stretch | Expands items equally to fill the container space while respecting max-width/max-height. |
| | Start | Packs items tightly against the start edge. |
| | Center | Centers all items along the cross-axis. |
| | End | Packs items at the end of the container. |
| | Space Between | Evenly distributes items; first aligns to start, last to end. |
| | Space Around | Adds equal space around each item; outer margins are half the inner gaps. |
| | Space Evenly | Keeps equal spacing between items and container edges. |

### Column Management

| Setting | Type | Description |
|---------|------|-------------|
| Add New Column | Button | Adds a new empty column to the row with the same width class as the last column. Flex columns inherit proportional sizing from their neighbors. |
| Clone | Button | Duplicates an existing column with all its settings and contained modules intact. |

### Drag and Drop Behavior

| Action | Behavior |
|--------|----------|
| Dragging rows into Flex Sections | Default top and bottom padding is automatically removed to integrate with the Flex layout. |
| Dragging columns between layouts | Moving a column from a Block Row to a Flex Row creates equal-width columns and removes Flex classes. Moving a column from a Flex Row to a Block Row assigns it the same Column Class as the column before it. |
| Dragging modules into Flex Rows | Default bottom margin is automatically removed to prevent unexpected spacing. |

## Layout Conversion

### Block to Flex Conversion

When converting a Block layout to Flex, Divi minimizes visual changes by:
- Applying default Horizontal Column Spacing instead of converting gutter width
- Mapping Block column classes to their Flex equivalents (e.g., 1/2 Block → 1/2 Flex)
- Preserving module content and settings

**Note**: If you use custom CSS targeting Block classes, visual differences may occur after conversion.

### Flex to Block Conversion

When converting a Flex layout to Block:
- All columns reset to equal width, similar to Block layout's default behavior
- Modules in columns beyond the sixth column are moved into the sixth column
- Nested rows remain nested within their parent structure

## Migration from Divi 4

### Existing Pages

Pages created in Divi 4 continue to use the Block layout system. You can:
- Keep them as-is with no changes required
- Gradually update them by converting sections/rows to Flex
- Mix Block and Flex layouts on the same page

### Full Width and Specialty Sections

These legacy section types are fully supported in Block layouts:
- Existing Full Width and Specialty Sections continue to function normally
- You can still edit them, but they cannot be added through the Add Section panel
- Consider converting to Flex rows for new layouts

## Code Examples

### CSS Flexbox Reference

Divi's Flex layout settings translate directly to CSS Flexbox properties:

```css
/* Flex container (applied to the row/section) */
.et_pb_flex_row {
  display: flex;
  flex-direction: row; /* or column, row-reverse, column-reverse */
  flex-wrap: wrap; /* or nowrap, wrap-reverse */
  justify-content: center; /* or flex-start, flex-end, space-between, space-around, space-evenly */
  align-items: center; /* or flex-start, flex-end, stretch */
  align-content: center; /* only applies when flex-wrap is enabled */
  column-gap: var(--horizontal-gap);
  row-gap: var(--vertical-gap);
}

/* Flex child (applied to columns) */
.et_pb_column {
  flex: 1; /* Equal share of available space */
  flex-basis: 50%; /* Or specific width */
  flex-shrink: 0; /* Prevent shrinking below content size */
}
```

### Working with Flex Gaps

Use the Horizontal and Vertical Gap settings instead of padding:

```css
/* Instead of padding columns (which breaks Flex alignment) */
/* Use gap spacing on the row */
.et_pb_flex_row {
  column-gap: 2rem; /* Horizontal spacing between columns */
  row-gap: 1.5rem; /* Vertical spacing between wrapped rows */
}
```

## Common Patterns

### Equal-Width Multi-Column Layouts

Set up consistent column widths using Flex's auto-sizing:

1. Create a Flex row
2. Set Layout Direction to "Row"
3. Add multiple columns (Flex automatically distributes space equally)
4. Set Horizontal Gap to your preferred spacing
5. Columns expand/shrink together as the viewport changes

![Equal-width columns pattern](../assets/screenshots/builder/flexbox-layout/pattern-equal-columns.png){ loading=lazy }
*Flex layout automatically equalizes column widths, making responsive multi-column designs effortless.*

### Centered Content with Space Around

Create a balanced layout with centered content and surrounding space:

1. Create a Flex row with custom height
2. Set Justify Content to "Center"
3. Set Align Items to "Center"
4. Add content columns—they'll center both horizontally and vertically

This pattern is ideal for hero sections, featured content blocks, and card layouts.

### Responsive Stacking with Flex Wrapping

Allow items to wrap to new lines on smaller screens:

1. Create a Flex row
2. Set Layout Wrapping to "Wrap"
3. Use column widths appropriate for your breakpoints
4. On mobile, set Layout Direction to "Column" in the mobile settings
5. Content automatically stacks without additional CSS

## Elegant Themes tutorials

- [Building Flexible Layouts with Divi 5 Flexbox](https://www.elegantthemes.com/blog/...){:target="_blank"} — Step-by-step guide to leveraging Flex layout in real-world designs

## Version Notes

!!! note "Divi 5 Only"
    Flexbox layout is exclusive to Divi 5. Divi 4 uses the Block layout system. Pages created in Divi 4 continue to work unchanged, but new sections and rows in Divi 5 default to Flex layout.

## Troubleshooting

### Columns Not Aligning Correctly

**Symptom**: Columns appear misaligned or have unexpected spacing.

**Solution**: 
- Verify that Justify Content and Align Items settings match your intended layout
- Check that custom heights are defined if using Justify Content (required for justify-content to have effect)
- Inspect the column width settings—ensure they're compatible with your chosen layout direction

### Spacing Issues After Drag-Drop

**Symptom**: Unexpected gaps or padding appear when moving modules into Flex rows.

**Solution**:
- Remember that Divi automatically removes default module margins when dragging into Flex layouts
- Use the Horizontal and Vertical Gap settings on the row instead of padding individual columns
- If spacing is still off, check for custom CSS targeting module margins

### Layout Breaks on Mobile

**Symptom**: Flex layout doesn't stack properly on smaller screens.

**Solution**:
- Create responsive breakpoint settings for Layout Direction (set to "Column" on mobile)
- Adjust Wrapping settings and column widths at each breakpoint
- Test on actual mobile devices, not just browser resize

### Converting Block Layouts Loses Styling

**Symptom**: After converting a Block layout to Flex, colors or spacing appear incorrect.

**Solution**:
- If you use custom CSS targeting Block column classes (e.g., `.et_pb_column_1_2`), update those selectors to target Flex classes instead
- Re-apply custom styling at the row level using gap properties instead of column padding
- Consider keeping legacy Block layouts as-is and using Flex for new content

## Related

- [Divi Visual Builder Basics](../builder/visual-builder.md)
- [Theme Builder Guide](../builder/theme-builder.md)
- [Working with Sections and Rows](../modules/the-section-in-divi-5.md)
- [Module Reference](../modules/index.md)
