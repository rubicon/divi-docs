---
title: "Page Manager"
category: builder
tags: ["builder", "pages", "workflow", "management", "navigation"]
related: ["layers-view", "visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/13557470"
---

# Page Manager

Create, duplicate, delete, and switch between pages without leaving the Visual Builder.

## Overview

The Page Manager turns the Divi 5 Visual Builder into a lightweight site management workspace. Instead of exiting the builder, navigating to the WordPress Pages screen, and relaunching the builder on a different page, you can perform all of those actions from a single panel inside the editor.

This is especially useful when working on small sites, landing-page funnels, or any project where you frequently move between a handful of related pages. The Page Manager eliminates the exit-navigate-relaunch cycle and keeps you in the design environment.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13557470).

## Core Capabilities

| Action | Description | Benefit |
|--------|-------------|---------|
| Create page | Add a new blank page from inside the builder | Start new pages without visiting the WordPress dashboard |
| Duplicate page | Clone an existing page as a starting point | Quickly scaffold pages that share a common layout |
| Delete page | Remove pages you no longer need | Keep the site tidy without switching interfaces |
| Open page | Switch to a different page for editing | Seamlessly move between pages in one session |

## Workflow Comparison

### Without Page Manager

1. Exit the Visual Builder.
2. Navigate to the WordPress Pages screen.
3. Locate or create the target page.
4. Launch the Visual Builder on that page.

### With Page Manager

1. Open the Page Manager panel inside the Visual Builder.
2. Select the desired action (create, duplicate, delete, or open).
3. Continue editing without any interface transitions.

## When to Use the Page Manager

| Scenario | Why It Helps |
|----------|-------------|
| Building a multi-page site from scratch | Create all pages in sequence without leaving the builder |
| Designing a sales funnel | Duplicate the base page, then customize each step |
| Cleaning up unused pages | Delete directly instead of switching to the dashboard |
| Editing related pages in a session | Open each page in turn to maintain design consistency |

## Tips and Best Practices

- **Use duplication for templated pages.** If several pages share a layout (e.g., service pages), build one and duplicate it rather than starting from scratch each time.
- **Save before switching pages.** Unsaved changes on the current page may be lost when you open a different page.
- **Combine with the Divi Library.** For reusable sections that appear on many pages, save them to the Library rather than duplicating entire pages.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If the Page Manager is not visible, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.

- **Duplicated page is missing content.** Ensure the source page was fully saved before duplicating. Draft or autosave content may not carry over.
- **Cannot delete a page.** WordPress may prevent deletion of the page set as the static front page or posts page. Change those assignments in Settings > Reading first.

## Related

- [Layers View](layers-view.md)
- [Visual Builder](visual-builder.md)
