---
title: "Upload SVG and JSON Files"
category: troubleshooting
tags: ["troubleshooting", "svg", "json", "file-upload", "lottie"]
related: ["lottie", "image"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11982083"
---

# Upload SVG and JSON Files

WordPress blocks SVG and JSON file uploads by default, which prevents you from using SVG images or Lottie animations (JSON) in Divi 5.

## Overview

WordPress restricts SVG and JSON uploads as a security measure. SVG files can contain embedded scripts, and JSON files may expose sensitive data. If you need to use SVG images or Lottie animations in your Divi 5 site, you must explicitly enable these file types.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11982083).

## Option 1: Use a Plugin (Recommended)

The safest approach is to use a plugin that handles file sanitization automatically.

1. Go to **Plugins > Add Plugin** in your WordPress dashboard.
2. Search for **File Upload Types by WPForms**.
3. Install and activate the plugin.
4. Navigate to **Settings > File Upload Types**.
5. Search for **SVG** and check its checkbox to enable it.
6. Click **Save Settings**.
7. Repeat for **JSON** if you need Lottie animation support.

The plugin sanitizes uploaded files automatically, reducing the risk of malicious code injection.

## Option 2: Add a Code Snippet

If you prefer not to install a plugin, add this code to your child theme's `functions.php` or use a code snippets plugin:

```php
function allow_svg_uploads( $mimes ) {
    $mimes['svg'] = 'image/svg+xml';
    return $mimes;
}
add_filter( 'upload_mimes', 'allow_svg_uploads' );

function allow_json_uploads( $mimes ) {
    $mimes['json'] = 'application/json';
    return $mimes;
}
add_filter( 'upload_mimes', 'allow_json_uploads' );
```

!!! warning "No built-in sanitization"
    This method does not sanitize uploaded files. Only upload SVGs and JSON files from sources you trust completely.

## Best Practices

- **Sanitize SVGs before uploading** using a tool like [SVGOMG](https://jakuba.net/svgomg/) to strip unnecessary metadata and potential script tags.
- **Restrict upload permissions** to administrators or trusted roles only.
- **Maintain regular backups** so you can recover quickly if a malicious file is uploaded.

## Related

- [Lottie Module](../modules/lottie.md)
- [Image Module](../modules/image.md)
