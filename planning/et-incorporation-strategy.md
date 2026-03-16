# ET Help Center Incorporation Strategy

## Core Approach: Reference, Don't Replicate

Elegant Themes maintains a comprehensive Help Center at help.elegantthemes.com with 209 articles covering Divi 5. Our strategy is to **link to ET as the authoritative source** for visual walkthroughs, animated GIFs, and step-by-step builder tutorials — while we write **developer-formatted settings tables, code examples, and AI interaction notes** that ET doesn't provide.

Every divi-docs page that corresponds to an ET article includes:
- An inline link in the Overview: "For additional reference, see the [official Elegant Themes documentation](URL)."
- The ET article URL in frontmatter as `source_url`
- Original content: settings tables (3-column: `Setting | Type | Description`), CSS/PHP code examples, troubleshooting, and cross-references

We do **not** copy ET's prose, screenshots, or GIFs. We write everything in our own developer-reference voice.

---

## ET Help Center Structure (209 Articles)

| Collection | Articles | Our Coverage | Gap |
|-----------|----------|-------------|-----|
| Getting Started | 13 | 0 pages | Full gap |
| Initial Site Setup (New Sites) | 6 | 0 pages | Full gap |
| Migrating from Divi 4 | 4 | 0 pages | Full gap |
| VB Basics | 8 | 1 page (visual-builder.md) | 7 articles |
| VB Core Concepts | 6 | partial (builder/ section) | ~3 articles |
| VB Advanced Concepts | 7 | partial (builder/ section) | ~4 articles |
| Modules | 51 | 44 pages | 7 new modules needed |
| WooCommerce Modules | 25 | 21 stub pages | 4 new + 21 enrichment |
| Options Groups | 42 | 0 pages | **Full gap — highest priority** |
| Features | 30 | partial (builder/ section) | ~20 articles |
| Flexbox Layout System | 10 | 0 pages | **Full gap** |
| CSS Grid Layout System | 2 | 0 pages | **Full gap** |
| FAQ and Troubleshooting | 15 | 1 page (troubleshooting/) | 14 articles |

**Biggest gaps:** Options Groups (42 articles, zero coverage) and Layout Systems (12 articles, zero coverage).

---

## Six Phases

### Phase 1: Options Groups + Layout System
**Status: In Progress**

- Create `docs/options-groups/` section with ~42 reference pages
- Create `docs/builder/flexbox.md` and `docs/builder/css-grid.md`
- These are the most cross-referenced pages — module docs link to them for shared Design/Advanced tab settings

### Phase 2: Module Enrichment + New Modules
**Status: Planned**

- Enrich all 44 existing module pages with verified settings (currently based on ET reference, needs 16wells.dev verification)
- Create 7 new module pages: Group, Group Carousel, Heading, Hero, Icon List, Lottie, Pagination
- These modules exist in Divi 5 but were added after our initial scrape

### Phase 3: WooCommerce Modules
**Status: Planned**

- Enrich 21 existing WooCommerce module stubs with full settings tables
- Create 4 new WooCommerce module pages to match ET's 25-article collection
- Requires WooCommerce active on 16wells.dev for verification

### Phase 4: Features + Builder Deep-Dive
**Status: Planned**

- Cover ET's 30 Features articles (presets, global colors, find & replace, split testing, etc.)
- Expand Builder section with VB Basics, Core Concepts, and Advanced Concepts content
- Map to existing builder/ pages and create new ones where needed

### Phase 5: Getting Started + FAQ/Troubleshooting
**Status: Planned**

- Create getting-started section (installation, activation, first page)
- Create migration guide (Divi 4 to Divi 5)
- Expand troubleshooting section with ET's 15 FAQ articles
- Lower priority for our developer audience but useful for completeness

### Phase 6: AI Bridge Playbooks
**Status: Ongoing**

- Update existing LLM playbooks with verified findings from Phases 1-5
- Cross-reference playbooks to new Options Groups and Layout System pages
- Add playbook-specific notes to module pages ("When assisting a user...")

---

## Content Rules

1. **Settings tables use three columns:** `Setting | Type | Description` — no Default column (defaults change across contexts)
2. **ET source links go inline in Overview:** "For additional reference, see the [official Elegant Themes documentation](URL)."
3. **Shared Design tab options reference Options Groups pages** instead of repeating descriptions. Example: "See [Spacing Options](../options-groups/spacing.md) for full details."
4. **Every setting from the ET article must be documented** — don't skip obscure ones
5. **Code examples must be original and tested** — CSS selectors, PHP hooks, JavaScript patterns
6. **Verification status markers** track confidence level (see verification-pipeline.md)
