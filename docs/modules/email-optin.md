---
title: "Email Optin"
category: modules
tags: ["modules", "forms", "interactive", "email", "optin", "newsletter", "subscription", "marketing"]
related: ["contact-form", "button"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10273324-the-email-optin-module-in-divi-5"
---

# Email Optin

The Email Optin module creates customizable email subscription forms that integrate directly with popular email marketing platforms.

## Overview

The Email Optin module lets you add fully styled newsletter signup forms anywhere in your Divi layout. It connects to over twenty email marketing services — including Mailchimp, ConvertKit, ActiveCampaign, AWeber, and others — so subscribers are automatically added to your chosen mailing list without any additional plugin or third-party form builder.

The module includes fields for first name, last name, and email address, along with a submit button and optional descriptive text. You control which fields are visible and whether they display at full width or half width. A title and body text area let you add a compelling call to action above the form fields, and a footer text area provides space for privacy disclaimers or additional context below the form.

After a visitor submits the form, you can either display a custom success message or redirect them to a thank-you page. Built-in Google reCAPTCHA support helps prevent spam submissions. The module also offers flexible layout options, letting you arrange the descriptive content and form fields side by side or stacked vertically.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10273324-the-email-optin-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/email-optin/)

![Email Optin module](../assets/screenshots/modules/email-optin/element.png){ loading=lazy }
*The Email Optin module displaying a styled newsletter subscription form.*

## Use Cases

1. **Newsletter Signup Section** — Place an email optin form in a dedicated section on your homepage or blog sidebar to grow your mailing list with a clear value proposition and minimal friction.
2. **Lead Magnet Landing Page** — Create a focused landing page with the email optin module front and center, offering a free resource (ebook, checklist, template) in exchange for an email address.
3. **Footer or Header Subscription Bar** — Add a compact email optin to your global header or footer template so it appears across every page, giving visitors a persistent opportunity to subscribe.

## How to Add the Email Optin Module

1. Open the Visual Builder on the page where you want the subscription form.
2. Click the gray **+** icon inside any row to add a new module.
3. Search for "Email Optin" in the module picker or browse the Form Elements category, then click to insert it.

## Settings & Options

The Email Optin module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the form text, email service integration, field configuration, success behavior, and spam protection.

| Setting | Type | Description |
|---------|------|-------------|
| Title | text | The heading displayed above the form. Use this to communicate the benefit of subscribing, such as "Get Weekly Design Tips" or "Join Our Newsletter." |
| Button Text | text | The label on the submit button. Defaults to "Subscribe" but can be customized to match your call to action (e.g., "Get Access," "Sign Up Free"). |
| Body | rich text editor | Descriptive text displayed between the title and the form fields. Use this to elaborate on what subscribers will receive and why they should sign up. |
| Footer | text | Optional text displayed below the form. Commonly used for privacy policy statements like "We respect your privacy. Unsubscribe anytime." |
| Email Account | select | Choose which connected email marketing provider to use. You must first configure your email service API keys in the Divi Theme Options under Integrations. |
| Email List | select | After selecting an email account, choose the specific mailing list or audience that new subscribers will be added to. |
| Use First Name | toggle | Show or hide the first name field on the form. Disabling this reduces form friction but collects less subscriber data. |
| Use Last Name | toggle | Show or hide the last name field on the form. |
| Success Action | select | Choose what happens after a successful form submission: display a custom success message within the module, or redirect the visitor to a specified URL (such as a thank-you page). |
| Success Message | text | The message displayed to the visitor after a successful submission when using the message success action. |
| Redirect URL | url | The page URL to redirect visitors to after a successful submission when using the redirect success action. |
| Enable Spam Protection | toggle | Activate Google reCAPTCHA to prevent automated spam submissions. Requires reCAPTCHA API keys configured in Divi Theme Options. |
| Link | url | Optionally wrap the entire module in a link, making the whole element clickable. |
| Background | background controls | Set a background color, gradient, image, or video behind the entire email optin module. |
| Loop | toggle | Enable the loop builder to use this module as a repeating element within dynamic content layouts. |
| Order | select | Control the module's display order when its parent row uses Flexbox or CSS Grid layout. |
| Meta | admin label | Assign a custom label to identify this module in the Visual Builder's layer panel. |

### Design Tab

