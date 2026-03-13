---
title: "Divi Presets"
category: builder
tags: [builder, presets, global-styles, design-system]
related: [visual-builder, global-elements, library]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: ""
---

# Divi Presets

Divi Presets are saved design configurations that can be applied to any section, row, column, or module to maintain consistent styling across your website.

## Overview

Presets allow you to define a set of design settings once and apply them to multiple elements throughout your site. When you update a preset, every element using that preset updates automatically. This makes presets one of the most powerful tools for maintaining a consistent design system.

Every module, row, section, and column in Divi has a **Default Preset** that defines its base appearance. You can modify the default preset to change how every instance of that element looks across your entire website, or create additional custom presets for different styling variations.

Presets work similarly to CSS classes in concept -- they define a reusable set of styles. But unlike CSS, presets are managed entirely through the Visual Builder's interface with no code required.

![Presets overview](../assets/screenshots/builder/presets/overview.png){ loading=lazy }
*The presets dropdown in the element settings window showing available presets.*

## How Presets Work

When you apply a preset to an element:

1. The element inherits all design settings from the preset
2. You can still override individual settings on the element level
3. Changes to the preset automatically propagate to all elements using it
4. Element-level overrides are preserved when the preset changes

| Concept | Description |
|---------|-------------|
| **Preset** | A saved collection of design settings for an element type |
| **Default Preset** | The base preset applied to all new instances of an element type |
| **Custom Preset** | An additional preset you create for a specific styling variation |
| **Override** | A setting changed on an individual element that takes priority over the preset |
| **Inheritance** | Elements automatically receive styles from their assigned preset |

## Creating a Preset

### Method 1: From the Presets Dropdown

1. Open any element's settings in the Visual Builder
2. Click the **Presets dropdown** below the element name
3. Click **Create New Preset**
4. Name your preset (e.g., "Primary Button", "Dark Section", "Card Row")
5. The new preset is created with the element's current settings
6. Click **Save** to confirm

### Method 2: From the Three-Dot Menu

1. Open an element's settings
2. Design the element as desired
3. Click the **three-dot menu** (vertical ellipsis)
4. Select **Apply Styles To Active Preset** to save current styles to the active preset
5. Or select **Edit Preset Style** to open the preset editor directly

### Method 3: From an Existing Element

1. Design an element with the exact styling you want
2. Open the element's settings
3. Click the **Presets dropdown**
4. Click **Create New Preset**
5. The preset captures all current design settings from the element

## Applying a Preset

1. Open the target element's settings in the Visual Builder
2. Click the **Presets dropdown** below the element name
3. Select the desired preset from the list
4. The element's design updates immediately to match the preset

!!! tip "Preset Scope"
    Presets are specific to element types. A Button module preset can only be applied to other Button modules. A Text module preset can only be applied to other Text modules.

## Editing a Preset

When you edit a preset, the changes apply to every element using that preset across your entire website.

### Editing from the Settings Window

1. Open any element that uses the preset
2. Click the **three-dot menu**
3. Select **Edit Preset Style**
4. The settings window switches to preset editing mode (indicated by a visual change)
5. Make your design changes
6. Click **Save** -- changes apply globally to all elements using this preset

### Editing from the Presets Dropdown

1. Open any element's settings
2. Click the **Presets dropdown**
3. Hover over the preset you want to edit
4. Click the **edit** (pencil) icon
5. Make changes and save

!!! warning "Preset Edits Are Global"
    Editing a preset affects every element on your website that uses it. If you want to change only one element, override the setting at the element level instead of editing the preset.

## The Default Preset

Every element type has a **Default Preset** that defines its base appearance. The default preset is special:

| Behavior | Description |
|----------|-------------|
| **Automatic assignment** | All new instances of the element type use the default preset |
| **Site-wide impact** | Changes to the default preset affect every instance of that element across the entire website |
| **Cannot be deleted** | The default preset always exists for every element type |
| **Baseline styles** | Serves as the foundation; custom presets and element overrides build on top of it |

### Modifying the Default Preset

1. Open any instance of the element type
2. Make sure the **Default** preset is selected in the Presets dropdown
3. Click the **three-dot menu**
4. Select **Edit Preset Style**
5. Make your design changes
6. Click **Save**

All instances of that element type across your site now reflect the updated defaults.

## Managing Presets

### Viewing All Presets for an Element

1. Open the element's settings
2. Click the **Presets dropdown**
3. All available presets for that element type are listed

### Deleting a Preset

1. Open the element's settings
2. Click the **Presets dropdown**
3. Hover over the preset to delete
4. Click the **delete** (trash) icon
5. Confirm deletion

!!! warning "Deleting a Preset"
    When you delete a preset, elements that were using it revert to the Default Preset. Any element-level overrides are preserved.

### Renaming a Preset

1. Open the Presets dropdown
2. Hover over the preset
3. Click the edit icon
4. Change the preset name at the top of the editor
5. Save

## Presets vs. Global Elements

Presets and [Global Elements](global-elements.md) both provide reusability, but they work differently:

| Feature | Presets | Global Elements |
|---------|---------|-----------------|
| **What is shared** | Design settings only | Entire element (content + design) |
| **Content independence** | Each element has its own content | All instances share the same content |
| **Use case** | Consistent styling with different content | Identical element repeated across pages |
| **Example** | All buttons share the same style but different labels | The same CTA block on every page |

## Best Practices

### Build a Design System with Presets

Create presets for your core design elements early in a project:

- **Button presets**: Primary, Secondary, Outline, Ghost
- **Section presets**: Light Background, Dark Background, Gradient
- **Text presets**: Body Text, Heading, Caption, Pull Quote
- **Row presets**: Standard Content, Card Grid, Full-Width

### Use Descriptive Names

Name presets clearly so you and other editors can identify them:

- "Primary CTA Button" instead of "Button Style 1"
- "Dark Hero Section" instead of "Section 2"
- "Blog Card Row" instead of "Custom Row"

### Limit Element-Level Overrides

Keep overrides to a minimum. If you find yourself overriding the same preset settings repeatedly, consider creating a new preset for that variation.

## Code Examples

### Targeting Preset Styles with CSS

```css
/* Presets apply styles through Divi's inline style system.
   To override a preset with custom CSS, use the element's
   CSS class or ID from the Advanced tab. */

/* Example: Override a specific preset's button styling */
.primary-cta-button .et_pb_button {
    letter-spacing: 2px;
    text-transform: uppercase;
}
```

<!-- TODO: Verify Divi 5 preset CSS class naming conventions -->

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Presets in Divi 5 build on the Global Presets system introduced in Divi 4 with an improved management interface.

## Troubleshooting

!!! warning "Preset Changes Not Appearing"
    If changes to a preset are not reflected on your site:

    1. Verify you are editing the preset and not the individual element (look for the preset editing indicator)
    2. Clear any page caching plugins
    3. Hard-refresh the browser (Cmd/Ctrl + Shift + R)
    4. Check that the affected elements are actually using the preset you edited

!!! warning "Element Override Not Working"
    If an element-level override is being ignored:

    1. Make sure you are editing the element, not the preset
    2. Check that the setting you changed is not being overridden by a parent element's style
    3. Verify the override is saved (click the green Save button)

## Related

- [Visual Builder](visual-builder.md) -- The editor where presets are created and managed
- [Global Elements](global-elements.md) -- Reusable elements that sync content and design
- [Divi Library](library.md) -- Saving and loading complete layouts
- [Theme Builder](theme-builder.md) -- Templates that benefit from preset-based design systems
