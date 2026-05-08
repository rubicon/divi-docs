# CLAUDE.md — Instructions for Claude Code

## Project Overview

This is the **Divi 5 Technical Documentation** site — a community-maintained MkDocs Material documentation project for the Divi 5 WordPress theme. The repo lives at https://github.com/16wells/divi-docs and deploys to https://16wells.github.io/divi-docs/ via GitHub Actions.

## Key Files

- **SKILL.md** — Complete documentation template, frontmatter schema, writing standards, and content type definitions. READ THIS FIRST before creating or editing any documentation pages.
- **claude-skills/README.md** — References to external Claude skills (e.g. style-guide → Divi variables); install/update from their repos.
- **mkdocs.yml** — Site config and navigation. Update this whenever you add new pages.
- **docs/manifest.json** — Machine-readable map of the site structure.
- **templates/doc-template.md** — Blank template for new reference doc pages.

## How to Get Oriented on Specific Topics

| If you need to know... | Read this |
|---|---|
| What's happening *right now* — in-progress work, awaiting decisions, deployed state | `01-context/state.md` |
| What changed recently across Claude surfaces (chronology) | `01-context/activity-log.md` |
| Open decisions or pending owner items | `01-context/decisions-log.md` |
| Working assumptions, patterns, or gotchas | `01-context/insights.md` |
| Client/project profile and voice constraints | `01-context/client-profile.md` |
| Scope boundaries and delivery architecture | `01-context/project-scope.md` |

## Iterative Memory — Update As You Go

Work may happen across multiple Claude surfaces (Cursor/Cowork, Claude Code, and Claude chats). These surfaces do not share live memory, so this repository's context files are the handoff mechanism — but only if they actually reflect reality. Memory upkeep is part of the work, not a chore at the end of it.

**Resume discipline — at session start, read in this order:**
1. This `CLAUDE.md` for project orientation.
2. `01-context/state.md` for what is happening *right now*.
3. The most recent 5 entries in `01-context/activity-log.md` for chronology.
4. Open items in `01-context/decisions-log.md`.

If `state.md` is current, the chat history should be irrelevant to resumption.

**Checkpoint triggers — update the appropriate file IMMEDIATELY when:**

| Event | Update |
|---|---|
| A decision is made (closed or opened) | `decisions-log.md` |
| A finding, quirk, gotcha, or pattern is discovered | `insights.md` |
| A meaningful step completes (commit, deploy, gate passed, file created, milestone met) | `activity-log.md` (append) and `state.md` (refresh in-progress section) |
| External system state changes (deploy, config, schedule, data) | `state.md` → External Systems State |
| You pause for human review or sign-off | `state.md` → Awaiting Human Decision |
| You sense context-window pressure or are about to be compacted | full flush of `state.md` first, then continue |
| The user says "checkpoint" or runs `/checkpoint` | full pass: state, activity log, decisions, insights — then commit |

**Commit discipline.** Commit after each significant checkpoint, not in batches at session end. The gap between *logged* and *committed* is what bites at thread-switch time.

**Visibility.** When you update a memory file, say so out loud ("logged decision X," "refreshed state.md"). The discipline has to be observable.

**If your context gets compacted mid-session:** re-read this `CLAUDE.md`, `01-context/state.md`, and the most recent activity-log entry before continuing. Compaction is a mini session-start.

**The mental model:** `state.md` is the live dashboard. `activity-log.md` is the chronological journal. `decisions-log.md` is the ledger. `insights.md` is the working-memory scratchpad.

## Content Types

This repo has three distinct content layers. Each has a different tone, audience, and writing style. See SKILL.md for full details.

| Directory | Content Type | Primary Audience | Tone |
|-----------|-------------|-----------------|------|
| `docs/modules/`, `docs/builder/`, `docs/theme-options/`, `docs/api/`, `docs/css-reference/` | Reference docs | Humans | Descriptive, thorough |
| `docs/playbooks/` | LLM Playbooks | AI assistants | Imperative, rule-based |
| `docs/internals/` | Architecture docs | Developers + LLMs | Factual, code-heavy |
| `docs/recipes/` | How-to guides | Humans | Step-by-step |
| `docs/troubleshooting/` | Problem/solution | Humans | Diagnostic, direct |

## Scope

**Divi 5 only.** Do not document Divi 4 behavior.

## Common Tasks

### Creating a new documentation page
1. Read SKILL.md for the template
2. Create the .md file in the correct directory
3. Add it to the `nav` section in mkdocs.yml
4. Update the section's index.md status table
5. Create the screenshot directory: `docs/assets/screenshots/{category}/{slug}/`
6. Run `mkdocs build` to verify

### Scraping a new page from Elegant Themes
```bash
python3 scripts/scrape_docs.py --url "URL" --category CATEGORY --screenshots
```
Then restructure the output to match our template.

### Elegant Themes blog tutorials (Divi Resources / Theme Releases)

Long-form **blog** posts are not auto-imported. When a post teaches the same feature as a reference page:

1. Add an **`## Elegant Themes tutorials`** section on that page (see `SKILL.md` for placement and link format).
2. Add a row to **`planning/et-blog-tutorials-map.md`** so weekly maintenance can find it.
3. During the **weekly monitor** run, check new Divi Resources / Theme Releases posts and update the map + links (see `claude-code/task-weekly-monitor.md`).

### Running the content monitor
```bash
python3 scripts/monitor_updates.py --all
```
Check `reports/update-report-YYYY-MM-DD.md` for findings.

### Checking external links (weekly)

```bash
pip install certifi
python3 scripts/check_external_links.py --write-report reports/external-link-check-$(date +%Y-%m-%d).md
```

(`certifi` is optional but recommended on macOS so TLS verification matches CI; it is installed in GitHub Actions with the other monitor dependencies.)

Review the report and **fix or remove** broken `https://` targets in `docs/`. Use `scripts/external_link_allowlist.txt` only for confirmed false positives. See `claude-code/task-weekly-monitor.md` Step 8.

### Building the site locally
```bash
pip install mkdocs-material mkdocs-glightbox
mkdocs serve  # Dev server at http://localhost:8000
mkdocs build  # Build to site/ directory
```

## Rules

1. **Never overwrite manually enriched pages** with scraped content. Check git history first.
2. **Every page must have complete YAML frontmatter** — title, category, tags, divi_version, last_updated.
3. **Settings tables must be comprehensive** — every setting, not just common ones.
4. **Screenshot placeholders use this syntax:**
   ```markdown
   ![Alt text](../assets/screenshots/category/slug/filename.png){ loading=lazy }
   *Caption text.*
   ```
5. **Code examples must have language tags** — \`\`\`php, \`\`\`css, \`\`\`javascript, \`\`\`html
6. **Cross-references use relative paths** — `[Page Title](../category/slug.md)`
7. **Always run `mkdocs build` before committing** to catch broken links and formatting errors.
8. **Commit messages should be descriptive** — include what changed and why.

## Task Files

Detailed task instructions for specific jobs are in `claude-code/`:
- `task-bulk-scrape-modules.md` — Initial bulk scrape of all module docs
- `task-scrape-other-sections.md` — Scrape theme options, builder, API sections
- `task-weekly-monitor.md` — Weekly content monitoring and update cycle
- `task-monthly-audit.md` — Monthly deep content and quality audit
