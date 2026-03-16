---
title: "Transitions Options"
description: "Divi 5 Transitions options group — duration, delay, and speed curve controls for smooth hover-state animations on any element."
category: options-groups
tags: ["options-groups", "transitions", "design", "styling"]
related: ["animation", "transform"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102770"
---

# Transitions Options

The Transitions options group controls the timing and easing of hover-state animations on Divi 5 elements.

!!! abstract "Quick Reference"
    **What it controls:** Transition duration, delay, and speed curve for hover-state property changes
    **Where to find it:** Advanced Tab → Transitions
    **Available on:** All modules
    **Responsive:** Yes — transition values apply across all breakpoints
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102770)

## Overview

The Transitions options group manages how smoothly and quickly an element animates between its default state and its hover state. Whenever you configure hover-specific values for settings like color, size, transform, or opacity, the transition controls determine the speed and feel of that change.

These settings are located in the Advanced tab of any element's settings panel under the Transitions group. Unlike the Animation options group, which handles entrance effects, Transitions specifically govern the interactive behavior that occurs when a user hovers over an element with their cursor.

Getting transitions right is important for a polished user experience. Values between 300ms and 500ms typically feel natural and professional for most hover effects. Shorter durations create snappy, responsive interactions, while longer durations produce smoother, more deliberate changes. The speed curve setting adds further nuance by controlling whether the animation accelerates, decelerates, or moves at a constant rate.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102770).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Transition Duration | Numeric input (milliseconds) | Sets how long the hover animation takes to complete. For example, 300ms produces a smooth, natural feel while 100ms creates a fast, snappy response. |
| Transition Delay | Numeric input (milliseconds) | Defines the wait time before the hover animation begins. Useful for creating staggered effects on grouped elements. |
| Transition Speed Curve | Dropdown select | Controls the acceleration pattern of the animation. Options include: **Ease** (smooth acceleration and deceleration), **Linear** (constant speed), **Ease-In** (starts slow, speeds up), **Ease-Out** (starts fast, slows down), and **Ease-In-Out** (slow start and finish with faster middle). |

## Which Elements Use This

The Transitions options group is available on all Divi 5 modules. It applies whenever hover-state values are set on any design property within the module, controlling the smoothness of the change between default and hover states. It is found in the Advanced tab rather than the Design tab.

## Code Examples

Apply a smooth hover transition to a button module:

```css
.my-button {
  background-color: #2ea3f2;
  transition: all 400ms ease;
}

.my-button:hover {
  background-color: #1a8cd8;
  transform: translateY(-2px);
}
```

Use different speed curves for enter and exit transitions:

```css
.my-module {
  transition: transform 300ms ease-out, opacity 300ms ease-out;
}

.my-module:hover {
  transform: scale(1.03);
  opacity: 0.95;
}
```

Add a staggered transition delay on navigation items:

```css
.nav-item {
  transition: color 250ms ease 0ms;
}

.nav-item:nth-child(2) { transition-delay: 50ms; }
.nav-item:nth-child(3) { transition-delay: 100ms; }
```

## Related

- [Animation Options](animation.md)
- [Transform Options](transform.md)
- [Filters Options](filters.md) — Animate filter values on hover using transition timing
- [Box Shadow Options](box-shadow.md) — Smooth shadow changes on hover with transition duration
- [Interactions](../builder/interactions.md) — Advanced multi-step transitions triggered by user actions
