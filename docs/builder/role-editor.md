---
title: "Role Editor"
description: "Divi 5 Role Editor — control which Divi builder features, settings tabs, module types, and library actions are available per WordPress user role."
category: builder
tags: ["builder", "permissions", "roles", "users", "security", "access-control"]
related: ["visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13820812-the-role-editor-in-divi-5"
---

# Role Editor

The Role Editor restricts which Divi builder features, settings tabs, module types, and library actions are available to each WordPress user role.

!!! abstract "Quick Reference"
    **What it does:** Provides granular permission controls that limit what each WordPress user role can access and modify within Divi 5.
    **Where to find it:** WordPress admin > Divi > Role Editor
    **Key features:** Per-role toggles for theme privileges, builder interface actions, library access, settings tabs, settings types, module use, Support Center, portability, and Divi AI
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/13820812-the-role-editor-in-divi-5)

## Overview

The Divi Role Editor gives site administrators precise control over what each WordPress user role can do inside Divi 5. By default, every role that has access to the WordPress editor can use the full range of Divi features. The Role Editor lets you lock down specific capabilities so that clients, guest authors, or junior editors only see the tools they need.

This is especially important on multi-author sites, client sites, or agency builds where you want to prevent accidental changes to global styles, theme options, or advanced module settings. Rather than relying on generic WordPress capabilities alone, the Role Editor adds a Divi-specific permission layer on top of the standard WordPress role system.

Each WordPress user role gets its own panel with identical toggle groups. You configure permissions per role, and those restrictions apply immediately to all users assigned that role. Custom roles created by third-party plugins also appear in the Role Editor and can be configured the same way.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13820812-the-role-editor-in-divi-5).

<!-- ![Role Editor overview](../assets/screenshots/builder/role-editor/overview.png){ loading=lazy } -->
<!-- *The Role Editor interface in Divi 5.* -->

## How to Access the Role Editor

1. Log in to WordPress as an Administrator.
2. Navigate to **Divi > Role Editor** in the WordPress admin sidebar.
3. Select the user role you want to configure from the available role panels.
4. Adjust the permission toggles as needed.
5. Click **Save Divi Roles** to apply your changes.

## WordPress User Roles

The Role Editor displays a configurable panel for each standard WordPress user role, plus any custom roles registered on the site:

| Role | Default WordPress Capabilities | Typical Role Editor Use |
|------|-------------------------------|------------------------|
| **Administrator** | Full access to all WordPress and Divi features | Usually left unrestricted; lock down only if multiple admins share access |
| **Editor** | Can publish and manage all posts/pages | Common client role — restrict theme options, advanced settings, and library management |
| **Author** | Can publish and manage their own posts only | Restrict to content editing; disable theme-level and structural changes |
| **Contributor** | Can write and save drafts but cannot publish | Limit to basic content entry; disable builder, library, and design controls |
| **Subscriber** | Can only manage their own profile | No builder access by default |
| **Shop Manager** | WooCommerce role — manages products and orders | Mirrors Editor defaults; restrict Divi features as needed |
| **Custom Roles** | Varies by plugin | Any roles created by third-party plugins (e.g., membership or LMS plugins) also appear and can be configured |

## Settings & Permissions Reference

Each user role panel contains the following permission groups. Every setting within each group is an independent toggle that can be enabled or disabled.

### Divi Theme Privileges

Controls access to top-level Divi admin features outside the builder.

| Permission | Description |
|-----------|-------------|
| Theme Options | Access the Divi > Theme Options panel in the WordPress admin |
| Theme Builder | Access the Divi > Theme Builder for creating header, footer, and body templates |
| Divi Library | Access the Divi > Divi Library for managing saved layouts, sections, rows, and modules |
| Theme Customizer | Access the Divi > Theme Customizer for site-wide styling controls |
| Divi AI | Use Divi AI features for content generation and image creation |
| Quick Sites | Access the Quick Sites wizard for one-click site creation |
| Portability | Access import/export functionality for Divi layouts and options |

### Builder Interface

Controls what structural actions a user can perform inside the Visual Builder.

| Permission | Description |
|-----------|-------------|
| Use Divi Builder | Enable or disable access to the Visual Builder entirely for this role |
| Edit Modules | Allow editing module settings within the builder |
| Edit Rows | Allow editing row settings |
| Edit Sections | Allow editing section settings |
| Move Modules | Allow dragging modules to reorder or reposition them |
| Move Rows | Allow dragging rows to reorder them |
| Move Sections | Allow dragging sections to reorder them |
| Delete Modules | Allow deleting modules from the layout |
| Delete Rows | Allow deleting rows from the layout |
| Delete Sections | Allow deleting sections from the layout |

### Library Settings

Controls access to the Divi Library within the builder interface.

