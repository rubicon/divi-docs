---
title: "Social Media Follow"
category: modules
tags: ["modules", "social-media", "social-icons", "follow-buttons", "networking", "social-links"]
related: ["person", "icon"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10364982-the-social-media-follow-module-in-divi-5"
---

# Social Media Follow

The Social Media Follow module displays linked social media icons that direct visitors to your profiles on various platforms.

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

| Setting | Type | Description |
|---------|------|-------------|
| Alignment | alignment control | Set the horizontal alignment of the social icons within the module container (left, center, or right). |
| Icon | icon styling | Customize the icon appearance including color, size, and hover state behavior across all items in the module. |
| Text | text styling | Style any visible text labels associated with the social network items, including font family, size, weight, color, letter spacing, and line height. |
| Follow Button | button styling | Control the shape and appearance of the follow button containers, including background color, border radius, padding, and hover state transitions. |
| Sizing | dimension controls | Set the module width, max width, and horizontal alignment within its column. |
| Spacing | margin/padding | Configure external margin and internal padding for the module. Responsive values can be set independently for each breakpoint. |
| Border | border styling | Add and customize borders around the module including width, color, style, and per-corner radius values. |
| Box Shadow | shadow controls | Apply a box shadow to the module with configurable horizontal offset, vertical offset, blur, spread, and color. |
| Filters | image filters | Apply CSS filter effects to the module including hue rotation, saturation, brightness, contrast, inversion, sepia, and blur. |
| Transform | transform controls | Apply CSS transforms including scale, translate, rotate, skew, and transform origin adjustments. |
| Animation | animation controls | Configure the module entrance animation triggered when scrolling into view, with style, direction, duration, delay, and intensity options. |

### Advanced Tab

The Advanced tab provides low-level controls for custom attributes, CSS targeting, conditional display logic, and scroll-driven effects.

| Setting | Type | Description |
|---------|------|-------------|
| Attributes | id/class inputs | Assign a unique CSS ID and one or more CSS classes to the module for targeting with custom CSS or JavaScript. |
| CSS | custom CSS editor | Add custom CSS rules targeting specific internal elements of the social media follow module such as the icon container, individual icons, and link wrappers. |
| HTML | html attributes | Configure additional HTML attributes on the module wrapper element. |
| Conditions | display logic | Set conditions that determine when the module is displayed, such as user role, page type, or custom logic rules. |
| Interactions | event handlers | Define interactive behaviors triggered by user actions like click or hover events on the module. |
| Visibility | device toggles | Control which devices display this module by toggling visibility independently for desktop, tablet, and phone. |
| Transitions | transition controls | Set the duration and timing of hover transition effects on interactive elements within the module. |
| Position | positioning controls | Configure the CSS positioning scheme (static, relative, absolute, fixed, or sticky), along with z-index and offset values. |
| Scroll Effects | scroll transforms | Enable transform effects like rotation, scaling, fading, and blur driven by the visitor's scroll position relative to the module. |

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
