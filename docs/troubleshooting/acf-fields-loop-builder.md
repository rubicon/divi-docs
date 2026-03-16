---
title: "Display ACF Fields in Loop Builder"
category: troubleshooting
tags: ["troubleshooting", "acf", "loop-builder", "dynamic-content", "custom-fields"]
related: ["loop-builder", "dynamic-content"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11930145"
---

# Display ACF Fields in Loop Builder

Use Advanced Custom Fields (ACF) data inside Divi 5's Loop Builder to create dynamic layouts powered by custom field values.

## Overview

Divi 5's Loop Builder has native support for ACF fields. When you enable looping on a module, any ACF fields associated with the queried post type appear automatically in the Dynamic Content dropdown. No extra plugins or custom code are required beyond ACF itself.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11930145).

## Prerequisites

- **Advanced Custom Fields** plugin installed and activated.
- At least one ACF field group assigned to a post type.
- Posts with populated ACF field values.

## Step-by-Step Guide

### 1. Enable Looping on a Module

Select the module where you want to display ACF data (e.g., a Text module). In its settings, activate the **Loop Element** toggle.

### 2. Open Dynamic Content

Click the **Dynamic Content** icon on the module field you want to populate (body text, title, etc.).

### 3. Select the Custom Field Source

From the Dynamic Content options, choose **Loop Post Custom Field**.

### 4. Pick Your ACF Field

Click the **Select Custom Field** dropdown. ACF fields appear at the top of the list, labeled with their field names. Select the one you need.

### 5. Apply the Selection

Click **Apply** to confirm. The module will now dynamically display the ACF field value for each post in the loop.

## Key Details

| Detail | Notes |
|--------|-------|
| **Field discovery** | ACF fields auto-populate in the dropdown -- no manual entry needed |
| **Sort order** | ACF fields appear first in the custom field list |
| **Compatible fields** | Body text and title fields on looped modules |
| **Field type matching** | Divi matches field types to compatible module fields (e.g., image fields work on Image modules, not Text modules) |

## Related

- [Loop Builder](../builder/loop-builder.md)
- [Dynamic Content](../builder/dynamic-content.md)
- [ACF Repeater Fields in Loop Builder](acf-repeater-loop-builder.md)
