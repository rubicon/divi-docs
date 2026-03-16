---
title: "Find & Replace Attributes"
category: builder
tags: ["builder", "find-replace", "attributes", "bulk-editing", "workflow"]
related: ["copy-paste-attributes", "right-click-menus"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13342542"
---

# Find & Replace Attributes

Swap a design value for another across a module, section, or entire page in a single operation.

## Overview

The Find & Replace Attributes feature lets you identify a specific design value -- a color, font size, spacing value, border radius, or any other numeric/color field -- and replace every matching instance across a chosen scope. Instead of manually editing dozens of elements one by one, you define the swap once and Divi applies it everywhere it finds a match. For the official Elegant Themes reference, see [Find & Replace Attributes](https://help.elegantthemes.com/en/articles/13342542){:target="_blank"}.

This is one of the fastest ways to handle rebranding, design system migrations, and consistency cleanup.

## How to Access Find & Replace

1. Click any element to open its settings (or click the gear icon).
2. Locate the specific field that contains the value you want to replace.
3. Right-click the field, or click the three-dot menu icon next to it.
4. Select **Find & Replace** from the context menu.

The Find & Replace modal opens with the **Source Element** and **Find Value** fields pre-populated based on where you right-clicked.

## The Find & Replace Dialog

| Field | Description |
|-------|-------------|
| **Source Element** | The element you right-clicked. Auto-populated. |
| **Find Value** | The current value to search for (e.g., `#2ea3f2`, `16px`, `20px`). Auto-populated from the field you selected. |
| **Replace Value** | The new value to substitute wherever the find value is matched. |
| **Location (Scope)** | Where to apply the replacement (see Scope Options below). |
| **Element Type** | Filter which element types are affected (see Element Type Filtering below). |
| **Only Replace Identical Fields** | When enabled, only replaces values in fields of the same type as the source field. |

## Scope Options

The **Location** dropdown controls how broadly the replacement is applied:

| Scope | Description |
|-------|-------------|
| **Entire Page** | All matching values across every element on the page. |
| **Current Element** | Only within the selected element itself. |
| **Current Element & Children** | The selected element plus its direct child elements. |
| **Current Element & Descendants** | The selected element plus all nested elements at every depth. |
| **Parent Column** | All sibling elements within the same column. |
| **Parent Row** | All sibling elements within the same row. |
| **Parent Section** | All sibling elements within the same section. |

## Element Type Filtering

Narrow the replacement to specific element categories:

| Filter | Targets |
|--------|---------|
| **All Elements** | Sections, rows, columns, and modules. |
| **All Modules** | Only modules (excludes layout containers). |
| **All Containers** | Only columns, rows, sections, and groups. |
| **Column** | Only column elements. |
| **Row** | Only row elements. |
| **Section** | Only section elements. |

## The "Only Replace Identical Fields" Option

This is an important safety toggle. When **enabled**, Divi only replaces values in fields that are the same type as the source field. For example, if you right-clicked a border-radius field with value `10px`, the replacement will only touch other border-radius fields -- not margin, padding, or font-size fields that might also happen to contain `10px`.

When **disabled**, any field containing the matching value is replaced regardless of field type.

!!! tip "Enable This for Safety"
    Leave "Only Replace Identical Fields" enabled unless you specifically need cross-field replacement. This prevents accidental changes to unrelated settings that happen to share the same numeric value.

## Replaceable Value Types

Find & Replace works with any design value stored in element settings:

| Category | Examples |
|----------|----------|
| **Colors** | Hex (`#ff6600`), RGB, HSL, and global color variables. |
| **Typography** | Font size, line height, letter spacing. |
| **Spacing** | Margin, padding, gap values. |
| **Borders** | Border width, border radius. |
| **Shadows** | Box shadow offsets and blur/spread values. |
| **Other Numeric** | Any numeric design field. |

## Practical Use Cases

### Rebranding: Replacing a Primary Color

1. Right-click any element using the old brand color.
2. Select **Find & Replace** on the color field.
3. Set the replacement to the new brand color.
4. Set scope to **Entire Page**.
5. Leave "Only Replace Identical Fields" disabled (colors are safe to replace globally).
6. Click Replace. Every instance of the old color is updated.

### Standardizing Inconsistent Spacing

1. Identify a padding value that should be uniform (e.g., `30px`).
2. Right-click the field and select **Find & Replace**.
3. Set the find value to the inconsistent value (e.g., `28px`).
4. Set the replace value to `30px`.
5. Scope to the section or page as needed.

### Migrating Static Values to Variables

1. Right-click a field using a hardcoded color value.
2. Select **Find & Replace**.
3. Replace the hardcoded value with a global design variable reference.
4. Scope to **Entire Page** to migrate all instances at once.

## Version Notes

!!! note "Divi 5 Only"
    Find & Replace Attributes is a Divi 5 feature. Divi 4 does not offer field-level find and replace for design values.

## Related

- [Copy & Paste Attributes](copy-paste-attributes.md) -- Transfer attributes between specific elements
- [Right-Click Menus](right-click-menus.md) -- Where Find & Replace is accessed
- [Element Presets](element-presets.md) -- An alternative approach to consistent styling
- [Multi-Select & Bulk Editing](multi-select-bulk-editing.md) -- Another bulk workflow
