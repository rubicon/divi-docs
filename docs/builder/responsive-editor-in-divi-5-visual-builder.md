---
title: "Responsive Editor in Divi 5 Visual Builder"
category: builder
tags: ["builder", "responsive", "breakpoints", "device", "tablet", "phone", "desktop", "editor"]
related: ["customizable-breakpoints-in-divi-5.md", "understanding-flex-layout-direction-in-divi-5.md"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/13002269-responsive-editor-in-divi-5-visual-builder"
---

# Responsive Editor in Divi 5 Visual Builder

The Responsive Editor in Divi 5 allows you to set device-specific values for individual settings without leaving the Visual Builder, making it easy to create truly responsive designs by adjusting layout, spacing, sizing, and other properties for Desktop, Tablet, and Phone breakpoints.

## Overview

Creating responsive designs in Divi 5 is faster than ever thanks to the integrated Responsive Editor. Instead of switching between desktop, tablet, and phone views and hunting for settings, you can now set device-specific overrides right from the Design or Content tab of any element.

The Responsive Editor is accessible via a small icon button next to most settings. When you open it, you'll see sliders or input fields for each breakpoint (Desktop, Tablet, Phone), allowing you to fine-tune values without affecting other devices. Changes are applied in real-time and you can preview them instantly by switching the builder's device view.

This workflow dramatically reduces the number of clicks needed to build a fully responsive site.

![Responsive Editor Overview](../assets/screenshots/builder/responsive-editor/overview.png){ loading=lazy }
*The Responsive Editor panel open, showing device-specific settings for text size.*

## How to Access

### From Any Setting

1. Locate any setting in the **Design** or **Content** tab (e.g., font size, padding, text color)
2. Look for the **Responsive Editor icon** (a small device/screen icon) next to that setting
3. Click the icon to open the Responsive Editor panel for that setting
4. Adjust values for Desktop, Tablet, and Phone as needed
5. Click the **X** or close button to return to the main editor
6. Save your changes in the Visual Builder

### Visual Indicator

The Responsive Editor icon **turns blue** when that setting has different values for one or more devices or states. This makes it easy to see which settings have responsive overrides at a glance.

## Using the Responsive Editor

### Text & Font Size

Text size is one of the most common responsive adjustments:

1. Select the element (Heading, Text Module, etc.)
2. Go to **Design** tab → find the **Text Size** or **Heading Size** option
3. Click the **Responsive Editor icon** next to the size setting
4. In the Responsive Editor panel:
   - **Desktop**: Set a comfortable, readable size (e.g., 48px for a large heading)
   - **Tablet**: Reduce the size so the heading fits nicely on the smaller screen (e.g., 36px)
   - **Phone**: Reduce it again so it stays readable without excessive wrapping (e.g., 28px)
5. Close the panel and save

### Padding & Margin

Spacing is equally important for responsive design:

1. Select the element
2. Go to **Design** tab → find the **Padding** or **Margin** option
3. Click the **Responsive Editor icon**
4. In the panel:
   - **Desktop**: Set comfortable spacing (e.g., 40px top/bottom, 60px left/right)
   - **Tablet**: Reduce padding slightly (e.g., 30px, 40px)
   - **Phone**: Minimize padding to maximize content area (e.g., 20px, 25px)
5. Close and save

### Gap (Space Between Items)

For rows or containers with multiple items (flex layout):

1. Select the Row or Section
2. Go to **Design** tab → **Layout** group → find **Gap** or **Item Spacing**
3. Click the **Responsive Editor icon**
4. Set values per device to control space between child items

![Responsive Editor Panel](../assets/screenshots/builder/responsive-editor/panel.png){ loading=lazy }
*Responsive Editor showing device-specific controls for padding, margin, and gap settings.*

## Common Responsive Patterns

| Setting | Desktop | Tablet | Phone |
|---------|---------|--------|-------|
| **Heading Size** | 48px | 36px | 28px |
| **Body Text Size** | 16px | 15px | 14px |
| **Section Padding** | 80px top/bottom | 50px | 30px |
| **Column Gap** | 40px | 30px | 15px |
| **Button Padding** | 15px 30px | 12px 25px | 10px 20px |

## Settings That Support Responsive Editor

Most settings in the Design tab support the Responsive Editor, including:

- Text sizes (heading, body, label)
- Padding and margin
- Gap (spacing between flex items)
- Font weight, line height
- Border radius
- Shadow blur and offset
- Column width (Column Class)
- Display properties
- Order (flex item order)

### Settings Without Responsive Editor

Some settings don't have responsive overrides (e.g., color, font family, background image). These are inherited per breakpoint or apply globally. If you need to change colors per device, adjust them using custom CSS or a child theme.

## Workflow Tips

1. **Start with Desktop**  
   Set your baseline values for desktop first. Then refine for smaller screens.

2. **Use the Device Preview**  
   After setting responsive values, switch the Visual Builder's device view (top toolbar: Desktop → Tablet → Phone) to preview your changes in real-time.

3. **Work Top-to-Bottom**  
   Open the Responsive Editor for one setting, set all device values, close it, and move to the next setting. This is faster than opening/closing repeatedly.

4. **Test on Real Devices**  
   The Visual Builder preview is close, but testing on an actual phone or tablet tablet catches subtle issues (font rendering, touch target size, etc.).

5. **Use Customizable Breakpoints**  
   If your site has custom breakpoints (not just Desktop/Tablet/Phone), the Responsive Editor adapts to show those breakpoints. See [Customizable Breakpoints in Divi 5](customize-the-divi-5-s-default-breakpoints.md) for setup.

## Troubleshooting

!!! warning "Responsive Editor icon is missing for a setting"
    Not all settings support the Responsive Editor. If an icon isn't present, that setting either applies globally or can only be adjusted via the device view selector at the top of the builder. Try switching to a different device view from the top toolbar and adjusting the setting there.

!!! warning "Changes don't apply to Tablet or Phone"
    1. Verify your values in the Responsive Editor (don't leave fields blank if you want to override)
    2. Save your page changes
    3. Clear your browser cache
    4. Refresh the page and check again in the builder preview

!!! note "Responsive values override global settings"
    If you set a global value (e.g., 16px font size) and then override it per device in the Responsive Editor, the device-specific values take precedence. To remove a device override, clear the value in the Responsive Editor and the global setting will apply again.

!!! tip "Copy values between devices"
    If you want to use the same value for Tablet as Desktop, copy the Desktop value, then paste it into the Tablet field in the Responsive Editor. (This varies slightly by setting, but most support this workflow.)

## Version Notes

!!! note "Divi 5 Only"
    The Responsive Editor interface is new in Divi 5. Divi 4 required switching device views to adjust responsive values, which was slower and more cumbersome.

## Related

- [Customizable Breakpoints in Divi 5](customize-the-divi-5-s-default-breakpoints.md)
- [Understanding Flex Layout Direction in Divi 5](understanding-flex-layout-direction-in-divi-5.md)
- [Mobile-First Design with Divi 5](responsive-editor-in-divi-5-visual-builder.md)
