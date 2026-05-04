---
title: "Social Media Follow"
description: "Complete Divi 5 Social Media Follow module reference — platform icons, profile links, Link Target (new tab), Theme Options social icons, brand colors, alignment, and button styling."
category: modules
tags: ["modules", "social-media", "social-icons", "follow-buttons", "networking", "social-links"]
related: ["person", "icon", "general"]
divi_version: "5.x"
last_updated: 2026-05-04
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
| Icon | icon settings | Configure the default icon style, **link target** (same window or new tab), and related behavior that applies across all social network items in the module. Individual items only expose profile URL and per-network colors — see [Open social icons in a new tab](#open-social-icons-in-a-new-tab). |
| Background | background controls | Set a background color, gradient, image, or video behind the entire social media follow module. |
| Loop | toggle | Control repeating behavior for the social network items. |
| Order | select | Control the display order of the social network items within the module. |
| Meta | admin label | Set an internal label for the module visible only in the Visual Builder's layer panel. |

#### Icon (parent module)

Expand the **Icon** section at the parent **Social Media Follow** module level (not inside a child Social Network item) to set options that apply to every icon at once.

| Setting | Type | Description |
|---------|------|-------------|
| Link Target | select | **In The Same Window** (default) or **In A New Tab**. Controls where all profile links open. There is no per-network override at the child level. |

#### Individual Social Network Item Settings

Each social network item within the module has its own configuration panel:

| Setting | Type | Description |
|---------|------|-------------|
| Social Network | select | Choose the social platform from the available list (Facebook, Twitter/X, Instagram, LinkedIn, YouTube, Pinterest, TikTok, and many more). This determines the default icon and brand color. |
| Profile URL | url | The full URL to your profile on the selected platform. This is where visitors are directed when they click the icon. Child items do not include a separate link-target field — use the parent module's **Link Target** under **Icon**. |
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

### PHP: Add rel attributes to social links (optional)

For the Social Media Follow module, prefer the **Link Target** control under **Content → Icon** so Divi outputs correct `target` and relationship attributes. Use this filter only if you must alter markup programmatically (for example legacy layouts or third-party patches).

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

## Open social icons in a new tab

Divi 5 can show social icons in two different ways, and each needs a different approach if you want links to open in a new tab.

### Which fix do I need?

**Are the icons in your header or footer set via Divi → Theme Options → General → Social Media Profiles?**

→ Use **Fix 1: Theme Options icons** (snippet required). Those URLs live in [General theme options](../theme-options/general.md); there is no native “open in new tab” toggle there.

**Are the icons from a Social Media Follow module on a layout or in a Theme Builder template?**

→ Use **Fix 2: Social Media Follow module** (UI only, no code).

**Not sure?** Open the page in the Visual Builder. If clicking an icon opens a module settings panel, it is the module (Fix 2). If the icons are not selectable as a module and only appear in the header or footer from theme integration, they are Theme Options icons (Fix 1).

---

### Fix 1: Theme Options icons (snippet required)

The header and footer social icons configured under **Divi → Theme Options → General** use a different markup path than this module. Add a small script so those links use `target="_blank"` and a safe `rel` value site-wide.

#### The gotcha: Divi 5 may defer or relocate jQuery

Under **Theme Options → Performance**, options such as **Defer jQuery and jQuery Migrate** and **Dynamic JavaScript Libraries** can move jQuery to the footer or load it asynchronously. An inline `<script>` that calls `jQuery` or `$` before the library is available throws `ReferenceError: jQuery is not defined`, which can halt execution and break other scripts (sliders, carousels, lazy-loaded modules).

Both options below avoid that failure mode.

#### Option A — Quick fix via Theme Options (polling)

Paste into **Divi → Theme Options → Integration → Add code to the `<body>`** (see [Integration](../theme-options/integration.md)):

```html
<script>
(function waitForJQuery() {
  if (typeof jQuery !== 'undefined') {
    jQuery(function($) {
      $('.et-social-icon a').attr({
        'target': '_blank',
        'rel': 'noopener noreferrer'
      });
    });
  } else {
    setTimeout(waitForJQuery, 50);
  }
})();
</script>
```

The function checks every 50ms until jQuery is available, then runs once. If jQuery is already loaded, it runs immediately. This pattern suits quick iteration and smaller sites without a child theme workflow.

#### Option B — Production-style via child theme `functions.php`

Hook into `wp_footer` so the script prints after Divi has enqueued jQuery — no polling:

```php
add_action('wp_footer', function() { ?>
  <script>
    jQuery(function($) {
      $('.et-social-icon a').attr({
        'target': '_blank',
        'rel': 'noopener noreferrer'
      });
    });
  </script>
<?php }, 100);
```

Priority `100` helps ensure output after jQuery is printed. Keeping this in a child theme keeps custom code in version control rather than the database.

---

### Fix 2: Social Media Follow module (no code)

The Social Media Follow module includes a **Link Target** setting at the **parent module** level. It applies to all child “Social Network” items at once. If you click an icon in the builder, the sidebar may open the **child** panel, which only shows **Profile URL** and no target field — that is the wrong panel.

**Steps**

1. Open the page in the **Visual Builder**.
2. Click a social icon. If you see only **Account Link URL** / **Profile URL** and no target option, you are in the child **Social Network** panel.
3. Use the breadcrumb at the top of the settings sidebar (for example `Footer › Section › Row › Column › … › Social Network`) and click the **back** arrow next to **Social Network**, or click the **Social Media Follow** parent in the breadcrumb until the panel title reads **Social Media Follow**.
4. Open the **Content** tab and expand the **Icon** section on the **parent** module.
5. Set **Link Target** to **In A New Tab** (default is **In The Same Window**).
6. Save the module, save the page, and exit the Visual Builder.

One setting updates every icon in that module instance.

**Across the site**

If the module appears in multiple places or lives in a global header or footer from Theme Builder, edit the **Global** header/footer template (or the global module) once and set **Link Target** there so the change propagates. If the same module was duplicated page by page instead of made global, consider converting it to a global module so future URL or target changes stay in one place.

If both Theme Options icons and a Social Media Follow module appear on the same page, duplicate icons confuse visitors — usually keep the module (more flexible) and clear the social URLs under Theme Options → General.

---

### Why `rel="noopener noreferrer"`

Without `rel="noopener"`, links that use `target="_blank"` can expose `window.opener` to the destination page (a tabnabbing risk). Modern browsers often mitigate this; setting `rel` explicitly is still good practice. The Social Media Follow module’s **In A New Tab** option handles this for module output. The Fix 1 snippets add `noopener noreferrer` explicitly.

!!! note "Person / Team Member module"
    Social icons in the [Person](person.md) module use different markup (for example `.et_pb_member_social_links`). This page does not cover that case; use a separate selector if you need the same behavior there.

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

!!! warning "Sliders, carousels, or lazy images break after a Theme Options body snippet"
    If you added Fix 1 inline JavaScript and other scripts stopped working, open DevTools → Console and look for `jQuery is not defined`. Divi may have deferred jQuery so the script ran too early. Switch to the polling snippet (Fix 1 Option A) or the `wp_footer` hook (Fix 1 Option B) in [Open social icons in a new tab](#open-social-icons-in-a-new-tab).

!!! warning "Only Profile URL in the panel — no Link Target"
    You are editing a child **Social Network** item. Navigate up to the parent **Social Media Follow** module (breadcrumb back arrow or parent name), then **Content → Icon → Link Target**. See [Fix 2](#fix-2-social-media-follow-module-no-code).

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

- [General theme options](../theme-options/general.md) — Social Media Profiles URLs in Theme Options (Fix 1 for new-tab behavior uses `.et-social-icon a`)
- [Integration](../theme-options/integration.md) — Add code to `<body>` for Theme Options snippet placement
- [Person](person.md) — Display team member profiles with photo, bio, and social links
- [Icon](icon.md) — Display a single decorative or functional icon
