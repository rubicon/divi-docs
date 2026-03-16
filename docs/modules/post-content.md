---
title: "Post Content"
description: "Complete Divi 5 Post Content module reference — settings, design options, code examples, and troubleshooting for displaying dynamic post body content in Theme Builder templates."
category: modules
tags: ["modules", "content-modules", "posts", "dynamic-content", "theme-builder", "text"]
related: ["post-title", "text", "comments"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10587147"
---

# Post Content

The Post Content module renders the full body content of a WordPress post or page within Theme Builder templates, including all text, images, embeds, and formatting from the post editor.

!!! abstract "Quick Reference"
    **What it does:** Dynamically displays the main content body of the current post or page in a Theme Builder template.
    **When to use it:** Theme Builder templates for blog posts, pages, and custom post types
    **Key settings:** Heading Text, Body Text, Image, Background
    **Block identifier:** `divi/post-content`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10587147)

!!! tip "When to Use This Module"
    - Building a Theme Builder template for blog posts that needs to display the post body content
    - Creating custom single-post layouts where the content area is styled separately from other elements
    - Designing page templates that render the WordPress editor content dynamically

!!! warning "When NOT to Use This Module"
    - For static text content authored directly in the Visual Builder — use [Text](text.md)
    - For displaying only the post title — use [Post Title](post-title.md)
    - For displaying the post comments section — use [Comments](comments.md)

## Overview

The Post Content module is an essential building block for any Theme Builder template. When you create a custom template for blog posts, pages, or custom post types in the Divi Theme Builder, the actual content authored in the WordPress editor needs a designated place to render. The Post Content module provides that outlet — it dynamically pulls the full body content from whatever post or page is being viewed and displays it within the template layout.

The content rendered by this module includes everything written in the WordPress block editor or classic editor: paragraphs, headings, lists, images, videos, embedded content, shortcodes, and any HTML markup. The module acts as a transparent passthrough that respects the formatting and structure of the original content while allowing you to apply consistent styling through the Design tab settings.

The Design tab offers controls for heading text and body text styling, which apply uniformly to all headings and body paragraphs within the rendered content. Image styling controls let you apply borders, shadows, or other visual treatments to images embedded in the post content. This is particularly useful for enforcing consistent visual standards across all posts without needing to style each one individually.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10587147).

<!-- ![Post Content module](../assets/screenshots/modules/post-content/element.png){ loading=lazy } -->
<!-- *The Post Content module rendering a blog post's body text, headings, and images within a Theme Builder template.* -->

## Use Cases

1. **Blog Post Template** — Place the Post Content module between the Post Title and Comments modules in a Theme Builder blog post template to create the standard reading layout where the main article content flows naturally between the header and discussion sections.
2. **Custom Page Template** — Use the module in a page template to render page content within a custom layout that includes a sidebar, header, footer, or other design elements not possible with the standard page builder approach.
3. **CPT Detail Template** — For custom post types (events, team members, recipes, etc.), the Post Content module renders whatever content was entered in the WordPress editor, allowing you to build a consistent detail page template while authors fill in the content through the standard editing interface.

## How to Add the Post Content Module

1. Navigate to **Divi > Theme Builder** and create or edit a template for the desired post type.
2. Open the Visual Builder on the template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Post Content" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10587147).

## Settings & Options

The Post Content module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab is minimal for this module, as the actual content is pulled dynamically from the current post. It provides background and layout ordering options.

| Setting | Type | Description |
|---------|------|-------------|
| Background | background controls | Set a background color, gradient, image, or video behind the post content module container. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |

<!-- ![Post Content Content tab settings](../assets/screenshots/modules/post-content/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls how the dynamically rendered content is styled, including headings, body text, and embedded images.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Image | image styling | Apply design effects to images embedded within the post content, including border, shadow, and spacing. |
| Heading Text | text styling | Customize the font, size, color, weight, and spacing of all heading elements (h1-h6) within the rendered post content. |
| Body Text | text styling | Style the body paragraphs and inline text within the post content, including font family, size, color, line height, and link styling. |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, hue, saturation, blending) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Post Content Design tab settings](../assets/screenshots/modules/post-content/settings-design.png){ loading=lazy } -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Choose the semantic HTML tag for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |

