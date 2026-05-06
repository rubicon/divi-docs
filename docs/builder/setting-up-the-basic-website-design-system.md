---
title: "Setting Up the Basic Website Design System"
category: builder
tags: ["builder", "design-system", "global-colors", "typography", "theme-customizer", "variables", "branding"]
related: ["global-variables", "design-variables", "element-presets", "advanced-styling-using-option-group-presets-in-divi-5"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/13884394-setting-up-the-basic-website-design-system"
---

# Setting Up the Basic Website Design System

Divi 5's design system provides a centralized place to define and manage your website's visual foundation: colors, typography, spacing, buttons, and layout defaults. By setting up a consistent design system early, you ensure all pages and templates follow your brand guidelines automatically.

!!! abstract "Quick Reference"
    **What it does:** Defines global design tokens (colors, fonts, spacing, button styles) that apply site-wide; inherited by all pages and templates unless overridden.
    
    **Access:** WordPress Dashboard → Divi → Theme Customizer (or Appearance → Customize)
    
    **Key sections:** General Settings, Typography, Buttons, Colors, Background
    
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/13884394-setting-up-the-basic-website-design-system)

## Overview

A well-designed website maintains consistent spacing, typography, colors, and component styles across all pages. Rather than setting button colors on every page individually, Divi's design system lets you define global defaults once and apply them everywhere.

The design system consists of:

1. **Layout Settings** — max-width, gutters, section/row heights
2. **Colors** — primary and secondary accent colors, text colors
3. **Typography** — body and heading fonts, sizes, line heights
4. **Buttons** — global button text, colors, borders, hover effects
5. **Background** — site-wide background color or image
6. **Advanced Styling** — additional color and spacing customizations

Setting these up early saves time and ensures brand consistency across your entire site.

## Accessing the Theme Customizer

The design system lives in the **Theme Customizer**:

1. Log in to your WordPress dashboard
2. Navigate to **Divi → Theme Customizer** (or **Appearance → Customize**)
3. A panel opens on the left showing customization sections
4. Changes preview live on the right side of the screen
5. Click **Publish** when done to save

## General Settings

### Site Identity

In the **Site Identity** section, set:

| Setting | Purpose |
|---------|---------|
| **Site Title** | Your website or business name (appears in browser tabs, search results, and site headers). |
| **Tagline** | A brief, one-sentence description of your business or site focus. |
| **Site Icon** | A square logo (512×512px minimum) appearing in browser tabs and bookmarks. |
| **Logo** | Your main site logo, displayed in the header. |

### Layout Settings

Navigate to **General Settings → Layout Settings** to define your site's spatial structure:

| Setting | Description |
|---------|-------------|
| **Website Content Width** | Maximum width of your main content area (typically 1200–1440px). Narrower widths feel more intimate; wider ones showcase more content. |
| **Sidebar Gutter Width** | Space between the main content and sidebar (if used). |
| **Website Gutter Width** | Space between columns inside a row (only applies if Row Layout Style is set to "Block"). Controls the gap between adjacent columns. |
| **Section Spacing** | Top and bottom padding applied to all sections site-wide. Increases breathing room on large viewports. |
| **Row Spacing** | Top and bottom padding applied to all rows. |

**Recommendations:**
- Content Width: 1200px–1440px for most sites
- Gutters: 20px–40px depending on design density
- Section Spacing: 60px–120px for airy layouts

### Background

Set your site's background:

| Setting | Purpose |
|---------|---------|
| **Background Color** | A solid background color for the entire site (typically white, light gray, or a branded color). |
| **Background Image** | Optional: a repeating or full-width background image (use carefully to avoid distracting from content). |

**Recommendations:**
- Use light, neutral colors (white, light gray, off-white) for readability
- If using an image, ensure it does not interfere with text contrast
- Test on mobile; background images can impact load time

## Colors

Primary and secondary colors serve as your brand's accent palette. These colors cascade to buttons, links, highlights, and accents throughout the site.

### Primary Color

Set your main accent color:

1. Click **General Settings → Primary Color**
2. Choose a color that reflects your brand
3. This color typically appears in:
   - Button backgrounds
   - Link colors
   - CTA elements
   - Section dividers or highlights

**Recommendation:** Choose a bold, distinctive color that stands out against your background and text.

### Secondary Color

Set a supporting accent color:

1. Click **General Settings → Secondary Color**
2. Choose a color that complements primary (e.g., complementary, analogous, or a lighter/darker variant)
3. Use for:
   - Alternate button styles
   - Secondary actions
   - Hover states
   - Accent borders or backgrounds

### Text Colors

In **General Settings → Typography**:

| Color | Purpose |
|-------|---------|
| **Body Link Color** | Links inside paragraphs (usually your primary color or a blue shade). |
| **Body Text Color** | Default text color (usually dark gray or near-black for readability). Ensure sufficient contrast with background. |

## Typography

Consistent typography strengthens your brand identity and improves readability. Define your site's font system early.

### Body Font

1. Go to **General Settings → Typography**
2. Click **Body Font**
3. Choose a readable, clean serif or sans-serif font (e.g., Open Sans, Lato, Inter)
4. Set **Body Text Size** (typically 16px–18px on desktop)
5. Set **Body Line Height** (1.4–1.6 for comfortable reading)

**Recommendations:**
- Use a sans-serif for modern, clean look (Arial, Helvetica, Open Sans, Roboto)
- Use a serif for traditional, elegant feel (Georgia, Merriweather)
- Avoid thin fonts (<400 weight) for body text; use 400 or 500 weight
- Ensure at least 1.5 line height for paragraphs

