---
title: "Divi Data Registry"
description: "Divi 5 Data Registry reference — window.divi.data.select() API for read-only access to module state, attributes, and layout structure in the Visual Builder."
category: api
tags: [data-registry, state, modules, visual-builder, read-only, javascript]
related: [javascript-api, hooks-filters, custom-modules]
divi_version: "5.x"
last_updated: 2026-03-16
---

# Divi Data Registry

⚠️ Observed — Everything on this page is reverse-engineered from Visual Builder inspection using browser DevTools. None of these APIs are officially documented by Elegant Themes. They may change without notice.

!!! abstract "Quick Reference"
    **Registry location:** `window.divi.data` (inside the VB iframe `#et-vb-app-frame`)
    **Primary store:** `window.divi.data.select('divi/edit-post')`
    **Key methods:** `getAllModuleIds()`, `getModuleName(id)`, `getModuleType(id)`, `getModuleAttrs(id)`
    **Access:** Read-only — no public dispatch/write API
    **Critical caveat:** Module IDs are ephemeral and change on every page reload

## Overview

Divi 5's Visual Builder maintains an internal state registry at `window.divi.data` inside the VB iframe. This registry provides read-only access to the current state of every module on the page — their types, attributes, and hierarchical structure.

The registry follows a store-based pattern similar to WordPress's `wp.data` API, but it is a completely separate implementation. Standard WordPress data stores (`wp.data.select()`, `wp.data.dispatch()`) are NOT initialized in the Visual Builder — see [Known Limitations](../playbooks/known-limitations.md#12-wpdata-is-not-available-in-the-visual-builder).

The data registry is useful for:

- Debugging module state during development
- Building diagnostic or analysis tools
- Reading module attributes programmatically
- Understanding the structure of a Divi layout

## Accessing the Registry

The data registry lives inside the Visual Builder's iframe, NOT in the parent window.

### Step 1: Get the iframe reference

```javascript
// From the parent window
var appFrame = document.querySelector('#et-vb-app-frame');
var iframeWin = appFrame.contentWindow;
```

### Step 2: Access the registry

```javascript
// Inside the iframe context
var store = iframeWin.window.divi.data.select('divi/edit-post');
```

### Or from DevTools directly

If you are working in the browser DevTools Console, you must first switch the execution context to the VB iframe:

1. Open the Visual Builder (URL must contain `?et_fb=1`)
2. Open DevTools (F12 or Cmd+Option+I)
3. In the Console tab, click the context dropdown (usually says "top")
4. Select `#et-vb-app-frame` from the list
5. Now you can access the registry directly:

```javascript
// After switching console context to the iframe
var store = window.divi.data.select('divi/edit-post');
store.getAllModuleIds();
```

## The select() API

⚠️ Observed — The `select()` method accepts a store name and returns an object with query methods. The only confirmed store name is `'divi/edit-post'`.

```javascript
window.divi.data.select(storeName: string): StoreObject
```

### Store: `divi/edit-post`

The primary store for accessing module data in the current page layout.

#### getAllModuleIds()

⚠️ Observed — Returns an array of all module IDs currently in the layout.

```javascript
store.getAllModuleIds(): string[]
```

**Returns:** `string[]` — Array of UUID strings for every module, section, row, and column in the layout.

```javascript
var store = window.divi.data.select('divi/edit-post');
var ids = store.getAllModuleIds();
console.log(ids.length);  // e.g., 47
console.log(ids[0]);      // e.g., "1b459396-b3b5-49d1-b00c-6120de1ac485"
```

#### getModuleName(id)

⚠️ Observed — Returns the specific module type identifier for a given module ID.

```javascript
store.getModuleName(id: string): string
```

**Returns:** `string` — The namespaced module type (e.g., `'divi/text'`, `'divi/section'`, `'divi/image'`, `'divi/blurb'`).

```javascript
var name = store.getModuleName('1b459396-b3b5-49d1-b00c-6120de1ac485');
console.log(name);  // "divi/text"
```

#### getModuleType(id)

⚠️ Observed — Returns the generic structural type for a given module ID.

```javascript
store.getModuleType(id: string): string
```

**Returns:** `string` — One of the generic type values: `'module'`, `'section'`, `'row'`, `'column'`.

```javascript
var type = store.getModuleType('1b459396-b3b5-49d1-b00c-6120de1ac485');
console.log(type);  // "module"
```

!!! tip "getModuleName vs getModuleType"
    Use `getModuleName()` when you need the specific module type (e.g., to find all Text modules). Use `getModuleType()` when you need the structural category (e.g., to filter out sections and rows and get only content modules).

#### getModuleAttrs(id)

⚠️ Observed — Returns the full attributes object for a given module ID. This includes all settings configured through the module's settings panel.

```javascript
store.getModuleAttrs(id: string): object
```

**Returns:** `object` — The complete attributes object. Structure varies by module type. Contains nested objects for `module.decoration` (spacing, sizing, background), `module.advanced` (text, CSS), and `content` (inner content).

```javascript
var attrs = store.getModuleAttrs('1b459396-b3b5-49d1-b00c-6120de1ac485');
console.log(JSON.stringify(attrs, null, 2));
```

