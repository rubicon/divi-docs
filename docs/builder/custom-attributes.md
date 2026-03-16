---
title: "Custom Attributes"
description: "Divi 5 Custom Attributes — add data-*, aria-*, role, and other HTML attributes to any element from the unified Advanced Tab attributes panel."
category: builder
tags: ["builder", "attributes", "accessibility", "html", "data-attributes"]
related: ["semantic-elements", "visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12274853"
---

# Custom Attributes

Add HTML attributes such as `data-*`, `aria-*`, `role`, and others to any Divi element directly from the Visual Builder.

!!! abstract "Quick Reference"
    **What it does:** Attaches arbitrary HTML attributes to any element's DOM node for accessibility, analytics, performance, and JS hooks.
    **Where to find it:** Any element's settings → Advanced Tab → Attributes option group → +Add Attribute.
    **Key features:**

    - Target dropdown to select which DOM node receives the attribute
    - Support for `aria-*`, `data-*`, `role`, `title`, `lang`, and other HTML attributes
    - Legacy CSS Class and CSS ID fields migrated into this unified panel
    - Multiple attributes per element with add/remove controls

    **ET Docs:** [Custom Attributes](https://help.elegantthemes.com/en/articles/12274853){:target="_blank"}

## Overview

Custom Attributes let you attach arbitrary HTML attributes to sections, rows, columns, and modules without writing code. This is essential for accessibility (ARIA labels and roles), analytics tracking (`data-*` attributes), performance hints (`loading`, `rel`), and JavaScript hook points.

The feature consolidates all attribute management into a single panel in the Advanced tab. Legacy CSS Class and CSS ID fields have been migrated into this new system, and all previous attribute-related settings outside of it are deprecated.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12274853).

## Where Custom Attributes Can Be Applied

| Element Type | Supported |
|-------------|-----------|
| Sections | Yes |
| Rows | Yes |
| Columns | Yes |
| Modules | Yes |

## How to Add a Custom Attribute

1. Open the element's settings (click the gear icon or the element itself).
2. Navigate to the **Advanced** tab.
3. Expand the **Attributes** option group.
4. Click **+Add Attribute**.
5. Select the **Target** element (choose which DOM node receives the attribute).
6. Enter the **Attribute name** (e.g., `aria-label`, `data-tracking`, `role`).
7. Enter the **Attribute value** (e.g., `Search Form`, `cta-button`, `navigation`).

Repeat steps 4--7 to add multiple attributes to the same element.

## Settings Reference

### Advanced Tab -- Attributes Option Group

| Setting | Type | Description |
|---------|------|-------------|
| Target | Dropdown | Selects which DOM element within the module receives the attribute |
| Attribute Name | Text input | The HTML attribute identifier (e.g., `data-section`, `aria-label`) |
| Attribute Value | Text input | The value assigned to the attribute |
| +Add Attribute | Button | Adds a new attribute row |
| Remove | Button | Deletes an existing attribute row |

## Common Attribute Categories

| Category | Example Attributes | Purpose |
|----------|-------------------|---------|
| Accessibility | `aria-label`, `aria-describedby`, `role` | Provide context to screen readers and assistive technologies |
| Data tracking | `data-tracking`, `data-event`, `data-category` | Hook into analytics tools (Google Tag Manager, Plausible, etc.) |
| Performance | `loading="lazy"`, `rel="noopener"`, `fetchpriority` | Control resource loading behavior |
| JavaScript hooks | `data-action`, `data-target`, `id` | Provide selectors for custom scripts |
| Native HTML | `title`, `lang`, `dir` | Standard HTML metadata on individual elements |

## Legacy Migration

Previous versions of Divi used separate CSS Class and CSS ID fields scattered across module settings. In Divi 5, these have been automatically migrated into the Attributes option group. If you open a page built in an earlier version, you will find those values already present as attributes.

All other attribute-related settings outside the Attributes group are deprecated.

## Tips and Best Practices

- **Use `aria-label` with semantic elements.** Pairing a `nav` semantic tag with `aria-label="Main Navigation"` gives screen readers a clear landmark name.
- **Keep `data-*` attribute names lowercase and hyphenated.** This follows the HTML5 spec and avoids issues with JavaScript `dataset` access.
- **Select the correct target.** Some modules render multiple DOM nodes (e.g., an outer wrapper and an inner element). Use the Target dropdown to place the attribute on the right node.
- **Do not duplicate native attributes.** Adding a `class` attribute will not merge with Divi's built-in classes -- it may override them. Use the dedicated CSS Class attribute for class additions.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The unified Attributes panel is new to Divi 5.

## Troubleshooting

!!! warning "Feature Not Available"
    If the Attributes option group is not visible in the Advanced tab, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.

- **Attribute not appearing in the rendered HTML.** Check that you selected the correct Target element. Some modules have multiple DOM nodes and the attribute may be on an inner element rather than the outer wrapper.
- **Legacy class or ID missing after migration.** Open the Attributes group -- the values should appear there. If not, re-add them manually.
- **JavaScript cannot find the data attribute.** Ensure the attribute name uses lowercase letters and hyphens only. Access it in JS via `element.dataset.yourName`.

## Related

- [Semantic Elements](semantic-elements.md)
- [Visual Builder](visual-builder.md)
