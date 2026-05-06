---
title: "Divi 5 Theme Options"
category: builder
tags: [builder, theme-options, settings, site-wide]
related: [divi-5-theme-builder, visual-builder-overview]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12958885-divi-5-theme-options"
---

# Divi 5 Theme Options

Divi 5 Theme Options is the site-wide settings panel where you configure default behaviors, global assets, performance settings, and integrations that apply across your entire site.

## Overview

Theme Options control site-wide defaults and behaviors, separate from the Visual Builder and Theme Builder which control individual pages and layouts. Access Theme Options from **Divi → Theme Options** in the WordPress admin menu.

In Divi 5, Theme Options is organized into multiple tabs:
- **General** — logo, navigation, gallery, blog, sidebar, and basic display options
- **Navigation** — header and menu configuration
- **Builder** — Visual Builder and Theme Builder defaults
- **Layout** — post/product count, date formatting, responsive behavior
- **Ads** — ad network integration settings
- **SEO** — site-wide SEO configuration
- **Integration** — analytics, tracking, and third-party service codes
- **Updates** — Elegant Themes account connection and auto-updates

![Theme Options panel overview](../assets/screenshots/builder/divi-5-theme-options/overview.png){ loading=lazy }
*The Theme Options panel provides centralized control over site-wide Divi 5 settings.*

## Settings & Options

### General Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Logo | Image Upload | None | Upload the main logo image used in your header. This is the default header logo displayed on all pages unless overridden in Theme Builder. |
| Fixed Navigation Bar | Toggle | Enabled | When enabled, the navigation bar remains visible at the top of the screen when scrolling. Disable to allow the navigation to scroll out of view. |
| Enable Divi Gallery | Toggle | Disabled | Enable this option to replace the default WordPress gallery with Divi's enhanced gallery module, which includes styling, lightbox, and layout options. |
| Use First Post Image for Featured Image | Toggle | Disabled | By default, post/product thumbnails use the Featured Image field. Enable this to automatically use the first image found within the post content as the thumbnail instead. |
| Blog Style Mode | Toggle | Disabled | By default, posts are truncated on index and archive pages to display as previews. Enable this to display full post content on index pages in traditional blog style. |
| Sidebar Layout | Select | Right | Choose the default sidebar position: Right, Left, or Full Width. This applies to archive, category, and single post pages unless overridden per-page. |
| WooCommerce Shop Page Layout | Select | Right | Set the default sidebar position for WooCommerce shop pages and product category pages. |
| Google API Key | Text | None | Required for the Maps module to function. Enter your valid Google Maps API key. See Elegant Themes documentation for steps to create one. |
| Use Google Fonts | Toggle | Enabled | Enable to load Google Fonts on your site. Disable to reduce external requests and improve performance if you're using a local font stack. |
| Google Fonts Subsets | Multi-select | English | Select non-English language subsets to enable Google Fonts support for international characters (e.g., Cyrillic, Greek, Hebrew). |
| Enqueue Google Maps Script | Toggle | Enabled | Controls whether the Google Maps API script loads site-wide. Disable if a third-party plugin also loads this script to avoid conflicts. Note: the Maps module will be unavailable if disabled. |
| Social Icons | Toggle + URLs | Disabled | Enable and configure social media profile icons (Facebook, X/Twitter, Instagram, RSS) that appear in the header/footer. Paste the full URL to each profile. |
| Custom CSS | Textarea | None | Add custom CSS that applies globally to your entire site. This field syncs with **Appearance → Customize → Additional CSS** in WordPress. |

![General tab settings](../assets/screenshots/builder/divi-5-theme-options/settings-general.png){ loading=lazy }
*The General tab contains logo, navigation, and display options.*

