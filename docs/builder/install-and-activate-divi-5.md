---
title: "Install and Activate Divi 5"
category: builder
tags: ["builder", "installation", "activation", "license"]
related: ["how-to-safely-migrate-from-divi-4-to-divi-5.md", "exploring-divi-5-s-new-features.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12951730-install-and-activate-divi-5"
---

# Install and Activate Divi 5

Get Divi 5 up and running on your WordPress site in minutes. This guide covers downloading from your Elegant Themes account, uploading to WordPress, and activating your license key.

## Prerequisites

Before you install Divi 5, ensure you have:

- **WordPress 6.0 or higher** installed and configured
- **Administrator access** to your WordPress dashboard
- **An active Elegant Themes subscription** with Divi 5 access
- **FTP or SFTP access** (if uploading manually), or file upload permissions in WordPress
- At least **50 MB free disk space** for the theme and its assets

## Step 1: Download Divi 5

1. Log in to your [Elegant Themes account](https://www.elegantthemes.com/my-account/){:target="_blank"}
2. Navigate to **Dashboard** → **Themes & Plugins**
3. Locate **Divi 5** in the available themes
4. Click **Download** (or **Download Theme**) and save the `.zip` file to your computer
5. Do not extract the `.zip` file — WordPress will handle that automatically

## Step 2: Upload and Install Divi 5

### Via WordPress Dashboard (Recommended)

1. In your WordPress dashboard, go to **Appearance** → **Themes**
2. Click **Add New** at the top of the page
3. Click **Upload Theme**
4. Click **Choose File** and select the Divi 5 `.zip` file you downloaded
5. Click **Install Now** and wait for the installation to complete
6. You should see a "Theme installed successfully" message

### Via FTP (Manual Upload)

If you prefer manual upload:

1. Unzip the Divi 5 file on your computer
2. Connect to your site via FTP
3. Navigate to `/wp-content/themes/`
4. Upload the entire `divi` folder to this directory
5. Return to **Appearance** → **Themes** to confirm the theme appears

## Step 3: Activate Divi 5

1. On the **Themes** page, locate **Divi 5** in your installed themes
2. Hover over the Divi 5 theme card and click **Activate**
3. You should see a confirmation message: "Divi activated successfully"
4. Your site now uses Divi 5 as the active theme

## Step 4: Activate Your License Key

To unlock all Elegant Themes features and receive updates, you must activate your license key.

1. In your WordPress dashboard, navigate to **Divi** → **Theme Options** (or **Divi** → **Settings**)
2. Look for **Updates** or **License Activation** section (the exact location may vary)
3. Click the **Log In to Activate Your License** button or similar prompt
4. Enter your **Elegant Themes username and password** and confirm
5. Alternatively, if prompted, generate an **API key** from your Elegant Themes account:
   - Go to [Elegant Themes Account](https://www.elegantthemes.com/my-account/){:target="_blank"}
   - Navigate to **Account** → **Username & API Key**
   - Generate a new API key if you don't have one
   - Copy the key
   - Paste it into the API key field in **Divi** → **Theme Options** → **Updates**
6. Click **Save Changes**

Your license is now active, and you have access to:

- Theme updates
- Elegant Themes support
- Cloud synchronization for designs
- Additional design resources and templates

## Troubleshooting

!!! warning "Installation Failed — Theme Could Not Be Installed"
    **Cause:** The `.zip` file may be corrupted or incomplete.
    
    **Solution:** Delete the attempted install, re-download the theme from your Elegant Themes account, and try uploading again. Verify the file size matches the original download.

!!! warning "License Activation Not Appearing"
    **Cause:** Plugin dependencies or theme conflicts.
    
    **Solution:** 
    - Ensure all other Elegant Themes plugins (like Bloom or Monarch) are also updated
    - Try deactivating other plugins temporarily to see if there's a conflict
    - Clear your browser cache and log out, then log back in

!!! warning "Cannot Access Divi Menu in Dashboard"
    **Cause:** Theme not fully installed or activation incomplete.
    
    **Solution:** 
    - Go to **Appearance** → **Themes** and confirm Divi 5 shows as "Active"
    - Try re-uploading the theme via FTP
    - Check that your WordPress user has administrator privileges

!!! warning "Updates Not Downloading"
    **Cause:** License not activated or API key invalid.
    
    **Solution:** 
    - Verify your license key is correctly entered in **Divi** → **Theme Options** → **Updates**
    - Generate a fresh API key from your Elegant Themes account and re-enter it
    - Ensure your Elegant Themes subscription is active

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 only. If you are upgrading from Divi 4, see [How to Safely Migrate from Divi 4 to Divi 5](../builder/how-to-safely-migrate-from-divi-4-to-divi-5.md) for migration instructions and version-specific considerations.

## Related

- [How to Safely Migrate from Divi 4 to Divi 5](../builder/how-to-safely-migrate-from-divi-4-to-divi-5.md)
- [Exploring Divi 5's New Features](../builder/exploring-divi-5-s-new-features.md)
- [Getting Started with Divi 5 Theme Builder](../builder/getting-started-with-divi-5-theme-builder.md)
