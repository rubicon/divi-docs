---
title: "Element Presets"
category: builder
tags: ["builder", "presets", "element-presets", "design-system", "global-styles"]
related: ["presets", "vb-interface", "left-sidebar"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13349150"
---

# Element Presets

Saved design configurations for specific element types that keep styling consistent across your entire Divi site.

## Overview

An Element Preset is a saved collection of all modified settings for a specific element type -- colors, typography, spacing, alignment, borders, shadows, effects, interactions, and hover states. Each element type (Button, Blurb, Section, Row, etc.) maintains its own separate preset list. When you apply a preset to matching elements, every instance inherits the same look and updates automatically when you edit the preset later. For the official Elegant Themes reference, see [Divi Element Presets](https://help.elegantthemes.com/en/articles/13349150){:target="_blank"}.

Element Presets are one layer in Divi 5's broader preset architecture. For the general concepts, default presets, and management workflows, see the main [Presets](presets.md) page. This page focuses on the element preset creation, management, and advanced features unique to the Divi 5 system.

## Creating Element Presets

### From Scratch

1. Open the Visual Builder and add the module type you want to create a preset for.
2. Open its settings and click the **Preset dropdown** at the top of the panel.
3. Click **Add New Preset**.
4. Name the preset in the **Content Tab > Preset Settings** field (e.g., "Primary Button", "Hero Section").
5. Style the element in the **Design** tab. All changes are saved to the preset, not the individual element.
6. Click **Save Preset**.

### From Existing Styles

If you have already styled an element and want to capture its look as a reusable preset:

1. Open the styled element's settings.
2. Click the **Preset dropdown**.
3. Select **New Preset From Current Styles**.
4. Name the preset and save.

The new preset captures all current design settings from the element.

## Applying a Preset

1. Open any element of the matching type.
2. Click the **Preset dropdown** at the top of the settings panel.
3. Select the desired preset from the list.
4. The element's design updates immediately.

!!! tip "Type-Specific"
    Presets are scoped to their element type. A Button preset can only be applied to Button modules. A Section preset can only be applied to sections.

## Managing Presets

### From the Preset Dropdown

Within any element's settings, the Preset dropdown lets you:

- **Apply** an existing preset by clicking its name.
- **Edit** a preset by hovering its name and clicking the **gear icon**. This opens the preset editor where changes propagate globally.
- **Set as default** by clicking the **star icon**. New instances of that element type will use this preset automatically.

### From the Preset Manager

The [Preset Manager](left-sidebar.md) in the left sidebar provides a centralized view of all presets across your site, organized by element type. From here you can browse, create, edit, rename, and delete presets without navigating to an individual element.

## Setting a Default Preset

Click the **star icon** next to any preset in the dropdown to designate it as the default for that element type. When you add a new module of that type, it uses the default preset automatically. Only one preset can be the default per element type.

## Advanced Features

### Stacked Presets

Divi 5 lets you apply **multiple presets** to a single element. When presets are stacked, later presets override earlier ones for any properties that overlap, following CSS-like specificity logic. This lets you create a base preset for general styling and layer variation presets on top for context-specific adjustments.

**Example**: A "Base Card" preset sets background, border, and shadow. A "Dark Card" preset overrides only the background and text color. Stacking both gives you a dark card with the same border and shadow as the base.

### Nested Presets (Option Group Presets)

Element Presets can incorporate **Option Group Presets** -- presets that define styling for a specific option group (spacing, typography, shadows) rather than an entire element. By nesting option group presets inside element presets, you create modular, composable design tokens.

**Example**: An "Ample Spacing" option group preset defines generous padding and margin values. You nest it inside both your "Hero Section" and "Feature Card" element presets, ensuring they share the same spacing system. Update the spacing preset once, and both element presets reflect the change.

### Design Variables Integration

Presets can reference global design variables for colors, fonts, and spacing. When a variable changes, every preset (and every element using that preset) updates automatically. This creates a three-tier design system:

1. **Variables** define raw values (brand colors, type scale, spacing scale).
2. **Option Group Presets** compose variables into reusable patterns.
3. **Element Presets** compose option group presets into complete element designs.

## Recommended Workflow

1. **Define global variables** for your brand colors, fonts, and spacing scale.
2. **Create base element presets** for your core element types (buttons, sections, text modules, rows).
3. **Build option group presets** for recurring design patterns (consistent spacing, standard borders, shadow styles).
4. **Nest option group presets** inside element presets to keep styling modular.
5. **Stack variation presets** when you need context-specific changes (dark mode, compact layout, etc.).
6. **Set defaults** so new elements inherit the correct preset automatically.

## Version Notes

!!! note "Divi 5 Only"
    Stacked presets, nested option group presets, and the Preset Manager sidebar panel are all new to Divi 5. Divi 4's Global Presets provided similar per-element-type styling but without the composability features.

## Troubleshooting

!!! warning "Preset Not Appearing in Dropdown"
    If a preset you created is not showing up, verify that you are looking at the correct element type. Button presets only appear on Button modules, Section presets only appear on sections, and so on.

!!! warning "Stacked Preset Conflicts"
    If two stacked presets define the same property, the last-applied preset wins. Reorder your stacked presets or remove the conflicting property from one of them.

## Related

- [Presets](presets.md) -- General preset concepts, default presets, and management
- [Visual Builder Interface](vb-interface.md) -- Where preset controls appear
- [Left Sidebar](left-sidebar.md) -- Preset Manager access
- [Copy & Paste Attributes](copy-paste-attributes.md) -- Alternative for one-off style transfers
