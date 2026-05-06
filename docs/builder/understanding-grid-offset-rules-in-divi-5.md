---
title: "Understanding Grid Offset Rules in Divi 5"
category: builder
tags: [builder, grid, layout, offset, css-grid]
related: [grid-module, responsive-design]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12352639-understanding-grid-offset-rules-in-divi-5"
---

# Understanding Grid Offset Rules in Divi 5

Grid offset rules are powerful CSS Grid targeting options that let you position and resize specific grid items based on their position in the grid — without modifying the HTML structure.

## Overview

Grid offset rules allow you to apply CSS Grid properties (column span, row span, column positioning, etc.) to grid items that match specific selection criteria. Instead of creating multiple custom classes or duplicating modules, you can use CSS Grid selectors like "every third item," "odd items," or custom nth-child expressions to apply layout rules dynamically.

This is especially useful for:

- Creating staggered or alternating layouts without extra markup
- Building responsive grids that adapt item sizes based on position
- Applying special styling to the first/last items in a grid
- Creating pattern-based layouts (masonry-like effects, hero item placements, etc.)

Grid offset rules are defined in the grid module's **Design tab → Layout section**, and are only available when the Layout Style is set to **Grid**.

![Grid offset rules in the Visual Builder](../assets/screenshots/builder/grid-offset-rules/overview.png){ loading=lazy }
*Grid offset rules panel showing the Target Offset selector and offset rule options.*

## Settings & Options

Grid offset rules are configured through the grid module's Design tab. Click **+ Add Grid Offset Rule** to create a new rule.

### Offset Rule Configuration

| Setting | Type | Description |
|---------|------|-------------|
| Admin Label | Text (optional) | A custom label to identify the offset rule in the Visual Builder. Useful when you have multiple rules. |
| Target Offset | Select | The selection criteria for which grid items this rule applies to. See target options below. |
| Offset Rule | Select | The CSS Grid property to apply (Column Span, Column Start, Column End, Row Span, Row Start, Row End, or Grid Template Columns). |
| Offset Value | Number | The numeric value for the offset rule (column count, row count, column number, etc.). Behavior depends on the Offset Rule selected. |

### Target Offset Options

Select which grid items the rule applies to:

| Target | Applies To |
|--------|-----------|
| First Item | The first item only (position 1) |
| Last Item | The last item only |
| Even Items | All even-positioned items (2, 4, 6, 8, ...) |
| Odd Items | All odd-positioned items (1, 3, 5, 7, ...) |
| Every Third Item | Items at positions 3, 6, 9, 12, ... (multiples of 3) |
| Every Fourth Item | Items at positions 4, 8, 12, 16, ... (multiples of 4) |
| Every Fifth Item | Items at positions 5, 10, 15, 20, ... (multiples of 5) |
| Every Sixth Item | Items at positions 6, 12, 18, 24, ... (multiples of 6) |
| Every Seventh Item | Items at positions 7, 14, 21, 28, ... (multiples of 7) |
| Every Eighth Item | Items at positions 8, 16, 24, 32, ... (multiples of 8) |
| Every Ninth Item | Items at positions 9, 18, 27, 36, ... (multiples of 9) |
| Every Tenth Item | Items at positions 10, 20, 30, 40, ... (multiples of 10) |
| Custom nth-child Rule | A custom CSS nth-child selector expression |

### Offset Rule Types

Once you've selected your target, choose which CSS Grid property to apply:

| Offset Rule | Behavior | Value Example |
|-------------|----------|---|
| Column Span | The selected item(s) span across multiple columns | `2` = 2-column span, `3` = 3-column span |
| Column Start | The selected item(s) start at a specific column number | `1` = start at column 1, `3` = start at column 3 |
| Column End | The selected item(s) end at a specific column number | `3` = end at column 3, `5` = end at column 5 |
| Row Span | The selected item(s) span across multiple rows | `2` = 2-row span, `3` = 3-row span |
| Row Start | The selected item(s) start at a specific row number | `1` = start at row 1, `2` = start at row 2 |
| Row End | The selected item(s) end at a specific row number | `2` = end at row 2, `3` = end at row 3 |
| Grid Template Columns | Redefine the grid column structure for the grid | `repeat(3, 1fr)` = 3 equal columns, `1fr 2fr 1fr` = variable widths |

