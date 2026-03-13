---
title: "Common CSS Overrides"
category: css-reference
tags: [css, overrides, customization, header, navigation, typography, buttons, responsive]
related: [class-reference]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: ""
---

# Common CSS Overrides

A collection of tested CSS snippets for the most frequently requested Divi 5 customizations. Each override includes the CSS code, an explanation of what it does, and notes on where to add it.

## Overview

While Divi 5's module settings cover most styling needs, some design requirements call for custom CSS. This page collects the overrides that Divi developers reach for most often: header adjustments, spacing fixes, typography tweaks, button restyling, responsive breakpoint handling, and visibility control.

All CSS on this page can be added via one of three methods:

1. **Divi Theme Options > General > Custom CSS** -- site-wide CSS that persists across theme updates.
2. **A child theme's `style.css`** -- recommended for production sites.
3. **A module's Advanced > Custom CSS** fields -- scoped to a single module instance.

For specificity, most overrides use `body` as a prefix. If an override does not work, increase specificity or add `!important` (see the troubleshooting section at the bottom).

## Header & Navigation Overrides

### Make the header transparent

Overlay the header on top of the first section (hero pattern):

```css
/* Transparent header with white text */
#main-header {
    background-color: transparent !important;
    position: absolute;
    width: 100%;
    z-index: 9999;
}

/* White logo text and menu links */
#main-header .logo_container a,
#top-header .et-menu li a,
#et-top-navigation .et-menu li a {
    color: #ffffff !important;
}

/* White hamburger icon on mobile */
.mobile_menu_bar:before {
    color: #ffffff !important;
}
```

### Change header background on scroll (sticky header)

Divi adds `.et-fixed-header` to the header when the user scrolls down:

```css
/* Default: transparent */
#main-header {
    background-color: transparent !important;
    transition: background-color 0.3s ease;
}

/* Scrolled: solid white */
#main-header.et-fixed-header {
    background-color: #ffffff !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

/* Swap link color when scrolled */
#main-header.et-fixed-header #et-top-navigation .et-menu li a {
    color: #333333 !important;
}
```

### Change the active menu item style

```css
/* Active page: underline effect */
#top-menu li.current-menu-item a {
    color: #7c4dff !important;
    border-bottom: 2px solid #7c4dff;
    padding-bottom: 4px;
}

/* Hover state */
#top-menu li a:hover {
    color: #7c4dff !important;
    opacity: 0.9;
}
```

### Reduce header height

```css
#main-header,
#main-header.et-fixed-header {
    padding-top: 10px !important;
    padding-bottom: 10px !important;
}

/* Shrink the logo proportionally */
#logo {
    max-height: 50px;
}
```

### Style dropdown submenus

```css
#top-menu li ul.sub-menu {
    background-color: #2d2d2d;
    border-top: 3px solid #7c4dff;
    border-radius: 0 0 4px 4px;
    padding: 10px 0;
}

#top-menu li ul.sub-menu li a {
    color: #ffffff !important;
    padding: 8px 20px;
    font-size: 14px;
}

#top-menu li ul.sub-menu li a:hover {
    background-color: #7c4dff;
    color: #ffffff !important;
}
```

## Module Spacing Overrides

### Remove default section padding

```css
/* Remove top and bottom padding from all sections */
.et_pb_section {
    padding: 0 !important;
}
```

### Set consistent section spacing

```css
/* 80px vertical padding on desktop */
.et_pb_section {
    padding-top: 80px !important;
    padding-bottom: 80px !important;
}

/* 50px on tablet */
@media (max-width: 980px) {
    .et_pb_section {
        padding-top: 50px !important;
        padding-bottom: 50px !important;
    }
}

/* 30px on phone */
@media (max-width: 767px) {
    .et_pb_section {
        padding-top: 30px !important;
        padding-bottom: 30px !important;
    }
}
```

### Remove row padding

```css
.et_pb_row {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}
```

### Set a maximum content width

```css
.et_pb_row {
    max-width: 1200px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
```

### Remove module bottom margin

Divi adds a default bottom margin to most modules:

```css
/* Remove bottom margin from all modules */
.et_pb_module {
    margin-bottom: 0 !important;
}

/* Or target specific modules */
.et_pb_text {
    margin-bottom: 0 !important;
}
.et_pb_image {
    margin-bottom: 0 !important;
}
```

### Remove column gutters

```css
.et_pb_gutters3 .et_pb_column {
    margin-right: 0 !important;
}

.et_pb_gutters3 .et_pb_column:last-child {
    margin-right: 0 !important;
}
```

## Typography Overrides

### Set global heading styles

