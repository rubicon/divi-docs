---
title: "Build Custom Loops using Loop Builder in Divi 5"
category: builder
tags: [builder]
related: []
divi_version: "5.x"
last_updated: 2026-04-06
source_url: "https://help.elegantthemes.com/en/articles/13644757-build-custom-loops-using-loop-builder-in-divi-5"
---

# Build Custom Loops using Loop Builder in Divi 5

<!-- AUTO-CREATED: 2026-04-06 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13644757-build-custom-loops-using-loop-builder-in-divi-5).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Loop Container |  | the element you turn into a loop (Section, Row, Column, Group, or specific modules). Divi repeats this element for every item in the query. |
| Loop Item Template |  | the layout inside that container (image, title, meta, button, etc.). This is the design that gets repeated. |
| Loop Query |  | the rules that define which items show in the loop (post type, category, order, item count, meta query, etc.). |
| Dynamic Content |  | special "Loop" fields like Loop Featured Image, Loop Post Title, Loop Excerpt, Loop Product Price, etc. These pull the correct data into each repeated card. |
| Pagination Module |  | optional, used to split large loops into pages. You point it at the loop you created, so the navigation controls that specific loop. |
| Loop |  | he Content tab, find theLoopoption group. |
| Loop Element |  | op Elementoption. |

### Design Tab

| Setting | Type | Description |
|---------|------|-------------|
| Image module |  | olumn, build your post "card":Add anImage module(for the post's featured image).Add aHeading module(for the post's title).Add aText module(for author or meta).Add another Text module for the post's excerpt text.Add aButton modulefor Read More. |
| Image module |  | module(for the post's featured image). |
| Heading module |  | odule(for the post's title). |
| Text module |  | odule(for author or meta). |
| Button module |  | odulefor Read More. |
| Content |  | s settings and go to theContenttab. |
| Loop Element |  | op Elementtogglein theLoopoptions group. |
| Design tab |  | Open the Row's settings and in theDesign tabchoose:Layout Style:Layout Wrapping: Wrap |
| Layout Style |  | Layout Wrapping: Wrap |
| Design tab |  | Open the Column's settings and in theDesign tabchoose:Sizing:Column Class: 1/3 |
| Sizing |  | Column Class: 1/3 |
| Query Type |  | ypetoPost Types(default). |
| Post Type |  | t TypetoPosts(your regular blog posts). |
| Posts Per Page |  | ageto how many cards you want visible at once (for example, 6 or 9). |
| Order By |  | BytoPublish Date(default) andOrdertoDescending(default) to show newest first. |
| Post Offset |  | ffsetat 0 for now (used later to skip items for secondary loops). |
| Include Posts With Specific Term |  | g withInclude Posts With Specific Termif this loop should show only certain topics. |

### Content Tab

| Setting | Type | Description |
|---------|------|-------------|
| Featured Image |  | Edit the Image module in the card.Hover over the Image field and click theDynamic Contenticon.ChooseLoop Featured Image. |
| Dynamic Content |  | Image field and click theDynamic Contenticon. |
| Loop Featured Image |  | Image. |
| Post Title |  | Edit the Heading module.Use the Dynamic Content icon on the text field.ChooseLoop Post Title. |
| Loop Post Title |  | Title. |
| Author / Meta |  | In a Text module, click the Dynamic Content icon.ChooseLoop Author,Loop Post Date, or similar meta fields, and optionally add static text before/after ("by", separators, etc.). |
| Loop Author |  | Author,Loop Post Date, or similar meta fields, and optionally add static text before/after ("by", separators, etc.). |
| Excerpt |  | In the excerpt Text module, use Dynamic Content and chooseLoop Excerpt.Set word count and "Read more" text if needed. |
| Loop Excerpt |  | pt Text module, use Dynamic Content and chooseLoop Excerpt. |
| Button / Card Link |  | In the Button module, set the link via Dynamic Content toLoop LinkorPost URL.Optionally, set the whole loop container to use Loop Link so clicking anywhere on the card opens the post by editing the Column settings, and in the Content Tab → Module link use the Dynamic Content Icon and choose Loop Link. |
| Loop Link |  | tton module, set the link via Dynamic Content toLoop LinkorPost URL. |
| Pagination |  | Paginationmodule. |
| Content tab → Target |  | gs →Content tab → Target, choose the Column that contains the Loop. |
| outside |  | ination module must sitoutsidethe loop container. |
| Posts Per Page |  | must havePosts Per Pageset to a finite number (for example, 6); otherwise, pagination has nothing to paginate. |

### Advanced Tab

| Setting | Type | Description |
|---------|------|-------------|
| Loop only where it makes sense |  | Use a single, clear loop container (often a column or group). Keep headings, section titles, and CTAs outside the loop so they don't repeat. |
| Use Admin Labels aggressively |  | Label your loop containers and pagination clearly so you can target the correct loop, especially on templates with multiple loops. |
| Always use Dynamic Content inside loops |  | If you leave static text or images inside the loop, that same content appears on every item. Use Loop-specific fields for anything that should change per item. |
| Control performance with query options |  | Use Posts Per Page, Order By, Offset, and Meta Queries to show only what you need and to avoid loading unnecessary items. |

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
