---
title: "Design System Setup"
category: playbooks
tags: [design-system, variables, typography, colors, globals, setup]
related: [build-a-page, visual-builder-ops]
divi_version: "5.x"
last_updated: 2026-03-12
content_type: playbook
audience: llm
---

# Playbook: Design System Setup

**Configure global typography, colors, and design variables BEFORE building any pages.**

!!! danger "CRITICAL: Do This First"
    If you skip this step, every text module on every page will need manual font, size, and color overrides. Setting globals first means ~80% of text styling is automatic. This is the single highest-leverage step in any Divi 5 build.

## Why This Matters

Divi 5 modules inherit from Theme Customizer globals. If the globals match the target design, most modules will look correct by default. Without globals set first, you'll spend exponentially more time on per-module styling and fight Divi's defaults (14px body text, 30px headings) on every single element.

Color globals (accent, link, header) cascade into buttons, links, and heading modules site-wide. Get these right once and they propagate everywhere.

## Step-by-Step Process

### Step 1: Audit the Target Design

Before touching Divi, identify these values from the client's style guide, existing site, or design comp:

| Token | What to Find | Example |
|-------|-------------|---------|
| Heading font | Font family + weight for H1-H6 | Poppins, 600 (Semi Bold) |
| Body font | Font family + weight for paragraphs | Rubik, 400 (Regular) |
| Heading color | Color for all heading tags | #223547 |
| Body text color | Color for paragraphs and general copy | #333333 |
| Accent color | Buttons, links, CTAs | #037d87 |
| Link color | Hyperlink color (often same as accent) | #037d87 |
| Section background colors | Alternating section backgrounds | #ffffff, #eeeeee, #3546b1 |
| Heading sizes | H1 through H6 base sizes | H1: 48px, H2: 36px, H3: 28px |
| Body text size | Base paragraph size | 17px |
| Line heights | Heading and body line heights | Headings: 1.2, Body: 1.5 |

### Step 2: Set Globals via Theme Customizer

Navigate to **Appearance → Customize** (or **Divi → Theme Customizer**).

The fastest method is using the `wp.customize` JavaScript API from the browser console while on the Customizer page:

```javascript
const api = wp.customize;

// Typography
api('et_divi[body_font]').set('Rubik');
api('et_divi[body_font_weight]').set('400');
api('et_divi[body_font_size]').set('17');
api('et_divi[body_line_height]').set('1.5');

// IMPORTANT: The key is "heading_font_weight", NOT "header_font_weight"
api('et_divi[heading_font_weight]').set('600');
api('et_divi[header_text_size]').set('36');
api('et_divi[header_line_height]').set('1.2');

// Colors
api('et_divi[header_color]').set('#223547');
api('et_divi[font_color]').set('#333333');
api('et_divi[accent_color]').set('#037d87');
api('et_divi[link_color]').set('#037d87');
```

Then click **Publish** in the Customizer.

### Step 3: Set the Heading Font via UI

The Divi font dropdown contains 11,000+ Google Fonts. Scrolling manually is impractical. Use JavaScript to find and click the target font:

```javascript
// Open the heading font dropdown first, then run:
const allLis = document.querySelectorAll('.customize-control li');
for (const li of allLis) {
  if (li.textContent.trim() === 'Poppins') {
    li.scrollIntoView({ block: 'center' });
    li.click();
    break;
  }
}
```

### Step 4: Configure Divi 5 Design Variables

After setting Theme Customizer globals, open the Visual Builder and configure **Design Variables** (Variable Manager):

- Map your hex colors to named variables (Primary, Secondary, Accent, etc.)
- Map font families and sizes to variables
- These variables can then be referenced in any module's settings

Audit the default Divi 5 variables against the client's style guide — the defaults may not match. Fix variables first, then verify that Element Presets (which inherit variable values) look correct.

### Step 5: Use Site Variables in Module Settings

When editing any field in the Design panel (spacing, sizing, typography, color, etc.), clicking into the field reveals a small **database icon** at the right edge. Clicking this icon lets you insert a **site variable** — a global design token from the Variable Manager.

**Use site variables instead of hardcoded values** whenever a value should be global: accent color, standard section padding, maximum content width. This means updating the global variable automatically propagates to every module using it — no hunting through dozens of modules to change a padding value.

### Step 6: Verify

Open any page with Divi content. Text modules should display the correct fonts, sizes, and colors without any per-module overrides. If they don't, check:

1. Did you click Publish in the Customizer?
2. Is there a caching plugin serving stale CSS? Clear caches.
3. Are there child theme CSS rules overriding the globals?

## Known Gotchas

!!! warning "Font dropdown shows 'Default Theme Font' after API set"
    After setting `body_font` via the JavaScript API, the dropdown may still visually display "Default Theme Font." This is cosmetic. Verify with `api('et_divi[body_font]').get()` — it will return the correct value. The setting saves correctly when Published.

!!! warning "Numeric fields need UI interaction"
    Body Text Size, Header Text Size, and Line Height fields are sometimes easier to set through the Customizer UI directly: triple-click the input field to select the value, then type the new number. The JavaScript API works but the UI may not reflect the change visually until you click away.

!!! warning "Variable Manager vs Theme Options: don't duplicate"
    Use Divi 5's Variable Manager as the primary system for design tokens. Use Theme Options > Custom CSS only for effects the Variable Manager can't handle (section numbering, card hover effects, sticky CTAs). Avoid setting the same values in both places — it creates maintenance confusion.

## When Assisting a User

If someone asks you to help build a Divi 5 site, your FIRST question should be: "Have you set up your global typography and colors in the Theme Customizer yet?" If the answer is no or unclear, walk them through this playbook before building any pages. It will save hours of per-module styling work later.
