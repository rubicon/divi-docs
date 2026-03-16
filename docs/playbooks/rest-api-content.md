---
title: "REST API Content Management"
description: "LLM playbook for Divi 5 REST API content — the create-vs-modify rule, brace-depth parsing, sequential chaining, content encoding, and save validation patterns."
category: playbooks
tags: [playbook, rest-api, content-management, programmatic, json, blocks]
related: [known-limitations, visual-builder-ops, build-a-page]
divi_version: "5.x"
last_updated: 2026-03-16
content_type: playbook
audience: llm
---

# Playbook: REST API Content Management

**How to read and modify Divi 5 page content via the WordPress REST API — the rules, the patterns, and the things that break.**

!!! danger "CRITICAL: The Create vs Modify Rule"
    **MODIFY** existing VB-created blocks via REST API = WORKS. The Visual Builder reads updated block JSON on next open and renders changes correctly.

    **CREATE** new blocks via REST API = renders on the frontend but is **INVISIBLE in the Visual Builder**. The client cannot edit the page.

    If the content must be editable in the Visual Builder, create it through the VB (use browser automation). Only modify existing blocks via REST API.

!!! abstract "Quick Rules"
    1. **Modify, never create.** REST API can change existing block attributes. It cannot create VB-editable blocks.
    2. **Use `wp.apiRequest`, not `wp.apiFetch`.** `wp.apiFetch` throws `TypeError` in the Divi context.
    3. **Chain requests sequentially.** Parallel `wp.apiRequest` calls hang indefinitely.
    4. **Use the brace-depth parser.** Regex and `indexOf('-->')` fail because `-->` can appear inside JSON string values.
    5. **Validate before saving.** Check section tag balance, double-comment patterns, and the `post-content` boundary.

## Why This Matters

When someone says "update the text on my Divi page" or "change all the button colors across my site," the REST API is the right tool. It is fast, scriptable, and works at scale. But the REST API has hard constraints that generic WordPress knowledge does not prepare you for. Get the create-vs-modify rule wrong and the client loses the ability to edit their page in the Visual Builder. Get the encoding wrong and content renders as escape sequences. Get the request pattern wrong and every call hangs.

This playbook is the complete reference for doing it right.

## The Create vs Modify Rule

### MODIFY Existing Blocks — This Works

Blocks created through the Visual Builder have a specific internal structure that the VB recognizes. When you modify the JSON attributes of those blocks via REST API, the VB reads the updated attributes on next open and renders the changes correctly.

This is the proven pattern for:

- Batch text updates across many pages
- Style migration (spacing, colors, typography)
- Content replacement (swap placeholder text with real copy)
- Stripping inline styles and moving them to block JSON attributes

### CREATE New Blocks — This Breaks VB Editing

Content created via the REST API, direct database writes, or any backend method using `wp:divi/placeholder` block format will render on the frontend. But the Visual Builder's Layers panel will show only a single empty "section" despite full content existing in `post_content`. The client cannot select, move, or edit any of the programmatically-created blocks.

**Why:** API-injected `wp:divi/placeholder` blocks do not register in Divi's internal React state. The VB loads content into its own state management layer, and blocks it did not create are invisible to that layer.

### Decision Tree

- **Need to change text, colors, spacing, or attributes on existing blocks?** Use REST API. This is fast and works perfectly.
- **Need to add a new section, row, or module?** Use browser automation (Playwright, Claude in Chrome) to drive the Visual Builder UI.
- **Need to create an entire page programmatically?** Ask: "Does this content need to be editable in the Visual Builder?" If yes, use browser automation. If the page is purely programmatic and will never be manually edited, REST API injection works for frontend rendering — but make this tradeoff explicit to the user.
- **Need to change styles across 50+ pages?** REST API batch modify with sequential chaining. Create the structure in the VB first, then use REST API for the bulk attribute changes.

## Step-by-Step: Reading Divi Content

### Step 1: Fetch the page content

Always use `context=edit` to get the raw block content, not the rendered HTML.