```css
/* Global heading hierarchy */
body h1 {
    font-family: 'Inter', sans-serif;
    font-size: 48px;
    font-weight: 700;
    line-height: 1.2;
    color: #1a1a2e;
}

body h2 {
    font-family: 'Inter', sans-serif;
    font-size: 36px;
    font-weight: 700;
    line-height: 1.25;
    color: #1a1a2e;
}

body h3 {
    font-family: 'Inter', sans-serif;
    font-size: 28px;
    font-weight: 600;
    line-height: 1.3;
    color: #1a1a2e;
}

body h4 {
    font-family: 'Inter', sans-serif;
    font-size: 22px;
    font-weight: 600;
    line-height: 1.35;
    color: #333333;
}
```

### Set global body text style

```css
body,
.et_pb_text p,
.et_pb_blurb_description p {
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    line-height: 1.7;
    color: #555555;
}
```

### Style links globally

```css
body a,
.et_pb_text a {
    color: #7c4dff;
    text-decoration: none;
    transition: color 0.2s ease;
}

body a:hover,
.et_pb_text a:hover {
    color: #5c35cc;
    text-decoration: underline;
}
```

### Override Divi's heading letter-spacing

Divi sometimes applies letter-spacing to headings. Reset it:

```css
h1, h2, h3, h4, h5, h6,
.et_pb_module h1, .et_pb_module h2,
.et_pb_module h3, .et_pb_module h4 {
    letter-spacing: 0 !important;
}
```

## Button Style Overrides

### Override all Divi buttons

Divi uses `.et_pb_button` for all button elements across modules:

```css
body .et_pb_button {
    font-family: 'Inter', sans-serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
    padding: 12px 28px !important;
    border: 2px solid #7c4dff !important;
    border-radius: 6px !important;
    background-color: #7c4dff !important;
    color: #ffffff !important;
    transition: all 0.3s ease !important;
}

body .et_pb_button:hover {
    background-color: #5c35cc !important;
    border-color: #5c35cc !important;
    color: #ffffff !important;
    letter-spacing: 0 !important;
    padding: 12px 28px !important;
}
```

### Remove the Divi button arrow icon

Divi buttons show an arrow icon on hover by default:

```css
body .et_pb_button:after {
    display: none !important;
}

/* Reset the extra right padding that accommodates the arrow */
body .et_pb_button:hover {
    padding: 12px 28px !important;
}
```

### Create a secondary (outline) button style

Use a custom CSS class on the module to apply an alternate button style:

```css
/* Apply class "outline-btn" to the Button module's CSS Class field */
body .outline-btn .et_pb_button,
body .et_pb_button.outline-btn {
    background-color: transparent !important;
    color: #7c4dff !important;
    border: 2px solid #7c4dff !important;
}

body .outline-btn .et_pb_button:hover,
body .et_pb_button.outline-btn:hover {
    background-color: #7c4dff !important;
    color: #ffffff !important;
}
```

### Full-width button

```css
body .full-width-btn .et_pb_button {
    display: block !important;
    text-align: center !important;
    width: 100% !important;
}
```

## Responsive Breakpoints

Divi 5 uses two primary breakpoints:

| Breakpoint | Max Width | Target |
|------------|-----------|--------|
| Tablet | 980px | Screens 768px -- 980px |
| Phone | 767px | Screens below 768px |

### Responsive template

```css
/* Desktop (default -- no media query needed) */
.my-element {
    font-size: 18px;
    padding: 40px;
}

/* Tablet */
@media (max-width: 980px) {
    .my-element {
        font-size: 16px;
        padding: 30px;
    }
}

/* Phone */
@media (max-width: 767px) {
    .my-element {
        font-size: 14px;
        padding: 20px;
    }
}
```

### Stack columns on tablet

By default Divi stacks columns at 980px. To keep columns side-by-side on tablet:

```css
@media (min-width: 768px) and (max-width: 980px) {
    .et_pb_column_1_2 {
        width: 48% !important;
        margin-right: 4% !important;
        float: left !important;
    }

    .et_pb_column_1_2:nth-child(2n) {
        margin-right: 0 !important;
    }
}
```

### Force single-column on tablet

```css
@media (max-width: 980px) {
    .et_pb_column {
        width: 100% !important;
        margin-right: 0 !important;
        float: none !important;
    }
}
```

### Hide the mobile menu hamburger text

```css
@media (max-width: 980px) {
    .mobile_menu_bar:before {
        font-size: 32px;
    }

    .et_mobile_nav_menu .mobile_nav span.select_page {
        display: none !important;
    }
}
```

## Hiding and Showing Elements

### Hide an element on specific devices

