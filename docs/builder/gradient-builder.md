---
title: "Gradient Builder"
description: "Divi 5 Gradient Builder — create linear and radial CSS gradients with multiple color stops, repeating patterns, and background layering options."
category: builder
tags: ["builder", "gradients", "design", "backgrounds"]
related: ["visual-builder", "presets"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/gradient-builder"
---

# Gradient Builder

How to add and edit gradients throughout your Divi designs.

!!! abstract "Quick Reference"
    **What it does:** Creates CSS gradients with multiple color stops for any element’s background.
    **Where to find it:** Any element’s settings → Content Tab → Background → Gradient tab.
    **Key features:**

    - Linear and radial gradient types with configurable angle/position
    - Multiple color stops with position control (%, px, em, vw/vh)
    - Repeating gradient option for striped and ringed patterns
    - Layer gradients above background images for overlay effects

    **ET Docs:** [Gradient Builder](https://www.elegantthemes.com/documentation/divi/gradient-builder){:target="_blank"}

Gradients are a great way to add interest and depth to your webpages. They can be created with two or more colors, various levels of transparency, and combined with pattern effects to create stunning visuals for your website. Let’s take a look at how to use the Divi Gradient Builder and explore all of the options available with it.

Divi’s Gradient Builder is part of Divi’s suite of background design options. Adding a gradient to any section, row, column, or module is easy. To demonstrate how to add gradients to a section, we’ll use one ofDivi’s layout packs.

<!-- ![Gradient Builder overview](../assets/screenshots/builder/gradient-builder/overview.png){ loading=lazy }
*The Gradient Builder interface in Divi 5.* -->

## Adding a Background Gradient

To add a gradient to any section, row, column, or module:

1. Open the element's settings.
2. Navigate to the **Content** tab > **Background** option group.
3. Click the **Gradient** tab (next to Solid Color, Image, Video, and Pattern).
4. Click the **+ Add Gradient Stop** button to add your first color stop.
5. Choose a color for the stop and adjust its position along the gradient bar.
6. Add a second color stop (at minimum, two stops are needed for a gradient).
7. Adjust the gradient type, direction, and other settings described below.

## Gradient Settings Reference

| Setting | Description | Default |
|---------|-------------|---------|
| **Gradient Type** | Linear (straight line) or Radial (circular). See types below. | Linear |
| **Direction / Angle** | For linear gradients, the angle in degrees (0--360) that controls the gradient line direction. | 180 deg (top to bottom) |
| **Radial Position** | For radial gradients, the center point of the gradient (center, top left, etc.). | Center |
| **Start Position** | Where the first color stop begins, as a percentage of the element. | 0% |
| **End Position** | Where the last color stop ends, as a percentage of the element. | 100% |
| **Color Stops** | Individual colors placed at specific positions along the gradient. Each stop has a color value and a position (%). | -- |
| **Repeat** | Whether the gradient pattern repeats. See Repeating Gradients below. | Off |
| **Place Above Background Image** | Layer the gradient on top of any background image. | Off |

## Divi Gradient Builder Types

### Linear Gradients

Linear gradients transition between colors along a straight line. The **angle** setting controls the direction of the line:

| Angle | Direction |
|-------|-----------|
| 0 deg | Bottom to top |
| 90 deg | Left to right |
| 180 deg | Top to bottom (default) |
| 270 deg | Right to left |

Any angle between 0 and 360 is supported for diagonal gradients.

### Radial Gradients

Radial gradients transition outward from a central point in a circular or elliptical shape. Use the **radial position** setting to place the center of the gradient at a specific location within the element (center, top-left corner, bottom-right, etc.).

## Repeating Gradients With the Divi Gradient Builder

When the **Repeat** option is enabled, the gradient pattern tiles itself across the element. This creates striped or banded effects. The size of each band is determined by the distance between your color stops. Tighter stop spacing produces thinner, more frequent bands.

Repeating gradients work with both linear and radial types:

- **Repeating linear** produces parallel stripes.
- **Repeating radial** produces concentric rings.

## Repeating Patterns and Interesting Effects

Combine repeating gradients with Divi's **Pattern** background overlay for complex visual effects. A few techniques:

- **Diagonal stripes**: Set a repeating linear gradient at 45 degrees with two alternating color stops spaced 10--20 px apart.
- **Target circles**: Use a repeating radial gradient with sharp color transitions (e.g., transparent-to-color at the same percentage) to create concentric rings.
- **Gradient + pattern overlay**: Place a semi-transparent gradient above a pattern background to tint the pattern with a color wash.

## Divi Gradient Builder Units

Gradient stop positions can be set using several CSS length units:

| Unit | Description |
|------|-------------|
| **%** | Percentage of the element's dimension (most common). |
| **px** | Fixed pixel values. |
| **em** | Relative to the element's font size. |
| **vw / vh** | Relative to the viewport width or height. |

Percentage is the most portable unit since it scales with the element size. Use fixed pixel values when you need precise, non-scaling stop positions.

## Best Practices for Using the Divi Gradient Builder

- **Start with two stops.** Begin with a simple two-color gradient and add complexity only as needed.
- **Use global colors.** Reference global color variables in your gradient stops so site-wide color changes automatically update your gradients.
- **Mind contrast.** Ensure text placed over a gradient background has sufficient contrast at every point of the gradient, not just the start or end color.
- **Layer gradients over images.** Use the "Place Above Background Image" option to add a gradient overlay that improves text readability on photo backgrounds.
- **Save as presets.** If you create a gradient you reuse frequently, save the element as a [preset](presets.md) so you can apply the same gradient to other elements instantly.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If this feature is not visible, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.

<!-- TODO: Add feature-specific troubleshooting items -->

## Related

- [Visual Builder](visual-builder.md)
- [Presets](presets.md)
