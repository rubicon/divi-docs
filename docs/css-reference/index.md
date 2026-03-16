---
title: "CSS Reference"
description: "Divi 5 CSS reference — design variables, presets, class naming conventions, selectors, advanced CSS units, and custom overrides for a variable-first styling workflow."
category: css-reference
tags: [css, selectors, classes, styling, design-variables, presets]
last_updated: 2026-03-16
---

# CSS Reference

Everything you need to write, debug, and maintain CSS in Divi 5 — organized around the principle that variables and presets should handle most styling, with custom CSS reserved for edge cases.

!!! abstract "Quick Reference"
    **What this section covers:** Design variables, presets, CSS class names, advanced CSS units, and tested override snippets for styling Divi 5 elements.
    **Key principle:** Use Design Variables for reusable values, Presets for reusable style collections, and Custom CSS only for what the UI can't handle.
    **Key prefix:** All Divi classes use the `et_pb_` prefix.

## Variable-First Styling

Divi 5's styling system operates on three levels: **Design Variables** for reusable values, **Presets** for reusable style collections, and **Custom CSS** for edge cases. This section documents all three, with an emphasis on using the right level for each task.

## The Right Tool for the Job

| Need | Right Approach | Wrong Approach |
|------|---------------|----------------|
| Consistent brand colors across the site | Color variables in the Variable Manager | Hard-coded hex values in custom CSS |
| All buttons styled the same way | Button Option Group Preset referencing variables | CSS override targeting `.et_pb_button` |
| Section padding standardized sitewide | Number variable for spacing, applied via presets | CSS targeting `.et_pb_section` with `!important` |
| One specific module needs a unique tweak | Module's Advanced > Custom CSS field | Global CSS that leaks to other instances |
| Pseudo-element decoration | Custom CSS (no Divi setting for this) | — (correct use of custom CSS) |
| Complex :nth-child selectors | Custom CSS | — (correct use of custom CSS) |

## Sections

| Page | What You'll Find |
|------|-----------------|
| [Design Variables](design-variables.md) | Variable types, CSS output behavior, cascade, and programmatic access |
| [Design System Workflow](design-system-workflow.md) | Step-by-step: variables > presets > pages |
| [Advanced CSS Units](advanced-css-units.md) | calc(), clamp(), min(), max(), var(), and responsive patterns |
| [Relative Colors & HSL](relative-colors-hsl.md) | Derived colors, hover states, and accessible color harmonies |
| [Class Reference](class-reference.md) | Divi CSS class naming conventions and selectors |
| [Common Overrides](common-overrides.md) | CSS snippets for edge cases the UI can't handle |

## Related

- [Presets](../builder/presets.md) — Reusable style collections managed through the Visual Builder
- [Design Variables](../builder/design-variables.md) — Named tokens for colors, numbers, fonts, and more
- [Style Inspector](../builder/style-inspector.md) — Audit and edit all styles on a page from one panel
- [CSS in Divi 5 Playbook](../playbooks/css-in-divi.md) — Decision framework for when and how to use CSS
