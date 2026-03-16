---
title: "Fields Options"
description: "Divi 5 Fields options group — background, text colors, typography, spacing, borders, and focus-state styling for form inputs."
category: options-groups
tags: ["options-groups", "fields", "advanced"]
related: ["form-field-content", "spam-protection", "button"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10260887"
---

# Fields Options

The Fields options group controls the visual styling of form input fields, including their colors, typography, spacing, and borders.

!!! abstract "Quick Reference"
    **What it controls:** Field background/text colors, focus-state colors, typography, spacing, borders, and rounded corners
    **Where to find it:** Design Tab → Fields
    **Available on:** Comments module (and other form-based modules)
    **Responsive:** Yes — field styling values can be set per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10260887)

## Overview

When a module contains form inputs, such as text fields, textareas, or dropdowns, the Fields options group provides a comprehensive set of design controls for those inputs. These settings are found under the Design tab and allow you to customize every visual aspect of form fields so they match your site's branding without writing any custom CSS.

The group covers four main areas: background and text colors (including separate focus-state colors), typography (font family, weight, size, spacing, and style), spacing (margin and padding around each field), and borders (width, color, style, and rounded corners). Focus-state settings let you define how a field looks when a user clicks into it, providing clear visual feedback.

These settings apply to all input fields within the module simultaneously. If you need to style individual fields differently, you can use the CSS options group in combination with field-specific class names.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10260887).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Fields Background Color | Color picker | Sets the background color of form input fields in their default state. |
| Fields Text Color | Color picker | Sets the text color inside form input fields in their default state. |
| Fields Focus Background Color | Color picker | Sets the background color of a field when it receives focus (is clicked or tabbed into). |
| Fields Focus Text Color | Color picker | Sets the text color of a field when it receives focus. |
| Fields Margin | Spacing input | Controls the outer spacing around each form field. Supports individual values for top, right, bottom, and left. |
| Fields Padding | Spacing input | Controls the inner spacing within each form field. Supports individual values for top, right, bottom, and left. |
| Fields Font | Font selector | Sets the font family used for text inside form fields. |
| Fields Font Weight | Dropdown | Sets the weight (thickness) of the field text. Options include Light, Regular, Bold, and other standard weights. |
| Fields Font Style | Multi-select | Applies additional text styling such as italics, uppercase, underline, or strikethrough. |
| Fields Text Alignment | Alignment buttons | Controls horizontal text alignment within the field: left, center, right, or justify. |
| Fields Text Size | Range slider / numeric input | Sets the font size of text inside form fields. |
| Fields Letter Spacing | Numeric input | Adjusts the horizontal spacing between characters in field text. |
| Fields Line Height | Numeric input | Sets the vertical spacing between lines of text within form fields. |
| Fields Text Shadow | Shadow controls | Adds a text shadow to field text with configurable position, blur radius, and color. |
| Fields Rounded Corners | Numeric input | Sets the border radius for field corners. Can be linked (uniform) or unlinked (individual corners). |
| Fields Border Width | Numeric input | Sets the thickness of the field border. Minimum value is 1px. |
| Fields Border Color | Color picker | Sets the color of the field border. |
| Fields Border Style | Dropdown | Sets the border style. Options are solid, dashed, dotted, double, groove, ridge, inset, outset, and none. |
| Use Focus Borders | Toggle | When enabled, allows you to define separate border styles for when a field is in focus. |

## Which Elements Use This

The Fields options group is currently used by the **Comments Module** in Divi 5. It appears under the **Design** tab in the module's settings panel.

## Code Examples

```css
/* Custom focus styles for form fields */
.et_pb_comments_module input:focus,
.et_pb_comments_module textarea:focus {
  border-color: #4299e1;
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.2);
  outline: none;
}
```

```css
/* Style placeholder text to match field design */
.et_pb_comments_module input::placeholder,
.et_pb_comments_module textarea::placeholder {
  color: #a0aec0;
  font-style: italic;
}
```

## Related

- [Form Field Content Options](form-field-content.md)
- [Spam Protection Options](spam-protection.md)
- [Button Options](button.md)
