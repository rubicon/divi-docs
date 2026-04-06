---
title: "Understanding Divi's New Flexbox Layout"
category: builder
tags: [builder]
related: []
divi_version: "5.x"
last_updated: 2026-04-06
source_url: "https://help.elegantthemes.com/en/articles/11754241-understanding-divi-s-new-flexbox-layout"
---

# Understanding Divi's New Flexbox Layout

<!-- AUTO-CREATED: 2026-04-06 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11754241-understanding-divi-s-new-flexbox-layout).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Default for New Containers |  | Flexlayout is now the default setting for all new elements. |
| Legacy Divi 4 Elements |  | Existing elements on your pages continue to use theBlocklayout |
| Switching Layouts |  | You can switch betweenFlexandBlocklayouts at any time. |
| Full Width and Specialty Sections |  | These remain supported in Divi 4 layouts and migrated layouts, but can no longer be added through theAdd Sectionpanel. If your layout already includes Fullwidth or Specialty Sections, they’ll continue to work normally, and you can still edit them. |
| Horizontal Gap |  | (column-gap): Controls the horizontal spacing between elements. |
| Vertical Gap |  | (row-gap): Controls the vertical spacing between elements. |
| Layout Direction |  | (flex-direction): Defines how items flow inside the container:Row: Left to rightRow Reverse: Right to leftColumn: Top to bottomColumn Reverse: Bottom to top |
| Row |  | Left to right |
| Row Reverse |  | Right to left |
| Column |  | Top to bottom |
| Column Reverse |  | Bottom to top |
| Justify Content |  | (justify-content):Note: This setting only affects layouts where a customheight,min-height, ormax-heightis defined.​Start: Aligns items to the left or top edge.Center: Aligns items to the center.End: Aligns items to the right or bottom edge.Space between: Aligns the first item to the left/top and the last item to the right/bottom, with equal space between all items.Space Around: Adds equal space around each item - outer margins are half the size of inner gaps.Space Evenly: Keeps spacing uniform between and around all items. |
| Start |  | Aligns items to the left or top edge. |
| Center |  | Aligns items to the center. |
| End |  | Aligns items to the right or bottom edge. |
| Space between |  | Aligns the first item to the left/top and the last item to the right/bottom, with equal space between all items. |
| Space Around |  | Adds equal space around each item - outer margins are half the size of inner gaps. |
| Space Evenly |  | Keeps spacing uniform between and around all items. |
| Align Item |  | s (align-items):Start: Aligns items to the left or top edge.Center: Aligns items to the center.End: Aligns items to the right or bottom edge.Stretch: Expands items to fill the width or height of the container. |
| Start |  | Aligns items to the left or top edge. |
| Center |  | Aligns items to the center. |
| End |  | Aligns items to the right or bottom edge. |
| Stretch |  | Expands items to fill the width or height of the container. |
| Layout Wrapping |  | (flex-wrap):No Wrap(default): Items stay on one line and do not wrap.Wrap: Moves items to the following line if the container isn’t wide enough.Wrap Revers: Moves items to the following line in reverse order if space runs out. |
| No Wrap(default) |  | Items stay on one line and do not wrap. |
| Wrap |  | Moves items to the following line if the container isn’t wide enough. |
| Wrap Revers |  | Moves items to the following line in reverse order if space runs out. |
| Wrapping Alignment |  | (align-content) - Only visible whenLayout Wrappingis enabled.Stretch: Expands items equally along the cross-axis to fill the container space while respecting any max-width or max-height limits.Start: Packs items tightly against the start edge of the container.Center: Centers all items along the cross-axis.End: Packs items at the end of the container along the cross axis.Space Between: Evenly distributes items along the cross axis. The first aligns to the start, and the last aligns to the end.Space Around: Adds equal space around each item; outer margins are half the size of the inner gaps.Space Evenly: Keeps equal spacing between items and container edges. |
| Stretch |  | Expands items equally along the cross-axis to fill the container space while respecting any max-width or max-height limits. |
| Start |  | Packs items tightly against the start edge of the container. |
| Center |  | Centers all items along the cross-axis. |
| End |  | Packs items at the end of the container along the cross axis. |
| Space Between |  | Evenly distributes items along the cross axis. The first aligns to the start, and the last aligns to the end. |
| Space Around |  | Adds equal space around each item; outer margins are half the size of the inner gaps. |
| Space Evenly |  | Keeps equal spacing between items and container edges. |
| + Add New Column |  | w Columnin the row settings adds an empty column with the same width class as the last column. |
| Clone |  | ingCloneon an existing column duplicates it, keeping all settings and contained modules. |
| Dragging Rows |  | When you drag a row into a Flex Section, its default top and bottom padding is automatically removed. |
| Dragging Columns |  | Moving a column from a Flex Row to a Block Row creates equal-width columns and removes the Flex class.Moving a column from a Block Row to a Flex Row assigns it the sameColumn Classas the column before it. |
| Column Class |  | umn from a Block Row to a Flex Row assigns it the sameColumn Classas the column before it. |
| Dragging Modules |  | When you drag modules into Flex Rows, their default bottom margin is automatically removed. |
| Block to Flex |  | When converting from Block to Flex, Divi minimizes visual changes by applying defaultHorizontal Column Spacinginstead of converting gutter width. Block classes map to new Flex classes (for example,1/2Block →1/2Flex). If you use custom CSS targeting Block classes, visual differences may occur. |
| Flex to Block |  | When converting from Flex to Block, all columns reset to equal width, similar to how Block layouts handle added or removed columns. If a Flex Row contains more than six columns, any modules in columns beyond the sixth are moved into the sixth column. Nested Rows remain nested. |

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
