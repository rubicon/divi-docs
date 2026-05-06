---
title: "What is the Divi 5 Migrator System?"
category: builder
tags: ["builder", "migration", "upgrade", "divi-5-migrator"]
related: ["how-to-safely-migrate-from-divi-4-to-divi-5.md", "backward-compatibility-and-third-party-divi-module-support.md", "how-to-rollback-to-divi-4.md", "divi-5-faq.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/9799364-what-is-the-divi-5-migrator-system"
---

# What is the Divi 5 Migrator System?

The Divi 5 Migrator System scans your Divi 4 website for compatibility with Divi 5 and provides a guided upgrade path. It converts supported modules to Divi 5 format while wrapping unsupported modules for backward compatibility.

## Overview

When you first install Divi 5 on an existing Divi 4 site, the Migrator System automatically appears. It performs a comprehensive audit of your content and provides clear recommendations before migration.

**The Migrator System:**
- Scans all pages, theme templates, WooCommerce products, Divi Library items, and widgets
- Identifies which modules are supported in Divi 5 and which require compatibility mode
- Generates a detailed compatibility report
- Allows you to migrate with a single click or explore Divi 5 first
- Lets you rollback to Divi 4 at any time

This system ensures you understand the compatibility status before committing to Divi 5.

## How the Migration Process Works

### What Gets Converted

When you click **"Migrate This Site to Divi 5"**, the system:

1. **Converts supported Divi 4 modules** — Transforms them into native Divi 5 format
   - Example: A Divi 4 Text module with red background and white text becomes a Divi 5 Text block with equivalent styling
   - All content, custom CSS, and responsive settings are preserved

2. **Wraps unsupported modules** — Keeps them functional using Divi 4 framework
   - Third-party modules not yet updated for Divi 5 remain wrapped
   - Pages containing unsupported modules will load the Divi 4 framework
   - Performance is affected only on pages with unsupported content

3. **Preserves all content** — Database-level conversion ensures no content loss
   - The conversion happens automatically in the database
   - You don't need to manually rebuild pages

### Performance Impact

- **Pages with only Divi 5 modules** — Enjoy full Divi 5 performance improvements
- **Pages with unsupported modules** — Divi 4 framework loads, reducing speed for those pages
- **Site-wide speed** — Generally improved, with per-page variability based on module support

!!! note "Conversion Example"
    Divi 4 Text module: `[et_pb_text background_color="#E02B20" text_color="white"]Content[/et_pb_text]`
    
    Becomes Divi 5 block format at the database level (not visible in editor, but functionally equivalent).

## Running the Migrator System

### On a Fresh Divi 5 Installation (Existing Divi 4 Site)

When you first install Divi 5:

1. A notification appears in WordPress admin
2. Click **"Migrate This Site to Divi 5"** or explore the report first
3. The Migrator scans for:
   - Pages with unsupported modules
   - Theme Builder templates using incompatible features
   - WooCommerce products with third-party modules
   - Divi Library items requiring compatibility
   - Widgets with unsupported content

4. Review the compatibility report (9 sections total)
5. Click **"Migrate This Site to Divi 5"** to proceed
6. Confirm the migration — this is irreversible until you use "Restore Divi 4 Content"

### On a Site with Only Divi 5-Compatible Content

If your Divi 4 site uses only modules and features supported by Divi 5:

1. The Migrator detects full compatibility
2. Click **"Upgrade This Site to Divi 5"** (instead of "Migrate")
3. All Divi 5 features activate immediately
4. No compatibility mode needed
5. Full performance improvements apply site-wide

## Compatibility Report Sections

The Migrator generates a report covering:

1. **Pages** — List of pages with compatibility status
2. **Theme Builder Templates** — Templates using deprecated Divi 4 features
3. **WooCommerce Products** — Product pages with third-party modules
4. **Divi Library** — Saved sections and rows requiring compatibility
5. **Widgets** — Widget areas containing unsupported modules
6. **Deprecated Features** — Divi 4-only features (Quick Access, Full Site Editing, etc.)
7. **Third-Party Modules** — Modules needing publisher updates
8. **Feature Status** — Overview of feature support in current Divi 5 version
9. **Recommendations** — Actionable next steps

## Important Considerations

### Before Migrating

!!! warning "Backup First"
    We strongly recommend backing up your site and testing migration in a staging environment before upgrading live.

**Timing Recommendations:**
- **Best for new sites** — Use Divi 5 on new WordPress sites without hesitation
- **For existing sites** — Test in staging, ensure third-party modules are compatible, then migrate to live
- **If unsure** — Use Divi 4 until third-party modules you rely on have Divi 5 updates available

### Current Limitations

- Divi 5 is still in active development
- Some Divi 4 features are not yet available (Quick Access, Full Site Editing, Draggable Spacing)
- Third-party module compatibility varies — check individual marketplace products
- Pages with unsupported modules experience slower load times

## Rollback Option

If you need to revert to Divi 4 after migration:

1. Go to the Migrator System (appears in admin if Divi 5 is active)
2. Click **"Restore Divi 4 Content"**
3. Your Divi 4 content is restored from backup
4. You can then deactivate Divi 5 and reactivate Divi 4

For detailed rollback instructions, see [How to Rollback to Divi 4](how-to-rollback-to-divi-4.md).

## Technical Details

### Module Conversion Format

Divi 4 modules use shortcode format:
```
[et_pb_module_name attribute="value"]Content[/et_pb_module_name]
```

Divi 5 modules use block format (WordPress-native):
```
<!-- wp:divi/module-name {"attribute":"value"} -->
Content
<!-- /wp:divi/module-name -->
```

The Migrator converts all compatible modules to Divi 5's block format during migration, maintaining all settings and styling.

### Unsupported Module Handling

Unsupported modules are wrapped in Divi 5's compatibility layer:
- They remain functional on the frontend
- The Divi 4 framework loads only for pages containing them
- They can be edited in the Visual Builder with backward compatibility active
- As publishers update modules for Divi 5, these pages will automatically benefit from improved performance

## Troubleshooting

**Q: My migration failed — what do I do?**
A: Check your hosting provider's error logs. Common issues include memory limits or timeout settings. Increase `WP_MEMORY_LIMIT` and `WP_MEMORY_LIMIT` in `wp-config.php`.

**Q: Some of my modules aren't converting — why?**
A: Modules from third-party authors need to be updated for Divi 5 support. Contact the plugin author or check the Divi Marketplace for updates.

**Q: Can I migrate a portion of my site and leave the rest in Divi 4?**
A: No — migration is site-wide. However, pages with only Divi 5 modules will have full performance improvements, while pages with unsupported modules will load Divi 4 framework.

**Q: How long does migration take?**
A: Depends on site size. Most sites complete in 1-5 minutes. Large sites with thousands of pages may take longer.

## Version Notes

!!! note "Divi 5 Only"
    This page documents the Divi 5 Migrator System. For pre-migration planning, see [How to Safely Migrate from Divi 4 to Divi 5](how-to-safely-migrate-from-divi-4-to-divi-5.md).

## Related

- [How to Safely Migrate from Divi 4 to Divi 5](how-to-safely-migrate-from-divi-4-to-divi-5.md)
- [Backward Compatibility and Third-Party Divi Module Support](backward-compatibility-and-third-party-divi-module-support.md)
- [How to Rollback to Divi 4](how-to-rollback-to-divi-4.md)
- [Divi 5 FAQ](divi-5-update-status.md)
- [Why Divi 5 Is Better than Divi 4](why-divi-5-is-better-than-divi-4.md)