The attributes object structure follows the patterns documented in [JSON Attribute Map](../internals/json-attribute-map.md).

### Other Possible Store Methods

🔬 Needs Testing — The following methods may exist on the `divi/edit-post` store but have not been confirmed:

| Method | Expected Signature | Notes |
|--------|-------------------|-------|
| `getModuleChildren(id)` | `(id: string) => string[]` | 🔬 Needs Testing — May return child module IDs for parent modules (sections, rows). |
| `getModuleParent(id)` | `(id: string) => string` | 🔬 Needs Testing — May return the parent module ID. |
| `getSelectedModuleId()` | `() => string \| null` | 🔬 Needs Testing — May return the currently selected module in the VB. |
| `isModuleVisible(id)` | `(id: string) => boolean` | 🔬 Needs Testing — May indicate module visibility state. |

### Other Possible Store Names

🔬 Needs Testing — The following store names may be available via `window.divi.data.select()`:

| Store Name | Expected Purpose |
|------------|-----------------|
| `'divi/settings'` | 🔬 Needs Testing — Global builder settings and preferences. |
| `'divi/history'` | 🔬 Needs Testing — Undo/redo history stack. |
| `'divi/ui'` | 🔬 Needs Testing — UI state (panel visibility, zoom level, breakpoint). |

## The dispatch() Question

⚠️ Observed — `window.divi.data.dispatch` may exist as a function, but there is **no documented or confirmed public dispatch API** for writing state. Calling dispatch methods — if they exist — could corrupt the builder's internal state and cause data loss.

**The data registry is read-only for all practical purposes.**

To modify module state programmatically, use one of these approaches:

