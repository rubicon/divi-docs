---
title: "Option Group Presets"
category: builder
tags: [builder, presets, option-group-presets, design-system, reusable-styles]
related: [stacked-nested-presets, preset-manager, presets]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10725144"
---

# Option Group Presets

Option group presets are reusable style blocks scoped to a single design option group — such as typography, background, borders, or buttons — that can be applied across any element type in Divi 5.

## Overview

Unlike [element presets](presets.md), which apply a full set of design settings to a specific element type, option group presets target a single option group and work across element boundaries. A typography preset created on a Text module can be applied to the title text of a Blurb, the heading of a Call to Action, or any other element that has a matching option group. This cross-element reusability makes option group presets function like CSS utility classes.

When you edit an option group preset, the change propagates site-wide to every element using it. This makes them a powerful tool for maintaining consistent typography scales, button styles, spacing rules, and background treatments across an entire site.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10725144) and the [expanded guide](https://help.elegantthemes.com/en/articles/13349301).

## Element Presets vs. Option Group Presets

| Feature | Element Presets | Option Group Presets |
|---------|-----------------|----------------------|
| Scope | Applies to one element type only | Applies to any element with a matching option group |
| Coverage | Full element styling (all settings) | Single option group (e.g., Typography, Background) |
| Cross-element reuse | No | Yes |
| Use case | Complete module designs | Shared style fragments |

## Available Option Group Types

Option group presets can be created for any option group that appears in the Design tab of an element's settings. Common groups include:

| Option Group | Description |
|--------------|-------------|
| Typography | Font family, size, weight, line height, letter spacing, color |
| Background | Background color, gradient, image, video |
| Borders | Border width, style, color, radius |
| Spacing | Margin and padding values |
| Buttons | Button text, background, border, spacing, hover states |
| Shadows | Box shadow settings |
| Effects | Filters, transforms, and scroll effects |

## Creating an Option Group Preset

1. Open any element's settings in the Visual Builder
2. Navigate to the **Design** tab
3. Hover over the target option group title to reveal the **preset icon**
4. Click the preset icon
5. Select **"Add New Preset"** or **"New Preset From Current Styles"**
6. Name the preset descriptively (e.g., "Section Heading H2", "Primary Button", "Card Background")
7. Adjust settings if needed
8. Click **"Save Preset"**

## Applying an Option Group Preset

1. Open any element's settings
2. Navigate to the relevant option group in the Design tab
3. Hover the option group title and click the **preset icon**
4. Select a preset from the dropdown list

## Management Actions

| Action | Icon | Description |
|--------|------|-------------|
| Edit | Gear | Open and modify the preset's settings; changes apply site-wide |
| Update from current | Arrow | Overwrite the preset with the element's current static styles |
| Duplicate | Copy | Clone the preset as a starting point for a variation |
| Delete | Trash | Remove the preset permanently |
| Set as default | Star | Make the preset the default for this option group on new elements |

## Design System Patterns

Option group presets work best when organized around a consistent design vocabulary:

| Pattern | Examples | Description |
|---------|----------|-------------|
| Heading scale | H1 Preset, H2 Preset, H3 Preset | Typography presets matching your typographic hierarchy |
| Button variants | Primary Button, Secondary Button, Ghost Button | Button style presets for different emphasis levels |
| Spacing rules | Section Large, Section Medium, Card Padding | Consistent spacing applied via preset |
| Card surfaces | Card Background, Dark Card, Elevated Card | Background + shadow combinations for card-like elements |

## Best Practices

- Keep each preset focused on a single function — avoid bundling unrelated settings
- Create presets after you notice two or more elements sharing the same styles
- Set core typography and button presets as defaults so new elements start consistently
- Use descriptive names reflecting the role, not the specific values

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Option group presets are stored separately from element presets. They are likely serialized in `wp_options` or a custom post type, with each preset containing the option group type, name, and a settings object. The exact storage key and data format need verification.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Divi REST API or `wp_options` query | Needs Testing | Presets likely stored as serialized arrays keyed by option group type |
| Modify | Divi REST API or `update_option()` | Needs Testing | Editing a preset should update all elements using it on next render |
| Create | Divi REST API or `update_option()` | Needs Testing | Must specify the option group type, name, and settings values |

<!-- TODO: Verify storage format — is it one option key per preset type or a single serialized array? -->
<!-- TODO: Confirm how presets are referenced in layout JSON (by ID? by name?) -->

## Related

- [Stacked & Nested Presets](stacked-nested-presets.md) — Layering multiple presets on one element
- [Preset Manager](preset-manager.md) — Centralized interface for managing all presets
- [Presets](presets.md) — Element-level presets overview
- [Design Variables](design-variables.md) — Variables that can be used within presets
