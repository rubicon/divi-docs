# Claude Code Task: Bulk Scrape & Generate Module Documentation

## Context

You are working on the `divi-docs` repo (https://github.com/16wells/divi-docs).
This is a MkDocs Material site that provides Divi 5 technical documentation.
Read SKILL.md at the repo root for the complete template, frontmatter schema, and writing standards.

## Task

Scrape the Elegant Themes documentation site for every Divi 5 module and generate
structured Markdown documentation pages in our format. Then commit and push the results.

## Step-by-Step Instructions

### 1. Install Dependencies

```bash
pip install requests beautifulsoup4 markdownify pyyaml
```

### 2. Discover All Module URLs

Fetch the Divi module documentation index page and extract all individual module URLs:

```
https://www.elegantthemes.com/documentation/divi/modules/
```

Also check these category pages for additional modules:
```
https://www.elegantthemes.com/documentation/divi/fullwidth-modules/
https://www.elegantthemes.com/documentation/divi/
```

Build a complete list of module URLs. The known modules include (but may not be limited to):

**Content Modules:**
- Accordion, Audio, Bar Counter, Blog, Blurb, Button, Call to Action,
  Circle Counter, Code, Comments, Contact Form, Countdown Timer,
  Divider, Email Optin, Filterable Portfolio, Gallery, Icon,
  Image, Login, Map, Menu, Number Counter, Person, Portfolio,
  Post Navigation, Post Slider, Post Title, Pricing Table,
  Search, Sidebar, Slider, Social Media Follow, Tabs, Testimonial,
  Text, Toggle, Video, Video Slider, Woo Modules

**Fullwidth Modules:**
- Fullwidth Code, Fullwidth Header, Fullwidth Image, Fullwidth Map,
  Fullwidth Menu, Fullwidth Portfolio, Fullwidth Post Slider,
  Fullwidth Post Title, Fullwidth Slider

### 3. For Each Module, Generate a Doc Page

For each module URL:

a. Fetch the page content
b. Extract the title, description, and any settings information
c. Restructure into our doc template (see SKILL.md for the exact format)
d. Generate the file at `docs/modules/{slug}.md`

**Every page MUST include:**

- Complete YAML frontmatter:
  ```yaml
  ---
  title: "Module Name"
  category: modules
  tags: [relevant, tags]
  related: [related-module-slugs]
  divi_version: "5.x"
  last_updated: 2026-03-12
  source_url: "https://www.elegantthemes.com/documentation/divi/MODULE/"
  ---
  ```

- Overview section (2-3 paragraphs based on scraped content)

- Settings tables for Content, Design, and Advanced tabs. Document every setting with:
  | Setting | Type | Default | Description |
  Use these types: text, toggle, select, range, color, upload, icon-picker, rich-text, url, number, code, multi-select
  Mark uncertain settings with `<!-- TODO: Verify setting name/type/default -->`

- Screenshot placeholders:
  ```markdown
  ![Overview](../assets/screenshots/modules/{slug}/overview.png){ loading=lazy }
  ![Content tab](../assets/screenshots/modules/{slug}/settings-content.png){ loading=lazy }
  ![Design tab](../assets/screenshots/modules/{slug}/settings-design.png){ loading=lazy }
  ```

- CSS code examples for common customizations of that module

- PHP hook/filter examples where known (use `et_module_shortcode_output` filter pattern)

- 2-3 common usage patterns

- Version Notes:
  ```markdown
  !!! note "Divi 5 Only"
      This page documents Divi 5 behavior exclusively.
  ```

- Troubleshooting section with at least one known issue

- Related module cross-references

### 4. Update docs/modules/index.md

Update the modules index page with a complete table of all modules, marking newly created ones as ✅.

### 5. Update mkdocs.yml

Add every new module page to the `nav` section under `Modules`.

### 6. Create Screenshot Directories

```bash
for slug in $(ls docs/modules/*.md | xargs -I{} basename {} .md | grep -v index); do
  mkdir -p docs/assets/screenshots/modules/$slug
  touch docs/assets/screenshots/modules/$slug/.gitkeep
done
```

### 7. Build and Verify

```bash
pip install mkdocs-material mkdocs-glightbox
mkdocs build
```

Fix any build errors before committing.

### 8. Commit and Push

```bash
git add .
git commit -m "Add scraped documentation for all Divi 5 modules

- Generated doc pages for X modules from elegantthemes.com
- Updated modules index with status tracking
- Updated mkdocs.yml navigation
- Created screenshot placeholder directories
- All pages include TODO markers for settings needing verification"
git push
```

## Important Notes

- SKIP modules that already have real content (blurb.md, text.md, blog.md) — don't overwrite them
- Divi 5 ONLY — do not include any Divi 4 specific content
- If the scraper can't extract meaningful settings info, still create the page with the correct structure and mark settings sections with `<!-- TODO: Settings need manual documentation -->`
- Be thorough on settings tables — these are the most valuable part for users
- Cross-reference related modules in the `related` frontmatter field AND the Related section at the bottom
