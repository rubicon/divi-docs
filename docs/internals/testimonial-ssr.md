---
title: "Testimonial Rendering Gaps"
category: internals
tags: [testimonial, ssr, bugs, author, rendering]
related: [ssr-rendering, content-encoding]
divi_version: "5.x"
last_updated: 2026-03-12
---

# Testimonial Rendering Gaps

Known SSR bugs in the Divi 5 testimonial module.

## Author and JobTitle Fields Not Rendered

The `wp:divi/testimonial` block supports `content.author` and `content.jobTitle` fields in JSON:

```json
{
  "content": {
    "author": {"desktop": {"value": "John Smith"}},
    "jobTitle": {"desktop": {"value": "CEO, Acme Corp"}},
    "innerContent": {"desktop": {"value": "Testimonial text here..."}}
  }
}
```

SSR renders ONLY the `innerContent` field. The `author` and `jobTitle` values exist in the JSON but produce no HTML output — no `<cite>`, `<span>`, or any other element.

## innerContent Is Plain Text, Not HTML

Unlike text blocks (which use unicode-encoded HTML), testimonial `innerContent` renders as plain text. Unicode-encoded HTML tags produce literal escape sequences on the page:

```
// Renders as visible text on the page:
\u003cp style=\u0022font-weight:bold\u0022\u003eJohn Smith\u003c/p\u003e
```

## Workaround

Append author attribution as plain text with an em dash:

```json
"innerContent": {
  "desktop": {
    "value": "Great service and professional team.\n\n— John Smith, CEO, Acme Corp"
  }
}
```

Renders as:
> Great service and professional team.
>
> — John Smith, CEO, Acme Corp

## Related

- [SSR Rendering](ssr-rendering.md) — broader SSR behavior and boundaries
- [Content Encoding](content-encoding.md) — encoding rules that work for text blocks but not testimonials
