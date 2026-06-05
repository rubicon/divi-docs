---
title: "Copy & Paste Attributes"
description: "Divi 5 Copy and Paste Attributes — transfer content, styles, and presets between elements with granular paste options and keyboard shortcuts."
category: builder
tags: ["builder", "attributes", "copy-paste", "styles", "workflow"]
related: ["find-replace-attributes", "right-click-menus", "keyboard-shortcuts"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13309833"
---

# Copy & Paste Attributes

Transfer content, styles, and presets between elements without cloning the entire element.

!!! abstract "Quick Reference"
    **What it does:** Copies content, styles, and/or presets from one element and pastes them onto another with granular control.
    **Where to find it:** Right-click → Copy Attributes / Paste options, or Cmd/Ctrl + Shift + C/V shortcuts.
    **Key features:**

    - Eight paste variants: All, Design, Content, Presets, and four "Select" options for cherry-picking
    - Scoped copy/paste at tab, option group, or individual field level
    - **Gradient fields** (Divi 5.7+) copy and paste as a single unified attribute — stops, type, and direction move together
    - Cross-module compatibility: Divi matches compatible attributes between different module types
    - Reset options to revert any paste operation

    **ET Docs:** [Copy & Paste Attributes](https://help.elegantthemes.com/en/articles/13309833){:target="_blank"}

## Overview

Divi 5 introduces a granular attribute management system that lets you copy specific parts of an element -- its content, its design styles, its preset assignments, or any combination -- and paste them onto another element. This is far more flexible than simply duplicating an element because you control exactly which properties transfer. For the official Elegant Themes reference, see [Copy & Paste Attributes](https://help.elegantthemes.com/en/articles/13309833){:target="_blank"}.

The system works at multiple levels of specificity: you can copy an entire element's attributes, a single settings tab (Content, Design, Advanced), a specific option group (Background, Button, Title Text), or even an individual field.

## Attribute Types

Divi 5 organizes element attributes into three categories:

| Type | What It Includes |
|------|-----------------|
| **Content** | Text, images, icons, links, and other data entered in the Content tab. |
| **Styles** | All design settings from the Design and Advanced tabs: colors, fonts, spacing, borders, shadows, transforms, etc. |
| **Presets** | The element presets and option group presets assigned to the element. |

## How to Copy Attributes

### Right-Click Method

1. Right-click the source element on the canvas (or in the Layers panel).
2. Select **Copy Attributes**.
3. All three attribute types (content, styles, presets) are placed on the clipboard.

### Keyboard Shortcut

Select the source element and press:

- **Mac**: Cmd + Shift + C
- **Windows**: Ctrl + Shift + C

## Paste Options

After copying attributes, right-click the target element and choose from the following paste options:

| Paste Option | What It Transfers |
|-------------|------------------|
| **Paste All Attributes** | Content, styles, and presets. The target becomes a near-clone of the source. |
| **Paste Design Attributes** | Styles and presets only. The target keeps its own content. |
| **Paste Content Attributes** | Content only. The target keeps its existing styles and presets. |
| **Paste Presets** | Preset assignments only. The target keeps its content and any non-preset style overrides. |
| **Paste Select Design Attributes** | Opens a picker so you can choose which modified styles and presets to apply. |
| **Paste Select Style Attributes** | Modified styles only (no presets, no content). |
| **Paste Select Content Attributes** | Opens a picker for selective content field pasting. |
| **Paste Select Presets** | Selective preset application, useful when the source has multiple nested presets. |

### Keyboard Paste Shortcuts

| Action | Mac | Windows |
|--------|-----|---------|
| **Paste All Attributes** | Cmd + Shift + V | Ctrl + Shift + V |
| **Paste Design Attributes** | Option + Cmd + V | Alt + Ctrl + V |

## Reset Options

If a paste operation produces undesired results, right-click the element and choose a reset option:

| Reset Option | What It Reverts |
|-------------|----------------|
| **Reset All Attributes** | Content, styles, and presets back to defaults. |
| **Reset Design Attributes** | Styles and presets only. |
| **Reset Style Attributes** | Styles only (presets remain). |
| **Reset Content Attributes** | Content only. |
| **Reset Presets** | Preset assignments only. |

## Scoped Copy & Paste

You do not have to copy at the element level. Right-click within specific areas of the settings panel to copy at narrower scopes:

| Scope | Example |
|-------|---------|
| **Tab level** | Right-click the Content tab header to copy all content settings. |
| **Option group level** | Right-click the Background group to copy only background settings. |
| **Field level** | Right-click an individual color picker or spacing field to copy that single value. |

This is useful when you want to transfer one group of settings (e.g., just the border styles) from one element to another without touching anything else.

## Typical Workflows

### Standardizing Button Styles Across a Page

1. Design a button with your desired colors, font, padding, and border radius.
2. Right-click the button and select **Copy Attributes**.
3. Right-click each other button and select **Paste Design Attributes**.
4. Every target button inherits the design while keeping its own label and link.

### Transferring a Background Between Section Types

1. Right-click the section with the gradient background.
2. Navigate to the Background option group in the right-click submenu and select **Copy**.
3. Right-click the target section's Background option group and select **Paste**.
4. Only the background transfers -- all other styles stay intact.

### Selective Preset Application

1. Copy attributes from a module that uses multiple stacked/nested presets.
2. On the target, choose **Paste Select Presets**.
3. Pick only the presets you want to apply, leaving others unchanged.

## Version Notes

!!! note "Divi 5 Only"
    The granular attribute copy/paste system (with separate content, style, and preset paste options) is new to Divi 5. Divi 4 supports copying and pasting module styles but does not offer the same level of granularity.

## Related

- [Find & Replace Attributes](find-replace-attributes.md) -- Bulk value replacement across elements
- [Right-Click Menus](right-click-menus.md) -- Where paste options live
- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Shortcut reference for copy/paste
- [Element Presets](element-presets.md) -- Understanding preset assignments
