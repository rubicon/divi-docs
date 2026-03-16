---
title: "Preset Manager"
category: builder
tags: [builder, presets, preset-manager, design-system, management]
related: [option-group-presets, stacked-nested-presets, presets]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13427552"
---

# Preset Manager

The Preset Manager is a centralized sidebar tool in the Divi 5 Visual Builder that lists every preset on your site — both element presets and option group presets — in one place, with search, filtering, reordering, and a live preview panel.

## Overview

As a design system grows, managing presets scattered across individual element settings becomes unwieldy. The Preset Manager solves this by providing a single interface where you can view, create, edit, duplicate, delete, reorder, and preview all presets. It also supports importing and exporting preset collections, making it possible to share entire design systems between Divi 5 sites.

The companion **Preview Panel** shows a live sample of each preset as you edit it. This lets you refine typography, colors, spacing, and other settings without affecting any real page content — the preview is fully isolated from the page layout.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13427552).

## Accessing the Preset Manager

Open the Visual Builder and locate the **Preset Manager** icon in the left sidebar. Clicking it opens the Preset Manager panel.

## Preset Categories

The Preset Manager organizes presets into two main categories:

| Category | Description |
|----------|-------------|
| Element Presets | Full styling configurations for modules, sections, rows, and columns |
| Option Group Presets | Style blocks for specific option groups (Typography, Button, Border, Spacing, etc.) |

You can filter and search across both categories to quickly locate specific presets.

## Management Operations

| Operation | Description |
|-----------|-------------|
| Create | Add a new element or option group preset from scratch |
| Edit | Modify a preset's settings; changes apply across your entire site |
| Duplicate | Clone a preset as a starting point for a variation |
| Delete | Remove unused presets |
| Set as default | Mark any element preset as the default so all new elements of that type start with those styles |
| Reorder | Drag presets to rearrange their order in the list |
| Search | Filter the preset list by name or type |

## Preview Panel

The Preview Panel provides a live rendering of the preset you are editing. This is an isolated environment — you are not modifying any real page content while adjusting presets.

| Feature | Type | Description |
|---------|------|-------------|
| Live updates | Behavior | Changes in the settings panel reflect immediately in the preview |
| Background testing | Setting | Test the preset against different background colors, including your site's color variables |
| Isolation mode | Behavior | The preview is independent of any page layout; no real modules are affected |

## Recommended Workflow

The Preset Manager supports a phased approach to building a design system:

| Phase | Activity | Description |
|-------|----------|-------------|
| Design | Create and refine | Build your preset library using the Preview Panel to iterate without touching pages |
| Organize | Sort and reorder | Move base and frequently-used presets to the top of the list |
| Build | Apply presets first | When building pages, reach for presets before making one-off style changes |
| Iterate | Edit presets, not pages | When designs need updating, modify the preset rather than individual elements |
| Share | Export and import | Move your preset library to new Divi 5 sites via export/import |

## Import and Export

The Preset Manager supports transferring entire design systems between sites:

| Action | Description |
|--------|-------------|
| Export | Packages all presets (or a selection) into a portable file |
| Import | Loads a preset package into the current site's Preset Manager |

This makes presets a key part of Divi 5's design system portability, alongside [global variables](global-variables.md) which are also embedded in layout exports.

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    The Preset Manager reads from and writes to the same storage as individual preset creation (likely `wp_options` or a custom post type). The manager is a UI layer on top of the underlying preset data. Import/export functionality suggests a defined serialization format.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Divi REST API or `wp_options` query | Needs Testing | The Preset Manager lists all presets; the underlying data store is shared with inline preset creation |
| Modify | Divi REST API or `update_option()` | Needs Testing | Editing via the manager is equivalent to editing inline — same propagation behavior |
| Create | Divi REST API or Preset Manager UI | Needs Testing | Import functionality may use a specific REST endpoint or file upload handler |

<!-- TODO: Identify the export file format — is it JSON? A Divi-specific format? -->
<!-- TODO: Test whether import deduplicates presets by name or creates new entries -->

## Related

- [Option Group Presets](option-group-presets.md) — The option group presets managed here
- [Stacked & Nested Presets](stacked-nested-presets.md) — Composing presets together
- [Presets](presets.md) — Element-level presets overview
- [Global Variables](global-variables.md) — Variables that complement presets in a design system
