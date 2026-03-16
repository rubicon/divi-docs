---
title: "Border Options"
description: "Divi 5 Border options group — border width, color, style, rounded corners, and per-side controls for all modules and structural elements."
category: options-groups
tags: ["options-groups", "border", "design", "styling"]
related: ["box-shadow", "filters"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102574"
---

# Border Options

The Border options group lets you add and customize borders and rounded corners on any Divi 5 element.

!!! abstract "Quick Reference"
    **What it controls:** Border width, color, style, per-side application, and rounded corner radius
    **Where to find it:** Design Tab → Border
    **Available on:** All modules, sections, rows, and columns
    **Responsive:** Yes — border and radius values can be configured per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102574)

## Overview

The Border options group provides controls for applying decorative borders around elements and rounding their corners. You can apply a border uniformly to all four sides or target individual sides independently, giving you fine-grained control over the visual framing of your content.

These settings are located in the Design tab of any element's settings panel under the Border group. The border controls include width, color, and style properties, while the rounded corners control lets you adjust the border-radius of each corner individually or uniformly using a link toggle.

Borders are a fundamental design tool for creating visual separation between elements, highlighting important content areas, and adding structure to your layouts. Combined with the rounded corners setting, you can achieve everything from sharp rectangular outlines to fully circular or pill-shaped containers.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102574).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Rounded Corners | Range slider with link toggle | Adjusts the border-radius of the element's corners. Use the link toggle to set all corners uniformly or unlock it to control each corner independently. |
| Border Width | Range slider / text input | Sets the thickness of the border in pixels. A minimum of 1px is required for the border to be visible. |
| Border Color | Color picker | Selects the border color from the site palette or a custom color picker. |
| Border Style | Dropdown select | Chooses the visual style of the border line. Options include Solid, Dashed, Dotted, Double, Groove, Ridge, Inset, Outset, and None. |
| Border Sides | Checkbox group | Determines which sides of the element receive the border. You can apply borders to all sides or select individual sides (top, right, bottom, left). |

## Which Elements Use This

The Border options group is available on all Divi 5 modules and structural elements including sections, rows, and columns. Any element that renders a visible box on the page can have borders applied through this options group.

## Code Examples

Apply a bottom border only for an underline effect:

```css
.my-module {
  border-bottom: 2px solid #333333;
  border-radius: 0;
}
```

Create a card-style container with rounded corners:

```css
.card-module {
  border: 1px solid #e0e0e0;
  border-radius: 12px;
}
```

Apply different border styles to each side:

```css
.accent-module {
  border-top: 4px solid #2ea3f2;
  border-bottom: 1px dashed #cccccc;
  border-left: none;
  border-right: none;
}
```

## Related

- [Box Shadow Options](box-shadow.md)
- [Filters Options](filters.md)
- [Background Options](background.md) — Backgrounds interact with border-radius for rounded corners
- [Image Module](../modules/image.md) — Images commonly use border radius and border styles
- [Button Module](../modules/button.md) — Buttons rely on border settings for shape and hover effects
