# Claude Code Scheduled Task: Weekly Content Monitor & Update

## Schedule

Run this task **every Monday** (or biweekly if preferred).

## Context

You are maintaining the `divi-docs` repo (https://github.com/16wells/divi-docs).
This is a community-maintained Divi 5 documentation site built with MkDocs Material.
Read SKILL.md at the repo root for template and writing standards.

The content monitor scrapes `help.elegantthemes.com` and compares upstream content against our local documentation. It uses content hashing (stored in `scripts/et_content_hashes.json`) to detect real changes vs. timestamp noise, so only genuine content updates trigger findings.

## CLI Modes

The monitor script supports three operating modes:

| Flag | Behavior |
|------|----------|
| `--dry-run` | Scans upstream, generates report, changes nothing on disk |
| `--auto-update` | Automatically updates settings tables in existing pages |
| `--auto-create` | Creates stub pages for new ET articles not yet in our docs |

**Safety rails:** The monitor never deletes content. `--auto-update` only modifies settings tables and adds `<!-- REVIEW: auto-updated YYYY-MM-DD -->` markers. `--auto-create` generates minimal stubs with TODO markers that require manual enrichment.

## Task Overview

1. Run the monitoring script to identify what needs attention
2. Review findings and act on them (manually or via auto-update)
3. Verify the build passes
4. Generate a summary of what was done and what needs human review

## Step-by-Step Instructions

### Step 1: Pull Latest and Run Monitor

```bash
cd /path/to/divi-docs
git pull origin main

pip install requests beautifulsoup4 markdownify pyyaml mkdocs-material mkdocs-glightbox

# Start with dry-run to see what changed upstream
python scripts/monitor_updates.py --all --dry-run
```

Read the generated report in `reports/update-report-YYYY-MM-DD.md`. The report will show:
- `CONTENT_CHANGED` — upstream content hash differs from last scan
- `NEW_PAGE` — ET article exists with no matching local page
- `SOURCE_GONE` — source URL returns 404
- `SOURCE_REDIRECTED` — source URL redirects to a new location
- `PLACEHOLDER` — local page is still a stub
- `MANY_TODOS` — local page has unresolved TODO markers

### Step 2: Apply Auto-Updates (if appropriate)

If the dry-run report shows `CONTENT_CHANGED` findings with settings table differences:

```bash
# Auto-update settings tables in existing pages
python scripts/monitor_updates.py --all --auto-update
```

Review the changes with `git diff` to verify the auto-updates are correct. The script only touches settings tables and adds review markers — it will not overwrite manually written prose, code examples, or recipes.

### Step 3: Handle New Pages

For any `NEW_PAGE` findings, you can either create stubs automatically or manually:

```bash
# Auto-create stubs for new ET articles
python scripts/monitor_updates.py --all --auto-create
```

Each stub will be added to `mkdocs.yml` and the relevant section index. Review stubs and enrich them:
- Add real settings tables (verify against a live Divi 5 install if possible)
- Add CSS customization examples
- Add common usage patterns
- Replace TODO markers with actual content

### Step 4: Handle Broken Source URLs

For any `SOURCE_GONE` or `SOURCE_REDIRECTED` findings:
- If redirected: update the `source_url` in the page's frontmatter to the new URL
- If gone (404): remove the `source_url` field and add a note: `<!-- Source URL no longer available as of YYYY-MM-DD -->`

### Step 5: Check for Divi Release Notes

Search the web for recent Divi 5 release notes and changelog entries:
- Search: "Divi 5 release notes 2026" and "Divi 5 changelog"
- If a new version has been released since our last check:
  - Review the changelog for changed module behavior, new settings, or deprecated features
  - Update affected documentation pages
  - Add version-specific notes where behavior has changed
  - Update `last_updated` dates on modified pages

### Step 6: Fill Content Gaps (if time allows)

From the `PLACEHOLDER` and `MANY_TODOS` findings, pick the 2-3 highest-impact pages
(prioritize modules with the most search volume — Image, Contact Form, Slider, CTA)
and flesh them out:
- Add real settings tables (verify against a live Divi 5 install if possible)
- Add CSS customization examples
- Add common usage patterns
- Remove TODO markers as you fill in content

### Step 7: Build, Commit, Push

```bash
mkdocs build  # Verify no errors

git add docs/ reports/ scripts/et_content_hashes.json mkdocs.yml
git commit -m "Weekly update: [brief summary of what changed]

- Auto-updated X settings tables
- Created Y new stub pages
- Fixed Z broken source URLs
- Filled in N content gaps
- See reports/update-report-YYYY-MM-DD.md for details"
git push
```

### Step 8: Generate Human Summary

After completing all automated steps, write a brief summary to stdout:

```
=== WEEKLY UPDATE COMPLETE ===
Date: YYYY-MM-DD
Settings tables auto-updated: X
New stub pages created: Y
Source URLs fixed: Z
Content gaps filled: N
Remaining placeholders: M

NEEDS HUMAN REVIEW:
- [list any pages with <!-- REVIEW: auto-updated --> markers]
- [list any new stubs that need enrichment]
- [e.g., "New Divi 5.2 release changes accordion behavior — verify in production"]
- [e.g., "Community post claims hook X is deprecated — needs verification"]
```

## GitHub Actions Integration

The workflows automate the two tiers of monitoring:

- **Weekly (`weekly-monitor.yml`):** Runs `--dry-run` by default. Generates a report and commits it, but makes no changes to documentation pages. This is the safe, observe-only mode.
- **Monthly (`monthly-audit.yml`):** Runs `--auto-update --auto-create` on the first Monday of each month. This is the aggressive mode that modifies docs, creates stubs, and commits everything. A build verification step runs afterward to catch any issues.

To switch the weekly workflow to auto-update mode once you are confident in the system, change `--dry-run` to `--auto-update` in `.github/workflows/weekly-monitor.yml`.

## Important Notes

- The monitor scrapes `help.elegantthemes.com` — this is the current Elegant Themes documentation site
- Content hashing (`scripts/et_content_hashes.json`) tracks what we last saw upstream, filtering out timestamp-only changes
- Do NOT overwrite pages that have been manually enriched (check git blame — if the last commit was from a human contributor, review auto-updates carefully before accepting)
- Always run `mkdocs build` before committing to catch broken links or formatting errors
- Keep the reports directory — it serves as an audit trail of what was checked and when
- If a finding seems wrong or ambiguous, leave it for human review rather than making a bad change
- The `reports/` directory should be gitignored for the deployed site but committed to the repo
