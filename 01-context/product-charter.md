# Product Charter — Divi 5 Technical Documentation

> This file is the source of truth for **what this product is, who it's for, why we're building it, and what's in/out of scope.** It's the internal-product analogue of `client-profile.md` in a client engagement — but for projects owned by 16Wells, not delivered to a client. Read this before any scope, positioning, or build decision.

## The Product

**One-liner:** A community-maintained technical reference for Divi 5 — modules, builder, theme options, API, CSS, troubleshooting, and recipes — published as a MkDocs Material site at [16wells.github.io/divi-docs](https://16wells.github.io/divi-docs/).

**What it does:** Fills the gaps in Elegant Themes' official Divi 5 documentation with practical, implementation-ready content. Scraped Elegant Themes pages get restructured into a consistent template; tested code examples, screenshots, and edge-case notes get added through community contributions. The site supports both human readers (Divi implementers) and AI assistants (via dedicated `docs/playbooks/` LLM-targeted content).

**Stage:** live — public deployment running, content pipeline established, scraping + screenshot workflows in place, weekly monitoring task automated. Steady-state content maintenance and expansion.

## Why We're Building It

Divi powers 800,000+ websites, but its official documentation has significant gaps — especially around Divi 5, which is a ground-up rebuild (not Divi 4 with updates). For 16Wells, that gap is a daily friction point: building client sites on Divi 5 requires implementation depth that Elegant Themes' references don't provide.

This project converts that friction into a published asset:

1. **Direct utility:** The same documentation 16Wells needs internally becomes searchable on a public site, useful for any session (client work, AI agent context, self-reference).
2. **Positioning leverage:** Owning the most-actionable Divi 5 technical reference establishes 16Wells as a credible Divi expert beyond client engagements.
3. **AI-readable surface:** With dedicated `docs/playbooks/` content written for LLM consumption, Claude and other AI assistants can navigate Divi 5 work more competently — improving the speed and quality of 16Wells's own AI-assisted client builds.
4. **Community contribution:** Public repo invites tested examples, troubleshooting tips, and screenshot contributions that scale the content beyond what 16Wells could maintain alone.

## The User

**Who uses it:** Two primary audiences with a third secondary one.

1. **Divi 5 implementers** — designers, developers, agencies, and DIY site owners building Divi 5 sites. They land on the docs via search or direct link looking for a specific module reference, troubleshooting answer, or how-to recipe.
2. **AI assistants** — Claude (Code, Cowork, Chat), Cursor, and other coding agents working on Divi 5 sites. The `docs/playbooks/` content is written *for* them — imperative, rule-based, machine-parsable.
3. **The 16Wells team itself** — daily reference for client builds, training material for contractors, source of truth when "how does Divi 5 do X" comes up mid-engagement.

**Decision-makers:** Skip Shean owns project direction, editorial quality, and merge approval. Community contributors can open PRs but Skip is the gatekeeper on publication-impacting changes.

**The job they hire it for:** Get a definitive, complete, current answer for how Divi 5 does X without sifting through Elegant Themes' fragmented official docs, outdated forum threads, or Divi 4 content that doesn't apply.

**Anti-persona — who this is *not* for:**
- Divi 4 users. **Out of scope.** Divi 4 is being phased out and is not covered.
- Non-Divi users looking for general WordPress documentation.
- Anyone wanting marketing content about why to choose Divi — this is an implementer's reference, not a sales site.

## Content Layers

Three distinct content layers, each with different tone, audience, and writing style (see `SKILL.md` for full details):

| Directory | Content Type | Primary Audience | Tone |
|-----------|-------------|-----------------|------|
| `docs/modules/`, `docs/builder/`, `docs/theme-options/`, `docs/api/`, `docs/css-reference/` | Reference docs | Humans | Descriptive, thorough |
| `docs/playbooks/` | LLM playbooks | AI assistants | Imperative, rule-based |
| `docs/internals/` | Architecture docs | Developers + LLMs | Factual, code-heavy |
| `docs/recipes/` | How-to guides | Humans | Step-by-step |
| `docs/troubleshooting/` | Problem/solution | Humans | Diagnostic, direct |

## Scope Boundaries

**In scope:**
- Divi 5 module references with full settings tables (every setting, not just common ones).
- Builder UI, theme options, API hooks/filters, CSS variables, recipes, troubleshooting.
- LLM playbooks for AI-assisted Divi 5 work.
- Automated scraping from Elegant Themes + screenshot capture pipelines.
- Weekly content monitoring and broken-link checks.
- Public deployment via GitHub Pages + GitHub Actions.

**Out of scope:**
- **Divi 4.** Not covered, not back-ported, not added even as historical reference.
- Marketing content selling Divi or the 16Wells practice.
- Divi 5 theme customization beyond what implementers need (no "10 prettiest Divi sites" listicles).
- Closed-source pivots — repo is community-maintained.

**Maybe-later parking lot:**
- Versioning + changelog convention so the site can target a specific Divi 5 minor version.
- Direct integration with the published `claude-skills/style-guide` Claude skill for in-editor lookups.
- Sponsorship or attribution model if community contribution volume warrants it.

## Success Criteria

> What "this worked" looks like.

- Comprehensive module coverage — every Divi 5 module has a reference page with the complete settings table.
- Weekly content monitor catches Divi 5 updates and produces actionable reports without manual chasing.
- The site is the default reference for 16Wells client builds — "how does X work in Divi 5" lands here, not on a search.
- At least 3 substantive community contributions land per quarter once the site is well-populated.
- `docs/playbooks/` is materially useful to AI assistants — measurable as fewer "what does this Divi 5 thing do" gaps in client-engagement AI-assisted work.

## Kill Criteria

> When would we sunset this.

- Elegant Themes ships official documentation that matches or exceeds this site's depth and currency. Unlikely soon; possible long-term.
- Divi 5 is abandoned by Elegant Themes or replaced by a different Divi successor that doesn't carry the Divi 5 architecture forward.
- Maintenance burden exceeds the value 16Wells gets from owning the asset (community contributions die off, automated monitor breaks, scraping pipeline becomes unmaintainable).

## Editorial Voice and Communication Preferences

- Technical, direct, and practical. No marketing language.
- Explicit instructions over high-level descriptions.
- Examples concrete and Divi 5 specific (never "in Divi" — always "in Divi 5").
- Settings tables comprehensive, not curated. Every setting documented.
- Code examples carry language tags. Cross-references use relative paths.
- LLM playbooks: imperative, deterministic, rule-based. Designed to compress well into agent context windows.

## Key Trust Signals / Proof Points

- Public Git repository with transparent history at github.com/16wells/divi-docs.
- Live docs deployment pipeline via GitHub Actions; site at 16wells.github.io/divi-docs.
- Structured content standards documented in `SKILL.md`.
- Automated scraping + monitor scripts visible in `scripts/`.
- Screenshot coverage for visual reference pages.
- AI-readable playbook content — demonstrates the site treats LLMs as a first-class audience.

---
*Sources this charter was built from:*
- The pre-2026-05-21 `client-profile.md` (now this file) — original positioning content.
- `CLAUDE.md` — content type table, scope rules, common tasks.
- `README.md` — public-facing project description and pipeline.
- `SKILL.md` — documentation template and writing standards.

*Last updated: 2026-05-21 (re-templated from `client-profile.md` to product-charter format; original positioning content preserved and expanded into the internal-product schema).*
