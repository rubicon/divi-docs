---
title: "Attributes Options"
category: options-groups
tags: ["options-groups", "attributes", "advanced"]
related: ["css", "meta"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102703"
---

# Attributes Options

The Attributes options group lets you assign CSS IDs, CSS classes, and custom HTML attributes to any element, providing hooks for custom styling and JavaScript targeting.

## Overview

Every element in Divi 5 includes an Attributes options group under the Advanced tab. The primary purpose of these settings is to give you a way to reference specific elements from your own CSS or JavaScript code. By assigning a unique ID or one or more reusable classes, you can write targeted styles that apply only to the elements you choose.

Beyond IDs and classes, the Attributes group also supports adding arbitrary HTML attributes with custom name-value pairs. This is useful for accessibility enhancements (such as `aria-label` or `role`), data attributes for JavaScript interaction, or any other HTML attribute your project requires. You can specify which sub-element within the module receives the attribute using the Target Element selector.

IDs must be unique across the entire page and cannot begin with a number or contain spaces or special characters. Classes can be reused on multiple elements, and you can assign several classes to a single element by separating them with spaces.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102703).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| CSS ID | Text input | Assigns a unique identifier to the element. Must be unique on the page, cannot start with a number, and cannot contain spaces or special characters like @, #, or &. |
| CSS Classes | Text input | Assigns one or more reusable class names to the element. Separate multiple classes with spaces. Cannot start with a number or contain # symbols. |
| Attribute Name | Text input | Specifies the HTML attribute to add (e.g., `class`, `id`, `data-custom`, `aria-label`). |
| Attribute Value | Text input | Specifies the value for the custom HTML attribute. |
| Target Element | Dropdown | Determines which sub-element within the module receives the custom attribute. The default target is the Module wrapper. |

## Which Elements Use This

All modules, columns, rows, and sections in the Divi 5 Visual Builder include the Attributes options group. The settings are found under the **Advanced** tab.

## Code Examples

After assigning a CSS ID or class in the Attributes settings, target the element in your custom CSS:

```css
/* Target an element by its CSS ID */
#hero-cta-button {
  background-color: #e53e3e;
  font-weight: 700;
  letter-spacing: 1px;
}
```

```css
/* Target elements sharing a CSS class */
.card-shadow {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

.card-shadow:hover {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}
```

Using custom data attributes for JavaScript:

```javascript
// Target elements with a custom data attribute
document.querySelectorAll('[data-track-click]').forEach(el => {
  el.addEventListener('click', () => {
    analytics.track('element_click', {
      label: el.getAttribute('data-track-click')
    });
  });
});
```

## Related

- [CSS Options](css.md)
- [Meta Options](meta.md)
