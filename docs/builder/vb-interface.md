---
title: "Visual Builder Interface"
description: "Divi 5 Visual Builder interface guide — top bar, left sidebar, central canvas, right settings panel, and interaction modes explained."
category: builder
tags: ["builder", "interface", "panels", "toolbar", "workspace"]
related: ["keyboard-shortcuts", "left-sidebar", "layers-view"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12991185"
---

# Visual Builder Interface

A guided tour of the Divi 5 Visual Builder workspace, covering every panel, toolbar, and interaction mode available in the editor.

!!! abstract "Quick Reference"
    **What it does:** Provides the complete workspace layout for the Divi 5 front-end editor.
    **Where to find it:** Loads automatically when you enable the Visual Builder on any page.
    **Key features:**

    - Top bar with device selector, zoom, history, and save controls
    - Left sidebar with panels for Layers, Presets, Variables, Pages, and more
    - Central canvas with click, hover, and grid interaction modes
    - Right settings panel with breadcrumb navigation and three-tab layout

    **ET Docs:** [Visual Builder Interface](https://help.elegantthemes.com/en/articles/12991185){:target="_blank"}

## Overview

The Divi 5 Visual Builder interface is organized into four primary areas: the **top bar**, the **left sidebar**, the **central canvas**, and the **right settings panel**. Together these regions give you fast access to every tool you need while keeping the editing canvas uncluttered. For the full Elegant Themes reference, see [Visual Builder Interface](https://help.elegantthemes.com/en/articles/12991185){:target="_blank"}.

Compared to Divi 4, the interface has been reorganized so that contextual tools live in a persistent left sidebar, settings open in a right-hand panel with breadcrumb navigation, and the top bar consolidates device previews, zoom, history, and save controls into a single strip.

## Top Bar

The top bar spans the full width of the editor and provides the controls you use most often while designing.

| Control | Description |
|---------|-------------|
| **Device Selector** | Switch between Desktop, Tablet, and Phone views. The canvas resizes to the selected breakpoint. |
| **Canvas Width** | Drag the edges of the preview area or type a custom pixel width to test arbitrary viewport sizes. |
| **Zoom** | Zoom in or out on the canvas for a bird's-eye view of the full page layout. |
| **History Controls** | Undo and redo buttons give quick access to the editing timeline. |
| **Save / Preview / Exit** | Save the current layout, preview the live page, or exit the Visual Builder. |

## Left Sidebar

The [left sidebar](left-sidebar.md) is a vertical toolbar that provides one-click access to the builder's major panels and modes. Each icon toggles a specific feature.

| Icon | Feature | Purpose |
|------|---------|---------|
| **Add Layout** | Opens the Divi Library and Cloud so you can insert premade or saved layouts. |
| **Layers View** | Toggles the [Layers View](layers-view.md) panel for structural navigation. |
| **Style Inspector** | Displays the styles, content, and presets applied to the selected element. |
| **Variable Manager** | Create and manage global design variables (colors, fonts, spacing). |
| **Preset Manager** | Centrally manage [element presets](element-presets.md) and option group presets. |
| **Page Manager** | Browse and switch between Divi-enabled pages without leaving the builder. |
| **Command Center** | A searchable command palette for executing actions quickly. |
| **Wireframe View** | Switches the canvas to [Wireframe View](wireframe-view.md). |
| **Action Icons Toggle** | Show or hide element action icons on hover. |
| **Parent Action Icons** | Show or hide parent-element action icons on hover. |
| **X-Ray Mode** | Displays outlines around all layout elements for structural clarity. |
| **Builder Settings** | Opens the global builder preferences panel. |
| **Help** | Access tutorials, documentation, and [keyboard shortcuts](keyboard-shortcuts.md). |
| **Light / Dark Mode** | Toggle the editor color scheme between light and dark. |

## Central Canvas

The central canvas is the main workspace where you design your page visually. It renders a live preview of your content and responds to whichever device breakpoint is active.

Key interactions on the canvas:

- **Click** any element to open its settings in the right panel.
- **Hover** over an element to reveal its action toolbar (duplicate, delete, move, settings).
- **Drag and drop** elements to reposition them within or across containers.
- **Right-click** any element to open the [right-click context menu](right-click-menus.md) with copy, paste, extend, lock, and other operations.
- **Resize** elements by dragging their edges to adjust padding, margin, or dimensions visually.

## Right Settings Panel

When you select an element on the canvas, its settings open in a panel on the right side of the screen. The panel includes:

- **Breadcrumb navigation** at the top showing the element hierarchy (Page > Section > Row > Column > Module). Click any level to jump to that parent element's settings.
- **Three tabs**: Content, Design, and Advanced, each grouping related settings.
- **Search bar** to quickly locate any setting by name.
- **Filter button** to narrow the view to modified styles, responsive styles, hover-state styles, or active content only.

### Content Tab

Houses content-specific settings that vary by element type: text, images, icons, links, backgrounds, and labels.

### Design Tab

Contains all visual styling controls: fonts, colors, spacing, sizing, borders, shadows, and more. Each setting supports responsive and hover-state values.

### Advanced Tab

Provides technical settings including Custom CSS, Visibility, Scroll Effects, Transitions, Conditions, and HTML Attributes.

## Interaction Modes

The Visual Builder offers three interaction modes, selectable from the left toolbar or bottom bar:

| Mode | Behavior |
|------|----------|
| **Hover Mode** | Element toolbars appear when you hover over an element. This is the default. |
| **Click Mode** | Element toolbars appear only when you click an element, reducing visual noise. |
| **Grid Mode** | All element toolbars and container outlines are visible at all times for maximum structural clarity. |

## Builder Settings

Click the Builder Settings icon in the left sidebar to customize the editor to your preferences.

| Setting | Description |
|---------|-------------|
| **Default View Mode** | Choose which view loads when you enter the builder (Visual, Wireframe). |
| **History State Interval** | How often auto-saves occur: after every action or every 10/20/30/40 actions. |
| **Modal Default Position** | Where settings panels appear: floating, fullscreen, fixed left/right, or fixed bottom. |
| **New Page Default** | What happens when you create a new page: Build from Scratch, Library, Clone, or Choose. |
| **Interface Color Scheme** | Pick a color accent for the builder UI (blue, purple, green, red, orange). |
| **Builder Animations** | Toggle interface animations when selecting objects. |
| **Show Disabled Modules** | Display disabled modules at reduced opacity while editing. |
| **Placeholder Content** | Whether new modules contain demo content when added. |
| **Admin Bar Visibility** | Show or hide the WordPress admin bar inside the builder. |

## Version Notes

!!! note "Divi 5 Only"
    This page documents the Divi 5 Visual Builder interface. The layout differs substantially from the Divi 4 builder, which used a bottom-docked toolbar and floating modals rather than a sidebar-plus-right-panel arrangement.

## Related

- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Speed up your workflow with hotkeys
- [Left Sidebar](left-sidebar.md) -- Deep dive into every sidebar panel
- [Layers View](layers-view.md) -- Navigating page structure in a tree view
- [Wireframe View](wireframe-view.md) -- Structural editing mode
- [Visual Builder](visual-builder.md) -- General Visual Builder documentation
