# Claude Code Task: Scrape Theme Options, Builder & Other Sections

## Context

You are working on the `divi-docs` repo (https://github.com/16wells/divi-docs).
Read SKILL.md at the repo root for template and writing standards.
The modules section has already been populated. Now populate the remaining reference sections.

## Task

Scrape and generate documentation for the Theme Options, Builder, and CSS Reference sections.

## Source URLs

### Theme Options
Scrape these and generate pages in `docs/theme-options/`:
```
https://www.elegantthemes.com/documentation/divi/theme-options/
https://www.elegantthemes.com/documentation/divi/general-settings/
https://www.elegantthemes.com/documentation/divi/navigation-settings/
https://www.elegantthemes.com/documentation/divi/layout-settings/
https://www.elegantthemes.com/documentation/divi/ads/
https://www.elegantthemes.com/documentation/divi/seo/
https://www.elegantthemes.com/documentation/divi/integration/
https://www.elegantthemes.com/documentation/divi/updates/
```

### Builder
Scrape these and generate pages in `docs/builder/`:
```
https://www.elegantthemes.com/documentation/divi/visual-builder/
https://www.elegantthemes.com/documentation/divi/theme-builder/
https://www.elegantthemes.com/documentation/divi/divi-builder/
https://www.elegantthemes.com/documentation/divi/library/
https://www.elegantthemes.com/documentation/divi/global-elements/
https://www.elegantthemes.com/documentation/divi/presets/
```

### API / Developer Docs
Check the Elegant Themes developer documentation:
```
https://www.elegantthemes.com/documentation/developers/
https://www.elegantthemes.com/documentation/divi/divi-module-api/
```

### Also Search For
Use web search to find additional Divi 5 documentation resources beyond elegantthemes.com:
- Divi 5 CSS class reference or cheat sheets
- Divi 5 hook/filter lists
- Divi 5 developer blog posts from Elegant Themes

## Output Format

Follow SKILL.md exactly. Each section type has its own tone:
- Theme Options → descriptive, every setting documented
- Builder → descriptive, workflow-focused
- API → technical, code-heavy
- CSS Reference → precise, selector-focused

## After Generating

1. Update each section's `index.md` with ✅ status markers
2. Update `mkdocs.yml` nav with new pages
3. Create screenshot directories
4. Build with `mkdocs build` to verify
5. Commit with descriptive message and push
