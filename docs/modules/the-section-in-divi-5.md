---
title: "The Section in Divi 5"
category: modules
tags: ["modules", "section", "layout", "structure", "full-width", "containers"]
related: ["the-row-in-divi-5", "advanced-styling-using-option-group-presets-in-divi-5", "element-presets"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/9996489-the-section-in-divi-5"
---

# The Section in Divi 5

The Section is the fundamental container block in Divi 5. It is the outermost structural element that holds all other content, spanning the full width of your page and serving as the primary layout foundation.

!!! abstract "Quick Reference"
    **What it does:** Defines a full-width page container that can hold rows and modules; controls spacing, background, layout mode, and visual effects for its entire contents.
    
    **Block identifier:** `divi/section`
    
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/9996489-the-section-in-divi-5)

## Overview

The Section is the foundational structural element in Divi 5. Every page layout starts with one or more sections, which divide your page into distinct horizontal zones. Within each section, you nest rows, and within rows you place modules or other content elements.

Think of a section as a "band" across your page. It can span the full browser width, have a limited max-width container, or use a flexible grid layout to organize its child rows. Sections control the visual background, spacing, borders, animations, and responsive behavior for everything inside them.

Sections are essential for:
- Creating full-width hero areas with background images or videos
- Organizing page content into distinct visual zones
- Applying consistent spacing, colors, or effects to multiple rows at once
- Building responsive layouts that adapt across devices

![The Section in context](../assets/screenshots/modules/the-section/overview.png){ loading=lazy }
*A page divided into multiple sections, each with distinct backgrounds and spacing.*

## Section Types

### Regular Section
The standard section that spans your full page width. Contains a max-width container to constrain content and keep it readable.

### Fullwidth Section
A section with no container constraints—child content expands to 100% of the browser viewport width, ideal for edge-to-edge backgrounds or hero areas.

### Specialty Section
A section configured with grid or advanced layout controls to create more complex multi-column structures without needing explicit rows.

## Anatomy

Every section consists of:

| Component | Description |
|-----------|-------------|
| **Container** | The outer wrapper that applies background, borders, spacing, and layout rules |
| **Rows** | Child elements nested inside the section's layout (uses Flexbox or Grid) |
| **Modules** | Individual content blocks (Text, Image, Button, etc.) placed inside rows |

## Settings & Options

### Content Tab

| Setting | Description |
|---------|-------------|
| **Link** | Make the entire section clickable, directing users to another page or external URL. |
| **Background** | Set the section's background: solid color, image, video, or gradient. |
| **Loop** | Enable the loop builder to repeat the section's content for dynamic data sources (posts, custom fields, etc.). |
| **Meta** | Assign a custom label to the section for easier identification in the builder; force its visibility in the visual editor. |

### Design Tab

| Setting | Description |
|---------|-------------|
| **Layout Style** | Choose how rows inside the section are arranged: Flex (default), Grid, or Block. |
| - Flex | Child rows stack vertically and adapt to content; responsive wrapping. |
| - Grid | Child rows follow a grid template, useful for advanced multi-column designs. |
| - Block | Child rows are laid out with block-level rules. |
| **Dividers** | Add decorative top or bottom dividers (waves, curves, slanted shapes, etc.); customize color, size, and rotation. |
| **Sizing** | Set the section's width (full-width, constrained max-width), height (auto, fixed, min-height), and padding/margin. |
| **Spacing** | Control top, bottom, left, and right padding (internal spacing) and margin (external spacing). |
| **Border** | Define border width, color, style (solid, dashed, dotted), and radius for the section's edges. |
| **Box Shadow** | Add shadow effects (blur, spread, offset, color) to give the section depth. |
| **Filters** | Apply CSS filters like hue rotation, saturation, brightness, contrast, blur, opacity, and blend modes. |
| **Transform** | Apply advanced 2D/3D transforms: scale, rotate, skew, translate. Useful for creative effects and animations. |
| **Animation** | Choose entrance animations, loop animations, or exit animations with customizable timing and easing. |

### Advanced Tab

| Setting | Description |
|---------|-------------|
| **Attributes** | Add a custom CSS ID, reusable CSS classes, or custom HTML attributes. Use these for targeted styling or JavaScript interactions. |
| **CSS** | Write custom CSS code to fine-tune the section's styling beyond the UI controls. |
| **HTML Tag** | Change the semantic HTML tag (default `section`, can use `div`, `article`, `main`, etc.) for better accessibility and SEO. |
| **Conditions** | Create conditional logic to show/hide the section based on user roles, devices, custom fields, or other criteria. |
| **Interactions** | Define custom interactive behaviors: show/hide on scroll, on click, or on hover; parallax; cursor-tracking. |
| **Visibility** | Control section visibility per device (hide on mobile, tablet, or desktop). |
| **Transitions** | Set animation duration, delay, and easing to smooth the section's animations. |
| **Position** | Use CSS position (static, relative, absolute, fixed) and offset values (top, left, bottom, right, z-index) for precise placement. |
| **Scroll Effects** | Define scroll-triggered effects: parallax, fade, scale, or custom CSS-based animations during scroll. |

## Common Patterns

### Hero Section
Create a full-width hero area with a background image, overlay, heading, and call-to-action button. Set the section's layout to Flex, add a background image, and use a row inside for text alignment.

```
Section (fullwidth, background image)
  └─ Row (centered alignment)
      └─ Column
          ├─ Heading (large, white text)
          ├─ Text (subheading)
          └─ Button (CTA)
```

### Services Grid
Display a grid of service cards by setting the section's layout to Grid and nesting multiple rows with equal columns.

```
Section (layout: grid)
  └─ Row (column structure: 3 equal columns)
      ├─ Column (service card 1)
      ├─ Column (service card 2)
      └─ Column (service card 3)
```

### Alternating Content + Image
Create a pattern where text and images alternate sides on each section using rows with reverse column orders.

```
Section 1 (light background)
  └─ Row (Text Left, Image Right)

Section 2 (dark background)
  └─ Row (Image Left, Text Right – reversed)
```

## Responsive Behavior

Sections are fully responsive. Use the device toggles in the Design tab to:
- Hide/show sections on mobile, tablet, or desktop
- Adjust padding and margins per device
- Change layout style (Flex to Block on mobile for stacking)
- Resize or reposition dividers for smaller screens

## Troubleshooting

**Section height is not what I set:**
- Check if the parent layout style (Flex vs. Grid) is overriding height rules.
- Verify padding/margin is not adding extra space.
- Use `min-height` instead of `height` for more predictable behavior.

**Background image not showing:**
- Ensure the image URL is correct and publicly accessible.
- Check the background size setting (cover, contain, or custom).
- Verify opacity/overlay settings are not hiding the image.

**Dividers misaligned or not showing:**
- Dividers require both top or bottom margin/padding and a defined height.
- Check the divider color matches your design (may be invisible if same as background).
- Ensure the SVG/shape asset is loaded (may be blocked by CORS).

**Section too wide or too narrow:**
- Verify the "Layout" or "Max Width" setting in Sizing.
- Check if the parent row's alignment is forcing a different width.
- Inspect CSS for conflicting width rules in custom CSS or child theme.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 used a different section structure and settings layout.

## Related

- [The Row in Divi 5](../modules/the-row-in-divi-5.md) — Structure and settings for rows nested inside sections
- [Advanced Styling Using Option Group Presets in Divi 5](../builder/advanced-styling-using-option-group-presets-in-divi-5.md) — Save and reuse section design patterns
- [Element Presets](../builder/element-presets.md) — Create preset configurations for sections
