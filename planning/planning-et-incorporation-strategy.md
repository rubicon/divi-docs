# ET Help Center Incorporation Strategy

*Created: 2026-03-16*

## Goal

Incorporate Elegant Themes' expanded Divi 5 Help Center (209 articles) into divi-docs as developer-first technical reference documentation, with links back to ET as the authoritative visual/tutorial source.

## The Core Problem

Divi 5 is built for humans clicking through a Visual Builder. There's no layout composition API, no CLI, no SDK. When an AI assistant is asked to help someone build with Divi, it needs to know exactly how Divi 5's element hierarchy works, what JSON block structures look like under the hood, which settings map to which CSS properties, and where the gotchas are. ET's documentation tells you how to click buttons. Our documentation tells an AI how to think about those same operations programmatically.

## Content Principles

### 1. Reference, Don't Replicate

Every page links to the corresponding ET Help Center article as the authoritative source. We do not copy their content wholesale. We restructure information into developer-formatted reference tables and add value layers ET doesn't provide.

**ET source callout pattern** (inline, not admonition):
```markdown
For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/XXXXX).
```

### 2. Developer-Formatted Reference, Not Tutorials

ET writes click-by-click tutorials. We write technical reference with settings tables in the established three-column format:

```markdown
| Setting | Type | Description |
|---------|------|-------------|
| Title | text | The heading text displayed in the clickable panel header. |
```

### 3. Shared Options Groups Referenced, Not Repeated

Design tab options (Sizing, Spacing, Border, Box Shadow, Text, Filters, Animation, Transform) are the same across most modules. Each module page references the ET Options Groups documentation rather than repeating identical descriptions. Module-specific design settings are documented individually.

### 4. AI Interaction Notes with Verification Status

Every programmatic claim gets a verification status marker indicating whether it's been tested on the 16wells.dev verification site. See `planning/verification-pipeline.md` for the full protocol.

### 5. Page Format Matches Established Template

All new pages follow the format established in the current module pages (e.g., `docs/modules/accordion.md`):

- YAML frontmatter with `source_url` pointing to the ET article
- Overview → Use Cases → How to Add → Settings & Options (Content/Design/Advanced tabs) → Code Examples → Common Patterns → AI Interaction Notes → Saving Your Work → Version Notes → Troubleshooting → Related
- Three-column settings tables (`Setting | Type | Description`)
- MkDocs Material admonitions for troubleshooting and version notes
- Screenshot placeholders with `{ loading=lazy }` and captions
- Relative path cross-references between pages

## What ET Now Covers (209 Articles)

| Collection | Articles | Our Coverage | Gap |
|---|---|---|---|
| Getting Started | ~13 | Partial | Install, migration, initial setup |
| VB Basics | 8 | Partial | Incomplete settings detail |
| VB Core Concepts | 6 | Partial via playbooks | Sections/Rows/Columns deep-dive |
| VB Advanced Concepts | 7 | Partial via internals | Nested modules, canvases, command center |
| **Modules** | **51** | **44 pages exist, recently rewritten** | **6 new modules + enrichment** |
| **WooCommerce Modules** | **25** | **21 pages exist, thin** | **4 missing + full settings** |
| **Options Groups** | **43** | **Zero dedicated pages** | **Entirely missing** |
| **Features** | **30** | **Partial via builder/** | **~20 features undocumented** |
| **Flexbox Layout** | **10** | **Zero dedicated pages** | **Entirely missing** |
| **CSS Grid Layout** | **2** | **Zero dedicated pages** | **Entirely missing** |
| FAQ & Troubleshooting | ~15 | Overview only | How-tos, CSS fixes, visibility |

## What We Write vs. What We Link To

| Content Type | We Write | We Link to ET |
|---|---|---|
| Settings tables (type + description) | ✅ Developer-formatted tables | Link for visual walkthrough |
| Click-by-click instructions | ❌ | ✅ Link as primary source |
| Screenshots of VB interface | Placeholder path only | ✅ Link to see screenshots |
| Element hierarchy / nesting rules | ✅ Structured tables | — |
| Code examples (PHP, CSS, JS) | ✅ Tested, working code | — |
| AI interaction notes | ✅ Original findings with verification status | — |
| Block JSON structures | ✅ Reverse-engineered | — |
| Design tab shared options | ✅ Reference link to ET collection | Link to ET's version |
| Troubleshooting diagnostics | ✅ Symptom→cause→fix admonitions | Link for visual guides |
| Playbooks (LLM-first docs) | ✅ 100% original | — |
| Internals (architecture docs) | ✅ 100% original | — |

## Phased Execution Plan

### Phase 1: Options Groups + Layout System (Weeks 1-3)
**Why first:** Options Groups are shared across every module. Layout System (Flexbox + CSS Grid) is Divi 5's biggest architectural change.

- Create `docs/options-groups/` section with ~43 reference pages
- Create `docs/builder/flexbox.md` and `docs/builder/css-grid.md`
- Create `docs/playbooks/layout-system.md` (LLM Playbook)
- Add Options Groups nav section to mkdocs.yml
- Scrape 55 ET articles (43 Options Groups + 12 Layout System)

### Phase 2: Module Enrichment + New Modules (Weeks 3-6)
**Why second:** With Options Groups documented, module pages can reference them.

- Enrich existing 44 module pages with ET source links and AI Interaction Notes
- Add 6 new Divi 5 modules: Group, Group Carousel, Heading, Hero, Icon List, Pagination
- Create `docs/playbooks/module-selection.md` (LLM Playbook)
- Scrape 51 ET module articles

### Phase 3: WooCommerce Modules (Weeks 6-8)
- Fill 21 existing WooCommerce module pages
- Add 4 missing: Woo Product Add to Cart, Woo Product Gallery, Woo Product Meta, Woo Product Upsell
- Create `docs/playbooks/woocommerce-templates.md` (LLM Playbook)
- Scrape 25 ET WooCommerce articles

### Phase 4: Features + Builder Deep-Dive (Weeks 8-10)
- Add ~18 new builder pages (nested modules, canvases, command center, presets, variables, interactions, etc.)
- Enrich existing builder pages
- Create `docs/playbooks/advanced-builder-ops.md` (LLM Playbook)
- Scrape ~51 ET articles (Features + VB Basics/Core/Advanced)

### Phase 5: Getting Started + FAQ/Troubleshooting (Weeks 10-11)
- Create `docs/getting-started/` section
- Enrich `docs/troubleshooting/` with ET FAQ articles
- Add recipes from ET how-to articles
- Scrape ~28 ET articles

### Phase 6: AI Bridge Playbooks (Weeks 11-12)
Capstone playbooks synthesizing all verified findings:
- `docs/playbooks/ai-divi-bridge.md` — Master AI ↔ Divi 5 interface patterns
- `docs/playbooks/ai-page-composition.md` — Building pages through AI
- `docs/playbooks/ai-content-operations.md` — Content CRUD through AI
- `docs/playbooks/ai-known-boundaries.md` — What AI cannot do in Divi 5

## ET Article URL Map

Complete mapping maintained in `planning/et-article-url-map.md`.
