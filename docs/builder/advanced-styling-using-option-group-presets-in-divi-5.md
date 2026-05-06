---
title: "Advanced Styling using Option Group Presets in Divi 5"
category: builder
tags: ["builder", "presets", "design-system", "options-groups", "styling"]
related: ["composable-settings-in-divi-5.md", "element-presets.md", "global-variables-in-divi-5.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/13349301-advanced-styling-using-option-group-presets-in-divi-5"
---

# Advanced Styling using Option Group Presets in Divi 5

Create reusable design patterns using Option Group Presets to maintain consistency and speed up your design workflow.

## Overview

Option Group Presets are one of Divi 5's most powerful features for building and maintaining a design system. Instead of manually configuring the same spacing, typography, shadow, or button style on every element, you create presets once and apply them across your site. These presets can be stacked—combining multiple presets on a single element for context-specific variations—and marked as defaults so new elements start with the correct styling automatically.

This approach dramatically reduces design inconsistencies, speeds up page building, and makes global style updates effortless. When you update a preset, all elements using that preset automatically reflect the changes.

![Option Group Presets Interface](../assets/screenshots/builder/advanced-styling-using-option-group-presets-in-divi-5/overview.png){ loading=lazy }
*Option Group Presets allow you to create and manage reusable style configurations across your entire site.*

## Creating Option Group Presets

### Create a Preset from Current Styles

The fastest way to create a preset is to style an element exactly how you want it, then save that styling as a preset:

1. Open any page in the Divi Visual Builder
2. Select a module or element and go to the **Design Tab**
3. Locate the option group you want to save as a preset (e.g., Border, Button, Title Text, Spacing, etc.)
4. Adjust all the options in that group to match your desired style
5. Click the **Preset icon** (located next to the option group's title)
6. Select **New Preset From Current Styles**
7. Enter a descriptive name (e.g., "Card Shadow / Soft" or "Button / Primary")
8. Click **Save Preset**

The preset is now saved and available throughout your site.

### Create a Preset from Scratch

1. Open the **Design Tab** of any element
2. Find the option group you want to create a preset for (e.g., Typography, Buttons, Spacing)
3. Click the **Preset icon** next to the group title
4. Select **New Preset**
5. Configure all options in that group to your specifications
6. Click **Save Preset** and enter a name

### Organize Presets

When creating or editing a preset, you can:

1. Give it a **clear, descriptive name** that indicates what it does (e.g., "Card / Shadow / Soft", "Heading / H1 / Large")
2. Optionally add a **category** or **tag** to organize related presets
3. Include the **context or variant** in the name to avoid confusion (e.g., "CTA Button / Hero Section" vs. "CTA Button / Compact")

## Editing and Managing Presets

### Edit an Existing Preset

1. While styling an element, click the **Preset icon** next to an option group
2. Hover over a preset in the list and click the **gear icon** to edit it
3. Choose one of these options:
   - **Update Preset** - Update the preset with any changes you've made on the current element
   - **Update preset from current static styles** - Pull in overrides you made on one element
   - **Duplicate** - Create a copy as a starting point for a variation
   - **Delete** - Remove the preset (this doesn't affect elements already using it)
   - **Set as Default** - Make this preset the automatic choice for new elements using this option group

### Set a Default Preset

1. Click the **Preset icon** next to an option group
2. Find the preset you want to set as default
3. Click the **gear icon** and select **Set as Default**

Now whenever you add a new element to your site, this preset will be automatically applied to that option group.

## Common Preset Categories

### Typography

Create presets for consistent text styling across your site:
- **Presets for H1 - H6** headings in various sizes
- **Body text** presets (normal, large, small)
- **Small labels** and metadata text presets

**Example names:**
- "Heading / H1 / Bold"
- "Body / Regular / Large"
- "Label / Small / Gray"

### Buttons

Create shared button presets and apply them across multiple modules:
- Primary action buttons (CTAs, submit buttons)
- Secondary action buttons (back, cancel)
- Link-style buttons

**Example names:**
- "Button / CTA / Blue"
- "Button / Secondary / Outline"
- "Button / Link / Underline"

### Spacing

Create spacing presets for cards, sections, rows:
- **Padding** presets like "Spacing / Card / Large" or "Spacing / Section / Medium"
- **Margin** presets for consistent gutters between elements
- **Gap** presets for row and grid spacing

**Example names:**
- "Spacing / Card / Medium"
- "Spacing / Section / Large"
- "Spacing / Padding / Compact"

### Borders & Shadows

Create presets for consistent visual depth:
- **Card outlines** with subtle borders
- **Soft shadows** for depth without drama
- **Hover shadows** for interactive elements
- **Dark mode borders** for contrast in dark sections

**Example names:**
- "Border / Card / Light Gray"
- "Shadow / Soft"
- "Shadow / Hover / Medium"

### Effects & Motion

Create presets for scroll effects, transforms, and conditions:
- **Scroll effects** used in multiple places
- **Transforms** (scale, rotate, skew)
- **Visibility conditions** for responsive behavior

**Example names:**
- "Effect / Fade In / Scroll"
- "Transform / Scale / Hover"

## Using Presets Effectively

### Apply a Single Preset

1. Select an element in the Visual Builder
2. Go to the **Design Tab**
3. Find the option group you want to style (e.g., Button, Border, Spacing)
4. Click the **Preset icon**
5. Select the preset you want from the list
6. The preset styling is applied immediately

### Stack Multiple Presets

You can combine multiple presets on a single element for complex styling:

1. Apply the **base preset** (e.g., "Spacing / Card / Medium")
2. Click the preset icon again and add an additional preset for a specific context (e.g., "Spacing / Card / Medium / Compact")
3. The presets are layered, with later selections adding to or overriding earlier ones

Stacking is useful for variations like:
- "Button / CTA / Primary" + "Button / CTA / Hero Section" (larger, bold version)
- "Card / Shadow / Soft" + "Card / Shadow / Dark Mode" (adjusted colors)

### Override Individual Options

Even when a preset is applied, you can override individual options:

1. Select the preset as the base
2. Adjust specific options (e.g., change just the padding while keeping the shadow)
3. Your overrides remain in place, but the other preset options are maintained

If you later update the preset, your manual overrides are preserved.

## Best Practices for Option Group Presets

### Keep presets focused

Each Option Group Preset should do one job well. Create "Card Shadow / Soft" rather than a "Card Everything" preset that includes shadow, border, padding, and background all at once. This makes presets reusable across different contexts.

### Create them early

As soon as you see a style repeated more than once, turn it into a preset instead of copying settings manually. This saves time and prevents inconsistencies from manual duplication.

### Use defaults for base styles

Make your core typography, button, and background presets the defaults so new elements start in the right place. This eliminates the need to manually apply the same preset to every new element.

### Use stacking for context, not basics

Let nested presets and defaults handle the foundations. Use stacked presets for context-specific tweaks like "hero version", "compact version", or "dark section"—not for basic styling.

### Name presets for their purpose

Use clear, hierarchical names like "Button / Primary / Large" or "Spacing / Section / Wide". This makes presets immediately understandable when browsing the preset list.

### Review and consolidate regularly

Periodically review your preset library to identify duplicates, unused presets, or opportunities to generalize. A lean, well-organized preset system is easier to maintain and update.

## Advanced Workflows

### Create a Design System

Use Option Group Presets as the foundation of a complete design system:

1. Define your color palette using Global Variables
2. Create typography presets for all heading and body text styles
3. Build button presets for all CTAs and interactions
4. Design spacing presets for common layouts
5. Create shadow and border presets for visual depth
6. Document your system in a design guide or README

Now when you build pages, you select presets from this system instead of making ad-hoc styling decisions.

### Update Styles Site-Wide

One of the biggest advantages of Option Group Presets:

1. Update a preset (e.g., change "Button / CTA / Blue" from #0066CC to #0088FF)
2. All elements using that preset automatically update
3. Your entire site reflects the new styling without manual page edits

### Maintain Brand Consistency

As your site grows, presets ensure consistency:
- All buttons that are marked as presets (not Option Group Presets) all come from Option Group Presets
- All section spacing follows preset patterns
- All typography matches your brand guidelines

If you ever need to adjust your brand (new colors, new typeface), you update your presets and the changes cascade everywhere.

## Troubleshooting

**Preset doesn't apply or appears to be ignored:**
- Verify the preset icon is next to the option group (not all options groups support presets)
- Confirm you clicked on the correct preset in the dropdown
- Check if manual overrides are conflicting with the preset (try clearing manual settings first)

**Changes to a preset aren't appearing site-wide:**
- Clear your WordPress object cache if using a caching plugin
- Verify you updated the preset itself (in the Design Tab), not just the current element
- Check that elements actually have the preset applied (look at the preset dropdown)
- Refresh the front end to clear browser cache

**Can't find a preset in the dropdown:**
- Search for the preset using the search field in the dropdown
- Verify the preset was saved successfully (look for a success notification)
- Check that you're looking in the correct option group (presets are organized by group)
- If the preset was recently deleted, it may not be available

**Default preset isn't applying to new elements:**
- Confirm the preset was marked as default (check the gear icon)
- If you've set defaults for multiple presets in the same group, the last one set takes precedence
- Try clearing your browser cache
- Verify the new element is of the correct type (presets apply to specific option groups)

## Version Notes

!!! note "Divi 5 Only"
    Option Group Presets are a Divi 5 feature. This page documents Divi 5 behavior exclusively. Earlier Divi versions have limited or no preset functionality.

## Related

- [Composable Settings in Divi 5](composable-settings-in-divi-5.md)
- [Element Presets](element-presets.md)
- [Global Variables in Divi 5](global-variables.md)
- [Design System Basics](setting-up-the-basic-website-design-system.md)
