---
title: "Text Module"
category: modules
tags: [text, content-modules, rich-text, wysiwyg]
related: [blurb, blog]
divi_version: "5.x"
last_updated: 2026-03-12
---

# Text Module

The Text module is Divi's core content block — a rich text editor for adding paragraphs, headings, lists, links, and inline media to your pages.

## Overview

The Text module wraps the standard WordPress visual editor (TinyMCE / block editor content) inside a Divi module container. It's the go-to module for any content that doesn't fit a more specialized module like Blurb or Call to Action.

Unlike the WordPress block editor's paragraph block, the Divi Text module gives you full control over typography, spacing, and animation through the Divi design interface while still supporting raw HTML in the text tab.

## Settings & Options

### Content Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Body | rich text | none | The main content area — supports visual editing and HTML |

### Design Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Text Font | typography | default | Font family, weight, style, and line height for body text |
| Text Color | color | theme default | Body text color |
| Text Size | range | theme default | Body text font size |
| Link Color | color | theme accent | Color for hyperlinks |
| Heading Font | typography | default | Applies to all heading tags (h1–h6) within the module |
| Heading Color | color | theme default | Color for heading tags |
| Ul/Ol Styling | typography | default | List item typography |
| Text Alignment | select | Left | `Left`, `Center`, `Right`, `Justified` |
| Max Width | range | 100% | Maximum width of the text container |

### Advanced Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| CSS ID | text | none | Custom HTML id attribute |
| CSS Class | text | none | Custom CSS class(es) |
| Custom CSS | code | none | Target `.et_pb_text_inner` and child elements |

## Code Examples

### Styling text module content

```css
/* Constrain line length for readability */
.et_pb_text_inner {
    max-width: 65ch;
}

/* Style the first paragraph differently */
.et_pb_text_inner p:first-of-type {
    font-size: 1.2em;
    font-weight: 500;
}

/* Custom list styling */
.et_pb_text_inner ul li {
    padding-left: 1em;
    position: relative;
}
.et_pb_text_inner ul li::before {
    content: "→";
    position: absolute;
    left: 0;
}
```

### Filtering text module output

```php
/**
 * Automatically add target="_blank" to external links in Text modules.
 */
function my_external_links_blank( $output, $render_slug ) {
    if ( 'et_pb_text' === $render_slug ) {
        $output = preg_replace_callback(
            '/<a\s+(.*?)href="(https?:\/\/(?!' . preg_quote( home_url(), '/' ) . ').*?)"(.*?)>/i',
            function ( $matches ) {
                if ( strpos( $matches[0], 'target=' ) === false ) {
                    return '<a ' . $matches[1] . 'href="' . $matches[2] . '"' . $matches[3] . ' target="_blank" rel="noopener">';
                }
                return $matches[0];
            },
            $output
        );
    }
    return $output;
}
add_filter( 'et_module_shortcode_output', 'my_external_links_blank', 10, 2 );
```

## Common Patterns

### Long-form content sections

Use the Text module for article-style content within Divi layouts. Set a max-width of 700–800px and center the module for optimal reading experience.

### HTML embeds

The Text module accepts raw HTML in its text editor, making it a common workaround for embedding third-party widgets, custom forms, or scripts that don't have a dedicated Divi module.

### Styled pull quotes

Combine a Text module with a custom CSS class to create pull quotes or callout blocks within longer content sections.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The inner wrapper class structure may differ from earlier Divi versions. Verify custom CSS selectors accordingly.

## Troubleshooting

!!! warning "Content disappearing in Visual Builder"
    If text content disappears when editing in the Visual Builder, check for unclosed HTML tags in the content. The Visual Builder's parser is stricter than the front-end renderer.

!!! warning "Typography settings not applying"
    Divi's typography settings use CSS specificity to override theme defaults. If your font settings aren't showing, check for conflicting styles from child themes or plugins with higher specificity.

## Related

- [Blurb Module](blurb.md) — for content paired with an icon or image
- [Blog Module](blog.md) — for displaying post content dynamically