### Navigation Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Primary Menu | Select | Unassigned | Choose which WordPress menu displays as the primary navigation. If none is selected, no menu will display. |
| Mobile Menu | Select | Unassigned | Specify a dedicated mobile menu, or leave unassigned to use the primary menu on mobile devices. |
| Vertical Menu Toggle | Select | Hamburger | Choose the icon style for the mobile menu toggle button (hamburger, lines, etc.). |
| Menu Text Color | Color | Inherited | Set the text color for navigation links. Inherits theme color if not specified. |
| Hover Color | Color | Accent Color | Set the color of navigation links when hovered. |
| Active Link Color | Color | Accent Color | Set the color of the currently active navigation link. |

![Navigation tab settings](../assets/screenshots/builder/divi-5-theme-options/settings-navigation.png){ loading=lazy }
*Configure header menus and styling in the Navigation tab.*

### Builder Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Post Type Integration | Multi-select | Pages, Posts | Choose which post types (pages, posts, custom post types, WooCommerce products) can use the Divi Builder. |
| Enable Theme Builder | Toggle | Enabled | Turn Theme Builder on or off. When disabled, Divi Builder is available but Theme Builder features (global headers/footers) are unavailable. |
| Visual Builder Default | Select | Enabled | Set whether the Visual Builder or Code Editor opens by default when editing a page. |
| Divi Product Tour | Toggle | Enabled | Enable the interactive product tour that highlights Divi features for new users in the Visual Builder. |
| Classic Editor Compatibility | Toggle | Disabled | Enable to force the WordPress Classic Editor to load instead of the Gutenberg block editor. |
| Divi 4 Shortcode Framework | Toggle | Disabled | Enable only if you have legacy Divi 4 shortcodes that need compatibility support. |

![Builder tab settings](../assets/screenshots/builder/divi-5-theme-options/settings-builder.png){ loading=lazy }
*The Builder tab controls Divi Builder availability and default behaviors.*

### Layout Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Posts Per Page (Category) | Number | WordPress default | Set how many posts display per page on category archive pages. Overrides WordPress Reading settings for categories only. |
| Posts Per Page (Archive) | Number | WordPress default | Set how many posts display per page on date, author, and other archive pages. |
| Posts Per Page (Search) | Number | WordPress default | Set how many posts display per page in search results. |
| Posts Per Page (Tag) | Number | WordPress default | Set how many posts display per page on tag archive pages. |
| Products Per Page (WooCommerce) | Number | WordPress default | Set how many products display per page on the shop page and product category pages. |
| Date Format | Select | Site Default | Choose how dates are formatted throughout the site (e.g., "January 5, 2026" vs. "2026-01-05"). Follows WordPress date format options. |
| Use Post Excerpts | Toggle | Enabled | When enabled, post excerpts display on archive/index pages if manually created. When disabled, no excerpt displays regardless. |
| Back to Top Button | Toggle | Enabled | Enable a floating "back to top" button that appears in the bottom-right corner on pages taller than one viewport height. |
| Smooth Scrolling | Toggle | Enabled | When enabled, page scrolling and anchor links animate smoothly. Disable for instant scrolling. |
| Enable Responsive Images | Toggle | Enabled | Enable to generate multiple image sizes (srcset) when uploading images, allowing browsers to load the optimal size for each device. |

![Layout tab settings](../assets/screenshots/builder/divi-5-theme-options/settings-layout.png){ loading=lazy }
*Configure post counts, date formatting, and responsive behavior in the Layout tab.*

### SEO Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Site Title | Text | WordPress Site Title | Override the site title used in search engine results. If blank, uses WordPress Site Title setting. |
| Site Description | Textarea | WordPress Tagline | Override the site description (meta description) used in search results. If blank, uses WordPress tagline. |
| OpenGraph Image | Image Upload | None | Set a default OpenGraph image displayed when your site is shared on social media. |
| Twitter Card Type | Select | Summary | Choose the format for Twitter card previews: Summary or Summary with Large Image. |

