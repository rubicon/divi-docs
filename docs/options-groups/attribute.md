---
title: "Attribute Options"
description: "Divi 5 Attribute options group — rel attribute values (nofollow, noopener, noreferrer) for button link SEO and security control."
category: options-groups
tags: ["options-groups", "attribute"]
related: ["attributes", "css"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10259880"
---

# Attribute Options

Defines the link relationship attributes for button elements, controlling SEO, security, and navigation behavior.

!!! abstract "Quick Reference"
    **What it controls:** Button rel attribute values (nofollow, noopener, noreferrer, external, bookmark)
    **Where to find it:** Advanced Tab → Attribute
    **Available on:** Modules with button elements (Button, CTA, and others with configurable link relationships)
    **Responsive:** No — link attributes are static across all breakpoints
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10259880)

## Overview

The Attribute options group provides a setting for specifying the `rel` attribute values on button links. The `rel` attribute describes the relationship between the current page and the linked destination, which affects how search engines interpret the link, how browsers handle security, and how referrer information is transmitted.

This setting is found in the Advanced tab of the module settings panel. It lets you apply one or more relationship values to a button link. Each value serves a specific purpose: `nofollow` prevents search engines from passing link equity, `noopener` closes a security vulnerability when opening links in new tabs, `noreferrer` prevents the destination page from seeing where the visitor came from, and `external` signals that the link points to a different website.

Proper use of link relationship attributes is important for SEO hygiene and security best practices. For external links, combining `noopener` and `noreferrer` is recommended as a standard security measure. The `nofollow` attribute should be applied to sponsored, paid, or user-generated links to comply with search engine guidelines.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10259880).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Button Relationship | Multi-select / dropdown | Specifies one or more `rel` attribute values for the button link. Available values: `bookmark` (anchor within the site), `external` (link to another website), `nofollow` (instructs search engines not to follow the link), `noreferrer` (prevents referrer information from being sent), `noopener` (prevents the linked page from accessing `window.opener` for security). |

## Which Elements Use This

The Attribute options group is used by modules that render button or link elements with configurable relationship attributes. This includes the Button module and other modules with button components accessible through the Advanced tab.

## Code Examples

```html
<!-- Example output with multiple rel values -->
<a href="https://example.com" rel="nofollow noopener noreferrer" target="_blank">
  Visit Example
</a>
```

```css
/* Style external links differently */
a[rel~="external"]::after {
  content: " \2197"; /* Arrow icon */
  font-size: 0.8em;
}
```

## Related

- [Attributes Options](attributes.md) -- CSS ID, classes, and custom HTML attributes
- [CSS Options](css.md) -- Custom CSS targeting specific element areas
