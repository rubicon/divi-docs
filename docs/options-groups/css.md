---
title: "CSS Options"
category: options-groups
tags: ["options-groups", "css", "advanced"]
related: ["attributes", "visibility"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102722"
---

# CSS Options

The CSS options group provides direct access to write custom CSS for any element, allowing fine-grained styling that goes beyond the built-in design controls.

## Overview

Divi 5 includes two distinct methods for applying custom CSS to an element: Free-Form CSS and Module Elements CSS. Both are located under the Advanced tab, and each serves a different purpose depending on how much control you need.

Free-Form CSS accepts complete CSS rule blocks, including selectors and multiple property declarations. You use the `selector` keyword as a placeholder for the current element, which Divi replaces with the actual CSS selector at render time. This approach is ideal when you need to write complex rules, target pseudo-classes, or apply multiple styles in a single block.

Module Elements CSS provides individual input fields for specific parts of a module, such as its title, body text, button, or image. These fields accept only CSS property declarations (not full rule blocks), making them simpler to use for targeted adjustments. Every module type exposes different element fields reflecting its internal structure, but three fields are always available: Before (the `::before` pseudo-element), Main Element, and After (the `::after` pseudo-element).

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102722).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Free-Form CSS | Code editor | Accepts complete CSS blocks with selectors. Use the `selector` keyword to target the current element. Supports multiple rules, pseudo-classes, and media queries. |
| Before | CSS declaration input | Applies CSS property declarations to the element's `::before` pseudo-element. Available on all module types. |
| Main Element | CSS declaration input | Applies CSS property declarations directly to the primary module wrapper element. Available on all module types. |
| After | CSS declaration input | Applies CSS property declarations to the element's `::after` pseudo-element. Available on all module types. |
| Module-Specific Elements | CSS declaration inputs | Additional fields that vary by module type (e.g., Title, Body, Button, Image). Each field targets a specific sub-element within the module and accepts property declarations only. |

## Which Elements Use This

All modules, columns, rows, and sections in the Divi 5 Visual Builder include the CSS options group. The settings are found under the **Advanced** tab.

## Code Examples

Free-Form CSS using the `selector` keyword:

```css
selector {
  border: 2px solid #333;
  transition: transform 0.3s ease;
}

selector:hover {
  transform: scale(1.05);
}
```

Module Elements CSS (declaration-only, no selector needed):

```css
/* In the "Title" field of a Blurb module */
font-size: 24px;
color: #2d3748;
text-transform: uppercase;
```

Using the `::before` pseudo-element field to add a decorative accent:

```css
/* In the "Before" field */
content: "";
display: block;
width: 50px;
height: 3px;
background-color: #4299e1;
margin-bottom: 15px;
```

## Related

- [Attributes Options](attributes.md)
- [Visibility Options](visibility.md)
