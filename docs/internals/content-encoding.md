---
title: "Content Encoding"
description: "Divi 5 content encoding internals — unicode escape rules for HTML inside block JSON attributes, including text block encoding and testimonial exceptions."
category: internals
tags: [encoding, unicode, html, json, content]
related: [block-format, ssr-rendering]
divi_version: "5.x"
last_updated: 2026-03-12
---

# Content Encoding

Unicode encoding rules for HTML content inside Divi 5 block JSON attributes.

!!! abstract "Quick Reference"
    **What this documents:** How HTML content must be encoded inside Divi 5 block JSON attributes using literal unicode escape strings.
    **Key data structures:** `\u003c` (`<`), `\u003e` (`>`), `\u0022` (`"`) — literal 6-character escape strings in `content.innerContent` values.
    **Last verified:** 2026-03-12

## Text Block Encoding

HTML content inside Divi text blocks MUST use literal 6-character unicode escape strings in the JSON — NOT JavaScript unicode escapes. These map to:

| Escape | Character | Usage |
|--------|-----------|-------|
| `\u003c` | `<` | Opening HTML tags |
| `\u003e` | `>` | Closing HTML tags |
| `\u0022` | `"` | Attribute quotes |

### Correct Encoding

```json
"content": {
  "innerContent": {
    "desktop": {
      "value": "\\u003ch2\\u003eHeading Text\\u003c/h2\\u003e\\u003cp\\u003eParagraph content here.\\u003c/p\\u003e"
    }
  }
}
```

This renders as:
```html
<h2>Heading Text</h2><p>Paragraph content here.</p>
```

## Testimonial Block Exception

Unlike text blocks, testimonial `innerContent` renders as **plain text, not HTML**. Appending unicode-encoded HTML tags results in literal escape sequences displayed on the page. See [Testimonial Rendering Gaps](testimonial-ssr.md).

## Related

- [Block Comment Format](block-format.md)
- [SSR Rendering](ssr-rendering.md)
- [Testimonial Rendering Gaps](testimonial-ssr.md)
