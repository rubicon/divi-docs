---
title: "Divi API Reference"
description: "Divi 5 API reference — developer documentation for PHP hooks, filter hooks, JavaScript events, custom module development, REST API integration, block JSON schema, and CLI tools."
category: api
tags: [api, hooks, filters, javascript, rest-api, modules, development]
divi_version: "5.x"
last_updated: 2026-03-16
---

# Divi API Reference

Developer documentation for extending, automating, and integrating with Divi 5.

!!! abstract "Quick Reference"
    **What this section covers:** Developer-facing documentation for extending Divi 5 — PHP hooks and filters, JavaScript events and the Builder API, custom module development, REST API integration, block JSON schema, and command-line tools.
    **Key PHP entry points:** `et_builder_ready` (register modules), `et_module_shortcode_output` (filter output), `et_save_post` (post-save logic)
    **Key JS entry points:** `et_builder_api_ready` (Builder API), `window.divi.data.select('divi/edit-post')` (read-only state)
    **Key REST endpoint:** `GET/POST /wp-json/wp/v2/pages/{id}?context=edit` (read/modify Divi content)

## Section Overview

The API Reference is for WordPress developers who want to extend Divi with custom modules, modify existing module behavior, manipulate Divi content programmatically, or build integrations (including AI-driven workflows). Each page documents a specific API surface with code examples, data structures, and known limitations.

These are reference docs — technical, precise, and code-heavy. For operational guides aimed at AI assistants, see the [Playbooks](../playbooks/index.md) section. For architecture internals, see the [Internals](../internals/index.md) section.

## Pages

| Page | What It Covers | Status |
|------|---------------|--------|
| [Hooks & Filters](hooks-filters.md) | PHP action/filter hooks and JS events | ✅ Complete |
| [Custom Modules](custom-modules.md) | Building custom Divi 5 modules | ✅ Complete |
| [REST API Integration](rest-api.md) | Reading and modifying Divi content via WP REST API | ✅ New |
| [Block JSON Reference](block-json-reference.md) | Block JSON attribute schema and module-specific structures | ✅ New |
| [JavaScript API](javascript-api.md) | Complete Builder JS API reference | ✅ New |
| [Divi Data Registry](divi-data-registry.md) | Read-only access to VB module state | ✅ New |
| [Module JSON Schema](module-json-schema.md) | module.json configuration schema | ✅ New |
| [Module Rendering Lifecycle](module-lifecycle.md) | Module lifecycle from registration to rendered output | ✅ New |
| [WP-CLI Integration](wp-cli.md) | Command-line operations for Divi content | ✅ New |

## Where to Start

Choose a path based on what you're building:

### Extending Divi with new modules

Start with [Custom Modules](custom-modules.md) for the end-to-end module development workflow. Reference [Module JSON Schema](module-json-schema.md) for the `module.json` configuration file that defines your module's settings, and [Module Rendering Lifecycle](module-lifecycle.md) to understand how your module moves from registration through server-side rendering to Visual Builder preview.

### Manipulating Divi content programmatically

Start with [REST API Integration](rest-api.md) to learn how to read and modify existing Divi page content through the WordPress REST API. Use [Block JSON Reference](block-json-reference.md) to understand the JSON attribute structure inside each block comment. For bulk operations or CI/CD workflows, see [WP-CLI Integration](wp-cli.md).

### Building AI integrations

Start with [REST API Integration](rest-api.md) for the programmatic content modification pattern, then [Block JSON Reference](block-json-reference.md) for the data structures you'll be reading and writing. Use [Divi Data Registry](divi-data-registry.md) for read-only access to module state inside the Visual Builder. Review the [Known Limitations](../playbooks/known-limitations.md) playbook before writing any automation code — it documents the create-vs-modify rule and other critical constraints.

### Customizing existing module behavior

Start with [Hooks & Filters](hooks-filters.md) for the complete PHP and JavaScript hook reference. Use [JavaScript API](javascript-api.md) for the full Builder API object documentation, including `API.Modules`, `API.Utils`, and event handling.

## Cross-References

The API Reference documents the *interfaces* for extending Divi. For the underlying architecture and data formats, see:

- **[Internals](../internals/index.md)** — Block comment format, JSON attribute map, content encoding rules, SSR rendering pipeline
- **[Playbooks](../playbooks/index.md)** — Operational guides for AI assistants: [REST API Content Management](../playbooks/rest-api-content.md), [Known Limitations](../playbooks/known-limitations.md), [Visual Builder Operations](../playbooks/visual-builder-ops.md)
- **[CSS Reference](../css-reference/index.md)** — Class names, selectors, and CSS override patterns for styling Divi output

## Related

- [Internals](../internals/index.md)
- [Playbooks](../playbooks/index.md)
- [CSS Reference](../css-reference/index.md)
