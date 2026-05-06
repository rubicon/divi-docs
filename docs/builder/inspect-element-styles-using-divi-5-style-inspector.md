---
title: "Inspect Element Styles Using Divi 5 Style Inspector"
category: builder
tags: [builder, style-inspector, debugging, colors, fonts, presets]
related: [visual-builder-overview, theme-builder-overview]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/13002652-inspect-element-styles-using-divi-5-style-inspector"
---

# Inspect Element Styles Using Divi 5 Style Inspector

A centralized panel that displays all styles, content, and presets applied to your design in one place, eliminating the need to click through individual modules to find where a color, font, or preset originates.

## Overview

The Divi 5 Style Inspector is a powerful debugging and auditing tool that lets you see everything affecting your page design at a glance. Instead of opening each module to track down a specific color or font, you can open the Style Inspector and review all applied styles, content values, and presets within seconds.

This is particularly useful for:

- **Design audits** — Spot inconsistent colors, font sizes, or spacing values across a page
- **Color management** — Map static (one-off) colors to global color variables
- **Typography cleanup** — Ensure your fonts and weights are limited to a curated set
- **Preset tracking** — See which modules use which presets and update them globally
- **Rapid inspection** — View all details for a selected element without opening its settings panel

The Style Inspector works in two scopes: page-level (for site-wide audits) and element-level (for focused inspection of a single component).

![Style Inspector overview](../assets/screenshots/builder/inspect-element-styles-using-divi-5-style-inspector/overview.png){ loading=lazy }
*The Style Inspector panel showing all colors, fonts, and other styles in use on a page.*

## How to Open the Style Inspector

1. Open a page in the **Divi 5 Visual Builder**
2. Look for the **Inspector icon** in the builder interface left sidebar panel (it looks like a magnifying glass)
3. Click the icon to open the **Divi 5 Style Inspector** panel on the right

You can open the Style Inspector with nothing selected to see a page-level overview, or with an element selected to see only what applies to that element.

## Page-Level vs Element-Level Inspection

The Divi 5 Style Inspector works in two scopes:

### Page-Level Inspection

Open the Style Inspector while no element is specifically selected.

| Aspect | Behavior |
|--------|----------|
| Scope | Shows a summary of all styles, content, and presets used on the entire current page |
| Use case | Best for audits and cleaning up inconsistent values across a page |
| View | All applied styles, grouped by category |

### Element-Level Inspection

Click on any element in your page to select it, then open the Style Inspector.

| Aspect | Behavior |
|--------|----------|
| Scope | Inspector filters to show only what affects the selected element |
| Selection | Click any element directly, or click the **Gear icon** to open its settings first |
| Switching | You can switch between elements while the Style Inspector is open; the panel updates to match whichever element you click |

## The Three Main Tabs

The Style Inspector has three tabs, each grouping information differently so you can focus on what you care about:

### Styles Tab

The **Styles tab** lets you inspect element styles across a page or element.

| Information | What It Shows |
|-------------|---------------|
| Colors | All colors in use, grouped. Global colors usually appear first, often sorted by frequency. Static (non-global) colors appear separately so you can spot odd one-off values. |
| Numbers | Font sizes, line heights, spacing, and other numeric values. Helps you identify if you have too many similar but slightly different values. |
| Fonts and weights | Which font families and weights are used. Helpful if you want to keep typography limited to a small set. |
| Layout | All Layout Styles used page-wide or on a selected element. |
| Media | Background images and other media used in your design. |
| Code | Custom CSS or code snippets tied to elements. |

![Styles tab view](../assets/screenshots/builder/inspect-element-styles-using-divi-5-style-inspector/settings-styles.png){ loading=lazy }
*The Styles tab showing colors, fonts, spacing, and other applied styles.*

### Content Tab

The **Content tab** lets you inspect element content grouped by type.

| Information | What It Shows |
|-------------|---------------|
| Media | Background images and other media used in your design. |
| Code | Custom CSS or code snippets tied to elements. |
| Attributes | IDs, classes, alt text, titles, and other HTML attributes. |
| Text | Actual text content used in modules. |