```javascript
wp.apiRequest({
    path: '/wp/v2/pages/123?context=edit',
    method: 'GET'
}).done(function(page) {
    var raw = page.content.raw;
    console.log('Content length:', raw.length);
    // raw contains the full block comment markup
});
```

### Step 2: Locate a block by content

Module UUIDs change on every page reload. Never hardcode a module UUID. Always locate a block by searching for a unique string in its content, then walk backward to find the block comment start.

```javascript
var idx = raw.indexOf('unique text anchor');
if (idx === -1) {
    console.error('Anchor text not found');
    return;
}
var blockStart = raw.lastIndexOf('<!-- wp:divi/text', idx);
var jsonStart = raw.indexOf('{', blockStart);
```

### Step 3: Parse the block JSON

Do NOT use regex. Do NOT search for `-->` to find the JSON end. Use the brace-depth parser (see below).

```javascript
var blockJson = extractBlockJson(raw, jsonStart);
// blockJson is now a parsed JavaScript object
```

### Step 4: Read attributes

```javascript
// Read the text content
var innerContent = blockJson.content.innerContent.desktop.value;

// Read design attributes
var bgColor = blockJson.module.decoration.background.desktop.value.color;
var padding = blockJson.module.decoration.spacing.desktop.value.padding;
var maxWidth = blockJson.module.decoration.sizing.desktop.value.maxWidth;

// Read text color
var textColor = blockJson.module.advanced.text.text.desktop.value.color;
```

## Step-by-Step: Modifying Divi Content

### Step 1: Fetch, locate, and parse (same as reading)

```javascript
wp.apiRequest({
    path: '/wp/v2/pages/123?context=edit',
    method: 'GET'
}).done(function(page) {
    var raw = page.content.raw;

    // Locate the block
    var idx = raw.indexOf('unique text anchor');
    var blockStart = raw.lastIndexOf('<!-- wp:divi/text', idx);
    var jsonStart = raw.indexOf('{', blockStart);

    // Parse with brace-depth parser
    var parseResult = extractBlockJsonWithEnd(raw, jsonStart);
    var blockJson = parseResult.json;
    var jsonEnd = parseResult.end;

    // Step 2: Modify attributes
    blockJson.module.decoration.background.desktop.value.color = '#1a1a2e';
    blockJson.module.decoration.spacing.desktop.value.padding = {
        top: '80px', bottom: '80px', left: '40px', right: '40px'
    };
    blockJson.module.advanced.text.text.desktop.value.color = '#ffffff';

    // Step 3: Rebuild the raw content
    var newJsonStr = JSON.stringify(blockJson);
    var newContent = raw.substring(0, jsonStart) + newJsonStr + raw.substring(jsonEnd + 1);

    // Step 4: Validate before saving
    validateContent(newContent);

    // Step 5: Save
    return wp.apiRequest({
        path: '/wp/v2/pages/123',
        method: 'POST',
        data: { content: newContent }
    });
}).done(function(result) {
    console.log('Save successful');
});
```

### Modifying text content

Text content inside block JSON is unicode-escaped. When modifying `innerContent`, encode HTML entities as literal 6-character escape strings:

```javascript
// Encoding table
// < → \u003c
// > → \u003e
// " → \u0022

// Example: set new heading text
var newHtml = '\\u003ch2\\u003eNew Heading\\u003c/h2\\u003e\\u003cp\\u003eNew paragraph text.\\u003c/p\\u003e';
blockJson.content.innerContent.desktop.value = newHtml;
```

Do NOT use raw `<`, `>`, or `"` in innerContent values. They must be unicode-escaped. See the [Content Encoding](../internals/content-encoding.md) reference for the full encoding table.

## The Brace-Depth Parser

Standard `JSON.parse` cannot extract JSON from block comments because you do not know where the JSON ends. Searching for `-->` fails because `-->` can appear inside JSON string values (e.g., in HTML content). The only reliable method is a character-by-character brace-depth parser.

