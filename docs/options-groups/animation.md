---
title: "Animation Options"
category: options-groups
tags: ["options-groups", "animation", "design", "styling"]
related: ["transform", "transitions", "scroll-effects"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102631"
---

# Animation Options

The Animation options group adds entrance motion effects to Divi 5 modules, making elements animate into view as the page loads or scrolls.

## Overview

The Animation options group lets you apply motion effects that trigger when an element enters the viewport, bringing your layouts to life with dynamic entrance animations. These effects can make content feel more engaging and guide the user's eye through the page as they scroll.

You will find the Animation controls in the Design tab of any module's settings panel. The group includes a style selector for choosing the type of animation, along with fine-tuning controls for duration, delay, opacity, easing, and whether the animation loops or plays once.

By combining different animation styles with staggered delay values across multiple modules, you can create cascading reveal effects where content appears in sequence. The speed curve setting provides additional control over how the animation accelerates and decelerates, letting you achieve either mechanical or natural-feeling motion.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102631).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Animation Style | Dropdown select | Chooses the type of entrance animation applied to the element. Options include fade, slide, zoom, bounce, and other preset styles. |
| Animation Duration | Range slider | Controls how long the animation takes to complete one full cycle, measured in milliseconds. |
| Animation Delay | Range slider | Sets the wait time before the animation begins after the element enters the viewport, measured in milliseconds. |
| Animation Starting Opacity | Range slider | Defines the initial transparency of the element at the start of the animation. A value of 0% means fully transparent; 100% means fully opaque. |
| Animation Speed Curve | Dropdown select | Selects the easing function that governs the animation's acceleration pattern. Options include Ease-In, Ease-Out, Ease-In-Out, and Linear. |
| Animation Repeat | Toggle / select | Determines whether the animation plays once and stops or loops continuously. |

## Which Elements Use This

The Animation options group is available on all Divi 5 modules. It is most commonly used on content modules like Text, Image, Blurb, and Call to Action to create entrance effects as users scroll through the page. Structural elements (sections, rows, columns) may also support animation settings.

## Code Examples

Create a simple fade-in-up animation with CSS:

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.my-module {
  animation: fadeInUp 600ms ease-out forwards;
}
```

Stagger animations on a series of elements using delay:

```css
.column:nth-child(1) .my-module { animation-delay: 0ms; }
.column:nth-child(2) .my-module { animation-delay: 150ms; }
.column:nth-child(3) .my-module { animation-delay: 300ms; }
```

## Related

- [Transform Options](transform.md)
- [Transitions Options](transitions.md)
- [Scroll Effects Options](scroll-effects.md)
