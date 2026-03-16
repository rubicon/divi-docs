---
title: "Extend Attributes"
category: builder
tags: ["builder", "extend-attributes", "extend-styles", "propagate", "workflow"]
related: ["attribute-management", "presets", "find-and-replace"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11550066"
---

# Extend Attributes

Propagate any attribute or collection of attributes from one element to many others across a defined scope, making sweeping design changes in a single action.

## Overview

Extend Attributes takes the concept of copy-paste styling and scales it to bulk operations. Instead of pasting attributes to each element individually, you choose a source element, define a target scope (same group, same column, same row, same section, or entire page), filter by element type, and select which attributes to propagate. Every matching element within the scope receives the specified attributes instantly.

This is the most efficient tool for making site-wide or section-wide design changes, such as updating all button styles in a section, applying consistent spacing to every module on a page, or propagating a preset across all elements of a specific type.

For the official Elegant Themes documentation, see [Extend Attributes](https://help.elegantthemes.com/en/articles/11550066).

## Accessing Extend Attributes

| Method | Steps |
|--------|-------|
| Right-click element | Right-click any element on the canvas and select **Extend Attributes** |
| Three-dot menu | Click the three-dot action icon on any section, row, or module |
| Option group level | Right-click an option group label in settings and choose **Extend Styles** |
| Field level | Right-click an individual field in settings to extend just that field's value |

When accessed from an option group or field, the Extend Attributes panel opens pre-configured with that group or field selected.

## Configuration Options

The Extend Attributes panel presents six configuration steps:

### 1. Extend From (Source Element)

| Setting | Type | Description |
|---------|------|-------------|
| Source Element | Dropdown / On-page selection | The element whose attributes will be propagated. Auto-selected when you right-click an element first. You can also click any element on the page while the panel is open to change the source. |

The panel is context-aware: it automatically switches source context as you click different modules on the page.

### 2. Extend To Location (Scope)

| Scope | Description |
|-------|-------------|
| Same Group | Only elements within the same Module Group container |
| Same Column | All matching elements in the same column |
| Same Row | All matching elements in the same row |
| Same Section | All matching elements in the same section |
| Entire Page | All matching elements on the entire page |

Choose the narrowest appropriate scope. For example, if you are styling modules on a dark background section, extend only within that section to avoid applying dark-mode styles to light sections.

### 3. Extend To Element Type (Target Filter)

| Setting | Type | Description |
|---------|------|-------------|
| Element Type | Multi-select dropdown | Filter targets by specific module types (e.g., only Buttons, only Blurbs) or element categories (e.g., all containers). Leave unfiltered to target all elements within scope. |

This filter is useful for extending attributes like button styles from a Contact Form module to all other modules that contain buttons.

### 4. Attribute Type

| Type | Description |
|------|-------------|
| Styles | Modified inline style values (colors, spacing, borders, etc.) |
| Content | Content values (text, images, links) |
| Presets | Preset assignments |
| Combinations | Any mix of the above categories |

### 5. Option Group

| Setting | Type | Description |
|---------|------|-------------|
| Option Group | Dropdown | Narrow the extension to a specific option group (e.g., only Border, only Spacing, only Button styles). Pre-selected when accessed from a group right-click. |

### 6. Fields

| Setting | Type | Description |
|---------|------|-------------|
| Fields | Searchable dropdown | Select individual fields to extend. Lists all modified settings from the source element. Pre-selected when accessed from a field right-click. |

## Workflow Summary

1. Select or right-click the source element.
2. Open Extend Attributes from the context menu.
3. Define the target scope (column, row, section, or page).
4. Optionally filter by element type.
5. Select the attribute category (styles, content, presets, or a combination).
6. Optionally narrow to a specific option group or individual fields.
7. Execute the extension.

## Common Use Cases

### Uniform Button Styling Across a Section

1. Style one button with the desired design.
2. Right-click and select **Extend Attributes**.
3. Set scope to **Same Section**.
4. Filter element type to **Button** modules.
5. Select **Styles** as the attribute type.
6. All buttons in the section receive the same styling.

### Propagating Spacing Values Page-Wide

1. Configure padding and margin on one module.
2. Right-click the **Spacing** option group and select **Extend Styles**.
3. Set scope to **Entire Page**.
4. Filter to the relevant module type.
5. Spacing values are applied to all matching modules on the page.

### Applying a Preset to All Modules in a Row

1. Apply a preset to one module.
2. Right-click and extend attributes.
3. Set scope to **Same Row**, attribute type to **Presets**.
4. All modules in the row receive the preset assignment.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Extended Attributes Not Applying to Some Elements"
    If certain elements are not receiving the extended attributes, they may not support the attribute type being extended. For example, extending button-specific styles to a Text module will have no effect on button-related fields the Text module does not have.

!!! warning "Unintended Changes Across Page"
    If the scope is set too broadly (e.g., Entire Page when only Same Section was intended), use Undo (Cmd/Ctrl + Z) immediately to revert. Always verify the scope before executing.

## Related

- [Attribute Management](attribute-management.md)
- [Find and Replace](find-and-replace.md)
- [Presets](presets.md)
- [Multi-Select & Bulk Editing](multi-select-bulk-editing.md)
