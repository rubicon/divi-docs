---
title: "Variable Generator in Divi 5"
category: builder
tags: [variable, generator, in, divi, 5]
related: []
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14851749-variable-generator-in-divi-5"
---

# Variable Generator in Divi 5

The Variable Generator in Divi 5 lets you build a complete sizing system and a complete color palette automatically, without writing a single line of CSS.

## Overview

You launch it from the **[Variable Manager](https://help.elegantthemes.com/en/articles/13348842-global-variables-in-divi-5)** inside the Visual Builder, choose what you want to generate, and Divi creates a set of reusable Global Variables that update everywhere on your site.

This article explains what the Variable Generator does, where to find it, and how to use both of its modes: the **Color Palette Generator** for building a **[relative color system](https://help.elegantthemes.com/en/articles/11631084-relative-colors-hsl-in-divi-5)**, and the **Fluid Sizing Variable Generator** for building responsive sizing scales like font sizes, spacing, gaps, and more.

[Screenshot: Variable Manager open in the Visual Builder with both generator buttons visible.]

## Settings & Options

## What the Variable Generator Does

Most design systems share two foundations: a set of brand colors that work together, and a set of sizing values (font sizes, spacing, radius, etc.) that scale consistently across screen sizes. Building those by hand takes time, and getting the math right (especially for fluid typography) requires an advanced understanding of how `clamp` math function works.

The Variable Generator does that work for you. It produces:

- **A relative color palette** built from a primary color, with light-to-dark shades and transparent variants that all update together when you adjust the primary.
- **A fluid sizing scale** built with `clamp()`, so values smoothly resize between a minimum and maximum as the viewport (the visible width of the browser) changes.
- **A fixed responsive scale** that outputs separate values per breakpoint (Phone, Tablet, Desktop, etc.).
- **A fixed single scale** that outputs one value across all screen sizes.

Whichever you generate, the output becomes a set of Global Variables in the **Variable Manager**. From there, every variable plugs straight into your design system. To learn more about how variables work, read **[Global Variables in Divi 5](https://help.elegantthemes.com/en/articles/13348842-global-variables-in-divi-5)**.

## Where to Find the Variable Generator

[![](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340116077/720109de1488582ed8a74a354677/+var-generator-2.png?expires=1778077800&signature=08f72941459760a321885f25802bbd1a7f34e3d8dd603545ca840d6323c55261&req=diMjFsh%2Fm4FYXvMW1HO4zVImD0XGZnxiaWiAhO6%2Bp6%2FgGfxzbhxysArhy7b3%0AvzlB3bFDxZa2dK3tHWo%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340116077/720109de1488582ed8a74a354677/+var-generator-2.png?expires=1778077800&signature=08f72941459760a321885f25802bbd1a7f34e3d8dd603545ca840d6323c55261&req=diMjFsh%2Fm4FYXvMW1HO4zVImD0XGZnxiaWiAhO6%2Bp6%2FgGfxzbhxysArhy7b3%0AvzlB3bFDxZa2dK3tHWo%3D%0A)

The Variable Generator lives inside the **[Variable Manager](https://help.elegantthemes.com/en/articles/13348842-global-variables-in-divi-5)**.

1. Open any page in the **Visual Builder**.
2. In the left sidebar, click the **Variable Manager**![](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340013742/1631740d10ef17bde0fb2aebb563/global-variable.png?expires=1778166000&signature=d7314a97ede7abb729954e986fb5cf00cc24bd2dd8b223ecbdd17e2b9c50ddec&req=diMjFsl%2FnoZbW%2FMW3Hu4gXl6HyuvZ7wtAysENWy479BtU2vwY7IL5uvKTutS%0ApA%3D%3D%0A)icon.
3. Hover over the **Colors** group to reveal the **Generate Color Palette Variables** button, or hover over the **Numbers** group to reveal the **Generate Fluid Sizing Variables** button.
4. Click the button for the generator you want to use.

The generator opens in a full-screen modal with a configuration sidebar on the left and a live preview area on the right.

## Using the Color Palette Generator

[![](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340043039/e9d591c8fd5f91c96f7df6766ab4/215_add-color-palette-generator.gif?expires=1778077800&signature=d3863ed9ae8ccf9d1f8a3907b2e878fabd9527a3a7d637918bb4f1be87ff6175&req=diMjFsl6noFcUPMW1HO4zb%2Fyw10qniP%2BF0rZguBwlAu%2Ba%2BE1mNb0D7NqpF6B%0ANp%2B3K9x1CHjyOKF2B98%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340043039/e9d591c8fd5f91c96f7df6766ab4/215_add-color-palette-generator.gif?expires=1778077800&signature=d3863ed9ae8ccf9d1f8a3907b2e878fabd9527a3a7d637918bb4f1be87ff6175&req=diMjFsl6noFcUPMW1HO4zb%2Fyw10qniP%2BF0rZguBwlAu%2Ba%2BE1mNb0D7NqpF6B%0ANp%2B3K9x1CHjyOKF2B98%3D%0A)

The Color Palette Generator builds a complete color system from a single primary color. It uses Divi's relative color system (a way of defining colors as variations of another color using HSL math) to create shades that stay mathematically linked. To learn more about the underlying color system, read **[Relative Colors & HSL in Divi 5](https://help.elegantthemes.com/en/articles/11631084-relative-colors-hsl-in-divi-5)**.

## Generate a Color Palette

1. In the **Variable Manager**, hover over the **Colors** group and click **Generate Color Palette Variables**.
2. Set your **primary color**. Divi uses this as the foundation for the entire palette.
3. Adjust the relationship to your **secondary color** (for example, complementary or analogous).
4. Choose how many shades you want for each color.
5. Click **Add Variables To My Site** to save the palette to your Variable Manager.

## What the Color Palette Generator Produces

The generator updates the four base color slots in your Variable Manager (**Primary**, **Secondary**, **Heading Text**, **Body Text**, and **Link**) and creates a spectrum of light-to-dark shades and transparent versions of those base colors.

Because every shade is defined relative to the primary color, changing the primary later updates every linked shade automatically. You only have to maintain one source color, and the rest of your palette follows.

## Using the Fluid Sizing Variable Generator

[![](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340048006/4cd3cff0896b7e9c74210bca4c09/216_add-fluid-sizing-variabable-generator.gif?expires=1778077800&signature=a0cddce8791e5ae0a596449948ec7ed8d0ee287f9d46fa1501870abb6794b565&req=diMjFsl6lYFfX%2FMW1HO4zW47ywdS36JRkAuCdGC3cZPMfczhwU3bTobRQa82%0Am2rqwN6okjQ08p0Ln2w%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340048006/4cd3cff0896b7e9c74210bca4c09/216_add-fluid-sizing-variabable-generator.gif?expires=1778077800&signature=a0cddce8791e5ae0a596449948ec7ed8d0ee287f9d46fa1501870abb6794b565&req=diMjFsl6lYFfX%2FMW1HO4zW47ywdS36JRkAuCdGC3cZPMfczhwU3bTobRQa82%0Am2rqwN6okjQ08p0Ln2w%3D%0A)

The **Fluid Sizing Variable Generator** builds a scale of related size values, like font sizes that step from small to large, or spacing tokens that step from tight to roomy.

You can generate scales for several different design properties (called token families) and pick how those values should respond to different screen sizes.

## Step 1: Open the Generator and Pick a Token Family

[![](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340069700/57e0fc0bbd3905fedc08102a22c5/+var-generator-1.png?expires=1778077800&signature=8e7b0bed677e51fe4284d5f94089195ec23460f46cf90510794f17e1642ad576&req=diMjFsl4lIZfWfMW1HO4zRJTrKyQ5Jj8Bl4f7FbkXxN6OBvivTlGHO5omEAv%0Aly35VZ0FkACB4G8TTp4%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340069700/57e0fc0bbd3905fedc08102a22c5/+var-generator-1.png?expires=1778077800&signature=8e7b0bed677e51fe4284d5f94089195ec23460f46cf90510794f17e1642ad576&req=diMjFsl4lIZfWfMW1HO4zRJTrKyQ5Jj8Bl4f7FbkXxN6OBvivTlGHO5omEAv%0Aly35VZ0FkACB4G8TTp4%3D%0A)

1. In the **Variable Manager**, hover over the **Numbers** group and click **Generate Fluid Sizing Variables**.
2. From the **Number variable type** dropdown in the sidebar, choose what you want to generate. The available token families are:

- **Font Size Scale** for typography
   - **Spacing scale** for padding and margin
   - **Gap scale** for the space between flex and grid items
   - **Radius scale** for border radius
   - **Border width scale** for border thickness
   - **Width scale** for element widths
   - **Clamp (generic)** for any single fluid value
   - **Size (generic)** for any single fixed value

Divi sets sensible defaults for each token family, so beginners can stop here and skip straight to step 4.

## Step 2: Choose a Scale Type

Each token family supports up to three scale types. Pick one based on how you want the values to respond to screen size.

- **Fluid** uses `clamp()`, a CSS function that smoothly interpolates a value between a minimum and maximum as the viewport resizes. This is the modern way to do responsive typography and spacing without breakpoints. To learn more, read **[Advanced Units, CSS Functions, and Variables For Divi 5](https://help.elegantthemes.com/en/articles/10823890-advanced-units-css-functions-and-variables-for-divi-5)**.
- **Fixed Responsive** outputs one value per enabled breakpoint (Phone, Tablet, Desktop, etc.). Use this when you want explicit control at each screen size instead of a smooth curve.
- **Fixed Single** outputs one value that applies across all screen sizes. Use this for tokens that should not respond to screen size at all.

## Step 3 (Optional): Customize the Scale

[![Divi 5 - Variable Generator - Customize the Scale](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340139007/225785dca35aab367e1165c1debf/218_add-scale.gif?expires=1778077800&signature=cf102f078199fe3f900cac07abf0f13f28e577faa25d6f87cbffcae19907a033&req=diMjFsh9lIFfXvMW1HO4zT4ovddPJaXOxh1OrftR0T2m1CWTF3ySw0RLzjcl%0A4xmJKQz99hvRS7fi6cA%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340139007/225785dca35aab367e1165c1debf/218_add-scale.gif?expires=1778077800&signature=cf102f078199fe3f900cac07abf0f13f28e577faa25d6f87cbffcae19907a033&req=diMjFsh9lIFfXvMW1HO4zT4ovddPJaXOxh1OrftR0T2m1CWTF3ySw0RLzjcl%0A4xmJKQz99hvRS7fi6cA%3D%0A)

If you want to tune the defaults, the sidebar exposes every aspect of the scale.

- **Variable prefix** - Sets the name prefix for every variable in the scale (for example, `text-` produces `--text-s`, `--text-m`, `--text-l`).
- **Generated CSS units -**  Lets you choose `rem` or `px` for the output.
- **Suffix style** switches between t-shirt names (xs, s, m, l, xl) and numeric names (1, 2, 3, 4, 5).
- **Base size -**  Sets which step in the scale is the baseline value.
- **Min. base** and **Max. base -** Define the size of that baseline at the smallest and largest viewport widths (fluid mode only).
- **Min. ratio** and **Max. ratio -** Control how aggressively each step grows or shrinks. Divi includes preset ratios like 1.125 (Major Second), 1.25 (Major Third), and 1.618 (Golden Ratio), or you can enter a custom ratio or a linear step.

You can also toggle special tokens like `gap-0`, `space-0`, `border-none`, `radius-none`, `radius-full`, and `width-full`, which are common values that sit outside the modular scale.

## Step 4: Preview and Add to Your Site

The right side of the generator shows a live results table with every variable in the scale, the computed values, and a visual preview of how each one will look in practice.

Typography previews show sample text, spacing previews show padded boxes, gap previews show flex rows, and so on.

A few useful controls in the results header:

- **Customize Values** lets you rename individual variables and override specific values without losing the rest of the scale.
- **Show CSS** displays the generated CSS for each variable.
- **Close Sidebar** hides the configuration panel so you can preview the scale at full width.

For fluid scales, a **Resize your browser to preview fluid values** section appears below the table. Drag your browser window narrower or wider to see the values respond in real time.

When you are ready, click **Add Variables To My Site**. If a prefix already exists in your Variable Manager, Divi will ask you to confirm before overriding the previous variables.

## How the Variable Generator Fits with Presets

The Variable Generator only creates Global Variables. To turn those variables into reusable styles, you combine them with the two preset systems in Divi 5.

- **[Element Presets](https://help.elegantthemes.com/en/articles/14093011-advanced-styling-using-element-presets-in-divi-5)** control the default design for an entire module type (every Button, every Heading, every Blurb).
- **[Option Group Presets](https://help.elegantthemes.com/en/articles/14093014-advanced-styling-using-option-group-presets-in-divi-5)** control specific groups of settings inside a module (for example, the Border group on a Button).
- **Global Variables** (created by the Variable Generator) hold the actual reusable values your presets reference.

A typical workflow looks like this:

1. Use the Variable Generator to create your sizing scale and color palette.
2. Build Option Group Presets that reference those variables for spacing, typography, borders, and color.
3. Stack those Option Group Presets inside Element Presets so each module type pulls from your generated variables by default.
4. When you build pages, drop in modules and let them inherit from the presets.

The result is a layered system: change a generated variable to adjust the raw value, change a preset to adjust how that value gets used, and only override on a single module when you need a one-off. To manage your presets, see **[Preset Manager and Preset Preview Systems in Divi 5](https://help.elegantthemes.com/en/articles/14093024-preset-manager-and-preset-preview-systems-in-divi-5).**

## Frequently Asked Questions

**Will the generator overwrite my existing variables?**

Only if you tell it to. If a prefix you are generating already exists in your Variable Manager, Divi prompts you to confirm before replacing the previous variables.

**Can I edit values after I add them to my site?**

Yes. Once added, the variables become regular Global Variables. Open the Variable Manager and edit them like any other variable.

**Why does the preview show px values when my unit is set to rem?**

The preview always displays sizes in px for readability. The generated CSS still uses your chosen unit (`rem` or `px`).

**What is the difference between Fluid and Fixed Responsive?**

Fluid outputs one `clamp()` value per token that scales smoothly between a minimum and maximum as the viewport resizes. Fixed Responsive outputs separate values per breakpoint, giving you explicit control at each screen size.

**Can I add more variables to a scale after I generate it?**

Yes. Use the **+ Add smaller variable** and **+ Add larger variable** buttons in the results table to extend the scale before you add it to your site.

---

Related Articles

[Advanced Units, CSS Functions, and Variables For Divi 5](https://help.elegantthemes.com/en/articles/10823890-advanced-units-css-functions-and-variables-for-divi-5)[Relative Colors & HSL in Divi 5](https://help.elegantthemes.com/en/articles/11631084-relative-colors-hsl-in-divi-5)[Exploring Divi 5's New Features](https://help.elegantthemes.com/en/articles/12331954-exploring-divi-5-s-new-features)[Global Variables in Divi 5](https://help.elegantthemes.com/en/articles/13348842-global-variables-in-divi-5)[Why Divi 5 Is Better than Divi 4](https://help.elegantthemes.com/en/articles/13762555-why-divi-5-is-better-than-divi-4)

## Code Examples

<!-- TODO: Add tested code examples -->

```css
/* TODO: Add CSS customization examples */
```

```php
// TODO: Add PHP hook/filter examples
```

## Common Patterns

<!-- TODO: Add 2-3 real-world use cases -->

## Version Notes

!!! note "Divi 5"
    This page documents Divi 5 behavior. Some settings or markup may differ from Divi 4.

## Troubleshooting

<!-- TODO: Add common issues and solutions -->

## Related

<!-- TODO: Add links to related pages -->
