---
title: "Advanced CSS Units & Functions"
category: css-reference
tags: [css-units, css-functions, calc, clamp, responsive, css-variables, var, min, max]
related: [design-variables, relative-colors-hsl, common-overrides, design-system-workflow]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/10823890"
---

# Advanced CSS Units & Functions

Build responsive layouts and computed spacing using CSS math functions, custom properties, and modern units without writing media queries.

## Overview

Divi 5's numeric fields support CSS functions (`calc()`, `clamp()`, `min()`, `max()`), CSS custom properties (`var(--name)`), and an expanded unit system beyond simple pixels. This page documents the CSS developer perspective — what units and functions are accepted by Divi fields, how to define and use custom properties at different scopes, and practical patterns for fluid responsive design.

For the builder interface side (unit picker UI, field behavior), see [Advanced Units (Builder)](../builder/advanced-units.md).

**Key capabilities:**
- CSS math: `calc()`, `clamp()`, `min()`, `max()`
- CSS keywords: `auto`, `none`, `inherit`, `unset`
- CSS custom properties: `var(--name)` at site, page, or element scope
- Units: `px`, `em`, `rem`, `%`, `vw`, `vh`, `vmin`, `vmax`, plus angle units

## Supported CSS Units

Every numeric field in Divi 5 accepts these units via the unit picker.

| Unit | Category | Description | Use Case |
|------|----------|-------------|----------|
| `px` | Absolute | Fixed pixels | Borders, small spacing, icon sizes that shouldn't scale |
| `em` | Relative | Relative to parent element's font size | Spacing tied to text size (e.g., button padding relative to button font) |
| `rem` | Relative | Relative to root (`<html>`) font size (typically 16px) | Typography, consistent spacing across pages |
| `%` | Relative | Percentage of parent dimension | Fluid widths, heights, padding as percentage of container |
| `vw` | Viewport | Percentage of viewport width (100vw = full browser width) | Full-width elements, viewport-dependent scaling |
| `vh` | Viewport | Percentage of viewport height | Hero sections, full-screen layouts, viewport-relative sizing |
| `vmin` | Viewport | Smaller of `vw` or `vh` | Orientation-independent sizing (portrait or landscape) |
| `vmax` | Viewport | Larger of `vw` or `vh` | Orientation-independent sizing (portrait or landscape) |
| `deg` | Angle | Degrees (360 per full rotation) | Transforms, rotations, gradients |
| `grad` | Angle | Gradians (400 per full rotation) | Transforms, rotations |
| `rad` | Angle | Radians (2π per full rotation) | Transforms, rotations |
| `turn` | Angle | Full rotations (1turn = 360deg) | Transforms, rotations |

**Not currently supported:** `ch`, `ex`, `dvw`, `dvh`, `svw`, `svh`, `lvw`, `lvh`, `cqi`, `cqb`.

!!! tip "Unit Selection Guide"
    - Use `rem` for typography and consistent spacing across the site
    - Use `em` when sizing elements relative to their own or parent's text size
    - Use `vw`/`vh` for viewport-dependent responsive layouts
    - Use `%` for fluid dimensions relative to the parent container
    - Use `px` for fixed elements (borders, hairlines) that should not scale

## CSS Math Functions

Divi 5 accepts CSS math functions in any numeric field. When a function is entered, the unit picker's increment/decrement buttons are disabled (since computed values cannot be adjusted by simple up/down arrows).

### `calc()` — Mixed-Unit Arithmetic

Combine different units in a single expression.

```css
/* Full viewport height minus a fixed header */
calc(100vh - 80px)

/* 50% width minus gutters */
calc(50% - 24px)

/* Responsive padding that scales with a minimum offset */
calc(2vw + 16px)

/* Width that is 100% of parent minus column gaps */
calc(100% - (24px * 2))
```

**In Divi fields:** Enter the full expression including `calc()`. The unit picker will show an em-dash while the function is active.

**Best for:** Subtracting fixed values from fluid dimensions (e.g., section height minus sticky header, column width minus gaps).

### `clamp()` — Responsive Ranges

Define a minimum, preferred, and maximum value. The browser uses the preferred value when it falls within the min/max bounds.

