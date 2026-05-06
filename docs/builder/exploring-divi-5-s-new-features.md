---
title: "Exploring Divi 5's New Features"
category: builder
tags: [builder, visual-builder, divi-5-features]
related: [flexbox-layout, css-grid-layout, nested-modules, loop-builder, design-variables, interactions, command-center]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12331954-exploring-divi-5-s-new-features"
---

# Exploring Divi 5's New Features

Divi 5 introduces a comprehensive suite of layout, design, and workflow enhancements that fundamentally transform how you build websites. This page provides an overview of the major features and capabilities introduced in Divi 5.

## Overview

Divi 5 represents a significant evolution of the Divi page builder, focusing on advanced layout control, intelligent design systems, and streamlined workflows. The new features are organized into several key categories: layout systems (Flexbox and CSS Grid), content management (Loop Builder and nested components), design and styling tools (Design Variables, presets, and color systems), and builder intelligence (search, commands, and attribute management).

Whether you're building complex multi-column layouts, creating dynamic content displays, or managing design consistency across a large site, Divi 5's new features provide the tools to accomplish these tasks efficiently without custom code.

![Divi 5 Visual Builder overview](../assets/screenshots/builder/exploring-new-features/overview.png){ loading=lazy }
*The Divi 5 Visual Builder with new layout and design tools.*

## Layout & Structure Systems

### Flexbox Layout

New flexbox options are available for every container element. You can control layout direction, wrapping, ordering, spacing, and child element positioning with intuitive visual controls.

**Key capabilities:**
- Control layout wrapping and direction
- Manage ordering of child elements
- Adjust spacing between items
- Position child elements precisely
- No custom CSS required

For detailed information, see the [Flexbox Layout documentation](../builder/understanding-divi-s-new-flexbox-layout.md).

![Flexbox layout controls](../assets/screenshots/builder/exploring-new-features/flexbox-layout.png){ loading=lazy }
*Flexbox layout options applied to a row.*

### CSS Grid Layout

CSS Grid is a new layout system integrated into Divi that allows for more efficient arrangement and alignment of items within containers. Grid is available for Sections, Rows, Columns, and Module Groups, enabling you to create complex multi-dimensional layouts with precise control.

**Key capabilities:**
- Define grid columns and rows
- Place items across grid cells
- Control alignment and justification
- Create responsive grid layouts
- No grid templates required — you control the design

For detailed information, see the [CSS Grid Layout documentation](../builder/understanding-divi-s-css-grid-layout.md).

![CSS Grid layout configuration](../assets/screenshots/builder/exploring-new-features/grid-layout.png){ loading=lazy }
*CSS Grid layout applied to a section.*

### Nested Modules

Nested modules let you place one module inside another, creating deeply layered designs. You can nest rows, tabs, sliders, and buttons as deeply as you like. Every element becomes a container with full flex and grid controls.

**Key capabilities:**
- Nest modules to any depth
- Access flex and grid controls on every element
- Use right-click controls to manage nesting
- Drag-and-drop to reorder nested content
- Maintain design integrity across layers

For detailed information, see the [Nested Modules documentation](../builder/nested-modules.md).

![Nested modules in Visual Builder](../assets/screenshots/builder/exploring-new-features/nested-modules.png){ loading=lazy }
*Nested modules displayed in the Visual Builder.*

### Nested Rows

You can now add rows inside other rows, creating advanced multi-level layouts. When you click the plus button inside a column, a new row tab allows you to select from Divi's premade row templates alongside regular modules.

**Key capabilities:**
- Add rows as children of columns
- Access premade row templates
- Maintain full design control at each level
- Nest rows multiple levels deep
- Use all Divi's layout tools on nested rows

For detailed information, see the [Nested Rows documentation](../builder/nested-rows.md).

### Group Module

The Group module is a new container in Divi's layout hierarchy (Sections > Rows > Columns > Groups). Groups can be added inside columns to group multiple modules into a shared container. Once grouped, your modules can be duplicated, dragged, dropped, styled, and managed as a single element.

**Key capabilities:**
- Group multiple modules together
- Apply shared styling to groups
- Duplicate entire groups as units
- Style groups using all design options
- Manage groups from the outline panel

For detailed information, see the [Group Module documentation](../modules/group.md).

## Content Management & Display

### Loop Builder

