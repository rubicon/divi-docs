---
title: "Updates Settings"
category: theme-options
tags: [theme-options, updates, api-key, account, version-rollback]
related: [general]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/theme-options/"
---

# Updates Settings

The Updates Settings tab is where you authenticate your Elegant Themes subscription to receive product updates and access version rollback functionality.

## Overview

The Updates tab is where you paste your Elegant Themes membership info so that your Divi install is linked to your Elegant Themes account. This ensures you have access to all future updates and features of Divi.

Before you can receive product updates, you must first authenticate your Elegant Themes subscription by entering both your Elegant Themes Username and your Elegant Themes API Key. To locate your API Key, log in to your Elegant Themes account and navigate to the Account > API Key page. If authentication fails, verify that your Username and API Key have been entered correctly.

![Updates Settings overview](../assets/screenshots/theme-options/updates/overview.png){ loading=lazy }
*The Updates Settings panel in Divi Theme Options.*

## Settings & Options

### General

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Username | text | — | Type your Elegant Themes username here. This is the username you use to log in to your Elegant Themes account. |
| API Key | text | — | Paste your unique API key here. You can find your API key by logging into your Elegant Themes account and navigating to Account > API Key. |
| Version Rollback | select | — | If you recently updated to a new version and are experiencing problems, you can roll back to the previously-installed version. It is recommended to always use the latest version and test updates on a staging site first. However, if you run into problems after updating, you can use this option to roll back. |

## Code Examples

```php
// Check if the Elegant Themes account is authenticated
$et_username = et_get_option('et_username');
$et_api_key = et_get_option('et_api_key');

if (!empty($et_username) && !empty($et_api_key)) {
    // Account is configured for updates
}
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Authentication Failing"
    If you see a message that your subscription cannot be authenticated, double-check that your Username and API Key are entered correctly with no extra spaces. Your API Key can be found at Account > API Key in your Elegant Themes dashboard. Also ensure your Elegant Themes subscription is active and not expired.

## Related

- [General Settings](general.md)
- [Builder Settings](builder-settings.md)
