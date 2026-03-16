---
title: "Text Module"
category: modules
tags: [text, content-modules, rich-text, wysiwyg, paragraphs, headings, html]
related: [blurb, code, button]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10365197-the-text-module-in-divi-5"
---

# Text Module

The Text module is Divi's primary content block, providing a rich text editor for adding paragraphs, headings, lists, links, and inline HTML to any page.

## Overview

The Text module is the most fundamental building block in the Divi module library. It wraps a full-featured visual text editor inside a Divi module container, giving you the ability to write and format content using familiar word-processing controls while retaining access to Divi's design system for typography, spacing, and animation.

Unlike more specialized modules such as Blurb or Call to Action, the Text module imposes no structural constraints on your content. You can write a single heading, a multi-paragraph article, an HTML embed, or a combination of all three. This flexibility makes it the default choice for any content that does not require the predefined layout of a dedicated module.

The module supports both the visual editor mode and a raw text/HTML mode, allowing advanced users to paste custom markup directly. Typography controls are split between general text settings, heading-specific settings, and body-specific settings, giving you granular control over every typographic element within the module.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10365197-the-text-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/text/)

![Text module](../assets/screenshots/modules/text/element.png){ loading=lazy }
*The Text module as it appears on the live demo.*

## Use Cases

1. **Long-Form Content Sections** — Use the Text module for article-style content within Divi layouts. Set a max-width of 700-800px and center the module to create an optimal reading experience with comfortable line lengths.

2. **HTML Embeds and Custom Markup** — The Text module accepts raw HTML in its editor, making it useful for embedding third-party widgets, custom forms, iframes, or script-based content that lacks a dedicated Divi module.

3. **Styled Typographic Elements** — Combine headings, body text, and lists within a single module and apply distinct typography settings to each. Use the heading typography controls to create visual hierarchy without needing separate heading and paragraph modules.

## How to Add the Text Module

1. **Open the Visual Builder** on the page where you want to add text content. Click the gray plus icon inside any row to open the module picker.

2. **Search for "Text"** in the module picker search bar, then click the Text module to insert it into the row.

3. **Enter your content** using the visual editor or switch to the text/HTML view for raw markup. Adjust typography, spacing, and design settings through the Design tab.

## Settings & Options

### Content Tab

The Content tab contains the text editor and structural controls for the module.

| Setting | Type | Description |
|---------|------|-------------|
| **Text** | | |
| Body | rich text | The main content area with a visual editor supporting paragraphs, headings, lists, links, images, and raw HTML |
| **Link** | | |
| Module Link URL | url | Makes the entire module a clickable link to the specified destination |
| Module Link Target | select | Opens the link in the same window or a new tab |
| **Background** | | |
| Background Color | color | Solid background color applied behind the module |
| Background Gradient | gradient | Gradient background with direction and color stop controls |
| Background Image | upload | An image displayed behind the module content |
| Background Video | url | A video URL (MP4 or WebM) used as a motion background |
| Background Pattern | select | A decorative pattern overlay applied to the background |
| Background Mask | select | A shaped mask overlay applied to the background |
| **Loop** | | |
| Dynamic Content | toggle | Enable dynamic content connections for supported fields |
| **Order** | | |
| Module Order | select | Position of this module relative to siblings in the row |
| **Meta** | | |
| Admin Label | text | A custom label shown in the builder layers panel for easy identification |
| Disable On | toggle | Disable the module on specific device sizes (phone, tablet, desktop) |

### Design Tab

The Design tab provides typography, sizing, and visual styling controls for all text elements within the module.

