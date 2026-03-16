---
title: "Custom Blog Feed with Loop Builder"
category: troubleshooting
tags: ["troubleshooting", "loop-builder", "blog", "custom-query"]
related: ["loop-builder", "blog", "dynamic-content"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/11904025"
---

# Custom Blog Feed with Loop Builder

Build a custom blog feed layout in Divi 5 using the Loop Builder to dynamically display posts with featured images, titles, dates, and excerpts.

## Overview

The default Blog module works well for standard layouts, but when you need a custom design -- such as a featured post alongside a grid of secondary posts -- the Loop Builder gives you full control over how post data is displayed. This guide walks through creating a two-column blog feed with a highlighted featured post.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11904025).

## Step 1: Create the Section

1. Add a new **Section** to your page.
2. Set the background color to a light gray (e.g., `#EFEFEF`) to visually separate the blog feed from other content.

## Step 2: Add a Title Row

1. Add a **single-column Row** inside the section.
2. Insert a **Heading** or **Text** module with your blog feed title (e.g., "Latest Posts").

## Step 3: Build the Content Row

1. Add a second Row using the **offset column layout** (the 9th layout option, which gives you a narrow left column and a wider right column).
2. The left column will hold the featured post; the right column will hold the post grid.

## Step 4: Configure the Post Grid (Right Column)

1. Select the wider (right) column.
2. Enable the **Loop Element** toggle.
3. Set **Posts Per Page** to `9`.
4. Set **Post Offset** to `1` so the featured post is not repeated.
5. Enable **Text Wrap** on the row to arrange posts in a grid.

## Step 5: Add Dynamic Content to the Grid

1. Add a **Group** module inside the right column.
2. Inside the Group, add an **Image** module and link it to **Loop Featured Image** via Dynamic Content.
3. Add **Text** modules for the post date, title, and excerpt, each connected to their respective Dynamic Content fields.

## Step 6: Configure the Featured Post (Left Column)

1. Select the left column.
2. Enable the **Loop Element** toggle.
3. Set **Posts Per Page** to `1` (only the most recent post).
4. Add the same Dynamic Content modules (image, title, date, excerpt) but style them larger to emphasize the featured post.

## Step 7: Style the Layout

- Apply padding (e.g., `15px`) and border radius (e.g., `15px`) to each post card for a clean appearance.
- Set background colors on the Group modules to distinguish cards from the section background.
- Adjust typography and spacing to match your site design.

## Tips

- The **Post Offset** setting on the grid row is what prevents the featured post from appearing twice.
- You can adjust the number of posts per page and the column layout to suit your design needs.
- Consider adding pagination if you have a large number of posts.

## Related

- [Loop Builder](../builder/loop-builder.md)
- [Blog Module](../modules/blog.md)
- [Dynamic Content](../builder/dynamic-content.md)
- [Group Module](../modules/group.md)
