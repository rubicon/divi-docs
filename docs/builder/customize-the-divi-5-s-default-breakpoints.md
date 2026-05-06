---
title: "Customize the Divi 5's Default Breakpoints"
category: builder
tags: ["builder", "responsive", "breakpoints", "design"]
related: ["responsive-editor-in-divi-5-visual-builder.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/13001900-customize-the-divi-5-s-default-breakpoints"
---

# Customize the Divi 5's Default Breakpoints

Fine-tune responsive layouts by customizing breakpoints to match your design needs and audience devices.

## Overview

Breakpoints are screen width thresholds where your layout changes to adapt to different devices. Divi 5 comes with five default breakpoints for phone, tablet, and desktop viewing. You can customize the width of existing breakpoints and enable optional additional ones (Phone Wide, Tablet Wide, Widescreen, Ultra Wide) to create more granular responsive control.

Customizing breakpoints affects your entire site at once—all pages use the same responsive breakpoints unless you override them on individual elements.

## Default Breakpoints

Divi 5 includes these default breakpoints:

| Breakpoint | Default Width | Media Query Type | Use Case |
|-----------|---------------|------------------|----------|
| Phone | 0–480px | `min-width` | Small phones, portrait |
| Phone Wide | 481–768px | `min-width` | Large phones, landscape |
| Tablet | 769–1024px | `min-width` | Tablets, portrait |
| Tablet Wide | 1025–1440px | `min-width` | Tablets landscape, small laptops |
| Desktop | 1441px+ | Base layer | Large screens, desktops |
| Widescreen | 1441–1920px | `max-width` | 1080p+ monitors |
| Ultra Wide | 1920px+ | `max-width` | 4K monitors and beyond |

### How Breakpoints Work

- **Phone, Phone Wide, Tablet, Tablet Wide** – Use `min-width` media queries (mobile-first approach)
- **Widescreen and Ultra Wide** – Use `max-width` media queries (large-screen specific styles)
- **Desktop** – Acts as the base layer between smallest and largest breakpoints; doesn't use media queries itself
- When you set styles on multiple breakpoints, the most specific (narrowest) breakpoint applies

## Accessing Breakpoint Settings

### Option 1: Sitewide Responsive Breakpoints Modal

1. Open the **Visual Builder** on any page
2. Click the **three-dot menu icon** in the top toolbar, next to the device preview icons (phone, tablet, desktop, etc.)
3. Select **Sitewide Responsive Breakpoints**
4. A modal opens showing all available breakpoints

### Option 2: Device Selectors in the Visual Builder

1. While editing, click a **device icon** in the top bar (phone, tablet, desktop icons) to switch the preview
2. Make changes to that breakpoint
3. Your edits apply only to that breakpoint
4. Switch between devices using the same icons

### Option 3: Element-Level Device Settings

1. Click a module to open its settings panel
2. Open the **Device selection dropdown** at the top
3. Choose which device/breakpoint you want to edit
4. Switch between devices and set different values as needed

## Customizing Breakpoint Widths

### Enable or Disable a Breakpoint

1. Open **Sitewide Responsive Breakpoints** modal
2. Find the breakpoint you want (for example, Phone Wide or Widescreen)
3. Toggle it **On** to enable or **Off** to disable
4. Disabled breakpoints don't delete their styles—Divi stores them in case you re-enable the breakpoint
5. Click **Save** at the bottom of the modal

### Change a Breakpoint's Width

1. Make sure the breakpoint you want to edit is **enabled**
2. In the **Sitewide Responsive Breakpoints** modal, find that breakpoint
3. Enter the new width value (in pixels)
4. Click **Save**

### Default vs. Custom Widths

If you modify a breakpoint width, Divi shows you the original default width for reference. You can reset to default at any time.

## Common Customization Scenarios

### Scenario: Fine-Tune Phone Layouts

Phones come in many sizes. If your design feels cramped only on larger phones:

1. Keep **Phone** at 0–480px
2. Create a **Phone Wide** breakpoint starting at 481px for larger phones
3. In Phone Wide, adjust padding, font sizes, or column counts to fit better

### Scenario: Optimize for Specific Tablets

Tablets have different aspect ratios:

1. Set **Tablet** to start at a lower width (for portrait) like 600px
2. Set **Tablet Wide** for larger tablet screens (landscape) starting at 1000px
3. Adjust column layouts and spacing separately for each

### Scenario: Support Ultra-Wide Monitors

If your audience uses 4K monitors:

1. Enable **Widescreen** for 1440–1920px
2. Enable **Ultra Wide** for screens 1920px and above
3. Add styles to ensure content doesn't stretch awkwardly on massive screens

## Testing Breakpoints

### Test on a Staging Environment First

Always test breakpoint changes on a **test page first**, not on your busy production site. Create a temporary page to verify the layout looks correct at each breakpoint.

### Use Browser DevTools

1. Open your page in a browser
2. Press **F12** to open Developer Tools
3. Click the **device toggle** to view at different screen sizes
4. Test your custom breakpoints by resizing the window

### Test on Real Devices

Test on actual phones, tablets, and monitors if possible. Browser emulation is helpful but doesn't capture all real-world conditions.

## Best Practices

1. **Use Ascending Order** – Set breakpoints in ascending order (smallest to largest) and avoid tiny gaps unless you really need them. Divi will help enforce this.
2. **Think Mobile-First** – Design for mobile first, then add styles for larger screens. This ensures a solid baseline experience.
3. **Keep It Simple** – Most sites only need 3–4 breakpoints (Phone, Tablet, Desktop). Only add Widescreen/Ultra Wide if you have specific needs.
4. **Use Consistent Increments** – If you customize widths, use consistent increments (e.g., 100–200px gaps) rather than arbitrary values.
5. **Document Your Choices** – If you customize breakpoints, document why so your team understands the design system.
6. **Test Content** – Long text, images, and large forms all behave differently at different breakpoints. Test content, not just layout.

## Troubleshooting

### Styles Not Applying at a Breakpoint

- Verify the breakpoint is **enabled** in the Sitewide Responsive Breakpoints modal
- Check that you set styles on the correct breakpoint (use the device selector)
- Ensure the breakpoint width doesn't overlap with another (Divi will show a warning)

### Breakpoint Widths Keep Resetting

If breakpoint widths revert after saving:

- Check that caching plugins aren't interfering (temporarily disable them)
- Ensure you clicked **Save** in the modal before exiting
- Clear your browser cache

### Large Gap Between Breakpoints Looks Bad

- Adjust breakpoint widths to reduce gaps
- Use intermediate breakpoints (Phone Wide, Tablet Wide) to fill gaps
- Test at the exact breakpoint widths to ensure the transition looks smooth

### Not Sure What Breakpoints to Use

Start with Divi's defaults (Phone, Tablet, Desktop) and only customize if you have a specific need. Most sites don't need more than 5 breakpoints.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 breakpoint customization exclusively. Divi 4 uses a different responsive approach.

## Related

- [Responsive Editor in Divi 5 Visual Builder](../builder/responsive-editor-in-divi-5-visual-builder.md)
- [How to Create a Responsive Layout](../builder/responsive-editor-in-divi-5-visual-builder.md)
- [Visual Builder Overview](../builder/visual-builder.md)