```javascript
function extractBlockJsonWithEnd(raw, jsonStart) {
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
    if (end === -1) throw new Error('Failed to find JSON end boundary');
    return {
        json: JSON.parse(raw.slice(jsonStart, end + 1)),
        end: end
    };
}

// Convenience wrapper that returns only the parsed object
function extractBlockJson(raw, jsonStart) {
    return extractBlockJsonWithEnd(raw, jsonStart).json;
}
```

**How it works:** Walk character by character from the opening `{`. Track brace depth (increment on `{`, decrement on `}`). Ignore braces inside quoted strings. When depth returns to zero, you have found the matching closing `}`. Slice and parse.

**The 50000 limit:** Block JSON is typically 500-5000 characters. The 50000 limit is a safety bound. If your blocks are larger (e.g., containing very long encoded HTML), increase this value.

## Content Encoding Rules

HTML inside block JSON `innerContent` values must use literal unicode escape strings. These are 6-character sequences stored as literal text in the JSON, not JavaScript unicode escapes.

| Character | Escape Sequence | Example |
|-----------|----------------|---------|
| `<` | `\u003c` | `\u003cp\u003e` = `<p>` |
| `>` | `\u003e` | `\u003c/p\u003e` = `</p>` |
| `"` | `\u0022` | `class=\u0022my-class\u0022` = `class="my-class"` |

### Encoding when writing

When building new innerContent values in JavaScript, use double-escaped sequences so they survive JSON stringification:

```javascript
// In JavaScript source code, double-escape to produce literal \u003c in the JSON
var encoded = '\\u003ch2\\u003eHeading\\u003c/h2\\u003e';
blockJson.content.innerContent.desktop.value = encoded;
// JSON.stringify will produce: "\\u003ch2\\u003eHeading\\u003c/h2\\u003e"
// Which, stored in post_content, is the literal string: \u003ch2\u003eHeading\u003c/h2\u003e
// Divi SSR decodes this to: <h2>Heading</h2>
```

### Decoding when reading

When you fetch content via REST API, the innerContent values contain the literal escape sequences. Decode them before displaying or processing:

```javascript
function decodeInnerContent(encoded) {
    return encoded
        .replace(/\\u003c/g, '<')
        .replace(/\\u003e/g, '>')
        .replace(/\\u0022/g, '"');
}
```

### Testimonial exception

Testimonial block `innerContent` is plain text, not HTML. Unicode-encoded HTML tags render as literal escape sequences on the page. Append attribution as plain text with an em dash: `— Author Name, Company`. See [Known Limitations](known-limitations.md) rule #3.

## `wp.apiRequest` vs `wp.apiFetch`

**Rule: Always use `wp.apiRequest`. Never use `wp.apiFetch` in the Divi context.**

`wp.apiFetch` is a modern WordPress JavaScript API, but it is NOT available when the Divi Visual Builder is loaded. Calling it throws `TypeError: wp.apiFetch is not a function`. This is because Divi does not enqueue the `wp-api-fetch` package in its editor bundle.

`wp.apiRequest` is jQuery-based and is always available when logged into wp-admin. It uses jQuery's Deferred pattern (`.done()`, `.fail()`, `.always()`).

```javascript
// CORRECT — always works in Divi context
wp.apiRequest({
    path: '/wp/v2/pages/123?context=edit',
    method: 'GET'
}).done(function(page) {
    // handle response
}).fail(function(err) {
    console.error('Request failed:', err.responseText);
});

// WRONG — throws TypeError in Divi context
wp.apiFetch({ path: '/wp/v2/pages/123?context=edit' })
    .then(function(page) { /* never reaches here */ });
```

## Sequential Chaining

**Rule: Never run REST API requests in parallel. Always chain sequentially.**

Running multiple `wp.apiRequest` calls simultaneously causes WordPress to throttle requests. They hang indefinitely — no timeout, no error, just silence. This happens because WordPress serializes authenticated REST API requests per session.

### The `.done()` chain pattern

