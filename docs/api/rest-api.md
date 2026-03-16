---
title: "REST API Integration"
description: "Divi 5 REST API reference — reading and modifying block content via WordPress endpoints, authentication, the create-vs-modify limitation, and batch operations."
category: api
tags: [rest-api, wordpress, endpoints, json, programmatic, content-management]
related: [block-json-reference, hooks-filters, custom-modules, wp-cli]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://developer.wordpress.org/rest-api/"
---

# REST API Integration

Reading and modifying Divi 5 block content via WordPress REST API endpoints.

!!! abstract "Quick Reference"
    **Authentication:** Application Passwords or cookie auth with `wpApiSettings.nonce`
    **Read content:** `GET /wp-json/wp/v2/pages/{id}?context=edit` → `response.content.raw`
    **Write content:** `POST /wp-json/wp/v2/pages/{id}` with `{ content: "..." }`
    **Critical rule:** MODIFY existing VB-created blocks = works. CREATE new blocks via API = renders on frontend but invisible in Visual Builder.
    **API method:** Use `wp.apiRequest` (NOT `wp.apiFetch`). Chain calls sequentially — parallel calls hang.
    **Last verified:** 2026-03-16

## How Divi 5 Content Is Stored

Divi 5 stores page content as WordPress block comments with JSON attributes in the `post_content` database field. Each module is a `<!-- wp:divi/{module} {JSON} /-->` block comment (leaf blocks) or an `<!-- wp:divi/{module} {JSON} -->...<!-- /wp:divi/{module} -->` pair (container blocks).

The full block hierarchy is:

```
placeholder → section → row → column → module(s)
```

See [Block Comment Format](../internals/block-format.md) for the complete structural reference and [Block JSON Reference](block-json-reference.md) for the attribute schema.

## Reading Divi Content

### Endpoint

```
GET /wp-json/wp/v2/pages/{id}?context=edit
```

The `context=edit` parameter is required to receive the raw block content. Without it, WordPress returns rendered HTML.

### Response Structure

```json
{
  "id": 42,
  "content": {
    "raw": "<!-- wp:divi/placeholder -->...<!-- /wp:divi/placeholder -->",
    "rendered": "<div class=\"et_builder_inner_content\">...</div>",
    "protected": false,
    "block_version": 1
  },
  "meta": {
    "_et_pb_use_builder": "on"
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `content.raw` | `string` | Raw block comment markup with JSON attributes |
| `content.rendered` | `string` | Server-side rendered HTML output |
| `meta._et_pb_use_builder` | `string` | Must be `"on"` for Divi SSR to process the page |

### JavaScript Example (Browser Console)

```javascript
// From within wp-admin or VB context
wp.apiRequest({
    path: '/wp/v2/pages/42?context=edit',
    method: 'GET'
}).done(function(response) {
    var raw = response.content.raw;
    console.log('Content length:', raw.length);
    console.log('Sections:', (raw.match(/wp:divi\/section/g) || []).length);
});
```

### cURL Example

```bash
curl -s "https://example.com/wp-json/wp/v2/pages/42?context=edit" \
  -u "username:xxxx xxxx xxxx xxxx xxxx xxxx" \
  -H "Content-Type: application/json" | python3 -m json.tool
```

## Modifying Existing Content

Updating the JSON attributes of blocks that were originally created through the Visual Builder works reliably. The VB reads the updated block JSON on next open and renders changes correctly.

### Endpoint

```
POST /wp-json/wp/v2/pages/{id}
```

### Request Body

```json
{
  "content": "<!-- wp:divi/placeholder -->...updated blocks...<!-- /wp:divi/placeholder -->"
}
```

### JavaScript Example

```javascript
wp.apiRequest({
    path: '/wp/v2/pages/42',
    method: 'POST',
    data: {
        content: updatedContent
    }
}).done(function(response) {
    console.log('Saved. Revision:', response.id);
}).fail(function(err) {
    console.error('Save failed:', err.responseJSON.message);
});
```

!!! danger "CRITICAL: The Create vs. Modify Rule"
    **Modifying** existing VB-created blocks via REST API: **Works perfectly.** The Visual Builder reads the updated JSON on next open and renders all changes correctly. This is the proven pattern for batch style migration, content updates, and attribute changes.

    **Creating** new content via REST API: **Breaks Visual Builder editing.** Content created via the REST API using `wp:divi/placeholder` block format renders on the frontend but is **completely invisible in the Visual Builder**. The Layers panel shows only a single empty "section" despite full content existing in `post_content`.

    **Why:** API-injected content using `wp:divi/placeholder` blocks does not register in Divi's internal React state. The Visual Builder initializes its state from the block structure, and programmatically created blocks lack whatever internal registration the VB requires.

    **The one exception:** If the page is purely programmatic and will never be edited in the VB (e.g., a dynamically generated landing page), REST API creation works for frontend rendering. Make this tradeoff explicit.

    See [Known Limitations — Rule #1](../playbooks/known-limitations.md) for the full explanation.

## Authentication

### Method 1: Application Passwords (External Scripts)

WordPress 5.6+ supports Application Passwords for REST API authentication. Generate one at **Users → Your Profile → Application Passwords**.

```bash
# Base64-encoded username:application_password
curl -X POST "https://example.com/wp-json/wp/v2/pages/42" \
  -u "admin:xxxx xxxx xxxx xxxx xxxx xxxx" \
  -H "Content-Type: application/json" \
  -d '{"content": "..."}'