![SEO tab settings](../assets/screenshots/builder/divi-5-theme-options/settings-seo.png){ loading=lazy }
*The SEO tab provides site-wide search and social sharing configuration.*

### Ads Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Ad Network Integration | Select | None | Choose which ad network to integrate (Google AdSense, etc.). Follow instructions to authenticate. |
| Ad Placement Rules | Varies | None | Configure where ads display (before posts, after posts, between paragraphs, etc.). |

### Integration Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Google Analytics Code | Textarea | None | Paste your Google Analytics measurement ID or tracking code here. The code loads on all pages. |
| Custom Analytics / Tracking Scripts | Textarea | None | Paste any additional tracking or analytics scripts (e.g., Facebook Pixel, Hotjar, Mixpanel, etc.). |
| Head Code | Textarea | None | Custom code to inject into the `<head>` section of every page (e.g., Meta tags, verification codes). |
| Body Code | Textarea | None | Custom code to inject at the start of the `<body>` section (e.g., tracking pixels that must load early). |
| Footer Code | Textarea | None | Custom code to inject before the closing `</body>` tag (e.g., chat widgets, analytics that defer). |

![Integration tab settings](../assets/screenshots/builder/divi-5-theme-options/settings-integration.png){ loading=lazy }
*Add analytics, tracking codes, and custom scripts in the Integration tab.*

### Updates Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Elegant Themes Username | Text | None | Your Elegant Themes account username. Required to enable automatic updates for Divi and child themes. |
| Elegant Themes API Key | Text | None | Your Elegant Themes API key (found in your ET account dashboard). Required along with username for auto-updates. |
| Enable Auto-Updates | Toggle | Enabled | When enabled, Divi automatically checks for and installs updates. Disable for manual update control. |
| Update Notifications | Toggle | Enabled | Receive email notifications when updates are available. |

![Updates tab settings](../assets/screenshots/builder/divi-5-theme-options/settings-updates.png){ loading=lazy }
*Connect your Elegant Themes account and configure update behavior in the Updates tab.*

## Common Patterns

### Configure a Basic Site Setup

1. Upload your logo in **General** → Logo
2. Set your primary menu in **Navigation** → Primary Menu
3. Create a child theme (recommended) via a child theme plugin
4. Enable post types that will use Divi Builder in **Builder** → Post Type Integration
5. Adjust post counts in **Layout** for your archive pages
6. Add your Google Analytics code in **Integration**
7. Enter your Elegant Themes credentials in **Updates** to enable auto-updates

### Export and Import Theme Options

To back up your Theme Options or move them to another site:

1. From **Divi → Theme Options**, look for the **Portability** icon (two arrows) in the top-right corner
2. Click **Export** and save the `.json` file to your computer
3. On another Divi site, open **Divi → Theme Options** and click the Portability icon
4. Click **Import** and select your saved `.json` file to restore all settings

This is especially useful when:
- Migrating a site to a new hosting provider
- Creating a staging environment with the same settings
- Sharing Theme Options with a client's development team
- Creating a backup before making major configuration changes

### Optimize Performance

Common Theme Options adjustments to improve performance:

| Setting | Optimization | Impact |
|---------|--------------|--------|
| Disable Google Fonts | If using a local font stack | Reduces external requests |
| Disable Google Maps Script | If no site uses the Maps module | Smaller initial page load |
| Disable Responsive Images | Only if images are pre-optimized | Saves image processing time |
| Disable Smooth Scrolling | Modern browser feature | Minimal impact, saves JS execution |
| Use lazy loading on images | Via a performance plugin | Defers off-screen image loads |

## Code Examples

### Programmatically Access Theme Options

```php
// Get a Theme Option value
$logo_url = get_theme_mod( 'et_divi_logo' );
$google_api = get_theme_mod( 'et_divi_google_api_key' );

// Check if a feature is enabled
$fixed_nav = get_theme_mod( 'et_divi_fixed_navigation', true );
if ( $fixed_nav ) {
    // Navigation is fixed
}

// Get custom CSS
$custom_css = get_theme_mod( 'et_divi_custom_css' );
echo wp_kses_post( $custom_css );
```

