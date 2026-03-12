# Claude Code Scheduled Task: Weekly Content Monitor & Update

## Schedule

Run this task **every Monday** (or biweekly if preferred).

## Context

You are maintaining the `divi-docs` repo (https://github.com/16wells/divi-docs).
This is a community-maintained Divi 5 documentation site built with MkDocs Material.
Read SKILL.md at the repo root for template and writing standards.

## Task Overview

1. Run the monitoring script to identify what needs attention
2. Act on the findings automatically where possible
3. Generate a summary of what was done and what needs human review

## Step-by-Step Instructions

### Step 1: Pull Latest and Run Monitor

```bash
cd /path/to/divi-docs
git pull origin main

pip install requests beautifulsoup4 markdownify pyyaml

python scripts/monitor_updates.py --all
```

Read the generated report in `reports/update-report-YYYY-MM-DD.md`.

### Step 2: Handle Broken Source URLs

For any `SOURCE_GONE` or `SOURCE_REDIRECTED` findings:
- If redirected: update the `source_url` in the page's frontmatter to the new URL
- If gone (404): remove the `source_url` field and add a note: `<!-- Source URL no longer available as of YYYY-MM-DD -->`
- Commit these fixes

### Step 3: Scrape New Documentation Pages

For any `NEW_PAGE` findings (pages at elegantthemes.com we don't have):
- Run the scraper for each new URL:
  ```bash
  python scripts/scrape_docs.py --url "URL" --category CATEGORY
  ```
- Restructure the output to match our template (see SKILL.md)
- Add proper frontmatter, screenshot placeholders, and TODO markers
- Add the new page to `mkdocs.yml` nav
- Update the relevant section's `index.md`

### Step 4: Check for Divi Release Notes

Search the web for recent Divi 5 release notes and changelog entries:
- Search: "Divi 5 release notes 2026" and "Divi 5 changelog"
- If a new version has been released since our last check:
  - Review the changelog for changed module behavior, new settings, or deprecated features
  - Update affected documentation pages
  - Add version-specific notes where behavior has changed
  - Update `last_updated` dates on modified pages

### Step 5: Search for New Community Resources

Search the web for recent, high-quality Divi 5 content:
- "Divi 5 tutorial 2026"
- "Divi 5 CSS class reference"
- "Divi 5 hooks filters developer"
- "Divi 5 custom module development"

For any substantial new resources found:
- If it's a CSS class list or hook reference → incorporate into our `css-reference/` or `api/` sections
- If it's a tutorial or how-to → create a new recipe in `docs/recipes/`
- If it reveals undocumented behavior → add to `docs/internals/`
- Always credit the source with a link

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

git add .
git commit -m "Weekly update: [brief summary of what changed]

- Scraped X new pages
- Fixed Y broken source URLs
- Updated Z pages for Divi X.Y release
- Filled in N content gaps
- See reports/update-report-YYYY-MM-DD.md for details"
git push
```

### Step 8: Generate Human Summary

After completing all automated steps, write a brief summary to stdout:

```
=== WEEKLY UPDATE COMPLETE ===
Date: YYYY-MM-DD
New pages scraped: X
Source URLs fixed: Y
Pages updated for new release: Z
Content gaps filled: N
Remaining placeholders: M

NEEDS HUMAN REVIEW:
- [list anything that requires judgment calls]
- [e.g., "New Divi 5.2 release changes accordion behavior — verify in production"]
- [e.g., "Community post claims hook X is deprecated — needs verification"]
```

## Important Notes

- Do NOT overwrite pages that have been manually enriched (check git blame — if the last commit was from a human contributor, don't overwrite with scraped content)
- Always run `mkdocs build` before committing to catch broken links or formatting errors
- Keep the reports directory — it serves as an audit trail of what was checked and when
- If a finding seems wrong or ambiguous, leave it for human review rather than making a bad change
- The `reports/` directory should be gitignored for the deployed site but committed to the repo
