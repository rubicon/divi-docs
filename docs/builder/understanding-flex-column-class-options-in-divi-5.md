---
title: "Understanding Flex Column Class Options in Divi 5"
category: builder
tags: ["builder", "flexbox", "layout", "columns", "responsive", "grid"]
related: ["understanding-flex-layout-wrapping-options-in-divi-5.md", "understanding-flex-justify-content-in-divi-5.md", "understanding-flex-align-items-options-in-divi-5.md", "responsive-options.md", "flexbox.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11884048-understanding-flex-column-class-options-in-divi-5"
---

# Understanding Flex Column Class Options in Divi 5

Divi 5 uses a flexible 24-column grid system to define column widths. The Column Class option allows you to specify how much space a column occupies relative to its container, enabling custom responsive layouts beyond Divi's default column structures.

## Overview

The Column Class setting determines how wide a column is on a 24-column grid. This is essential for creating custom layouts where columns need different widths than Divi's built-in row structures provide.

For example:
- **1/1** = Full width (24/24 columns)
- **1/2** = Half width (12/24 columns)
- **1/3** = One-third width (8/24 columns)
- **1/4** = One-quarter width (6/24 columns)
- **1/8** = One-eighth width (3/24 columns)

Combined with Divi 5's responsive options, Column Class enables pixel-perfect control over layout behavior across all screen sizes.

## How to Access

1. Select a **Column** in your Row
2. Open the **Design tab**
3. Navigate to **Sizing** → **Column Class**

!!! note "Columns Only"
    The Column Class option is only available on Column elements, not on Sections, Rows, or Group modules.

## Available Column Class Options

The 24-column grid supports these common fractions:

| Column Class | Width | Use Case |
|---|---|---|
| **1/1** | 100% (full width) | Single-column layouts, full-width sections |
| **1/2** | 50% (half width) | Two-column equal layouts |
| **1/3** | 33.33% (third) | Three-column equal layouts |
| **2/3** | 66.66% (two-thirds) | Asymmetrical 2-column layouts |
| **1/4** | 25% (quarter) | Four-column equal layouts |
| **3/4** | 75% (three-quarters) | Asymmetrical 4-column layouts |
| **1/5** | 20% (fifth) | Five-column equal layouts |
| **1/6** | 16.67% (sixth) | Six-column equal layouts |
| **1/8** | 12.5% (eighth) | Eight-column equal layouts |
| **Custom values** | Based on grid | Advanced fractional widths |

## Common Use Cases

### Use Case 1: Multi-Column Responsive Layout (Quick Method)

Build a responsive layout using Divi's **Change Column Structure** action:

**Desktop:** 8 equal columns
**Tablet:** 4 equal columns  
**Phone:** 1 column (full width)

Steps:
1. Add a Row and select an **8-column equal** layout
2. Switch to **Tablet viewport**
3. Click the **Change Column Structure** icon
4. Select **4-column layout**
5. Enable **Design tab** → **Layout** → **Layout Wrapping** → **Wrap**
6. Switch to **Phone viewport**
7. Click **Change Column Structure** icon
8. Select **1-column layout**

**Result:**
- Desktop: Each column has Column Class **1/8**
- Tablet: Each column has Column Class **1/4** (auto-set)
- Phone: Each column has Column Class **1/1** (auto-set)

The Column Class values are set automatically, and Layout Wrapping ensures proper reflowing.

### Use Case 2: Custom Responsive Layout (Advanced Method)

Manually control Column Class for non-standard layouts:

**Goal:** Build an 8-column layout that becomes 4-column on tablet and 1-column on phone

Steps:
1. Add a Row and select an **8-column equal layout**
2. Switch to **Tablet viewport**
3. Edit each column → **Design tab** → **Sizing** → **Column Class**
4. Select **1/4** for each column
5. Enable **Design tab** → **Layout** → **Layout Wrapping** → **Wrap**
6. Switch to **Phone viewport**
7. Edit each column → **Design tab** → **Sizing** → **Column Class**
8. Select **Fullwidth (1/1)** for each column

**Result:**
- Desktop: 8 columns side-by-side
- Tablet: 2 rows of 4 columns each
- Phone: All 8 columns stack vertically

### Use Case 3: Asymmetrical Layouts

Create layouts where columns have different widths:

Example: Sidebar layout (1/3 sidebar, 2/3 content)
- Column 1: Column Class = **1/3** (sidebar)
- Column 2: Column Class = **2/3** (main content)

Example: Featured + grid layout (1/2 featured, two 1/4 columns)
- Column 1: Column Class = **1/2** (featured image)
- Column 2: Column Class = **1/4** (item 1)
- Column 3: Column Class = **1/4** (item 2)

## Technical Details

### Grid System

Divi 5's Column Class uses a 24-column grid system:
- Each fractional unit represents columns out of 24 total
- 1/1 = 24 columns
- 1/2 = 12 columns
- 1/3 = 8 columns
- 1/4 = 6 columns
- 1/6 = 4 columns
- 1/8 = 3 columns

### Combined with Layout Wrapping

Column Class defines **width**, while **Layout Wrapping** defines **when to wrap**:
- Set Column Class to control how wide each column is
- Enable Layout Wrapping so columns move to the next line when space is limited
- Use responsive options to change Column Class at different breakpoints

### CSS Implementation

Column Class maps to CSS flexbox:
```css
/* Column with Column Class = 1/3 */
.column {
  flex-basis: 33.333%;
  flex-grow: 0;
  flex-shrink: 1;
}
```

Changing Column Class updates `flex-basis`, controlling the column's starting width.

## Related Settings

- **Layout Wrapping** — Controls when columns wrap to the next line
- **Layout → Justify Content** — Controls spacing along the main axis
- **Layout → Align Items** — Aligns columns vertically
- **Gap** — Controls spacing between columns
- **Responsive Options** — Set different Column Class values per breakpoint

## Responsive Column Class

Change Column Class at different viewport sizes:

1. Edit a column
2. Click the **responsive option indicator** next to Column Class
3. Select the breakpoint (Tablet, Phone, etc.)
4. Choose a different Column Class for that breakpoint
5. Save

Each breakpoint can have its own Column Class value, enabling fully responsive layouts without media query overrides.

## Troubleshooting

**Q: My columns aren't wrapping when expected.**
A: Enable **Design tab** → **Layout** → **Layout Wrapping** → **Wrap** on the Row. Column Class defines width, but wrapping must be enabled separately.

**Q: How do I make columns equal width?**
A: Use Divi's **Change Column Structure** action in the Row. This automatically sets equal Column Classes for all columns.

**Q: Can I use custom fractions not in the dropdown?**
A: The dropdown provides common options. For advanced layouts, custom Column Classes can be set via CSS in the Advanced tab.

**Q: Why is my layout broken on mobile?**
A: Check that you've set an appropriate Column Class for phone (usually **1/1** for stacking). Use the responsive options to set phone-specific values.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5's 24-column grid system. Divi 4 uses a different column structure. For migration guidance, see [How to Safely Migrate from Divi 4 to Divi 5](how-to-safely-migrate-from-divi-4-to-divi-5.md).

## Related

- [Understanding Flex Layout Wrapping Options in Divi 5](understanding-flex-layout-wrapping-options-in-divi-5.md)
- [Understanding Flex Justify Content in Divi 5](understanding-flex-justify-content-in-divi-5.md)
- [Understanding Flex Align Items Options in Divi 5](understanding-flex-align-items-options-in-divi-5.md)
- [Responsive Options in Divi 5](responsive-options.md)
- [Flexbox Layout Guide](flexbox.md)