<!-- ![Post Content Advanced tab settings](../assets/screenshots/modules/post-content/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the post content container */
.et_pb_post_content {
    max-width: 720px;
    margin: 0 auto;
    line-height: 1.8;
}

/* Style headings within post content */
.et_pb_post_content h2 {
    font-size: 28px;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 16px;
    color: #222;
}

.et_pb_post_content h3 {
    font-size: 22px;
    font-weight: 600;
    margin-top: 30px;
    margin-bottom: 12px;
    color: #333;
}

/* Style paragraphs */
.et_pb_post_content p {
    font-size: 17px;
    color: #444;
    margin-bottom: 1.5em;
}

/* Style images within content */
.et_pb_post_content img {
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    margin: 20px 0;
}

/* Style blockquotes */
.et_pb_post_content blockquote {
    border-left: 4px solid #2ea3f2;
    padding: 15px 20px;
    margin: 25px 0;
    background: #f8f9fa;
    font-style: italic;
    color: #555;
}

/* Style code blocks */
.et_pb_post_content pre {
    background: #1e1e1e;
    color: #f8f8f2;
    padding: 20px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 14px;
}

/* Style links within content */
.et_pb_post_content a {
    color: #2ea3f2;
    text-decoration: underline;
    text-decoration-color: rgba(46, 163, 242, 0.3);
    transition: text-decoration-color 0.2s ease;
}

.et_pb_post_content a:hover {
    text-decoration-color: #2ea3f2;
}

/* Responsive typography */
@media (max-width: 980px) {
    .et_pb_post_content h2 {
        font-size: 24px;
    }
    .et_pb_post_content p {
        font-size: 16px;
    }
}
```

### PHP Hooks

```php
/* Filter the Post Content module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_post_content' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Add content before or after the post content */
add_filter('the_content', function($content) {
    if (is_single()) {
        $content .= '<div class="post-content-footer">Thank you for reading!</div>';
    }
    return $content;
});
```

## Common Patterns

1. **Centered Reading Layout** — Constrain the Post Content module width to 700-750px and center it horizontally using auto margins. This creates an optimal reading column width that improves readability for long-form blog posts, similar to Medium or Substack article layouts.

2. **Two-Column Post with Sidebar** — Place the Post Content module in the wider column of a two-column row, with a sidebar column containing related posts, author bio, or table of contents. This classic layout provides content and context side by side.

3. **Full-Width with Contained Text** — Place the module in a full-width row but use the Sizing settings to set a max-width on the text content while allowing images to extend wider. This creates a modern editorial layout where text is readable but images make a visual impact.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/post-content` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For dynamic post body content in Theme Builder templates use Post Content; for static text authored in the Visual Builder use Text; for the post title use Post Title; for comments use Comments.

## Saving Your Work

After configuring the post content module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Post Content module does not appear on the front end, verify that:

    - The module is placed inside a Theme Builder template (not a regular page built with the Visual Builder)
    - The template is assigned to the correct post type or specific posts/pages
    - The post or page being viewed has actual content in its WordPress editor

!!! warning "Content Appears Unstyled or Broken"
    If the content renders but does not look right, check that:

    - Design tab settings for Heading Text and Body Text are not conflicting with your theme's global CSS
    - The original content was authored in the WordPress editor (not within Divi builder blocks on the post itself)
    - Shortcodes in the content are from active plugins

!!! tip "Post Content Shows Builder Layout Instead of Text"
    If the post was built using the Visual Builder rather than the WordPress editor, the Post Content module will render the Divi builder output. For Theme Builder templates, it is typical to author posts using the standard WordPress editor and use the Post Content module to render that content within the template layout.

## Related

- [Post Title](post-title.md) — Displays the post title dynamically in Theme Builder templates
- [Text](text.md) — Static text module for content authored in the Visual Builder
- [Comments](comments.md) — Displays the post comments section
- [Blog](blog.md) — Blog post feed with excerpts and pagination
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
