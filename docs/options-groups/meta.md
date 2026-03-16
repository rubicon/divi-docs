---
title: "Meta Options"
category: options-groups
tags: ["options-groups", "meta", "advanced"]
related: ["attributes", "link"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10066900"
---

# Meta Options

The Meta options group provides builder-level organization settings, letting you label elements for easier identification and control their visibility during editing.

## Overview

The Meta options group is focused entirely on the development and editing experience within the Divi 5 Visual Builder. Unlike most other options groups, its settings have no effect on the front-end appearance of your site. Instead, they help you stay organized and work more efficiently as your layouts grow in complexity.

The Element Label setting (previously known as "Admin Label" in earlier versions of Divi) lets you give any element a descriptive name that appears in the Visual Builder's layer panel and breadcrumbs. This is especially valuable on pages with many similar elements, where default labels like "Text Module" or "Row" make it difficult to find what you need. Descriptive labels like "Hero Headline" or "Pricing Row" make navigation faster and improve collaboration when multiple team members work on the same layout.

The Force Visible setting addresses a common workflow challenge: editing elements that are hidden by conditions, visibility rules, or other display logic. Rather than temporarily removing those rules, you can force the element to remain visible while the builder is open or while you are actively editing it, then let it return to its conditional behavior on the front end.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10066900).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Element Label | Text input | Assigns a custom name to the element that appears in the Visual Builder's layer panel, breadcrumbs, and tooltips. Does not affect front-end output. |
| Force Visible | Dropdown | Controls whether a hidden element is temporarily shown in the Visual Builder. Options are Never (default behavior, element follows its normal visibility rules), While in Builder (element is always visible when the Visual Builder is active), and While Editing Element (element is visible only when its settings panel is open). |

## Which Elements Use This

All modules, columns, rows, and sections in the Divi 5 Visual Builder include the Meta options group. The settings are found under the **Advanced** tab.

## Code Examples

The Meta options group does not produce any front-end output, so there are no CSS or JavaScript examples. Its functionality is limited to the Visual Builder editing environment.

A best practice for element labels is to use a consistent naming convention across your project:

```
Section: Hero
  Row: Hero Content
    Column: Hero Left
      Module: Hero Headline
      Module: Hero Subtext
    Column: Hero Right
      Module: Hero Image
```

## Related

- [Attributes Options](attributes.md)
- [Link Options](link.md)
