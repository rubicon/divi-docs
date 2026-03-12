---
title: "Contributing to Divi 5 Technical Documentation"
category: meta
tags: [contributing, community]
last_updated: 2026-03-12
---

# Contributing to Divi 5 Technical Documentation

This is a community-maintained documentation project for the Divi WordPress Theme. We welcome contributions from anyone — whether you're fixing a typo, adding a missing setting, or writing an entirely new page.

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