| Permission | Description |
|-----------|-------------|
| Access Divi Library | Allow browsing and loading items from the Divi Library inside the builder |
| Edit Global Modules | Allow editing global (synced) modules, rows, and sections — restricting this is recommended for client roles to prevent unintended site-wide changes |

### Settings Tabs

Controls which module/row/section settings tabs are visible.

| Permission | Description |
|-----------|-------------|
| Content Tab | Access the Content tab in module, row, and section settings |
| Design Tab | Access the Design tab for visual styling controls |
| Advanced Tab | Access the Advanced tab for CSS, conditions, visibility, and developer settings |

### Settings Types

Controls access to specific categories of settings across all tabs.

| Permission | Description |
|-----------|-------------|
| Text Settings | Access text and content input fields |
| Color Settings | Access color pickers and color-related controls |
| Layout Settings | Access layout, sizing, spacing, and structural controls |

### Module Use

Controls which individual module types a user can insert and edit. Each Divi module has its own toggle. When a module is disabled for a role, users with that role cannot add new instances of that module and cannot edit existing instances.

This is useful for limiting clients to a subset of modules. For example, you might allow only the Text, Image, and Button modules for an Author role while disabling more complex modules like Code, Theme Builder, or Fullwidth modules.

### Support Center

Controls access to the Divi Support Center features.

| Permission | Description |
|-----------|-------------|
| Access Support Center | Allow opening the Divi Support Center panel |
| Contact Support | Allow submitting support requests to Elegant Themes |
| Enable Safe Mode | Allow activating Safe Mode for troubleshooting |
| Grant Remote Access | Allow granting Elegant Themes support team remote access to the site |

### Portability

Controls import and export capabilities.

| Permission | Description |
|-----------|-------------|
| Import | Allow importing layouts, presets, and theme options from JSON files |
| Export | Allow exporting layouts, presets, and theme options to JSON files |

## Interface Controls

The Role Editor interface includes several utility features:

- **Save Divi Roles** — Saves all permission changes across all roles at once.
- **Toggle All** — Quickly enable or disable all permissions within a group. Useful for rapidly configuring a restrictive role.
- **Undo** — Reverts the most recent unsaved change.
- **Portability** — Import or export role configurations as JSON files. This lets you replicate permission setups across multiple sites.

## Use Case Example: Client Editor Role

A common scenario is configuring the Editor role for a client who should be able to update page content but not modify the site's overall design or structure:

1. Open the **Editor** role panel.
2. Under **Divi Theme Privileges**, disable Theme Options, Theme Builder, Theme Customizer, and Portability. Leave Divi Library enabled if the client needs access to saved layouts.
3. Under **Builder Interface**, keep Edit Modules enabled but disable Move Sections, Delete Sections, and Delete Rows to prevent structural changes.
4. Under **Settings Tabs**, disable the **Advanced Tab** to prevent access to custom CSS, conditions, and developer settings.
5. Under **Module Use**, disable complex modules like Code, Fullwidth modules, or any modules the client does not need.
6. Click **Save Divi Roles**.

## Best Practices

1. **Start restrictive, then open up** — It is easier to grant additional permissions when a user requests them than to recover from unintended changes made with too-broad access.

2. **Test as the configured role** — After saving role settings, log in as a user with that role (or use a role-switching plugin) to verify the restrictions work as expected. Some permissions interact with each other, and testing ensures the experience matches your intent.

3. **Protect global modules** — Disable "Edit Global Modules" for any role that should not make site-wide changes. Editing a global module updates every instance across the site, which can cause unintended layout changes.

4. **Document your configuration** — Use the Portability export feature to save a JSON backup of your role settings. Store it alongside your site documentation so the configuration can be restored or replicated on other installations.

5. **Restrict Divi AI for non-admin roles** — If you want to control AI-generated content quality or manage API usage costs, disable Divi AI access for roles that do not need it.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Role Restrictions Not Taking Effect"
    If a user can still access features you have disabled:

    - Confirm the user's WordPress role matches the role you configured in the Role Editor. Check their profile under Users > All Users.
    - Verify you clicked **Save Divi Roles** after making changes. Unsaved changes are not applied.
    - Clear any page caches or object caches that might be serving a stale version of the builder interface.
    - If the user is an Administrator, note that some restrictions may not apply to the Administrator role by design.

!!! warning "Module Still Visible After Disabling"
    If a module type is disabled under Module Use but still appears in existing layouts:

    - Disabling a module prevents adding new instances and editing existing ones. The module may still render on the front end in published content.
    - To fully remove a module from a page, an Administrator must edit the layout and delete the module instance.

!!! tip "Resetting Role Editor to Defaults"
    If role permissions become misconfigured, you can reset them by using the Portability feature to import a clean default configuration, or by toggling all permissions back to enabled for the affected role and re-configuring from scratch.

## Related

- [Visual Builder](visual-builder.md) — The page editing interface controlled by Role Editor permissions
- [Theme Builder](theme-builder.md) — Template management that can be restricted per role
