---
title: "Contributing to Divi 5 Technical Documentation"
description: "Contributing guide for Divi 5 technical documentation — how to submit edits, create new pages, report issues, and follow documentation standards."
category: meta
tags: [contributing, community]
last_updated: 2026-04-21
---

# Contributing to Divi 5 Technical Documentation

This is a community-maintained documentation project for the Divi WordPress Theme. We welcome contributions from anyone — whether you're fixing a typo, adding a missing setting, or writing an entirely new page.

!!! abstract "Quick Reference"
    **Quick edits:** Click the pencil icon on any page to propose changes directly on GitHub — no git knowledge needed.
    **New pages:** Fork the repo, copy `templates/doc-template.md`, fill in the template, submit a pull request.
    **Key rules:** Complete YAML frontmatter required, Divi 5 only, code examples must have language tags, test before submitting.

## How to Contribute

### Quick Edits (no git required)

Every page on this site has an **edit icon** (pencil) in the top right. Click it and you'll be taken to the file on GitHub where you can propose changes directly in your browser. GitHub will walk you through creating a pull request — no git knowledge needed.

### New Pages

1. Fork this repository on GitHub
2. Copy `templates/doc-template.md` to the appropriate folder under `docs/`
3. Fill in the template — follow the existing pages as examples
4. Submit a pull request

### Reporting Issues

If you spot an error but don't have time to fix it yourself, [open an issue](https://github.com/16wells/divi-docs/issues/new/choose) using one of our templates.

## Documentation Standards

### Frontmatter

Every page must include YAML frontmatter at the top:

```yaml
---
title: "Human-Readable Page Title"
category: modules
tags: [relevant, tags, here]
related: [other-page-slug]
divi_version: "5.x"
last_updated: 2026-03-12
---
```

### Writing Style

- **Be specific.** Document actual behavior, not marketing language.
- **Show, don't just tell.** Include code examples, screenshots, or settings tables.
- **Document Divi 5 behavior. Divi 4 is out of scope.
- **Write for practitioners.** Assume the reader knows WordPress basics but may be learning Divi.
- **Keep it scannable.** Use headings, tables, and admonitions to break up long sections.

### Code Examples

- Always use fenced code blocks with language tags (` ```php `, ` ```css `, ` ```html `)
- Test your code before submitting — examples should actually work
- Include comments explaining non-obvious behavior
- Show both the minimal example and a real-world usage

### Admonitions

Use MkDocs admonition syntax for callouts:

```markdown
!!! note "Title"
    Content here.

!!! warning "Common Pitfall"
    Content here.

!!! tip "Pro Tip"
    Content here.
```

### File Naming

- Use lowercase with hyphens: `visual-builder.md`, not `Visual Builder.md`
- Match the slug to the feature name as closely as possible
- Place files in the correct category folder

## Content Categories

| Category | What goes here |
|----------|---------------|
| `modules/` | Individual Divi module documentation (Blurb, Text, Blog, etc.) |
| `theme-options/` | Divi Theme Options panel settings |
| `builder/` | Visual Builder and Theme Builder features |
| `api/` | Hooks, filters, custom module development |
| `css-reference/` | CSS class names, selectors, common overrides |
| `recipes/` | Step-by-step "how to build X" walkthroughs |
| `troubleshooting/` | Common issues and their solutions |

## Elegant Themes blog tutorials

Official **Divi Resources** and **Theme Releases** articles on elegantthemes.com are great walkthroughs, but they are not the same as Help Center reference material.

When you add or update a page for a feature that has a matching blog post:

1. Add an **`## Elegant Themes tutorials`** section on the **reference page** for that feature (not a duplicate full article). Use bullet links with `{:target="_blank"}` and one line of context each. See **`SKILL.md`** for the exact heading and placement (before `## Version Notes`, or before `## Related` if there is no Version Notes section).
2. Add the URL to **`planning/et-blog-tutorials-map.md`** so maintainers can keep links in sync during regular updates.

### External links

`python3 scripts/check_external_links.py` (see `CLAUDE.md`) probes `https://` targets referenced from `docs/`. Install **`certifi`** first on macOS if you see TLS verify errors. When the report shows failures, **update or remove** those links in the cited files, or add a reviewed substring to `scripts/external_link_allowlist.txt` for false positives.

## Review Process

All contributions go through pull request review before being published. We check for:

- Accuracy (does it match actual Divi behavior?)
- Completeness (are settings and options documented?)
- Formatting (does it follow the template?)
- Code quality (do examples actually work?)

Most PRs are reviewed within a few days. If you're working on something large, consider opening an issue first to discuss the approach.

## Code of Conduct

Be helpful, be respectful, be accurate. This project exists to make Divi better for everyone. We don't tolerate harassment, spam, or deliberately incorrect information.

## License

Contributions are licensed under [MIT](https://opensource.org/licenses/MIT). By submitting a pull request, you agree to license your contribution under the same terms.
