---
title: "Flexbox Layout System"
description: "Divi 5 Flexbox layout system — direction, alignment, gap, wrapping, and ordering controls for sections, rows, columns, and module groups."
category: builder
tags: ["builder", "layout", "flexbox", "responsive"]
related: ["css-grid"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/collections/13895918-flexbox-layout-system"
---

# Flexbox Layout System

Divi 5 uses CSS Flexbox as its default layout engine, giving designers native control over alignment, spacing, direction, and ordering within every container element.

!!! abstract "Quick Reference"
    **What it does:** Controls one-dimensional layout flow (horizontal or vertical) for all container elements using CSS Flexbox.
    **Where to find it:** Any element's settings → Design Tab → Layout (Layout Type: Flex).
    **Key features:**

    - Layout Direction: row, row-reverse, column, column-reverse (`flex-direction`)
    - Justify Content and Align Items for main/cross axis alignment
    - Horizontal and Vertical Gap settings (`column-gap`, `row-gap`)
    - Layout Wrapping with wrapping alignment (`flex-wrap`, `align-content`)
    - Column Class for 24-column fractional widths and Order for visual resequencing

    **ET Docs:** [Flexbox Layout System](https://help.elegantthemes.com/en/collections/13895918-flexbox-layout-system){:target="_blank"}

## Overview

Divi 5 replaces the fixed column grid of Divi 4 with a true Flexbox layout system. Every new Section, Row, Column, and Module Group defaults to Flex mode, enabling one-dimensional flow control along either the horizontal or vertical axis. This means child elements inside any container can be arranged, aligned, spaced, wrapped, and reordered using standard CSS Flexbox properties, all through the Visual Builder interface.

The Flexbox settings live under **Design Tab > Layout** for container elements. Because Flex is the default for new elements, you only need to interact with Block layout mode when working with legacy Divi 4 content that has been migrated forward.

Flexbox in Divi 5 is fully responsive. Every layout property can be configured independently per breakpoint (Desktop, Tablet, Phone), making it straightforward to rearrange content flow and alignment for different screen sizes without duplicating modules.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/collections/13895918-flexbox-layout-system).

## How Flexbox Works in Divi 5

Divi 5 maintains the **Section > Row > Column > Module** hierarchy, but each level now acts as an independent Flex container. A Section is a Flex container whose children are Rows. A Row is a Flex container whose children are Columns. A Column is a Flex container whose children are Modules or Module Groups. Module Groups themselves can also be Flex containers.

This nested structure means Flexbox properties set on a Row (such as gap, direction, or alignment) govern how its Columns are arranged, while properties set on a Column govern how its Modules are arranged. Each level can have completely different layout settings.

### Layout Type

The **Layout Type** setting determines whether a container uses Flex or Block rendering. All Flex-specific settings only appear when Layout Type is set to Flex.

| Setting | Type | Description |
|---------|------|-------------|
| Layout Type | Dropdown | Choose between **Flex** (default for new elements) and **Block** (legacy mode). When set to Flex, all flexbox layout options become available. Block mode is retained for backward compatibility with Divi 4 content. |

## Layout Direction

The Layout Direction setting maps to the CSS `flex-direction` property and determines the primary axis along which child elements flow inside the container. It is available on Sections, Rows, Columns, and Module Groups.

| Setting | Type | Description |
|---------|------|-------------|
| Layout Direction | Dropdown | Controls the directional flow of child elements. Located under **Design Tab > Layout**. |

**Available values:**

| Value | CSS Equivalent | Behavior |
|-------|---------------|----------|
| Row | `flex-direction: row` | Items flow left to right horizontally (default). |
| Row Reverse | `flex-direction: row-reverse` | Items flow right to left. Useful for right-aligned headers or RTL language layouts. |
| Column | `flex-direction: column` | Items stack top to bottom vertically. Common for mobile layouts or hero sections. |
| Column Reverse | `flex-direction: column-reverse` | Items stack bottom to top. Allows reversing visual flow on smaller devices without duplicating content. |

Layout Direction can be set independently per responsive breakpoint, so you can use Row on desktop and Column on mobile to reflow content automatically.

## Gap Settings

Gap settings control the spacing between flex items without adding margin to outer edges. They are set on the parent container element.

| Setting | Type | Description |
|---------|------|-------------|
| Horizontal Gap | Input (supports all unit values) | Controls the space between flex items along the horizontal axis. Maps to the CSS `column-gap` property. Default value is **5.5%**. Located under **Design Tab > Layout**. |
| Vertical Gap | Input (supports all unit values) | Controls the space between flex items along the vertical axis. Maps to the CSS `row-gap` property. Default value is **40px**. Located under **Design Tab > Layout**. |

Both settings accept any of Divi 5's supported unit values including pixels, percentages, em, rem, vw, and vh.

## Justify Content

Justify Content controls the distribution of child elements along the primary axis (the axis defined by Layout Direction). It is available on Sections, Rows, Columns, and Module Groups.

| Setting | Type | Description |
|---------|------|-------------|
| Justify Content | Dropdown | Aligns and distributes child elements along the main axis. When Layout Direction is Row, this controls horizontal distribution. When Layout Direction is Column, this controls vertical distribution. Located under **Design Tab > Layout**. |

**Available values:**

| Value | Behavior |
|-------|----------|
| Start | Items align to the start edge of the container (left for Row, top for Column). |
| Center | Items are centered along the main axis. |
| End | Items align to the end edge of the container (right for Row, bottom for Column). |
| Space Between | Items are evenly distributed; the first item is flush with the start, the last with the end. |
| Space Around | Items are evenly distributed with equal space around each item (half-size space on edges). |
| Space Evenly | Items are evenly distributed with exactly equal space between and around all items. |

!!! note
    For Row layouts, child items need defined widths for Justify Content to take effect. For Column layouts, the container needs a defined height (height, min-height, or max-height).

## Align Items

Align Items controls the positioning of child elements along the cross axis (perpendicular to the main axis). It is available on Sections, Rows, Columns, and Module Groups.

| Setting | Type | Description |
|---------|------|-------------|
| Align Items | Dropdown | Positions child elements along the cross axis. In a Row direction layout, this controls vertical alignment. In a Column direction layout, this controls horizontal alignment. Located under **Design Tab > Layout**. |

**Available values:**

| Value | Behavior |
|-------|----------|
| Start | Items align to the start of the cross axis (top edge in Row layouts). |
| Center | Items are centered on the cross axis. |
| End | Items align to the end of the cross axis (bottom edge in Row layouts). |
| Stretch | Items expand to fill the full cross-axis dimension of the container. This is the default value. |

## Layout Wrapping

Layout Wrapping determines whether child elements stay on a single line or wrap onto multiple lines when they exceed the container width. It is available on Sections, Rows, Columns, and Module Groups.

| Setting | Type | Description |
|---------|------|-------------|
| Layout Wrapping | Dropdown | Controls whether flex items wrap to new lines when they run out of space. Maps to the CSS `flex-wrap` property. Located under **Design Tab > Layout**. Can be configured independently per responsive breakpoint. |

**Available values:**

| Value | CSS Equivalent | Behavior |
|-------|---------------|----------|
| No Wrap | `flex-wrap: nowrap` | All items stay on a single line, even if they overflow the container. Useful for horizontal scrolling layouts. This is the default. |
| Wrap | `flex-wrap: wrap` | Items automatically move to the next line when they exceed available space. Essential for responsive layouts with multiple items. |
| Wrap Reverse | `flex-wrap: wrap-reverse` | Items wrap to new lines but in reverse order. |

## Wrapping Alignment

Wrapping Alignment becomes available when Layout Wrapping is set to Wrap or Wrap Reverse. It controls how multiple lines of wrapped items are distributed within the container along the cross axis.

| Setting | Type | Description |
|---------|------|-------------|
| Wrapping Alignment | Dropdown | Aligns multiple rows (or columns) of wrapped flex items within the container. Maps to the CSS `align-content` property. Only appears when wrapping is enabled. Located under **Design Tab > Layout**. |

**Available values:**

| Value | Behavior |
|-------|----------|
| Stretch | Wrapped lines stretch to fill all available space in the container (default). |
| Start | Wrapped lines are packed to the start of the cross axis. |
| Center | Wrapped lines are centered within the container. |
| End | Wrapped lines are packed to the end of the cross axis. |
| Space Between | First and last lines are pushed to the container edges; remaining lines are evenly spaced between them. |
| Space Around | Equal space is placed around each wrapped line, with half-size space at the edges. |
| Space Evenly | Equal space is distributed between and around all wrapped lines. |

## Column Class

The Column Class setting provides a 24-column grid system for defining column widths within Flex Rows. It is only available on Column elements.

| Setting | Type | Description |
|---------|------|-------------|
| Column Class | Dropdown | Defines the width of a column using a 24-column fractional grid system. Located under **Design Tab > Sizing**. Only available on Columns within Flex Rows. Commonly used in responsive layouts to redefine column widths at different breakpoints. |

Column Class values are expressed as fractions (e.g., 1/1 for full width, 1/2 for half, 1/3 for third, 1/4 for quarter, 1/8 for eighth). The system automatically accounts for horizontal gap (gutter) values when calculating widths.

To use Column Class effectively, **Layout Wrapping** must be enabled on the parent Row so that columns can flow to the next line when their combined widths exceed 100%.

## Column Structure

Divi 5 provides multiple ways to modify the column layout within a Row after it has been placed.

| Setting | Type | Description |
|---------|------|-------------|
| Change Column Structure | Modal selector | Accessible from the Row action icon or **Content Tab** in Row settings. Provides pre-made column structure templates to quickly reconfigure the column layout. |
| Add New Column | Action button | Inserts an additional column into the Row. For rows with 1-2 columns, the Column Class adjusts automatically. For rows with 9 or more columns, you must set the Column Class manually. |
| Duplicate Column | Action button | Creates a copy of an existing column. Requires manual Column Class adjustment via **Design Tab > Sizing**. |

## Order

The Order setting allows you to control the visual display sequence of individual items within a Flex container, independently of their position in the page builder.

| Setting | Type | Description |
|---------|------|-------------|
| Order | Numeric input | Controls the visual display position of an element within its Flex container. Lower numbers appear first. Located under **Content Tab** in the Order option group (above Admin Label). Does not change the DOM structure; only affects visual rendering. Can be set per responsive breakpoint. |

## Common Layout Patterns

### Equal-height columns
Set **Align Items** to **Stretch** on the Row (this is the default). All columns will expand to match the tallest column.

### Centered content within a column
Set **Justify Content** to **Center** and **Align Items** to **Center** on the Column. This centers modules both horizontally and vertically within the column.

### Responsive column reflow
Set **Layout Wrapping** to **Wrap** on the Row. Use **Column Class** to set columns at 1/3 width on desktop. Change Column Class to 1/2 on tablet and 1/1 on phone via responsive breakpoints so items reflow naturally.

### Reversed mobile order
Use the **Order** setting on individual modules or columns to change their visual sequence on phone breakpoints without rearranging them in the builder.

### Horizontal button group with spacing
Place multiple Button modules in a Module Group. Set **Layout Direction** to **Row**, **Horizontal Gap** to your desired spacing, and **Layout Wrapping** to **Wrap** so buttons stack on smaller screens.

## Code Examples

### Custom gap override via CSS

```css
/* Override flex gap on a specific row */
.my-custom-row {
    column-gap: 20px !important;
    row-gap: 30px !important;
}
```

### Reverse column order on mobile

```css
/* Reverse column flow on screens below 768px */
@media (max-width: 768px) {
    .my-row {
        flex-direction: column-reverse !important;
    }
}
```

### Force equal-width flex items

```css
/* Make all direct children of a row equal width */
.my-equal-row > * {
    flex: 1 1 0 !important;
}
```

### Center a single module inside a column

```css
/* Center content both axes */
.my-centered-column {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    min-height: 300px;
}
```

## Related

- [CSS Grid Layout System](css-grid.md)
- [Responsive Preview](responsive-preview.md)
- [Visual Builder](visual-builder.md)
- [Sizing Options](../options-groups/sizing.md) — Control flex item width, height, and grow/shrink behavior
- [Spacing Options](../options-groups/spacing.md) — Margin and padding that interact with flex gap
- [Playbook: Layout Patterns](../playbooks/layout-patterns.md) — Common layout recipes using flexbox