```

!!! warning "Application Passwords on Shared Hosting"
    Some shared hosts strip the `Authorization` header from requests, causing 401 errors despite valid credentials. If this happens, use cookie auth from the browser instead. See [Known Limitations — Rule #13](../playbooks/known-limitations.md).

### Method 2: Cookie Auth with Nonce (Browser Context)

When running scripts from the browser console while logged into wp-admin, use the built-in nonce:

```javascript
// wpApiSettings.nonce is automatically available in wp-admin
wp.apiRequest({
    path: '/wp/v2/pages/42?context=edit',
    method: 'GET'
}).done(function(response) {
    // Authenticated via cookie + nonce
});
```

`wp.apiRequest` automatically includes the nonce from `wpApiSettings.nonce`.

### wp.apiRequest vs wp.apiFetch

| Method | Available in Divi? | Based On | Notes |
|--------|-------------------|----------|-------|
| `wp.apiRequest` | **Yes** | jQuery AJAX | Always available in wp-admin. Returns jQuery Deferred. ⚠️ Observed |
| `wp.apiFetch` | **No** | Fetch API | Throws `TypeError: wp.apiFetch is not a function` in Divi context. ⚠️ Observed |

Always use `wp.apiRequest` when writing scripts that run in the Divi editor context. See [Known Limitations — Rule #15](../playbooks/known-limitations.md).

## Relevant Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/wp/v2/pages/{id}?context=edit` | `GET` | Read page content with raw block JSON |
| `/wp/v2/pages/{id}` | `POST` | Update page content |
| `/wp/v2/posts/{id}?context=edit` | `GET` | Read post content with raw block JSON |
| `/wp/v2/posts/{id}` | `POST` | Update post content |
| `/wp/v2/et_pb_layout?context=edit` | `GET` | List Divi Library layouts 🔬 Needs Testing |
| `/wp/v2/et_pb_layout/{id}?context=edit` | `GET` | Read a single library layout 🔬 Needs Testing |
| `/wp/v2/et_template?context=edit` | `GET` | List Theme Builder templates 🔬 Needs Testing |
| `/wp/v2/et_template/{id}?context=edit` | `GET` | Read a single Theme Builder template 🔬 Needs Testing |

!!! note "Custom Post Type REST Availability"
    The `et_pb_layout` and `et_template` endpoints are available only if Divi registers these CPTs with `show_in_rest: true`. This is the case in current Divi 5 beta versions but may change. 🔬 Needs Testing

## Sequential Request Chaining

Running multiple `wp.apiRequest` calls in parallel causes WordPress to throttle or hang requests indefinitely. Always chain calls sequentially using `.done()` callbacks. ⚠️ Observed

### Pattern: Sequential Chaining

```javascript
// CORRECT: Sequential chaining
wp.apiRequest({
    path: '/wp/v2/pages/42?context=edit',
    method: 'GET'
}).done(function(page42) {
    console.log('Page 42 loaded');

    return wp.apiRequest({
        path: '/wp/v2/pages/43?context=edit',
        method: 'GET'
    });
}).done(function(page43) {
    console.log('Page 43 loaded');

    return wp.apiRequest({
        path: '/wp/v2/pages/44?context=edit',
        method: 'GET'
    });
}).done(function(page44) {
    console.log('Page 44 loaded');
    console.log('All pages loaded successfully');
});
```

