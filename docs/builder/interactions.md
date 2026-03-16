---
title: "Interactions"
description: "Divi 5 Interactions — define trigger-effect pairs for clicks, hovers, scrolls, and page loads to create dynamic behaviors without custom JavaScript."
category: builder
tags: ["builder", "interactions", "animations", "triggers", "effects", "dynamic"]
related: ["canvases", "condition-options", "presets"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11666517"
---

# Interactions

Define event-driven behaviors that respond to clicks, hovers, scrolling, and other user actions to create dynamic, animated page experiences without custom JavaScript.

!!! abstract "Quick Reference"
    **What it does:** Attaches trigger-effect pairs to elements for dynamic behaviors like popups, toggles, scroll animations, and more.
    **Where to find it:** Any element's settings → Advanced Tab → Interactions → Add Interaction.
    **Key features:**

    - Eight trigger types: Click, Mouse Enter/Exit, Viewport Enter/Exit, Load, Breakpoint Enter/Exit
    - Effects: Toggle/Show/Hide visibility, Add/Remove/Toggle presets and attributes, cookies, scroll-to, mirror mouse
    - Target options: Self, Parent, Child, or any element via CSS selector
    - Multiple interactions per element, each with independent trigger, effect, and target

    **ET Docs:** [Interactions](https://help.elegantthemes.com/en/articles/11666517){:target="_blank"}

## Overview

The Interactions system in Divi 5 lets you attach trigger-effect pairs to any element. When a specified event occurs (a click, a hover, a scroll position), one or more effects execute on target elements. Effects include toggling visibility, applying or removing presets, manipulating HTML attributes, managing cookies, scrolling to elements, and mirroring mouse movement.

Interactions replace the need for custom JavaScript in most common dynamic UI scenarios: popups, content toggles, scroll-triggered animations, pricing table switchers, and more. They integrate tightly with [Canvases](canvases.md) for off-canvas content patterns and with [Condition Options](condition-options.md) for conditional display logic.

For the official Elegant Themes documentation, see [Interactions](https://help.elegantthemes.com/en/articles/11666517).

## Core Components

Every interaction requires three components:

| Component | Description |
|-----------|-------------|
| Trigger | The event that initiates the interaction (click, hover, scroll, page load, etc.) |
| Effect | The action that executes when the trigger fires (show/hide element, apply preset, set cookie, etc.) |
| Target | The element(s) affected by the effect (self, parent, child, or any element via CSS selector) |

## Trigger Types

| Trigger | Description |
|---------|-------------|
| Click | Fires when the user clicks or taps the element |
| Mouse Enter | Fires when the cursor moves over the element |
| Mouse Exit | Fires when the cursor leaves the element |
| Viewport Enter | Fires when the element scrolls into the visible viewport |
| Viewport Exit | Fires when the element scrolls out of the visible viewport |
| Load | Fires when the page finishes loading |
| Breakpoint Enter | Fires when the browser window enters a specified responsive breakpoint |
| Breakpoint Exit | Fires when the browser window leaves a specified responsive breakpoint |

## Available Effects

### Visibility Effects

| Effect | Description |
|--------|-------------|
| Toggle Visibility | Switches the target element between visible and hidden states |
| Show Element | Makes a hidden target element visible |
| Hide Element | Hides a visible target element |

### Preset Effects

| Effect | Description |
|--------|-------------|
| Toggle Preset | Switches a preset on and off on the target element, with optional replacement preset |
| Add Preset | Applies a preset style class to the target element |
| Remove Preset | Removes a preset style class from the target element |

### Attribute Effects

| Effect | Description |
|--------|-------------|
| Toggle Attribute | Adds or removes an HTML attribute value on the target |
| Add Attribute | Adds an HTML attribute to the target if not already present |
| Remove Attribute | Removes an HTML attribute from the target |

### Cookie Effects

| Effect | Description |
|--------|-------------|
| Toggle Cookie | Adds or removes a browser cookie |
| Add Cookie | Creates a cookie with a specified name and value |
| Remove Cookie | Deletes a specified cookie |

### Other Effects

| Effect | Description |
|--------|-------------|
| Scroll To Element | Smoothly scrolls the page to bring the target element into the viewport |
| Mirror Mouse Movement | Makes the target element follow the cursor position using translate, scale, opacity, tilt, or rotate transformations with adjustable sensitivity |

## Target Options

The target determines which element(s) the effect acts upon:

| Target Type | Description |
|-------------|-------------|
| Self | The effect applies to the same element that has the interaction |
| Parent | The effect applies to the parent container of the trigger element |
| Child | The effect applies to a child element within the trigger element |
| CSS Selector | The effect targets any element on the page matching a specified CSS ID or class |

Using CSS selectors as targets is essential for cross-element interactions, such as a button that shows or hides a section elsewhere on the page.

## Setting Up an Interaction

1. Select the element that will serve as the trigger in the Visual Builder.
2. Open the element's settings panel.
3. Navigate to the **Advanced Tab**.
4. Scroll to the **Interactions** option group.
5. Click **Add Interaction** to open the interaction editor.
6. Select a **Trigger** from the available trigger types.
7. Choose an **Effect** from the effects list.
8. Define the **Target** element(s).
9. Configure effect-specific settings (animation duration, delay, sensitivity).
10. Save and preview the interaction.

You can add multiple interactions to a single element. Each interaction operates independently with its own trigger, effect, and target.

## Effect Settings

Each effect type has configurable parameters:

| Setting | Type | Description |
|---------|------|-------------|
| Duration | Time input | How long the effect animation takes to complete |
| Delay | Time input | Time to wait before the effect begins after the trigger fires |
| Sensitivity | Range (Mirror Mouse only) | How closely the target follows mouse movement |
| Movement Type | Dropdown (Mirror Mouse only) | Translate, scale, opacity, tilt, or rotate |

## Common Patterns

### Popup / Modal Dialog

1. Design the popup content in a Section on a separate [Canvas](canvases.md).
2. Set the section's position to **Fixed** with a high **Z-index**.
3. Add a **Load** trigger with a **Hide Element** effect targeting the popup section (hidden by default).
4. On the trigger button, add a **Click** trigger with **Show Element** targeting the popup.
5. On a close button within the popup, add a **Click** trigger with **Hide Element** targeting the popup.

### Content Toggle (e.g., Pricing Monthly/Annual)

1. Create two content modules (monthly pricing, annual pricing).
2. Hide one by default using a Load interaction.
3. On toggle button A, add a **Click** trigger with **Show Element** for content A and **Hide Element** for content B.
4. On toggle button B, add the inverse effects.

### Scroll-Triggered Reveal

1. Add a **Viewport Enter** trigger to the target element.
2. Set the effect to **Add Preset** with an animation preset that includes a fade-in or slide-in transition.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Interactions are a new system in Divi 5, replacing and extending the limited hover and animation options in Divi 4.

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Interaction definitions are stored as attributes on the block that owns the interaction. Each interaction likely appears as a JSON object within the block's `attrs` containing the trigger type, effect type, target selector, and effect configuration parameters.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Parse the block's `attrs` for interaction-related keys in `post_content` JSON | Needs Testing | Look for an `interactions` array or similarly named attribute containing trigger/effect/target objects |
| Modify | Update the interaction objects within the block's `attrs` and serialize back | Needs Testing | Each interaction object likely contains `trigger`, `effect`, `target`, and `settings` keys |
| Create | Add a new interaction object to the block's interactions attribute array | Needs Testing | Must match the expected schema for trigger type, effect type, and target format |

!!! warning "Cross-Element References"
    Interactions that target elements via CSS selectors store string references (class names or IDs). If the target element's selector changes, the interaction will silently fail. When programmatically modifying element classes or IDs, check for interaction references that may need updating.

## Troubleshooting

!!! warning "Interaction Not Firing"
    Verify that the trigger element is accessible and clickable on the front end. Elements with zero dimensions, hidden overflow, or covered by other elements may not receive the expected events.

!!! warning "Effect Targets Wrong Element"
    When using CSS selectors as targets, ensure the selector is unique if you intend to affect only one element. A class selector will affect all elements with that class.

!!! warning "Cookie Effects Not Persisting"
    Cookie effects depend on the browser's cookie settings. If the visitor has cookies disabled or is using a privacy-focused browser, cookie-based interactions will not persist across page loads.

## Related

- [Canvases](canvases.md)
- [Condition Options](condition-options.md)
- [Presets](presets.md)
- [Visual Builder](visual-builder.md)
- [Animation Options](../options-groups/animation.md) — Entrance animations that complement interactions
- [Transform Options](../options-groups/transform.md) — Transform properties driven by interaction triggers
- [Scroll Effects Options](../options-groups/scroll-effects.md) — Scroll-driven effects as an alternative to click/hover
