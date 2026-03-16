---
title: "JSON Attribute Map"
description: "Divi 5 JSON attribute map — CSS-to-JSON path mapping, brace-depth parser, block locating patterns, and inline style migration via the REST API."
category: internals
tags: [json, attributes, css, mapping, decoration, advanced, migration]
related: [block-format, ssr-rendering, content-encoding]
divi_version: "5.x"
last_updated: 2026-03-12
---

# JSON Attribute Map

Complete mapping between CSS properties and Divi 5 block JSON attribute paths, plus the proven patterns for modifying block attributes via the REST API.

!!! abstract "Quick Reference"
    **What this documents:** The complete mapping between CSS properties and Divi 5 block JSON attribute paths, plus the brace-depth parser and inline style migration patterns.
    **Key data structures:** `module.decoration.*` (layout, spacing, sizing, background), `module.advanced.text.text.*` (text orientation, color), `content.innerContent` (unicode-encoded HTML).
    **Last verified:** 2026-03-12

## CSS Property → JSON Path Mapping

| CSS Property | JSON Path | Example Value |
|---|---|---|
| `text-align: center` | `module.advanced.text.text.desktop.value.orientation` | `"center"` |
| `color: #ffffff` | `module.advanced.text.text.desktop.value.color` | `"#ffffff"` |
| `max-width: 900px` | `module.decoration.sizing.desktop.value.maxWidth` | `"900px"` |
| `padding: 60px 20px` | `module.decoration.spacing.desktop.value.padding` | `{top:"60px", bottom:"60px", left:"20px", right:"20px"}` |
| `margin: 0 auto 20px auto` | `module.decoration.spacing.desktop.value.margin` | `{top:"0px", bottom:"20px", left:"auto", right:"auto", syncVertical:"off", syncHorizontal:"off"}` |
| `background-color` | `module.decoration.background.desktop.value.color` | `"#037d87"` |
| `display: block` | `module.decoration.layout.desktop.value.display` | `"block"` |

## Key Distinction: decoration vs advanced

- **`module.decoration.*`** — layout, spacing, sizing, background — rendered as CSS on the module's root element (`.et_pb_text_N`)
- **`module.advanced.text.text.*`** — text orientation and color — rendered targeting the inner element (`.et_pb_text_N .et_pb_text_inner`)

## How Divi 5 Renders These to CSS

Divi 5 generates a `<style>` tag in the page `<head>` with targeted rules:

```css
.et_pb_text_1 {
  margin-top: 0px !important;
  margin-right: auto !important;
  margin-bottom: 20px !important;
  margin-left: auto !important;
  padding-top: 60px !important;
  padding-right: 20px !important;
  padding-bottom: 60px !important;
  padding-left: 20px !important;
  max-width: 900px;
  text-align: center;
}
.et_pb_text_1 .et_pb_text_inner {
  color: #ffffff !important;
}
```

Note: `margin` and `padding` are output with `!important`. `max-width` and `text-align` are not. `color` on `.et_pb_text_inner` gets `!important`.

## Brace-Depth JSON Parser

Standard regex extraction fails because `-->` can appear inside JSON string values. Use a character-by-character parser:

```javascript
var depth = 0, inStr = false, esc = false, end = -1;
for (var i = jsonStart; i < jsonStart + 50000; i++) {
  var c = raw[i];
  if (esc) { esc = false; continue; }
  if (c === '\\') { esc = true; continue; }
  if (c === '"') { inStr = !inStr; continue; }
  if (!inStr) {
    if (c === '{') depth++;
    else if (c === '}') { depth--; if (depth === 0) { end = i; break; } }
  }
}
var blockJson = JSON.parse(raw.slice(jsonStart, end + 1));
```

## Locating Blocks by Content

Module UUIDs change on every page reload. Always locate blocks by searching for a unique string in the content, then walking backward to find the block start:

```javascript
var idx = raw.indexOf('vendor-neutral');  // unique text anchor
var blockStart = raw.lastIndexOf('<!-- wp:divi/text', idx);
var jsonStart = raw.indexOf('{', blockStart);
```

## Inline Style Migration Pattern

The proven approach for migrating inline HTML styles into Divi block JSON attributes:

1. Fetch the page content via REST API (`context=edit`)
2. Locate each `wp:divi/text` block by content search
3. Parse the block JSON using the brace-depth parser
4. Extract `color` and `text-align` from `<h1>`-`<h6>` and `<p>` style attributes
5. If all styled elements share one color → set `module.advanced.text.text.desktop.value.color`
6. If elements have mixed colors → strip inline styles only, let theme globals handle it
7. If all styled elements share one `text-align` → set `module.advanced.text.text.desktop.value.orientation`
8. Strip `style=` attributes from `<h1>`-`<h6>` and `<p>` tags (preserve `<div>`, `<a>`, `<video>`, `<img>` styles)
9. Save via REST API with double-comment safety check

**Critical rules:**
- Always use `wp.apiRequest` (not `wp.apiFetch`) — `apiFetch` is not available in the Divi context
- Always chain REST API calls sequentially — parallel calls hang indefinitely
- Always run the double-comment safety check before saving
- Content strings in block JSON are unicode-escaped — decode `innerContent` before scanning for inline styles

## Divi Data Registry (Read-Only)

From inside the VB iframe (`#et-vb-app-frame`), module state is accessible via:

```javascript
var store = window.divi.data.select('divi/edit-post');

store.getAllModuleIds();       // array of all module IDs on the page
store.getModuleName(id);       // specific type: 'divi/text', 'divi/section', etc.
store.getModuleType(id);       // generic type: 'module', 'section', 'row', 'column'
store.getModuleAttrs(id);      // full attributes object
```

Module IDs are ephemeral — they change on every page reload. Always re-query after navigation or reload.

## Related

- [Block Comment Format](block-format.md) — the outer block structure containing these JSON attributes
- [SSR Rendering](ssr-rendering.md) — how the JSON attributes are processed into CSS
- [Content Encoding](content-encoding.md) — unicode encoding in `innerContent` values
