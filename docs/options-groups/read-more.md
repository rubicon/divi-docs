---
title: "Read More Options"
description: "Divi 5 Read More options group — font, size, color, weight, and spacing controls for Read More links in blog feed layouts."
category: options-groups
tags: ["options-groups", "read-more"]
related: ["button", "text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10248771"
---

# Read More Options

Controls the typography and appearance of "Read More" links displayed in blog feed and content listing modules.

!!! abstract "Quick Reference"
    **What it controls:** Font, weight, size, color, alignment, letter spacing, line height, and text shadow for Read More links
    **Where to find it:** Design Tab → Read More
    **Available on:** Blog module
    **Responsive:** Yes — all typography values can be set per breakpoint
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10248771)

## Overview

The Read More options group provides typographic styling for the "Read More" link that appears below post excerpts in feed layouts. This link directs visitors to the full post content and is a key interactive element in any blog listing.

These settings are located in the Design tab of the module settings panel. They offer the standard set of text styling controls: font selection, weight, style, alignment, color, size, letter spacing, line height, and text shadow. This consistency with other typography groups makes it straightforward to create a cohesive design across all text elements.

Styling the Read More link distinctly from body text helps draw attention to the call-to-action. Common approaches include using a contrasting color, bold weight, uppercase text, or increased letter spacing to make the link visually prominent and clearly actionable.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10248771).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Read More Font | Font selector | Selects the typeface for the Read More link, supporting default and custom fonts. |
| Read More Font Weight | Selector | Adjusts the boldness of the Read More text from light to extra-bold. |
| Read More Font Style | Toggle options | Applies italics, capitalization, small caps, underline, or strikethrough to the link text. |
| Read More Text Alignment | Alignment selector | Positions the Read More link as left, center, right, or justified. |
| Read More Text Color | Color picker | Sets the color of the Read More link from the site palette or a custom value. |
| Read More Text Size | Range slider / input | Defines the font size of the Read More link. |
| Read More Letter Spacing | Range slider / input | Controls the spacing between characters in the Read More text. |
| Read More Line Height | Range slider / input | Sets the vertical distance between lines of Read More text. |
| Read More Text Shadow | Shadow editor | Adds a shadow effect with controls for position, blur strength, and shadow color. |

## Which Elements Use This

The Read More options group is used by the Blog module in Divi 5. It styles the "Read More" link that appears below post excerpts in both grid and fullwidth blog layouts.

## Code Examples

```css
/* Style the Read More link */
.et_pb_post .more-link {
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #6c5ce7;
}

.et_pb_post .more-link:hover {
  color: #5a4bd1;
}
```

## Related

- [Button Options](button.md) -- Full button styling controls for module buttons
- [Text Options](text.md) -- General text alignment and shadow settings
