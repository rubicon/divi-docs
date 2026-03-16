---
title: "Speculative Prerendering"
category: builder
tags: ["builder", "performance", "prerendering", "speed", "navigation"]
related: ["visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13820117"
---

# Speculative Prerendering

Preload pages in the background based on cursor movement so builder navigation feels instant.

## Overview

Speculative Prerendering uses the browser's Speculation Rules API to begin loading a page before you actually click the link. Divi monitors your cursor position and, when the mouse approaches a navigation target (such as the "Edit with Divi" button in the admin bar or a result in the Command Center), it triggers a background prerender of the destination page. By the time you click, the page is already loaded, eliminating or dramatically reducing perceived load times.

This feature operates entirely within the builder and WordPress admin context -- it does not affect front-end page loads for site visitors. It is enabled by default and can be toggled off if server resources are constrained.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13820117).

## How It Works

| Step | Detail |
|------|--------|
| 1. Cursor approaches a link | Divi detects the mouse moving toward a clickable navigation target |
| 2. Prerender begins | The browser starts loading the destination page in a hidden background tab |
| 3. User clicks | The fully (or partially) loaded page is swapped in immediately |
| 4. Result | Near-instant navigation with no visible loading delay |

Prerendering is limited to same-domain pages. Only builder and admin navigation targets are prerendered -- external links are not affected.

## Where Prerendering Activates

| Context | Trigger |
|---------|---------|
| Admin bar | Cursor moves toward the "Edit with Divi" button |
| Builder exit | Navigating from the builder back to the WordPress editor or front end |
| Command Center (Cmd+K / Ctrl+K) | Typing a page name or selecting a result in the command palette |

## Settings

### Enable / Disable

1. Open any page in the Divi 5 Visual Builder.
2. Click the **Builder Settings** icon in the left sidebar.
3. Toggle **Speculative Prerendering** on or off.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Speculative Prerendering | Toggle | Enabled | Controls whether background prerendering is active in the builder |

## Browser Support

Speculative Prerendering depends on the Speculation Rules API, which is not yet universally supported.

| Browser | Supported |
|---------|-----------|
| Chrome | Yes |
| Edge | Yes |
| Opera | Yes |
| Safari | No |
| Firefox | No |

On unsupported browsers, the feature is silently inactive. No errors are thrown, and navigation works normally with standard load times.

## Performance Considerations

- **Benefit scales with server speed.** On slow hosting, a 5-second load reduced by 1.5 seconds is a 30% improvement in perceived speed. On fast hosting, the benefit is smaller but still noticeable.
- **Each prerender is a server request.** If your server is resource-constrained, the additional background requests could add load. Disable the feature in that situation.
- **No front-end impact.** This feature only operates within the builder and admin screens. Site visitors are not affected.
- **No configuration needed.** The default on-state works automatically for supported browsers.

## Tips and Best Practices

- **Leave it enabled unless you have a reason to disable.** The default behavior benefits all Chromium-based browser users at no configuration cost.
- **Monitor server resources if hosting is limited.** Each prerender counts as a full page request. Shared or low-resource hosting plans may benefit from disabling the feature.
- **Combine with the Command Center.** The speed benefit is most noticeable when using Cmd+K / Ctrl+K to navigate between pages -- the prerender fires as soon as you highlight a result.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If the Speculative Prerendering toggle is not visible in Builder Settings, ensure you are running the latest version of Divi 5.

- **Navigation still feels slow.** Check your browser -- Safari and Firefox do not support the Speculation Rules API. Switch to Chrome or Edge to benefit from prerendering.
- **Server load increased after enabling.** Each prerender generates a page request. On resource-limited hosting, disable the toggle to reduce load.
- **Feature is enabled but navigation is not instant.** The prerender may not finish before you click if the server response is very slow. The feature reduces load time but cannot eliminate it entirely on very slow servers.

## Related

- [Visual Builder](visual-builder.md)
