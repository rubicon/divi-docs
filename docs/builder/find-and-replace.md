---
title: "Find and Replace"
description: "Divi 5 Find and Replace — search for specific design values and replace them in bulk across an element, section, or entire page layout."
category: builder
tags: ["builder", "find-and-replace", "bulk-editing", "attributes", "workflow"]
related: ["attribute-management", "multi-select-bulk-editing", "extend-attributes"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11623616"
---

# Find and Replace

Search for specific attribute values across your layout and replace them in bulk, scoped to a single element, a section, or the entire page.

!!! abstract "Quick Reference"
    **What it does:** Finds a specific design value and replaces it with another across a chosen scope and element type filter.
    **Where to find it:** Right-click any field in element settings → Find & Replace.
    **Key features:**

    - Auto-populated source element and find value from the right-clicked field
    - Scope options: Current Element, Descendants, Parent Elements, Entire Page
    - Element type filter to restrict replacement to specific module or container types
    - "Only Replace Identical Fields" toggle to prevent cross-field value replacement

    **ET Docs:** [Find and Replace](https://help.elegantthemes.com/en/articles/11623616){:target="_blank"}

## Overview

Find and Replace in Divi 5 works like find-and-replace in a text editor, but for design attributes. You select a source field that contains the value you want to change, specify the replacement value, define how broadly the replacement should apply, and execute. This is invaluable for design system updates, rebranding tasks, migrating hard-coded values to Global Variables, and correcting repeated values across a layout.

Unlike [Extend Attributes](extend-attributes.md) which propagates values from one element to others, Find and Replace searches for a specific existing value and swaps it wherever it appears. This distinction matters: Extend sets a value regardless of what was there before, while Find and Replace only changes elements that currently have the matched value.

For the official Elegant Themes documentation, see [Find and Replace](https://help.elegantthemes.com/en/articles/11623616).

## Accessing Find and Replace

1. Open the settings of any element (click the gear icon or double-click the module).
2. Locate the field containing the value you want to find.
3. Right-click the field.
4. Select **Find & Replace** from the context menu.

The Find and Replace modal opens with the source element and find value pre-populated from the field you right-clicked.

## Modal Fields

| Field | Type | Description |
|-------|------|-------------|
| Source Element | Auto-populated | The element containing the original value. Identifies where the find value originated. |
| Find Value | Auto-populated / Editable | The current value to search for across the defined scope |
| Replace Value | Input | The new value that will replace every instance of the find value |

## Scope Options (Find and Replace Location)

Control how broadly the replacement applies:

| Scope | Description |
|-------|-------------|
| Current Element Only | Replace the value only within the selected element's settings |
| Current Element and Descendants | Replace the value in the selected element and all its child elements |
| Parent Elements | Replace the value in parent containers above the current element |
| Entire Page | Replace the value in every element on the page that contains the matching value |

## Element Type Filter

Narrow the replacement to specific element types within the defined scope:

| Filter | Description |
|--------|-------------|
| All Elements | No filtering; replacement applies to every matching element |
| Specific Modules | Restrict replacement to selected module types (e.g., only Buttons, only Text modules) |
| Container Elements | Restrict replacement to container types (Sections, Rows, Columns, Groups) |

## Identical Fields Filter

| Setting | Type | Description |
|---------|------|-------------|
| Only Replace Identical Fields | Toggle | When enabled, the replacement is restricted to fields of the same type as the source field. For example, if the find value comes from a border radius field, only other border radius fields with the matching value will be replaced. When disabled, any field containing the matching value will be replaced regardless of field type. |

This filter prevents unintended replacements. For example, if you are replacing a specific pixel value like `20px`, you probably want to replace it only in spacing fields, not in every field that happens to contain `20px` (such as a font size or border width).

## Workflow

1. Open the settings panel for an element containing the value you want to change.
2. Right-click the specific field.
3. Select **Find & Replace**.
4. Verify the pre-populated **Source Element** and **Find Value**.
5. Enter the **Replace Value** (the new value).
6. Set the **Location** scope (element, descendants, parent, or entire page).
7. Optionally filter by **Element Type**.
8. Optionally enable **Only Replace Identical Fields** to restrict by field type.
9. Click the replace button to execute.

## Common Use Cases

### Migrating to Global Variables

Replace a hard-coded color value (e.g., `#2D3748`) across the entire page with a Global Variable reference. This converts a static design to a variable-driven system in one action.

### Rebranding Color Updates

Find the old brand color and replace it with the new brand color across the entire page. Use the Element Type filter to target specific module types if the color is used differently in different contexts.

### Standardizing Spacing

Find a spacing value (e.g., `30px` padding) and replace it with a consistent value (e.g., `40px`) across all modules on the page. Enable **Only Replace Identical Fields** to ensure only padding fields are affected, not font sizes or other fields that might coincidentally use `30px`.

### Correcting Repeated Mistakes

If you accidentally set the wrong border radius on multiple elements, find the incorrect value and replace it with the correct one across the section or page.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Find and Replace is a builder-time operation that modifies block attributes in `post_content`. It does not store its own persistent data; instead, it reads and writes the `attrs` of blocks within the defined scope. The operation iterates over blocks, compares attribute values to the find value, and updates matches with the replace value.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | N/A — Find and Replace is a transient operation, not a stored data structure | Needs Testing | The operation itself is not persisted; only its results (modified block attrs) are saved |
| Modify | Replicate the behavior by iterating over blocks in `post_content`, comparing attr values, and replacing matches | Needs Testing | Must respect scope (element, descendants, page) and field type filtering logic |
| Create | Not applicable — Find and Replace is an action, not a data entity | N/A | To achieve similar bulk replacement programmatically, parse and walk the block tree |

!!! warning "Irreversible in Code"
    Unlike the builder UI which supports Undo, programmatic find-and-replace operations on `post_content` cannot be undone unless you preserve a backup of the original content before modifying it.

## Troubleshooting

!!! warning "Replacement Not Affecting Expected Elements"
    Check the scope setting. If set to "Current Element Only," the replacement will not propagate beyond the selected element. Expand the scope to "Entire Page" for site-wide changes.

!!! warning "Unintended Replacements"
    If the replacement affected fields you did not intend to change, you likely had **Only Replace Identical Fields** disabled. Use Undo (Cmd/Ctrl + Z) to revert and re-run with the filter enabled.

!!! warning "Find Value Not Matching"
    The find value must match exactly, including units. For example, `20px` will not match `20` or `20 px`. Verify the exact value by checking the source field.

## Related

- [Attribute Management](attribute-management.md)
- [Extend Attributes](extend-attributes.md)
- [Multi-Select & Bulk Editing](multi-select-bulk-editing.md)
- [Presets](presets.md)
