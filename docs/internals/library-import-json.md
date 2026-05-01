---
title: "Library Import JSON Structure"
description: "Divi 5 library and design system import file formats — Global Variables, Presets, Theme Builder templates, Theme Customizer, and layout JSON structure."
category: internals
tags: [internals, library, import, design-system, json, presets, global-variables]
related: [block-format, json-attribute-map, import-library-elements]
divi_version: "5.x"
last_updated: 2026-04-30
---

# Library Import JSON Structure

How Divi 5’s **Divi Library** and **Design System** import/export JSON files are structured. This is reverse‑engineered from the [Divi 5 Launch Design System](https://www.elegantthemes.com/blog/divi-resources/divi-5-launch-gift-design-system) ZIP and applies to imports via **Divi > Divi Library > Import & Export**, **Theme Builder**, and **Theme Customizer**.

!!! abstract "Quick Reference"
    **What this documents:** The root `context`, top-level keys, and main data shapes for each import file type.
    **File types:** Global Variables | Presets | Theme Builder Templates | Theme Customizer | Layouts (pages, sections, premade).
    **Last verified:** 2026-03-17 (Design System ZIP); 2026-04-30 (library `terms` taxonomies — see [Document changelog](#document-changelog))

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

### Preset examples

**Minimal module preset** (no overrides — uses module defaults):

```json
{
  "id": "vruk2g8yjw",
  "name": "Heading Preset 1",
  "moduleName": "divi/heading",
  "version": "5.0.0-public-beta.3",
  "type": "module",
  "created": 1758716832549,
  "updated": 1758716832549
}
```

**Module preset with attrs** (Subheading — font size, line height, color from Design Variables):

```json
{
  "id": "1qsg0gx514",
  "name": "Subheading",
  "moduleName": "divi/heading",
  "version": "5.0.0-public-beta.3",
  "type": "module",
  "created": 1759320987336,
  "updated": 1763853708881,
  "attrs": {
    "title": {
      "decoration": {
        "font": {
          "font": {
            "desktop": {
              "value": {
                "headingLevel": "h4",
                "size": "$variable({\"type\":\"content\",\"value\":{\"name\":\"gvid-6kxjcrjyig\",\"settings\":{}}})$",
                "lineHeight": "$variable({\"type\":\"content\",\"value\":{\"name\":\"gvid-un2vx5k3ld\",\"settings\":{}}})$",
                "color": "$variable({\"type\":\"color\",\"value\":{\"name\":\"gcid-heading-color\",\"settings\":{}}})$"
              }
            }
          }
        }
      }
    },
    "css": {
      "desktop": {
        "value": {
          "mainElement": "padding-bottom: 0;"
        }
      }
    }
  },
  "renderAttrs": { }
}
```

Here `gvid-6kxjcrjyig` is a numbers variable (e.g. Subheading font size), `gvid-un2vx5k3ld` line height, and `gcid-heading-color` a global color. Layout blocks reference this preset via `modulePreset`: `["1qsg0gx514"]`.

**Group preset on a layout block** — layouts attach group presets in the block JSON like this:

```json
"groupPreset": {
  "module.decoration.spacing": {
    "presetId": ["sjv7gwfcxt"],
    "groupName": "divi/spacing"
  },
  "module.decoration.boxShadow": {
    "presetId": ["wuw39vfwm8"],
    "groupName": "divi/box-shadow"
  }
}
```

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
| `post_meta` | Key/value meta (see [`_et_pb_predefined_layout`](#post_meta-layout-flags)) |
| `terms` | Taxonomy terms — **required** for correct Visual Builder library pickers; see [Taxonomy reference (`terms`)](#taxonomy-reference-terms) |

Layout content lives in **`post_content`**: Gutenberg-style block comments (`wp:divi/section`, `wp:divi/row`, `wp:divi/column`, `wp:divi/heading`, etc.) with JSON attributes. Attributes can include:

- `module` — module settings (meta, decoration, sizing, etc.)
- `builderVersion`
- `modulePreset` — array of preset ids (e.g. `["vk5yn8ek75"]`)
- `groupPreset` — e.g. `{ "module.decoration.spacing": { "presetId": ["sjv7gwfcxt"], "groupName": "divi/spacing" } }`

Import via **Divi Library > Import & Export**; choose the appropriate layout type (pages, sections, etc.).

### Taxonomy reference (`terms`)

Each library layout in `data` should include a **`terms`** array with **WordPress term-shaped objects**. Divi 5 uses (at least) **three custom taxonomies** on `et_pb_layout` posts. For a **full page layout** that must appear under **Visual Builder → Add Layout → Saved Layout**, all three must be present with compatible slugs.

Official import **context** naming for library exports is documented by Elegant Themes (e.g. [`et_builder_layouts`](https://help.elegantthemes.com/en/articles/2612617-how-to-fix-the-this-file-should-not-be-imported-in-this-context-error-when-importing-a-json-file-in-divi)).

#### 1. `layout_type`

Classifies what kind of library item this is (page layout vs section vs row vs module). The **slug must match how the Visual Builder filters the “Load from Library” / “Saved Layout” lists** for each entry point — not the English label you might expect (see [Common pitfalls](#common-pitfalls-library-json-imports)).

| Slug | Typical meaning | Verification |
|------|-----------------|--------------|
| `layout` | Full page layout (appears in **Add Layout → Saved Layout**) | Verified on Divi 5 (community testing, Nov 2025; doc update Apr 2026) |
| `section` | Saved section | **Not verified in this doc revision** — export a saved section from **Divi → Divi Library** and inspect `terms` |
| `row` | Saved row | **Not verified in this doc revision** — export a saved row and inspect `terms` |
| `module` | Saved module | **Not verified in this doc revision** — export a saved module and inspect `terms` |

The **display name** (`name`) in JSON often mirrors the admin “Type” column (e.g. `"Layout"`, `"Section"`). The **`slug`** is what must be correct for the builder UI.

#### 2. `scope`

Whether the item behaves as an ordinary library item or a **global** (site-wide) one.

| Slug | Typical meaning | Verification |
|------|-----------------|--------------|
| `not_global` | Regular library item | Verified for non-global full page layouts (community testing, Nov 2025) |
| `global` | Global library item | **Not verified in this doc revision** — export a known global element and inspect `terms` |

#### 3. `module_width`

For section-level items, distinguishes **regular** sections from **specialty** sections in Divi’s internal classification.

| Slug | Typical meaning | Verification |
|------|-----------------|--------------|
| `regular` | Standard (non-specialty) | Verified for typical full page layouts (community testing, Nov 2025) |
| `specialty` | Specialty section layout | **Not verified in this doc revision** — export a specialty section if applicable |

Each term object generally includes: `name`, `slug`, `taxonomy`, `term_group`, `term_taxonomy_id`, `description`, `parent`, `count`, `filter` — mirroring what Divi writes when **exporting** a layout. Placeholder zeros in export files are normal; Divi assigns real IDs on import.

### Visual Builder entry points filter by `layout_type`

There is **no single “generic” library item** that appears in every “Add from Library” picker. The Visual Builder **filters saved library items by the user’s entry point**:

| User action | Picker | Expect `layout_type` slug |
|-------------|--------|---------------------------|
| **Add Layout** (page) | Saved Layout | `layout` |
| **Add Section** | Add From Library | `section` |
| **Add Row** | Add From Library | `row` |
| **Add Module** | Add From Library | `module` |

If you generate `et_builder_layouts` JSON programmatically, **`layout_type` must match the workflow** your users will use. Correct `post_content` alone is not enough if the taxonomies disagree.

### `post_meta` layout flags

| Key | Example | Meaning |
|-----|---------|--------|
| `_et_pb_predefined_layout` | `"off"` | User-created / imported layout (not a bundled premade) |
| `_et_pb_predefined_layout` | `"on"` | Bundled or predefined layout treatment (see also [Global Elements](../builder/global-elements.md)) |

Setting `_et_pb_predefined_layout` to `"off"` for custom imports matches typical exported user layouts and avoids treating the item like a premade package layout.

### Minimal `terms` example (full page layout)

Verified combination for a **non-global, regular** full page layout that surfaces under **Add Layout → Saved Layout**:

```json
"terms": [
  {
    "name": "Layout",
    "slug": "layout",
    "term_group": 0,
    "term_taxonomy_id": 0,
    "taxonomy": "layout_type",
    "description": "",
    "parent": 0,
    "count": 1,
    "filter": "raw"
  },
  {
    "name": "Not Global",
    "slug": "not_global",
    "term_group": 0,
    "term_taxonomy_id": 0,
    "taxonomy": "scope",
    "description": "",
    "parent": 0,
    "count": 1,
    "filter": "raw"
  },
  {
    "name": "Regular",
    "slug": "regular",
    "term_group": 0,
    "term_taxonomy_id": 0,
    "taxonomy": "module_width",
    "description": "",
    "parent": 0,
    "count": 1,
    "filter": "raw"
  }
]
```

### Verifying taxonomy slugs before you rely on them

This page **does not** substitute for inspecting a real export on your Divi version:

1. In Divi 5, save a library item of the type you care about (section, row, module, global, specialty section, etc.).
2. **Export** it from **Divi → Divi Library** (or the same portability flow you use for production JSON).
3. Open the JSON and copy the `terms` array from the matching `data` entry.

If a slug in the tables above differs from your export, **trust your export** and consider opening a PR to update this doc.

### Common pitfalls: library JSON imports

!!! warning "Silent failure: import succeeds but the layout never appears in the Visual Builder"
    **Symptom:** JSON imports without error; the item appears in **WP Admin → Divi → Divi Library**, but it **does not** appear in the Visual Builder picker (e.g. **Add Layout → Saved Layout**).

    **Cause:** Wrong or incomplete **`terms`** — especially **`layout_type`** — so the admin list and the builder filters disagree.

    **`slug: "page"` on `layout_type`:** The word “page” feels semantically right for a full page layout, but it is **not** the slug the builder uses for the Saved Layout list. **`layout_type` must use `slug: "layout"`** for that entry point (verified Nov 2025). Replacing `page` with `layout` fixed the issue with no other JSON changes.

    **Remediation:** Use the [minimal `terms` example](#minimal-terms-example-full-page-layout) as a baseline for full page layouts; for other item types, **export a known-good item** and mirror its `terms`.

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

## Root schema quick reference

Compact view of required root keys per context. Optional or often-empty keys (`canvases`, `images`, `thumbnails`) omitted.

**`et_builder`** (Global Variables and/or Presets):

```text
context: "et_builder"
data: []
presets: [] | { module?: { [moduleSlug]: { default, items } }, group?: { [groupName]: { default, items } } }
global_colors: [ [id, { color, status, label } ], ... ]
global_variables: [ { id, label, value, order, status, lastUpdated, variableType, type, groupKey? }, ... ]
```

**`et_builder_layouts`** (pages, sections, premade):

```text
context: "et_builder_layouts"
data: { [postId]: { ID, post_content, post_title, post_type, post_meta, terms, ... } }
```

**`et_theme_builder`**:

```text
context: "et_theme_builder"
templates: [ { title, default, enabled, use_on, exclude_from, layouts: { header, body, footer }, description }, ... ]
layouts: { [layoutId]: { context, data, post_title, post_type, theme_builder, global_colors, post_meta, ... } }
presets?: {}
global_colors?: []
global_variables?: []
has_default_template?: boolean
has_global_layouts?: boolean
```

**`et_divi_mods`** (Theme Customizer):

```text
context: "et_divi_mods"
data: { body_font_size, heading_font, body_font, header_color, font_color, link_color, accent_color, ... }
```

---

## Step-by-step: Importing the Design System

Use this order on a **clean Divi 5 site** to avoid conflicts and missing variable references.

1. **Download and extract** the Design System ZIP (e.g. from the [Divi 5 Launch Gift](https://www.elegantthemes.com/blog/divi-resources/divi-5-launch-gift-design-system) post).
2. **Divi → Divi Library → Import & Export**
   - **Import Presets:** Choose `Divi-5-Launch-Freebie_Presets.json`, ensure **Import Presets** is checked, import.
   - **Import Global Variables:** Choose `Divi-5-Launch-Freebie_Global-Variables.json`, ensure **Import Global Variables** is checked, import.
   - **Import section layouts:** Choose `Divi-5-Launch-Freebie_All-Sections_Layouts.json` (or `Divi-5-Launch-Freebie_All-Individual-Sections.json` for individual sections). Import as layouts.
   - **Import page layouts:** Choose `Divi-5-Launch-Freebie_Pages.json` (and optionally `Divi-5-Launch-Freebie_Preset-Pages.json`, `Divi-5-Launch-Freebie_Premade-Layouts.json`). Import as layouts.
3. **Divi → Theme Builder → ↑↓** (Import/Export)
   - Import `Divi-5-Launch-Freebie_Theme-Builder-Templates.json` with **Presets** enabled. Allow override of existing template assignments if the site is new.
4. **Optional — Divi → Theme Customizer → ↑↓**
   - Import `Divi-5-Launch-Freebie_Theme-Customizer.json` to apply baseline typography and colors at the Customizer level.

After import, customize via **Design Variables** first (colors, fonts, spacing); presets and layouts that reference them will update automatically.

---

## Document changelog

| Date | Change |
|------|--------|
| 2026-04-30 | Documented library `terms` taxonomies (`layout_type`, `scope`, `module_width`), Visual Builder entry-point filtering, `_et_pb_predefined_layout`, minimal full-page `terms` example, and silent-failure pitfall (`layout_type` `page` vs `layout`). Slugs for section/row/module/global/specialty called out as **not re-verified in-repo** — confirm via export on Divi 5. |
| 2026-03-17 | Initial structure from Design System ZIP (`context` keys, presets, Theme Builder, Customizer, layout posts). |

## Related

- [Block Comment Format](block-format.md) — structure of `post_content` and block JSON attributes
- [JSON Attribute Map](json-attribute-map.md) — CSS-to-JSON paths and style migration
- [Import Elements from Divi Library](../troubleshooting/import-library-elements.md) — end-user picker workflows that these taxonomies must satisfy
