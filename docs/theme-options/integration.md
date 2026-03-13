---
title: "Integration Settings"
category: theme-options
tags: [theme-options, integration, tracking, analytics, code-injection, javascript, css]
related: [general, seo]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/theme-options/"
---

# Integration Settings

The Integration Settings tab provides code injection fields for adding custom CSS, JavaScript, and tracking code to various locations in your site.

## Overview

In the Integration tab, you'll find settings for enabling and adding code to the `<head>` of your blog, the `<body>` tag, and the top and bottom of single posts. This is a convenient place to add tracking pixels, analytics code, social bookmarking links, and other custom code snippets without editing theme files directly.

Each code area has a corresponding enable/disable toggle, allowing you to temporarily remove injected code while saving it for later use. This is especially useful for debugging or temporarily disabling tracking scripts.

![Integration Settings overview](../assets/screenshots/theme-options/integration/overview.png){ loading=lazy }
*The Integration Settings panel in Divi Theme Options.*

## Settings & Options

### Code Integration

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable header code | toggle | Enabled | Disabling this option removes the header code below from your blog. This allows you to remove the code while saving it for later use. |
| Enable body code | toggle | Enabled | Disabling this option removes the body code below from your blog. This allows you to remove the code while saving it for later use. |
| Enable single top code | toggle | Enabled | Disabling this option removes the single top code below from your blog. This allows you to remove the code while saving it for later use. |
| Enable single bottom code | toggle | Enabled | Disabling this option removes the single bottom code below from your blog. This allows you to remove the code while saving it for later use. |
| Add code to the `<head>` of your blog | code | — | Any code placed here will appear in the head section of every page of your blog. Useful for adding JavaScript or CSS to all pages. |
| Add code to the `<body>` (good for tracking codes such as Google Analytics) | code | — | Any code placed here will appear in the body section of all pages of your blog. Useful for inputting tracking pixels for stat counters such as Google Analytics. |
| Add code to the top of your posts | code | — | Any code placed here will be placed at the top of all single posts. Useful for integrating things such as social bookmarking links. |
| Add code to the bottom of your posts, before the comments | code | — | Any code placed here will be placed at the bottom of all single posts. Useful for integrating things such as social bookmarking links. |

## Code Examples

```html
<!-- Example: Adding Google Analytics to the <head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

```html
<!-- Example: Adding social share buttons to the top of posts -->
<div class="custom-social-share">
  <a href="https://twitter.com/intent/tweet?url={permalink}" target="_blank">Share on Twitter</a>
  <a href="https://www.facebook.com/sharer/sharer.php?u={permalink}" target="_blank">Share on Facebook</a>
</div>
```

```php
// Access integration settings programmatically
$header_code_enabled = et_get_option('divi_integration_head', 'on');
$head_code = et_get_option('divi_integration_head_code');
$body_code = et_get_option('divi_integration_body_code');
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Code Not Appearing on Site"
    If your integration code is not appearing, first check that the corresponding "Enable" toggle is turned on. Also verify that caching plugins are not serving a cached version of the page without your code. Clear all caches after adding integration code.

## Related

- [General Settings](general.md)
- [SEO Settings](seo.md)
- [Builder Settings](builder-settings.md)