| Setting | Type | Description |
|---------|------|-------------|
| **Text** | | |
| Text Alignment | select | Horizontal alignment for all content (left, center, right, justified) |
| Text Color Scheme | select | Light or dark text color scheme for the module |
| **Heading Text** | | |
| Heading Font | typography | Font family, weight, style, and line height for heading tags (H1-H6) |
| Heading Text Color | color | Font color for all heading elements |
| Heading Text Size | range | Font size for heading elements |
| Heading Letter Spacing | range | Letter spacing for heading text |
| Heading Line Height | range | Line height for heading elements |
| Heading Text Shadow | composite | Shadow effect applied to heading text |
| **Body Text** | | |
| Body Font | typography | Font family, weight, style, and line height for paragraph text |
| Body Text Color | color | Font color for body paragraph text |
| Body Text Size | range | Font size for body text |
| Body Letter Spacing | range | Letter spacing for body text |
| Body Line Height | range | Line height for body text |
| Body Text Shadow | composite | Shadow effect applied to body text |
| Link Color | color | Color applied to hyperlinks within the module |
| Unordered List Font | typography | Font settings for unordered list items |
| Ordered List Font | typography | Font settings for ordered list items |
| Block Quote Font | typography | Font settings for blockquote elements |
| **Sizing** | | |
| Width | range | The overall width of the module |
| Max Width | range | Maximum width the module can expand to |
| Module Alignment | select | Horizontal alignment of the module within its column |
| Min Height | range | Minimum height of the module container |
| Height | range | Fixed height of the module container |
| Max Height | range | Maximum height the module container can reach |
| **Spacing** | | |
| Margin | composite | External spacing around the module (top, right, bottom, left) |
| Padding | composite | Internal spacing within the module (top, right, bottom, left) |
| **Border** | | |
| Border Width | range | Width of the border around the module |
| Border Color | color | Color of the module border |
| Border Style | select | Style of the border (solid, dashed, dotted, double, groove, ridge) |
| Border Radius | range | Corner rounding applied to the module container |
| **Box Shadow** | | |
| Box Shadow | composite | Shadow effect applied to the module container |
| **Filters** | | |
| Hue Rotate | range | Rotates the hue of all module colors |
| Saturate | range | Adjusts color saturation of the module |
| Brightness | range | Adjusts brightness of the module |
| Contrast | range | Adjusts contrast of the module |
| Invert | range | Inverts the module colors |
| Sepia | range | Applies a sepia tone to the module |
| Opacity | range | Controls the transparency of the module |
| Blur | range | Applies a Gaussian blur to the module |
| Blend Mode | select | CSS mix-blend-mode for how the module blends with its background |
| **Transform** | | |
| Scale | composite | Scale the module horizontally and vertically |
| Translate | composite | Move the module along the X and Y axes |
| Rotate | composite | Rotate the module on the X, Y, and Z axes |
| Skew | composite | Skew the module horizontally and vertically |
| Transform Origin | select | The point around which transformations are applied |
| **Animation** | | |
| Animation Style | select | Entrance animation type (fade, slide, bounce, zoom, flip, fold, roll) |
| Animation Direction | select | Direction from which the animation enters |
| Animation Duration | range | How long the entrance animation takes in milliseconds |
| Animation Delay | range | Delay before the animation starts |
| Animation Intensity | range | The distance or intensity of the animation movement |
| Animation Starting Opacity | range | The opacity value at the start of the animation |
| Animation Speed Curve | select | Easing function for the animation (ease, ease-in, ease-out, linear) |
| Animation Repeat | toggle | Whether the animation replays each time the element enters the viewport |

### Advanced Tab

The Advanced tab provides technical controls for custom attributes, CSS overrides, conditional display logic, and scroll-based effects.

| Setting | Type | Description |
|---------|------|-------------|
| **Attributes** | | |
| CSS ID | text | A unique HTML `id` attribute applied to the module wrapper |
| CSS Class | text | One or more CSS class names added to the module wrapper |
| **CSS** | | |
| Before | code | Custom CSS applied to the module's `::before` pseudo-element |
| Main Element | code | Custom CSS applied to the main module container |
| After | code | Custom CSS applied to the module's `::after` pseudo-element |
| Text | code | Custom CSS targeting the inner text container |
| **HTML** | | |
| Custom Attributes | text | Additional HTML attributes added to the module element (e.g., `data-*` attributes) |
| **Conditions** | | |
| Display Conditions | composite | Rules that determine when the module is shown (logged-in status, date range, page type, etc.) |
| **Interactions** | | |
| Cursor Style | select | Custom cursor appearance when hovering over the module |
| **Visibility** | | |
| Disable On | toggle | Hide the module on desktop, tablet, or phone screen sizes |
| Overflow X | select | Horizontal overflow behavior (visible, hidden, scroll, auto) |
| Overflow Y | select | Vertical overflow behavior (visible, hidden, scroll, auto) |
| **Transitions** | | |
| Transition Duration | range | Duration of hover and state change transitions |
| Transition Delay | range | Delay before transition effects begin |
| Transition Speed Curve | select | Easing curve for transition animations |
| **Position** | | |
| Position | select | CSS position type (static, relative, absolute, fixed, sticky) |
| Z Index | number | Stack order of the module relative to other elements |
| Horizontal Offset | range | Left or right offset for positioned elements |
| Vertical Offset | range | Top or bottom offset for positioned elements |
| **Scroll Effects** | | |
| Vertical Motion | composite | Moves the module vertically as the user scrolls |
| Horizontal Motion | composite | Moves the module horizontally as the user scrolls |
| Fade In and Out | composite | Fades the module in or out based on scroll position |
| Scaling Up and Down | composite | Scales the module based on scroll position |
| Rotating | composite | Rotates the module as the user scrolls |
| Blur | composite | Applies a progressive blur based on scroll position |

