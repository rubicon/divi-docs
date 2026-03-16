---
title: "Block Comment Format"
description: "Divi 5 block comment format internals — how WordPress stores Divi content as wp:divi/* blocks with JSON attributes in post_content."
category: internals
tags: [block-format, wp-blocks, json, content-storage]
related: [ssr-rendering, content-encoding]
divi_version: "5.x"
last_updated: 2026-03-12
---

# Block Comment Format

How Divi 5 stores page content as WordPress block comments in `post_content`.

!!! abstract "Quick Reference"
    **What this documents:** The WordPress block comment structure Divi 5 uses to store page content in `post_content`, including JSON attribute schema and column type values.
    **Key data structures:** `wp:divi/placeholder`, `wp:divi/section`, `wp:divi/row`, `wp:divi/column`, `wp:divi/text` — container blocks (opening/closing tags) and leaf blocks (self-closing).
    **Last verified:** 2026-03-12

## Structure

Divi 5 uses WordPress block comments with JSON attributes:

```
<!-- wp:divi/placeholder -->
  <!-- wp:divi/section {JSON_ATTRS} -->
    <!-- wp:divi/row {JSON_ATTRS} -->
      <!-- wp:divi/column {JSON_ATTRS} -->
        <!-- wp:divi/text {JSON_ATTRS} /-->
      <!-- /wp:divi/column -->
    <!-- /wp:divi/row -->
  <!-- /wp:divi/section -->
<!-- /wp:divi/placeholder -->
```

**Container blocks** (section, row, column, placeholder) use opening and closing tags:
```
<!-- wp:divi/section {...} -->
  ...children...
<!-- /wp:divi/section -->
```

**Leaf blocks** (text, testimonial, button, etc.) are self-closing:
```
<!-- wp:divi/text {...} /-->
```

## JSON Attribute Structure

Each block carries a JSON configuration object:

```json
{
  "module": {
    "meta": {
      "adminLabel": { "desktop": { "value": "section" } }
    },
    "decoration": {
      "layout": { "desktop": { "value": { "display": "block" } } },
      "background": { "desktop": { "value": { "color": "#037d87" } } },
      "spacing": { "desktop": { "value": { "padding": { "top": "60px", "bottom": "60px" } } } },
      "sizing": { "desktop": { "value": { "width": "80%", "maxWidth": "1080px" } } }
    }
  },
  "content": {
    "innerContent": { "desktop": { "value": "encoded HTML content here" } }
  },
  "builderVersion": "5.0.0-public-beta.1"
}
```

## Column Type Values

Columns use a `type` field indicating their width fraction:

| Type | Width | Usage |
|------|-------|-------|
| `4_4` | 100% (full) | Single column layout |
| `1_2` + `1_2` | 50% + 50% | Two equal columns |
| `1_3` + `1_3` + `1_3` | 33% each | Three equal columns |
| `1_4` + `3_4` | 25% + 75% | Sidebar + main |
| `3_4` + `1_4` | 75% + 25% | Main + sidebar |
| `1_4` + `1_4` + `1_4` + `1_4` | 25% each | Four equal columns |

## Registered Block Types

Divi 5 registers 76+ block types with WordPress (`divi/section`, `divi/row`, `divi/column`, `divi/text`, `divi/testimonial`, `divi/button`, etc.). All are `is_dynamic: true` (server-side rendered).

## Related

- [SSR Rendering](ssr-rendering.md) — how blocks are rendered on the frontend
- [Content Encoding](content-encoding.md) — unicode encoding rules for HTML inside blocks
