---
title: "Form Field Content Options"
category: options-groups
tags: ["options-groups", "form-field-content", "advanced"]
related: ["fields", "spam-protection"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10272945"
---

# Form Field Content Options

The Form Field Content options group manages the content, type, and validation rules for individual form fields within the Contact Form module.

## Overview

Each form field inside the Divi 5 Contact Form module has its own content settings that determine what kind of input it collects, how that input is validated, and whether the field is required. These settings are accessed by clicking on an individual field within the Contact Form module's settings panel.

The group is organized into three sections. The Text section handles identification, letting you assign a unique Field ID and a visible title label. The Field Options section controls the input type (plain text, email, textarea, checkboxes, radio buttons, or dropdown), character length limits, and which character types are allowed. The Conditional Logic section lets you show or hide a field based on the values entered in other fields, enabling dynamic forms that adapt to user input.

Conditional logic supports both "all conditions must match" and "any condition can match" evaluation modes, giving you flexibility in how rules combine. This is useful for creating multi-step forms where later fields appear only after specific earlier selections are made.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10272945).

## Settings Reference

### Text

| Setting | Type | Description |
|---------|------|-------------|
| Field ID | Text input | Assigns a unique identifier to the field. Restricted to alphanumeric characters and underscores. Used to reference the field in conditional logic rules and form processing. |
| Title | Text input | Sets the visible label displayed above or beside the form field. |

### Field Options

| Setting | Type | Description |
|---------|------|-------------|
| Field Type | Dropdown | Determines what kind of input the field accepts. Options are Input (single-line text), Email (validated email address), Textarea (multi-line text), Checkboxes (multiple selections), Radio Buttons (single selection from options), and Select Dropdown (single selection from a dropdown list). |
| Minimum Length | Numeric input | Sets the minimum number of characters required in the field. Submissions with fewer characters will be rejected. |
| Maximum Length | Numeric input | Sets the maximum number of characters allowed in the field. Input beyond this limit will be prevented or rejected. |
| Allowed Symbols | Dropdown | Restricts the types of characters that can be entered. Options are Letters Only, Numbers Only, and Alphanumeric (letters and numbers). |
| Required Field | Toggle | When enabled, the field must be filled out before the form can be submitted. Leaving it empty will trigger a validation error. |

### Conditional Logic

| Setting | Type | Description |
|---------|------|-------------|
| Enable | Toggle | Activates conditional logic for this field. When enabled, the field will only appear if the specified conditions are met. |
| Relation | Dropdown | Determines how multiple conditions are evaluated. "All" requires every condition to be true; "Any" requires at least one condition to be true. |
| Rules | Rule builder | Defines the conditions that control this field's visibility. Each rule references another field's value and a comparison operator. |

## Which Elements Use This

The Form Field Content options group is used by individual fields within the **Contact Form Module** in Divi 5. Each field added to a contact form has its own independent set of these content options.

## Code Examples

```css
/* Style required field labels differently */
.et_pb_contact_form .et_pb_contact_field.et_pb_required_field label {
  font-weight: 700;
}

.et_pb_contact_form .et_pb_contact_field.et_pb_required_field label::after {
  content: " *";
  color: #e53e3e;
}
```

```css
/* Style the select dropdown to match other field types */
.et_pb_contact_form select {
  appearance: none;
  background-image: url("data:image/svg+xml,...");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 40px;
}
```

## Related

- [Fields Options](fields.md)
- [Spam Protection Options](spam-protection.md)
