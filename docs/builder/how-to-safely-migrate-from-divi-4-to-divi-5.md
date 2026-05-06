---
title: "How to Safely Migrate from Divi 4 to Divi 5"
category: builder
tags: ["builder", "migration", "divi-4", "upgrade"]
related: ["how-to-rollback-to-divi-4.md", "what-is-the-divi-5-migrator-system.md", "backward-compatibility-and-third-party-divi-module-support.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12767407-how-to-safely-migrate-from-divi-4-to-divi-5"
---

# How to Safely Migrate from Divi 4 to Divi 5

Migrate your Divi 4 site to Divi 5 with confidence using the built-in Migrator tool and compatibility scan.

## Overview

Divi 5 is a major upgrade that rebuilds the theme from the ground up for better performance and new capabilities. The Divi 5 Migrator is a specialized tool that handles the migration process automatically, scanning your site for compatibility issues before migration and providing a detailed report so you can make an informed decision.

The migration system is designed to be safe and reversible. Divi creates a backup of your Divi 4 content before migration, and you can restore it at any time if needed. Most sites can migrate with minimal or no issues, especially if you use primarily Divi native modules.

## Before You Migrate

### Prerequisites

- Divi 5 must be installed and activated on your site
- WordPress, Divi, and all plugins must be fully updated
- Backup your entire WordPress installation before starting
- Test migration on a staging environment first, if possible
- Note which custom or third-party modules you use

### Backup Your Site

Create a full WordPress backup using your hosting provider or a backup plugin (like UpdraftPlus, BackWPup, or Duplicator). This protects you in case something unexpected occurs during migration.

## Step 1: Enable Divi 5 Updates

1. Go to **Divi → Dashboard** in the WordPress admin
2. Look for the "Divi Overview" card
3. Click the **Update** link to access the Divi 5 Updates section
4. Click **Update now** to install Divi 5

Once installed, both Divi 4 and Divi 5 are available on your site.

## Step 2: Run the Compatibility Scan

The Migrator tool automatically runs a compatibility scan to identify potential issues.

1. Navigate to **Divi → Divi 5 Migrator** from the WordPress admin
2. The scan automatically begins and analyzes these areas:
   - Pages
   - Posts
   - Custom post types
   - Theme Builder templates
   - WooCommerce products
   - Divi Library items
   - Widgets
   - Presets

### Understanding the Scan Report

The compatibility report shows:

- **Green indicators** – Items fully compatible with Divi 5, no changes needed
- **Orange warning icons** – Items containing unsupported or legacy modules that will run in backward-compatibility mode after migration
- **Module details** – Specific modules causing warnings so you can plan replacements

Review this report carefully before proceeding. If you have heavily customized layouts or many legacy third-party modules, consider waiting for plugin updates or replacing modules before migrating.

## Step 3: Decide: Migrate Now or Wait?

### Migrate Now If:

- Most of your modules are convertible (green in the scan report)
- You only have a few legacy modules
- You want to use Divi 5 features on new pages
- Third-party plugins have released Divi 5 versions

### Wait If:

- Your site relies heavily on unsupported third-party modules
- Key plugins haven't released Divi 5-compatible versions yet
- You need to replace many custom modules first

Divi 4 and Divi 5 can coexist on your site, allowing you to migrate pages gradually if preferred.

## Step 4: Perform the Migration

1. In **Divi → Divi 5 Migrator**, review the compatibility report one final time
2. Click **Migrate This Site to Divi 5**
3. Confirm the action when prompted
4. The process typically completes in seconds to a couple of minutes (larger sites may take longer)
5. You'll see a confirmation when migration is complete

Divi 4 content is preserved and stored. You can restore it at any time.

## Step 5: Verify the Migration

### Check Your Site

1. Exit the migrator and view your site on the frontend
2. Test key pages, forms, and interactive elements
3. Check responsive layouts on mobile and tablet
4. Verify WooCommerce functionality if applicable
5. Test any custom integrations

### Backward Compatibility Mode

If your site still contains Divi 4 modules after migration, you may see a "Backward Compatibility Mode Enabled" notice on the frontend. This is expected behavior:

- Divi 4 framework loads in the background to support legacy modules
- Performance impact is temporary
- Replace unsupported modules with Divi 5 equivalents to improve performance
- This mode affects only frontend performance, not your ability to edit

## Troubleshooting

### Layouts Look Broken

This is usually caused by incompatible third-party plugins or modules. 

**Solution:** Check that your Divi Marketplace plugins are compatible with Divi 5 and update them to the latest versions.

### Builder Glitches or Crashes

Divi 5 is in active development, so occasional bugs are expected.

**Solution:** 
- Clear your browser cache
- Clear the Divi cache (Divi → Settings → Cache)
- Disable any caching plugins temporarily
- Check the browser console (F12) for JavaScript errors
- Try a different browser

### Slow Performance on Certain Pages

Pages with unsupported legacy modules load the Divi 4 framework as a compatibility layer, which impacts performance.

**Solution:**
- Replace legacy modules with Divi 5-native versions
- Check the compatibility report for which modules need updating
- As plugin authors release Divi 5 versions, update them
- Performance will improve as backward compatibility is phased out

### Migration Fails or Doesn't Complete

The migrator may fail if your site is missing updates.

**Solution:**
- Ensure WordPress is fully updated
- Update Divi to the latest version
- Update all plugins to their latest versions
- Try running the migrator again

### White Screen of Death or Fatal Errors

This can occur if a plugin is incompatible with Divi 5.

**Solution:**
- Enable WordPress debug mode to see the error
- Deactivate third-party plugins one by one to identify the culprit
- Update or replace the incompatible plugin
- Contact the plugin author for Divi 5 support

## Rolling Back to Divi 4

If you need to revert to Divi 4:

1. Go to **Divi → Divi 5 Migrator**
2. Click **Restore Divi 4 Content**
3. Confirm the action
4. Uninstall Divi 5 and reinstall Divi 4 if needed

See [How to Roll Back to Divi 4](../builder/how-to-rollback-to-divi-4.md) for detailed steps.

## Common Migration Scenarios

### Scenario: Small Blog or Portfolio Site

Most of these sites use basic Divi modules (text, images, buttons, galleries). Migration is typically seamless with no issues.

### Scenario: E-commerce Site with WooCommerce

Divi 5 has native WooCommerce module support. If you use third-party product module plugins, check compatibility before migrating.

### Scenario: Site with Many Custom Layouts and Presets

Presets migrate automatically. Custom CSS and custom styling settings are preserved.

### Scenario: Agency with Multiple Client Sites

Test on one client site first, document the process and any issues, then apply lessons to other sites.

## Performance Impact

Divi 5 is designed to be faster than Divi 4:

- Faster page loads due to optimized code
- Smaller CSS/JS bundles
- Improved database queries
- Better caching strategies

However, sites with many legacy modules in backward-compatibility mode may see temporary performance dips until modules are updated.

## Post-Migration Best Practices

1. **Replace Unsupported Modules** – Gradually replace any legacy modules with Divi 5 equivalents
2. **Update Plugins** – Keep all plugins updated, especially those with Divi integration
3. **Test Regularly** – Test pages in the builder and on the frontend frequently
4. **Monitor Performance** – Use tools like Google PageSpeed Insights to track performance
5. **Update Your Team** – Train team members on Divi 5's new interface and features
6. **Save to Library** – Store commonly used sections and layouts in your Divi Library for reuse

## Version Notes

!!! note "Divi 5 Only"
    This page documents the Divi 5 migration process exclusively. For information on Divi 4 features, see the legacy documentation.

## Related

- [How to Roll Back to Divi 4](../builder/how-to-rollback-to-divi-4.md)
- [What is the Divi 5 Migrator System?](../builder/what-is-the-divi-5-migrator-system.md)
- [Backward Compatibility and Third-Party Divi Module Support](../builder/backward-compatibility-and-third-party-divi-module-support.md)
- [Enable Divi 5 Updates](../builder/install-and-activate-divi-5.md)
