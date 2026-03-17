---
title: "Design: Style Guide → Divi 5 Global Variables Import"
category: internals
tags: [design-system, global-variables, tokens, import, json]
divi_version: "5.x"
last_updated: 2026-03-17
---

# Design: Style Guide → Divi 5 Global Variables Import

Define a repeatable workflow (and companion Claude skill) that takes an arbitrary “style guide” input (prose and/or design tokens) and produces a **Divi 5–importable** JSON file for **Global Variables**.

## Goals

- Accept **format-agnostic** style guides (Markdown, copied doc text, “PDF text dump”, etc.).
- Prefer **explicit tokens** (JSON/table/CSV) when provided; fall back to extraction from prose.
- Output a valid Divi import file with `context: "et_builder"` containing:
  - `global_colors`
  - `global_variables`
- Keep IDs **stable** across re-runs to support safe re-import and updates.
- Never invent values: only emit variables with explicit values; provide a “missing tokens” report.

## Non-goals

- Generating Divi module presets automatically (future phase; higher schema volatility).
- Perfectly parsing every possible style guide format with zero ambiguity.

## Inputs

### Required

- **Style guide source text** (any text). This may be highly structured or purely narrative.

### Optional (preferred)

- **Tokens payload**, one of:
  - **JSON** (any reasonable token structure)
  - **Table/CSV** with (at minimum): `name`, `type`, `value` (optional: `category`)

## Output artifact

### Divi 5 Global Variables import JSON

Single JSON object (root):

- `context`: `"et_builder"`
- `data`: `[]`
- `presets`: `[]`
- `global_colors`: array of tuples `[id, { color, status, label }]`
- `global_variables`: array of objects `{ id, label, value, order, status, lastUpdated, variableType, type, groupKey? }`
- `canvases`: `[]`
- `images`: `[]`
- `thumbnails`: `[]`

See `docs/internals/library-import-json.md` for the reverse-engineered schema.

## Extraction model

### Precedence

1. **Tokens payload** (if provided)
2. **Style guide prose extraction**

If both provide the same logical token, tokens payload wins.

### Confidence gating (prose)

Only extract when there is an **explicit value** present, e.g.:

- Colors: `#RRGGBB`, `rgb(...)`, `rgba(...)`, `hsl(...)`, `hsla(...)`
- Sizes: `48px`, `1.2` (line-height), `-0.5px` (letter-spacing)
- Shadows: `0 2px 8px rgba(0,0,0,0.08)`
- URLs/emails/phones
- Font families: quoted or clearly named families (e.g. `Inter`, `Open Sans`)

If the text describes intent without a value (e.g. “use a deep navy”), it is reported as missing.

## Normalization rules

- **Colors**: keep as hex if present; otherwise keep original functional color string (`rgb/rgba/hsl/hsla`).
- **Numbers**: store as string values with units when appropriate (`"16px"`, `"1200px"`, `"1.2"`).
- **Fonts**: store font family names as plain strings.
- **Strings/Links**: store as plain strings.

## Token taxonomy (canonical names)

The generator should map found values into a canonical name hierarchy:

- `color.brand.*`, `color.neutral.*`, `color.semantic.*`
- `font.heading.family`, `font.body.family`
- `type.h1.size`, `type.h1.lineHeight`, `type.h1.letterSpacing`, `type.h1.weight`, `type.h1.color` (if present)
- `space.*` (scale), `radius.*`, `shadow.*`
- `layout.container.max`, `layout.text.max`, `layout.breakpoint.*` (if present)
- `link.*`, `string.*`

These names are used for labels/IDs and for a human-facing “token report”.

## ID strategy (stable)

Divi global identifiers are free-form strings. Use stable, deterministic IDs:

- **Global colors**: `gcid-<slug>`
- **Global variables**: `gvid-<slug>`

Where `<slug>` is derived from canonical name (or label), normalized to:

- lowercase
- alphanumerics and hyphens only
- collapse repeats, trim hyphens

Collision handling: append `-2`, `-3`, etc.

## Divi variable typing

Map token categories to Divi’s `type`:

- Colors → `colors` (+ mirrored entry in `global_colors`)
- Font families → `fonts`
- Measurements, type scale, spacing, radii, shadows → `numbers`
- Brand phrases, address, CTA copy → `strings`
- URLs → `links`
- Images (if present) → `images`

For each variable object:

- `status`: `"active"`
- `lastUpdated`: ISO 8601 (generation time)
- `variableType`: same as `type`
- `order`: `""` (or a numeric string, if we decide to enforce ordering later)
- `groupKey`: optional, may be used to group in UI (e.g. `"colors"`, `"fonts"`)

## Deliverables for documentation

Update `docs/recipes/import-design-systems.md` with a new section:

- “Generate a Divi Global Variables JSON from a style guide”
- Include a minimal token table schema (BYO mapping) to maximize reliability
- Include import steps and troubleshooting notes

## Companion Claude skill

Implemented as **[16wells/divi-styleguide-variables](https://github.com/16wells/divi-styleguide-variables)** (Claude skill “divi-variables-from-style-guide”):

- Accept: brand name/slug + style guide text + optional tokens payload (JSON/table)
- Output:
  - importable JSON (`context: "et_builder"`)
  - a token/ID report table
  - a missing/ambiguous tokens checklist

