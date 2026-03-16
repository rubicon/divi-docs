---
title: "Stacked & Nested Presets"
description: "Divi 5 stacked and nested presets — layer multiple presets on one element and embed option group presets inside element presets for composable design."
category: builder
tags: [builder, presets, stacked-presets, nested-presets, design-system, inheritance]
related: [option-group-presets, preset-manager, presets]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12817235"
---

# Stacked & Nested Presets

Stacked presets let you apply multiple presets to a single element, while nested presets let you embed option group presets inside element presets — enabling layered, composable design systems in Divi 5.

!!! abstract "Quick Reference"
    **What it does:** Combines multiple presets on one element (stacking) and embeds option group presets within element presets (nesting).
    **Where to find it:** Element settings → Module Preset icon for stacking; Element preset editor for nesting.
    **Key features:**

    - Stacked presets apply in order; later presets override overlapping properties
    - Nested presets bundle option group presets inside element presets for automatic application
    - Four-level priority: element preset → nested option group presets → stacked presets → element overrides
    - Changes to any preset in the chain cascade to all referencing elements

    **ET Docs:** [Stacked & Nested Presets](https://help.elegantthemes.com/en/articles/12817235){:target="_blank"}

## Overview

Basic preset usage assigns one preset to one element. Stacked and nested presets extend this model by allowing composition: you can layer multiple presets on a single element (stacking) and embed option group presets within element presets (nesting). Together, these features let you build modular design tokens that combine in predictable ways.

Stacking is order-dependent — presets are applied in sequence, and later presets override earlier ones where settings overlap. Nesting works by bundling option group presets into element presets, so applying one element preset also applies all its nested option group presets. Changes to any preset in the chain cascade to every element that references it.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12817235).

## Stacked Presets

Stacked presets apply more than one preset to an element or option group. This is useful when you want to combine a base style with context-specific adjustments.

### How Stacking Works

| Concept | Description |
|---------|-------------|
| Application order | Presets are applied in the order they are added |
| Override behavior | When two presets define the same setting, the later preset wins |
| Non-overlapping settings | Settings defined in only one preset apply without conflict |
| Cascading updates | Changes to any stacked preset propagate to all elements using that stack |

### Stacking Workflow

1. Open an element's settings in the Visual Builder
2. Click the **Module Preset icon** in the settings panel
3. Select a first preset from the list
4. Select additional presets — they are added in order
5. If presets conflict on the same setting, the last-added preset takes precedence
6. Adjust the order if needed to control which preset has priority

### Use Cases for Stacking

| Pattern | Description |
|---------|-------------|
| Base + context | Apply a "Card Base" preset, then stack a "Dark Mode Card" preset that only overrides background and text color |
| Typography + spacing | Stack a heading typography preset with a spacing preset for consistent but separate control |
| Shared core + variant | Layer a core button preset with a "Large" or "Small" size variant |

## Nested Presets

Nested presets place option group presets inside element presets. When you apply the element preset, all its nested option group presets are applied automatically.

### How Nesting Works

| Concept | Description |
|---------|-------------|
| Composition | An element preset can include one or more option group presets |
| Automatic application | Applying the element preset applies all nested option group presets |
| Independent editing | Editing a nested option group preset updates everywhere it is used — both standalone and inside element presets |
| Cascading changes | Updates to a nested preset propagate through the parent element preset to all elements using it |

### Nesting Workflow

1. Create the option group presets you want to embed (e.g., a Typography preset and a Background preset)
2. Create or edit an element preset
3. Within the element preset settings, add the option group presets to the relevant option groups
4. Save the element preset
5. Apply the element preset to elements — the nested presets are applied automatically

## Inheritance and Priority

When stacked and nested presets are combined, Divi resolves settings in a predictable order:

1. **Element preset** base settings are applied first
2. **Nested option group presets** override matching settings within the element preset
3. **Stacked presets** are applied in sequence, with later presets overriding earlier ones
4. **Element-level overrides** (manual changes on the individual element) take highest priority

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Stacked presets are likely stored as an ordered array of preset IDs on the element. Nested presets are references within an element preset's data structure pointing to option group preset IDs. The exact format of these references needs verification.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Divi REST API or layout JSON inspection | Needs Testing | Look for an array of preset references on element attributes |
| Modify | Divi REST API or layout JSON update | Needs Testing | Changing the order of stacked presets changes which styles take priority |
| Create | Divi REST API or element preset editor | Needs Testing | Nested presets are added during element preset creation/editing |

<!-- TODO: Verify how stacked preset order is stored in the layout JSON -->
<!-- TODO: Test whether removing a nested option group preset from an element preset removes its styles from all dependent elements -->

## Related

- [Option Group Presets](option-group-presets.md) — The presets that can be stacked and nested
- [Preset Manager](preset-manager.md) — Centralized interface for managing all presets
- [Presets](presets.md) — Element-level presets overview
