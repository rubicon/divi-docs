---
title: "How to Fix the Dropdown Menu That's Cut Off or Hidden Behind Page Content in Divi 5"
category: troubleshooting
tags: [troubleshooting]
related: []
divi_version: "5.x"
last_updated: 2026-06-01
source_url: "https://help.elegantthemes.com/en/articles/15324394-how-to-fix-the-dropdown-menu-that-s-cut-off-or-hidden-behind-page-content-in-divi-5"
---

# How to Fix the Dropdown Menu That's Cut Off or Hidden Behind Page Content in Divi 5

<!-- AUTO-CREATED: 2026-06-01 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/15324394-how-to-fix-the-dropdown-menu-that-s-cut-off-or-hidden-behind-page-content-in-divi-5).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| The dropdown opens but gets cut off at an edge. |  | You can see the top items but the rest is sliced off where the header ends. This is an overflow clipping problem. |
| The dropdown opens but is partially or fully invisible. |  | You can sometimes see text from the page bleeding through the menu, or the dropdown doesn't appear at all. This is a z-index stacking problem. |
| Theme Builder |  | der template in theTheme Builder, or open the page in theVisual Builder. |
| Section |  | heSectionthat contains your Menu module. |
| Advanced |  | eAdvancedtab. |
| Visibility |  | sibilityoption group. |
| Horizontal Overflow |  | lowandVertical OverflowtoVisible. |
| Row |  | eat the same check on the parentRowandColumnif the dropdown is still clipped. |

### Content Tab

| Setting | Type | Description |
|---------|------|-------------|
| Section |  | heSectionthat contains your Menu module. |
| Advanced |  | eAdvancedtab. |
| Position |  | Positionoption group. |
| Z-index |  | dexto a high number like100,999, or9999. |
| Section |  | he firstSectionbelow your header. |
| Advanced |  | eAdvancedtab. |
| Scroll Effects |  | Effectsoption group. |
| Sticky Position |  | onis set, or if anyScroll Transform Effectsare active, the dropdown will likely stack behind them. |
| Position |  | isable the effect, or open the section'sPositionoption group and setZ-indexto0so the header's higher z-index wins. |
| Divi → Theme Options → Clear CSS Cache |  | heme Options → Clear CSS Cachein the top right, then reload in an incognito window. |
| Safe Mode |  | e ModeunderDivi → Support Centerto rule out a plugin or custom code conflict. |
| Divi → Theme Options → General → Custom CSS |  | m CSSfor rules that setoverflow: hiddenon.et-l-header,.et_pb_menu, or any related selectors. These will clip the dropdown regardless of your Visibility settings. |

## Code Examples

<!-- TODO: Add CSS/PHP code examples -->

## Common Patterns

<!-- TODO: Document 2-3 common usage patterns -->

## Troubleshooting

<!-- TODO: Document common issues and solutions -->

## AI Interaction Notes

| Task | Confidence | Notes |
|------|-----------|-------|
| Basic placement | 🔬 Needs Testing | Untested — stub page |
| Settings configuration | 🔬 Needs Testing | Untested — stub page |
| Custom styling | 🔬 Needs Testing | Untested — stub page |

## Related

<!-- TODO: Add links to related documentation pages -->
