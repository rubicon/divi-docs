---
title: "The Canvas Portal Module in Divi 5"
category: modules
tags: [the, canvas, portal, module, in, divi, 5]
related: []
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14718409-the-canvas-portal-module-in-divi-5"
---

# The Canvas Portal Module in Divi 5

The Canvas Portal module injects content from a detached canvas into a specific spot on your main canvas or Theme Builder template. Instead of letting Divi auto-append canvas content when an interaction triggers, the Canvas Portal renders that canvas exactly where you place it.

## Overview

This makes the module essential when position matters: mega menus anchored to a header link, popups placed relative to a CTA, or reusable content blocks dropped into specific layout spots.

# **Add The Divi Canvas Portal Module**

When you load the Visual Builder, Divi automatically adds a **[Section](https://intercom.help/elegantthemes/en/articles/9996489-the-divi-regular-section)**.

## Settings & Options

1. Click the **Green Plus** icon ![](https://downloads.intercomcdn.com/i/o/hrpt54hy/1233840290/14e0b902982fdead446dfe547be6/add-row-icon.png?expires=1778166000&signature=ec70fcc812d3b56fa3dbf50956f36514e0b9c3ea7663a2ddccbddab770c76358&req=dSIkFcF6nYNWWfMW3Hu4gSfLZuvkMXWourhm1LfIokgrPW%2FC47%2FckgsaRM3%2B%0Abw%3D%3D%0A) to insert a **[Row](https://intercom.help/elegantthemes/en/articles/10316106-the-divi-row)**.
2. Click the **Gray Plus** icon ![](https://downloads.intercomcdn.com/i/o/hrpt54hy/1233840526/11cf2c3a95fcaced3ad5ad5667e1/add-module-icon.png?expires=1778166000&signature=4106b8792d0c8df35a0f56bb5541fb0de5d8a55a5e522b9ede89f31c759ceb81&req=dSIkFcF6nYRdX%2FMW3Hu4gfE8Rzqs58PYF4hNVCtbpIgXzqiEFMTEzshLcbEp%0AiQ%3D%3D%0A) inside the Row, which will show the list of all available Divi modules.
3. Find the **Canvas Portal Module** and click on it to load it. Alternatively, you can use the Search option to find it.

[![Divi 5 - Add the Canvas Portal Module](https://downloads.intercomcdn.com/i/o/hrpt54hy/2306162447/728cfe669f9899f20ba79be83655/212_add-canvas-module-no-borders.gif?expires=1778077800&signature=d4c9c4d49c5e03f6e9657f01b39316325077fa6a96121d17fa98b8005d86ccd4&req=diMnEMh4n4VbXvMW1HO4zQwN6Yz%2BuViOEJjJJJfJvW1uV6%2B37Hn3ss69N17j%0AHQ7sYNslCDKZLvtsOVc%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2306162447/728cfe669f9899f20ba79be83655/212_add-canvas-module-no-borders.gif?expires=1778077800&signature=d4c9c4d49c5e03f6e9657f01b39316325077fa6a96121d17fa98b8005d86ccd4&req=diMnEMh4n4VbXvMW1HO4zQwN6Yz%2BuViOEJjJJJfJvW1uV6%2B37Hn3ss69N17j%0AHQ7sYNslCDKZLvtsOVc%3D%0A)

# The Canvas Portal Module Use Cases

1. **Mega menu anchored to a header link**: Build an off-canvas mega menu on its own canvas, then drop a Canvas Portal inside the text or link module that holds the parent menu item. The mega menu renders relative to the link, so it opens exactly where you need it instead of appearing in a default off-canvas position.
2. **Newsletter popup with precise placement**: Design a newsletter popup in a detached canvas and use a Canvas Portal to inject it into a specific section of the page. Combine it with an on-load interaction and a delay, and the pop-up appears in the right spot at the right time while staying out of your way in the builder.
3. **Reusable content blocks across pages**: Build global content such as pricing tables, testimonial sliders, or announcement banners inside a global canvas. Drop a Canvas Portal into any page or Theme Builder template to display that canvas wherever you need it. Update the source canvas once, and every Canvas Portal reflects the change.

# Canvas Portal Module Settings Breakdown

Once you've added the Canvas Portal Module, the module settings automatically pop up. This is where this module's content and design styles are configured. These settings are organized into three groups via the tabs at the top of the module:

- **Content**
- **Design**
- **Advanced**

## The Content tab

The Content tab is where you pick the canvas the module displays, along with link and background styling.

[![Divi 5 - Canvas Portal Module Module's Content tab](https://downloads.intercomcdn.com/i/o/hrpt54hy/2306020531/28c02a079c739071207a10fd13c9/01_content-tab.png?expires=1778077800&signature=c8b9ff76841d1d3ec08a493d95dd1964e46a7cf4e15e47df4b33e45d5ba0e81d&req=diMnEMl8nYRcWPMW1HO4zStb%2BWB46AN0RjqPM54ztHXHHqQjxniCY2%2BVyDc4%0A%2FDISff4JTVZmBRdtIsg%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2306020531/28c02a079c739071207a10fd13c9/01_content-tab.png?expires=1778077800&signature=c8b9ff76841d1d3ec08a493d95dd1964e46a7cf4e15e47df4b33e45d5ba0e81d&req=diMnEMl8nYRcWPMW1HO4zStb%2BWB46AN0RjqPM54ztHXHHqQjxniCY2%2BVyDc4%0A%2FDISff4JTVZmBRdtIsg%3D%0A)

1. **[Canvas](https://help.elegantthemes.com/en/articles/13249775-divi-5-canvases-off-canvas-menus-popups-canvas-portals)** - Select an existing canvas from the dropdown to display inside the module. The canvas content renders in place of the Canvas Portal on the front end.
2. **[Link](https://help.elegantthemes.com/en/articles/10066994-understanding-the-link-option-group-in-divi-5)** - Make the entire Canvas Portal clickable, creating a seamless way to direct users to another page, section, or external site.
3. **[Background](https://help.elegantthemes.com/en/articles/10063358-understanding-the-background-option-group-in-divi-5)** - Choose the Canvas Portal's background styles.
4. **[Meta](https://help.elegantthemes.com/en/articles/10066900-understanding-the-meta-option-group-in-divi-5)** - Choose the Canvas Portal's Label text and force its Visibility inside the Visual Builder.

---

## The Design tab

All the design styles and options for the **Canvas Portal Module** are in this tab.

[![Divi 5 - Canvas Portal Module Module's Design tab](https://downloads.intercomcdn.com/i/o/hrpt54hy/2306020824/d6bb6aa74ece3306122dfbe41178/02_design-tab.png?expires=1778077800&signature=93c66b58917b5203430d8b31a67634fd9dadc75e86a18fa313c3e0985965323c&req=diMnEMl8nYldXfMW1HO4zRdj7Thwl%2Bp162byCWg7Cttz3H8dx%2Bdc6HSw0VJw%0AYhHlKP97P6ySVNCFiE0%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2306020824/d6bb6aa74ece3306122dfbe41178/02_design-tab.png?expires=1778077800&signature=93c66b58917b5203430d8b31a67634fd9dadc75e86a18fa313c3e0985965323c&req=diMnEMl8nYldXfMW1HO4zRdj7Thwl%2Bp162byCWg7Cttz3H8dx%2Bdc6HSw0VJw%0AYhHlKP97P6ySVNCFiE0%3D%0A)

1. **[Sizing](https://help.elegantthemes.com/en/articles/10102469-understanding-the-sizing-option-group-in-divi-5)** - Choose the Canvas Portal's sizing.
2. **[Spacing](https://help.elegantthemes.com/en/articles/10102490-understanding-the-spacing-option-group-in-divi-5)** - Choose the Canvas Portal's spacing.
3. **[Border](https://help.elegantthemes.com/en/articles/10102574-understanding-the-border-option-group-in-divi-5)** - Choose the Canvas Portal's border styles.
4. **[Box Shadow](https://help.elegantthemes.com/en/articles/10102594-understanding-the-box-shadow-option-group-in-divi-5)** - Choose the Canvas Portal's Box Shadow styles.
5. **[Filters](https://help.elegantthemes.com/en/articles/10102602-understanding-the-filters-option-group-in-divi-5)** - Choose the Canvas Portal's filters, such as hue shifts, saturation changes, and blending modes.
6. **[Transform](https://help.elegantthemes.com/en/articles/10102613-understanding-the-transform-option-group-in-divi-5)** - Choose the Canvas Portal's advanced design effects, such as scaling, rotating, skewing, and translating.
7. **[Animation](https://help.elegantthemes.com/en/articles/10102631-understanding-the-animation-option-group-in-divi-5)** - Choose the Canvas Portal's animation styles, adding personality and interactivity while keeping a polished, professional feel.

---

## The Advanced tab

The **Advanced tab** provides tools for experienced designers, including options for adding CSS IDs and Classes, controlling visibility, managing transitions, adjusting element positions, and creating scroll effects.

[![Divi 5 - Canvas Portal Module Module's Advanced tab](https://downloads.intercomcdn.com/i/o/hrpt54hy/2306021257/fa3d23c9caac47ee1e1b4461aea0/03_advanced-tab.png?expires=1778077800&signature=59a4f54fbae993b23c889664b9e04148e37fd2560c5bdc977e0e1bb5a616a0fd&req=diMnEMl8nINaXvMW1HO4zZmAL8t8nsFZ3xC2S3DFXfOE0l1twvEQwNZNJw0i%0A%2FKUSl260GMp2Nnvfo5w%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2306021257/fa3d23c9caac47ee1e1b4461aea0/03_advanced-tab.png?expires=1778077800&signature=59a4f54fbae993b23c889664b9e04148e37fd2560c5bdc977e0e1bb5a616a0fd&req=diMnEMl8nINaXvMW1HO4zZmAL8t8nsFZ3xC2S3DFXfOE0l1twvEQwNZNJw0i%0A%2FKUSl260GMp2Nnvfo5w%3D%0A)

1. **[Attributes](https://help.elegantthemes.com/en/articles/10102703-understanding-the-attributes-option-group-in-divi-5)** - Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings.
2. **[CSS](https://help.elegantthemes.com/en/articles/10102722-understanding-the-css-option-group-in-divi-5)** - Allows you to add custom CSS code to fine-tune your Canvas Portal, enabling advanced styling that perfectly aligns with your vision.
3. **[HTML](https://help.elegantthemes.com/en/articles/13284097-semantic-elements-custom-html-wrappers-for-divi-5)** - Choose the semantic HTML tag for the Canvas Portal module.
4. **[Conditions](https://help.elegantthemes.com/en/articles/10102758-understanding-the-conditions-options-in-divi-5)** - Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time.
5. **[Interactions](https://help.elegantthemes.com/en/articles/11666517-interactions-in-divi-5)** - Create custom interactions, such as showing or hiding the Canvas Portal, and many more.
6. **[Visibility](https://help.elegantthemes.com/en/articles/10102735-understanding-the-visibility-option-group-in-divi-5)** - Choose the Canvas Portal's visibility based on different devices.
7. **[Transitions](https://help.elegantthemes.com/en/articles/10102770-understanding-the-transitions-option-group-in-divi-5)** - Choose how long the Canvas Portal's animation takes, adding subtle, impactful animations that enhance user experience and make your module stand out.
8. **[Position](https://help.elegantthemes.com/en/articles/10102783-understanding-the-position-option-group-in-divi-5)** - Choose precise control of the Canvas Portal's placement and create dynamic, visually engaging designs.
9. **[Scroll Effects](https://help.elegantthemes.com/en/articles/10102792-understanding-the-scroll-effects-option-group-in-divi-5)** - Control how the Canvas Portal behaves and transforms during scrolling.

---

# What's the next step?

## Save your changes and exit the Visual Builder

To save the page design, you can type **`CMD + S` on a Mac** or **`CTRL + S` on a PC**.

You can also:

1. Click on the **Save** button.
2. Click on the **Exit** button.

[![Divi 5 - Save and Exit Visual Builder](https://downloads.intercomcdn.com/i/o/hrpt54hy/2305989961/de1dbad21a5589c8f9b0656cde4c/save-and-exit.png?expires=1778077800&signature=e29ffd047b69d01625e083f93390507e6de7f66c3e73a1831fd7d09956b278c0&req=diMnE8B2lIhZWPMW1HO4zU7abdea%2BK76FMtdzFg5e%2Fug1KV3lbNl0EMGKUlb%0AdFqaxZYNJnlMRMmWjyc%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2305989961/de1dbad21a5589c8f9b0656cde4c/save-and-exit.png?expires=1778077800&signature=e29ffd047b69d01625e083f93390507e6de7f66c3e73a1831fd7d09956b278c0&req=diMnE8B2lIhZWPMW1HO4zU7abdea%2BK76FMtdzFg5e%2Fug1KV3lbNl0EMGKUlb%0AdFqaxZYNJnlMRMmWjyc%3D%0A)

---

Related Articles

[The Comments Module in Divi 5](https://help.elegantthemes.com/en/articles/10260827-the-comments-module-in-divi-5)[The Sidebar Module in Divi 5](https://help.elegantthemes.com/en/articles/10364419-the-sidebar-module-in-divi-5)[The Toggle Module in Divi 5](https://help.elegantthemes.com/en/articles/10368052-the-toggle-module-in-divi-5)[Divi 5 Canvases (Off-Canvas Menus, Popups & Canvas Portals)](https://help.elegantthemes.com/en/articles/13249775-divi-5-canvases-off-canvas-menus-popups-canvas-portals)[The Dropdown Module in Divi 5](https://help.elegantthemes.com/en/articles/13714244-the-dropdown-module-in-divi-5)

## Code Examples

<!-- TODO: Add tested code examples -->

```css
/* TODO: Add CSS customization examples */
```

```php
// TODO: Add PHP hook/filter examples
```

## Common Patterns

<!-- TODO: Add 2-3 real-world use cases -->

## Version Notes

!!! note "Divi 5"
    This page documents Divi 5 behavior. Some settings or markup may differ from Divi 4.

## Troubleshooting

<!-- TODO: Add common issues and solutions -->

## Related

<!-- TODO: Add links to related pages -->
