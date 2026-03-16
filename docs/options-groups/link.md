---
title: "Link Options"
category: options-groups
tags: ["options-groups", "link", "advanced"]
related: ["meta", "attributes"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10066994"
---

# Link Options

The Link options group turns an entire module into a clickable hyperlink, directing visitors to another page, section, or external URL.

## Overview

The Link options group provides a simple way to make any supported module function as a hyperlink without needing to wrap it in an anchor tag manually. When a Module Link URL is set, clicking anywhere on the module navigates the visitor to the specified destination. This is commonly used for card-style layouts, image modules, or blurb modules where the entire element should be clickable rather than just a specific text link or button within it.

The settings are located under the Content tab of the module's settings panel, keeping them close to the other content-related options. You specify the destination URL and choose whether the link should open in the same browser window or in a new tab. Opening in the same window is the default and works well for internal navigation, while opening in a new tab is appropriate for external links where you want to keep the visitor on your site.

This feature is distinct from button links or text hyperlinks that exist within a module's content. The Module Link wraps the entire element, so every clickable area within the module will navigate to the specified URL.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10066994).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Module Link URL | Text input | Specifies the destination URL. When set, the entire module becomes clickable. Accepts internal paths, full URLs, and anchor links. |
| Module Link Target | Dropdown | Controls how the link opens. Options are In the Same Window (default, navigates in the current tab) and In a New Tab (opens the destination in a new browser tab while preserving the current page). |

## Which Elements Use This

The Link options group is available on modules in the Divi 5 Visual Builder that support module-level linking. The settings are found under the **Content** tab of the module's settings panel.

## Code Examples

```css
/* Add a pointer cursor and hover effect to linked modules */
.et_pb_module[data-module-link] {
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.et_pb_module[data-module-link]:hover {
  opacity: 0.9;
}
```

```css
/* Style a card-like linked blurb module */
.linked-card {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.linked-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}
```

## Related

- [Meta Options](meta.md)
- [Attributes Options](attributes.md)
