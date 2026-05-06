---
title: "Backward Compatibility and Third-Party Divi Module Support"
category: builder
tags: ["builder", "migration", "compatibility", "third-party", "modules"]
related: ["what-is-the-divi-5-migrator-system.md", "how-to-safely-migrate-from-divi-4-to-divi-5.md", "how-to-rollback-to-divi-4.md", "divi-5-faq.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/9824521-backward-compatibility-and-third-party-divi-module-support"
---

# Backward Compatibility and Third-Party Divi Module Support

Divi 5 maintains backward compatibility with Divi 4 content while introducing a completely new architecture. Third-party modules are supported through a compatibility mode bridge, though full feature parity requires publisher updates.

## Overview

While Divi 5 represents a major architectural shift from Divi 4, backward compatibility is a core priority. Most existing Divi 4 content continues to function after upgrading, though some limitations apply.

**Key points:**
- Core Divi modules are fully compatible with Divi 5
- Third-party modules run in compatibility mode if not yet updated for Divi 5
- Some Divi 4 features (Quick Access, Full Site Editing, Draggable Spacing) are not yet available in Divi 5
- Unsupported modules may cause performance slowdowns on individual pages
- You can rollback to Divi 4 at any time

The compatibility strategy allows sites to benefit from Divi 5's modern architecture while waiting for third-party developers to release Divi 5-native versions of their plugins.

## Backward Compatibility Mode

### What It Does

When a page contains unsupported Divi 4 modules, Divi 5 automatically loads the Divi 4 framework for that page only. This allows older modules to function, but with performance limitations.

### Performance Impact

- **Pages with only Divi 5 modules** — Full Divi 5 performance and speed improvements
- **Pages with unsupported Divi 4 modules** — Divi 4 framework loads, reducing speed gains for that page only
- **Builder experience** — Unsupported modules can be edited using Divi 5's Visual Builder with backward compatibility mode active

### Admin Notification

When viewing a page with unsupported modules in the frontend, a notification appears in the WordPress Admin bar showing which modules need updates. Clicking the notification provides detailed compatibility information.

!!! warning "Performance Considerations"
    Backward compatibility mode is a temporary bridge. For optimal performance, migrate to fully Divi 5-compatible modules as soon as available.

## Third-Party Module Support Status

### Checking Compatibility

Check module compatibility directly in the [Divi Marketplace](https://www.elegantthemes.com/marketplace/). Each product page displays its Divi 5 compatibility status.

### Marketplace Creator Updates

Many third-party developers are actively updating their products for Divi 5 native support. Compatibility improves regularly as more products are released. If a module shows no Divi 5 compatibility badge, contact the author—they may have an update in progress.

### Unsupported Modules in Divi 5

When migrating a site with unsupported third-party modules:
- The modules are automatically wrapped in the Divi 4 framework during migration
- They continue to display and function on the frontend
- They can be edited in the builder using backward compatibility
- The affected page will load the Divi 4 framework, affecting performance

## Opt-Out Mechanism for Plugin Authors

### How It Works

Third-party plugin authors can opt out of Divi 5 compatibility. When a plugin has opted out:
- The plugin cannot be activated while Divi 5 is active
- An error message prevents activation and lists the conflicting plugin(s)
- You must deactivate the plugin to use Divi 5

### If You Need the Plugin

If you require a plugin that has opted out of Divi 5 compatibility, you can [rollback to Divi 4](how-to-rollback-to-divi-4.md).

## Feature Availability Matrix

| Feature | Divi 4 | Divi 5 | Status |
|---------|--------|--------|--------|
| Core modules (Text, Image, Button, etc.) | Yes | Yes | Full support |
| Third-party modules | Yes | Partial | Compatibility mode; authors updating |
| Quick Access | Yes | No | Not yet in Divi 5 |
| Full Site Editing | Yes | No | Not yet in Divi 5 |
| Draggable Spacing | Yes | No | Not yet in Divi 5 |
| Marketplace products | Yes | Depends | Check individual product pages |

## Migration Considerations

### Before Migrating

1. Backup your site and test migration in staging first
2. Check [Divi Marketplace](https://www.elegantthemes.com/marketplace/) for third-party module compatibility
3. Contact plugin authors about Divi 5 support if uncertain
4. Review [Divi 5 FAQ](divi-5-update-status.md) for known limitations

### What Gets Migrated

During migration via the [Divi 5 Migrator System](what-is-the-divi-5-migrator-system.md):
- Divi 4 pages are converted to Divi 5 format
- Supported modules are converted to Divi 5 native equivalents
- Unsupported modules are wrapped in shortcode format to maintain functionality
- Content and settings are preserved

### Performance After Migration

- Pages with only Divi 5 modules benefit from full performance improvements
- Pages with unsupported modules experience slower load times due to Divi 4 framework loading
- Enable Layout Wrapping and other Divi 5 features gradually as compatible modules become available

## Expectations and Limitations

!!! note "Plugin Author Timeline"
    Third-party plugin authors are not expected to have Divi 5 versions ready immediately. Divi provides development resources, but publishers set their own update schedules.

### What's Supported

- All core Divi modules (Text, Image, Button, Blurb, etc.)
- Divi-native features like Global Colors, Global Fonts, and Dynamic Content
- Responsive editing and breakpoints
- Visual Builder for both Divi 5 and legacy modules

### What's Not Fully Supported Yet

- Third-party Marketplace modules without Divi 5 updates
- Divi 4-specific features (Quick Access, Full Site Editing, Draggable Spacing)
- Some advanced third-party integrations may require publisher updates

## Troubleshooting

**Q: Can I use Divi 5 with my third-party modules?**
A: Yes, through backward compatibility mode. Check the Divi Marketplace for each module's status and contact authors for updates.

**Q: Why is my page slow after upgrading to Divi 5?**
A: Pages containing unsupported Divi 4 modules load the Divi 4 framework. Migrate to compatible modules to restore performance.

**Q: Can I rollback to Divi 4 if needed?**
A: Yes. See [How to Rollback to Divi 4](how-to-rollback-to-divi-4.md) for detailed instructions.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 and its relationship to Divi 4. For information on upgrading, see [How to Safely Migrate from Divi 4 to Divi 5](how-to-safely-migrate-from-divi-4-to-divi-5.md).

## Related

- [What is the Divi 5 Migrator System?](what-is-the-divi-5-migrator-system.md)
- [How to Safely Migrate from Divi 4 to Divi 5](how-to-safely-migrate-from-divi-4-to-divi-5.md)
- [How to Rollback to Divi 4](how-to-rollback-to-divi-4.md)
- [Divi 5 FAQ](divi-5-update-status.md)
- [Why Divi 5 Is Better than Divi 4](why-divi-5-is-better-than-divi-4.md)
