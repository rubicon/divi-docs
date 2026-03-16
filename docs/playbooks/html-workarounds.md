---
title: "HTML Workarounds"
description: "LLM playbook for Divi 5 HTML workarounds — table-based cards, inline SVG icons, logo bars, and styled layouts that survive WordPress content sanitization."
category: playbooks
tags: [html, tables, svg, inline-css, workarounds, cards, icons]
related: [css-in-divi, known-limitations]
divi_version: "5.x"
last_updated: 2026-03-12
content_type: playbook
audience: llm
---

# Playbook: HTML Workarounds

**Patterns for building complex layouts inside Divi text blocks using HTML that survives WordPress content sanitization.**

!!! abstract "Quick Rules"
    1. Use HTML tables for card-style layouts inside Divi text blocks — `<table>`, `<tr>`, `<td>` and their `style` attributes survive WordPress content sanitization.
    2. Only use these workarounds when Divi's native module settings cannot achieve the layout — prefer built-in modules for maintainability.
    3. SVG icons survive WordPress content filtering when placed inside table cells — use `stroke` styles with `fill="none"` for line-art icons.
    4. For full-bleed background images in text blocks, set the row to `maxWidth: 100%` with zero padding.

## When to Use These

Use these patterns when:
- Divi's native module settings can't achieve the layout you need
- You need card-style borders/shadows on groups of content
- You need inline SVG icons
- Column/Row visual controls are unreliable for your specific layout
- You're working with programmatic content (REST API) where Divi module JSON is cumbersome

Do NOT use these when a native Divi module handles the job well. These are workarounds, not replacements.

## Why Tables Work

WordPress strips many inline HTML elements and attributes during content sanitization, but `<table>`, `<tr>`, `<td>`, and their `style` attributes are allowed through. This makes tables a reliable vehicle for styled layouts inside Divi text blocks.

## Pattern: Card with Border and Shadow

Creates a card-style container with rounded corners and a subtle shadow:

```html
<table style="width:100%; border:1px solid #e0e0e0; border-radius:12px; text-align:center; padding:30px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
  <tr><td style="text-align:center; padding:10px 15px;">
    <h3 style="color:#1B4F72; margin-top:15px; font-size:22px;">Card Title</h3>
    <p style="color:#555; font-size:15px; line-height:1.6;">Card description text goes here.</p>
  </td></tr>
</table>
```

## Pattern: Card with Inline SVG Icon

SVG icons survive WordPress content filtering when placed inside table cells. Use `stroke` styles with `fill="none"` for line-art icons:

```html
<table style="width:100%; border:1px solid #e0e0e0; border-radius:12px; text-align:center; padding:30px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
  <tr><td style="text-align:center; padding:10px 15px;">
    <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- SVG path data here -->
    </svg>
    <h3 style="color:#1B4F72; margin-top:15px; font-size:22px;">Service Name</h3>
    <p style="color:#555; font-size:15px; line-height:1.6;">Service description.</p>
  </td></tr>
</table>
```

## Pattern: Stacked Image Cards

When content is baked into images (common in site migrations), stack them in card-style tables within a single text block:

```html
<table style="width:100%; max-width:800px; margin:0 auto 30px auto; border:1px solid #e0e0e0; border-radius:12px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.08);">
  <tr><td><img style="width:100%; height:auto; display:block;" src="image-1.png" alt="Description" /></td></tr>
</table>

<table style="width:100%; max-width:800px; margin:0 auto 30px auto; border:1px solid #e0e0e0; border-radius:12px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.08);">
  <tr><td><img style="width:100%; height:auto; display:block;" src="image-2.png" alt="Description" /></td></tr>
</table>
```

**Key insight:** Consolidating multiple small Divi columns (e.g., three 1/3 columns) into a single full-width column with stacked table cards often produces a better visual result and reduces block structure complexity.

## Pattern: Logo Bar with CSS Filter

Display partner logos at consistent sizing with white coloring on dark backgrounds:

```html
<table style="width:100%; max-width:1100px; margin:0 auto; border-collapse:collapse;">
  <tr>
    <td style="text-align:center; padding:15px 25px; vertical-align:middle;">
      <img src="logo-1.png" style="max-height:60px; width:auto; filter:brightness(0) invert(1); opacity:1;" alt="Partner 1" />
    </td>
    <td style="text-align:center; padding:15px 25px; vertical-align:middle;">
      <img src="logo-2.png" style="max-height:60px; width:auto; filter:brightness(0) invert(1); opacity:1;" alt="Partner 2" />
    </td>
    <!-- Repeat for each logo -->
  </tr>
</table>
```

**CSS filter trick:** `filter:brightness(0) invert(1)` converts any colored PNG logo to pure white. Works regardless of original logo colors — no need for separate white-version logo files.

## Pattern: Two-Column Stat Layout

For side-by-side statistics or metrics where Divi column controls are unreliable:

```html
<table style="width:100%; max-width:900px; margin:0 auto;">
  <tr>
    <td style="width:50%; vertical-align:top; padding:20px;">
      <h3 style="font-size:48px; color:#ffffff;">173,000+</h3>
      <p style="color:#e0e0e0;">Small businesses served</p>
    </td>
    <td style="width:50%; vertical-align:top; padding:20px;">
      <h3 style="font-size:48px; color:#ffffff;">4.5M</h3>
      <p style="color:#e0e0e0;">Employees covered</p>
    </td>
  </tr>
</table>
```

## Pattern: Full-Bleed Background Image Section

When Divi SSR doesn't render section-level background images reliably, use inline CSS in a text block inside a full-width row:

```html
<div style="background: linear-gradient(rgba(10,30,80,0.75), rgba(10,30,80,0.75)), url(https://site.com/image.jpg) center/cover no-repeat; padding: 80px 20px; text-align:center;">
  <h2 style="color:#ffffff; font-size:36px;">Section Heading</h2>
  <p style="color:#e0e0e0; font-size:18px; max-width:700px; margin:0 auto;">Supporting text for this section.</p>
</div>
```

!!! warning "Row Must Be Full-Width"
    When the background image lives inside a text block (not at the section level), the row must have `maxWidth: 100%` and zero padding for the image to span edge-to-edge. See the [Known Limitations](known-limitations.md) playbook for row width details.

## When Guiding a User

If someone asks you to build a layout that Divi's native controls handle poorly (multi-card grids, icon cards with shadows, logo bars on dark backgrounds), suggest these HTML table patterns. They're more reliable than fighting with Divi's column/row controls for these specific use cases, and they render consistently via SSR.

For simple layouts that Divi handles natively (single images, basic text, standard columns), always prefer Divi's built-in modules — they'll be easier for the user to maintain in the Visual Builder.
