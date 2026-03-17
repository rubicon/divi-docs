---
title: "Divi 5 Internals"
description: "Divi 5 internals documentation — block comment format, SSR rendering, content encoding, Visual Builder architecture, TinyMCE state sync, and JSON attributes."
category: internals
tags: [internals, architecture, ssr, block-format, developer]
last_updated: 2026-03-12
---

# Divi 5 Internals

Under-the-hood documentation of how Divi 5 actually works — block format, SSR rendering, state management, and the gaps between documented and actual behavior.

!!! abstract "Quick Reference"
    **What this section covers:** Reverse-engineered internals of Divi 5 — how content is stored, rendered, and managed by the Visual Builder.
    **Topics:** Block Comment Format | SSR Rendering | Content Encoding | VB Architecture | TinyMCE State Sync | JSON Attribute Map | Library Import JSON | Testimonial SSR Gaps
    **Source:** Production testing and reverse engineering, not official Elegant Themes documentation.

This section documents things Elegant Themes hasn't documented publicly. It's based on production testing and reverse engineering, not official sources. Treat it as accurate-as-of-the-date-written but subject to change as Divi 5 matures.

## Sections

| Topic | Description | Status |
|-------|-------------|--------|
| [Block Comment Format](block-format.md) | How Divi 5 stores content as WordPress block comments | ✅ Documented |
| [SSR Rendering](ssr-rendering.md) | Server-side rendering behavior, boundaries, and gaps | ✅ Documented |
| [Content Encoding](content-encoding.md) | Unicode encoding rules for HTML in block JSON | ✅ Documented |
| [Visual Builder Architecture](vb-architecture.md) | Dual-frame structure, React state, global objects, data registry | ✅ Documented |
| [TinyMCE State Sync](tinymce-state.md) | How the text editor syncs (and doesn't sync) with Divi's save state | ✅ Documented |
| [JSON Attribute Map](json-attribute-map.md) | CSS-to-JSON path mapping, brace-depth parser, style migration patterns | ✅ Documented |
| [Library Import JSON](library-import-json.md) | Global Variables, Presets, Theme Builder, Customizer, and layout JSON structure | ✅ Documented |
| [Style Guide to Divi Variables Design](style-guide-to-divi-variables-design.md) | Design spec: generating Divi 5 Global Variables JSON from style guides or tokens | ✅ Documented |
| [Testimonial Rendering Gaps](testimonial-ssr.md) | Known SSR bugs in the testimonial module | ✅ Documented |
