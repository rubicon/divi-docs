---
title: "Social Media Follow"
description: "Complete Divi 5 Social Media Follow module reference — platform icons, profile links, brand colors, alignment, and button styling."
category: modules
tags: ["modules", "social-media", "social-icons", "follow-buttons", "networking", "social-links"]
related: ["person", "icon"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10364982-the-social-media-follow-module-in-divi-5"
---

# Social Media Follow

The Social Media Follow module displays linked social media icons that direct visitors to your profiles on various platforms.

!!! abstract "Quick Reference"
    **What it does:** Displays a row of social media icons linked to your profiles across multiple platforms.
    **When to use it:** Site footer social links, author bio sections, contact page supplements
    **Key settings:** Social Networks (repeater), Profile URL, Social Network type, Icon color/size, Alignment
    **Block identifier:** `divi/social-media-follow`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10364982-the-social-media-follow-module-in-divi-5)

!!! tip "When to Use This Module"
    - Adding social profile links to headers, footers, or contact pages
    - Displaying branded social media icons with custom colors and sizes
    - Creating a row of follow buttons alongside author or team bios

!!! warning "When NOT to Use This Module"
    - Displaying team member profiles with social links built in → use [Person](person.md)
    - Showing a single decorative or functional icon → use [Icon](icon.md)

## Overview

The Social Media Follow module provides a visual set of social media icons that link to your profiles across dozens of platforms. Each icon is added as a repeatable child item within the module, allowing you to include as many or as few networks as needed. The module supports a wide range of platforms beyond the major ones, covering niche and regional social networks as well.

Unlike simple icon lists, this module is purpose-built for social profile linking. Each item carries its own platform selection, profile URL, and customizable appearance. The icons render with recognizable brand styling by default, and you can override colors and shapes to match your site's design system. The module works well in headers, footers, sidebars, and within content areas wherever you want to encourage visitors to connect with you on social media.

The layout adapts to its container and offers alignment controls to position icons left, center, or right. On smaller screens, icons reflow naturally to maintain tap-friendly sizing. Combined with the Design tab's icon and text styling options, you can produce anything from a minimal row of monochrome icons to fully branded follow buttons with network names.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10364982-the-social-media-follow-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/social-media-follow/)

![Social Media Follow module](../assets/screenshots/modules/social-media-follow/element.png){ loading=lazy }
*The Social Media Follow module as it appears on the live demo.*

## Use Cases

1. **Site Footer Social Links** — Place the module in your footer to provide a persistent row of social profile links across every page, encouraging visitors to follow your brand.
2. **Author Bio Section** — Combine the module with a Person module or text block to display an author's social profiles alongside their bio and headshot on blog posts.
3. **Contact Page Supplement** — Add social follow icons to a contact page alongside a contact form, giving visitors alternative ways to reach and connect with your organization.

## How to Add the Social Media Follow Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Social Media Follow" in the module picker or find it in the Content Elements category, then click to insert it.

## Settings & Options

The Social Media Follow module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab manages the individual social network items and module-level configuration for icons, backgrounds, and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Social Networks (Repeater) | item list | Manage individual social network items. Click **+** to add a new network, the pencil icon to edit, the trash icon to delete, and drag to reorder. Each item has its own settings detailed below. |
| Icon | icon settings | Configure the default icon style and behavior that applies across all social network items in the module. |
| Background | background controls | Set a background color, gradient, image, or video behind the entire social media follow module. |
| Loop | toggle | Control repeating behavior for the social network items. |
| Order | select | Control the display order of the social network items within the module. |
| Meta | admin label | Set an internal label for the module visible only in the Visual Builder's layer panel. |

#### Individual Social Network Item Settings

Each social network item within the module has its own configuration panel:

| Setting | Type | Description |
|---------|------|-------------|
| Social Network | select | Choose the social platform from the available list (Facebook, Twitter/X, Instagram, LinkedIn, YouTube, Pinterest, TikTok, and many more). This determines the default icon and brand color. |
| Profile URL | url | The full URL to your profile on the selected platform. This is where visitors are directed when they click the icon. |
| Background Color | color picker | Override the default brand color for this specific network icon's background. |
| Icon Color | color picker | Override the default icon color for this specific network item. |
| Skype Action | select | When Skype is selected as the network, choose whether the link initiates a call or opens a chat. Only visible for the Skype network type. |

### Design Tab

