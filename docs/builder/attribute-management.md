---
title: "Attribute Management"
category: builder
tags: ["builder", "attributes", "copy-paste", "reset", "workflow"]
related: ["extend-attributes", "find-and-replace", "presets"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11401198"
---

# Attribute Management

Copy, paste, and reset element attributes at the field, group, tab, or element level for efficient design consistency across your layout.

## Overview

Divi 5's attribute management system provides granular control over how you transfer and reset styling, content, and presets between elements. Rather than copying an entire element, you can selectively copy just the design attributes, just the content, or just the presets, and paste them onto a different element. The system works at multiple levels of specificity: individual fields, option groups, settings tabs, or the entire element.

This is particularly valuable during rebranding workflows, when applying consistent styling across many elements, or when you want to transfer the design of one module to a completely different module type. Divi automatically matches compatible attributes and skips any that do not apply to the target element.

For the official Elegant Themes documentation, see [Attribute Management](https://help.elegantthemes.com/en/articles/11401198).

## Copy Attributes

To copy attributes from an element, right-click the element on the canvas or in the Layers View and select **Copy Attributes**. This captures the element's content, presets, and modified style values.

You can also copy at a more granular level by right-clicking within the settings panel:

| Copy Level | How to Access | What It Captures |
|------------|---------------|------------------|
| Entire element | Right-click element on canvas | All content, presets, and styles |
| Settings tab | Right-click a tab header in the settings panel | All attributes within that tab (Content, Design, or Advanced) |
| Option group | Right-click an option group label | All attributes within that specific group (e.g., Border, Spacing) |
| Individual field | Right-click a specific setting field | The value of that single field |

## Paste Attributes

After copying, right-click the target element and hover over **Paste Attributes** to see the available paste options:

| Option | Description |
|--------|-------------|
| Paste All Attributes | Applies content, presets, and styles from the copied element |
| Paste Design Attributes | Applies presets and modified styles only; leaves content untouched |
| Paste Style Attributes | Applies modified style values only; does not change presets or content |
| Paste Content Attributes | Applies content values only (text, images, links); leaves design unchanged |
| Paste Presets | Applies preset assignments only; does not change inline styles or content |

### Pasting to Specific Groups

You can also paste at the option group level. Right-click on an individual option group within the target element's settings panel to paste attributes into just that group. This is useful when you only want to transfer border styles or spacing values without affecting other design properties.

### Cross-Module Compatibility

When pasting between different module types (e.g., from a Blurb to a Call to Action), Divi matches compatible attributes automatically and ignores any that do not exist on the target module. This means you can safely paste design attributes from any module to any other module without causing errors.

## Reset Attributes

Right-click an element, option group, or field and choose from the reset options:

| Option | Description |
|--------|-------------|
| Reset All Attributes | Clears content, presets, and all modified styles, returning the element to its default state |
| Reset Design Attributes | Clears presets and modified styles; leaves content intact |
| Reset Style Attributes | Clears modified style values only; preserves presets and content |
| Reset Content Attributes | Clears content values only; leaves design unchanged |
| Reset Presets | Removes preset assignments only; inline styles and content remain |

Reset operations can be performed at the same levels as copy: entire element, tab, option group, or individual field.

## Keyboard Shortcuts

| Action | Mac | Windows |
|--------|-----|---------|
| Copy Attributes | Cmd + Shift + C | Ctrl + Shift + C |
| Paste Attributes | Cmd + Shift + V | Ctrl + Shift + V |
| Reset Attributes | Cmd + Shift + R | Ctrl + Shift + R |

These shortcuts operate on the currently selected element and apply the "All Attributes" variant by default.

## Common Workflows

### Consistent Button Styling

1. Design one button with the desired colors, borders, and spacing.
2. Right-click the button and select **Copy Attributes**.
3. Select each additional button, right-click, and choose **Paste Design Attributes**.
4. Each button retains its own text and link but receives the copied design.

### Rebranding Color Updates

1. Update one module with the new brand colors.
2. Copy the design attributes.
3. Paste Design Attributes onto similar modules across the page.
4. For broader changes, consider using [Extend Attributes](extend-attributes.md) or [Find and Replace](find-and-replace.md).

### Selective Group Transfer

1. Configure the Border settings on one element.
2. Right-click the **Border** option group and copy it.
3. On the target element, right-click the **Border** option group and paste.
4. Only border values transfer; all other settings remain unchanged.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Pasted Attributes Not Applying"
    If pasted attributes appear to have no effect, the source and target modules may not share compatible settings for the selected paste type. Try using "Paste Design Attributes" or "Paste Style Attributes" for a more targeted transfer.

!!! warning "Keyboard Shortcut Conflict"
    If the keyboard shortcuts do not work, check for browser extension or OS-level shortcut conflicts with Cmd/Ctrl + Shift + C/V/R.

## Related

- [Extend Attributes](extend-attributes.md)
- [Find and Replace](find-and-replace.md)
- [Presets](presets.md)
- [Multi-Select & Bulk Editing](multi-select-bulk-editing.md)
