---
title: "Semantic Elements"
description: "Divi 5 Semantic Elements — assign HTML5 tags (nav, header, footer, article) and inject custom HTML wrappers for accessibility and SEO."
category: builder
tags: ["builder", "semantic", "html", "accessibility", "seo"]
related: ["custom-attributes", "visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13284097"
---

# Semantic Elements

Assign meaningful HTML tags and inject custom HTML wrappers on any Divi element to improve accessibility and SEO.

!!! abstract "Quick Reference"
    **What it does:** Replaces generic `div` tags with semantic HTML5 elements and allows custom HTML injection before/after any element.
    **Where to find it:** Any element's settings → Advanced Tab → HTML option group → Element Type.
    **Key features:**

    - Swap element tags to `nav`, `header`, `footer`, `section`, `article`, or `button`
    - HTML Before/After fields for injecting custom wrappers or tracking code
    - No visual change to the element — only the underlying HTML changes
    - Improves screen reader navigation and search engine understanding

    **ET Docs:** [Semantic Elements](https://help.elegantthemes.com/en/articles/13284097){:target="_blank"}

## Overview

Semantic HTML communicates the purpose of each section of a page to browsers, screen readers, and search-engine crawlers. By default, Divi renders its layout containers as generic `div` elements. The Semantic Elements feature lets you replace those generic tags with proper HTML5 elements such as `nav`, `header`, `footer`, `article`, `section`, and `button` -- all without changing the visual design.

In addition to tag reassignment, you can inject arbitrary HTML before and after any element. This effectively gives every module two built-in Code-module slots, useful for wrapping content in custom markup or adding helper code that needs to sit adjacent to the element in the DOM.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13284097).

## Available Semantic Tags

| Tag | Typical Use | Example |
|-----|-------------|---------|
| `nav` | Primary or secondary navigation blocks | Wrapping a Menu module |
| `header` | Introductory content or a group of navigational aids | Page hero area |
| `footer` | Footer content for a section or the page | Bottom-of-page info row |
| `section` | Thematic grouping of content | A distinct content band |
| `article` | Self-contained composition | Blog post or product card |
| `button` | Interactive control | CTA element that should be a real button |

## How to Set the Element Type

1. Click the element (section, row, column, or module) to open its settings.
2. Navigate to the **Advanced** tab.
3. Expand the **HTML** option group.
4. Open the **Element Type** dropdown and choose the desired semantic tag.
5. Save settings.

The visual appearance of the element does not change; only the underlying HTML tag is swapped.

## Settings Reference

### Advanced Tab -- HTML Option Group

| Setting | Type | Description |
|---------|------|-------------|
| Element Type | Dropdown | Choose the semantic HTML tag (`nav`, `section`, `header`, `article`, `footer`, `button`) |
| HTML Before Element | Text area | Raw HTML injected immediately before the element in the DOM |
| HTML After Element | Text area | Raw HTML injected immediately after the element in the DOM |

## Custom HTML Wrappers

The **HTML Before Element** and **HTML After Element** fields accept any valid HTML. Common uses include:

- Opening and closing a custom wrapper `div` with specific classes or ARIA roles.
- Adding `<a>` link wrappers around an element for card-style click targets.
- Inserting tracking pixels or script hooks adjacent to a module.

Because the HTML is injected directly into the rendered output, you can pair an opening tag in the "before" field with its matching closing tag in the "after" field to wrap the entire element.

## Use Cases

| Scenario | Tag | Benefit |
|----------|-----|---------|
| Menu module used as main navigation | `nav` | Screen readers identify it as navigation |
| Hero section at top of page | `header` | Crawlers understand the page introduction |
| Blog post content area | `article` | Machines can extract the primary content |
| Call-to-action element | `button` | Assistive technology announces it as interactive |
| Thematic content band | `section` | Provides document outline structure |

## Tips and Best Practices

- **Do not nest landmarks improperly.** A `nav` inside another `nav` is rarely correct; plan your semantic structure before applying tags.
- **Use HTML wrappers sparingly.** They are powerful but can introduce unclosed-tag bugs if the before/after fields are mismatched.
- **Test with a screen reader** (VoiceOver, NVDA) after applying semantic tags to confirm the reading order makes sense.
- **Combine with custom attributes.** Add `aria-label` values via the [Custom Attributes](custom-attributes.md) feature to further enhance accessibility.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If the HTML option group is not visible in the Advanced tab, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.

- **Layout breaks after adding a semantic tag.** The tag change itself should not affect layout. Check the HTML Before/After fields for unclosed or malformed markup.
- **Screen reader does not announce the landmark.** Some tags (like `section`) only become landmarks when paired with an `aria-label`. Add one via Custom Attributes.

## Related

- [Custom Attributes](custom-attributes.md)
- [Visual Builder](visual-builder.md)
