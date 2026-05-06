---
title: "How to Convert a Global Element to a Non-Global Element in Divi 5"
category: troubleshooting
tags: ["troubleshooting", "global-elements", "presets", "library", "element-management"]
related: ["advanced-styling-using-option-group-presets-in-divi-5", "divi-library-in-divi-5", "import-library-elements"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14430506-how-to-convert-a-global-element-to-a-non-global-element-in-divi-5"
---

# How to Convert a Global Element to a Non-Global Element in Divi 5

Convert a global element back to a standard, independent element that doesn't sync changes across all instances.

## Overview

In Divi 5, global elements are saved to your library and any changes made to the global element update automatically across all pages where it's used. However, there are times when you may want to convert a global element back to a regular (non-global) element—for example, if you need to customize it for a specific page without affecting all other instances.

This process is simple: you remove the global element's connection to the library while keeping the element itself intact on your page.

## Steps

1. **Navigate to the page** containing the global element you want to convert to a regular element.

2. **Locate the global element** on the canvas. Global elements typically display with a special indicator (badge or icon) showing they are linked to the library.

3. **Right-click on the global element** to open the context menu.

4. **Select "Disable Global"** from the menu options.

5. **Confirm the action** if prompted. The element will immediately convert to a regular, non-global element. Any previous changes or updates from the global version will remain on the page, but future edits will only affect this instance.

### Alternative Method (Using Three-Dot Menu)

If right-click context menu is unavailable:

1. Select the global element.
2. Click the **three-dot menu icon** (⋯) in the element's toolbar or options panel.
3. Choose **Disable Global** from the dropdown menu.
4. The element converts to a regular element.

## Converting Back to Global

If you later want to make this element global again:

1. Right-click on the non-global element.
2. Choose **Save To Library**.
3. In the save modal that appears, check the **"Save as Global"** option.
4. Click the **"Add to Library"** button.
5. The element becomes global again and will be available for use across your site.

## Troubleshooting

!!! warning "Check for dependent pages before converting"
    If you disable global on an element that's used across multiple pages, remember that those other instances will no longer receive updates. Make sure you're converting the correct element and that you understand the impact on your other pages.

!!! warning "Changes are kept, not reverted"
    Converting a global element to non-global keeps all the styling and content from the current version. Any custom edits made to *this specific instance* before conversion will remain. Only future edits will be isolated to this page.

!!! warning "Cannot convert back automatically"
    Once you disable global, the element is no longer connected to the library version. If other pages still have the global version, those will continue to update independently. You'll need to manually "Save to Library" as a global to reconnect them, which creates a new library entry.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Related

- [Option Group Presets](../builder/advanced-styling-using-option-group-presets-in-divi-5.md)
- [Divi Library in Divi 5](../builder/divi-library-in-divi-5.md)
- [Import Library Elements](import-library-elements.md)
