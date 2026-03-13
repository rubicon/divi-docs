---
title: "Call to Action"
category: modules
tags: ["modules", "cta", "call-to-action", "button", "conversion"]
related: ["button", "blurb", "fullwidth-header"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/cta/"
---

# Call to Action

The Call to Action module displays a heading, description text, and a prominent button to drive user conversions.

## Overview

The Call to Action (CTA) module is designed for a single purpose: getting visitors to take action. It combines a title, body text, and a button into one visually distinct block that stands out from surrounding content. Common uses include email newsletter signups, contact form prompts, product promotions, event registrations, and any situation where you want to direct the visitor toward a specific goal.

The module supports a configurable background color that helps it contrast with the rest of the page. By default it renders with a blue (#2ea3f2) background, white text, and a centered layout, but every aspect can be customized through the Design tab. The button only appears when both Button Text and Button URL are provided.

CTAs work well in any column width. Place them at natural decision points in your content: after describing a product's benefits, at the end of a blog post, or in a dedicated section between content blocks. For maximum impact, limit the text to one or two sentences and use a clear, action-oriented button label.

![Call to Action module overview](../assets/screenshots/modules/call-to-action/overview.png){ loading=lazy }
*The Call to Action module as it appears in the Divi 5 Visual Builder.*

## Settings & Options

### Content Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Title | text | — | The main heading displayed at the top of the CTA. Supports dynamic content. |
| Button Text | text | — | Label for the call-to-action button. The button is hidden when this field is empty. |
| Description | rich-text | — | Body text displayed between the title and button. Supports HTML formatting, lists, and inline styles. |
| Use Background Color | toggle | Yes | When enabled, the module renders with a solid background color. Disable for a transparent background. |
| Background Color | color | #2ea3f2 | The background fill color. Only visible when Use Background Color is enabled. |
| Background Image | upload | — | Optional background image displayed behind the CTA content. |
| Background Gradient | gradient | — | Apply a gradient background instead of or layered with a solid color. |
| Admin Label | text | — | Internal label visible only in the Visual Builder. Useful for identifying modules in complex layouts. |

#### Link Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Button Link URL | url | — | Destination URL for the button. The button will not render without both text and a URL. |
| Button Link Target | select | Same Window | Where the link opens: Same Window or New Tab. |
| Module Link URL | url | — | Makes the entire CTA module clickable, linking to this URL. Overrides the button link behavior. |

![Call to Action Content tab settings](../assets/screenshots/modules/call-to-action/settings-content.png){ loading=lazy }
*Content tab with title, description, button text, and background color options.*

### Design Tab

#### Text Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Title Font | font | Default | Font family for the CTA title. |
| Title Font Weight | select | Bold | Weight of the title text. |
| Title Font Style | toggle | — | Italic, uppercase, underline, or strikethrough for the title. |
| Title Text Alignment | select | Center | Horizontal alignment of the title. |
| Title Text Color | color | #ffffff | Color of the title text. |
| Title Text Size | range | 26px | Font size of the title. Responsive — set independently for desktop, tablet, and phone. |
| Title Letter Spacing | range | 0px | Space between characters in the title. |
| Title Line Height | range | 1em | Vertical space between lines for multi-line titles. |
| Title Text Shadow | select | None | Shadow effect applied to the title. |
| Body Font | font | Default | Font family for the description text. |
| Body Font Weight | select | Regular | Weight of the body text. |
| Body Font Style | toggle | — | Italic, uppercase, underline, or strikethrough for body text. |
| Body Text Alignment | select | Center | Horizontal alignment of the description text. |
| Body Text Color | color | #ffffff | Color of the description text. |
| Body Text Size | range | 14px | Font size of the description. Responsive. |
| Body Letter Spacing | range | 0px | Space between characters in the body. |
| Body Line Height | range | 1.7em | Vertical space between lines in the description. |
| Body Text Shadow | select | None | Shadow effect applied to body text. |

#### Button Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Use Custom Styles for Button | toggle | Off | When enabled, exposes detailed button styling options below. |
| Button Text Size | range | 20px | Font size of the button label. |
| Button Text Color | color | #ffffff | Color of the button text. |
| Button Background Color | color | transparent | Background fill color of the button. |
| Button Border Width | range | 2px | Thickness of the button border. |
| Button Border Color | color | #ffffff | Color of the button border. |
| Button Border Radius | range | 3px | Corner rounding of the button. |
| Button Font | font | Default | Font family for the button text. |
| Button Icon | icon | Arrow | Icon displayed alongside the button text. |
| Button Icon Placement | select | Right | Position of the icon relative to the button text (Left or Right). |
| Button On Hover | toggle | Yes | When enabled, the icon slides in on hover. When disabled, the icon is always visible. |

#### Module Layout

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Text Orientation | select | Center | Overall alignment of all CTA content (Left, Center, Right). |
| Max Width | range | — | Maximum width of the module. Centers the module when narrower than the column. |
| Module Alignment | select | Center | Horizontal alignment of the module when its width is less than the column width. |

#### Border

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Border Width | range | 0px | Thickness of the module border on all sides, or set individually per side. |
| Border Color | color | #333333 | Color of the module border. |
| Border Style | select | Solid | Border line style (Solid, Dashed, Dotted, Double, Groove, Ridge, Inset, Outset). |
| Border Radius | range | 0px | Corner rounding of the module. |

#### Box Shadow

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Box Shadow | select | None | Apply a shadow effect around the module. Choose from presets or configure custom values. |
| Box Shadow Horizontal | range | 0px | Horizontal offset of the shadow. |
| Box Shadow Vertical | range | 0px | Vertical offset of the shadow. |
| Box Shadow Blur | range | 0px | Blur radius of the shadow. |
| Box Shadow Spread | range | 0px | Spread radius of the shadow. |
| Box Shadow Color | color | rgba(0,0,0,0.3) | Color of the box shadow. |

#### Spacing

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Custom Margin | range | — | Space outside the module (top, right, bottom, left). Responsive. |
| Custom Padding | range | 40px 30px | Space inside the module between its edges and the content. Responsive. |

#### Animation

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Animation Style | select | None | Entrance animation when the module scrolls into view (Fade, Slide, Bounce, Zoom, Flip, Fold, Roll). |
| Animation Direction | select | Center | Direction of the entrance animation. |
| Animation Duration | range | 1000ms | Length of the entrance animation. |
| Animation Delay | range | 0ms | Delay before the entrance animation begins. |
| Animation Intensity | range | 50% | Intensity of the entrance animation effect. |

![Call to Action Design tab settings](../assets/screenshots/modules/call-to-action/settings-design.png){ loading=lazy }
*Design tab showing typography, button, border, and spacing controls.*

### Advanced Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| CSS ID | text | — | Assign a unique CSS ID to the module for targeting with custom CSS or JavaScript. |
| CSS Class | text | — | Assign one or more CSS classes to the module, separated by spaces. |
| Custom CSS | code | — | Add custom CSS to specific elements: Main Element, Title, Description, Button, and Button Icon. |
| Visibility | toggle | Show on all devices | Control which devices display this module (Desktop, Tablet, Phone). |
| Transition Duration | range | 300ms | Duration of hover transition effects on interactive elements. |
| Horizontal Overflow | select | Default | How content that overflows the module width is handled. |
| Vertical Overflow | select | Default | How content that overflows the module height is handled. |
| Position | select | Default | CSS positioning scheme (Static, Relative, Absolute, Fixed, Sticky). |
| Z Index | number | — | Stacking order of the module relative to other elements. |
| Scroll Effects | toggle | Off | Enable transform effects triggered by scroll position. |

## Code Examples

### Gradient Background CTA

```css
/* Apply a gradient background to the CTA */
.et_pb_promo.gradient-cta {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border-radius: 12px;
    overflow: hidden;
}

/* Add a subtle pattern overlay */
.et_pb_promo.gradient-cta::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at 20% 50%, rgba(255,255,255,0.1) 0%, transparent 50%);
    pointer-events: none;
}
```

### Side-by-Side Layout (Text Left, Button Right)

```css
/* Reflow the CTA into a horizontal layout */
.et_pb_promo.side-by-side .et_pb_promo_description {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
    text-align: left;
}

/* Let the text block take available space */
.et_pb_promo.side-by-side .et_pb_promo_description .et_pb_promo_button_wrapper {
    flex-shrink: 0;
}

/* Stack vertically on mobile */
@media (max-width: 767px) {
    .et_pb_promo.side-by-side .et_pb_promo_description {
        flex-direction: column;
        text-align: center;
    }
}
```

### Animated Button Hover Effect

```css
/* Animated button with background fill on hover */
.et_pb_promo .et_pb_promo_button {
    background: transparent;
    border: 2px solid #ffffff;
    color: #ffffff;
    padding: 14px 32px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    z-index: 1;
}

.et_pb_promo .et_pb_promo_button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: #ffffff;
    transition: left 0.3s ease;
    z-index: -1;
}

.et_pb_promo .et_pb_promo_button:hover {
    color: #667eea;
}

.et_pb_promo .et_pb_promo_button:hover::before {
    left: 0;
}
```

### PHP: Add Tracking Attributes

```php
/* Add data attributes for analytics tracking to CTA buttons */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_cta' !== $render_slug) {
        return $output;
    }
    $output = str_replace(
        'class="et_pb_promo_button',
        'data-track="cta-click" class="et_pb_promo_button',
        $output
    );
    return $output;
}, 10, 2);
```

## Common Patterns

### 1. Newsletter Signup CTA

A centered CTA with a brief value proposition as the title ("Join 10,000+ Subscribers"), one sentence of description text explaining what the subscriber receives, and a "Subscribe Now" button that links to a dedicated signup page or triggers a popup form. Use a bold background color that contrasts with the surrounding section. Keep padding generous to make the CTA stand out as its own visual block.

![Newsletter CTA pattern](../assets/screenshots/modules/call-to-action/pattern-newsletter-cta.png){ loading=lazy }
*A newsletter signup CTA with contrasting background and bold button.*

### 2. Pricing CTA

Place the CTA below a pricing table or feature comparison. Use the title to reinforce the offer ("Start Your Free Trial Today") and the description for urgency or reassurance ("No credit card required. Cancel anytime."). Style the button with a bright accent color and increased border radius for a pill-shaped appearance. This pattern works well at 1/2 or 2/3 column width, centered in the row.

![Pricing CTA pattern](../assets/screenshots/modules/call-to-action/pattern-pricing-cta.png){ loading=lazy }
*A pricing CTA with reassurance text and a prominent trial button.*

### 3. Banner CTA

A full-width CTA used as a page divider or banner between content sections. Use a background image with a dark overlay (set via Background Color with transparency) and the side-by-side CSS layout from the code examples above. Keep the title short and punchy. This pattern works best in a fullwidth section or a single-column row with no padding on the row.

![Banner CTA pattern](../assets/screenshots/modules/call-to-action/pattern-banner-cta.png){ loading=lazy }
*A full-width banner CTA with background image and side-by-side layout.*

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Button Not Appearing"
    If the CTA button is not visible:

    - Both **Button Text** and **Button Link URL** must be filled in. The button will not render if either field is empty.
    - Check the button text color against the button background color — they may be the same, making the text invisible.
    - If using custom button styles, verify that the button text size is not set to 0.
    - Inspect the element in browser DevTools to confirm the button HTML is present but possibly hidden by CSS.

!!! warning "Button Not Clickable"
    If the button appears but does not respond to clicks:

    - Verify the **Button Link URL** contains a valid URL (including the `https://` protocol).
    - If a **Module Link URL** is also set, it wraps the entire module in a link, which can interfere with the button link. Use one or the other, not both.
    - Check for overlapping elements with a higher z-index that may be intercepting clicks. Use DevTools to inspect the stacking order.
    - JavaScript errors from other plugins can prevent click handlers from firing. Check the browser console.

!!! warning "Text Alignment Not Working"
    If text does not align as expected:

    - The **Text Orientation** setting in the Design tab controls the overall alignment. Verify it is set correctly.
    - If using the side-by-side CSS layout, the `text-align` property in the custom CSS overrides the module setting.
    - On mobile, Divi may reset alignment to center. Use the responsive toggle on the Text Orientation setting to set mobile alignment explicitly.

!!! warning "Background Color Not Showing"
    If the background appears transparent when it should have a color:

    - Confirm that **Use Background Color** is toggled to **Yes** in the Content tab.
    - Check whether a background image is covering the background color. Images render on top of solid colors.
    - If a parent section or row has a background set, it may visually blend with the CTA background.

## Related

- [Button](button.md) — Standalone button module for simpler link elements
- [Blurb](blurb.md) — Icon/image with text; useful for feature blocks that lead into a CTA
- [Fullwidth Header](fullwidth-header.md) — Full-width hero section with similar heading + button layout
- [Email Optin](email-optin.md) — Built-in email signup form with provider integrations
