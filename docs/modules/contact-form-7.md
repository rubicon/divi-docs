---
title: "Contact Form 7"
description: "Divi 5 Contact Form 7 module — embed Contact Form 7 forms in the builder and style them with Divi’s harmonized form field design tools, presets, and pseudo-class editing."
category: modules
tags: ["modules", "forms", "interactive", "contact-form-7", "cf7", "third-party", "wordpress-plugins"]
related: ["contact-form", "email-optin", "login"]
divi_version: "5.x"
last_updated: 2026-04-21
source_url: "https://www.elegantthemes.com/blog/theme-releases/new-form-options-field-presets-focus-editing-and-cf7-module"
---

# Contact Form 7

The Contact Form 7 module embeds forms created with the free [Contact Form 7](https://wordpress.org/plugins/contact-form-7/) WordPress plugin and styles them using the same **Input**, **Checkbox**, and **Radio** design groups, **pseudo-class editing** (`:focus`, `:checked`), and **form field presets** as Divi’s other form-based modules.

!!! abstract "Quick Reference"
    **What it does:** Renders a selected CF7 form inside a Divi block and exposes full Visual Builder styling for field types and states.
    **When to use it:** You already use Contact Form 7 for submissions, mail tags, add-ons, or non-Divi workflows and want Divi-level design control.
    **Key setup:** Install and activate Contact Form 7 → create forms in **Contact → Contact Forms** → pick the form in the module.
    **ET announcement:** [Better Form Styling, Field Presets, Focus Editing, And CF7 Module for Divi 5](https://www.elegantthemes.com/blog/theme-releases/new-form-options-field-presets-focus-editing-and-cf7-module){:target="_blank"}

!!! note "Same wording as Divi customer email (April 2026)"
    Elegant Themes describes harmonizing field options across **all form-based modules** with better styling for **radio buttons and checkboxes**; **:focus** and **:checked** editing modes alongside hover; **presets** on the **Input**, **Checkbox**, and **Radio** groups so forms share one modular design system; and this **Contact Form 7** module so you can render and style CF7 forms with Divi’s full design suite—the **first of many** integration modules.

!!! tip "When to Use This Module"
    - You rely on Contact Form 7 features (mail tags, Flamingo, reCAPTCHA integration, third-party CF7 extensions).
    - You are migrating existing CF7 forms and want to keep the same form definitions while rebuilding the page in Divi 5.

!!! warning "When NOT to Use This Module"
    - For simple site contact flows with no CF7 dependency → the native [Contact Form](contact-form.md) module is self-contained and does not require an extra plugin.

## Overview

Divi 5.2+ adds a **first-party** Contact Form 7 module as part of Elegant Themes’ push toward **integration-based modules**—bringing popular plugins into the builder with native blocks. The module does not replace Contact Form 7; it **displays** a form you build in the CF7 admin and connects Divi’s design layer to that markup.

Form behavior (validation, email delivery, messages) continues to be handled by Contact Form 7 and your WordPress environment. Divi controls layout and styling: harmonized **Input**, **Checkbox**, and **Radio** option groups, full access to Divi’s design controls (including [Composable Settings](../builder/composable-settings-in-divi-5.md) where applicable), **focus** and **checked** editing modes, and **presets** for each field-type group so forms stay consistent across modules.

<!-- ![Contact Form 7 module overview](../assets/screenshots/modules/contact-form-7/overview.png){ loading=lazy }
*TODO: Screenshot — module on canvas with CF7 form selected.* -->

## Prerequisites

1. **Divi 5** updated to a build that includes the Contact Form 7 module (see the [release announcement](https://www.elegantthemes.com/blog/theme-releases/new-form-options-field-presets-focus-editing-and-cf7-module){:target="_blank"}).
2. **Contact Form 7** installed from [WordPress.org](https://wordpress.org/plugins/contact-form-7/) and **activated**.
3. At least **one CF7 form** created under **Contact → Contact Forms** in the WordPress admin.

## How to Add the Contact Form 7 Module

1. Open the **Visual Builder** on the page or template you want to edit.
2. Click **+** to insert a module.
3. Search for **Contact Form 7** (or browse the **Forms** category) and insert the module.
4. In the module’s **Content** tab, choose the **form** to display from the list of CF7 forms.
5. Use the **Design** tab to style inputs, checkboxes, radios, labels, placeholders, and state-specific styles (including **:focus** and **:checked**).

For how the shared form styling system works across modules, see [Form field design (Input, Checkbox, Radio)](../options-groups/fields.md).

## Settings & Options

### Content Tab

| Setting | Type | Description |
|---------|------|-------------|
| Form | select | The Contact Form 7 form to render. Options are populated from **Contact → Contact Forms**. |

Additional standard Content options (background, link, etc.) match other Divi modules where exposed.

### Design Tab

Styling follows the **harmonized form field model** introduced in the April 2026 update:

- **Input** — text fields, textareas, selects, and similar controls.
- **Checkbox** — checkbox inputs and their labels.
- **Radio** — radio inputs and their labels.

Each group supports Divi’s full design toolkit, **pseudo-class editing** (including **:focus** and **:checked** alongside hover), and **presets** so you can reuse the same field styling site-wide. Label and placeholder text also receive dedicated styling controls within these groups.

See [Fields / form field design](../options-groups/fields.md) and [Divi Presets](../builder/presets.md) for concepts; exact control names match the current Visual Builder for your Divi version.

### Advanced Tab

Standard Divi **Advanced** options ([Attributes](../options-groups/attributes.md), [CSS](../options-groups/css.md), [Conditions](../options-groups/conditions.md), interactions, visibility, etc.) apply to the module wrapper like other modules.

## Code Examples

Styling is normally handled in the builder. For edge cases, target CF7 markup with care—classes can differ by form structure. Prefer Divi field groups before adding custom CSS.

```css
/* Example: reinforce focus visibility for CF7 fields inside Divi */
.et-db #et-boc .et-l .wpcf7 input:focus,
.et-db #et-boc .et-l .wpcf7 textarea:focus {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

## Troubleshooting

!!! warning "Module does not appear in the module list"
    Update Divi to the latest version. The Contact Form 7 module ships with Divi; it is not the legacy third-party [Divi Contact Form 7](https://www.elegantthemes.com/marketplace/divi-contact-form-7/) marketplace product (different product).

!!! warning "Form list is empty"
    Confirm **Contact Form 7** is activated and that you have created at least one form under **Contact → Contact Forms**.

!!! warning "Emails or validation behave unexpectedly"
    Divi styles the form; **submission behavior is entirely CF7’s**. Check CF7’s **Mail** tab, spam plugins, SMTP configuration, and JavaScript conflicts in the browser console.

## Related

- [Contact Form](contact-form.md) — Native Divi form module (no CF7 required).
- [Form Field Content](../options-groups/form-field-content.md) — Per-field content and validation (native Contact Form module).
- [Form field design](../options-groups/fields.md) — Input / Checkbox / Radio groups, focus and checked modes, presets.
- [Spam Protection](../options-groups/spam-protection.md) — Native Contact Form spam options (CF7 uses its own integrations).

**Block identifier:** `divi/contact-form-7` — *Confirm in layout JSON / block inserter for your Divi build.*
