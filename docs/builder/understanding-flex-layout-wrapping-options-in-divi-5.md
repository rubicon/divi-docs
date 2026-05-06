---
title: "Understanding Flex Layout Wrapping Options in Divi 5"
category: builder
tags: ["builder", "flexbox", "layout", "responsive", "wrapping"]
related: ["understanding-flex-column-class-options-in-divi-5.md", "understanding-flex-justify-content-in-divi-5.md", "understanding-flex-wrapping-alignment-options-in-divi-5.md", "understanding-flex-order-option-in-divi-5.md", "responsive-options.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/11883478-understanding-flex-layout-wrapping-options-in-divi-5"
---

# Understanding Flex Layout Wrapping Options in Divi 5

Divi 5 relies on native CSS flexbox to control how child elements wrap inside flex containers. The Layout Wrapping option determines whether modules automatically move to the next line when space is limited or remain forced on a single line.

## Overview

Flex layout wrapping controls the behavior of child elements (modules) when there isn't enough horizontal space in their flex container. This is essential for creating responsive layouts that adapt gracefully to different screen sizes and content arrangements.

The Layout Wrapping option is particularly useful when building:
- Responsive button groups
- Image galleries with flexible dimensions
- Multi-column layouts that need to reflow on smaller screens
- Sliders and carousels that maintain horizontal scrolling on mobile

Without proper wrapping controls, elements may overflow their containers or create unintended layout breaks on responsive designs.

## How to Access

1. Select a **Section**, **Row**, **Column**, or **Group module**
2. Open the **Design tab**
3. Navigate to **Layout** → **Layout Wrapping**

The Layout Wrapping option is available on any element that acts as a flex container for child elements.

## Layout Wrapping Options

### Wrap
Modules automatically move to the next line when there isn't enough horizontal space. This is the default behavior for responsive layouts and is useful when:
- Building button groups that need to stack on mobile
- Creating product showcases with flexible image sizing
- Designing multi-column layouts that reflow based on screen width

### No Wrap
Forces all child modules to stay on a single line, even if they overflow the container. Use this for:
- Horizontal sliders that require manual scrolling
- Navigation bars that should remain inline
- Custom layouts where you control overflow behavior with CSS

### Wrap Reverse
Modules wrap to the next line in reverse order, with new lines appearing above previous content. This is useful for specialized layouts where visual order needs to reverse alongside the text direction.

## Common Use Cases

### Responsive Column Restructuring

Create layouts that adapt across viewport sizes by combining Layout Wrapping with column class adjustments:

**Desktop**: 8 equal columns side-by-side
**Tablet**: 4 columns per row (2 rows total)
**Phone**: 1 column (full width stack)

Steps:
1. Add a Row with 8 equal columns
2. Switch to Tablet viewport → Click the Column Structure icon → Select 4-column layout
3. Go to Design tab → Layout → Layout Wrapping → Enable **Wrap**
4. Switch to Phone viewport → Click Column Structure icon → Select 1-column layout

### Button Group Layouts

Use wrapping to create button groups that stack responsively without requiring viewport-specific edits:
- Set all buttons to a fixed width (e.g., 150px)
- Enable Layout Wrapping on the container
- Buttons automatically flow to multiple lines when needed

### Responsive Image Galleries

Build flexible image galleries where images wrap based on available space rather than fixed grid definitions:
- Set Column Class to allow flexible sizing
- Enable Layout Wrapping on the parent Row
- Images reflow naturally without media query overrides

## Technical Details

Divi 5's Layout Wrapping maps directly to the CSS flexbox `flex-wrap` property:
- **Wrap** = `flex-wrap: wrap`
- **No Wrap** = `flex-wrap: nowrap`
- **Wrap Reverse** = `flex-wrap: wrap-reverse`

The wrapping behavior works in conjunction with the **Column Class** setting, which controls element width on a 24-column grid system. Elements wrap when their combined width exceeds the container width.

## Related Settings

- **Column Class** — Define precise column widths for responsive layouts
- **Layout → Justify Content** — Control how wrapped items are distributed along the main axis
- **Layout → Align Items** — Align items vertically within their flex container
- **Layout → Gap** — Add consistent spacing between wrapped child elements

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 uses a different layout system. For migration guidance, see [How to Safely Migrate from Divi 4 to Divi 5](how-to-safely-migrate-from-divi-4-to-divi-5.md).

## Related

- [Understanding Flex Column Class Options in Divi 5](understanding-flex-column-class-options-in-divi-5.md)
- [Understanding Flex Justify Content in Divi 5](understanding-flex-justify-content-in-divi-5.md)
- [Understanding Flex Wrapping Alignment Options in Divi 5](understanding-flex-wrapping-alignment-options-in-divi-5.md)
- [Understanding Flex Order Option in Divi 5](understanding-flex-order-option-in-divi-5.md)
- [Responsive Options in Divi 5](responsive-options.md)
- [Flexbox Layout Guide](flexbox.md)