```css
/* Fluid text: 16px minimum, scales with viewport, caps at 24px */
clamp(16px, 2vw + 10px, 24px)

/* Responsive section padding: 30px minimum, 6vw preferred, 80px max */
clamp(30px, 6vw, 80px)

/* Container width that adapts but stays bounded */
clamp(320px, 90vw, 1200px)

/* Responsive spacing that scales smoothly */
clamp(16px, 3vw + 8px, 48px)
```

**In Divi fields:** Enter `clamp(min, preferred, max)` as the value. This is the single most useful function for responsive design without breakpoints — one value handles mobile, tablet, and desktop automatically.

**How it works:** At 320px viewport, the preferred value (6vw) equals 19.2px, which is less than the minimum (30px), so 30px wins. At 1440px viewport, the preferred value (86.4px) exceeds the maximum (80px), so 80px wins. At 768px, the preferred value (46px) is within bounds, so it's used.

### `min()` and `max()` — Bounded Values

`min()` resolves to the smallest value among its arguments. `max()` resolves to the largest.

```css
/* Width that is either 1200px or 90% of viewport — whichever is smaller */
min(1200px, 90vw)

/* Padding that is at least 20px, even on narrow viewports */
max(20px, 3vw)

/* Font size that does not drop below 14px */
max(14px, 1.2vw)

/* Responsive gap that scales but has both upper and lower bounds */
max(12px, min(32px, 3vw))
```

**When to use:**
- `min()` for capping responsive values (e.g., maximum width content area)
- `max()` for establishing responsive minimums (e.g., padding that never goes below a threshold)

## CSS Keywords

CSS keywords are entered directly into numeric fields. The unit picker displays an em-dash when a keyword is active.

| Keyword | Description | Common Use |
|---------|-------------|------------|
| `auto` | Let the browser determine the value | Margins for centering, heights for intrinsic sizing, widths for natural content flow |
| `none` | Remove a property constraint | Removing width caps (`max-width: none`), removing aspect ratio, clearing limits |
| `inherit` | Inherit from the parent element | Match parent spacing, sizing, or computed values |
| `unset` | Reset to inherited or initial value | Removing Divi-applied defaults or overrides |

## CSS Custom Properties (CSS Variables)

CSS custom properties (`--variable-name` syntax) can be defined and used in Divi 5 fields. They are distinct from [design variables](design-variables.md) — see that page for the detailed comparison.

### Three Scope Levels

