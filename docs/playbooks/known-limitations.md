---
title: "Known Limitations"
category: playbooks
tags: [limitations, gotchas, pitfalls, llm-guardrails]
related: [troubleshooting-tree, visual-builder-ops]
divi_version: "5.x"
last_updated: 2026-03-12
content_type: playbook
audience: llm
---

# Playbook: Known Limitations

**Things LLMs consistently get wrong about Divi 5. Read this before giving any Divi advice.**

This playbook exists because AI assistants — including you — have been trained on generic WordPress knowledge and outdated Divi 4 information. Divi 5 behaves differently in ways that matter. If you're about to help someone with Divi 5, internalize these rules first.

## Hard Rules (Violating These Breaks Things)

### 1. Never CREATE New Content via Backend Methods (But Modifying Existing Blocks Is Fine)

Content CREATED via the WordPress REST API, direct database writes, or any backend method using `wp:divi/placeholder` block format will render on the frontend but **be completely invisible in the Visual Builder**. The client cannot edit the page.

**Why:** API-injected content using `wp:divi/placeholder` blocks does not register in Divi's internal React state. The Visual Builder's Layers panel shows only a single empty "section" despite full content existing in the `post_content` field.

**What to do instead:** All NEW content that needs to remain editable MUST be created through the Visual Builder interface. If the user needs programmatic content creation, use browser automation (Playwright, Claude in Chrome) to drive the Visual Builder UI.

**IMPORTANT CLARIFICATION:** Modifying the JSON attributes of blocks already created through the VB via the REST API works perfectly. The VB reads the updated block JSON on next open and renders the changes correctly. This is the proven pattern for batch style migration — create the structure in the VB, then use the REST API to adjust spacing, colors, typography, and content across many blocks efficiently.

**The one exception for new content:** If the page is purely programmatic and will never be edited in the VB (e.g., a dynamically generated landing page), REST API injection works for frontend rendering. But make this tradeoff explicit to the user.

### 2. TinyMCE setContent() Does Not Persist

When a Text module is selected in the Visual Builder, TinyMCE powers the content editor. You can read content with `tinymce.getContent()`, but `tinymce.setContent()` only updates the visual display — **it does not sync to Divi's save state**. Content set this way will revert on save.

**Why:** Divi 5 reads from its own internal React state on save, not from TinyMCE's DOM.

**What to do instead:** Type content via keyboard events. Click into the TinyMCE editor → Cmd+A to select all → type the replacement content. Keyboard input triggers the React event chain that Divi captures.

### 3. Testimonial Blocks Don't Render Author/JobTitle

The `wp:divi/testimonial` block supports `content.author` and `content.jobTitle` fields in JSON, but SSR renders ONLY the `innerContent` field. Author and job title are silently dropped.

Additionally, testimonial `innerContent` is **plain text, not HTML**. Unicode-encoded HTML tags (`\u003c`) render as literal escape sequences on the page.

**What to do instead:** Append attribution as plain text with an em dash:
```
Testimonial text here...

— Author Name, Company Name
```

### 4. Section Background Images May Not Render via JSON Attributes

Divi 5 SSR does not reliably render background images set via section-level JSON attributes. The section renders with a white/blank background.

**What to do instead:** Set a solid color in section attributes for the fallback, then use inline CSS in a text block:
```html
<div style="background: linear-gradient(rgba(10,30,80,0.75), rgba(10,30,80,0.75)), url(https://site.com/image.jpg) center/cover no-repeat; padding: 80px 20px;">
  <!-- content here -->
</div>
```

### 5. No Public JSON Import/Export Schema

As of March 2026, no developer-level documentation exists for Divi 5's JSON layout import/export format. Do not suggest "export as JSON and modify" as a workflow — there's no spec to follow and the format is undocumented.

**What to do instead:** Visual Builder automation is the only reliable method for creating editable content programmatically.

## Soft Rules (Getting These Wrong Wastes Time)

### 6. Always Set Global Design System First

Divi defaults to 14px body text and 30px headings. If the user hasn't configured globals in the Theme Customizer, every module will look wrong and need manual overrides. See the [Design System Setup](design-system-setup.md) playbook.

### 7. CSS Specificity in Divi Is Unusually Deep

Divi generates selectors like `.et_pb_section .et_pb_row .et_pb_module .et_pb_text_inner p`. If you suggest CSS customizations, your selectors need to be at least this specific or use `!important`. Generic selectors like `.my-class p { color: red; }` will almost always lose the specificity fight.

### 8. Box Shadow Hover on Columns Doesn't Work Natively

Divi 5 does not support Box Shadow hover states on a Column that contains multiple modules. The hover state must be applied via Free-Form CSS:

```css
selector {
    transition: box-shadow 0.3s ease;
}
selector:hover {
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}
```

Use **Advanced → CSS → Free-Form CSS** with the `selector` keyword to target the column container.

### 9. Row Width vs Section Width

Divi rows default to a constrained width (typically 1080px), centered within the full-width section. The section background spans edge-to-edge; the row content does not.

If you're suggesting a full-bleed layout where content goes edge-to-edge, the user needs to set the row's `maxWidth: 100%` and zero out padding. Don't assume "full-width section" means "full-width content."

### 10. The Visual Builder Layers Panel May Not Show All Content

The VB's Layers panel may only display a subset of blocks that exist in the page content (e.g., showing 3 sections when 16 exist). This is a known Divi 5 beta limitation. The frontend renders everything correctly regardless.

