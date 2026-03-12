---
title: "Visual Builder Operations"
category: playbooks
tags: [visual-builder, vb, ui, panels, saving, architecture]
related: [build-a-page, known-limitations]
divi_version: "5.x"
last_updated: 2026-03-12
content_type: playbook
audience: llm
---

# Playbook: Visual Builder Operations

**How Divi 5's Visual Builder works — the information an LLM needs to give accurate UI guidance.**

## Opening the Visual Builder

Navigate to any page and either:
- Click "Edit with Divi" from the WordPress admin bar
- Append `?et_fb=1&PageSpeed=off` to the page URL

Wait for both the sidebar and Layers panel to fully load before interacting.

## Interface Layout

### Sidebar (Left Side)

Icons from top to bottom:

| Icon | Function |
|------|----------|
| **+** (plus) | Add modules — opens the module picker |
| **Diamond** | Layers panel — shows the page structure tree (sections → rows → columns → modules) |
| **Pages** | Navigate between pages |
| **Clipboard** | Clipboard history |
| **Database** | Saved layouts and library |
| **Code** | Code snippets |
| **Lightning** | Display conditions |
| **List** | Settings |
| **Grid toggles** | Action icons |
| **Wrench** | Tools |
| **?** | Help |

**The Layers panel is the most reliable way to select and navigate elements.** Clicking directly on the canvas can be unreliable, especially for nested or overlapping elements.

### Top Toolbar

Settings gear, View mode toggle, Three dots (breakpoints and responsive settings), Device previews (desktop/tablet/phone), Width control, Zoom, Exit, Preview, Save (with dropdown for draft/publish options).

### Settings Panel (Right Side)

When any element is selected, the settings panel appears on the right with three tabs:

- **Content** — Module-specific content (text, images, URLs, toggles)
- **Design** — Typography, spacing, sizing, borders, box shadows, animations
- **Advanced** — CSS ID/Class, Custom CSS, Free-Form CSS, visibility, transitions

## Adding Elements

### Via the Canvas
Click the green **+ADD** button that appears on the canvas. Choose the element type (Section, Row, Module) and the specific module.

### Via the Layers Panel
Right-click any element in the Layers panel → "Add Element" → choose position (Before, After, Inside) → pick the module type.

**Recommendation for LLMs guiding users:** The Layers panel method is more predictable. Tell users to use the Layers panel rather than canvas clicks when precision matters.

## Editing Content

### Text Modules
1. Select the Text module (click it in Layers or on canvas)
2. The Content tab opens in the settings panel on the right
3. Expand the "Text" section
4. Click inside the TinyMCE editor area
5. Edit text directly — use the TinyMCE toolbar for formatting

**TinyMCE shortcuts that work:**
- Cmd+B / Ctrl+B → Bold
- Cmd+I / Ctrl+I → Italic
- Cmd+K / Ctrl+K → Insert link
- Paragraph dropdown → Change heading level (H1-H6)
- Cmd+A / Ctrl+A → Select all (useful for replacing content)

### Design Settings
1. Select the element
2. Switch to the **Design** tab
3. Expand the relevant section (Typography, Spacing, Background, etc.)
4. Click fields and type or select values

### Advanced CSS
1. Select the element
2. Switch to the **Advanced** tab
3. For simple class/ID additions → use CSS ID and CSS Class fields
4. For targeted CSS → expand "Custom CSS" to target specific sub-elements
5. For complex CSS → use "Free-Form CSS" with the `selector` keyword

The `selector` keyword in Free-Form CSS targets the module's container element:
```css
selector {
    transition: box-shadow 0.3s ease;
}
selector:hover {
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}
```

## Right-Click Context Menu

Right-clicking any element (in canvas or Layers) provides:

| Action | What It Does |
|--------|-------------|
| Undo/Redo | Standard undo/redo |
| Duplicate | Creates a copy immediately after the element |
| Delete | Removes the element |
| Add Element | Add Before, After, or Inside (for containers) |
| Lock | Prevents accidental edits |
| Copy/Cut | With sub-options for Parent, Element, or Children |
| Copy Attributes | Copy styling to paste onto another element |
| Extend Attributes | Apply styling to all instances of this module type |
| Reset Attributes | Clear all custom styling |
| Inspect | Browser developer tools |
| Save To Library | Save as a reusable layout |

## Saving

Click the **Save** button (top right). Wait 2-3 seconds for the save to complete.

**To verify the save worked:** Open the page in a new tab without `?et_fb=1` and check that the frontend renders correctly.

!!! warning "Visual Builder Save vs REST API"
    The VB save triggers Divi's internal save mechanism, which re-parses and re-serializes all blocks. It ONLY preserves blocks the builder's Layers panel can see. If the page has programmatically-added content (via REST API), the VB save may destroy sections it doesn't recognize. **Never save through the Visual Builder if the page has programmatically-added content.**

## Dual-Frame Architecture

For LLMs assisting with browser automation or advanced debugging:

Divi 5's Visual Builder uses two windows:

- **Parent window** — Contains the sidebar, settings panel (React app), toolbar, and Layers panel. This is where `window.tinymce` lives.
- **Iframe (`#et-vb-app-frame`)** — Contains the page canvas/preview. Houses the page DOM, WordPress core (`wp.*`), and Divi runtime objects.

```javascript
// Access the iframe window
const appFrame = document.querySelector('#et-vb-app-frame');
const iframeWin = appFrame.contentWindow;
```

**Key objects in the iframe:**

| Object | Contents |
|--------|----------|
| `iframeWin.DIVI` | Builder config: item counts, selectors |
| `iframeWin.ET_Builder` | Builder API: `API`, `Frames`, `Misc` |
| `iframeWin.ETCloudApp` | Cloud/Library functions |
| `iframeWin.wp` | WordPress core (hooks, i18n, ajax) — **NOTE: `wp.data` is NOT available** |

**React root:** `#et-vb-app-frame-wrapper` in the parent window. Divi 5 does NOT expose a Redux store or `wp.data` stores. State management is internal.

## Responsive Editing

Access responsive settings via the three-dot menu in the top toolbar → **Sitewide Responsive Breakpoints**.

Divi 5 uses **max-width (desktop-first)** breakpoints:
- Seven breakpoints are available
- Three are enabled by default (Desktop, Tablet, Phone <478px)
- Switch between device previews using the device icons in the toolbar
- Per-module responsive overrides are set by switching to the target device view, then modifying the setting — Divi stores device-specific values automatically
