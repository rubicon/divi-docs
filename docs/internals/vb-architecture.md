---
title: "Visual Builder Architecture"
description: "Divi 5 Visual Builder architecture internals — dual-frame structure, React state management, global objects, and the divi.data read-only registry."
category: internals
tags: [visual-builder, architecture, react, iframe, dual-frame]
related: [tinymce-state, block-format]
divi_version: "5.x"
last_updated: 2026-03-12
---

# Visual Builder Architecture

The dual-frame structure, React state management, and global objects inside Divi 5's Visual Builder.

!!! abstract "Quick Reference"
    **What this documents:** The internal architecture of Divi 5's Visual Builder, including the dual-frame window structure, global JavaScript objects, and state management.
    **Key data structures:** Parent window (sidebar, TinyMCE, React settings panel), iframe `#et-vb-app-frame` (page canvas, `wp.*`, `DIVI`, `ET_Builder`), `window.divi.data` read-only registry.
    **Last verified:** 2026-03-12

## Dual-Frame Structure

Divi 5's VB uses two separate windows:

**Parent window** — Contains the sidebar, settings panel (React app), toolbar, and Layers panel. This is where `window.tinymce` and the settings-panel React components live.

**Iframe (`#et-vb-app-frame`)** — Contains the page canvas/preview. Houses the page DOM, WordPress core (`wp.*`), and Divi runtime objects (`DIVI`, `ET_Builder`, `ETCloudApp`).

```javascript
// Access the iframe window
const appFrame = document.querySelector('#et-vb-app-frame');
const iframeWin = appFrame.contentWindow;
```

## Global Objects

### In the Iframe

| Object | Contents |
|--------|----------|
| `iframeWin.DIVI` | Builder config: `item_count`, `items_count`, `row_selector` |
| `iframeWin.ET_Builder` | Builder API: `API`, `Frames`, `Misc` |
| `iframeWin.ETCloudApp` | Cloud/Library: `retryUseLayout`, `setState`, `toggleTab`, `setCloudToken` |
| `iframeWin.wp` | WordPress core: hooks, i18n, ajax, media |
| `iframeWin.et_common_data` | Config and i18n data |

### In the Parent Window

| Object | Contents |
|--------|----------|
| `window.tinymce` | TinyMCE instances (when a text module is selected) |
| React root at `#et-vb-app-frame-wrapper` | The settings panel and sidebar UI |

## State Management

Divi 5 does NOT expose a Redux store or standard `wp.data` stores. Despite WordPress core being available in the iframe, the standard `wp.data` is not initialized.

However, Divi 5 exposes its own data registry at `window.divi.data` inside the VB iframe:

```javascript
var store = window.divi.data.select('divi/edit-post');

store.getAllModuleIds();       // all module IDs on the page
store.getModuleName(id);       // 'divi/text', 'divi/section', etc.
store.getModuleType(id);       // generic: 'module', 'section', 'row', 'column'
store.getModuleAttrs(id);      // full attributes object
```

This is **read-only** — there is no documented public API for writing state. Module IDs are ephemeral and change on every page reload.

This means:
- Standard `wp.data.select()` and `wp.data.dispatch()` are NOT available
- `window.divi.data.select()` provides read-only access to module state
- The only reliable way to MODIFY builder state is through UI interaction (clicks, keyboard input)
- For batch attribute changes, the REST API approach (modifying block JSON in `post_content`) works for blocks already created via the VB

## Related

- [TinyMCE State Sync](tinymce-state.md) — how text editing syncs with Divi's state
- [Block Comment Format](block-format.md) — the data format the VB reads and writes
