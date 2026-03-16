---
title: "Design System Workflow"
description: "Divi 5 design system workflow — step-by-step process for building with variables, option group presets, element presets, and the Style Inspector."
category: css-reference
tags: [design-system, workflow, variables, presets, best-practices]
related: [design-variables, advanced-css-units, common-overrides]
divi_version: "5.x"
last_updated: 2026-03-16
---

# Design System Workflow

A practical, step-by-step process for building a Divi 5 site using variables, presets, and the Style Inspector — so design changes cascade predictably and CSS overrides become the exception, not the rule.

!!! abstract "Quick Reference"
    **The 5-step process:**

    1. Define variables (colors, fonts, spacing, images, text, links)
    2. Create option group presets (typography scales, button styles, spacing rules)
    3. Create element presets (default looks for each module type)
    4. Build pages (new modules inherit defaults; override only when needed)
    5. Maintain (change variables and presets, not individual modules)

    **Key principle:** Variables first, presets second, element overrides third, custom CSS last.

## Why a Design System Matters

Without a system, every module is styled independently. Changing a brand color means hunting through dozens of pages. With Divi 5's variable-and-preset architecture, a single change propagates everywhere.

| Approach | Change Brand Color | Change All Button Styles | Change Section Spacing | Effort Level |
|----------|-------------------|--------------------------|----------------------|--------------|
| Raw CSS overrides | Find/replace across all custom CSS | Rewrite every button override | Update every `@media` block | Hours |
| Variables only | Update 1 color variable | Update each button module manually | Update 1 spacing variable | Minutes |
| Variables + Presets | Update 1 color variable | Update 1 button preset (or 0 if it uses the variable) | Update 1 spacing preset (or 0 if it uses the variable) | Seconds |

The rest of this page walks through building the "Variables + Presets" approach from scratch.

## Step 1: Define Variables

Before touching any module, create the raw values your entire site will reference. Open the [Variable Manager](../builder/design-variables.md) and create variables for each category.

### Recommended Starter Variables

| Category | Variable Name | Example Value | Used For |
|----------|--------------|---------------|----------|
| **Colors** | Primary Brand | `#1A73E8` | Buttons, links, accents |
| | Secondary Brand | `#F4511E` | CTAs, highlights |
| | Dark Text | `#1A1A2E` | Headings |
| | Body Text | `#555555` | Paragraphs, descriptions |
| | Light Background | `#F8F9FA` | Alternating sections |
| | Dark Background | `#1A1A2E` | Hero, footer, dark sections |
| | Border Color | `#E0E0E0` | Cards, form inputs, dividers |
| **Fonts** | Heading Font | `Montserrat` | All headings |
| | Body Font | `Inter` | Body text, UI elements |
| **Numbers** | Section Padding Large | `80px` | Primary section spacing |
| | Section Padding Medium | `50px` | Compact sections |
| | Section Padding Small | `30px` | Tight sections, mobile |
| | Content Max Width | `1200px` | Row max-width |
| | Border Radius Standard | `8px` | Cards, images, buttons |
| | Border Radius Small | `4px` | Inputs, tags |
| | Fluid Heading Size | `clamp(28px, 4vw, 48px)` | Responsive hero headings |
| **Images** | Logo | `/uploads/logo.svg` | Header, footer |
| | Default OG Image | `/uploads/og-default.jpg` | Social sharing fallback |
| **Text** | Phone Number | `(555) 123-4567` | Header bar, contact pages |
| | Business Address | `123 Main St, City` | Footer, contact pages |
| **Links** | Primary CTA URL | `/get-started/` | Main call-to-action buttons |

**Tips:**

- Use purpose-based names, not value-based names (`Primary Brand` not `Blue`)
- Use [relative colors](relative-colors-hsl.md) for hover states and tints instead of creating separate variables for every shade
- Number variables support `calc()` and `clamp()` — use them for responsive values (see [Advanced CSS Units](advanced-css-units.md))

## Step 2: Create Option Group Presets

[Option group presets](../builder/option-group-presets.md) bundle settings for a single design concern (typography, spacing, buttons, backgrounds) and can be reused across any element type. They are the "utility classes" of the Divi builder.

### Recommended Starter Presets

| Preset Type | Preset Name | Key Settings | Referenced Variables |
|-------------|-------------|-------------|---------------------|
| Typography | H1 Heading | Font: Heading Font, Size: 48px, Weight: 700, Color: Dark Text | Heading Font, Dark Text |
| Typography | H2 Heading | Font: Heading Font, Size: 36px, Weight: 700, Color: Dark Text | Heading Font, Dark Text |
| Typography | H3 Heading | Font: Heading Font, Size: 28px, Weight: 600, Color: Dark Text | Heading Font, Dark Text |
| Typography | Body Text | Font: Body Font, Size: 16px, Line Height: 1.7, Color: Body Text | Body Font, Body Text |
| Spacing | Section Large | Padding: Section Padding Large (top/bottom) | Section Padding Large |
| Spacing | Section Compact | Padding: Section Padding Small (top/bottom) | Section Padding Small |
| Buttons | Primary Button | Background: Primary Brand, Color: white, Radius: Border Radius Standard, Padding: 14px 32px | Primary Brand, Border Radius Standard |
| Buttons | Secondary Button | Background: transparent, Border: 2px solid Primary Brand, Color: Primary Brand | Primary Brand |
| Background | Light Surface | Background Color: Light Background | Light Background |
| Background | Dark Surface | Background Color: Dark Background | Dark Background |
| Borders | Card Border | Border: 1px solid Border Color, Radius: Border Radius Standard | Border Color, Border Radius Standard |
| Box Shadow | Subtle Shadow | Box Shadow: 0 2px 12px rgba(0,0,0,0.08) | (none — shadows rarely need variables) |

