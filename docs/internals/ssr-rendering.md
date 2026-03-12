---
title: "SSR Rendering"
category: internals
tags: [ssr, rendering, post-content, boundary, server-side]
related: [block-format, content-encoding, testimonial-ssr]
divi_version: "5.x"
last_updated: 2026-03-12
---

# SSR Rendering

How Divi 5's server-side rendering processes block comments into HTML, and the critical boundaries that determine what renders.

## The `post-content` Boundary

**This is the #1 gotcha for programmatic content management with Divi 5.**

Page content often ends with a `<!-- /wp:post-content -->` closing tag. This marks the boundary of the WordPress block parser's content area. Any Divi blocks inserted AFTER this tag will NOT be rendered by SSR.

Blocks after the boundary appear in `view-source:` as unprocessed block comments (invisible to users on the rendered page).

### How to Detect

Content appears in raw HTML source but not in the rendered DOM. Block comments are passed through literally instead of being processed into `<div class="et_pb_section_X">` elements.

### How to Prevent

Always insert new blocks BEFORE `<!-- /wp:post-content -->`:

```javascript
const closeIdx = raw.indexOf('<!-- /wp:post-content -->');
const newContent = raw.substring(0, closeIdx) + newSection + '\n' + raw.substring(closeIdx);
```

## The Double Comment Bug

When removing or rearranging sections in raw content, it's possible to accidentally create a `<!--<!--` double comment opener. This causes the browser to interpret everything after the stray `<!--` as one giant HTML comment node, making entire sections invisible.

### Detection

```javascript
// Check for comment nodes containing section content
const content = document.querySelector('.et_builder_inner_content');
content.childNodes.forEach(n => {
  if (n.nodeType === 8 && n.textContent.length > 1000) {
    console.error('Sections trapped in comment node!', n.textContent.length, 'chars');
  }
});
```

### Prevention

Before saving, always validate:
```javascript
const doubleComments = (newContent.match(/<!--\s*<!--/g) || []).length;
if (doubleComments > 0) throw new Error('Double comment detected! Do not save.');
```

### Root Cause

When Divi SSR processes `<!-- wp:divi/section {...} -->`, it consumes the `-->` to close its processing. A stray `<!--` before the block comment gets output literally. The browser then sees `<!--<div class="et_pb_section_N"...` and starts an HTML comment that never closes.

## Background Image Rendering Gap

Divi 5 SSR does not reliably render background images set via section JSON attributes. Sections render with a white/blank background.

**Workaround:** Set a solid `color` in section attributes, then use inline CSS in a text block for the actual background image. See the [HTML Workarounds](../playbooks/html-workarounds.md) playbook.

## Post Meta Requirements

For Divi SSR to process a page, the `_et_pb_use_builder` post meta must be set to `"on"`. This is automatic for pages created through the Visual Builder but must be explicitly set when creating pages via REST API.

## Section Validation Checklist

Before every programmatic content save:

1. Section open and close tag counts must be equal
2. Zero `<!--<!--` double comment patterns
3. Content starts with `<!-- wp:divi/placeholder -->` (if using placeholder wrapper)
4. Content ends before `<!-- /wp:post-content -->` boundary
5. No raw HTML between section close tags and next section open tags
6. Total character count is reasonable (not accidentally truncated)

## Related

- [Block Comment Format](block-format.md) — the block structure that SSR processes
- [Content Encoding](content-encoding.md) — how HTML is encoded in block JSON
- [Testimonial Rendering Gaps](testimonial-ssr.md) — SSR bugs specific to testimonials
