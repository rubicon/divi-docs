---
title: "Call to Action"
description: "Complete Divi 5 Call to Action module reference — heading, description, and button settings for conversion-focused content blocks."
category: modules
tags: ["modules", "cta", "call-to-action", "button", "conversion", "marketing"]
related: ["button", "blurb", "text"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10259934-the-call-to-action-module-divi-5"
---

# Call to Action

The Call to Action module displays a heading, description text, and a prominent button to drive user conversions.

!!! abstract "Quick Reference"
    **What it does:** Bundles a title, body text, and a clickable button into one conversion-focused content block.
    **When to use it:** Newsletter signups, pricing conversion prompts, promotional banners, content divider sections
    **Key settings:** Title, Button Text, Body, Link (button URL), Background
    **Block identifier:** `divi/cta`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10259934-the-call-to-action-module-divi-5)

!!! tip "When to Use This Module"
    - You need a heading, short description, and button together as a single conversion block
    - Promotional banners or signup prompts positioned at natural decision points
    - Full-width call-to-action sections between content areas

!!! warning "When NOT to Use This Module"
    - You need only a standalone button without heading or description → use [Button](button.md)
    - You need an icon or image with text (feature card) → use [Blurb](blurb.md)
    - You need a form-based email capture → use [Email Optin](email-optin.md)

## Overview

The Call to Action (CTA) module is purpose-built for directing visitors toward a specific action. It bundles a title, body text, and a clickable button into one visually distinct block that stands apart from surrounding content. Typical applications include newsletter signups, product promotions, contact prompts, event registrations, and any scenario where you need to funnel attention toward a single goal.

The module ships with a configurable background that helps it contrast with the rest of the page. Out of the box it renders with a colored background, white text, and centered alignment, but every visual property can be adjusted through the Design tab. The button only renders when both button text and a URL are provided, so the module gracefully degrades to a text-only block when no action link is needed.

CTAs perform well in any column width. Position them at natural decision points: after describing a product's benefits, at the end of a blog post, or in a dedicated section between content blocks. For maximum effectiveness, keep the description to one or two sentences and use a clear, action-oriented button label.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10259934-the-call-to-action-module-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/call-to-action/)

![Call to Action module](../assets/screenshots/modules/call-to-action/element.png){ loading=lazy }
*The Call to Action module as it appears on the live demo.*

## Use Cases

1. **Newsletter Signup Prompt** — Place a CTA with a brief value proposition as the title, one sentence describing what subscribers receive, and a "Subscribe Now" button linking to a signup page or popup form.
2. **Pricing Conversion Block** — Position below a pricing table or feature comparison to reinforce the offer with reassurance text and a prominent trial or purchase button.
3. **Content Divider Banner** — Use as a full-width visual break between content sections with a background image, overlay, and a short action-oriented message.

## How to Add the Call to Action Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Call to Action" in the module picker or find it in the Content Elements category, then click to insert it.


## Settings & Options

The Call to Action module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the CTA's text content, link behavior, background, and module metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Title | text | The main heading displayed at the top of the CTA block. Supports dynamic content. |
| Button Text | text | Label for the call-to-action button. The button is hidden when this field is empty. |
| Body | rich text editor | Descriptive text displayed between the title and button. Supports HTML formatting, lists, and inline styles. |
| Link | url/link settings | Destination URL for the button and optional module-level link. Includes target (same window or new tab), link relationship attributes, and a module link option that makes the entire CTA clickable. |
| Background | background controls | Set a background color, gradient, image, or video behind the entire CTA module. Multiple background layers can be combined. |
| Loop | toggle | Enables the loop builder, allowing the CTA to repeat dynamically based on a data source such as posts or custom queries. |
| Order | number | Controls the display order of this module when its parent row or column uses Flexbox or CSS Grid layout modes. |
| Meta | admin label | Set an admin label for the module to help identify it in the Visual Builder's layer panel. Also controls Visual Builder visibility. |

![Call to Action Content tab settings](../assets/screenshots/modules/call-to-action/settings-content.png){ loading=lazy }

### Design Tab

