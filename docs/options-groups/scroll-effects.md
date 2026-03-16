---
title: "Scroll Effects Options"
category: options-groups
tags: ["options-groups", "scroll-effects", "advanced"]
related: ["position", "animation", "transform"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102792"
---

# Scroll Effects Options

The Scroll Effects options group controls how an element behaves as the user scrolls the page, enabling sticky positioning and scroll-driven visual transformations.

## Overview

Scroll Effects give you two broad capabilities: making an element stick to the viewport during scrolling, and applying motion-based transformations that animate as the element enters and exits the visible area. These settings live under the Advanced tab of every module in the Divi 5 Visual Builder.

Sticky positioning is useful for keeping important elements like navigation bars, promotional banners, or call-to-action buttons visible as the user moves through the page. You can choose whether the element sticks to the top of the viewport, the bottom, or both.

Scroll transform effects let you create parallax-style animations without writing any code. As the user scrolls, elements can move vertically or horizontally, fade in and out, scale up or down, rotate, or blur. A motion trigger setting controls the scroll position at which these effects begin, giving you fine-grained control over the timing of each animation.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102792).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Sticky Position | Dropdown | Fixes the element to the viewport while scrolling. Options are None (default), Top (sticks to the top edge), Bottom (sticks to the bottom edge), and Top and Bottom (sticks to both edges). |
| Vertical Motion | Transform toggle | Moves the element up or down based on the user's scroll position, creating a parallax-like vertical movement effect. |
| Horizontal Motion | Transform toggle | Moves the element left or right based on the user's scroll position. |
| Fade In & Out | Transform toggle | Adjusts the element's opacity as it scrolls through the viewport, making it appear or disappear gradually. |
| Scale Up & Down | Transform toggle | Resizes the element proportionally based on scroll position, growing or shrinking as the user scrolls. |
| Rotate | Transform toggle | Rotates the element around its center axis as the user scrolls through the page. |
| Blur | Transform toggle | Applies a progressive blur filter to the element based on scroll position. |
| Motion Effect Trigger | Dropdown | Determines the scroll position at which transform effects begin. Options are Top of Element, Middle of Element, and Bottom of Element. |

## Which Elements Use This

All modules in the Divi 5 Visual Builder include the Scroll Effects options group. The settings are located under the **Advanced** tab of any element's settings panel.

## Code Examples

While scroll effects are configured through the Visual Builder interface, you can complement them with custom CSS for additional control:

```css
/* Ensure smooth transitions on sticky elements */
.sticky-header {
  transition: box-shadow 0.3s ease;
}

.sticky-header.et-sticky--active {
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
}
```

```css
/* Prevent content shift when an element becomes sticky */
.sticky-wrapper {
  min-height: inherit;
}
```

## Related

- [Position Options](position.md)
- [Animation Options](animation.md)
- [Transform Options](transform.md)