```css
/* Hide on phone only */
@media (max-width: 767px) {
    .hide-on-phone {
        display: none !important;
    }
}

/* Hide on tablet only */
@media (min-width: 768px) and (max-width: 980px) {
    .hide-on-tablet {
        display: none !important;
    }
}

/* Hide on desktop only */
@media (min-width: 981px) {
    .hide-on-desktop {
        display: none !important;
    }
}
```

### Show an element only on mobile

```css
/* Hidden by default */
.mobile-only {
    display: none !important;
}

/* Visible on phone */
@media (max-width: 767px) {
    .mobile-only {
        display: block !important;
    }
}
```

### Hide the top header bar on mobile

```css
@media (max-width: 980px) {
    #top-header {
        display: none !important;
    }
}
```

### Hide the Divi footer credits

```css
#footer-info {
    display: none !important;
}
```

## Image Overrides

### Force images to full width inside modules

```css
.et_pb_image img,
.et_pb_blurb_image img {
    width: 100% !important;
    height: auto !important;
}
```

### Add a rounded corners to all images

```css
.et_pb_image img {
    border-radius: 8px;
}
```

### Add a hover zoom effect to images

```css
.et_pb_image {
    overflow: hidden;
    border-radius: 8px;
}

.et_pb_image img {
    transition: transform 0.4s ease;
}

.et_pb_image:hover img {
    transform: scale(1.05);
}
```

## Blog Module Overrides

### Style blog post cards in grid layout

```css
.et_pb_blog_grid .et_pb_post {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    overflow: hidden;
    transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.et_pb_blog_grid .et_pb_post:hover {
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    transform: translateY(-2px);
}

.et_pb_blog_grid .et_pb_post .post-content-inner {
    padding: 20px;
}
```

### Remove the "read more" link

```css
.et_pb_blog_grid .et_pb_post .more-link,
.et_pb_posts .et_pb_post .more-link {
    display: none !important;
}
```

## Form Overrides

### Style contact form inputs

```css
.et_pb_contact_form_container .input {
    border: 1px solid #e0e0e0 !important;
    border-radius: 4px !important;
    padding: 12px 16px !important;
    font-size: 16px !important;
    background-color: #fafafa !important;
    transition: border-color 0.2s ease;
}

.et_pb_contact_form_container .input:focus {
    border-color: #7c4dff !important;
    outline: none !important;
    background-color: #ffffff !important;
}

/* Submit button */
.et_pb_contact_form_container .et_pb_contact_submit {
    background-color: #7c4dff !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 14px 32px !important;
    font-weight: 600 !important;
    cursor: pointer;
}
```

## Where to Add Custom CSS

| Method | Scope | Survives Updates | Best For |
|--------|-------|------------------|----------|
| Divi Theme Options > Custom CSS | Site-wide | Yes | Quick site-wide tweaks |
| Child theme `style.css` | Site-wide | Yes | Production sites with many overrides |
| Module > Advanced > Custom CSS | Single module | Yes | Module-specific one-off styles |
| Additional CSS (Customizer) | Site-wide | Yes | Small tweaks without leaving the front end |
| Custom plugin with `wp_enqueue_style` | Site-wide | Yes | Team workflows, version-controlled CSS |

!!! tip "Use a child theme for production"
    For sites with more than a handful of CSS overrides, a child theme is the most maintainable approach. It keeps your CSS in version control and separated from Divi's files.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Class names and selectors are verified against Divi 5. Some selectors that worked in Divi 4 may require adjustment due to changes in Divi 5's HTML structure and class naming.

## Troubleshooting

!!! warning "CSS override not applying"
    **Symptom:** You added CSS but the element does not change.

    **Possible causes:**

    - **Specificity:** Divi's built-in styles have higher specificity. Prefix your selector with `body` or the page ID, or use `!important`.
    - **Caching:** A caching plugin or CDN is serving the old stylesheet. Clear all caches and test in an incognito window.
    - **Load order:** Your CSS loads before Divi's. Ensure your stylesheet depends on Divi's CSS handle (`divi-style`).

    **Fix:** Open DevTools, inspect the element, and check which styles are winning. Look for crossed-out rules to identify specificity conflicts.

!!! warning "Override works on desktop but not mobile"
    **Symptom:** Your CSS looks correct on desktop but reverts or breaks on smaller screens.

    **Possible cause:** Divi applies responsive styles using `@media` queries that may override your desktop-only CSS at smaller breakpoints.

    **Fix:** Add your override inside the appropriate `@media` query to match Divi's breakpoints (980px for tablet, 767px for phone).

## Related

- [CSS Class Reference](../css-reference/class-reference.md)
- [CSS in Divi 5 Playbook](../playbooks/css-in-divi.md)
- [Responsive Design Playbook](../playbooks/responsive-design.md)