The Loop Builder lets you display dynamic content from your website's database (posts, products, categories, authors) with custom designs for each item. This enables you to create custom blog feeds, product lists, event calendars, course lists, and category pages without plugins.

**Supported content types:**
- Blog posts and custom post types
- Products (WooCommerce and custom)
- Categories and taxonomies
- Authors
- Custom database queries

For detailed information, see the [Loop Builder documentation](../builder/loop-builder.md).

![Loop Builder interface](../assets/screenshots/builder/exploring-new-features/loop-builder.png){ loading=lazy }
*Loop Builder displaying a custom blog feed.*

### Group Carousel Module

Unlike other carousels, each slide in the Group Carousel is a blank canvas where you can add any module. You control the number of slides, slide content, animation settings, and styling through Divi's wide range of design options.

**Key capabilities:**
- Add any module to carousel slides
- Control slide count and transitions
- Apply animations and effects
- Style slides with all design tools
- No carousel template limitations

For detailed information, see the [Group Carousel Module documentation](../modules/group-carousel.md).

![Group Carousel module](../assets/screenshots/builder/exploring-new-features/group-carousel.png){ loading=lazy }
*Group Carousel with custom module content on each slide.*

## New Modules

### Lottie Module

The Lottie module makes it easy to add Lottie animations to your website. Lottie animations are JSON and SVG-based, making them lightweight and pixel-perfect. You can control animation playback and add interactions.

**Key capabilities:**
- Upload or link Lottie animation files
- Control animation playback settings
- Add click and scroll interactions
- Responsive animation scaling
- Lightweight file sizes

For detailed information, see the [Lottie Module documentation](../modules/lottie.md).

![Lottie module animation](../assets/screenshots/builder/exploring-new-features/lottie-module.png){ loading=lazy }
*Lottie animation displayed in Divi.*

### Icon List Module

The Icon List module simplifies creating lists with unique icons assigned to each item. It fills a gap in Divi's basic module library for simple but styled icon lists.

**Key capabilities:**
- Create custom icon lists
- Assign different icons to each item
- Style icons and text independently
- Control list layout and spacing
- Responsive icon sizing

For detailed information, see the [Icon List Module documentation](../modules/icon-list.md).

![Icon List module](../assets/screenshots/builder/exploring-new-features/icon-list-module.png){ loading=lazy }
*Icon List module with custom icons and styling.*

## Responsive Design & Breakpoints

### Customizable Breakpoints

Divi 5 comes with seven pre-defined breakpoints covering every device type, and you can customize the width of each breakpoint. This gives you control of your design at every screen size.

**Pre-defined breakpoints:**
- Desktop (large)
- Desktop (medium)
- Desktop (small)
- Tablet (landscape)
- Tablet (portrait)
- Mobile (landscape)
- Mobile (portrait)

For detailed information, see the [Customizable Breakpoints documentation](../builder/customize-the-divi-5-s-default-breakpoints.md).

### Responsive Editor

The new responsive editor lets you make responsive changes to design options without switching view modes. Click the responsive editor icon and adjust values across all breakpoints simultaneously. This is especially helpful when using design variables, as you can update multiple responsive values without constant view switching.

For detailed information, see the [Responsive Editor documentation](../builder/responsive-editor.md).

## Design & Styling Systems

### Design Variables

Design Variables is a new system for managing your website's design consistency. Define variables for colors, fonts, numbers, images, and text, then plug them into Divi elements and presets. When you update a variable, your entire website's design updates instantly.

**Variable types:**
- Color variables
- Font variables
- Number variables
- Image variables
- Text variables

For detailed information, see the [Design Variables documentation](../builder/design-variables.md).

![Design Variables interface](../assets/screenshots/builder/exploring-new-features/design-variables.png){ loading=lazy }
*Defining and applying design variables.*

### Relative Colors & HSL

The Relative Colors & HSL system allows you to define colors as variables and create variations based on a primary color by adjusting hue, saturation, lightness, and opacity. When the base color changes, all dependent colors automatically update while retaining their color relationships.

**Key capabilities:**
- Define primary colors as variables
- Create HSL-based color variations
- Auto-update dependent colors
- Maintain color harmony across the site
- No manual color adjustment needed

For detailed information, see the [Relative Colors & HSL documentation](../builder/relative-colors-hsl.md).

### Option Group Presets