1. **UI interaction** — Drive the Visual Builder interface (clicks, keyboard input) via browser automation tools like Playwright or Claude in Chrome.
2. **REST API** — Modify block JSON attributes in `post_content` via `wp.apiRequest`. This works for blocks already created through the VB. See [Known Limitations](../playbooks/known-limitations.md#1-never-create-new-content-via-backend-methods-but-modifying-existing-blocks-is-fine) for details and caveats.

## Module ID Ephemerality

⚠️ Observed — Module IDs (UUIDs like `1b459396-b3b5-49d1-b00c-6120de1ac485`) are ephemeral. They are generated fresh every time the Visual Builder loads a page. The same module will have a different ID after:

- A page reload in the browser
- Closing and reopening the Visual Builder
- Navigating away and back to the page

**Never cache module IDs across sessions.** Always re-query `getAllModuleIds()` after any reload.

To reliably identify a specific module across sessions, locate it by its content or a unique attribute value:

```javascript
// Find a module by searching for unique content
var store = window.divi.data.select('divi/edit-post');
var ids = store.getAllModuleIds();

var targetId = null;
for (var i = 0; i < ids.length; i++) {
    var attrs = store.getModuleAttrs(ids[i]);
    // Look for a unique string in the module's content
    if (attrs && attrs.content && attrs.content.innerContent &&
        attrs.content.innerContent.indexOf('unique-identifier-text') !== -1) {
        targetId = ids[i];
        break;
    }
}
```

## Practical Usage Examples

### Enumerate all modules on a page

⚠️ Observed

```javascript
var store = window.divi.data.select('divi/edit-post');
var ids = store.getAllModuleIds();

ids.forEach(function(id) {
    var name = store.getModuleName(id);
    var type = store.getModuleType(id);
    console.log(type + ': ' + name + ' (' + id.substring(0, 8) + '...)');
});

// Output:
// section: divi/section (1b459396...)
// row: divi/row (a3f72c01...)
// column: divi/column (8e2d1f09...)
// module: divi/text (c4b89e12...)
// module: divi/image (f1a23d45...)
```

### Find all Text modules

⚠️ Observed

```javascript
var store = window.divi.data.select('divi/edit-post');
var ids = store.getAllModuleIds();

var textModules = ids.filter(function(id) {
    return store.getModuleName(id) === 'divi/text';
});

console.log('Found ' + textModules.length + ' Text modules');
```

### Count modules by type

⚠️ Observed

```javascript
var store = window.divi.data.select('divi/edit-post');
var ids = store.getAllModuleIds();
var counts = {};

ids.forEach(function(id) {
    var name = store.getModuleName(id);
    counts[name] = (counts[name] || 0) + 1;
});

console.table(counts);
// divi/section: 5
// divi/row: 8
// divi/column: 12
// divi/text: 15
// divi/image: 7
```

### Read a specific module's spacing settings

⚠️ Observed

```javascript
var store = window.divi.data.select('divi/edit-post');
var ids = store.getAllModuleIds();

// Get the first Text module
var textId = ids.find(function(id) {
    return store.getModuleName(id) === 'divi/text';
});

if (textId) {
    var attrs = store.getModuleAttrs(textId);
    // Navigate the attribute structure
    var spacing = attrs.module &&
                  attrs.module.decoration &&
                  attrs.module.decoration.spacing &&
                  attrs.module.decoration.spacing.desktop &&
                  attrs.module.decoration.spacing.desktop.value;

    if (spacing) {
        console.log('Padding:', JSON.stringify(spacing.padding));
        console.log('Margin:', JSON.stringify(spacing.margin));
    }
}
```

### Check if a module has a preset assigned

⚠️ Observed

```javascript
var store = window.divi.data.select('divi/edit-post');
var attrs = store.getModuleAttrs(moduleId);

// Presets are typically stored in the module's root attributes
if (attrs && attrs.preset) {
    console.log('Module uses preset:', attrs.preset);
} else {
    console.log('Module uses custom settings (no preset)');
}
```

### Export all module attributes for analysis

⚠️ Observed

```javascript
var store = window.divi.data.select('divi/edit-post');
var ids = store.getAllModuleIds();

var exportData = ids.map(function(id) {
    return {
        id: id,
        name: store.getModuleName(id),
        type: store.getModuleType(id),
        attrs: store.getModuleAttrs(id)
    };
});

// Copy to clipboard for analysis
copy(JSON.stringify(exportData, null, 2));
console.log('Exported ' + exportData.length + ' modules to clipboard');
```

## Console Exploration Guide

Step-by-step instructions for exploring the data registry from browser DevTools.

### Step 1: Open the Visual Builder

Navigate to any page in WordPress and click "Enable Visual Builder" from the admin bar, or add `?et_fb=1` to the page URL.

### Step 2: Open DevTools

Press `F12` (Windows/Linux) or `Cmd+Option+I` (Mac) to open browser DevTools.

### Step 3: Switch execution context to the iframe

In the Console tab, find the context selector dropdown. It typically shows "top" by default. Click it and select the `#et-vb-app-frame` iframe. This is required because the data registry lives inside the iframe, not the parent window.

### Step 4: Verify access

```javascript
// This should return an object, not undefined
window.divi.data.select('divi/edit-post');
```

If this returns `undefined`, ensure you are in the correct iframe context and the page has fully loaded.

### Step 5: Explore module IDs

```javascript
var store = window.divi.data.select('divi/edit-post');
var ids = store.getAllModuleIds();
console.log('Total elements:', ids.length);
```

### Step 6: Inspect a specific module

```javascript
// Pick any ID from the list
var firstModule = ids[0];
console.log('Name:', store.getModuleName(firstModule));
console.log('Type:', store.getModuleType(firstModule));
console.log('Attrs:', store.getModuleAttrs(firstModule));
```

### Step 7: Discover available methods

⚠️ Observed — You can inspect the store object itself to discover additional methods:

```javascript
var store = window.divi.data.select('divi/edit-post');
console.log(Object.keys(store));
// Logs all available method names on the store
```

### Step 8: Discover available stores

⚠️ Observed — You can inspect the registry itself for other store names:

```javascript
console.log(Object.keys(window.divi.data));
// May reveal: select, dispatch, subscribe, etc.
```

## Limitations

| Limitation | Details |
|------------|---------|
| **Read-only** | No public write/dispatch API. You cannot modify module state through the registry. |
| **Ephemeral IDs** | Module UUIDs change on every page reload. Never persist or cache them. |
| **VB-only** | The registry exists only inside the Visual Builder iframe. It is not available on the front end or in the WordPress admin. |
| **`wp.data` is separate** | Standard WordPress `wp.data` stores are NOT initialized in the VB. Do not confuse `window.divi.data` with `wp.data`. They are entirely different systems. |
| **Undocumented** | This entire API is reverse-engineered. Elegant Themes has not published official documentation for `window.divi.data`. Behavior may change in any Divi update. |
| **Iframe context required** | From the parent window, you must access the registry through `document.querySelector('#et-vb-app-frame').contentWindow.divi.data`. Direct `window.divi.data` only works from within the iframe context. |

## Version Notes

!!! note "Divi 5 Only"
    The `window.divi.data` registry is specific to Divi 5. Divi 4 does not have an equivalent client-side data registry. The registry was first observed in Divi 5 beta builds and has been stable in structure across updates through March 2026, though this does not guarantee future stability.

!!! warning "Not a Public API"
    This page documents behavior observed through browser DevTools inspection. Elegant Themes has not officially documented or committed to maintaining this API. Use it for debugging and development tooling, not for production extensions that end users depend on. Production code should use the official `API` object from `et_builder_api_ready` — see [JavaScript API](javascript-api.md).

## Related

- [JavaScript API](javascript-api.md) — The official Builder JavaScript API (`et_builder_api_ready`)
- [Hooks & Filters](hooks-filters.md) — PHP and JavaScript hooks for extending Divi
- [Custom Modules](custom-modules.md) — Building custom modules with PHP and JavaScript
- [VB Architecture](../internals/vb-architecture.md) — Dual-frame structure and global objects
- [JSON Attribute Map](../internals/json-attribute-map.md) — CSS-to-JSON path mapping for module attributes
- [Known Limitations](../playbooks/known-limitations.md) — Divi 5 gotchas including `wp.data` unavailability
- [Block Comment Format](../internals/block-format.md) — The data format the VB reads and writes