```javascript
// WRONG: Parallel calls — these hang indefinitely
var p1 = wp.apiRequest({ path: '/wp/v2/pages/42?context=edit' });
var p2 = wp.apiRequest({ path: '/wp/v2/pages/43?context=edit' });
var p3 = wp.apiRequest({ path: '/wp/v2/pages/44?context=edit' });
// p2 and p3 will hang
```

See [Known Limitations — Rule #16](../playbooks/known-limitations.md).

## Extracting JSON from Block Comments

Standard regex extraction fails because `-->` can appear inside JSON string values. Use a brace-depth character-by-character parser.

### The Brace-Depth Parser

```javascript
/**
 * Extract JSON object from raw block content starting at a given position.
 * Handles nested braces and strings containing --> safely.
 *
 * @param {string} raw - The raw post_content string
 * @param {number} jsonStart - Index of the opening { character
 * @returns {Object} Parsed JSON object
 */
function extractBlockJson(raw, jsonStart) {
    var depth = 0, inStr = false, esc = false, end = -1;
    for (var i = jsonStart; i < jsonStart + 50000; i++) {
        var c = raw[i];
        if (esc) { esc = false; continue; }
        if (c === '\\') { esc = true; continue; }
        if (c === '"') { inStr = !inStr; continue; }
        if (!inStr) {
            if (c === '{') depth++;
            else if (c === '}') {
                depth--;
                if (depth === 0) { end = i; break; }
            }
        }
    }
    if (end === -1) throw new Error('JSON extraction failed — no matching closing brace');
    return JSON.parse(raw.slice(jsonStart, end + 1));
}
```

### Locating Blocks by Content

Module UUIDs change on every page reload. Always locate blocks by searching for a unique string in the content, then walking backward to find the block start:

```javascript
/**
 * Find a text block containing a specific string.
 *
 * @param {string} raw - The raw post_content
 * @param {string} anchor - A unique string in the block's content
 * @returns {{ blockStart: number, jsonStart: number, json: Object }}
 */
function findTextBlock(raw, anchor) {
    var idx = raw.indexOf(anchor);
    if (idx === -1) throw new Error('Anchor not found: ' + anchor);

    var blockStart = raw.lastIndexOf('<!-- wp:divi/text', idx);
    var jsonStart = raw.indexOf('{', blockStart);
    var json = extractBlockJson(raw, jsonStart);

    return { blockStart: blockStart, jsonStart: jsonStart, json: json };
}
```

See [JSON Attribute Map — Brace-Depth Parser](../internals/json-attribute-map.md) for the original reference.

## The Post-Content Boundary

Page content often ends with a `<!-- /wp:post-content -->` closing tag. Any Divi blocks inserted AFTER this boundary are **not rendered** by SSR — they appear in `view-source:` as raw block comments, invisible to users. ⚠️ Observed

### Detection and Prevention

```javascript
/**
 * Insert content before the post-content boundary.
 *
 * @param {string} raw - Current post_content
 * @param {string} newSection - Block content to insert
 * @returns {string} Updated content with blocks properly placed
 */
function insertBeforeBoundary(raw, newSection) {
    var closeIdx = raw.indexOf('<!-- /wp:post-content -->');
    if (closeIdx === -1) {
        // No boundary — append normally
        return raw + '\n' + newSection;
    }
    return raw.substring(0, closeIdx) + newSection + '\n' + raw.substring(closeIdx);
}
```

See [SSR Rendering — Post-Content Boundary](../internals/ssr-rendering.md) for the full explanation.

## The Double-Comment Safety Check

When modifying raw block content, it is possible to accidentally create a `<!--<!--` double comment opener. This causes the browser to interpret everything after the stray `<!--` as one giant HTML comment node, making entire sections invisible on the frontend. ⚠️ Observed

### Pre-Save Validation

```javascript
/**
 * Validate content before saving via REST API.
 * Checks for double comments, balanced tags, and boundary placement.
 *
 * @param {string} content - The content to validate
 * @throws {Error} If validation fails
 */
function validateBeforeSave(content) {
    // 1. Double comment check
    var doubleComments = (content.match(/<!--\s*<!--/g) || []).length;
    if (doubleComments > 0) {
        throw new Error('Double comment detected (' + doubleComments + ' instances). Do not save.');
    }

    // 2. Balanced section tags
    var opens = (content.match(/<!-- wp:divi\/section/g) || []).length;
    var closes = (content.match(/<!-- \/wp:divi\/section/g) || []).length;
    if (opens !== closes) {
        throw new Error('Unbalanced sections: ' + opens + ' opens, ' + closes + ' closes.');
    }

    // 3. Content before boundary
    var boundaryIdx = content.indexOf('<!-- /wp:post-content -->');
    if (boundaryIdx > -1) {
        var afterBoundary = content.substring(boundaryIdx + 25);
        if (afterBoundary.indexOf('wp:divi/') > -1) {
            throw new Error('Divi blocks found after post-content boundary.');
        }
    }

    // 4. Reasonable length
    if (content.length < 100) {
        throw new Error('Content suspiciously short (' + content.length + ' chars). Possible truncation.');
    }
}
```

See [SSR Rendering — Double Comment Bug](../internals/ssr-rendering.md) and [SSR Rendering — Section Validation Checklist](../internals/ssr-rendering.md).

## Common Operations

| Operation | Approach | Notes |
|-----------|----------|-------|
| Change text in a module | Find block by content anchor, update `content.innerContent`, save | Must use unicode encoding for HTML. See [Content Encoding](../internals/content-encoding.md). |
| Change a module's color | Find block, set `module.advanced.text.text.desktop.value.color`, save | See [JSON Attribute Map](../internals/json-attribute-map.md) for paths. |
| Change spacing/padding | Find block, set `module.decoration.spacing.desktop.value.padding`, save | Use object: `{top, right, bottom, left}` |
| Change max-width | Find block, set `module.decoration.sizing.desktop.value.maxWidth`, save | String value: `"900px"` |
| Change background color | Find block, set `module.decoration.background.desktop.value.color`, save | Hex string: `"#037d87"` |
| Batch update across pages | Loop through page IDs, chain requests sequentially, modify each | Never parallelize requests |
| Add responsive value | Add `tablet` and `phone` keys alongside `desktop` | `{"desktop":{"value":"..."},"tablet":{"value":"..."},"phone":{"value":"..."}}` |

## Complete Working Example

This script reads a page, finds a text block by content, modifies its text and color, validates the result, and saves it back.

```javascript
// Complete example: modify a text block's content and color via REST API
// Run from browser console while logged into wp-admin

var PAGE_ID = 42;
var ANCHOR_TEXT = 'Welcome to Our Site';  // Unique text to find the block

// Step 1: Read the page
wp.apiRequest({
    path: '/wp/v2/pages/' + PAGE_ID + '?context=edit',
    method: 'GET'
}).done(function(response) {
    var raw = response.content.raw;
    console.log('Loaded page. Content length:', raw.length);

    // Step 2: Find the target text block
    var idx = raw.indexOf(ANCHOR_TEXT);
    if (idx === -1) {
        console.error('Anchor text not found');
        return;
    }
    var blockStart = raw.lastIndexOf('<!-- wp:divi/text', idx);
    var jsonStart = raw.indexOf('{', blockStart);

    // Step 3: Extract JSON using brace-depth parser
    var depth = 0, inStr = false, esc = false, end = -1;
    for (var i = jsonStart; i < jsonStart + 50000; i++) {
        var c = raw[i];
        if (esc) { esc = false; continue; }
        if (c === '\\') { esc = true; continue; }
        if (c === '"') { inStr = !inStr; continue; }
        if (!inStr) {
            if (c === '{') depth++;
            else if (c === '}') { depth--; if (depth === 0) { end = i; break; } }
        }
    }
    var blockJson = JSON.parse(raw.slice(jsonStart, end + 1));
    console.log('Found block. Current content:',
        blockJson.content.innerContent.desktop.value.substring(0, 80));

    // Step 4: Modify the block
    // Update text content (must use unicode encoding for HTML)
    blockJson.content.innerContent.desktop.value =
        '\\u003ch2\\u003eWelcome to Our New Site\\u003c/h2\\u003e' +
        '\\u003cp\\u003eWe have redesigned our website. Explore our services below.\\u003c/p\\u003e';

    // Update text color
    if (!blockJson.module.advanced) blockJson.module.advanced = {};
    if (!blockJson.module.advanced.text) blockJson.module.advanced.text = {};
    if (!blockJson.module.advanced.text.text) blockJson.module.advanced.text.text = {};
    blockJson.module.advanced.text.text.desktop = { value: { color: '#1a1a2e' } };

    // Step 5: Rebuild the content string
    var newJsonStr = JSON.stringify(blockJson);
    var newContent = raw.substring(0, jsonStart) + newJsonStr + raw.substring(end + 1);

    // Step 6: Validate before saving
    var doubleComments = (newContent.match(/<!--\s*<!--/g) || []).length;
    if (doubleComments > 0) {
        console.error('ABORT: Double comment detected!');
        return;
    }
    var sectionOpens = (newContent.match(/<!-- wp:divi\/section/g) || []).length;
    var sectionCloses = (newContent.match(/<!-- \/wp:divi\/section/g) || []).length;
    if (sectionOpens !== sectionCloses) {
        console.error('ABORT: Unbalanced sections:', sectionOpens, 'vs', sectionCloses);
        return;
    }

    // Step 7: Save via REST API
    return wp.apiRequest({
        path: '/wp/v2/pages/' + PAGE_ID,
        method: 'POST',
        data: { content: newContent }
    });
}).done(function(response) {
    if (response) {
        console.log('Saved successfully. Page ID:', response.id);
    }
}).fail(function(err) {
    console.error('Error:', err.responseJSON ? err.responseJSON.message : err.statusText);
});
```

## Troubleshooting

!!! warning "REST API returns 401 Unauthorized"
    **Cause:** Application Password not set up, or the host strips `Authorization` headers.

    **Fix:** Verify Application Password at **Users → Profile → Application Passwords**. If on shared hosting, use browser cookie auth with `wpApiSettings.nonce` instead. See [Known Limitations — Rule #13](../playbooks/known-limitations.md).

!!! warning "Content saved but invisible in Visual Builder"
    **Cause:** Content was CREATED (not modified) via the REST API. New blocks injected via API do not register in Divi's React state.

    **Fix:** There is no fix — the content must be recreated through the Visual Builder. This is a fundamental limitation. See the Create vs. Modify Rule above.

!!! warning "REST API requests hang indefinitely"
    **Cause:** Multiple `wp.apiRequest` calls running in parallel.

    **Fix:** Chain all requests sequentially using `.done()` callbacks. See the Sequential Request Chaining section above.

!!! warning "`wp.apiFetch is not a function`"
    **Cause:** `wp.apiFetch` is not available in the Divi editor context.

    **Fix:** Use `wp.apiRequest` instead. It is jQuery-based and always available in wp-admin. See [Known Limitations — Rule #15](../playbooks/known-limitations.md).

!!! warning "Sections disappear after saving"
    **Cause:** A `<!--<!--` double comment was introduced during content manipulation, causing the browser to swallow sections into a single comment node.

    **Fix:** Always run the double-comment safety check before saving. See the Pre-Save Validation section above and [SSR Rendering — Double Comment Bug](../internals/ssr-rendering.md).

!!! warning "New blocks render on frontend but not in view-source"
    **Cause:** Blocks were inserted after the `<!-- /wp:post-content -->` boundary.

    **Fix:** Always insert blocks before the boundary. See the Post-Content Boundary section above and [SSR Rendering — Post-Content Boundary](../internals/ssr-rendering.md).

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior. Divi 4 used shortcode-based content (`[et_pb_section]...[/et_pb_section]`) stored in `post_content`. Divi 5 uses WordPress block comments with JSON attributes. The REST API endpoints are standard WordPress — the difference is entirely in the content format.

!!! info "Beta Behavior"
    The create-vs-modify limitation and the `wp.apiFetch` unavailability are observed in Divi 5 public beta (2025–2026). These behaviors may change in future releases. ⚠️ Observed

## Related

- [Block JSON Reference](block-json-reference.md) — complete JSON attribute schema for Divi 5 blocks
- [WP-CLI Integration](wp-cli.md) — command-line tools for Divi content management
- [Hooks & Filters](hooks-filters.md) — PHP and JavaScript hooks for extending Divi
- [Custom Modules](custom-modules.md) — building custom Divi 5 modules
- [Block Comment Format](../internals/block-format.md) — how blocks are structured in `post_content`
- [JSON Attribute Map](../internals/json-attribute-map.md) — CSS-to-JSON path mapping
- [SSR Rendering](../internals/ssr-rendering.md) — server-side rendering behavior and gotchas
- [Content Encoding](../internals/content-encoding.md) — unicode encoding rules for HTML in JSON
- [Known Limitations](../playbooks/known-limitations.md) — the 20 rules for working with Divi 5
- [VB Architecture](../internals/vb-architecture.md) — Visual Builder dual-frame structure