Option Group Presets let you create reusable style collections and apply them to any element. Unlike other presets, these are not module-specific, allowing them to be mixed and matched across all elements. If you use the same background, border, or text style repeatedly, define it once and apply it everywhere.

**Key capabilities:**
- Create reusable style presets
- Apply presets across different module types
- Update presets and apply changes site-wide
- Organize presets into groups
- Export and import preset libraries

For detailed information, see the [Option Group Presets documentation](../builder/option-group-presets.md).

### Advanced Units

The Advanced Units system includes a multi-functional unit field supporting the full range of CSS units, functions, and variables. It supports unitless values (unset, fit-content), CSS functions (clamp(), calc()), and custom CSS variables, making responsive design with fluid typography easier.

**Supported units and functions:**
- All CSS units (px, em, rem, %, vh, vw, etc.)
- CSS functions (calc(), clamp(), min(), max())
- Unitless values (unset, fit-content)
- Custom CSS variables
- Relative values and calculations

For detailed information, see the [Advanced Units documentation](../builder/advanced-units.md).

## Builder Intelligence & Workflow

### Style Inspector

The Style Inspector gives you a complete overview of everything applied to your design in one place. It shows styles, content, and presets and lets you edit them directly. Work at the page level to see all applied values, or focus on a specific element.

**Key capabilities:**
- View all applied styles on an element
- See preset and variable usage
- Edit styles directly from inspector
- Filter by style type
- Page-level and element-level views

For detailed information, see the [Style Inspector documentation](../builder/style-inspector.md).

![Style Inspector panel](../assets/screenshots/builder/exploring-new-features/style-inspector.png){ loading=lazy }
*Style Inspector showing all applied styles.*

### Attribute Management

The Attribute Management system allows you to selectively or collectively copy, paste, and reset attributes across elements. You can copy styles, presets, and content from one element and paste them onto another, at the field, group, or element level. Right-click menus provide quick access to attribute operations.

**Key capabilities:**
- Copy and paste individual attributes
- Copy and paste attribute groups
- Reset specific attributes
- Apply attributes collectively
- Right-click attribute management

For detailed information, see the [Attribute Management documentation](../builder/attribute-management.md).

### Extend Attributes

Extend Attributes lets you propagate attributes through your page to make sweeping changes instantly. Right-click any element and select Extend Attributes to choose which attributes (styles, presets, content) to extend and which elements to apply them to.

**Key capabilities:**
- Extend styles across multiple elements
- Extend presets to similar elements
- Extend content properties
- Apply changes instantly to all targets
- Selective attribute extension

For detailed information, see the [Extend Attributes documentation](../builder/extend-attributes.md).

### Settings Search and Filtering

Settings Search and Filtering eliminates the frustration of clicking through tabs and scrolling to find the one setting you need. Search for any setting by name and Divi instantly jumps to it, dramatically speeding up the design workflow.

**Key capabilities:**
- Search for settings by keyword
- Filter settings by type
- Jump to settings instantly
- Works across all tabs and groups
- Supports all module types

For detailed information, see the [Settings Search and Filtering System documentation](../builder/settings-search.md).

### Find and Replace

The new Find and Replace system lets you swap dozens of static instances with design variables in just a few clicks. For example, swap all static font instances with a new title font variable created using Divi 5's design variable system. This is an excellent way to remove static values and replace them with variables.

**Use cases:**
- Replace static fonts with font variables
- Replace static colors with color variables
- Batch-update multiple elements
- Modernize older designs
- Standardize design systems

For detailed information, see the [Find and Replace documentation](../builder/find-and-replace.md).

### Command Center

The Divi 5 Command Center lets you run builder actions from a single search box. Use it to add elements, jump to specific settings, open modals, switch view modes, navigate your site, and run common edit actions without digging through menus.

**Key capabilities:**
- Add modules and sections
- Jump to specific settings
- Switch view modes
- Open panels and modals
- Navigate site structure
- Keyboard-driven workflow

For detailed information, see the [Command Center documentation](../builder/command-center.md).

![Command Center interface](../assets/screenshots/builder/exploring-new-features/command-center.png){ loading=lazy }
*Command Center providing quick access to builder actions.*

## Advanced Features

### Interactions

The Interactions System is a robust system for creating interactive elements such as popups and toggles, and creative scroll-based and mouse-movement-based effects. Add interactivity without custom code.