**Tips:**

- Reference variables inside presets wherever possible — this creates the cascade chain
- Keep presets single-purpose; a typography preset should not include spacing
- See [Stacked & Nested Presets](../builder/stacked-nested-presets.md) for combining multiple option group presets

## Step 3: Create Element Presets

[Element presets](../builder/element-presets.md) define the complete default appearance for each module type. They can nest option group presets from Step 2.

### Recommended Element Presets

| Element Type | Preset Name | Nested Option Group Presets | Additional Settings |
|-------------|-------------|---------------------------|-------------------|
| Section | Default Section | Section Large (spacing) | — |
| Section | Dark Section | Section Large (spacing), Dark Surface (background) | Text color: white |
| Button | Primary CTA | Primary Button (button) | — |
| Button | Secondary CTA | Secondary Button (button) | — |
| Text | Body Content | Body Text (typography) | — |
| Blurb | Feature Card | Card Border (borders), Subtle Shadow (shadow), H3 Heading (title typography) | Padding: 24px |
| Image | Standard Image | — | Border radius: Border Radius Standard |

**Tips:**

- Set the most commonly used preset as the **default** (star icon) for each element type
- New modules then inherit correct styling with zero configuration
- See the [Preset Manager](../builder/preset-manager.md) for centralized management

## Step 4: Build Pages

With variables, option group presets, and element presets in place, page building becomes assembly:

1. **Add a section** — it inherits the default section preset (spacing, background)
2. **Add modules** — each inherits its element type's default preset
3. **Override only when needed** — a specific hero section needs more padding? Override at the element level
4. **Assign alternate presets** — a dark section? Switch from "Default Section" to "Dark Section" preset

At this stage, most modules require no manual styling. The design system handles consistency.

### When to Use Custom CSS

Even with a complete variable-and-preset system, some situations call for custom CSS:

| Situation | Example | Approach |
|-----------|---------|----------|
| Divi does not expose the property | `backdrop-filter`, `clip-path`, `scroll-snap` | Custom CSS field or Theme Options CSS |
| Complex selectors needed | Target nth-child, adjacent siblings, pseudo-elements | Custom CSS field |
| Third-party integration | Style a plugin's output inside Divi sections | Child theme CSS |
| Animation keyframes | Custom `@keyframes` for scroll-triggered effects | Theme Options CSS or child theme |

See [Common Overrides](common-overrides.md) for tested snippets.

## Step 5: Maintain

The payoff of a design system is in maintenance. When the brand evolves:

| Change Needed | What to Edit | Where |
|--------------|-------------|-------|
| New brand color | Update the color variable | Variable Manager |
| New heading font | Update the font variable | Variable Manager |
| Tighter section spacing | Update the number variable | Variable Manager |
| New button style (rounded) | Update the button option group preset | Option group preset editor |
| New card look | Update the card element preset | Element preset editor |
| One-off module override | Edit the individual module | Module settings |

### Using the Style Inspector

The [Style Inspector](../builder/style-inspector.md) is your audit tool:

- **Find inconsistencies** — open page-level inspection, look for one-off colors or font sizes that should be variables
- **Identify unlinked values** — static values that match a variable's value but are not referencing it
- **Verify preset coverage** — the Presets tab shows which elements use presets and which are styled manually

## When This Workflow Does Not Apply

The variables-first approach adds overhead that is not always justified:

| Situation | Recommendation |
|-----------|---------------|
| Simple one-page site | Skip variables; use presets for repeated elements, direct styles for everything else |
| Rapid prototype | Style directly, extract variables later when the design stabilizes |
| Inherited Divi 4 site | Migrate incrementally — create variables for new work, convert old pages during redesigns |
| Single-use landing page | Use element presets for brand consistency, but do not create page-specific variables |

## Version Notes

!!! note "Divi 5 Only"
    This workflow relies on Divi 5 features: the Variable Manager, option group presets, stacked/nested presets, and the Style Inspector. Divi 4 had Global Presets but lacked the variable system and option group preset composability.

## Related

- [Design Variables (CSS Reference)](design-variables.md) — How variables resolve to CSS output
- [Design Variables (Builder)](../builder/design-variables.md) — Variable Manager UI walkthrough
- [Option Group Presets](../builder/option-group-presets.md) — Creating cross-element style blocks
- [Element Presets](../builder/element-presets.md) — Per-element-type saved configurations
- [Stacked & Nested Presets](../builder/stacked-nested-presets.md) — Composing presets for layered styling
- [Style Inspector](../builder/style-inspector.md) — Auditing and editing styles from one panel
- [Advanced CSS Units & Functions](advanced-css-units.md) — Responsive values with `clamp()`, `calc()`, and `var()`
- [Common Overrides](common-overrides.md) — CSS snippets for when the builder is not enough
