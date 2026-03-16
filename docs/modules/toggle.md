---
title: "Toggle Module"
category: modules
tags: [toggle, accordion, collapsible, faq, expandable-content, content-modules]
related: [accordion, tabs]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10368052-the-toggle-module-in-divi-5"
---

# Toggle Module

The Toggle module creates a collapsible content panel that visitors can expand or collapse by clicking its title bar.

## Overview

The Toggle module provides a simple show/hide interaction for content sections. Each toggle consists of a clickable title bar and a body area that expands or collapses when the title is clicked. This pattern helps you present large amounts of information in a compact format without overwhelming visitors with a wall of text.

Toggles are one of the most effective ways to organize informational content on a page. They work especially well for FAQ sections, product specifications, service descriptions, pricing breakdowns, and any scenario where visitors may only need to read a subset of the available content. By letting users choose what to expand, you reduce cognitive load and improve the overall browsing experience.

Unlike the Accordion module, which groups multiple collapsible items together and ensures only one is open at a time, each Toggle module operates independently. You can place multiple toggles in a row and visitors can open as many as they want simultaneously. You can also set the default state of each toggle to open or closed, giving you control over what content is visible when the page first loads.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10368052-the-toggle-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/toggle/)

![Toggle module](../assets/screenshots/modules/toggle/element.png){ loading=lazy }
*The Toggle module as it appears on the live demo.*

## Use Cases

1. **FAQ Sections** — Stack multiple Toggle modules in a single column to create a frequently asked questions page. Set each toggle title to a question and the body to the answer. Set all toggles to closed by default so visitors can scan the questions and open only the ones relevant to them.

2. **Product or Service Details** — Use toggles to organize detailed specifications, feature lists, or service tiers. Each toggle can represent a category of information (dimensions, materials, warranty, shipping), keeping the page clean while making all details accessible.

3. **Step-by-Step Instructions** — Present multi-step processes where each toggle represents one step. Visitors can work through the steps sequentially, closing completed steps and opening the next. This keeps long instructional content manageable.

## How to Add the Toggle Module

1. **Open the Visual Builder** on the page where you want the collapsible content to appear. Click the gray plus icon inside any row to open the module picker.

2. **Search for "Toggle"** in the module picker search bar, then click the Toggle module to insert it into the row.

3. **Configure the toggle** by entering a title and body content in the Content tab. Set the default state (open or closed) and adjust design settings to match your site's style. Repeat by adding additional Toggle modules in the same column for a multi-item list.

## Settings & Options

### Content Tab

The Content tab holds the toggle's text content, default state, and structural controls.

| Setting | Type | Description |
|---------|------|-------------|
| **Text** | | |
| Title | text | The clickable heading text displayed on the toggle bar |
| Body | rich text | The collapsible content area, supports visual editing and HTML |
| **State** | | |
| Open State | toggle | Whether the toggle is expanded (open) or collapsed (closed) when the page loads |
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

The Design tab provides visual controls for the toggle icon, title bar appearance, and all typography elements.

| Setting | Type | Description |
|---------|------|-------------|
| **Icon** | | |
| Open Icon | icon picker | The icon displayed when the toggle is in the expanded state |
| Close Icon | icon picker | The icon displayed when the toggle is in the collapsed state |
| Icon Color | color | Color of the toggle open/close icon |
| Icon Size | range | Size of the toggle icon in pixels |
| **Toggle** | | |
| Open Toggle Background Color | color | Background color of the toggle when it is expanded |
| Closed Toggle Background Color | color | Background color of the toggle when it is collapsed |
| Open Toggle Icon Color | color | Icon color when the toggle is in the open state |
| Closed Toggle Icon Color | color | Icon color when the toggle is in the closed state |
| **Text** | | |
| Text Alignment | select | Horizontal alignment for all text content (left, center, right, justified) |
| Text Color Scheme | select | Light or dark text color scheme for the module |
| **Title Text** | | |
| Title Font | typography | Font family, weight, style, and line height for the toggle title |
| Title Text Color | color | Font color for the toggle title |
| Title Text Size | range | Font size for the toggle title |
| Title Letter Spacing | range | Letter spacing for the title text |
| Title Line Height | range | Line height for the title text |
| Title Text Shadow | composite | Shadow effect applied to the title text |
| **Closed Title Text** | | |
| Closed Title Font | typography | Font family, weight, style, and line height for the title when the toggle is closed |
| Closed Title Text Color | color | Font color for the title in the closed state |
| Closed Title Text Size | range | Font size for the title in the closed state |
| Closed Title Letter Spacing | range | Letter spacing for the closed state title |
| Closed Title Line Height | range | Line height for the closed state title |
| Closed Title Text Shadow | composite | Shadow effect on the closed state title |
| **Body Text** | | |
| Body Font | typography | Font family, weight, style, and line height for the toggle body content |
| Body Text Color | color | Font color for the body content |
| Body Text Size | range | Font size for the body content |
| Body Letter Spacing | range | Letter spacing for the body text |
| Body Line Height | range | Line height for the body text |
| Body Text Shadow | composite | Shadow effect applied to body text |
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
| Toggle Title | code | Custom CSS targeting the toggle title bar element |
| Toggle Icon | code | Custom CSS targeting the open/close icon |
| Toggle Content | code | Custom CSS targeting the collapsible body content area |
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
/* Remove default border and add card-style shadow */
.et_pb_toggle {
    border: none;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
    margin-bottom: 16px;
    overflow: hidden;
}

