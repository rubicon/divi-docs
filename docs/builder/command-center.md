---
title: "Command Center"
category: builder
tags: ["builder", "command-center", "keyboard-shortcuts", "workflow", "productivity"]
related: ["visual-builder", "presets"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13741079"
---

# Command Center

A keyboard-driven command palette for quickly adding elements, opening panels, applying presets, and navigating the builder without using the mouse.

## Overview

The Command Center is Divi 5's command palette interface, similar to the command palettes found in code editors and design tools. It provides instant access to every builder action through a searchable, keyboard-navigable menu. You can add modules, open settings panels, switch views, apply presets, and navigate between pages, all from a single text input.

Beyond basic command execution, the Command Center supports queue operators that let you chain multiple actions into a single command string. This means you can create complex nested layouts, apply presets, and duplicate elements in one operation.

For the official Elegant Themes documentation, see [Command Center](https://help.elegantthemes.com/en/articles/13741079).

## Opening the Command Center

| Method | Action |
|--------|--------|
| Keyboard shortcut | Press **Cmd/Ctrl + K** |
| UI button | Click the lightning bolt icon in the builder sidebar |

## Command Categories

The Command Center organizes available actions into categories. You can filter results by category using the `:` prefix.

| Category | Function | Examples |
|----------|----------|---------|
| Element | Add page elements to the layout | Button, Blurb, Group, Text, Image |
| Modal | Open builder dialog panels | Variables, Import/Export, Library |
| Settings | Jump to specific option groups in the active settings panel | Animation, Border, Interactions, Spacing |
| View | Switch display and preview modes | Desktop, Tablet, Phone, Wireframe |
| Modify | Perform actions on the selected element | Duplicate, Delete, Copy, Cut, Paste, Reset |
| Navigate | Switch between pages and admin screens | Page names, Theme Builder, Theme Options |
| Preset | Apply a saved design preset to the selected element | Any custom preset by name |
| Page | Execute page-level actions | Save, Exit, Preview |

### Filtering by Category

Type `:` followed by the category name to narrow results. For example:

- `:modal` shows only modal-related commands
- `:element` shows only element insertion commands
- `:view` shows only view switching commands

## Queue Operators

Queue operators let you combine multiple commands into a single execution string. This is the Command Center's most powerful feature for rapid layout building.

| Operator | Purpose | Example |
|----------|---------|---------|
| `>` | Nest an element inside the previous element | `blurb > button` inserts a Button nested inside a Blurb |
| `*` | Multiply (duplicate) an element | `button *2` adds two Button modules |
| `^` | Place element above the currently selected element | `^ button` inserts a Button above the selection |
| `+` | Attach a preset to the element | `button + Primary Preset` adds a Button with the Primary Preset applied |

### Combining Operators

Operators can be chained to build complex structures in a single command:

- `blurb > group > button *2` — Creates a Blurb containing a Group containing two Buttons
- `button + Primary Preset *3` — Adds three Buttons, each with the Primary Preset applied
- `blurb > group > button + Primary Preset *2` — Full nested layout with presets in one command

## Workflow

### Basic Command Execution

1. Press **Cmd/Ctrl + K** to open the Command Center.
2. Type the command name or a partial match.
3. Press **Enter** to execute the selected command.

### Queue Mode (Chaining Commands)

1. Press **Cmd/Ctrl + K** to open the Command Center.
2. Type the first command.
3. Press **Cmd/Ctrl + Enter** to enter queue mode.
4. Add operators and additional commands to the queue string.
5. Press **Enter** to execute the full queue.

### Search Behavior

The Command Center uses fuzzy matching, so typing partial names filters the results in real time. For example, typing "blu" will surface the Blurb element command, and typing "ani" will surface the Animation settings command.

## Context-Aware Insertion

Element commands are context-aware. When you add an element through the Command Center, it is inserted relative to the currently selected element on the canvas. If no element is selected, the new element is appended to the end of the page. The `^` operator overrides default placement by inserting above the selection.

## Common Shortcuts

These standard keyboard shortcuts work throughout the builder, independent of the Command Center:

| Action | Shortcut |
|--------|----------|
| Open Command Center | Cmd/Ctrl + K |
| Save Page | Cmd/Ctrl + S |
| Undo | Cmd/Ctrl + Z |
| Redo | Cmd/Ctrl + Shift + Z |

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Command Center is a new feature in Divi 5 with no equivalent in Divi 4.

## Troubleshooting

!!! warning "Command Not Found"
    If a command does not appear in search results, verify the spelling or try a shorter search term. Category-specific commands only appear when the relevant context is active (e.g., Modify commands require an element to be selected).

!!! warning "Queue Operators Not Working"
    Ensure you are entering queue mode with **Cmd/Ctrl + Enter** before adding operators. Pressing Enter alone executes the current command immediately without queuing.

## Related

- [Visual Builder](visual-builder.md)
- [Presets](presets.md)
- [Nested Modules](nested-modules.md)
