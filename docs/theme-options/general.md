---
title: "General Settings"
category: theme-options
tags: [theme-options, general, performance, logo, colors, social-media, fonts, css]
related: [navigation, layout, builder-settings]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/theme-options/"
---

# General Settings

The General Settings tab contains core site-wide options for branding, social media, display preferences, and performance optimization.

## Overview

This is where the general settings for Divi's Theme Options live. Here you'll find two sub-tabs: **General** and **Performance**.

In the **General** sub-tab, you'll find settings for your site's logo, color palette, social media links, Google Fonts, the back-to-top button, a custom CSS block, and more. These options control the fundamental appearance and behavior of your Divi-powered site.

Under the **Performance** sub-tab, you'll find settings that control CSS and JavaScript loading that can be used to optimize your site's performance. Settings like Dynamic Module Framework, Dynamic CSS, Critical CSS, and Dynamic JavaScript Libraries can help improve the speed of your website.

<!-- ![General Settings overview](../assets/screenshots/theme-options/general/overview.png){ loading=lazy }
*The General Settings panel in Divi Theme Options.* -->

## Settings & Options

### General

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Logo | upload | — | Upload a global logo for your website. Click the upload button to load the WordPress Media Library and select or upload a logo. The logo set here will appear wherever a logo is called in your Divi Theme, such as in the Menu module. |
| Fixed Navigation Bar | toggle | Enabled | Controls whether the navigation bar is fixed (sticks to the top of the screen as the page scrolls). When disabled, the navigation bar stays at the top of the page and scrolls out of view. Only applies when not using the Theme Builder for your navigation bar. |
| Enable Divi Gallery | toggle | Disabled | Replaces the default WordPress gallery style with the Divi-style gallery. Applies to the "Create Gallery" feature in the WordPress media library uploader. |
| Color Pickers Default Palette | color | — | Choose which colors appear by default in color pickers across the Visual Builder. See the Color Management Documentation for additional color settings in Divi. |
| Grab the first post image | toggle | Disabled | Automatically generates thumbnail images using the first image in your post instead of using custom fields. The image must be hosted on your website. |
| Blog Style Mode | toggle | Disabled | Displays full posts on index/home pages instead of truncated post previews. Activate this for a traditional blog layout. |
| Sidebar Layout | select | Right | Defines where default sidebars appear on a page. Select Left or Right from the dropdown menu. |
| Shop Page & Category Page Layout for WooCommerce | select | — | Defines which layout your shop uses on product and product category pages when using WooCommerce integration. |
| Google API Key | text | — | Enter your Google Maps API Key here. The Divi Maps module requires a valid Google API Key in order to function. |
| Use Google Fonts | toggle | Enabled | Enable this option to use Google Fonts on your website. Google Fonts is a free font service that provides over a thousand free fonts. |
| Google Fonts Subsets | toggle | Disabled | Enables Google Fonts for non-English languages. |
| Enqueue Google Maps Script | toggle | Enabled | Controls whether the Google Maps API script is loaded on Divi Builder pages. Disabling may improve compatibility with third-party plugins that also enqueue this script. Note: Modules like Maps and Fullwidth Maps will not function while this option is disabled unless you manually add the Google Maps API script. |
| Show Facebook Icon | toggle | Enabled | Show or hide the Facebook icon in modules that call for it, such as the Social Media Follow module. |
| Show Twitter Icon | toggle | Enabled | Show or hide the Twitter icon in modules that call for it, such as the Social Media Follow module. |
| Show Instagram Icon | toggle | Enabled | Show or hide the Instagram icon in modules that call for it, such as the Social Media Follow module. |
| Show RSS Icon | toggle | Enabled | Show or hide the RSS icon in modules that call for it. |
| Facebook Profile URL | url | — | Paste the link to your Facebook profile here. |
| Twitter Profile URL | url | — | Paste the link to your Twitter profile here. |
| Instagram Profile URL | url | — | Paste the link to your Instagram profile here. |
| RSS Icon URL | url | — | Paste the link to your RSS Feed here. |
| Number of Products displayed on WooCommerce archive pages | number | — | Designate how many WooCommerce products are displayed on the archive page. This option works independently from Settings > Reading in wp-admin. |
| Number of Posts displayed on Category page | number | — | Define how many posts are displayed when a user visits a Category Page. |
| Number of Posts displayed on Archive pages | number | — | Define how many posts are displayed when a user visits an Archive Page. |
| Number of Posts displayed on Search pages | number | — | Define how many posts are displayed when a user visits a Search Results Page. |
| Number of Posts displayed on Tag pages | number | — | Define how many posts are displayed when a user visits a Tag Page. |
| Date format | text | — | Change how dates are displayed. Refer to the WordPress Codex for Formatting Date and Time options. |
| Use excerpts when defined | toggle | Disabled | Enables the use of excerpts in posts or pages. |
| Back To Top Button | toggle | Enabled | Displays a Back To Top button at the bottom right of the page while scrolling. |
| Smooth Scrolling | toggle | Disabled | Enables a smooth scrolling effect with mouse wheel. Especially useful when using anchor links to link to specific areas of the page. |
| Disable Translations | toggle | Disabled | Disable translations if you don't want to display translated theme strings on your site. |
| Enable Responsive Images | toggle | Enabled | Generates responsive image sizes when uploading images and adds the srcset attribute for image elements. |
| Custom CSS | code | — | Enter any custom CSS to customize your site. For extensive CSS modifications, it is recommended to use a child theme. |