**Interaction types:**
- Click interactions (toggle, show/hide, scroll)
- Hover interactions
- Scroll-based animations
- Mouse-movement effects
- Custom animation sequences

For detailed information, see the [Interactions documentation](../builder/interactions.md).

![Interactions configuration](../assets/screenshots/builder/exploring-new-features/interactions.png){ loading=lazy }
*Setting up interactive effects on a module.*

### Custom Attributes

Attributes play an essential role in accessibility. With the new custom attributes system, you can define the characteristics you need to ensure screen readers understand your content. This is especially important for complex layouts and custom modules.

**Key capabilities:**
- Add ARIA attributes for accessibility
- Define data attributes for JavaScript
- Custom HTML attributes
- Improve screen reader understanding
- Enhance SEO with semantic attributes

For detailed information, see the [Custom Attributes documentation](../builder/custom-attributes.md).

### Semantic Elements & Custom HTML Wrappers

In Divi 5, you can change the element type of any module and use semantic tags like nav, section, header, article, footer, and button to give your content inherent meaning. This helps both accessibility and SEO.

**Semantic tags:**
- nav, header, footer, main
- section, article, aside
- Semantic button, link tags
- Custom HTML wrappers
- Proper page structure

For detailed information, see the [Semantic Elements & Custom HTML Wrappers documentation](../builder/semantic-elements.md).

### Divi 5 Canvases (Off-Canvas, Popups & Canvas Portals)

A canvas in Divi 5 is a workspace detached from your main post content. Use canvases as staging areas for design updates, a place to organize off-canvas components, or a safe space to experiment with new ideas without touching what visitors see.

**Canvas types:**
- Off-canvas navigation menus
- Popup modals
- Canvas portals (nested canvases)
- Staging areas for design work

For detailed information, see the [Divi 5 Canvases documentation](../builder/canvases.md).

## Preset & Content Management

### Preset Manager and Preset Preview Systems

Preset Manager and Preset Preview give you a central place to manage all your presets and a safe preview area to edit them without touching your actual page content. Browse every preset on your site, edit and reorder them, and see results in a dedicated previewer before committing changes.

**Key capabilities:**
- Browse all presets on your site
- Edit presets safely in preview mode
- Reorder presets
- Duplicate presets
- Export and import presets

For detailed information, see the [Preset Manager and Preset Preview Systems documentation](../builder/preset-manager.md).

### Page Manager, Preview Mode, and Content Drill Down

These new Divi 5 features allow you to work more efficiently inside the Visual Builder by quickly previewing your work and navigating deeply nested content without hunting for elements. The Page Manager displays your site structure, Preview Mode shows front-end rendering, and Content Drill Down lets you navigate nested elements easily.

**Key capabilities:**
- Page Manager for site structure
- Quick preview of changes
- Navigate nested content without scrolling
- Outline view of element hierarchy
- Efficient element selection

For detailed information, see the [Page Manager, Preview Mode, and Content Drill Down documentation](../builder/page-manager.md).

## Full Site Editing

### Editable Theme Builder Areas

Edit every part of your website — header, footer, and body templates — directly from the front end, without visiting the Theme Builder separately. This streamlines your workflow when making global design changes.

**Editable areas:**
- Header template
- Footer template
- Body content area
- Direct front-end editing
- No Theme Builder required

For detailed information, see the [Editable Theme Builder Areas documentation](../builder/editable-theme-builder-areas-in-divi-5.md).

### Composable Settings

Composable Settings give you the ability to enable any of Divi's design options on any module sub-element. Instead of being limited to default options for each sub-element, you can toggle on additional settings like backgrounds, borders, transforms, sizing, and animations without writing CSS.

**Composable options:**
- Background settings
- Border settings
- Transform effects
- Sizing controls
- Animation options

For detailed information, see the [Composable Settings documentation](../builder/composable-settings-in-divi-5.md).

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 features exclusively. All features described are available only in Divi 5 and later.

## Related

- [Flexbox Layout](../builder/understanding-divi-s-new-flexbox-layout.md)
- [CSS Grid Layout](../builder/understanding-divi-s-css-grid-layout.md)
- [Nested Modules](../builder/nested-modules.md)
- [Loop Builder](../builder/loop-builder.md)
- [Design Variables](../builder/design-variables.md)
- [Interactions](../builder/interactions.md)
- [Command Center](../builder/command-center.md)
- [Divi 5 Canvases](../builder/canvases.md)
