---
title: "Relative Colors & HSL"
description: "Divi 5 relative colors — derive hover states, dark variants, and color harmonies from base colors using HSL offset filters with automatic cascade updates."
category: css-reference
tags: [colors, hsl, relative-colors, hover-states, color-system, design-system]
related: [design-variables, design-system-workflow, common-overrides]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11631084"
---

# Relative Colors & HSL — CSS Reference

How Divi 5's relative color system translates to CSS, practical patterns for derived color palettes, and when to use relative colors vs. separate variables.

!!! abstract "Quick Reference"
    **What this covers:** The CSS and developer perspective on Divi 5's HSL-based relative color system — what the browser sees, how to build efficient palettes, and accessibility considerations.
    **Builder UI docs:** See [Relative Colors & HSL (Builder)](../builder/relative-colors-hsl.md) for the color picker interface and Color Filters drawer.
    **Key takeaway:** Relative colors resolve to static hex/RGBA values in CSS output. The HSL offset relationship exists in Divi's data layer, not in the browser.

    **ET Docs:** [Relative Colors (HSL)](https://help.elegantthemes.com/en/articles/11631084){:target="_blank"}

## How Relative Colors Work

Divi 5's color system uses HSL (Hue, Saturation, Lightness) as its native model. Every color in the color picker can be modified with relative offset filters:

```
Base Color + HSL Offsets = Derived Color
```

The offsets are stored as deltas, not absolute values. When the base color changes, the same offsets are reapplied to produce a new derived color that maintains the same relationship.

**Example:**

- Base: `#1A73E8` (Primary Blue, HSL roughly 217, 82%, 50%)
- Offset: Lightness -15%
- Result: `#1557B0` (darker blue for hover state)

Change the base to `#E84315` (orange) — the offset produces a darker orange, maintaining the same "15% darker" relationship.

## CSS Output

Like [design variables](design-variables.md), relative colors resolve to static values in the rendered CSS. The browser never sees an HSL relationship or offset calculation.

```css
/* What the browser receives */
.et_pb_button_0 {
    background-color: #1A73E8;  /* Base color */
}

.et_pb_button_0:hover {
    background-color: #1557B0;  /* Derived color — resolved from base - 15% lightness */
}
```

!!! warning "Observed Behavior"
    The HSL offset relationship exists only in Divi's data layer. You cannot inspect the relationship in DevTools — you see only the resolved hex or RGBA values. Changing the base color requires Divi to recalculate all derived colors and regenerate CSS.

**Implications for developers:**

- Cannot use CSS `color-mix()` or `hsl()` functions to replicate the relationship
- No `var()` reference to the base color in the output
- Override with standard CSS specificity rules — the derived value is just a static color

## Practical Color Patterns

These patterns reduce the number of manually defined colors by deriving related values from a single base.

### Hover States

Darken the base color by reducing lightness. This is the most common use case.

| Interaction | HSL Offset | Effect |
|-------------|-----------|--------|
| Button hover | Lightness: -15% | Noticeably darker, clear feedback |
| Link hover | Lightness: -10% | Subtle darkening |
| Card hover background | Lightness: -5% | Gentle surface shift |
| Active/pressed state | Lightness: -20% | Deeper press effect |

**CSS equivalent** (for context — Divi handles this through the Color Filters drawer):

```css
/* If you were writing this manually */
.button { background-color: hsl(217, 82%, 50%); }
.button:hover { background-color: hsl(217, 82%, 35%); } /* -15% lightness */
```

### Light Backgrounds from Bold Colors

Create tinted section backgrounds from brand colors.

| Pattern | HSL Offset | Effect |
|---------|-----------|--------|
| Light tint | Lightness: +40%, Saturation: -20% | Soft pastel background |
| Very light tint | Lightness: +45%, Saturation: -30% | Nearly white with a color hint |
| Medium tint | Lightness: +25%, Saturation: -10% | Noticeable but not overwhelming |

**Example flow:** Primary Brand `#1A73E8` with Lightness +40%, Saturation -20% produces a soft blue-grey suitable for alternating section backgrounds.

### Complementary and Accent Colors

Shift hue to create color harmonies.

| Pattern | HSL Offset | Effect |
|---------|-----------|--------|
| Complementary | Hue: +180° | Opposite on the color wheel |
| Analogous warm | Hue: +30° | Adjacent warm color |
| Analogous cool | Hue: -30° | Adjacent cool color |
| Triadic | Hue: +120° or -120° | One third around the wheel |
| Split complementary | Hue: +150° or +210° | Near-complementary pair |

!!! tip "Use sparingly"
    Hue shifts are useful for generating accent colors during design exploration. For production sites, verify the derived colors meet your brand guidelines — mathematical color harmony does not always match brand identity.

### Muted and Desaturated Variants

Reduce saturation for secondary or background uses of a bold color.

| Pattern | HSL Offset | Effect |
|---------|-----------|--------|
| Muted variant | Saturation: -30% | Toned down for secondary use |
| Greyscale hint | Saturation: -60% | Nearly grey with a color hint |
| Neutral from color | Saturation: -80%, Lightness: +20% | Warm/cool grey derived from brand |

### Transparent Overlays

Reduce opacity to create color washes over backgrounds or images.

| Pattern | Opacity Offset | Effect |
|---------|---------------|--------|
| Image overlay | Opacity: 70-80% (reduce to 20-30%) | Color wash over hero images |
| Subtle tint | Opacity: 90-95% (reduce to 5-10%) | Barely visible color layer |
| Glass effect | Opacity: 60-70% (reduce to 30-40%) | Semi-transparent surface |

## Relative Colors vs. Separate Variables

Not every color relationship should be a relative color. Use the right tool for the situation.

| Scenario | Use Relative Colors | Use Separate Variables |
|----------|--------------------|-----------------------|
| Hover state of a button | Yes — should always track the button color | No |
| Light background from brand color | Yes — should shift when brand color changes | No |
| Warning/error/success status colors | No — these have fixed meaning | Yes |
| Two brand colors with no mathematical relationship | No — they are independent choices | Yes |
| Dark mode version of a color | Maybe — if the light/dark relationship is a consistent offset | Maybe — if dark mode colors are independently chosen |
| Text color on a colored background | Maybe — if derived from the background for guaranteed contrast | Yes — if the text color is an independent brand choice |

**Rule of thumb:** If changing the base color should automatically change the derived color, use a relative color. If the two colors happen to be related today but could diverge tomorrow, use separate variables.

## Building an Efficient Palette

Combine [design variables](design-variables.md) with relative colors to minimize the number of things you need to manage.

### Minimal Variable Set

| Variable | Value | Derived Colors (via relative offsets) |
|----------|-------|--------------------------------------|
| Primary Brand | `#1A73E8` | Primary Hover (-15% L), Primary Light (+40% L, -20% S), Primary Muted (-30% S) |
| Secondary Brand | `#E84315` | Secondary Hover (-15% L), Secondary Light (+40% L, -20% S) |
| Dark Text | `#1A1A2E` | — (no derivatives needed) |
| Body Text | `#555555` | — (no derivatives needed) |
| Light Background | `#F8F9FA` | — (or derive from Primary Brand +45% L, -30% S) |

With 5 variables and relative offsets, you get 10+ usable colors. Without relative colors, you would need 10+ separate variables.

## Color Accessibility

Relative colors can help or hurt accessibility depending on how offsets are chosen.

### Maintaining WCAG Contrast

When deriving text colors or interactive state colors, verify that the lightness offset maintains sufficient contrast:

| WCAG Level | Required Contrast Ratio | Applies To |
|------------|------------------------|------------|
| AA (normal text) | 4.5:1 | Body text, links |
| AA (large text) | 3:1 | Headings 18px+, bold 14px+ |
| AAA (normal text) | 7:1 | Enhanced accessibility |

**Lightness offset guidelines for contrast:**

| Base Lightness | Offset for AA on White | Offset for AA on Dark |
|----------------|----------------------|---------------------|
| 50% (medium) | No offset needed (4.5:1 usually met) | Lightness +30% or more |
| 30% (dark) | Works on white already | Lightness +40% or more |
| 70% (light) | Lightness -25% or more | No offset needed |

!!! warning "Always Test"
    HSL lightness is not perceptually uniform — a 15% lightness change produces different perceived contrast depending on the hue. Blue appears darker than yellow at the same HSL lightness. Always verify contrast ratios with a tool like [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

### Safe Hover State Patterns

For interactive elements, the hover state must also maintain adequate contrast:

```
Base color on white background: 4.5:1 contrast ✓
Hover color (lightness -15%) on white background: Still 4.5:1? ✓ (darker = more contrast)
Hover color (lightness +15%) on white background: Still 4.5:1? ⚠️ Check — lighter = less contrast
```

Darkening for hover states is generally safe for contrast. Lightening is risky — always verify.

## AI Interaction Notes

!!! info "Data Storage — 🔬 Needs Testing"
    Relative color data is likely stored as a compound object in the element's attributes: a reference to the base color (either a static value or a variable ID) plus HSL and opacity offset values. The exact data format needs verification.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read derived color | Layout JSON inspection | 🔬 Needs Testing | Look for objects with base + offset fields rather than flat hex strings |
| Read resolved value | Render the page and inspect CSS output | 🔬 Needs Testing | The CSS output contains the resolved static value |
| Modify base color | Update the variable or static value | 🔬 Needs Testing | All derived colors recalculate on next render |
| Modify offsets | Update the offset values in the element's attributes | 🔬 Needs Testing | Must preserve the base reference |

<!-- TODO: Verify storage format — is it {base_color, hue_offset, saturation_offset, lightness_offset, opacity_offset}? -->
<!-- TODO: Test whether relative color relationships are preserved in Divi Library exports or flattened to static values -->
<!-- TODO: Check if relative colors work with CSS custom properties entered in the color picker -->

## Version Notes

!!! note "Divi 5 Only"
    The Color Filters drawer and HSL-native color model are new to Divi 5. Divi 4's color picker supported hex and RGB input but did not provide relative color offset functionality.

## Related

- [Relative Colors & HSL (Builder)](../builder/relative-colors-hsl.md) — Color picker UI and Color Filters drawer walkthrough
- [Design Variables (CSS Reference)](design-variables.md) — Variable types including color variables
- [Design Variables (Builder)](../builder/design-variables.md) — Creating and managing color variables
- [Global Variables](../builder/global-variables.md) — Site-wide color variables and the global palette
- [Design System Workflow](design-system-workflow.md) — Using relative colors within a systematic design approach
- [Common Overrides](common-overrides.md) — CSS color overrides for when builder controls are insufficient
