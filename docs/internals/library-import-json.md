---
title: "Library Import JSON Structure"
description: "Divi 5 library and design system import file formats — Global Variables, Presets, Theme Builder templates, Theme Customizer, and layout JSON structure."
category: internals
tags: [internals, library, import, design-system, json, presets, global-variables]
related: [block-format, json-attribute-map]
divi_version: "5.x"
last_updated: 2026-03-17
---

# Library Import JSON Structure

How Divi 5’s **Divi Library** and **Design System** import/export JSON files are structured. This is reverse‑engineered from the [Divi 5 Launch Design System](https://www.elegantthemes.com/blog/divi-resources/divi-5-launch-gift-design-system) ZIP and applies to imports via **Divi > Divi Library > Import & Export**, **Theme Builder**, and **Theme Customizer**.

!!! abstract "Quick Reference"
    **What this documents:** The root `context`, top-level keys, and main data shapes for each import file type.
    **File types:** Global Variables | Presets | Theme Builder Templates | Theme Customizer | Layouts (pages, sections, premade).
    **Last verified:** 2026-03-17 (Design System ZIP)

---

## Overview

Each import file is a **single JSON object** with a **`context`** field that tells Divi which importer to use:

| Context | File purpose | Import location |
|--------|--------------|-----------------|
| `et_builder` | Global Variables, Presets (and optionally embedded colors/variables) | Divi Library > Import & Export |
| `et_builder_layouts` | Pages, sections, premade layouts | Divi Library > Import & Export |
| `et_theme_builder` | Theme Builder templates + embedded layouts | Theme Builder > ↑↓ |
| `et_divi_mods` | Theme Customizer settings | Theme Customizer > ↑↓ |

The same root object often includes **shared trailing keys** (`global_colors`, `global_variables`, `canvases`, `images`, `thumbnails`) for portability; import may use only the key(s) relevant to that context.

---

## 1. Global Variables (`context: "et_builder"`)

**File example:** `Divi-5-Launch-Freebie_Global-Variables.json`

**Root shape:**

```json
{
  "context": "et_builder",
  "data": [],
  "presets": [],
  "global_colors": [ ["id", { "color", "status", "label" } ], ... ],
  "global_variables": [ { "id", "label", "value", "order", "status", "lastUpdated", "variableType", "type" }, ... ],
  "canvases": [],
  "images": [],
  "thumbnails": []
}
```

### `global_colors`

Array of **tuples** `[ id, definition ]`:

- **id:** string, e.g. `gcid-primary-color`, `gcid-s0kqi6v11w`
- **definition:** object
  - `color` — hex, rgba, or `$variable(...)$` reference
  - `status` — `"active"` | `"inactive"`
  - `label` — display name

Colors can reference other global colors via the **variable syntax** (see [Variable reference format](#variable-reference-format) below).

### `global_variables`

Array of **variable objects**. Each has:

| Field | Type | Notes |
|-------|------|--------|
| `id` | string | e.g. `gvid-3ycvkww27b`, `gcid-primary-color` |
| `label` | string | Display name |
| `value` | string | e.g. `"16px"`, `"clamp(24px, 6vw, 90px)"`, `"#2176ff"`, `"Inter"` |
| `order` | string | Sort order (can be `""`) |
| `status` | string | `"active"` \| `"archived"` |
| `lastUpdated` | string | ISO 8601 |
| `variableType` | string | Same as `type` |
| `type` | string | `"numbers"` \| `"strings"` \| `"colors"` \| `"fonts"` \| `"images"` \| `"links"` |
| `groupKey` | string | *(optional)* e.g. `"colors"`, `"fonts"` |

**Variable types in the design system:**

- **numbers** — spacing, font sizes, border radius, line height, max-widths (e.g. `"60px"`, `"clamp(...)"`)
- **strings** — CTAs, company name, address, phone, email, URLs
- **colors** — same IDs as `global_colors`; value can be hex/rgba or `$variable(...)$`
- **fonts** — e.g. `"--et_global_heading_font"`, `"Inter"`
- **images** — base64 data URLs or URLs
- **links** — URL strings

Import this file with **“Import Global Variables”** checked in the Library import dialog.

---

## 2. Presets (`context: "et_builder"`)

**File example:** `Divi-5-Launch-Freebie_Presets.json`

**Root shape:**

```json
{
  "context": "et_builder",
  "data": [],
  "presets": {
    "module": { "divi/heading": { "default", "items" }, "divi/row": { ... }, ... },
    "group": { "divi/button": { ... }, "divi/font": { ... }, "divi/spacing": { ... }, ... }
  },
  "global_colors": [ ... ],
  "global_variables": [ ... ],
  "canvases": [],
  "images": [],
  "thumbnails": []
}
```

### `presets.module`

Keyed by **module slug** (e.g. `divi/heading`, `divi/row`, `divi/section`, `divi/column`, `divi/text`, `divi/button`, `divi/contact-form`, `divi/signup`). Each value:

- `default` — id of the default preset for that module
- `items` — object of preset id → **preset object**

**Module preset object** (per item):

| Field | Description |
|-------|-------------|
| `id` | Unique preset id (e.g. `vruk2g8yjw`) |
| `name` | Display name (e.g. `"Heading Preset 1"`, `"Subheading"`) |
| `moduleName` | Module slug (e.g. `divi/heading`) |
| `version` | Builder version (e.g. `5.0.0-public-beta.3`) |
| `type` | `"module"` |
| `created` | Timestamp (ms) |
| `updated` | Timestamp (ms) |
| `attrs` | *(optional)* Partial module attributes (e.g. `title.decoration.font`, `css`) — can reference `$variable(...)$` |
| `renderAttrs` | *(optional)* Serialized render attributes |

### `presets.group`

**Option group presets** (shared across modules). Keys are group names, e.g.:

- `divi/button`, `divi/font`, `divi/font-header`, `divi/font-body`
- `divi/border`, `divi/box-shadow`, `divi/spacing`, `divi/background`
- `divi/layout`, `divi/text`, `divi/sizing`, `divi/filters`

Structure is analogous to `module`: `default` + `items` (id → preset object). Layouts reference these via `groupPreset` (e.g. `module.decoration.spacing` → `presetId` + `groupName`).

Import with **“Import Presets”** checked.

---

## 3. Theme Builder Templates (`context: "et_theme_builder"`)

**File example:** `Divi-5-Launch-Freebie_Theme-Builder-Templates.json`

**Root shape:**

```json
{
  "context": "et_theme_builder",
  "templates": [ { "title", "autogenerated_title", "default", "enabled", "use_on", "exclude_from", "layouts", "description" }, ... ],
  "layouts": { "220016": { layout object }, "220031": { ... }, ... },
  "presets": { ... },
  "global_colors": [ ... ],
  "global_variables": [ ... ],
  "has_default_template": true,
  "has_global_layouts": true
}
```

### `templates`

Array of **template objects**:

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | e.g. `"Default Website Template"`, `"All Posts"` |
| `autogenerated_title` | boolean | Whether title was auto-generated from assignments |
| `default` | boolean | Is the default template |
| `enabled` | boolean | |
| `use_on` | string[] | Assignment rules, e.g. `["singular:post_type:post:all"]`, `[]` for default |
| `exclude_from` | string[] | Exclusion rules |
| `layouts` | object | `header`, `body`, `footer` → `{ "id": number, "enabled": boolean }` (id references `layouts` key) |
| `description` | string | HTML snippet for UI |

### `layouts`

Object keyed by **layout ID** (numeric, as string). Each value is a **full layout payload**:

- `context`, `data`, `images`, `post_title`, `post_type`, `theme_builder`, `global_colors`, `canvases`, `post_meta`
- `data` contains the actual layout post(s) (same structure as `et_builder_layouts` per layout).

Import via **Theme Builder > ↑↓** with Presets enabled; can override existing template assignments.

---

## 4. Theme Customizer (`context: "et_divi_mods"`)

**File example:** `Divi-5-Launch-Freebie_Theme-Customizer.json`

**Root shape:**

```json
{
  "context": "et_divi_mods",
  "data": {
    "body_font_size": 16,
    "heading_font": "Inter",
    "body_font": "Inter",
    "header_color": "#000000",
    "font_color": "rgba(0,0,0,0.7)",
    "link_color": "#2ea3f2",
    "accent_color": "#2176ff",
    "secondary_accent_color": "#ff5700",
    "content_width": "1080",
    "section_padding": "4",
    "row_padding": "2",
    "primary_nav_bg": "#ffffff",
    "footer_bg": "#222222",
    "et_global_data": { "global_colors": { ... } },
    ... many other theme mod keys ...
  },
  "presets": "",
  "global_colors": "",
  "global_variables": "",
  "canvases": [],
  "images": [],
  "thumbnails": []
}
```

`data` is a flat (and nested `et_global_data`) **WordPress theme mods** object: typography, colors, layout widths, header/footer/nav options, builder preferences, etc. Import via **Theme Customizer > ↑↓**.

---

## 5. Layouts — Pages, Sections, Premade (`context: "et_builder_layouts"`)

**Files:** `Divi-5-Launch-Freebie_Pages.json`, `Divi-5-Launch-Freebie_All-Sections_Layouts.json`, `Divi-5-Launch-Freebie_Premade-Layouts.json`, `Divi-5-Launch-Freebie_Preset-Pages.json`, `Divi-5-Launch-Freebie_All-Individual-Sections.json`, and per‑section files under `Individual Sections/By Section Type/`.

**Root shape:**

```json
{
  "context": "et_builder_layouts",
  "data": {
    "228292": { layout post object },
    "228701": { ... }
  }
}
```

### Layout post object

Each value in `data` is a **WP post-like object**:

| Field | Description |
|-------|-------------|
| `ID` | Post ID (numeric) |
| `post_date`, `post_date_gmt` | |
| `post_content` | **Block markup** — `<!-- wp:divi/placeholder --><!-- wp:divi/section ... -->` … (see [Block Comment Format](block-format.md)) |
| `post_title` | |
| `post_excerpt` | |
| `post_status`, `comment_status`, `ping_status`, `post_password` | |
| `post_name` | Slug |
| `post_modified`, `post_modified_gmt` | |
| `post_content_filtered` | |
| `post_parent`, `menu_order` | |
| `post_type` | e.g. `et_pb_layout` |
| `post_mime_type`, `comment_count`, `filter` | |
| `post_meta` | Key/value meta |
| `terms` | Taxonomy terms |

Layout content lives in **`post_content`**: Gutenberg-style block comments (`wp:divi/section`, `wp:divi/row`, `wp:divi/column`, `wp:divi/heading`, etc.) with JSON attributes. Attributes can include:

- `module` — module settings (meta, decoration, sizing, etc.)
- `builderVersion`
- `modulePreset` — array of preset ids (e.g. `["vk5yn8ek75"]`)
- `groupPreset` — e.g. `{ "module.decoration.spacing": { "presetId": ["sjv7gwfcxt"], "groupName": "divi/spacing" } }`

Import via **Divi Library > Import & Export**; choose the appropriate layout type (pages, sections, etc.).

---

## Variable reference format

Global colors and variables can reference other variables with a **wrapper syntax**:

```
$variable({"type":"<type>","value":{"name":"<variable-id>","settings":{<optional overrides>}}})$
```

**Examples:**

- Color with opacity: `"$variable({\"type\":\"color\",\"value\":{\"name\":\"gcid-y43rzvjcdl\",\"settings\":{\"opacity\":90}}})$"`
- Content (e.g. number): `"$variable({\"type\":\"content\",\"value\":{\"name\":\"gvid-6kxjcrjyig\",\"settings\":{}}})$"`

`type` can be `color`, `content`, etc.; `name` is the global variable/color id; `settings` can override (e.g. `opacity` for colors).

---

## Design System ZIP file map

| JSON file | Context | Purpose |
|-----------|---------|--------|
| `Divi-5-Launch-Freebie_Global-Variables.json` | `et_builder` | Design variables (colors, numbers, strings, fonts, images, links) |
| `Divi-5-Launch-Freebie_Presets.json` | `et_builder` | Module + option group presets |
| `Divi-5-Launch-Freebie_Theme-Builder-Templates.json` | `et_theme_builder` | Template definitions + header/body/footer layouts |
| `Divi-5-Launch-Freebie_Theme-Customizer.json` | `et_divi_mods` | Theme Customizer options |
| `Divi-5-Launch-Freebie_Pages.json` | `et_builder_layouts` | Full page layouts |
| `Divi-5-Launch-Freebie_Preset-Pages.json` | `et_builder_layouts` | Preset demo pages |
| `Divi-5-Launch-Freebie_Premade-Layouts.json` | `et_builder_layouts` | Premade layout set |
| `Divi-5-Launch-Freebie_All-Sections_Layouts.json` | `et_builder_layouts` | All section layouts in one file |
| `Divi-5-Launch-Freebie_All-Individual-Sections.json` | `et_builder_layouts` | Same sections as individual layout entries |
| `Individual Sections/By Section Type/Divi-5-Launch-Freebie_*_Sections.json` | `et_builder_layouts` | One file per section type (Hero, FAQ, Team, etc.) |

Recommended **import order** (from Elegant Themes): Presets → Global Variables → Section Layouts → Page Layouts → Theme Builder Templates → Theme Customizer (optional).

---

## Related

- [Block Comment Format](block-format.md) — structure of `post_content` and block JSON attributes
- [JSON Attribute Map](json-attribute-map.md) — CSS-to-JSON paths and style migration
