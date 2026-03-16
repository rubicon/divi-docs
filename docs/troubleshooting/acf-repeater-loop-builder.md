---
title: "ACF Repeater Fields in Loop Builder"
category: troubleshooting
tags: ["troubleshooting", "acf", "repeater-fields", "loop-builder"]
related: ["loop-builder", "dynamic-content"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11930200"
---

# ACF Repeater Fields in Loop Builder

Display ACF repeater field data dynamically in Divi 5 using the Loop Builder's built-in repeater query type.

## Overview

ACF repeater fields store multiple rows of sub-field data within a single post. Divi 5's Loop Builder natively supports repeater fields through a dedicated query type, so you can loop through repeater rows just like you would loop through posts.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11930200).

## Prerequisites

- **Advanced Custom Fields Pro** installed (repeater fields require the Pro version).
- A repeater field group configured and assigned to a post type.
- Posts with populated repeater field data.

## Step-by-Step Guide

### 1. Enable Loop Element

Select the module that will display your repeater data. Activate the **Loop Element** toggle in its settings.

### 2. Set the Query Type

In the Loop Element settings, open the **Query Type** dropdown and select **ACF Repeater: [Your Repeater Field Name]**.

### 3. Map Content with Dynamic Content

Click the **Dynamic Content** icon on the module field you want to populate (body, title, image, etc.).

### 4. Choose the Subfield

From the Dynamic Content options, select the specific repeater subfield to display.

### 5. Apply Changes

Click **Apply** to confirm. The module will now iterate through each row of the repeater field and display the mapped subfield values.

## Context-Aware Field Matching

Divi intelligently restricts the available subfields based on the module field type you are mapping to:

- **Text-based module fields** only show text-compatible ACF subfields.
- **Image module fields** show image-type ACF subfields.
- Incompatible combinations (e.g., mapping an ACF image field to a text input) are filtered out automatically.

## Related

- [Loop Builder](../builder/loop-builder.md)
- [Dynamic Content](../builder/dynamic-content.md)
- [ACF Fields in Loop Builder](acf-fields-loop-builder.md)