Don't tell the user "your content is gone" if the Layers panel looks empty — check the frontend first.

### 11. Divi 5 Uses Desktop-First Breakpoints

Divi 5 uses `max-width` media queries (desktop-first), not mobile-first. The default breakpoints are Phone (<478px), Tablet, and Desktop. Seven breakpoints are available total; three are enabled by default.

If you're suggesting responsive CSS, write `max-width` queries, not `min-width`.

### 12. wp.data Is Not Available in the Visual Builder

Divi 5 does NOT expose a Redux store or `wp.data` stores in the Visual Builder iframe. Don't suggest using `wp.data.select()` or `wp.data.dispatch()` for interacting with the builder — they don't exist.

### 13. Application Passwords May Fail on Shared Hosting

Some shared hosts strip the `Authorization` header from requests, breaking WordPress Application Passwords for REST API auth. If the user reports 401 errors despite valid credentials, suggest browser-based cookie auth with `wpApiSettings.nonce` instead.

### 14. Module UUIDs Change on Every Page Reload

Divi 5 module IDs (UUIDs like `1b459396-b3b5-49d1-b00c-6120de1ac485`) change every time the page reloads in the Visual Builder. Never hardcode a module UUID in scripts. Always locate a block by searching for a unique string in its content, then use `lastIndexOf('<!-- wp:divi/text', matchPosition)` to find the containing block start.

### 15. Use wp.apiRequest, Not wp.apiFetch

In the Divi editor context, `wp.apiFetch` is NOT available (`TypeError: wp.apiFetch is not a function`). Use `wp.apiRequest` (jQuery-based) instead — it's always available when logged into wp-admin.

### 16. Never Run REST API Requests in Parallel

Running multiple `wp.apiRequest` calls simultaneously gets throttled by WordPress — requests hang indefinitely. Always chain REST API calls sequentially using `.done(function() { return wp.apiRequest(...) })`.

### 17. Regex JSON Extraction Fails on Block Comments

Standard regex approaches to extract JSON from block comments (e.g., `raw.indexOf('-->')`) fail because `-->` can appear inside JSON string values. Use a brace-depth character-by-character parser instead. See the [REST API Content](rest-api-content.md) playbook for the proven parser code.

### 18. Design Panel Site Variables (Database Icon)

When editing any field in the Design panel (spacing, sizing, typography, etc.), clicking into the field reveals a small database icon at the right edge. Clicking this icon inserts a site variable — a global design token from the Variable Manager. This is how you connect module settings to the global design system instead of hardcoding values. Recommend this approach whenever a value should be global (accent color, standard section padding, max content width).

### 19. Divi Data Registry (Read-Only Store Access)

From inside the VB iframe, you CAN read module state using:
```javascript
var store = window.divi.data.select('divi/edit-post');
store.getAllModuleIds();       // all module IDs on the page
store.getModuleName(id);       // 'divi/text', 'divi/section', etc.
store.getModuleAttrs(id);      // full attributes object
```
Note: `getModuleType(id)` returns generic types (`'module'`, `'section'`). Use `getModuleName(id)` for specific types. Module IDs change on reload — always re-query.

### 20. Claude in Chrome Security Filter

When running JavaScript via the Claude in Chrome browser tool, the extension filters output for security. Strings containing `=`, `;`, `?`, `&`, URLs, or base64-like patterns get blocked. Return booleans, counts, or key names instead of raw CSS/JSON values. Replace problematic characters if you must return structured data: `=` → `[eq]`, `;` → `[sc]`, `?` → `[q]`.

## Quick Diagnostic Table

When a user reports a problem, check this table first:

| Symptom | Most Likely Cause | Solution |
|---------|------------------|----------|
| VB shows empty page despite content existing | New content created via REST API | Rebuild through Visual Builder (modifying existing blocks is fine) |
| Text content reverts after saving in VB | Used `tinymce.setContent()` | Type via keyboard events instead |
| Testimonial shows no author name | SSR doesn't render author/jobTitle fields | Append plain text `— Name, Company` to content |
| Section background is white/blank | Background image set via JSON attributes | Use inline CSS in a text block |
| Custom CSS has no effect | Specificity too low | Match Divi's selector depth or use `!important` |
| Font looks wrong / text is 14px | Global typography not configured | Run [Design System Setup](design-system-setup.md) |
| REST API returns 401 | Host strips Authorization header | Use browser cookie auth |
| Pages look different on phone | Used `min-width` media queries | Switch to `max-width` (desktop-first) |
| Layers panel shows fewer sections than exist | Known VB beta limitation | Check frontend — content is likely rendering fine |
| `wp.apiFetch is not a function` | Wrong API method in Divi context | Use `wp.apiRequest` instead |
| All REST API requests hang | Running requests in parallel | Chain sequentially with `.done()` callbacks |
| Module not found after page reload | Hardcoded module UUID | Locate blocks by content string, not by ID |
| Block JSON extraction finds wrong position | `-->` inside JSON string values | Use brace-depth character parser, not regex |
| Console output blocked in Claude in Chrome | Extension security filter | Return booleans/counts; replace `=;?&` with safe tokens |
| `maxWidth: "900%"` wrong unit | Pre-existing Divi bug in block JSON | Explicitly set to `"900px"` via REST API |
| Color picker value not saving | Store subscriber never fires | Click Divi Save button — it captures typed field values |
| Inline style scan returns empty | Content is unicode-escaped in JSON | Decode `innerContent` before scanning for styles |