### Performance

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Dynamic Module Framework | toggle | Enabled | Allows the Divi Framework to only load the modules that are used on the page and process the logic for the features in use. |
| Dynamic CSS | toggle | Enabled | Greatly reduces CSS file size by dynamically generating only the assets necessary for the features and modules you use, eliminating file bloat and improving load times. |
| Dynamic Icons | toggle | Enabled | The Divi icon font is broken up into subsets that load only when needed. Disable this option to load the entire icon font library on all pages (useful if you use the icon font in your child theme). |
| Load Dynamic Stylesheet In-line | toggle | Enabled | Dequeues the Divi style.css file and prints the contents in-line, removing a render-blocking request and improving PageSpeed scores. However, it also prevents the style.css file from being cached. Recommended to keep enabled since the stylesheet is small. |
| Critical CSS | toggle | Enabled | Greatly improves website load times and Google PageSpeed scores by deferring non-critical styles and eliminating render-blocking CSS requests. |
| Critical Threshold Height | range | — | When Critical CSS is enabled, Divi determines an "above the fold threshold" and defers styles for elements below the fold. Increasing threshold height defers fewer styles, resulting in slightly slower load times but less chance for Cumulative Layout Shifts (CLS). Increase this if you are experiencing CLS issues. |
| Dynamic JavaScript Libraries | toggle | Enabled | Only loads external JavaScript libraries when they are needed by specific Divi modules on the page, removing unused JavaScript from the main scripts bundle and improving load times. |
| Disable WordPress Emojis | toggle | Disabled | Removes WordPress emoji assets. Modern browsers support native emojis, making WordPress's emojis unnecessary in most cases. Removing them improves performance. |
| Defer Gutenberg Block CSS | toggle | Enabled | If a page is built with the Divi Builder, the Gutenberg block CSS file is moved from the header to the footer, removing a render-blocking request and improving performance. |
| Improve Google Fonts Loading | toggle | Enabled | Enables caching of Google Fonts and loads them inline, reducing render-blocking requests and improving page load times. |
| Limit Google Fonts Support For Legacy Browsers | toggle | Enabled | Lowers the size of Google Fonts and improves load times but limits Google Fonts support in some very old browsers. Turn this off to increase support for older browsers at a slight cost to performance. |
| Defer jQuery and jQuery Migrate | toggle | Disabled | When possible, moves jQuery and jQuery Migrate to the body to speed up load times. If a third-party plugin registers jQuery as a dependency, it will be moved back to the head. |
| Enqueue jQuery Compatibility Script | toggle | Disabled | Loads an additional compatibility script to prevent console errors when jQuery is deferred. Some third-party scripts may be incorrectly enqueued without declaring jQuery as a dependency. Enable this if you experience console errors after enabling "Defer jQuery And jQuery Migrate". |
| Defer Additional Third Party Scripts | toggle | Disabled | When enabled, scripts registered by plugins and themes will be deferred to improve performance and jQuery will always be loaded in the body. Warning: This can cause JavaScript errors in some cases and should be used with care. |

## Code Examples

```css
/* Example: Adding custom CSS via the Custom CSS field */
.et_pb_section {
    padding: 60px 0;
}

.et_pb_button {
    border-radius: 4px !important;
    text-transform: uppercase;
}
```

```php
// Access General Settings values programmatically
$logo = et_get_option('divi_logo');
$fixed_nav = et_get_option('divi_fixed_nav', 'on');
$google_api_key = et_get_option('et_google_api_settings_api_key');
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Performance Settings Can Cause Conflicts"
    Enabling "Defer Additional Third Party Scripts" can cause JavaScript errors with some third-party plugins. If you experience issues after enabling performance options, disable them one at a time to identify the conflict. Always test performance changes on a staging site first.

## Related

- [Navigation Settings](navigation.md)
- [Layout Settings](layout.md)
- [Builder Settings](builder-settings.md)
- [Integration Settings](integration.md)