### Header Font

1. Still in **Typography**, click **Header Font**
2. Choose a font for headings (can match body or use a contrasting typeface)
3. Set **Header Text Size** — scales H1–H6 (usually 1.2–1.8 multiplier from base size)
4. Set **Header Line Height** and adjust **Letter Spacing** for impact
5. Optionally set **Header Font Weight** (700 or 800 for bold headings)

**Recommendations:**
- Use a contrasting font if body is sans-serif (e.g., Georgia for headings)
- Or reuse body font with larger size and bolder weight
- Ensure headings have sufficient contrast and are easy to scan

### Color Adjustments

In **Typography**, also set:

| Setting | Description |
|---------|-------------|
| **Body Link Color** | Color of links in paragraphs (use primary color or a distinct shade). |
| **Body Text Color** | Default paragraph text (ensure good contrast with background). |
| **Link Hover Color** | Color when hovering over links (usually a lighter or darker variant). |

## Buttons

Global button styling applies to all standard button modules across your site.

### Button Style

1. In the Customizer, click **Buttons**
2. Click **Button Style** to expand
3. Configure:

| Setting | Description |
|---------|-------------|
| **Button Text Size** | Font size for button text (typically 14px–16px). |
| **Button Text Color** | Text color (often white or contrasting with background). |
| **Button Background Color** | Button background (usually your primary color). |
| **Border Width** | Width of the button border (0 for no border, 1–3px for visible border). |
| **Border Color** | Border color (can match background, button color, or contrast). |
| **Border Radius** | Roundness of button corners (0 = square, 10px+ = rounded, 50px = pill-shaped). |

**Recommendations:**
- Use your primary color as button background
- Use white or light text for contrast
- Set border radius to 4–8px for modern feel, or 0 for minimal
- No border needed if button color provides sufficient contrast

### Button Hover Style

1. Click **Button Hover Style**
2. Define a hover effect (slight color change, border change, or shadow)
3. Examples:
   - Lighten the background by 10–15%
   - Darken the text slightly
   - Add a subtle box shadow
   - Change border color

**Recommendation:** Keep hover effects subtle; a small color shift or shadow is enough to indicate interactivity.

## Advanced Settings (Optional)

### Additional Colors

If needed, define extra colors for specific purposes:

- **Accent Color 3:** Tertiary accent for special elements
- **Error/Alert Colors:** For notifications, warnings, or error messages
- **Success/Confirmation Colors:** For positive actions or confirmations

### Spacing Scale

Define a spacing scale (commonly 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px) and apply it consistently across sections, rows, and modules.

## Building Your Design System: Step-by-Step

### 1. Define Your Brand Colors

Choose a primary and secondary color that reflect your brand:

```
Primary: #007ACC (blue)
Secondary: #FF6B35 (orange)
Background: #FFFFFF (white)
Text: #333333 (dark gray)
```

### 2. Choose Your Typography

Select two fonts (body and headings):

```
Body: Open Sans, 16px, line-height 1.6
Headings: Playfair Display, 40px–16px (H1–H6), line-height 1.4
```

### 3. Set Layout Spacing

Define your site's breathing room:

```
Content Width: 1200px
Gutter Width: 30px
Section Spacing: 80px
```

### 4. Customize Buttons

Define your button style:

```
Background: Primary Color (#007ACC)
Text: White
Border Radius: 6px
Hover: Darker blue (#005A9E)
```

### 5. Apply and Test

Click **Publish** in the Customizer, then:

- Visit your homepage and preview changes
- Check buttons, links, and text colors
- Verify readability on mobile devices
- Adjust as needed

## Common Design Systems

### Minimal / Clean

- Colors: Black, white, single accent color (navy, dark gray)
- Typography: Single sans-serif (Open Sans, Roboto)
- Buttons: Flat style, minimal border radius, sharp edges
- Spacing: Generous gutters and section spacing

### Modern / Bold

- Colors: Primary and secondary accent, white background
- Typography: Mixed (sans-serif body, serif headings)
- Buttons: Rounded corners, hover shadow effects
- Spacing: Moderate gutters, clear visual hierarchy

### Elegant / Serif

- Colors: Primary (gold, deep blue), secondary (cream), white background
- Typography: Serif body (Georgia, Merriweather), sans-serif headings
- Buttons: Bordered style, minimal background color
- Spacing: Generous padding and margins

## Testing & Refinement

After setting up your design system, test:

1. **Readability:** Text contrast, font size on mobile
2. **Brand Consistency:** Colors match across all pages
3. **Responsive:** Layout and spacing work on mobile, tablet, desktop
4. **Performance:** Check that global colors are inherited (no manual color overrides per page)

## Override When Needed

While consistency is important, you can override design system settings on individual pages or modules:

- Open a module → **Design tab** → override a color, font, or spacing
- Open a section → **Content tab** → set a custom background independent of the global setting
- These overrides take precedence over global settings

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 Theme Customizer behavior exclusively. Divi 4 used a different customization interface.

## Related

- [Global Variables](../builder/global-variables.md) — Advanced: use custom CSS variables for dynamic theming
- [Design Variables](../builder/design-variables.md) — Define reusable design tokens
- [Element Presets](../builder/element-presets.md) — Save and reuse component styles
- [Advanced Styling Using Option Group Presets in Divi 5](../builder/advanced-styling-using-option-group-presets-in-divi-5.md) — Build preset style libraries
