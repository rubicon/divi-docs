---
title: "Understanding Divi's CSS Grid Layout"
category: builder
tags: [builder]
related: []
divi_version: "5.x"
last_updated: 2026-04-06
source_url: "https://help.elegantthemes.com/en/articles/12350654-understanding-divi-s-css-grid-layout"
---

# Understanding Divi's CSS Grid Layout

<!-- AUTO-CREATED: 2026-04-06 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12350654-understanding-divi-s-css-grid-layout).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Design tab → Layout |  | gn tab → Layout. |
| Layout Style dropdown |  | dropdown. |
| Grid |  | seGrid. |
| Horizontal and Vertical Gap |  | Defines the horizontal and vertical space between grid items |
| Column Width |  | Defines the size of each column inside the grid layout. |
| Number of Columns |  | Defines the total number of columns the Grid will use to display the elements. |
| Collapse Empty Columns |  | If enabled, it will eliminate empty Grid columns. |
| Grid Auto Columns |  | Define the size for implicit columns that are automatically created when grid items are placed outside the explicitly defined Grid. This controls the width of overflow columns. |
| Row Heights |  | Choose how grid rows should be sized. Auto height adjusts to content, equal height creates uniform rows, minimum height sets a baseline, and fixed height maintains consistent row dimensions. |
| Number of Rows |  | Defines the number of rows in the Grid. This determines how many horizontal rows your grid layout will have down the container height. |
| Grid Auto Rows |  | Defines the size for implicit rows that are automatically created when grid items are placed outside the explicitly defined Grid. This controls the height of overflow rows. |
| Grid Direction |  | Control the auto-placement algorithm for grid items. Choose row to fill rows first, or column to fill columns first. This determines how items automatically flow when not explicitly positioned.Row(default): fill rows firstColumn: fill columns first (this required the Number of Rows value to be set) |
| Row |  | (default): fill rows first |
| Column |  | fill columns first (this required the Number of Rows value to be set) |
| Grid Density |  | Control how grid items fill empty spaces in the Grid.Dense(default): Attempts to fill gaps with smaller itemsAuto: Maintains the natural document order |
| Dense |  | (default): Attempts to fill gaps with smaller items |
| Auto |  | Maintains the natural document order |
| Justify Content |  | Control how child elements are distributed along the main axis.Start(default): Aling the Grid items to the left edge.Center: Align the grid items to the center.End: Align the grid items to the right edge.Space Between: Distributes thegrid tracks as a groupalong theinline axis(usually left ↔ right).The first track is pushed flush against the container’s start edge (left in LTR).The last track is pushed flush against the container’s end edge (right in LTR).Any extra free space in between is divided evenly as gaps between the tracks.There’s no space at the edges — all of it goes between.Space Around: Controls how theset of grid tracks(columns, in the inline axis) is distributed inside the containerwhen there’s extra space left over.Equal space is placedaroundeach track.That means each track has an equal-sized “margin” on its left and right.Because the tracks at the edges share their outer space with the container edge, theouter gaps are half the size of the inner gaps.Space Evenly: Distributes theset of grid tracksacross the inline axis so thatall gaps - including the ones at the container edges - are exactly the same size.The leftover free space in the container is split intoN+1 gaps, whereN = number of tracks – 1(the gaps between) plus the 2 outer edges.Every single gap gets the same width.That means the spacing between tracks, and the spacing at the container’s start and end, are equal. |
| Start |  | (default): Aling the Grid items to the left edge. |
| Center |  | Align the grid items to the center. |
| End |  | Align the grid items to the right edge. |
| Space Between |  | Distributes thegrid tracks as a groupalong theinline axis(usually left ↔ right).The first track is pushed flush against the container’s start edge (left in LTR).The last track is pushed flush against the container’s end edge (right in LTR).Any extra free space in between is divided evenly as gaps between the tracks.There’s no space at the edges — all of it goes between. |
| Space Around |  | Controls how theset of grid tracks(columns, in the inline axis) is distributed inside the containerwhen there’s extra space left over.Equal space is placedaroundeach track.That means each track has an equal-sized “margin” on its left and right.Because the tracks at the edges share their outer space with the container edge, theouter gaps are half the size of the inner gaps. |
| around |  | space is placedaroundeach track. |
| outer gaps are half the size of the inner gaps |  | ter space with the container edge, theouter gaps are half the size of the inner gaps. |
| Space Evenly |  | Distributes theset of grid tracksacross the inline axis so thatall gaps - including the ones at the container edges - are exactly the same size.The leftover free space in the container is split intoN+1 gaps, whereN = number of tracks – 1(the gaps between) plus the 2 outer edges.Every single gap gets the same width.That means the spacing between tracks, and the spacing at the container’s start and end, are equal. |
| N+1 gaps |  | over free space in the container is split intoN+1 gaps, whereN = number of tracks – 1(the gaps between) plus the 2 outer edges. |
| Align Items |  | Controls howitems are positioned inside their grid cells along the block axis(usually vertical, top ↔ bottom).​​⚠︎ Note: This requires the grid container to have a height or a min height value set.Start: Aligns items to thestart edge of the cell(top in an LTR horizontal writing mode). The item’s top edge hugs the cell’s top; any extra vertical space remains below.Center: Aligns items to thecenter of the cell vertically. Equal space above and below the item, so it floats in the middle.End: Aligns items to theend edge of the cell(bottom in horizontal writing mode). The item’s bottom edge hugs the cell’s bottom; leftover space is above.Stretch(default): Makes itemsexpand to fill the whole cell height, unless the item has a fixed height. This is why grid children often look “full height” by default. |
| Start |  | Aligns items to thestart edge of the cell(top in an LTR horizontal writing mode). The item’s top edge hugs the cell’s top; any extra vertical space remains below. |
| Center |  | Aligns items to thecenter of the cell vertically. Equal space above and below the item, so it floats in the middle. |
| End |  | Aligns items to theend edge of the cell(bottom in horizontal writing mode). The item’s bottom edge hugs the cell’s bottom; leftover space is above. |
| Stretch |  | (default): Makes itemsexpand to fill the whole cell height, unless the item has a fixed height. This is why grid children often look “full height” by default. |
| Align Content |  | aligns the entire set of rows (the grid block) inside the container’s block axis (usually vertical, top to bottom). It only matters when the grid container is taller than the total Grid (rows + row gaps) or there’s leftover vertical space to distributeStretch(default): Expands row tracks proportionally to fill the container’s height. The grid block grows until it fills all available space.Start: Packs all rows at the top of the container. Free space sits below the Grid.Center: Packs the rows into the vertical middle of the container. Equal free space above and below the Grid.End: Packs all rows at the bottom of the container. Free space sits above the Grid.Space Between: Rows are spread out vertically. First row sticks to the top, last row to the bottom. Any free space is divided evenly between rows (no extra space at edges).Space Around: Equal space placed around each row. Outer edges (top/bottom) get half-sized gaps compared to the middle gaps.Space Evenly: Free space is divided into equal gaps everywhere, including the edges. Top, bottom, and the spaces between rows are identical. |
| Stretch |  | (default): Expands row tracks proportionally to fill the container’s height. The grid block grows until it fills all available space. |
| Start |  | Packs all rows at the top of the container. Free space sits below the Grid. |
| Center |  | Packs the rows into the vertical middle of the container. Equal free space above and below the Grid. |
| End |  | Packs all rows at the bottom of the container. Free space sits above the Grid. |
| Space Between |  | Rows are spread out vertically. First row sticks to the top, last row to the bottom. Any free space is divided evenly between rows (no extra space at edges). |
| Space Around |  | Equal space placed around each row. Outer edges (top/bottom) get half-sized gaps compared to the middle gaps. |
| Space Evenly |  | Free space is divided into equal gaps everywhere, including the edges. Top, bottom, and the spaces between rows are identical. |
| Justify Items |  | Aligns the content of grid items inside their own cells along the horizontal axis (left to right). It only matters when a grid cell is wider than the item inside it.Start: Places the content against the left edge of its grid cell. Any extra space sits to the right of the item.Center: Places the content in the horizontal middle of its grid cell. Extra space is split evenly on both sides of the item.End: Places the content against the right edge of its grid cell. Any extra space sits to the left of the item.Stretch (default): Makes the content expand to fill the entire width of its grid cell. If the item has a fixed width, that width is kept; otherwise, it stretches across the whole cell. |
| Grid Offset Rules |  | Create rules to target and style specific child grid items usingnth-childselectors. Define custom positioning, spanning, and layout properties for individual grid items to create complex, asymmetrical grid layouts. |

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