The Design tab controls the visual appearance of the social icons, text labels, button styling, and overall module layout.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Alignment | alignment control | Set the horizontal alignment of the social icons within the module container (left, center, or right). |
| Icon | icon styling | Customize the icon appearance including color, size, and hover state behavior across all items in the module. |
| Follow Button | button styling | Control the shape and appearance of the follow button containers, including background color, border radius, padding, and hover state transitions. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow for text labels |
| [Sizing](../options-groups/sizing.md) | Width, max-width, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding with responsive breakpoint controls |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Horizontal/vertical offset, blur, spread, color, position |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue rotation, blur, invert, sepia, opacity, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, direction, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level controls for custom attributes, CSS targeting, conditional display logic, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (icon container, individual icons, link wrappers) |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

## Code Examples

### Custom CSS: Monochrome Icon Style

```css
/* Override brand colors with a uniform monochrome look */
.et_pb_social_media_follow li a {
    background-color: #333333 !important;
    color: #ffffff !important;
    transition: background-color 0.3s ease;
}

.et_pb_social_media_follow li a:hover {
    background-color: #0073aa !important;
}
```

### Custom CSS: Circular Icons with Spacing

```css
/* Round icons with consistent spacing between them */
.et_pb_social_media_follow li {
    margin: 0 6px;
}

.et_pb_social_media_follow li a {
    border-radius: 50%;
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
}
```

### Custom CSS: Responsive Icon Sizing

```css
/* Larger tap targets on mobile devices */
@media (max-width: 767px) {
    .et_pb_social_media_follow li a {
        width: 52px;
        height: 52px;
        font-size: 20px;
    }

    .et_pb_social_media_follow li {
        margin: 4px;
    }
}
```

### PHP: Add rel Attributes to Social Links

```php
/* Add noopener and noreferrer to all social follow links */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_social_media_follow' !== $render_slug) {
        return $output;
    }
    $output = str_replace(
        'target="_blank"',
        'target="_blank" rel="noopener noreferrer"',
        $output
    );
    return $output;
}, 10, 2);
```

## Common Patterns

### 1. Footer Social Bar

Place the module in a dedicated footer row with center alignment. Use a dark background color on the row and set the icon colors to white or light gray for contrast. Keep spacing tight between icons and add moderate vertical padding to the row for visual separation from surrounding content.

### 2. Branded Buttons with Labels

Enable text labels alongside the icons to display network names (e.g., "Follow on Instagram"). Use each platform's brand color as the button background and white text for the label. This approach works well on contact pages where you want to be explicit about each destination.

### 3. Minimal Header Icons

Add the module to a header row and align it to the right. Use small icon sizes with no background color, relying on a single icon color that matches your header text. This creates an unobtrusive row of social links that does not compete with the primary navigation.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/social-media-follow` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Child network items | Nested blocks | Each item has network type and profile URL |

!!! tip "Module Selection Guidance"
    For social media profile links use Social Media Follow; for team profiles with social links use Person; for standalone icons use Icon.

## Saving Your Work

After configuring your social media icons, save your changes by clicking the **Save** button (checkmark icon) in the Visual Builder's bottom toolbar. For reusable configurations, right-click the module and select **Save to Library** to store it as a preset that can be reused across your site.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Social Media Follow settings and class names may differ from Divi 4.

## Troubleshooting

!!! warning "Icons Not Linking to Profiles"
    If clicking a social icon does not navigate to the correct profile:

    - Verify that the **Profile URL** field contains a complete URL including `https://`.
    - Ensure the URL points to a valid, publicly accessible profile page.
    - If the link opens but shows a 404 error, double-check that the username or handle in the URL is correct.

!!! warning "Icons Displaying Incorrect Brand Colors"
    If the icon colors do not match the expected platform branding:

    - Check whether a custom **Background Color** or **Icon Color** override has been set on the individual item that is overriding the default brand color.
    - Design tab icon styling may apply a global color that overrides per-item brand colors. Review the icon color settings at the module level.
    - Custom CSS targeting the social follow module may be overriding the inline brand color styles.

!!! warning "Icons Not Aligning Properly"
    If the social icons are not positioned as expected within their container:

    - Check the **Alignment** setting in the Design tab and set it to your desired position (left, center, or right).
    - If the module is inside a column with text alignment set, the column's alignment may conflict with the module's own alignment setting.
    - On narrow columns, icons may wrap to a second line. Either reduce the number of visible networks or decrease the icon size.

## Related

- [Person](person.md) — Display team member profiles with photo, bio, and social links
- [Icon](icon.md) — Display a single decorative or functional icon