| Scope | Definition Location | Availability | Persistence | Use Case |
|-------|---------------------|-------------|-------------|----------|
| Site-wide | Theme Options > Custom CSS | Every page and template | Survives across page changes | Brand dimensions, spacing scale, repeated values |
| Page-specific | Page Settings > Advanced > Custom CSS | Current page only | Saved with page | Page-specific header height, accent colors |
| Element-specific | Element > Advanced > Free-Form CSS | Element and its children | Saved with element | Component-level spacing, component-specific colors |

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
    --spacing-unit: 8px;
}
```

```css
/* Page-specific: Page Settings > Advanced > Custom CSS */
:root {
    --hero-height: 90vh;
    --page-accent: #E84315;
    --hero-padding: 60px;
}
```

```css
/* Element-specific: Element > Advanced > Free-Form CSS */
.my-card {
    --card-padding: 24px;
    --card-radius: 8px;
    --card-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
```

### Using Custom Properties in Divi Fields

Enter `var(--variable-name)` in any numeric field's value input:

```css
/* In a height field */
var(--header-height)

/* In a max-width field */
var(--content-max-width)

/* Combining var() with calc() */
calc(100vh - var(--header-height))

/* In margin or padding fields */
var(--spacing-unit)

/* With a fallback (browser uses fallback if variable undefined) */
var(--custom-spacing, 16px)
```

### When to Use CSS Custom Properties vs. Design Variables

| Scenario | Use Design Variables | Use CSS Custom Properties |
|----------|---------------------|--------------------------|
| Brand colors managed by non-developers | ✓ | |
| Responsive spacing with CSS overrides | | ✓ |
| Values that should be inspectable in browser DevTools | | ✓ |
| Content fields (text, images, links) | ✓ | |
| Custom CSS fields (theme or element level) | | ✓ |
| Computed values in `calc()` expressions | | ✓ |
| Design tokens that don't change per page | | ✓ |

### Divi's Internal CSS Custom Properties

!!! info "🔬 Needs Testing"
    Divi 5 may generate its own CSS custom properties (e.g., `--et-*` or `--divi-*` prefixed variables) during rendering. These could provide advanced customization hooks if documented. The existence, naming convention, stability, and public API status of any internal custom properties need verification.

<!-- TODO: Inspect Divi 5 rendered output for --et-* or --divi-* custom properties -->
<!-- TODO: Test whether internal custom properties are considered public API or implementation details -->

## Practical Patterns

### Fluid Typography Without Breakpoints

Instead of setting different font sizes at each breakpoint, use `clamp()` for smooth scaling across all screen sizes:

```css
/* In a heading font-size field */
clamp(24px, 3vw + 12px, 56px)
```

This produces:
- ~24px at 320px viewport (mobile)
- ~36px at 768px viewport (tablet)
- ~56px at 1440px+ viewport (desktop)

Set it once and it scales smoothly. No media queries required.

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

Now when the header height changes, update one property instead of finding every `calc()` reference.

### Responsive Section Padding

```css
/* In a section padding field — works across all devices */
clamp(30px, 6vw, 80px)
```

Actual values:
- At 320px viewport: ~30px (6vw = 19.2px, below minimum)
- At 768px viewport: ~46px (6vw = 46px, within bounds)
- At 1440px viewport: 80px (6vw = 86.4px, above maximum)

### Responsive Grid Gaps

```css
/* In a CSS Grid gap field */
clamp(12px, 2vw, 32px)
```

Gaps scale smoothly from 12px on small screens to 32px on large screens.

### Aspect Ratio Containers

Use percentage padding to create aspect-ratio containers without modern CSS (useful for sections with background images):

```css
/* In a section padding-bottom field for 16:9 aspect ratio */
56.25%

/* For 4:3 aspect ratio */
75%

/* For a square (1:1 aspect ratio) */
100%
```

The width is set to 100%, padding-bottom creates the height via the percentage of width.

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
/* Auto-responsive grid — no breakpoints needed */
display: grid;
grid-template-columns: repeat(auto-fill, minmax(var(--card-min-width), 1fr));
gap: var(--card-gap);
padding: var(--card-padding);
border-radius: var(--card-radius);
```

Each card automatically wraps to the next line when there's not enough space for another full card.

## Data Storage & Programmatic Access

!!! info "🔬 Needs Testing"
    Advanced unit values (including `calc()`, `clamp()` expressions, and `var()` references) are stored as raw strings in the element's layout JSON. CSS custom properties defined in Theme Options or page settings are stored as part of the Custom CSS field value.

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read field value | Layout JSON inspection or `get_post_meta()` | 🔬 Testing needed | Functions stored as complete strings, e.g. `"clamp(16px, 2vw, 24px)"` |
| Modify field value | Layout JSON update or `update_post_meta()` | 🔬 Testing needed | Must preserve entire expression syntax including spaces |
| Define CSS custom property | Write to Theme Options Custom CSS or page Custom CSS | 🔬 Testing needed | Standard CSS syntax in the appropriate scope field |
| Read CSS custom properties | Parse the Custom CSS field value | 🔬 Testing needed | No dedicated API endpoint — parse from CSS text |

<!-- TODO: Verify how calc/clamp expressions are stored in layout JSON — raw string or parsed tokens? -->
<!-- TODO: Test whether CSS custom properties defined at element scope are available in sibling elements -->
<!-- TODO: Determine if internal custom properties (--et-*, --divi-*) are documented or accessible via API -->

## Version Notes

!!! note "Divi 5 Only"
    The advanced unit picker with `calc()`, `clamp()`, `min()`, `max()`, keywords, and `var()` support is new to Divi 5. Divi 4 supported only static numeric values with basic unit selection — no functions or custom properties in numeric fields.

## Related

- [Advanced Units (Builder)](../builder/advanced-units.md) — Unit picker UI, field behavior, and supported formats
- [Design Variables (CSS Reference)](design-variables.md) — How design variables differ from CSS custom properties and when to use each
- [Design System Workflow](design-system-workflow.md) — Using variables and functions in a systematic design approach
- [Relative Colors & HSL](relative-colors-hsl.md) — HSL color functions for derived color values
- [Common Overrides](common-overrides.md) — CSS snippets using standard units and selectors
- [Responsive Options (Builder)](../builder/responsive-options.md) — Divi's built-in responsive controls as an alternative to CSS functions
- [Custom Breakpoints (Builder)](../builder/custom-breakpoints.md) — When you need media query breakpoints beyond what `clamp()` can handle
