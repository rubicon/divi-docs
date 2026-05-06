---
title: "Understanding Flex Layout Direction in Divi 5"
category: builder
tags: ["builder", "flexbox", "layout", "direction", "responsive", "row", "column"]
related: ["understanding-divi-s-new-flexbox-layout.md", "understanding-flex-column-structure-changes-in-divi-5.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11767556-understanding-flex-layout-direction-in-divi-5"
---

# Understanding Flex Layout Direction in Divi 5

Flex Layout Direction controls how child elements (rows or modules) are arranged within their parent container, using CSS flexbox properties to create flexible, responsive layouts.

## Overview

Divi 5 introduced a modern flexbox-based layout system that replaces the grid-based approach of Divi 4. The Direction setting is one of the most fundamental properties—it determines whether items flow horizontally or vertically, and in which order they appear.

The four core direction values map directly to CSS `flex-direction` properties:
- **Row** (left to right) — the default, horizontal layout
- **Row Reverse** (right to left) — horizontal with reversed order
- **Column** (top to bottom) — vertical stacking
- **Column Reverse** (bottom to top) — vertical with reversed order

This flexibility makes it trivial to change your layout structure per breakpoint. For example, you might use Row on desktop and Column on mobile to stack items vertically without duplicating or hiding content.

![Flex Direction Overview](../assets/screenshots/builder/flex-layout-direction/overview.png){ loading=lazy }
*The four flex-direction options visualized: Row, Row Reverse, Column, and Column Reverse.*

## How to Access

1. Select a **Section** or **Row** in the Visual Builder
2. Open the **Design** tab
3. Locate the **Layout** group
4. Find the **Direction** dropdown (or **Flex Direction** depending on your UI version)
5. Choose from the four options below

## Options

| Value | CSS Property | Description | Use Case |
|-------|--------------|-------------|----------|
| **Row** | `flex-direction: row` | Items line up horizontally from left to right. This is the default. | Typical horizontal layouts, navigation bars, product grids on desktop |
| **Row Reverse** | `flex-direction: row-reverse` | Items line up horizontally from right to left. The first item in the HTML appears last visually. | RTL (right-to-left) languages, designer portfolios where you want visual order different from source order |
| **Column** | `flex-direction: column` | Items are stacked vertically from top to bottom. | Mobile layouts, vertical navigation menus, content stacks |
| **Column Reverse** | `flex-direction: column-reverse` | Items are stacked vertically but in reverse order, from bottom to top. | Rare, but useful for certain design patterns (e.g., chat threads, timeline reverse) |

![Layout Direction Settings](../assets/screenshots/builder/flex-layout-direction/settings.png){ loading=lazy }
*Design tab → Layout group → Direction dropdown.*

## Code Examples

Here's how these values translate to CSS in your exported theme or custom CSS:

```css
/* Row (default) */
.section-layout {
  display: flex;
  flex-direction: row;
  /* child items flow left to right */
}

/* Row Reverse */
.section-layout {
  display: flex;
  flex-direction: row-reverse;
  /* child items flow right to left, last item appears first */
}

/* Column */
.section-layout {
  display: flex;
  flex-direction: column;
  /* child items stack top to bottom */
}

/* Column Reverse */
.section-layout {
  display: flex;
  flex-direction: column-reverse;
  /* child items stack bottom to top */
}
```

## Common Patterns

1. **Responsive Navigation**  
   Set Row direction on Desktop, Column on Phone. Your menu items automatically stack on mobile without duplicating HTML or hiding elements.

2. **Product Grid to Stack**  
   Use Row for desktop product grids. Switch to Column on tablet/phone so products stack vertically for easier mobile scrolling.

3. **Two-Column Layout with Sidebar**  
   Use Row with a main content section (flex: 1) and sidebar (flex: 0 0 300px) on desktop. Switch to Column on mobile to place the sidebar below the content.

4. **RTL Language Support**  
   If designing for Arabic or Hebrew, use Row Reverse to flip the visual order without changing your HTML source.

## Troubleshooting

!!! warning "Direction setting has no effect"
    The Direction property only works when the parent element has **Display: Flex** enabled. If you're not seeing direction changes:
    1. Open the parent Section/Row Design tab
    2. Go to Layout group
    3. Verify **Display** is set to **Flex** (not Grid or Block)

!!! note "Order of items in HTML vs. Visual"
    Row Reverse and Column Reverse change only the *visual* order, not the DOM order. This is important for accessibility—screen readers will still read items in source order. For critical changes to element order, modify the HTML source or use JavaScript.

!!! tip "Combine with Justify Content and Align Items"
    Direction controls flow direction, but pair it with:
    - **Justify Content** (main axis alignment: flex-start, center, space-between, etc.)
    - **Align Items** (cross-axis alignment: flex-start, center, stretch, etc.)  
    Together, these give you complete control over item placement.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 used a grid-based layout system without native flexbox direction support.

## Related

- [Understanding Divi's New Flexbox Layout](understanding-divi-s-new-flexbox-layout.md)
- [Understanding Flex Column Structure Changes in Divi 5](understanding-flex-column-structure-changes-in-divi-5.md)
- [Responsive Editor in Divi 5 Visual Builder](responsive-editor-in-divi-5-visual-builder.md)
