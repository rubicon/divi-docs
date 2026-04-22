---
title: "Form Field Design (Input, Checkbox, Radio)"
description: "Divi 5 harmonized form field styling — Input, Checkbox, and Radio design groups, :focus and :checked pseudo-class editing, presets, and composable settings across form-based modules."
category: options-groups
tags: ["options-groups", "fields", "forms", "presets", "focus", "advanced"]
related: ["form-field-content", "spam-protection", "button", "contact-form"]
divi_version: "5.x"
last_updated: 2026-04-21
source_url: "https://www.elegantthemes.com/blog/theme-releases/new-form-options-field-presets-focus-editing-and-cf7-module"
---

# Form Field Design (Input, Checkbox, Radio)

Divi **harmonized field options across all form-based modules**: field styling is organized into **Input**, **Checkbox**, and **Radio** design groups, with **additional styling options** for radios and checkboxes that were previously inconsistent or unavailable. Together with **[Composable Settings](../builder/composable-settings-in-divi-5.md)**, you can use Divi’s full design suite on form elements instead of filling gaps with custom CSS.

!!! abstract "Quick Reference"
    **What it controls:** Visual design for text-like inputs, checkboxes, and radios — per state (default, hover, **:focus**, **:checked**).
    **Where to find it:** Design tab → **Input**, **Checkbox**, and **Radio** groups on form-based modules.
    **Pseudo-classes:** In addition to hover editing, use **:focus** and **:checked** modes for field-based pseudo-classes.
    **Presets:** Each of the three groups supports presets for site-wide consistency.
    **ET source:** [Feature announcement](https://www.elegantthemes.com/blog/theme-releases/new-form-options-field-presets-focus-editing-and-cf7-module){:target="_blank"} (aligns with Divi customer email, April 2026).

## Overview

Previously, many form-based modules exposed a single **Fields** (or similarly named) bucket with **inconsistent** controls—some modules offered one-off focus colors, others omitted label or placeholder styling, and radios and checkboxes could not be designed with the same depth as text inputs.

Current Divi 5 splits field design into three groups:

1. **Input** — single-line inputs, email fields, textareas, dropdowns (`select`), and related controls.
2. **Checkbox** — checkbox inputs and their labels.
3. **Radio** — radio inputs and their labels.

Each group receives the **same set of options** wherever that field type appears, and each can use Divi’s **full** background, border, spacing, typography, filters, transforms, and other design tools where enabled. **Label text** and **placeholder text** styling are available within these groups so you can tune copy independently from the field body.

For the original Help Center article that described the older consolidated **Fields** UI on some modules, see [Understanding fields styling](https://help.elegantthemes.com/en/articles/10260887){:target="_blank"} — behavior in current Divi follows the harmonized model above.

## Pseudo-class editing (`:focus`, `:checked`)

Divi already supported **hover** state customization for many elements. For forms, Divi added editing modes for **field-based pseudo-classes**:

| Mode | Typical use |
|------|-------------|
| **Default** | Resting appearance of the control. |
| **Hover** | Pointer-over styling (existing workflow). |
| **:focus** | When the visitor tabs or clicks into an input — keyboard and accessibility-friendly focus treatment. |
| **:checked** | Selected radio or checked checkbox. |

Earlier **focus-only** color pickers and similar shortcuts were **deprecated** and migrated into **:focus** editing mode so focus styling lives alongside other states instead of as disconnected toggles.

Switch pseudo-class modes from the same workflow you use for hover (Responsive Editor / state strip in the Visual Builder — see [Button styling reference](../modules/button-styling-reference.md) for the general hover pattern; form fields add **:focus** and **:checked** where applicable).

## Form field presets {#form-field-presets}

**Input**, **Checkbox**, and **Radio** groups **support presets**. Create a preset per group (for example, “Input / Default”, “Checkbox / Compact”) and reuse it across the [Contact Form](../modules/contact-form.md), [Contact Form 7](../modules/contact-form-7.md), [Email Optin](../modules/email-optin.md), [Login](../modules/login.md), [Search](../modules/search.md), [Comments](../modules/comments.md), WooCommerce checkout modules, and other **form-based** elements—adjust the preset once, and dependent modules pick up the base design.

See [Divi Presets](../builder/presets.md) for how presets propagate and override.

## Which elements use this

Any **form-based module** that renders text inputs, textareas, selects, checkboxes, or radios uses the harmonized groups. That includes (non-exhaustive):

- [Contact Form](../modules/contact-form.md), [Contact Form 7](../modules/contact-form-7.md), [Email Optin](../modules/email-optin.md), [Login](../modules/login.md), [Search](../modules/search.md), [Comments](../modules/comments.md)
- WooCommerce checkout and cart modules that expose native form fields (billing, shipping, coupons, etc.)

Exact group labels match the Visual Builder for your installed Divi version.

## Historical reference: legacy “Fields” table

The following table described the **pre-harmonization** consolidated **Fields** group as documented for the Comments module. **Current Divi may show Input / Checkbox / Radio instead**, with controls reorganized into pseudo-class modes and composable settings. Retained for migration context only:

| Setting | Type | Description |
|---------|------|-------------|
| Fields Background Color | Color picker | Default-state background for inputs. |
| Fields Text Color | Color picker | Default-state text color. |
| Fields Focus Background Color | Color picker | *(Superseded by :focus mode in harmonized UI.)* |
| Fields Focus Text Color | Color picker | *(Superseded by :focus mode in harmonized UI.)* |
| Fields Margin / Padding | Spacing | Outer/inner spacing for fields. |
| Fields Font, Weight, Style, Alignment, Size, Letter Spacing, Line Height, Text Shadow | Typography | Text inside fields. |
| Fields Rounded Corners | Numeric | Border radius. |
| Fields Border Width / Color / Style | Border | Border appearance. |
| Use Focus Borders | Toggle | *(Superseded by :focus border styling in harmonized UI.)* |

## Code Examples

Prefer builder presets and pseudo-class modes first; use CSS when you need selectors Divi does not expose.

```css
/* Example: stronger focus ring for comment form after migration from legacy Fields */
.et_pb_comments_module input:focus-visible,
.et_pb_comments_module textarea:focus-visible {
  outline: 2px solid #3182ce;
  outline-offset: 2px;
}
```

## Related

- [Form Field Content Options](form-field-content.md) — Field IDs, types, validation (native Contact Form)
- [Spam Protection Options](spam-protection.md) — reCAPTCHA and honeypot (native Contact Form)
- [Button Options](button.md) — Submit buttons on forms
- [Divi Presets](../builder/presets.md) — Preset manager and inheritance
