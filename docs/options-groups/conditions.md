---
title: "Conditions Options"
description: "Divi 5 Conditions options group — dynamic display rules based on login status, device, browser, OS, and visitor behavior."
category: options-groups
tags: ["options-groups", "conditions", "advanced"]
related: ["visibility", "css"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10102758"
---

# Conditions Options

The Conditions options group lets you define rules that determine whether an element is displayed on the front end, enabling personalized content based on user behavior and system attributes.

!!! abstract "Quick Reference"
    **What it controls:** Dynamic display rules using login status, visited pages, device, browser, OS, and purchase history
    **Where to find it:** Advanced Tab → Conditions
    **Available on:** All modules
    **Responsive:** No — conditions evaluate at page load based on visitor context, not device breakpoints
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10102758)

## Overview

Conditions go beyond simple device-based visibility by evaluating dynamic criteria at page load. Instead of hiding an element from all mobile users, for instance, you can show it only to logged-in visitors who are using Chrome on a desktop. This makes Conditions a powerful tool for personalization and targeted messaging.

Each condition rule specifies a single criterion, and you can stack multiple rules on the same element. When multiple conditions are present, they are evaluated together using AND logic, meaning every condition must be met for the element to appear. This combinatorial approach lets you build precise audience segments without writing any code.

The Visual Builder includes a built-in preview mode for conditions, so you can simulate different user scenarios (device type, browser, login status) and verify that elements show or hide as expected before publishing.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10102758).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Add Condition | Button | Opens the condition builder and lets you add a new visibility rule to the element. |
| Logged-In Status | Condition selector | Shows or hides the element depending on whether the visitor is logged in or logged out. |
| Visited Page | Condition selector | Displays the element only if the visitor has previously viewed a specific page on the site. |
| Purchase History | Condition selector | Displays the element only to visitors who have completed a prior purchase, useful for WooCommerce stores. |
| Device Type | Condition selector | Targets visitors by device category: mobile, tablet, or desktop. |
| Browser Type | Condition selector | Targets visitors by their browser, such as Chrome, Safari, Firefox, or Edge. |
| Operating System | Condition selector | Targets visitors by their operating system, such as iOS, Android, Windows, or macOS. |

## Which Elements Use This

All modules in the Divi 5 Visual Builder include the Conditions options group. The settings are found under the **Advanced** tab of any element's settings panel.

## Code Examples

Conditions are configured entirely through the Visual Builder interface and do not require custom code. However, you can use conditions alongside custom CSS for more advanced use cases:

```css
/* Style an element that only appears for logged-in users */
.member-exclusive-banner {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  padding: 20px;
  border-radius: 8px;
}
```

## Related

- [Visibility Options](visibility.md)
- [CSS Options](css.md)
- [Condition Options](../builder/condition-options.md) — Builder-level condition system for advanced display rules
- [Dynamic Content](../builder/dynamic-content.md) — Pull conditional values from post meta and user data
- [Login Module](../modules/login.md) — Show login forms conditionally based on user authentication state
