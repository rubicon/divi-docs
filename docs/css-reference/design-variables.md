---
title: "Design Variables"
description: "Divi 5 Design Variables from a CSS perspective — variable types, CSS output, cascade behavior, naming conventions, and programmatic access patterns."
category: css-reference
tags: [design-variables, css-variables, design-system, tokens, programmatic]
related: [design-system-workflow, advanced-css-units, common-overrides, class-reference]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11027601"
---

# Design Variables — CSS Reference

How Divi 5 design variables translate to CSS output, how they differ from native CSS custom properties, and when to use each approach.

!!! abstract "Quick Reference"
    **What this covers:** The CSS and developer perspective on design variables — how values resolve, what the browser sees, and how variables fit into a layered design system.
    **Builder UI docs:** See [Design Variables (Builder)](../builder/design-variables.md) for the full Variable Manager walkthrough.
    **Key takeaway:** Design variables resolve to static values in the rendered CSS. They are not CSS custom properties — the browser never sees a `var()` reference for a design variable.

    **ET Docs:** [Design Variables](https://help.elegantthemes.com/en/articles/11027601){:target="_blank"}

## Variable Types at a Glance

Divi 5 supports six variable types. Each maps to specific CSS properties when applied to element fields.

| Type | Stored As | CSS Properties Affected | Example |
|------|-----------|------------------------|---------|
| Color | Hex / RGBA | `color`, `background-color`, `border-color`, `fill`, `box-shadow` color | `Primary Brand: #1A73E8` |
| Font | Font family string | `font-family` | `Heading Font: Montserrat` |
| Number | Value + unit | `font-size`, `padding`, `margin`, `border-radius`, `width`, `height`, `gap` | `Section Padding: 60px` |
| Image | URL | `background-image`, `content` url, `src` attribute | `Logo: /uploads/logo.svg` |
| Link | URL string | `href` attribute values (not CSS) | `CTA URL: /contact/` |
| Text | String | Text content, `aria-label`, `title` attributes (not CSS) | `Phone: (555) 123-4567` |

Color, Font, and Number variables directly affect CSS output. Image variables affect CSS when used as backgrounds. Link and Text variables affect HTML attributes and content, not CSS.

## How Variables Become CSS

When you assign a design variable to a field, Divi resolves the variable at render time and writes the **actual value** into the element's CSS output. The variable reference exists only in Divi's data layer — it never appears in the rendered stylesheet.

```css
/* What you might expect */
.et_pb_section_0 {
    padding-top: var(--section-padding); /* NOT how it works */
}

/* What Divi actually outputs */
.et_pb_section_0 {
    padding-top: 60px; /* Resolved from the "Section Padding" variable */
}
```

!!! warning "Observed Behavior"
    This means you cannot target or override a design variable's value using CSS custom properties. The browser sees only the resolved value. To change a variable's effect, you must change the variable itself through the Variable Manager or programmatic API.

**Implications for developers:**

- DevTools shows the resolved value, not a variable reference
- You cannot use `getComputedStyle()` to find which variable produced a value
- Changing a variable updates all CSS output on next render, but requires Divi to regenerate styles
- Custom CSS fields cannot reference design variables by name

## Design Variables vs. CSS Custom Properties

Divi 5 supports both design variables (via the Variable Manager) and CSS custom properties (via [Advanced Units](../builder/advanced-units.md)). They serve different purposes and work differently.

| Feature | Design Variable | CSS Custom Property (`var()`) |
|---------|----------------|-------------------------------|
| Managed through | Variable Manager UI | Code — Theme Options CSS, page CSS, or element CSS |
| Editable by non-developers | Yes | No |
| Available in Content tab | Yes (text, links, images) | No |
| Available in Design tab | Yes (colors, fonts, numbers) | Numbers only (via unit picker) |
| Updates sitewide | Yes (all references) | Yes (all `var()` references in scope) |
| Visible in DevTools | As resolved value only | As `var(--name)` — inspectable and overridable |
| Works in Custom CSS fields | No | Yes |
| Supports responsive overrides | Per-variable (set once, applies everywhere) | Per-scope (redefine at breakpoints in CSS) |
| Works with `calc()` | Number variables can use `calc()` in their value | Yes, natively |

**When to use which:**

- **Design variables** when the value is managed by designers or content editors through the UI, and when it needs to apply to Content tab fields (text, images, links)
- **CSS custom properties** when you need the value inspectable in DevTools, overridable in custom CSS fields, or scoped to specific breakpoints without Divi's responsive system

## The Three-Layer Cascade

Design variables are the foundation of Divi 5's design system hierarchy:

```
Variables (raw values) → Presets (style collections using variables) → Elements (using presets)
```

| Layer | What It Stores | Change Impact |
|-------|---------------|---------------|
| Variables | Single values (colors, fonts, numbers, images, text, links) | All presets and elements referencing the variable update |
| Option Group Presets | Bundled settings for one option group (typography, spacing, etc.), can reference variables | All element presets and elements using the option group preset update |
| Element Presets | Complete element styling, can nest option group presets and reference variables | All elements assigned the preset update |
| Element Overrides | Individual element settings that override the preset | Only that element is affected |

**Cascade example:** You set `Primary Brand` variable to `#1A73E8`. An "H2 Typography" option group preset references it for heading color. A "Card" element preset nests that typography preset. Every card module on the site shows `#1A73E8` headings. Change the variable to `#E84315` — every card heading turns orange.

For the full workflow of building with this cascade, see [Design System Workflow](design-system-workflow.md).

## Naming Conventions

Variable names are user-defined. Choose a convention and stick with it.

| Approach | Example | Pros | Cons |
|----------|---------|------|------|
| Purpose-based | `Primary Background`, `CTA Hover`, `Section Padding Large` | Self-documenting, survives rebrand | Names become misleading if repurposed |
| Value-based | `Blue 1`, `40px`, `Montserrat` | Quick to create | No context about where/why it is used |
| Semantic tokens | `color-surface-primary`, `spacing-section-lg`, `font-heading` | Scalable, design-system-friendly | Steeper learning curve for non-developers |

**Recommendation:** Use purpose-based names for teams with non-technical editors. Use semantic tokens for developer-driven projects where the variable list will grow beyond 20-30 entries.

## CSS Output Patterns

Understanding what CSS Divi generates helps when writing overrides or debugging.

### Color variables

When a color variable is applied to a background field:

```css
/* Divi generates inline or scoped styles like: */
.et_pb_section_0 {
    background-color: #1A73E8;
}
```

The same color variable applied to different fields produces different CSS properties — `color`, `border-color`, `background-color`, etc. — depending on which field it is assigned to.

### Number variables

Number variables include a unit. The CSS output uses the value and unit directly:

```css
/* Variable "Section Padding" = 60px */
.et_pb_section_0 {
    padding-top: 60px;
    padding-bottom: 60px;
}
```

Number variables that use CSS functions are output as-is:

```css
/* Variable "Fluid Heading" = clamp(24px, 4vw, 48px) */
.et_pb_text_0 h2 {
    font-size: clamp(24px, 4vw, 48px);
}
```

### Font variables

```css
/* Variable "Heading Font" = Montserrat */
.et_pb_text_0 h2 {
    font-family: 'Montserrat', sans-serif;
}
```

## Overriding Variable-Set Values with CSS

Because variables resolve to static CSS values, you can override them with standard CSS specificity:

```css
/* The variable sets padding to 60px, but you need 0 for a specific section */
body .hero-section.et_pb_section {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}
```

However, this creates a disconnect — the Variable Manager shows one value, but the element renders differently. **Prefer changing the variable or using element-level overrides in the builder** instead of CSS overrides when possible.

## AI Interaction Notes

!!! info "Data Storage — 🔬 Needs Testing"
    Design variables are likely stored in `wp_options` or a custom database table — not in `post_content` or individual element attributes. Each variable stores a name, type, and value. The exact storage key and serialization format need verification.

**Why variables matter for AI workflows:**

- A single variable change updates all referencing fields sitewide — this is the most efficient way to make brand-level changes
- When a user asks to "change the brand color," modify the variable, not individual modules
- When a user asks to "make all headings bigger," check if a number variable controls heading size before editing individual elements

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read all variables | Divi REST API or `wp_options` query | 🔬 Needs Testing | Variables may be serialized in a Divi-specific options key |
| Read variable value | Divi REST API | 🔬 Needs Testing | Look for an endpoint that returns variable name, type, and current value |
| Modify value | Divi REST API or `update_option()` | 🔬 Needs Testing | Changing a value triggers CSS regeneration on next page render |
| Create variable | Divi REST API or `update_option()` | 🔬 Needs Testing | Must include name, type, and value; number variables require unit |
| Delete variable | Divi REST API or `update_option()` | 🔬 Needs Testing | Deleted variables are archived until next save (see builder docs) |

<!-- TODO: Identify the exact wp_options key or database table for variable storage -->
<!-- TODO: Test whether variable values appear in the layout JSON or only by reference ID -->
<!-- TODO: Verify CSS regeneration behavior — does changing a variable require a full site rebuild or per-page regeneration? -->

## Version Notes

!!! note "Divi 5 Only"
    Design variables are a Divi 5 feature. Divi 4 did not have a built-in variable system — CSS custom properties in Theme Options Custom CSS were the closest equivalent.

## Related

- [Design Variables (Builder)](../builder/design-variables.md) — Full Variable Manager UI walkthrough
- [Global Variables](../builder/global-variables.md) — Site-wide variables that persist across all pages
- [Design System Workflow](design-system-workflow.md) — Step-by-step process for building with variables and presets
- [Advanced CSS Units & Functions](advanced-css-units.md) — CSS custom properties and math functions in Divi fields
- [Relative Colors & HSL](relative-colors-hsl.md) — Derive color variations from variable-defined base colors
- [Common Overrides](common-overrides.md) — CSS snippets that may override variable-set values
- [CSS Class Reference](class-reference.md) — Selectors for targeting Divi elements in custom CSS