The Design tab controls the layout arrangement, field styling, typography, button appearance, and all visual effects.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose how the body content and form fields are arranged: body on left with form on right, body on right with form on left, body on top with form below, or body on bottom with form above. |
| First Name Fullwidth | toggle | When enabled, the first name field spans the full width of the form area. When disabled, it shares a row with other fields. |
| Last Name Fullwidth | toggle | When enabled, the last name field spans the full width of the form area. |
| Email Fullwidth | toggle | When enabled, the email field spans the full width of the form area. |
| Fields | field styling | Style the form input fields — background color, text color, focus border color, placeholder text color, and field padding. |
| Description Text | text styling | Style the body/description text separately from the title. Control font, size, weight, color, and line height. |
| Result Message Text | text styling | Style the success or error message text that appears after form submission. Set font, size, color, and weight. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Title Text](../options-groups/text.md) | Font, size, color, letter spacing for the title heading |
| [Button](../options-groups/button.md) | Submit button text color, background, border, font, icon, hover states |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, etc.) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

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
| Privacy | Control whether subscriber IP addresses are included (GDPR compliance) |

## Code Examples

### Custom CSS

```css
/* Style the email optin container */
.et_pb_newsletter {
    border-radius: 12px;
    overflow: hidden;
}

/* Style the form title */
.et_pb_newsletter .et_pb_newsletter_description h2 {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Style the form input fields */
.et_pb_newsletter .et_pb_newsletter_form input[type="text"],
.et_pb_newsletter .et_pb_newsletter_form input[type="email"] {
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 16px;
}

/* Style input fields on focus */
.et_pb_newsletter .et_pb_newsletter_form input:focus {
    border-color: #2ea3f2;
    outline: none;
    box-shadow: 0 0 0 3px rgba(46, 163, 242, 0.15);
}

/* Style the submit button */
.et_pb_newsletter .et_pb_newsletter_button {
    background-color: #2ea3f2;
    border-radius: 8px;
    padding: 14px 28px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Style the success message */
.et_pb_newsletter .et_pb_newsletter_success p {
    color: #27ae60;
    font-weight: 600;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_newsletter .et_pb_newsletter_description {
        margin-bottom: 20px;
    }
    .et_pb_newsletter .et_pb_newsletter_form input {
        margin-bottom: 10px;
    }
}
```

### PHP Hooks

```php
/* Filter the Email Optin module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_signup' !== $render_slug) {
        return $output;
    }
    // Example: add a privacy notice below the form
    $privacy = '<p class="privacy-notice">By subscribing, you agree to our <a href="/privacy-policy">Privacy Policy</a>.</p>';
    $output = str_replace('</form>', $privacy . '</form>', $output);
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Split Layout Signup** — Use the side-by-side layout option (body on left, form on right) with a background image or color. Place a compelling headline and two to three sentences of body text on the left describing the newsletter's value, with the form fields and button on the right. This creates an engaging, magazine-style signup section.

2. **Minimal Inline Form** — Hide the first and last name fields so only the email field and button are visible. Set the email field to full width and place it in a narrow row. Style the button with a bold accent color. This creates a compact, low-friction signup strip ideal for headers, footers, or between content sections.

3. **Lead Magnet with Redirect** — Configure the success action to redirect to a thank-you page that delivers the promised resource (PDF download, video access, etc.). Use the title and body text to describe the free resource, and set the button text to something specific like "Download Free Guide." Add a footer text line about privacy to build trust.

## Saving Your Work

After configuring the email optin form:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Form Submissions Not Reaching Email Provider"
    If visitors can submit the form but subscribers do not appear in your email marketing platform, verify your API keys in Divi Theme Options under the Integrations tab. Make sure the correct email account and list are selected in the module's Content tab. Also check your email provider's dashboard for pending confirmations if double opt-in is enabled.

!!! warning "reCAPTCHA Not Working"
    If spam protection is enabled but the reCAPTCHA widget does not appear, confirm that your reCAPTCHA Site Key and Secret Key are entered correctly in Divi Theme Options. Ensure you are using reCAPTCHA v2 (checkbox) keys, not v3 keys, unless your Divi version specifically supports v3. Also check that no JavaScript errors on the page are preventing the reCAPTCHA script from loading.

!!! tip "Form Layout Breaks on Mobile"
    If the side-by-side layout looks cramped on smaller screens, switch to a stacked layout (body on top, form on bottom) for tablet and phone devices. You can also use the fullwidth toggles for name and email fields to ensure each field gets its own row on narrow viewports. Test the form on actual mobile devices to verify spacing and tap target sizes.

## Related

- [Contact Form](contact-form.md) — General-purpose contact form for visitor inquiries, with customizable fields
- [Button](button.md) — Standalone call-to-action button that can complement email optin sections
