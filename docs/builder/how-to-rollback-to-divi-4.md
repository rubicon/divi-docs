---
title: "How to Rollback to Divi 4"
category: builder
tags: ["builder", "rollback", "downgrade", "divi-4", "migration", "troubleshooting", "theme-update"]
related: ["how-to-safely-migrate-from-divi-4-to-divi-5.md", "install-and-activate-divi-5.md", "backward-compatibility-and-third-party-divi-module-support.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/9858053-how-to-rollback-to-divi-4"
---

# How to Rollback to Divi 4

If you encounter compatibility issues, missing features, or design breaks after upgrading to Divi 5, you can roll back to Divi 4. This involves either restoring your site's content via the Divi 5 Migrator tool, or downloading and manually installing the Divi 4 theme file.

## Overview

Rolling back to Divi 4 is a two-part process:

1. **Restore Divi 4 content** (if you used the Divi 5 Migrator during the upgrade)
2. **Downgrade the theme file** (download Divi 4 and upload it to WordPress)

Most sites that upgraded from Divi 4 to Divi 5 have a backup of their Divi 4 content saved by the Migrator tool. If you do, you can restore it in one click. Otherwise, you'll need to manually re-work your designs or restore from a site backup.

## Before You Rollback

**Important Warnings:**

- **Divi 5 designs are not backward compatible with Divi 4.** Sections, rows, and modules built in Divi 5 may display incorrectly or break in Divi 4.
- **Custom CSS and code changes specific to Divi 5** (e.g., flexbox layout code, new setting names) will not work in Divi 4.
- **Third-party plugins and child themes** may be incompatible with Divi 4 if they were designed for Divi 5. Test thoroughly after rolling back.
- **Backup your database first.** Use a backup plugin (UpdraftPlus, Backup Buddy, etc.) or your hosting provider's backup tool before making any changes.
- **Notify your hosting provider if you're rolling back.** Some managed WordPress hosts automatically update Divi; rolling back may trigger re-updates.

## Method 1: Restore Divi 4 Content (Quick)

If you upgraded to Divi 5 and used the Divi 5 Migrator, your Divi 4 content is saved and can be restored in one click.

### Step 1: Open the Divi 5 Migrator

1. Log in to your WordPress dashboard
2. Navigate to **Divi** → **Divi 5 Migrator**

### Step 2: Restore Divi 4 Content

1. In the Divi 5 Migrator panel, click the **Restore Divi 4 Content** button
2. Confirm the action (a popup will ask if you're sure you want to restore)
3. Wait for the restoration to complete—this may take a few minutes depending on site size
4. When finished, your Divi 4 content (sections, rows, modules, settings) will be restored to all pages/posts

**Note:** This restores *content only*, not the theme file. You still need to downgrade the theme (see Method 2 below).

## Method 2: Downgrade the Theme File (Manual)

To actually run Divi 4 instead of Divi 5, you must download and upload the Divi 4 theme file.

### Step 1: Access Your Elegant Themes Account

1. Go to [Elegant Themes Account](https://www.elegantthemes.com/account) and log in
2. Navigate to **My Downloads** or **Downloads** section
3. Find **Divi Theme** in the list

### Step 2: Download Divi 4

1. Click the **Download the Divi Theme** button
2. A dropdown menu may appear with version options; **select Divi 4** (you may see "Latest", "Divi 4.x.x", etc.)
3. Download the `Divi.zip` file to your computer

**Note:** If only one "Download" button appears, it will download the latest version. Check the file version after download by opening the zip and viewing the `style.css` file header (look for `Version: 4.x.x`).

### Step 3: Upload Divi 4 to WordPress

#### Option A: Upload via WordPress Admin (Easiest)

1. Log in to your WordPress dashboard
2. Go to **Appearance** → **Themes**
3. Click the **Add New Theme** button (at the top)
4. Click the **Upload Theme** button (at the top right)
5. Click **Choose File** and select the `Divi.zip` file you downloaded
6. Click **Install Now** and wait for the upload to complete
7. Once installed, click **Activate** to switch to Divi 4

#### Option B: Upload via FTP (Manual)

If you prefer FTP or the admin upload fails:

1. Connect to your server via FTP client (Filezilla, etc.)
2. Navigate to `/wp-content/themes/`
3. Delete or rename the existing `Divi` folder (e.g., rename to `divi-5-backup`)
4. Extract the `Divi.zip` file on your computer
5. Upload the extracted `Divi` folder to `/wp-content/themes/`
6. In WordPress Admin, go to **Appearance** → **Themes** and activate Divi

### Step 4: Verify the Downgrade

1. Go to **Appearance** → **Themes**
2. Verify that Divi is active and the version displays as 4.x.x (not 5.x.x)
3. Visit your site frontend and check that pages load correctly

## After Rolling Back

### What to Expect

- **Divi 4 layouts reload** — Your restored content appears in the Divi 4 builder
- **Some features are unavailable** — Divi 5 features (flexbox, Responsive Editor, etc.) are not present
- **Third-party plugins may conflict** — Some plugins built for Divi 5 may not work; check with the plugin author
- **Custom code needs review** — Any custom CSS or PHP referencing Divi 5 features will need adjustment

### What May Break

- **Divi 5-specific designs** — Sections built purely in Divi 5 may look broken or display incorrectly
- **Mobile layouts** — If you used the Responsive Editor extensively, mobile breakpoints may need re-adjustment in Divi 4
- **Third-party integrations** — Plugins, child themes, or extensions designed for Divi 5 may not function

### Next Steps

1. **Test thoroughly** — Visit all key pages on the frontend. Check mobile, tablet, and desktop views.
2. **Update custom CSS** — Remove or rewrite any Divi 5-specific CSS rules in your child theme or Custom CSS section.
3. **Notify users** — If your site is client-facing, let stakeholders know of the downgrade and any design changes.
4. **Report issues** — If you rolled back due to a bug, contact Elegant Themes support with details so they can fix the issue in Divi 5.

## Preventing Future Rollback Needs

- **Test in staging first** — Before upgrading to Divi 5 on a live site, set up a staging environment and test all pages.
- **Use a compatibility checklist** — Review your plugins, child theme, and custom code against Divi 5 requirements before upgrading.
- **Backup before upgrading** — Always have a full database and files backup before any major theme update.
- **Stay updated** — Elegant Themes regularly releases Divi 5 updates and fixes. Many early issues are resolved in patches.

## Troubleshooting

!!! warning "Divi 5 Migrator tool is not showing"
    If you don't see **Divi** → **Divi 5 Migrator** in the WordPress admin:
    1. Make sure Divi 5 is currently active
    2. Go to **Divi** → **Dashboard** and check if any warnings appear
    3. Refresh the page
    4. If still missing, your Divi 4 content may not have been backed up during the upgrade. Proceed to Method 2 (manual downgrade) and consider restoring from a full-site backup if available.

!!! warning "Theme upload fails or file is corrupted"
    If the Divi 4 zip file fails to upload:
    1. Verify the file size is under your hosting provider's upload limit
    2. Try uploading via FTP instead (Option B above)
    3. Contact your hosting provider if FTP upload also fails
    4. Ensure you downloaded the file from the correct Elegant Themes account link

!!! warning "Site looks broken after rolling back"
    If pages display incorrectly or layouts are missing:
    1. Verify Divi 4 is active (**Appearance** → **Themes**)
    2. Clear your browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
    3. Go to **Divi** → **Dashboard** → **Tools** → **Clear Cache** (if available)
    4. Run the Divi 5 Migrator's **Restore Divi 4 Content** again
    5. If layouts still don't show, restore from a full-site backup taken before the Divi 5 upgrade

!!! note "Elegant Themes support"
    If you encounter persistent issues during rollback, contact Elegant Themes support (support@elegantthemes.com) with:
    - Your site URL
    - A screenshot of the issue
    - The step where you got stuck
    - Your Elegant Themes account email

## Version Notes

!!! note "Divi 5 & Divi 4 Incompatibility"
    This guide applies specifically to rolling back from Divi 5 to Divi 4. Divi 4 layouts and custom code will not work identically in Divi 5 due to architectural differences (grid vs. flexbox, new settings schema, etc.).

## Related

- [How to Safely Migrate from Divi 4 to Divi 5](how-to-safely-migrate-from-divi-4-to-divi-5.md)
- [Install and Activate Divi 5](install-and-activate-divi-5.md)
- [Backward Compatibility and Third-Party Divi Module Support](backward-compatibility-and-third-party-divi-module-support.md)
- [Divi 5 Update Guide](divi-5-update-status.md)
