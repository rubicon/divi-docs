# Walkthrough: Test Divi Variables From Style Guide skill + import to 16wells.dev

Use this to verify the **Divi Variables From Style Guide** Claude skill and import Global Variables into the example Divi docs site at **16wells.dev**.

## Prerequisites

- Skill installed and enabled (Claude.ai: Settings → Capabilities/Skills, or Claude Code skills directory).
- Access to 16wells.dev with Divi 5 and Visual Builder.
- Test assets in this repo: `docs/assets/imports/`

---

## Part 1 — Test the skill

### 1.1 Where to run the skill

- **Claude.ai:** Ensure the skill is uploaded and enabled in Settings → Capabilities/Skills.
- **Cursor / Claude Code:** Ensure the skill folder is in your Claude Code skills directory (see [claude-skills/README.md](../claude-skills/README.md)).

### 1.2 Provide inputs

Open a conversation and ask the skill to generate a Divi Global Variables import. For example:

**Prompt (option A — token table):**

> Use the Divi Variables From Style Guide skill. Brand name: **16wells-dev**. Convert these design tokens into a Divi 5 Global Variables import file:
>
> [Paste the token table from `docs/assets/imports/16wells-dev-style-guide-test.md`]

**Prompt (option B — prose):**

> Use the Divi Variables From Style Guide skill. Brand name: **16wells-dev**. Convert this style guide into a Divi 5 Global Variables import:
>
> Brand Primary: #2176ff. Brand Dark: #1a2332. Body text: #374151. Font: Inter. H1: 48px, body: 16px. Spacing: 16px, 32px. Radius: 4px. Max width: 1200px. Site URL: https://16wells.dev

### 1.3 What you should get

The skill should output:

1. **Filename suggestion** — e.g. `16wells-dev_Global-Variables.json`
2. **Full JSON** — valid `context: "et_builder"` with `global_colors` and `global_variables`
3. **Token report table** — token name, Divi ID, type, value, label
4. **Missing/ambiguous checklist** — anything it could not derive (should be empty if you used the token table)

### 1.4 Compare with repo file (optional)

A pre-built import file is in the repo so you can import even without running the skill:

- **File:** `docs/assets/imports/16wells-dev_Global-Variables.json`
- Same tokens as the test style guide; stable IDs (`gcid-*`, `gvid-*`).

If you ran the skill, compare its JSON structure and IDs to this file. Small differences in labels or `lastUpdated` are fine; the important part is valid `global_colors` tuples and `global_variables` objects with correct `type` and `groupKey`.

---

## Part 2 — Import into 16wells.dev

### 2.1 Get the JSON file

- **If you used the skill:** Save the JSON from the skill output as `16wells-dev_Global-Variables.json` (or the suggested name).
- **If you’re skipping the skill test:** Use `docs/assets/imports/16wells-dev_Global-Variables.json` from this repo.

### 2.2 Open Divi Library import on 16wells.dev

1. Log in to **16wells.dev** (WordPress admin).
2. Open any page and launch the **Visual Builder** (or use a front-end page and “Enable Visual Builder”).
3. In the builder toolbar, open the **Divi Library** (three-dots menu or Library icon).
4. Go to **Import & Export** (or the import tab).

### 2.3 Import Global Variables only

1. Click **Import** / **Choose File** and select your `*_Global-Variables.json` file.
2. In the import options, **enable** “Import Global Variables” (or equivalent).
3. **Disable** importing layouts, presets, or Theme Builder if you only want variables for this test.
4. Run the import.

### 2.4 Verify

1. In the Visual Builder, open the **Variable Manager** (toolbar).
2. Check **Colors**: you should see “Brand · Primary”, “Brand · Dark”, “Neutral · Text” (or the labels from your file).
3. Check **Fonts**: “Font · Heading · Family” and “Font · Body · Family” = Inter.
4. Check **Numbers**: type scale (H1, body), space (16px, 32px), radius (4px), container max (1200px).
5. Check **Links**: “Link · Site” = https://16wells.dev.

If any variable is missing or wrong, re-check the JSON and that you imported with “Import Global Variables” enabled. If the host blocks `.json` uploads, see [Upload SVG and JSON Files](../docs/troubleshooting/upload-svg-json.md).

### 2.5 Optional: use variables on the page

- Edit a heading or text module → typography → font family → open the variable picker and choose the global “Font · Heading · Family” or “Font · Body · Family”.
- Edit a section or row background color → choose “Brand · Primary” or “Brand · Dark” from global colors.

---

## Troubleshooting

| Issue | What to do |
|-------|------------|
| Skill not found / doesn’t run | Confirm it’s installed and enabled (Claude.ai or Code). Use the exact phrasing “Divi Variables From Style Guide” or “convert this style guide into Divi 5 variables”. |
| Import says “invalid file” | Ensure the JSON is a single object with `"context": "et_builder"` and arrays for `global_colors` and `global_variables`. Validate at jsonlint.com if needed. |
| Upload blocked (security/host) | See [Upload SVG and JSON Files](../docs/troubleshooting/upload-svg-json.md). |
| Fonts don’t look like Inter | Variables store font names only. Ensure Inter is available (e.g. Google Fonts, Divi typography settings, or theme). |
| Duplicate or conflicting variables | Re-importing the same file with stable IDs should update in place. If you had an older import with different IDs, you may see duplicates; remove or archive the old ones in the Variable Manager. |

---

## Summary

1. **Test skill:** Paste the token table or prose from `docs/assets/imports/16wells-dev-style-guide-test.md` into Claude with the skill enabled → get JSON + report.
2. **Import:** In 16wells.dev, Divi Library → Import & Export → choose `*_Global-Variables.json` → enable “Import Global Variables” → import.
3. **Verify:** Variable Manager → check colors, fonts, numbers, links.

Related: [Import a Design System](../docs/recipes/import-design-systems.md), [Style Guide → Divi Variables design](../docs/internals/style-guide-to-divi-variables-design.md), [divi-styleguide-variables skill](https://github.com/16wells/divi-styleguide-variables).
