---
title: "New Form Field Options in Divi 5"
category: builder
tags: ["builder", "forms", "form-fields", "contact-form", "design"]
related: ["contact-form", "composable-settings"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14715602-new-form-field-options-in-divi-5"
---

# New Form Field Options in Divi 5

Divi 5 overhauls how you style form fields across every form-based module. Input, checkbox, and radio fields now have their own dedicated option groups, the same settings appear consistently across all form modules, and you can edit the **focus** and the **checked** states directly in the builder.

## Overview

## What Changed

![New form field options interface showing separated option groups.](../assets/screenshots/builder/new-form-field-options/overview.png){ loading=lazy }

The old **Field** group has been split into three separate groups:

- **Input**
- **Checkbox**
- **Radio**

Each field type now has its own complete set of design options.

The improvements allow:

- Every form-based module now shares the same field settings. No more one-off options that exist in one module but not another.
- Label text and placeholder text have dedicated settings in each group.
- Field groups work with **Composable Settings**, so you can enable additional design options on any field sub-element.
- Field groups support presets, so you can reuse a single design across every form on your site.
- A new Contact Form 7 module lets you render CF7 forms inside Divi and style them with the same field options.

## Where to Find the New Options

1. Open the settings of any form-based module: **Contact Form**, **Email Optin**, **Login**, **Comments**, or the new Contact Form 7 module.
2. Go to the **Design** tab.
3. Locate the **Input**, **Checkbox**, and **Radio** option groups.

Each group contains the full suite of Divi design options: background, text, spacing, border, sizing, box shadow, filters, and more.

## Input, Checkbox, and Radio Option Groups

![Form field options harmony across different field types.](../assets/screenshots/builder/new-form-field-options/field-options-harmony.png){ loading=lazy }

Each field type is now styled independently.

| Field Type | Description |
|---|---|
| **Input** | Controls single-line text inputs, email fields, number fields, textareas, and select menus. Includes settings for the field itself, label text, and placeholder text. |
| **Checkbox** | Controls checkbox fields. Includes settings for the checkbox, its label, and its checked state. |
| **Radio** | Controls radio button fields. Includes settings for the radio input, its label, and its checked state. |

Because these groups are separate, you can give checkboxes one style, radios another, and inputs a third—all inside the same form.

## Editing Focus and Checked States

![States selector showing focus and checked state editing options.](../assets/screenshots/builder/new-form-field-options/focus-checked-states.png){ loading=lazy }

Divi already supports the **hover state** editing on any module. Divi 5 adds two more editing modes for form fields:

- **focus** - The style applied when a user clicks or tabs into a field.
- **checked** - The style applied when a checkbox or radio is selected.

To edit a pseudo-class state:

1. Open the module settings and go to the option group you want to style (**Input**, **Checkbox**, or **Radio**).
2. Switch the editing mode from normal to **Focus** or **Checked** using the mode selector in the option group header.
3. Adjust any design option while in that mode. The change only applies to that state.

**Note**: Divi's older focus-specific design options have been deprecated. Existing values are automatically migrated to the new **focus state** editing mode.

## Form Field Presets

Form field groups now support **Divi's preset system**. You can create a preset for inputs, another for checkboxes, and another for radios, then apply them across every form-based module on your site.

To create a field preset:

1. Open a form-based module and go to the **Design** tab.
2. Open the **Input**, **Checkbox**, or **Radio** option group.
3. Configure the styles you want to reuse.
4. Save the configuration as a preset using the preset dropdown at the top of the group.

Any module that uses that preset will pick up the styling automatically. Edit the preset once, and every form updates.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Related

- [Contact Form Module](../modules/contact-form.md)
- [Composable Settings](composable-settings-in-divi-5.md)
- [Option Group Presets](advanced-styling-using-option-group-presets-in-divi-5.md)
- [Contact Form 7 Styler Module](../modules/the-contact-form-7-styler-module-in-divi-5.md)