/* Style the toggle title bar */
.et_pb_toggle_title {
    font-weight: 600;
    padding: 20px 24px;
    position: relative;
}

/* Change the open/close icon to a plus/minus */
.et_pb_toggle_title::after {
    content: "+";
    font-size: 24px;
    font-weight: 300;
    position: absolute;
    right: 24px;
    top: 50%;
    transform: translateY(-50%);
}
.et_pb_toggle_open .et_pb_toggle_title::after {
    content: "\2013";
}

/* Add a left accent border to open toggles */
.et_pb_toggle_open {
    border-left: 4px solid #2ea3f2;
}

/* Responsive adjustments */
@media (max-width: 767px) {
    .et_pb_toggle_title {
        padding: 16px 20px;
        font-size: 16px;
    }
    .et_pb_toggle_content {
        padding: 16px 20px;
    }
}
```

### PHP Hooks

```php
/**
 * Add schema.org FAQ structured data to pages with Toggle modules.
 */
function add_toggle_faq_schema( $output, $render_slug ) {
    if ( 'et_pb_toggle' !== $render_slug ) {
        return $output;
    }

    // Extract title and content from the module output
    preg_match( '/<h[1-6][^>]*class="et_pb_toggle_title"[^>]*>(.*?)<\/h[1-6]>/s', $output, $title_match );
    preg_match( '/<div class="et_pb_toggle_content[^"]*">(.*?)<\/div>/s', $output, $content_match );

    if ( ! empty( $title_match[1] ) && ! empty( $content_match[1] ) ) {
        $question = wp_strip_all_tags( $title_match[1] );
        $answer   = wp_strip_all_tags( $content_match[1] );

        $schema = '<script type="application/ld+json">';
        $schema .= json_encode( array(
            '@context'   => 'https://schema.org',
            '@type'      => 'Question',
            'name'       => $question,
            'acceptedAnswer' => array(
                '@type' => 'Answer',
                'text'  => $answer,
            ),
        ) );
        $schema .= '</script>';

        $output .= $schema;
    }

    return $output;
}
add_filter( 'et_module_shortcode_output', 'add_toggle_faq_schema', 10, 2 );
```

## Common Patterns

1. **FAQ Page** — Stack multiple Toggle modules in a single column, each with a question as the title and the answer as the body content. Set all toggles to the closed state by default. Apply consistent styling across all toggles using a shared CSS class for visual uniformity. Consider adding FAQ schema markup for SEO benefits.

2. **Categorized Information Sections** — Group related toggles under heading modules to create organized information sections. For example, a product page might have a "Specifications" heading followed by toggles for Dimensions, Materials, and Care Instructions, then a "Shipping" heading with toggles for Delivery Times and Return Policy.

3. **Progressive Disclosure for Long Content** — Break lengthy content into logical sections using toggles. This works well for legal pages (terms of service, privacy policies), documentation, or detailed guides where visitors typically need only specific sections rather than reading everything end to end.

## Saving Your Work

After configuring your Toggle module, click the green checkmark at the bottom of the settings panel to save the module settings. Save the page using the purple save button in the bottom dock of the Visual Builder, or use `Ctrl + S` (Windows) or `Cmd + S` (Mac). If you build a toggle with specific styling that you want to reuse, save it to the Divi Library as a reusable module.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Toggle module in Divi 5 uses the updated options framework and may have different CSS class structures compared to Divi 4. Verify custom CSS selectors when migrating from earlier versions.

## Troubleshooting

!!! warning "Toggle Not Opening or Closing"
    If clicking the toggle title does not expand or collapse the content:

    - Check for JavaScript errors in the browser console that may be blocking the toggle interaction
    - Verify that no other plugins are conflicting with Divi's JavaScript (common with caching plugins that defer or combine scripts)
    - Ensure the toggle module is not wrapped inside a link element, which can intercept click events

!!! warning "Content Overflowing When Toggle Opens"
    If the toggle body content extends beyond its container or overlaps other elements when expanded:

    - Check the Overflow settings in the Advanced tab and set them to `visible`
    - Remove any fixed height values from the Sizing settings in the Design tab
    - If using images or embeds in the toggle body, ensure they have responsive widths (max-width: 100%)

!!! warning "Open State Not Respecting Default Setting"
    If a toggle opens or closes on page load contrary to your State setting:

    - Confirm the Open State toggle in the Content tab is set to your desired default
    - Clear all caching layers (plugin cache, server cache, CDN cache) as cached pages may reflect a previous setting
    - Check for JavaScript that may be programmatically toggling the state on page load

## Related

- [Accordion Module](accordion.md) — groups multiple collapsible items where only one can be open at a time
- [Tabs Module](tabs.md) — organizes content into horizontal or vertical tabbed panels