### Custom nth-child Rule Examples

When you select "Custom nth-child Rule," you can enter any valid CSS nth-child selector:

| Expression | Selects |
|------------|---------|
| `5` | The 5th item only |
| `3n` | Every 3rd item (3, 6, 9, 12, ...) |
| `3n+1` | Items 1, 4, 7, 10, 13, ... |
| `3n+2` | Items 2, 5, 8, 11, 14, ... |
| `-n+3` | The first 3 items (1, 2, 3) |
| `odd` | All odd items (1, 3, 5, 7, ...) |
| `even` | All even items (2, 4, 6, 8, ...) |
| `n+4` | Items 4 and beyond |

![Offset rule settings panel](../assets/screenshots/builder/grid-offset-rules/settings-design.png){ loading=lazy }
*Grid offset rule configuration showing target selection and offset rule options.*

## Common Patterns

### Alternating Column Span

Create visual interest by making every other item wider:

1. Create a grid with 3 columns
2. Add Grid Offset Rule #1:
   - Target: Odd Items
   - Offset Rule: Column Span
   - Value: 1
3. Add Grid Offset Rule #2:
   - Target: Even Items
   - Offset Rule: Column Span
   - Value: 2

Result: Items 1, 3, 5 are 1 column wide. Items 2, 4, 6 span 2 columns.

![Alternating column span pattern](../assets/screenshots/builder/grid-offset-rules/pattern-alternating-span.png){ loading=lazy }
*Grid with alternating 1-column and 2-column items.*

### Hero Item Layout

Highlight the first item in a grid by making it span multiple rows and columns:

1. Create a grid with 3 columns
2. Add Grid Offset Rule:
   - Target: First Item
   - Offset Rule: Column Span
   - Value: 2
3. Add another Grid Offset Rule:
   - Target: First Item
   - Offset Rule: Row Span
   - Value: 2

Result: First item spans 2 columns and 2 rows, creating a featured "hero" effect.

![Hero item with 2x2 span](../assets/screenshots/builder/grid-offset-rules/pattern-hero-item.png){ loading=lazy }
*First item displayed as a 2x2 hero at the start of the grid.*

### Every Nth Item Offset

Create a repeating pattern where every 4th item has different positioning:

1. Create a grid with 3 columns
2. Add Grid Offset Rule:
   - Target: Every Fourth Item
   - Offset Rule: Column Start
   - Value: 2

Result: Items 4, 8, 12 start at column 2, while others start at column 1.

![Every fourth item offset pattern](../assets/screenshots/builder/grid-offset-rules/pattern-every-n.png){ loading=lazy }
*Grid showing every 4th item offset to column 2.*

## Tips & Best Practices

- **Overlap awareness:** CSS Grid can allow items to overlap. If multiple offset rules target the same items, ensure they don't create unintended overlaps.
- **Responsive rules:** Grid offset rules respect the grid's responsive behavior. If your grid changes column count on mobile, offset rules still apply based on item position.
- **Admin labels:** Use descriptive Admin Labels when you have multiple offset rules to make future maintenance easier.
- **Custom nth-child complexity:** While custom nth-child selectors are powerful, overly complex expressions can be hard to debug. Document your logic in the Admin Label.
- **Visual Builder preview:** Always preview your grid in the Visual Builder to verify that offset rules create the desired layout.

## Version Notes

!!! note "Divi 5 Only"
    Grid offset rules are a Divi 5 feature. This page documents Divi 5 behavior exclusively.

## Related

- [Grid Module](../builder/understanding-divi-s-css-grid-layout.md)
- [Understanding Grid in Divi 5](../builder/understanding-divi-s-css-grid-layout.md)
- [Responsive Design with Grid](../builder/responsive-editor-in-divi-5-visual-builder.md)
- [CSS Grid Selectors Reference](../builder/understanding-grid-offset-rules-in-divi-5.md)