The Design tab controls the visual appearance of the CTA's text, button, layout, borders, and effects.

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Title Text](../options-groups/text.md) | Font, size, color, letter spacing for the CTA title |
| [Body Text](../options-groups/text.md) | Font, size, color, line height for description content |
| [Button](../options-groups/button.md) | Text size, colors, border, radius, font, icon, hover behavior |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, etc.) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

![Call to Action Design tab settings](../assets/screenshots/modules/call-to-action/settings-design.png){ loading=lazy }

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, interactions, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

![Call to Action Advanced tab settings](../assets/screenshots/modules/call-to-action/settings-advanced.png){ loading=lazy }

## Code Examples

### Custom CSS

```css
/* Gradient background CTA with rounded corners */
.et_pb_promo.gradient-cta {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border-radius: 12px;
    overflow: hidden;
}

/* Side-by-side layout — text left, button right */
.et_pb_promo.side-by-side .et_pb_promo_description {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
    text-align: left;
}

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

/* Animated button fill effect on hover */
.et_pb_promo .et_pb_promo_button {
    position: relative;
    overflow: hidden;
    z-index: 1;
    transition: all 0.3s ease;
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

.et_pb_promo .et_pb_promo_button:hover::before {
    left: 0;
}
```

### PHP Hooks

```php
/* Add analytics tracking attributes to CTA buttons */
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

1. **Newsletter Signup CTA** — A centered CTA with a brief value proposition as the title, one sentence of description, and a "Subscribe Now" button linking to a signup page. Use a bold background color that contrasts with the surrounding section and generous padding to make the block stand out visually.

2. **Pricing Reinforcement** — Place below a pricing table with the title reinforcing the offer ("Start Your Free Trial Today") and a short reassurance line as the description ("No credit card required. Cancel anytime."). Style the button with a bright accent color and increased border radius for a pill-shaped look.

3. **Full-Width Banner Divider** — A full-width CTA used between content sections with a background image and a semi-transparent color overlay. Use the side-by-side CSS layout from the code examples to position text on the left and the button on the right. Works best in a fullwidth section or single-column row with no row padding.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/cta` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Title | `attrs.title` | CTA heading text |
| Body | `attrs.content` | Description text between title and button |
| Button Text | `attrs.button_text` | Label on the CTA button |
| Button URL | `attrs.button_url` | Destination link for the button |

!!! tip "Module Selection Guidance"
    For heading+text+button combos use CTA; for icon+text use Blurb; for standalone buttons use Button.

## Saving Your Work

After configuring the CTA:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Button Not Appearing"
    If the CTA button is not visible:

    - Both **Button Text** and **Link URL** must be filled in. The button will not render if either field is empty.
    - Check the button text color against the button background color — they may be identical, making the text invisible.
    - If using custom button styles, verify that the button text size is not set to 0.
    - Inspect the element in browser DevTools to confirm the button HTML is present but possibly hidden by CSS.

!!! warning "Background Color Not Showing"
    If the background appears transparent when it should have a color:

    - Confirm that the **Background** settings in the Content tab have a color or gradient applied.
    - Check whether a background image is covering the background color. Images render on top of solid colors unless layered intentionally.
    - If a parent section or row has its own background set, it may visually blend with the CTA background.

!!! tip "Text Alignment Issues on Mobile"
    If text alignment looks correct on desktop but breaks on smaller screens:

    - Divi may reset alignment to center on mobile. Use the responsive toggle on the text alignment setting to specify alignment for each breakpoint independently.
    - If using custom CSS for a side-by-side layout, ensure your media queries include a fallback to stacked/centered layout below your breakpoint.

## Related

- [Button](button.md) — Standalone button module for simpler link elements without heading or description text
- [Blurb](blurb.md) — Icon or image with text; useful for feature blocks that lead into a CTA
- [Text](text.md) — Rich text content module for descriptive content that supports the CTA's message
- [Email Optin](email-optin.md) — Form-based email capture with ESP integration for newsletter signups
- [Background Options](../options-groups/background.md) — Configure background colors, gradients, and images that make CTAs stand out
- [Button Options Group](../options-groups/button.md) — Shared button design settings used by the CTA button
