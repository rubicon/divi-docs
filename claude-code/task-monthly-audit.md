# Claude Code Scheduled Task: Monthly Deep Content Audit

## Schedule

Run this task on the **first Monday of each month**.

## Context

You are maintaining the `divi-docs` repo (https://github.com/16wells/divi-docs).
Read SKILL.md for template and standards. This is a deeper audit than the weekly check.

## Task Overview

Once a month, do a comprehensive quality and completeness audit of the entire documentation site.
This catches things the weekly monitor doesn't: stale content, missing cross-references,
inconsistent formatting, and opportunities to improve high-traffic pages.

## Step-by-Step Instructions

### Step 1: Content Completeness Audit

Scan every page in the docs directory and categorize:

```
COMPLETE    — Has Overview, Settings tables, Code Examples, Patterns, Troubleshooting
DRAFT       — Has content but missing 2+ major sections
PLACEHOLDER — Stub page with no real content
MISSING     — Known Divi 5 feature with no page at all
```

Generate a completeness scorecard:
```
=== CONTENT COMPLETENESS ===
Modules:       X/Y complete (Z%)
Theme Options: X/Y complete (Z%)
Builder:       X/Y complete (Z%)
API:           X/Y complete (Z%)
CSS Reference: X/Y complete (Z%)
Playbooks:     X/Y complete (Z%)
Internals:     X/Y complete (Z%)
Recipes:       X/Y complete (Z%)
Troubleshooting: X/Y complete (Z%)
```

### Step 2: Cross-Reference Audit

Check that:
- Every page's `related` frontmatter field points to pages that actually exist
- Every page's Related section at the bottom has working links
- Related pages link back to each other (bidirectional)
- Module pages reference relevant CSS Reference and API pages where applicable

Fix broken or missing cross-references.

### Step 3: Formatting Consistency Check

Verify every non-placeholder page follows the template:
- Has proper YAML frontmatter with all required fields
- Uses the correct heading hierarchy (# for title, ## for sections, ### for subsections)
- Settings tables use the correct column format (Setting | Type | Default | Description)
- Code blocks have language tags
- Screenshots use `{ loading=lazy }` syntax
- Admonitions use MkDocs `!!!` syntax
- Version notes use the standard "Divi 5 Only" admonition

Fix inconsistencies.

### Step 4: Stale Content Check

For pages with a `last_updated` date older than 90 days:
- Re-scrape the source URL (if available) and diff against our content
- If the source has changed materially, flag for update
- If the source is unchanged, bump the `last_updated` date to confirm freshness
- For playbooks and internals (no source URL), flag pages older than 90 days for human review

### Step 5: Screenshot Inventory

Count how many pages reference screenshots vs how many actual screenshot files exist:
```
Pages referencing screenshots: X
Screenshot files present: Y
Missing screenshots: Z (list them)
```

### Step 6: Search Engine Health Check

Verify the generated site has:
- A working sitemap.xml
- Proper page titles and meta descriptions (from frontmatter)
- No orphan pages (pages not in the nav)
- No broken internal links

Run `mkdocs build --strict` to catch warnings.

### Step 7: Playbook Freshness Check

For each playbook, search the web for:
- New Divi 5 behaviors that contradict our documented rules
- New community discoveries about Divi 5 internals
- Changes to the Visual Builder UI that would affect our operations guides

Flag anything that needs updating.

### Step 8: Generate Monthly Report

Write a comprehensive report to `reports/monthly-audit-YYYY-MM.md`:

```markdown
# Monthly Content Audit — YYYY-MM

## Completeness Scorecard
[table]

## Actions Taken
- Fixed X cross-references
- Updated Y formatting issues
- Re-verified Z pages against source
- Flagged N pages for human review

## Stale Content (needs human attention)
- [list]

## Missing Screenshots
- [list]

## Playbook Updates Needed
- [list]

## Recommendations
- [prioritized list of what to work on next month]
```

### Step 9: Commit and Push

```bash
git add .
git commit -m "Monthly audit: [month] [year]

- Completeness: X% overall
- Fixed Y cross-references, Z formatting issues
- Flagged N pages for human review
- See reports/monthly-audit-YYYY-MM.md for full details"
git push
```
