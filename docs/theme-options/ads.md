---
title: "Ads Settings"
category: theme-options
tags: [theme-options, ads, advertising, banners, adsense]
related: [general, integration]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/theme-options/"
---

# Ads Settings

The Ads Settings tab configures banner advertisements displayed on your website outside of widget areas.

## Overview

In the Ads tab, you'll find settings that configure ads displayed on your website that are not configured through widgets. These settings allow you to place a 468x60 banner ad on single post pages and integrate AdSense code.

The settings are grouped under the **Manage Un-widgetized Advertisements** section. When enabled, a banner ad will display at the bottom of your post pages below the single post content. You must provide both a banner image URL and a destination URL for the ad to function properly.

<!-- ![Ads Settings overview](../assets/screenshots/theme-options/ads/overview.png){ loading=lazy }
*The Ads Settings panel in Divi Theme Options.* -->

## Settings & Options

### Manage Un-widgetized Advertisements

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable Single Post 468x60 banner | toggle | Disabled | Enabling this option displays a 468x60 banner ad on the bottom of your post pages below the single post content. If enabled, you must fill in the banner image and destination URL below. |
| Input 468x60 advertisement banner image | url | — | Provide the URL for your 468x60 banner image. |
| Input 468x60 advertisement destination url | url | — | Provide the destination URL that the 468x60 banner ad links to when clicked. |
| Input 468x60 adsense code | code | — | Place your AdSense code here to display AdSense ads instead of or in addition to a banner image. |

## Code Examples

```php
// Check if the single post banner is enabled
$banner_enabled = et_get_option('divi_468_enable', 'off');

// Get the banner image URL
$banner_image = et_get_option('divi_468_image');

// Get the banner destination URL
$banner_url = et_get_option('divi_468_url');

// Get the AdSense code
$adsense_code = et_get_option('divi_468_adsense');
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Banner Not Displaying"
    If you have enabled the banner but it is not appearing, verify that both the banner image URL and destination URL fields are filled in. Also check that the image URL is accessible and the image dimensions are correct (468x60 pixels).

## Related

- [General Settings](general.md)
- [Integration Settings](integration.md)
- [Layout Settings](layout.md)
