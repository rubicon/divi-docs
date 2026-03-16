---
title: "Where to Add Custom CSS"
category: troubleshooting
tags: ["troubleshooting", "css", "custom-css", "theme-options"]
related: ["fix-custom-css", "css"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13480630"
---

# Where to Add Custom CSS

Divi 5 provides several locations for adding custom CSS, each with a different scope and syntax.

## Overview

Choosing the right place to add CSS depends on whether you need site-wide styles, page-specific rules, or element-level overrides. Divi 5 offers seven distinct methods, and understanding their scope helps you keep your styles organized and maintainable.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13480630).

## Methods at a Glance

| Method | Scope | Best For |
|--------|-------|----------|
| Theme Options Custom CSS | Site-wide | Global overrides and utility classes |
| Page Settings CSS | Single page | Page-specific adjustments |
| Element Free-Form CSS | Single element | Targeted element styling |
| Module Elements Tab | Single element | Quick property overrides |
| Code Module | Page/section | Complex CSS blocks |
| Child Theme `style.css` | Site-wide | Production-grade customizations |
| Inline Styles | Single element | One-off overrides in text modules |

## Theme Options Custom CSS

**Path:** Divi > Theme Options > General > Custom CSS

This is the most common location for site-wide CSS. Rules added here apply to every page and sync automatically with **Appearance > Customize > Additional CSS** in WordPress.

## Page Settings CSS

**Path:** Open a page in the Visual Builder > Page Settings (gear icon) > Advanced > Custom CSS

CSS added here applies only to the current page. Useful for page-specific layout tweaks that should not affect other pages.

## Element Free-Form CSS

**Path:** Select any element > Advanced tab > CSS > Free Form CSS

Write CSS scoped to a single element. To target the element itself, use the `selector.` prefix:

```css
selector. {
    background-color: #f5f5f5;
    border-radius: 8px;
}
```

To target child elements, extend from `selector.`:

```css
selector. h2 {
    color: #333;
}
```

## Module Elements Tab

**Path:** Select any element > Advanced tab > CSS > Module Elements

This area accepts **CSS property-value pairs only** -- no selectors. For example:

```css
color: red;
font-weight: bold;
```

Each target area in the Module Elements list corresponds to a specific part of the module (title, body, image, etc.).

## Code Module

Add a Code module to any row and wrap your CSS in `<style>` tags:

```html
<style>
.my-custom-class {
    margin-top: 20px;
}
</style>
```

This is useful for complex CSS that should live alongside the content it affects.

## Child Theme

For production sites, placing CSS in a child theme's `style.css` keeps customizations safe across Divi updates. Edit via **Appearance > Theme File Editor** or your preferred code editor.

## Inline Styles

In text-based modules (Text, Code), you can add inline styles directly in the HTML:

```html
<p style="color: blue; font-size: 18px;">Styled paragraph</p>
```

Use this sparingly -- inline styles are hard to maintain and override.

## Related

- [Fix Custom CSS Not Working](fix-custom-css.md)
- [CSS Options Group](../options-groups/css.md)
- [CSS in Divi 5 Playbook](../playbooks/css-in-divi.md)
