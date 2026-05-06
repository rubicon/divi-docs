---
name: divi-5-docs-skill
description: Write, maintain, and review documentation pages for the Divi 5 Technical Documentation project. Use when creating new Divi 5 doc pages, processing scraped content from elegantthemes.com, reviewing contributions, updating existing docs, or working on any content for the divi-docs GitHub repository. Produces correctly formatted Markdown with proper frontmatter, screenshot references, and consistent structure.
---

# Divi 5 Technical Documentation — Claude Skill

## Overview

This skill produces documentation pages for the Divi 5 Technical Documentation project (https://github.com/16wells/divi-docs). Every page follows a strict template, uses YAML frontmatter, and targets the MkDocs Material static site generator.

**Scope: Divi 5 only.** Divi 4 is being phased out and is not documented in this project.

## Content Pipeline

Documentation is built through a scrape-then-enrich workflow:

1. **Scrape**: Content is crawled from elegantthemes.com and other Divi resources using `scripts/scrape_docs.py`
2. **Draft**: Scraped content is converted to structured Markdown matching our template
3. **Enrich**: Claude (in this project) or human contributors add tested code examples, screenshots, troubleshooting tips, and cross-references
4. **Screenshot**: `scripts/capture_screenshots.py` captures, crops, and optimizes screenshots from live Divi sites
5. **Review**: All content goes through PR review before publishing
6. **Update**: When source material changes, pages are re-scraped and diffs are reviewed

When processing scraped content, Claude should:
- Restructure the raw content to match the doc template below
- Fill in settings tables from the scraped data (every setting, not just common ones)
- Add `<!-- TODO: ... -->` markers for anything that needs human verification
- Flag any content that seems outdated or inconsistent
- Add `source_url` to frontmatter so we can re-scrape later

## Repository Structure

```
divi-docs/
├── mkdocs.yml              ← Site config and navigation
├── scripts/
│   ├── scrape_docs.py      ← Content scraper
│   ├── capture_screenshots.py  ← Screenshot tool
│   └── screenshots.yml     ← Batch screenshot config
├── docs/
│   ├── index.md            ← Homepage
│   ├── manifest.json       ← Machine-readable doc map
│   ├── contributing.md     ← How to contribute
│   ├── assets/
│   │   └── screenshots/    ← All screenshots organized by section
│   │       ├── modules/
│   │       │   ├── blurb/
│   │       │   ├── text/
│   │       │   └── ...
│   │       ├── builder/
│   │       ├── theme-options/
│   │       └── ...
│   ├── modules/            ← Individual module docs
│   ├── theme-options/      ← Theme Options panel settings
│   ├── builder/            ← Visual Builder + Theme Builder
│   ├── api/                ← Hooks, filters, custom modules
│   ├── css-reference/      ← Class names, selectors, overrides
│   ├── recipes/            ← Step-by-step how-to guides
│   └── troubleshooting/    ← Common issues and fixes
└── templates/
    └── doc-template.md     ← Template for new pages
```

## Page Template

Every documentation page MUST follow this structure:

```markdown
---
title: "Human-Readable Title"
category: modules | theme-options | builder | api | css-reference | recipes | troubleshooting
tags: [tag1, tag2, tag3]
related: [other-page-slug, another-page-slug]
divi_version: "5.x"
last_updated: YYYY-MM-DD
source_url: "https://elegantthemes.com/..."
---

# Page Title

One-sentence description of what this is and what it does.

## Overview

2-3 paragraphs: what it is, when/why to use it, how it fits into Divi 5.

![Overview screenshot](../assets/screenshots/category/slug/overview.png){ loading=lazy }
*Caption describing what the screenshot shows.*

## Settings & Options

### Content Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Name    | type | default | What it does |

![Content tab settings](../assets/screenshots/category/slug/settings-content.png){ loading=lazy }

### Design Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|

![Design tab settings](../assets/screenshots/category/slug/settings-design.png){ loading=lazy }

### Advanced Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|

## Code Examples

Real, tested code with language-tagged fenced blocks.

## Common Patterns

2-3 real-world use cases with screenshots of the end result.

![Pattern example](../assets/screenshots/category/slug/pattern-card-grid.png){ loading=lazy }
*Three-column blurb card grid with hover effects.*

## Elegant Themes tutorials

Long-form posts on the Elegant Themes **blog** (Divi Resources, Theme Releases). Link them here when a tutorial teaches the same feature as this page. Use a short bullet list; each link should open in a new tab: `[Post title](https://www.elegantthemes.com/blog/...){:target="_blank"} — one-line context`.

Add new URLs to `planning/et-blog-tutorials-map.md` for weekly maintenance.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

Known issues with admonition blocks.

## Related

- [Related Page](../category/slug.md)
```

## Screenshot Conventions

Screenshots are central to this project. Every doc page should include screenshots of:

1. **The module/feature in the Visual Builder** — what it looks like when editing
2. **Each settings tab** — Content, Design, Advanced panels
3. **Front-end output** — what the module renders on a live site
4. **Common patterns** — real-world usage examples
5. **Before/after** for troubleshooting sections where applicable

### File Organization

```
docs/assets/screenshots/
└── {category}/
    └── {page-slug}/
        ├── overview.png           ← Hero screenshot of the feature
        ├── settings-content.png   ← Content tab in settings panel
        ├── settings-design.png    ← Design tab in settings panel
        ├── settings-advanced.png  ← Advanced tab in settings panel
        ├── frontend-default.png   ← Default front-end rendering
        ├── pattern-{name}.png     ← Common pattern examples
        └── issue-{name}.png       ← Troubleshooting screenshots
```

### Screenshot Naming

- Lowercase with hyphens: `settings-content.png`, not `Settings Content.png`
- Prefix with context: `settings-`, `frontend-`, `pattern-`, `issue-`
- Be descriptive: `pattern-card-grid.png` not `pattern-1.png`

### Markdown Image Syntax

Always use MkDocs Material's lazy loading and include a caption:

```markdown
![Alt text describing the screenshot](../assets/screenshots/category/slug/filename.png){ loading=lazy }
*Caption explaining what we're looking at and why it matters.*
```

### Capturing Screenshots

Use `scripts/capture_screenshots.py` for automated captures:
- Element-specific captures use CSS selectors (e.g., `--selector ".et_pb_blurb"`)
- Settings panels use `--selector ".et-fb-settings-content"`
- Images are auto-optimized to max 1200px wide at 2x resolution for retina
- Batch configs go in `scripts/screenshots.yml`

For manual screenshots (e.g., from the Visual Builder where automation is tricky):
- Capture at 2x resolution (retina)
- Crop to show only the relevant UI — no browser chrome, no taskbar
- Save as PNG
- Run through the optimizer: `python3 scripts/capture_screenshots.py` with the `--max-width 1200` flag
- Place in the correct `docs/assets/screenshots/{category}/{slug}/` directory

## Writing Standards

### Scope
- **Divi 5 only.** Do not document Divi 4 behavior, settings, or differences.
- If a feature is new in Divi 5, just document it — no need to say "new in Divi 5"
- If a feature existed before but works differently now, just document the current behavior

### Tone
- Write for practitioners — assume WordPress knowledge, don't assume Divi expertise
- Be specific and precise — document actual behavior, not marketing language
- Show, don't just tell — screenshots and code examples over descriptions

### Code Examples
- Always use fenced code blocks with language tags: ```php, ```css, ```html
- Test code before including it — examples must actually work
- Include comments explaining non-obvious behavior
- Show both minimal and real-world usage

### Settings Tables
- Document EVERY setting, not just the commonly used ones
- Include the type (text, toggle, select, range, color, upload, etc.)
- Include the default value
- Describe behavior, not just what the label says
- Group by tab: Content, Design, Advanced

### Cross-References
- Use relative paths for internal links: `[Blurb Module](../modules/blurb.md)`
- Include related pages in frontmatter AND in the Related section at the bottom

### Elegant Themes blog tutorials (maintenance)
- When Divi Resources or Theme Releases publishes a tutorial for a documented feature, add **`## Elegant Themes tutorials`** to the matching reference page (see template above) and a row to **`planning/et-blog-tutorials-map.md`**.
- Place the section **immediately before `## Version Notes`** when that heading exists; otherwise **immediately before `## Related`**.
- Prefer linking to the blog post over pasting its full text — the Help Center `source_url` remains the primary re-scrape target unless superseded.

### Admonitions (MkDocs syntax)
```markdown
!!! note "Title"
    Content

!!! warning "Title"
    Content

!!! tip "Title"
    Content
```

## After Creating a New Page

1. Add the page to the `nav` section in `mkdocs.yml`
2. Update the section's `index.md` status table (change 🔲 to ✅)
3. Add entries to `scripts/screenshots.yml` for screenshots needed
4. Add related page cross-references to/from existing pages
5. If Elegant Themes published a **blog** tutorial for the same feature, add **`## Elegant Themes tutorials`** plus an entry in `planning/et-blog-tutorials-map.md`

## Processing Scraped Content Workflow

When given raw scraped content to process:

1. Extract the title and restructure into our template
2. Build complete settings tables from any settings info in the source
3. Mark missing settings with `<!-- TODO: Verify setting name/type/default -->`
4. Add screenshot placeholders with the correct file paths
5. Add `source_url` to frontmatter
6. Generate a summary of what screenshots are needed
7. List any `mkdocs.yml` nav additions required

## LLM Playbooks (docs/playbooks/)

Playbooks are **LLM-first documentation**. Their primary reader is an AI assistant that's been asked to help someone work with Divi 5. Their secondary reader is a human. This changes how they're written.

### Playbook Frontmatter

```yaml
---
title: "Playbook Title"
category: playbooks
tags: [relevant, tags]
related: [other-playbook-slug]
divi_version: "5.x"
last_updated: YYYY-MM-DD
content_type: playbook
audience: llm
---
```

### Writing Style for Playbooks

Playbooks differ from reference docs in tone and structure:

- **Imperative voice.** "Do this. Then do this. Never do this." Not "you might consider..."
- **Rules before explanations.** State the rule, then explain why. LLMs need the rule first.
- **Decision trees over descriptions.** "If X, do A. If Y, do B." Not "there are several approaches."
- **Explicit failure modes.** Every rule should include what goes wrong if you break it.
- **Diagnostic tables.** End major playbooks with a symptom → cause → fix table.
- **"When Assisting a User" sections.** End each playbook with specific instructions for how an LLM should apply this knowledge during a conversation.

### Playbook Structure Template

```markdown
# Playbook: Title

**One-line summary of what this teaches.**

!!! danger "CRITICAL" (if applicable)
    The most important rule, stated bluntly.

## Why This Matters
Brief context — why an LLM needs to know this.

## Step-by-Step Process
Numbered, imperative steps.

## Known Gotchas
Admonition blocks for each gotcha.

## Quick Diagnostic Table (if applicable)
| Symptom | Cause | Fix |

## When Assisting a User
Instructions for how to apply this playbook in conversation.
```

## Internals (docs/internals/)

Internals document Divi 5's undocumented architecture — reverse-engineered from production builds. These are technical reference for developers and LLMs doing advanced work.

### Writing Style for Internals

- **Factual, precise, no opinions.** Document observed behavior, not recommendations.
- **Code-heavy.** Show the actual data structures, JSON, and JavaScript.
- **Date-stamped findings.** Divi 5 is in beta; behavior may change. Always note when something was last verified.
- **Cross-reference aggressively.** Internals pages should link to each other and to relevant playbooks.

## Content Types Summary

| Location | Content Type | Primary Reader | Tone |
|----------|-------------|---------------|------|
| `docs/modules/` | Reference docs | Humans looking things up | Descriptive, thorough |
| `docs/theme-options/` | Reference docs | Humans looking things up | Descriptive, thorough |
| `docs/builder/` | Reference docs | Humans looking things up | Descriptive, thorough |
| `docs/api/` | Reference docs | Developers | Technical, precise |
| `docs/css-reference/` | Reference docs | Developers | Technical, precise |
| `docs/playbooks/` | LLM playbooks | AI assistants | Imperative, rule-based |
| `docs/internals/` | Architecture docs | Developers + advanced LLMs | Factual, code-heavy |
| `docs/recipes/` | How-to guides | Humans following steps | Step-by-step, practical |
| `docs/troubleshooting/` | Problem/solution pairs | Humans debugging | Diagnostic, direct |
