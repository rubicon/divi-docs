# Divi 5 Filterable Gallery Plugin — Project Handoff

> Paste this at the start of your first conversation in the divi-docs project. It bootstraps a fresh Claude with everything needed to continue building.

---

## Project context

Building a generic WordPress plugin — **Filterable Gallery for Divi 5** — that adds Media Library category tagging and filter buttons to the standard Divi 5 Gallery module. Originated as a Palm Valley Barn need but built generic from day one to publish as a Recipe on 16wells/divi-docs (https://16wells.github.io/divi-docs/) as an Easter egg.

**Final destination:** Recipe page at `https://16wells.github.io/divi-docs/recipes/divi5-filterable-gallery/`, written in the existing recipe format (Quick Reference admonition, Overview, Use Cases, code with file labels, troubleshooting).

---

## Locked decisions (do not revisit)

| Item | Value |
|---|---|
| Plugin slug | `divi5-filterable-gallery` |
| Display name | "Filterable Gallery for Divi 5" |
| Function/option prefix | `dfg_` |
| CSS class prefix | `dfg-` |
| Shortcode | `[dfg_gallery_filters]` |
| Taxonomy slug | `gallery_category` |
| Default active button color | `#2271b1` (WP admin blue), overridable via `--dfg-active-bg` |
| Distribution | Free with email capture |
| Architecture | 3 layers: taxonomy → output filter → frontend UI |
| Build target | Generic plugin (no PVB-specific content) |

---

## Three-chunk delivery plan

- **Chunk 1: Foundation** — main plugin file, taxonomy, output filter, shortcode, frontend JS/CSS, uninstall.php ✅ **COMPLETE (v1.0.2)**
- **Chunk 2: Admin settings page** — CodeMirror CSS editor + class reference panel ← **NEXT**
- **Chunk 3: Live preview pane + Danger Zone reset feature**

---

## Chunk 1 — Complete (v1.0.2)

**Files in current distribution:**
- `divi5-filterable-gallery.php` (main plugin, v1.0.2)
- `assets/filter.js` (vanilla JS, no jQuery)
- `assets/filter.css`
- `uninstall.php` (intentionally empty — data preserved unless user uses Chunk 3 Danger Zone reset)
- `readme.txt`
- `INSTALL.md`

**Bugs fixed in v1.0.2 (vs original v1.0.1):**

1. **Output filter class matching.** Divi 5 renders BOTH `et_pb_gallery_item` (outer wrapper, has `style="display: block;"` — this is the togglable element) AND `et_pb_gallery_image` (inner wrapper, has layout class like `landscape`). Original code only matched the outer; v1.0.2 matches either via XPath `or`.

2. **Term counts on attachment taxonomy.** Default `_update_post_term_count` only counts `publish` posts but attachments are `inherit`. Fixed by adding `'update_count_callback' => '_update_generic_term_count'` to `register_taxonomy()` args.

**Known-but-deferred Chunk 1 issues to address in Chunk 2 or later:**

- **Duplicate dead code.** Lines 117–232 define `dfg_attachment_fields_to_edit` and `dfg_attachment_fields_to_save`. Lines 258–353 define `dfg_render_modal_checkboxes` and `dfg_save_modal_categories`. Both pairs hook the same filters at priority 10. Second pair wins; first pair is dead. Delete the first pair when convenient.
- **Bullet markers from theme `<ul>` styles.** Need to fold this into plugin CSS with stronger specificity (currently patched in user's Customizer):
  ```css
  .dfg-gallery-filters ul.clearfix,
  .dfg-gallery-filters ul.clearfix li {
      list-style: none !important;
      padding-left: 0 !important;
      margin-left: 0 !important;
  }
  .dfg-gallery-filters ul.clearfix li::before,
  .dfg-gallery-filters ul.clearfix li::marker {
      content: none !important;
      display: none !important;
  }
  ```
- **Pagination conflict.** Frontend JS only filters items currently in the DOM. Galleries with `data-per_page` set will misbehave when filtering — corporate images on page 2 won't appear when "corporate" is clicked from page 1. Options for resolution: (a) AJAX-load all pages on filter, (b) detect pagination at render time and warn, (c) intercept Divi's pagination AJAX and merge results. Document for users in readme until solved.

**Divi 5 technical anchors (confirmed in production):**
- Block render_slug: `et_pb_gallery`, block name: `divi/gallery`
- Outer wrapper: `<div class="et_pb_gallery_item et_pb_grid_item et_pb_gallery_item_0_X first_in_row" style="display: block;">`
- Inner wrapper: `<div class="et_pb_gallery_image landscape" data-per_page="X">`
- Image: `<img class="wp-image-{ID}" ...>`
- Hooks used: `render_block` (Divi 5 block path) + `et_module_shortcode_output` (Divi 4 fallback)
- Filterable Portfolio convention: `.et_pb_portfolio_filters > ul > li > a.active` — the plugin mirrors this for visual consistency

**Confirmed-working frontend behavior:**
- Buttons render, sorted by image count descending, with "All" reset always first
- Active state via `li.dfg-filter.active`
- URL parameter `?filter=slug` pre-filters on load
- Vanilla JS, no jQuery
- Mobile: filters scroll horizontally
- Accessibility: ARIA roles, keyboard nav, reduced-motion respected

---

## Chunk 2 scope (build next)

Admin settings page at **Media → Filterable Gallery**:

- **Two-pane layout:** CodeMirror CSS editor (left) + class reference panel with click-to-copy selectors (right)
- **CSS injection:** Custom CSS output in `<head>` AFTER plugin's default styles → user rules win cascade naturally, no `!important` battles
- **Save protection:** Dirty-state indicator + `beforeunload` warning if user navigates away unsaved
- **CodeMirror source:** WP core's bundled CodeMirror via `wp_enqueue_code_editor( array( 'type' => 'text/css' ) )` — no external dependency, no extra HTTP request, same path WP Customizer Additional CSS uses
- **Class reference panel:** Lists every `.dfg-*` selector the plugin renders, with description and click-to-copy. Probably 6–10 selectors total.
- **Activation seed:** Default CSS option pre-populated with the bullet-fix block above (so the bullet issue is fixed out of the box for new installs)

**New files:**
- `admin/settings-page.php`
- `assets/admin.css`

**Main plugin file additions** (~3 small blocks):
- `add_action( 'admin_menu', ... )` to register the settings page
- `register_setting()` + sanitization callback for the CSS option
- `wp_head` action that prints the user CSS in a `<style>` tag

---

## Chunk 3 scope (final)

- **Live preview pane** in the settings page — renders a sample gallery + filter UI inline so user sees CSS changes update without leaving the page
- **Danger Zone reset feature** — three-friction-point destructive flow:
  1. Click red "Reset All Plugin Data" button
  2. Modal explains what gets deleted (taxonomy terms, image taggings, custom CSS, all settings)
  3. User must type `RESET` to confirm
  4. Final destructive-styled red button executes
- `uninstall.php` stays intentionally empty (deletion via WP admin Plugins page remains safe by design — full reset requires explicit Danger Zone use first)

---

## Recipe document (parallel deliverable)

Once the plugin code is final, write a Recipe page in the docs site format and PR it to `16wells/divi-docs` under `/recipes/divi5-filterable-gallery/`. Existing recipe format reference: any current page in `/recipes/` on the site.

Recipe sections to include:
1. Quick Reference admonition (the `!!! info` block)
2. Overview / what it does
3. Use cases
4. Installation
5. Tagging images (Media Library walkthrough)
6. Adding the filter shortcode
7. Customizing the styles
8. Troubleshooting (cover the two bugs we hit + the pagination caveat)
9. Architecture notes (the 3-layer breakdown)

---

## How to start

In the next conversation in the divi-docs project, paste this whole document at the top of your first message, then say something like: "Continuing from this handoff. I've got the v1.0.2 plugin files locally — ready to build Chunk 2."