```javascript
// CORRECT — sequential chaining
wp.apiRequest({
    path: '/wp/v2/pages/101?context=edit',
    method: 'GET'
}).done(function(page1) {
    var updated1 = modifyContent(page1.content.raw);
    return wp.apiRequest({
        path: '/wp/v2/pages/101',
        method: 'POST',
        data: { content: updated1 }
    });
}).done(function() {
    return wp.apiRequest({
        path: '/wp/v2/pages/102?context=edit',
        method: 'GET'
    });
}).done(function(page2) {
    var updated2 = modifyContent(page2.content.raw);
    return wp.apiRequest({
        path: '/wp/v2/pages/102',
        method: 'POST',
        data: { content: updated2 }
    });
}).done(function() {
    console.log('All pages updated');
}).fail(function(err) {
    console.error('Chain failed:', err.responseText);
});
```

```javascript
// WRONG — parallel calls hang
var p1 = wp.apiRequest({ path: '/wp/v2/pages/101?context=edit', method: 'GET' });
var p2 = wp.apiRequest({ path: '/wp/v2/pages/102?context=edit', method: 'GET' });
// Both requests hang indefinitely
```

### Batch processing pattern

For operations across many pages, build a sequential queue:

```javascript
var pageIds = [101, 102, 103, 104, 105];
var chain = jQuery.Deferred().resolve();

pageIds.forEach(function(id) {
    chain = chain.then(function() {
        return wp.apiRequest({
            path: '/wp/v2/pages/' + id + '?context=edit',
            method: 'GET'
        }).done(function(page) {
            var updated = modifyContent(page.content.raw);
            return wp.apiRequest({
                path: '/wp/v2/pages/' + id,
                method: 'POST',
                data: { content: updated }
            });
        });
    });
});

chain.done(function() {
    console.log('All ' + pageIds.length + ' pages updated');
});
```

## Save Validation Checklist

Run these checks before every programmatic content save. Skipping them risks corrupting the page.

### 1. Section tag balance

Every `<!-- wp:divi/section` must have a matching `<!-- /wp:divi/section -->`. Count them.

```javascript
var opens = (newContent.match(/<!-- wp:divi\/section /g) || []).length;
var closes = (newContent.match(/<!-- \/wp:divi\/section -->/g) || []).length;
if (opens !== closes) throw new Error('Section tag mismatch: ' + opens + ' opens, ' + closes + ' closes');
```

### 2. No double comment patterns

A stray `<!--<!--` causes the browser to interpret everything after it as one giant HTML comment node. Entire sections disappear.

```javascript
var doubleComments = (newContent.match(/<!--\s*<!--/g) || []).length;
if (doubleComments > 0) throw new Error('Double comment detected! Do not save.');
```

### 3. Content before `post-content` boundary

Any blocks inserted AFTER `<!-- /wp:post-content -->` will not render. Always insert before this boundary.

```javascript
var boundary = newContent.indexOf('<!-- /wp:post-content -->');
if (boundary !== -1) {
    var lastSection = newContent.lastIndexOf('<!-- /wp:divi/section -->');
    if (lastSection > boundary) {
        throw new Error('Content exists after post-content boundary — it will not render');
    }
}
```

### 4. Post meta `_et_pb_use_builder` is `"on"`

For Divi SSR to process a page, this post meta must be set. It is automatic for VB-created pages but must be explicitly set for programmatic pages.

```javascript
// Check and set if needed
wp.apiRequest({
    path: '/wp/v2/pages/123',
    method: 'POST',
    data: { meta: { _et_pb_use_builder: 'on' } }
});
```

### Complete validation function

```javascript
function validateContent(content) {
    var errors = [];

    // Section tag balance
    var opens = (content.match(/<!-- wp:divi\/section /g) || []).length;
    var closes = (content.match(/<!-- \/wp:divi\/section -->/g) || []).length;
    if (opens !== closes) {
        errors.push('Section mismatch: ' + opens + ' opens, ' + closes + ' closes');
    }

    // Double comment check
    if ((content.match(/<!--\s*<!--/g) || []).length > 0) {
        errors.push('Double comment pattern detected');
    }

    // Post-content boundary check
    var boundary = content.indexOf('<!-- /wp:post-content -->');
    if (boundary !== -1) {
        var lastSection = content.lastIndexOf('<!-- /wp:divi/section -->');
        if (lastSection > boundary) {
            errors.push('Content after post-content boundary');
        }
    }

    // Sanity: content is not empty or truncated
    if (content.length < 100) {
        errors.push('Content suspiciously short (' + content.length + ' chars)');
    }

    if (errors.length > 0) {
        throw new Error('Validation failed:\n- ' + errors.join('\n- '));
    }
    return true;
}
```

