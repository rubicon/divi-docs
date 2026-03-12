---
title: "TinyMCE State Sync"
category: internals
tags: [tinymce, text-editor, state, react, saving]
related: [vb-architecture, block-format]
divi_version: "5.x"
last_updated: 2026-03-12
---

# TinyMCE State Sync

How the TinyMCE text editor syncs (and fails to sync) with Divi 5's internal save state.

## How It Works

When a Text module is selected in the Visual Builder, TinyMCE powers the content editor in the settings panel:

```javascript
// Get the active TinyMCE editor (only when a text module is selected)
const editor = window.tinymce.get('_content-innerContent_vb_tiny_mce');
const html = editor.getContent(); // Reading works
```

## The Sync Problem

`tinymce.setContent()` updates the settings panel UI but does NOT sync to Divi's internal React state. When the user clicks Save, Divi reads from its own state — not from TinyMCE. Content set via `setContent()` will appear in the panel but will revert after save.

## What Does Work

Keyboard input triggers the proper React event chain that Divi captures. The reliable workflow for setting text content programmatically:

1. Click into the TinyMCE editor area (in the settings panel)
2. Select all content: Cmd+A / Ctrl+A
3. Type the replacement content via keyboard events

For browser automation tools (Playwright, Claude in Chrome), this means using `type()` actions rather than JavaScript DOM manipulation.

## TinyMCE Formatting Shortcuts

These keyboard shortcuts work within the TinyMCE editor and properly sync:

| Shortcut | Action |
|----------|--------|
| Cmd+B / Ctrl+B | Bold |
| Cmd+I / Ctrl+I | Italic |
| Cmd+K / Ctrl+K | Insert link |
| Cmd+A / Ctrl+A | Select all |
| Paragraph dropdown | Change heading level (H1-H6) |

## Related

- [Visual Builder Architecture](vb-architecture.md) — the dual-frame context where TinyMCE lives
