---
title: "Button Module — Styling Reference"
category: modules
tags: [button, hover, presets, css-classes, styling, design-system]
related: [button, design-system-setup, global-elements]
divi_version: "5.x"
last_updated: 2026-04-15
source_url: "https://help.elegantthemes.com/en/articles/10259665-the-button-module-divi-5"
---

# Button Module — Styling Reference

Quick reference for hover states, custom CSS classes, and creating reusable button presets in Divi 5.

## Overview

Divi 5 changed how button styling works compared to Divi 4. Hover states are now inside the Responsive Editor, custom CSS classes moved to the Attributes panel, and the preset system replaced the need for most custom CSS. This page covers all three workflows.

<!-- TODO: Screenshot of a styled light button on a dark background section -->

## Setting Hover States on a Button

In Divi 5, hover state controls are inside the **Responsive Editor** — the same panel that handles desktop, tablet, and mobile breakpoints.

### How to Access Hover States

1. Open the Button module settings.
2. Go to **Design → Button**.
3. Toggle **"Use Custom Styles for Button"** to **YES**.
4. Next to any style property (e.g., Button Background Color), click the **"Edit Responsive Values"** icon.
5. The Responsive Editor opens with **four rows**:
    - **Desktop** (monitor icon)
    - **Tablet** (tablet icon)
    - **Mobile** (phone icon)
    - **Hover** (cursor/pointer icon — bottom row)
6. Set your hover value in the **bottom row**.
7. Close the Responsive Editor.

<!-- TODO: Screenshot of the Responsive Editor showing the four rows with hover at the bottom -->

!!! tip "Hover Is Always the Bottom Row"
    The hover field sits below the three device breakpoints in every Responsive Editor panel. If you don't see it, scroll down — it's there for every style property that supports hover states.

### Properties That Support Hover States

Repeat the Responsive Editor workflow for each property you want to change on hover:

| Property | Common Hover Use |
|----------|-----------------|
| Button Background Color | Darken or lighten on hover |
| Button Text Color | Contrast shift |
| Button Border Color / Width | Border emphasis or removal |
| Button Border Radius | Subtle shape change |
| Button Box Shadow | Add depth on hover |
| Button Icon Color | Match text color change |

## Adding Custom CSS Classes in Divi 5

The Divi 4 approach (**Advanced → CSS ID & Classes** toggle) no longer exists. In Divi 5, CSS classes are added through the **Attributes** panel.

### How to Add a Custom Class

1. Open the Button module settings.
2. Go to **Advanced → Attributes**.
3. Click **"Add Attribute"**.
4. Set **Attribute Name** to `class`.
5. Set **Attribute Value** to your class name (e.g., `light-cta`).
6. Confirm.

<!-- TODO: Screenshot of Advanced → Attributes panel with a class attribute added -->

!!! warning "Divi 4 → Divi 5 Migration"
    If you're migrating from Divi 4, existing CSS ID and class values carry over automatically. They appear in the Attributes list when you open the element in Divi 5. No manual migration required.

### Targeting the Button with Custom CSS

If you add a class via Attributes, target it in your page or theme custom CSS:

```css
.light-cta .et_pb_button {
  background-color: #ffffff !important;
  color: #000000 !important;
  border-color: #ffffff !important;
}
```

!!! note "Presets Are Usually Better"
    In most cases, a Button Preset (see below) is a better approach than custom CSS classes. Presets are managed visually, don't require `!important` overrides, and update globally when edited.

## Creating a Reusable Button Preset

Presets are the recommended way to create reusable button styles in Divi 5. Style once, apply anywhere, update globally from a single source.

### Step-by-Step: Create a "Light Button" Preset

1. Open the Button module settings.
2. Go to **Design → Button**.
3. Toggle **"Use Custom Styles for Button"** to **YES**.
4. Set **default state** styles:
    - Button Background Color → `#FFFFFF`
    - Button Text Color → `#000000`
    - Button Border Color → `#FFFFFF`
5. Set **hover state** styles (via the Responsive Editor):
    - Button Background Color (hover) → `#F0F0F0`
    - Button Text Color (hover) → `#000000`
    - Button Border Color (hover) → `#F0F0F0`
6. At the top of the settings panel, click the **Preset dropdown** (icon next to the module name).
7. Choose **"Create New Preset From Current Styles"**.
8. Name it (e.g., `Light Button` or `Button - Light on Dark`).
9. Click **Save Preset**.

<!-- TODO: Screenshot of the Preset dropdown showing "Create New Preset From Current Styles" -->

### Applying the Preset to Other Buttons

1. Add or open any Button module.
2. Click the **Preset dropdown** at the top of the settings panel.
3. Select your **"Light Button"** preset.
4. The button inherits all default and hover styles immediately.

### Updating the Preset Globally

1. Open any Button module that uses the preset.
2. In the Preset dropdown, hover the preset name and click the **gear icon**.
3. The settings panel switches to **Global Preset editing mode** (gray header).
4. Make your changes.
5. Click **"Save Preset"** — all instances update site-wide.

!!! tip "Set a Default Preset"
    If one button style is used most often on your site, set it as the default by clicking the **star icon** on the preset in the dropdown. Every new Button module you add will use it automatically.

## Stacked Presets for Button Variations

Divi 5 supports applying **multiple presets** to the same element. Styles are layered — later presets override earlier ones for the same property.

### Example: Base + Light Variant

| Preset | Controls |
|--------|----------|
| **"Default Button"** (Preset 1) | Font size, padding, border radius, icon |
| **"Light Variant"** (Preset 2) | Background → white, text → dark |

Apply both to a button: it gets the base sizing and shape from Preset 1 and the light color treatment from Preset 2. Change the base padding later and all buttons — light and dark — update together.

### When to Use Stacked Presets

- You have multiple button color treatments (light, dark, accent) but want consistent sizing across all of them.
- You want to separate structural styles (spacing, radius) from color styles.
- You're building a design system with base + modifier patterns.

For a full walkthrough of the Divi 5 preset system including Option Group Presets and nested presets, see the [Design System Setup playbook](../playbooks/design-system-setup.md).

## Troubleshooting

### "Identifier is expected" Error in Custom CSS

This error appears when writing CSS in the module's **Advanced → CSS → Free-Form CSS** area. The most common cause is a **trailing comma** after a selector with nothing following it:

```css
/* ❌ WRONG — trailing comma expects another selector */
.et-light-button,
.et-light-button:hover {
  background-color: #ffffff;
}
```

```css
/* ✅ CORRECT — separate rule blocks, no trailing comma */
.et-light-button {
  background-color: #ffffff;
}
.et-light-button:hover {
  background-color: #f0f0f0;
}
```

### Free-Form CSS: The `selector` Keyword

In Divi 5's Free-Form CSS area, use the `selector` keyword to target the current module without needing to know its generated class:

```css
selector {
  background-color: #ffffff;
  color: #000000;
}
```

### `.et-light-button` Class Not Working

The `.et-light-button` class was a Divi 4 convention. It may not exist or behave the same way in Divi 5. Use the Design tab's built-in button styling options or create a preset instead.

## Related

- [Design System Setup Playbook](../playbooks/design-system-setup.md) — full guide to presets, variables, and global styling
- [Global Elements](../builder/global-elements.md) — saving buttons as reusable global modules
- [Button Module Reference](https://help.elegantthemes.com/en/articles/10259665-the-button-module-divi-5) — official Elegant Themes documentation
