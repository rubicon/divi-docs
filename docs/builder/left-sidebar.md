---
title: "Left Sidebar"
description: "Divi 5 Left Sidebar reference — every panel and toggle in the persistent vertical toolbar, including Layers, Presets, Variables, and more."
category: builder
tags: ["builder", "sidebar", "panels", "navigation", "workflow"]
related: ["vb-interface", "layers-view", "wireframe-view"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10469656"
---

# Left Sidebar

The persistent vertical toolbar on the left side of the Divi 5 Visual Builder, providing one-click access to every major panel and editing mode.

!!! abstract "Quick Reference"
    **What it does:** Houses all major builder panels and mode toggles in a slim vertical strip.
    **Where to find it:** Always visible on the left edge of the Visual Builder canvas.
    **Key features:**

    - Layout and content panels: Add Layout, Layers, Style Inspector, Variable Manager, Preset Manager, Page Manager, Command Center
    - Display controls: Action Icons, Parent Icons, X-Ray Mode, Wireframe View
    - Settings and support: Builder Settings, Help, Light/Dark Mode

    **ET Docs:** [Divi Left Sidebar](https://help.elegantthemes.com/en/articles/10469656){:target="_blank"}

## Overview

The Left Options Sidebar is one of the most significant interface changes in Divi 5. It replaces the bottom-docked toolbar approach of Divi 4 with a slim vertical strip of icons that stays visible at all times without obscuring the design canvas. Each icon opens a specific panel or toggles an editing mode. For the official Elegant Themes reference, see [Divi Left Sidebar](https://help.elegantthemes.com/en/articles/10469656){:target="_blank"}.

The sidebar is divided into three logical groups: layout and content tools at the top, display and mode controls in the middle, and settings and support at the bottom.

## Sidebar Panels

### Add Layout

Opens the Divi Library browser where you can insert premade layouts from the Elegant Themes library, your own saved layouts, or layouts from your Divi Cloud account. You can also clone an existing page directly from this panel.

### Layers View

Toggles the [Layers View](layers-view.md) panel, which displays a collapsible tree of every section, row, column, and module on the page. From the tree you can click to select elements, drag to reorder them, and right-click for context menu operations.

### Style Inspector

Displays a read-only summary of the styles, content, and presets applied to the currently selected element. This is useful for understanding where a particular style comes from -- whether it is set at the element level, inherited from a preset, or derived from a global variable.

### Variable Manager

Create, edit, and organize global design variables for colors, fonts, and spacing values. Variables defined here can be referenced throughout your presets and element settings, making site-wide design changes a single-edit operation.

### Preset Manager

A centralized interface for managing [element presets](element-presets.md) and option group presets across your entire site. You can browse presets by element type, create new ones, edit existing presets, and set defaults -- all without navigating to individual element settings.

### Page Manager

Browse and manage all Divi-enabled pages on your site without leaving the Visual Builder. Switch to a different page for editing, view page status, or create new pages directly from this panel.

### Command Center

A searchable command palette that lets you execute builder actions by typing. You can add elements, navigate to settings, switch modes, and trigger operations without mousing through menus. This is the hub of a keyboard-driven workflow.

### Wireframe View

Switches the canvas to [Wireframe View](wireframe-view.md), which strips away visual styling and displays all elements as labeled structural blocks. Toggle back to the visual canvas by clicking the same icon again.

## Display Controls

### Action Icons on Hover

When enabled (the default), hovering over any element on the canvas reveals its action toolbar with icons for settings, duplicate, and delete. Disable this if you prefer a cleaner canvas and want to access actions via right-click or the Layers panel instead.

### Parent Action Icons on Hover

When enabled (the default), hovering over a child element also reveals action icons on its parent containers (row, section). This makes it easy to jump up the hierarchy without switching to Layers View.

### X-Ray Mode

Toggles outlines around every layout element on the canvas -- sections, rows, columns, and modules. X-Ray mode is helpful for identifying empty containers, overlapping elements, or understanding the nesting structure of a complex layout.

## Settings & Support

### Builder Settings

Opens the builder preferences panel where you can configure defaults for the entire editor experience. Available settings include:

| Setting | Description |
|---------|-------------|
| **Default View Mode** | Visual or Wireframe when entering the builder. |
| **History State Interval** | Frequency of auto-save snapshots. |
| **Modal Default Position** | Where settings panels appear (floating, sidebar, fullscreen, bottom). |
| **New Page Default** | Behavior when creating a new page. |
| **Top Bar Icon Visibility** | Show or hide specific top-bar icons. |
| **Disabled Element Opacity** | Whether disabled elements render at reduced opacity. |
| **Toggle Grouping** | Whether setting groups open collapsed or expanded by default. |
| **Placeholder Content** | Whether new modules are pre-filled with demo content. |
| **Interface Mode** | Switch between standard and streamlined editing. |
| **Color Scheme** | Pick a UI accent color (blue, purple, green, red, orange). |
| **Admin Bar Visibility** | Show or hide the WordPress admin bar in the builder. |

### Help

Opens the help overlay with links to Elegant Themes documentation, video tutorials, and the full [keyboard shortcuts](keyboard-shortcuts.md) reference.

### Light / Dark Mode

Toggle the editor between a light and dark color scheme. This is a cosmetic preference and does not affect your page design.

## Version Notes

!!! note "Divi 5 Only"
    The left sidebar is a Divi 5 feature. Divi 4 uses a bottom-docked toolbar for equivalent controls. The Style Inspector, Variable Manager, Preset Manager, Page Manager, Command Center, and X-Ray Mode are all new to Divi 5.

## Related

- [Visual Builder Interface](vb-interface.md) -- Full interface overview
- [Layers View](layers-view.md) -- Tree-based element navigation
- [Wireframe View](wireframe-view.md) -- Structural editing mode
- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Hotkey reference