Use this tab to audit content values across your page and clean up inconsistent or missing attributes (e.g., missing alt text, incorrect title tags, stray IDs).

![Content tab view](../assets/screenshots/builder/inspect-element-styles-using-divi-5-style-inspector/settings-content.png){ loading=lazy }
*The Content tab showing media, code, attributes, and text values.*

### Presets Tab

The **Presets tab** shows you which presets are in play.

| Information | What It Shows |
|-------------|---------------|
| Module presets | Presets applied to specific modules on the page. |
| Option group presets | Presets applied to option groups such as buttons, title text, backgrounds, etc. |

Use this tab to verify that modules and option groups are using the correct presets, and to update presets so all attached elements inherit the new styles.

![Presets tab view](../assets/screenshots/builder/inspect-element-styles-using-divi-5-style-inspector/settings-presets.png){ loading=lazy }
*The Presets tab showing which module and option group presets are active.*

## Making Changes Directly in the Style Inspector

The Divi 5 Style Inspector is not just a viewer—you can edit many things directly from the panel.

### Common Editing Workflows

#### Update a Color

1. In the **Styles tab**, pick a color value
2. Change it to another color or map it to the correct global color
3. All uses of that value update in the active scope (page or element)

#### Fix Inconsistent Font Sizes

1. Look at the list of font sizes in the **Styles tab**
2. Adjust or remove odd one-off values and align them to your core sizes

#### Clean Up Content Attributes

1. In the **Content tab**, fix missing alt text, wrong titles, or stray IDs
2. This is often faster than opening every module separately

#### Adjust Presets

1. In the **Presets tab**, see which presets are used
2. Update presets so all attached elements inherit the new styles

## Inspect Element Styles Step by Step

### Example: Inspecting a Single Module

1. Open the page in the Visual Builder
2. Click the element (section, row, or module) you want to inspect
3. Open the Divi 5 Style Inspector
4. In the **Styles tab**:
   - Check which colors, sizes, and fonts are in use for that module
   - Ensure it is using the correct static or global color and font
5. In the **Presets tab**:
   - Check if it uses the correct button, text, or component preset
   - Update the preset if all buttons of that type should match

### Example: Page-Wide Audits

1. Open the Divi 5 Visual Builder (don't select any element)
2. Open the Style Inspector with nothing selected
3. Review all global and static colors in use
4. Check fonts and weights
5. Check spacing values like padding and margin
6. In the **Content tab**:
   - See what images and backgrounds are used
   - Review IDs, classes, and alt text for consistency
7. In the **Presets tab**:
   - Make sure the presets you expect to see are actually used

## Common Use Cases

### Color Audit and Standardization

Use the Style Inspector to find all colors on a page and map static colors to global color variables. This ensures consistent color usage and makes brand updates easier.

### Typography Review

Review all fonts and weights in use to ensure your design is limited to a curated typography set. This keeps designs clean and reduces file size.

### Preset Verification

Verify that buttons, titles, backgrounds, and other reusable components are using presets, not custom overrides. This makes bulk updates faster and keeps your design system intact.

### Missing or Incomplete Content

Audit alt text, titles, and IDs across a page to ensure accessibility and SEO best practices are met.

## Tips for Using the Divi 5 Style Inspector

- **Switch elements while inspecting** — The Style Inspector panel updates in real-time as you click different elements, so you don't need to close and reopen it
- **Use page-level view for big-picture insights** — Before diving into individual elements, open the Style Inspector at page level to understand your design's color and font usage patterns
- **Combine with global variables** — Use the Style Inspector to identify static colors, then map them to global colors for centralized control
- **Run regular audits** — Make style audits part of your design process to catch inconsistencies before they multiply across pages

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Style Inspector is a new feature in Divi 5 and is not available in Divi 4.

## Related

- [Visual Builder Overview](../builder/visual-builder.md)
- [Theme Builder Overview](../builder/theme-builder.md)
- [Global Colors and Variables](../builder/global-variables.md)