### Filter Theme Option Values

```php
// Modify logo before output
add_filter( 'theme_mod_et_divi_logo', function( $value ) {
    // Return a different logo URL based on logic
    if ( is_front_page() ) {
        return home_url( '/images/logo-homepage.png' );
    }
    return $value;
} );

// Change Google API key conditionally
add_filter( 'theme_mod_et_divi_google_api_key', function( $value ) {
    // Use different key in staging vs. production
    if ( defined( 'STAGING' ) && STAGING ) {
        return 'staging-api-key-here';
    }
    return $value;
} );
```

### Enqueue Global Styles Based on Theme Options

```php
// Add custom scripts/styles if Theme Options are enabled
add_action( 'wp_enqueue_scripts', function() {
    $smooth_scroll = get_theme_mod( 'et_divi_smooth_scrolling', true );
    if ( $smooth_scroll ) {
        wp_enqueue_script( 'smooth-scroll', get_template_directory_uri() . '/js/smooth-scroll.js' );
    }
} );
```

## Elegant Themes Tutorials

- [Setting up Theme Options](https://www.elegantthemes.com/blog/wordpress/divi-theme-options){:target="_blank"} — Initial setup walkthrough
- [Using the Divi Gallery](https://www.elegantthemes.com/blog/wordpress/divi-gallery){:target="_blank"} — Gallery configuration and features
- [WooCommerce Integration in Divi 5](https://www.elegantthemes.com/blog/wordpress/divi-woocommerce){:target="_blank"} — Setting up WooCommerce with Theme Options

## Troubleshooting

### Theme Options Not Saving

**Symptoms:** Settings in Theme Options revert to defaults after saving.

**Common causes:**
- PHP memory limit is too low; increase to at least 128MB in `wp-config.php`
- A conflicting plugin is preventing customizer changes
- Your hosting provider has disabled the WordPress Customizer API

**Solutions:**
1. Check PHP error logs for memory exhaustion errors
2. Temporarily disable all plugins and retry
3. Contact your hosting provider to ensure the WordPress Customizer is available

### Google Maps Not Displaying

**Symptoms:** Maps module shows an error or blank area even though it's configured.

**Common causes:**
- Google API Key is invalid or missing
- API Key doesn't have Maps API enabled in Google Cloud Console
- The Google Maps script is disabled in Theme Options

**Solutions:**
1. Verify the Google API Key in **Divi → Theme Options → General**
2. In Google Cloud Console, ensure both "Maps JavaScript API" and "Maps Static API" are enabled
3. Check that **Enqueue Google Maps Script** is toggled ON in Theme Options
4. Verify the key is not restricted to specific websites

### Social Icons Not Showing

**Symptoms:** Social icons don't appear in header/footer even though enabled in Theme Options.

**Common causes:**
- Social Icons are not enabled in Theme Options
- URLs are invalid or missing
- Theme Builder or custom header layout doesn't include the icon component

**Solutions:**
1. Go to **Divi → Theme Options → General** and ensure **Social Icons** is toggled ON
2. Verify that each social profile URL is complete (e.g., `https://facebook.com/yourpage`)
3. Check your Theme Builder header to ensure the social icons module is placed in the design
4. Clear your browser cache to see changes

## Related

- [Divi 5 Theme Builder](../builder/theme-builder.md) — Global headers, footers, and templates
- [Visual Builder Overview](../builder/visual-builder.md) — Page-level Divi Builder interface
- [Divi Child Themes](../builder/install-and-activate-divi-5.md) — Customization best practices

!!! note "Divi 5 Only"
    This page documents Divi 5 Theme Options exclusively. Divi 4 used a different Theme Options interface with different settings.
