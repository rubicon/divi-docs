# Divi 5 Technical Documentation

Community-maintained technical documentation for [Divi 5](https://www.elegantthemes.com/gallery/divi/) by Elegant Themes.

**📖 Read the docs: [16wells.github.io/divi-docs](https://16wells.github.io/divi-docs/)**

## Why This Exists

Divi powers over 800,000 websites, but its official documentation has significant gaps — especially for Divi 5. This project provides accurate, thorough, screenshot-rich technical documentation covering modules, theme options, the builder, API hooks/filters, CSS references, and practical how-to recipes.

## Scope

This project documents **Divi 5 only**. Divi 4 is being phased out and is not covered here.

## Content Pipeline

Documentation is built from two sources:

1. **Scraped content** from elegantthemes.com and other Divi resources, processed into structured Markdown drafts
2. **Community contributions** that enrich, verify, and expand those drafts with tested code examples, screenshots, and troubleshooting tips

### Scraping & Screenshots

```bash
# Install tools
pip install -r requirements.txt
playwright install chromium

# Scrape a documentation page into a Markdown draft
python3 scripts/scrape_docs.py --url "https://www.elegantthemes.com/documentation/divi/blurb/" --category modules --screenshots

# Capture screenshots from a live Divi site
python3 scripts/capture_screenshots.py --url "https://your-site.com/page" --output docs/assets/screenshots/modules/blurb/

# Batch capture from config
python3 scripts/capture_screenshots.py --batch scripts/screenshots.yml
```

## Contributing

We welcome contributions from the entire Divi community. Every page has an edit button, or you can fork the repo and submit a pull request. See the [Contributing Guide](https://16wells.github.io/divi-docs/contributing/) for details.

## Local Development

```bash
pip install mkdocs-material mkdocs-glightbox
mkdocs serve
```

Then open [http://localhost:8000](http://localhost:8000).

## Tech Stack

- [MkDocs](https://www.mkdocs.org/) with [Material theme](https://squidfunk.github.io/mkdocs-material/)
- [Playwright](https://playwright.dev/python/) for automated screenshot capture
- Hosted on GitHub Pages, auto-deployed via GitHub Actions

## License

MIT — see [LICENSE](LICENSE).

## Disclaimer

This is an independent community project. It is not affiliated with, endorsed by, or connected to Elegant Themes or Divi in any official capacity.
