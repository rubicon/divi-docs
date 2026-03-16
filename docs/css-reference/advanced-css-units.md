---
title: "Advanced CSS Units & Functions"
description: "Divi 5 CSS units and functions — calc(), clamp(), min(), max(), var(), supported units, and practical responsive patterns without custom breakpoints."
category: css-reference
tags: [css-units, css-functions, calc, clamp, responsive, css-variables]
related: [design-variables, relative-colors-hsl, common-overrides, design-system-workflow]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10823890"
---

# Advanced CSS Units & Functions

How to use CSS math functions, custom properties, and modern units in Divi 5 fields — with practical patterns for responsive design, computed layouts, and dynamic spacing.

!!! abstract "Quick Reference"
    **What this covers:** The CSS developer perspective on Divi 5's advanced unit system — which units and functions are supported, how CSS custom properties differ from design variables, and real-world patterns.
    **Builder UI docs:** See [Advanced Units (Builder)](../builder/advanced-units.md) for the unit picker interface and field behavior.
    **Key capabilities:**

    - CSS math: `calc()`, `clamp()`, `min()`, `max()`
    - CSS keywords: `auto`, `none`, `inherit`, `unset`
    - CSS custom properties: `var(--name)` at site, page, or element scope
    - Units: `px`, `em`, `rem`, `%`, `vw`, `vh`, `vmin`, `vmax`, plus angle units

    **ET Docs:** [Advanced Units](https://help.elegantthemes.com/en/articles/10823890){:target="_blank"}

## Supported CSS Units

Every numeric field in Divi 5 has a unit picker that supports these units.

| Unit | Category | Description | Common Use |
|------|----------|-------------|------------|
| `px` | Absolute | Fixed pixels | Borders, small spacing, icon sizes |
| `em` | Relative | Relative to parent element's font size | Spacing relative to text size |
| `rem` | Relative | Relative to root (`<html>`) font size | Typography, consistent spacing |
| `%` | Relative | Percentage of parent dimension | Widths, heights, fluid layouts |
| `vw` | Viewport | Percentage of viewport width | Full-width elements, fluid typography |
| `vh` | Viewport | Percentage of viewport height | Hero sections, full-screen layouts |
| `vmin` | Viewport | Smaller of `vw` or `vh` | Orientation-independent sizing |
| `vmax` | Viewport | Larger of `vw` or `vh` | Orientation-independent sizing |
| `grad` | Angle | Gradians (400 per full rotation) | Transform rotations |
| `rad` | Angle | Radians | Transform rotations |
| `turn` | Angle | Full rotations (1turn = 360deg) | Transform rotations |

**Not currently supported:** `ch`, `ex`, `dvw`, `dvh`, `svw`, `svh`, `lvw`, `lvh`, `cqi`, `cqb`.

!!! tip "Unit Choice Guide"
    Use `rem` for typography and spacing when you want root-relative consistency. Use `em` when you want sizing relative to the parent context (e.g., button padding that scales with button font size). Use `vw`/`vh` for viewport-dependent layouts. Use `px` for borders and hairlines that should not scale.

## CSS Math Functions

Divi 5 accepts CSS math functions in any numeric field. When a function is entered, the unit picker's arrow incrementer and scrubber are disabled since computed values cannot be adjusted by simple increment/decrement.

### `calc()` — Mixed-Unit Arithmetic

Combine different units in a single value.

```css
/* Full viewport height minus a fixed header */
calc(100vh - 80px)

/* 50% width minus gutters */
calc(50% - 24px)

/* Responsive padding that scales but has a minimum */
calc(2vw + 16px)
```

**In Divi fields:** Enter the full expression including `calc()` in the value input. The unit picker switches to an em-dash display.

### `clamp()` — Responsive Ranges

Define a minimum, preferred, and maximum value in one declaration. The browser uses the preferred value when it falls within the min/max bounds.

```css
/* Fluid text: minimum 16px, scales with viewport, caps at 24px */
clamp(16px, 2vw + 10px, 24px)

/* Responsive section padding: 30px minimum, 6vw preferred, 80px max */
clamp(30px, 6vw, 80px)

/* Container width that adapts but stays bounded */
clamp(320px, 90vw, 1200px)
```

**In Divi fields:** Enter `clamp(min, preferred, max)` as the value. This is the single most useful function for responsive design without breakpoints — one value handles desktop, tablet, and phone.

### `min()` and `max()` — Bounded Values

`min()` resolves to the smallest of its arguments. `max()` resolves to the largest.

```css
/* Width that is either 1200px or 90% of viewport — whichever is smaller */
min(1200px, 90vw)

/* Padding that is at least 20px even when the viewport is narrow */
max(20px, 3vw)

/* Font size that does not drop below 14px */
max(14px, 1.2vw)
```

## CSS Keywords

CSS keywords are entered directly into numeric fields. The unit picker shows an em-dash when a keyword is active.

| Keyword | Description | Common Use |
|---------|-------------|------------|
| `auto` | Let the browser determine the value | Margins for centering, heights for intrinsic sizing |
| `none` | Remove a property constraint | `max-width: none` to remove width caps |
| `inherit` | Inherit from the parent element | Match parent spacing or sizing |
| `unset` | Reset to inherited or initial value | Remove Divi-applied overrides |

## CSS Custom Properties in Divi

CSS custom properties (`--variable-name` syntax) can be defined and used in Divi 5 fields. They are distinct from [design variables](design-variables.md) — see that page for the full comparison.

### Three Scope Levels

| Scope | Where to Define | Availability | Persistence |
|-------|----------------|-------------|-------------|
| Site-wide | Theme Options > Custom CSS | Every page and template | Survives page changes |
| Page-specific | Page Settings > Advanced > Custom CSS | Current page only | Saved with page |
| Element-specific | Element Settings > Advanced > Free-Form CSS | Element and its children | Saved with element |

### Defining Custom Properties

Define properties using standard CSS syntax in the appropriate scope:

```css
/* Site-wide: Theme Options > Custom CSS */
:root {
    --header-height: 80px;
    --content-max-width: 1200px;
    --brand-primary: #1A73E8;
    --brand-primary-hover: #1557B0;
    --transition-speed: 0.3s;
}
```

```css
/* Page-specific: Page Settings > Custom CSS */
:root {
    --hero-height: 90vh;
    --page-accent: #E84315;
}
```

```css
/* Element-specific: Element > Advanced > Free-Form CSS */
.my-card {
    --card-padding: 24px;
    --card-radius: 8px;
}
```

### Using Custom Properties in Divi Fields

Enter `var(--variable-name)` in any numeric field's value input:

- `var(--header-height)` in a height field
- `var(--content-max-width)` in a max-width field
- `calc(100vh - var(--header-height))` mixing `var()` with `calc()`

### When to Use CSS Custom Properties vs. Design Variables

| Scenario | Use Design Variables | Use CSS Custom Properties |
|----------|---------------------|--------------------------|
| Brand colors managed by non-developers | Yes | No |
| Responsive spacing with breakpoint overrides in CSS | No | Yes |
| Values that need to be visible/overridable in DevTools | No | Yes |
| Content fields (text, images, links) | Yes | No |
| Custom CSS fields (element or theme level) | No | Yes |
| Computed values in `calc()` expressions in custom CSS | No | Yes |

### Divi's Internal CSS Custom Properties

!!! info "🔬 Needs Testing"
    Divi 5 may generate its own CSS custom properties (e.g., `--et-*` or `--divi-*` prefixed variables) for internal styling. These could provide hooks for advanced customization if documented. The existence, naming convention, and stability of any internal custom properties need verification.

<!-- TODO: Inspect Divi 5 rendered output for --et-* or --divi-* custom properties -->
<!-- TODO: Test whether internal custom properties are considered public API or implementation details -->

## Practical Patterns

### Fluid Typography Without Breakpoints

Instead of setting different font sizes at each breakpoint, use `clamp()` for smooth scaling:

```css
/* In a heading font-size field */
clamp(24px, 3vw + 12px, 56px)
```

This produces:

- ~24px at 320px viewport (phone)
- ~36px at 768px viewport (tablet)
- ~56px at 1440px+ viewport (desktop)

No media queries needed. Set it once in the Divi field or in a [number variable](design-variables.md).

### Full-Height Hero Minus Sticky Header

```css
/* In a section min-height field */
calc(100vh - 80px)
```

Better yet, define the header height as a CSS custom property and reference it:

```css
/* Theme Options > Custom CSS */
:root {
    --header-height: 80px;
}
```

```css
/* In the hero section's min-height field */
calc(100vh - var(--header-height))
```

If the header height changes, update one property instead of finding every `calc()` reference.

### Responsive Section Padding

```css
/* In a section padding field — works across all devices */
clamp(30px, 6vw, 80px)
```

At 320px viewport: `~49px` (6vw = 19.2px, but clamped minimum is 30px, so 30px).
At 768px viewport: `~46px` (6vw = 46px).
At 1440px viewport: `80px` (6vw = 86.4px, capped at 80px).

### Responsive Grid Gaps

```css
/* In a CSS Grid gap field */
clamp(12px, 2vw, 32px)
```

Gaps scale smoothly from 12px on small screens to 32px on large screens.

### Aspect Ratio Sections

Use padding-bottom percentage to create aspect-ratio containers (useful for sections with background images):

```css
/* In a section padding-bottom field for 16:9 aspect ratio */
56.25%

/* For 4:3 aspect ratio */
75%

/* For a square */
100%
```

### Viewport-Aware Content Width

```css
/* In a row max-width field */
min(1200px, 90vw)
```

The content area is 90% of the viewport on narrow screens, capping at 1200px on wide screens. No breakpoint override needed.

### Combined: Responsive Card Layout

Using CSS custom properties with Divi's CSS Grid:

```css
/* Theme Options > Custom CSS */
:root {
    --card-min-width: 280px;
    --card-gap: clamp(16px, 2vw, 32px);
    --card-padding: clamp(16px, 2vw, 24px);
    --card-radius: 8px;
}
```

Then in a section or row's Custom CSS field:

```css
/* Auto-responsive grid — no breakpoints */
display: grid;
grid-template-columns: repeat(auto-fill, minmax(var(--card-min-width), 1fr));
gap: var(--card-gap);
```

## AI Interaction Notes

!!! info "Data Storage — 🔬 Needs Testing"
    Advanced unit values (including `calc()`, `clamp()` expressions) are stored as raw strings in the element's attribute data within the layout JSON. CSS custom properties defined in Theme Options are stored in `wp_options` as part of the Custom CSS field value.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read field value | Layout JSON inspection or `get_post_meta()` | 🔬 Needs Testing | Functions stored as complete strings, e.g. `"clamp(16px, 2vw, 24px)"` |
| Modify field value | Layout JSON update or `update_post_meta()` | 🔬 Needs Testing | Must preserve entire expression syntax |
| Define CSS custom property | Write to Theme Options Custom CSS or page Custom CSS | 🔬 Needs Testing | Standard CSS syntax in the appropriate field |
| Read CSS custom properties | Parse the Custom CSS field value | 🔬 Needs Testing | No API endpoint for individual properties — parse from CSS text |

<!-- TODO: Verify how calc/clamp expressions are stored in layout JSON — raw string or parsed tokens? -->
<!-- TODO: Test whether CSS custom properties defined at element scope are available in sibling elements -->

## Version Notes

!!! note "Divi 5 Only"
    The advanced unit picker with `calc()`, `clamp()`, `min()`, `max()`, keywords, and `var()` support is new to Divi 5. Divi 4 did not support CSS functions in its numeric fields — only static values with unit selection.

## Related

- [Advanced Units (Builder)](../builder/advanced-units.md) — Unit picker UI, field behavior, and supported formats
- [Design Variables (CSS Reference)](design-variables.md) — How design variables differ from CSS custom properties
- [Design System Workflow](design-system-workflow.md) — Using variables and functions in a systematic design approach
- [Relative Colors & HSL](relative-colors-hsl.md) — HSL color functions for derived color values
- [Common Overrides](common-overrides.md) — CSS snippets using standard units and selectors
- [Responsive Options (Builder)](../builder/responsive-options.md) — Divi's built-in responsive controls as an alternative to CSS functions
- [Custom Breakpoints (Builder)](../builder/custom-breakpoints.md) — When you need breakpoints beyond what `clamp()` can handle