## Quick Diagnostic Table

| Symptom | Cause | Fix |
|---------|-------|-----|
| New content invisible in VB | Created via API, not VB | Use browser automation for new content |
| `wp.apiFetch is not a function` | Wrong API method | Use `wp.apiRequest` |
| All requests hang | Parallel requests | Chain sequentially with `.done()` |
| Content renders blank | After `post-content` boundary | Insert before `<!-- /wp:post-content -->` |
| Sections disappear after save | Double comment bug | Run double-comment safety check before saving |
| Unicode escape sequences visible on page | Wrong encoding | Use `\u003c` not `<` in JSON strings |
| Block JSON extraction finds wrong end | Used regex for `-->` | Use brace-depth parser |
| Page not using Divi builder | Missing post meta | Set `_et_pb_use_builder` to `"on"` |
| Testimonial shows escape sequences | HTML in testimonial innerContent | Use plain text only — testimonials do not render HTML |
| `maxWidth: "900%"` wrong unit | Pre-existing Divi bug | Explicitly set to `"900px"` via REST API |
| Content correct in source, invisible on page | SSR not processing blocks | Verify `_et_pb_use_builder` meta and block structure |
| Inline styles visible after migration | innerContent not decoded before scanning | Decode `\u003c` sequences before processing |

## When Assisting a User

Apply these decision rules when a user asks for help with Divi content:

- **User says "update text on my Divi page"** — Use the REST API modify pattern. Fetch the page, locate the text block by its current content, replace the innerContent value (with proper unicode encoding), validate, and save.

- **User says "add a new section to my page"** — Use browser automation, NOT REST API. New sections created via REST API will be invisible in the Visual Builder. Guide the user through the VB, or use Playwright/Claude in Chrome to automate the VB UI.

- **User says "change colors across all pages"** — REST API batch modify with sequential chaining. Fetch each page, locate the relevant blocks, update the `module.decoration.background` or `module.advanced.text.text` attributes, validate, and save. Use the batch processing pattern with `jQuery.Deferred`.

- **User says "create a landing page programmatically"** — Ask: "Does this content need to be editable in the Visual Builder?" If yes, use browser automation to build the page structure. If the page is auto-generated and never manually edited, REST API creation works for frontend rendering. Make the tradeoff explicit.

- **User says "migrate inline styles to Divi attributes"** — Follow the inline style migration pattern from the [JSON Attribute Map](../internals/json-attribute-map.md): fetch, locate blocks, parse JSON, extract inline CSS, map to block JSON paths, strip inline styles, validate, save.

- **User reports "my page looks blank" after programmatic changes** — Check: (1) Is content after the `post-content` boundary? (2) Is `_et_pb_use_builder` set to `"on"`? (3) Are there double comment patterns? (4) Are section open/close tags balanced?

- **Always ask:** "Does this content need to be editable in the Visual Builder?" The answer determines whether to use REST API (modify existing) or browser automation (create new).

## Related

- [Known Limitations](known-limitations.md) — The 20 rules, including the create-vs-modify rule
- [Visual Builder Operations](visual-builder-ops.md) — VB architecture and UI guidance
- [Block Comment Format](../internals/block-format.md) — Block structure reference
- [JSON Attribute Map](../internals/json-attribute-map.md) — CSS-to-JSON path mapping and brace-depth parser
- [Content Encoding](../internals/content-encoding.md) — Unicode encoding rules
- [SSR Rendering](../internals/ssr-rendering.md) — Post-content boundary and validation rules
- [Hooks & Filters](../api/hooks-filters.md) — Which hooks fire during REST API saves
- [REST API Integration](../api/rest-api.md) — Full REST API reference