## Code Examples

### Custom CSS

```css
/* Constrain line length for readability */
.et_pb_text_inner {
    max-width: 65ch;
}

/* Style the first paragraph as a lead-in */
.et_pb_text_inner p:first-of-type {
    font-size: 1.2em;
    font-weight: 500;
    line-height: 1.6;
}

/* Custom unordered list styling with arrow markers */
.et_pb_text_inner ul li {
    padding-left: 1.5em;
    position: relative;
    list-style: none;
}
.et_pb_text_inner ul li::before {
    content: "\2192";
    position: absolute;
    left: 0;
}

/* Styled blockquote */
.et_pb_text_inner blockquote {
    border-left: 4px solid #2ea3f2;
    padding-left: 20px;
    margin: 24px 0;
    font-style: italic;
    color: #666;
}

/* Responsive font size reduction */
@media (max-width: 767px) {
    .et_pb_text_inner {
        font-size: 15px;
    }
}
```

### PHP Hooks

```php
/**
 * Automatically add target="_blank" and rel="noopener" to external links
 * within Text modules.
 */
function divi_text_external_links( $output, $render_slug ) {
    if ( 'et_pb_text' !== $render_slug ) {
        return $output;
    }

    $site_url = preg_quote( home_url(), '/' );

    $output = preg_replace_callback(
        '/<a\s+([^>]*?)href="(https?:\/\/(?!' . $site_url . ')[^"]*)"([^>]*?)>/i',
        function ( $matches ) {
            $before = $matches[1];
            $href   = $matches[2];
            $after  = $matches[3];

            if ( strpos( $matches[0], 'target=' ) === false ) {
                return '<a ' . $before . 'href="' . $href . '"' . $after . ' target="_blank" rel="noopener">';
            }
            return $matches[0];
        },
        $output
    );

    return $output;
}
add_filter( 'et_module_shortcode_output', 'divi_text_external_links', 10, 2 );
```

## Common Patterns

1. **Readable Article Layout** — Place the Text module in a row with a single column, set the module max-width to 750px, and center-align it. This constrains line length for comfortable reading and mirrors the layout conventions of modern editorial websites.

2. **Two-Column Text Blocks** — Use two Text modules in a two-column row to create side-by-side content areas. This works well for comparing features, presenting before/after scenarios, or splitting an introduction from a detail list.

3. **Inline HTML Embeds** — Switch to the text/HTML editing mode to paste embed codes for third-party services such as forms, maps, or social feeds. The Text module renders arbitrary HTML on the front end, making it a versatile fallback when no dedicated module exists for the content you need.

## Saving Your Work

After editing your Text module content and design, click the green checkmark at the bottom of the settings panel to apply the changes. Save the page using the purple save button in the bottom dock of the Visual Builder, or use the keyboard shortcut `Ctrl + S` (Windows) or `Cmd + S` (Mac). If you plan to reuse the same text block configuration across multiple pages, save it to the Divi Library for quick access.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The inner wrapper class structure and CSS selectors may differ from Divi 4. Verify custom CSS selectors using your browser inspector when migrating styles from earlier versions.

## Troubleshooting

!!! warning "Content Disappearing in the Visual Builder"
    If text content disappears while editing in the Visual Builder, check for unclosed HTML tags in the content body. The Visual Builder's parser is stricter than the front-end renderer and will drop content that follows malformed markup. Switch to the text/HTML view to inspect and fix any unclosed tags.

!!! warning "Typography Settings Not Applying"
    Divi's typography settings rely on CSS specificity to override theme defaults. If your font, size, or color changes are not visible on the front end:

    - Confirm you are editing the correct typography group (Heading Text vs. Body Text)
    - Check for conflicting styles from child themes or third-party plugins with higher specificity
    - Clear all caching layers (plugin cache, server cache, browser cache) and reload

!!! warning "Dynamic Content Not Rendering"
    If dynamic content placeholders show raw tokens instead of resolved values:

    - Verify that the dynamic content source (custom field, post meta, etc.) contains data for the current post
    - Ensure the Loop settings are correctly configured if pulling data from a query
    - Check that the field name matches exactly, including case sensitivity

## Related

- [Blurb Module](blurb.md) — pairs text content with an icon or image for feature blocks
- [Code Module](code.md) — for raw HTML, CSS, and JavaScript that should not be processed by the visual editor
- [Button Module](button.md) — adds a styled call-to-action button linked to any URL
