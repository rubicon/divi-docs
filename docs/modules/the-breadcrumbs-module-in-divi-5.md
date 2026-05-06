---
title: "The Breadcrumbs Module in Divi 5"
category: modules
tags: [the, breadcrumbs, module, in, divi, 5]
related: []
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14852183-the-breadcrumbs-module-in-divi-5"
---

# The Breadcrumbs Module in Divi 5

The Divi **Breadcrumbs Module** displays a clickable trail that shows visitors where the current page sits inside your site - for example, **Home → Blog → Category → Post**. It helps visitors orient themselves, makes it easy to step back up the hierarchy, and gives search engines a clear signal about your content structure.

## Overview

This article covers how to add the Breadcrumbs Module to a page, walks through every setting on the **Content**, **Design**, and **Advanced** tabs, and explains how the module's sub-element design groups work alongside Divi 5's [Composable Settings](https://help.elegantthemes.com/en/articles/14332889-composable-settings-in-divi-5). If you're building breadcrumbs specifically for a WooCommerce product page, use the [Woo Breadcrumbs Module](https://help.elegantthemes.com/en/articles/12032985-the-woo-breadcrumbs-module-in-divi-5) instead.

[Screenshot: Breadcrumbs module displayed in the Visual Builder]

# Add a Breadcrumbs Module

## Settings & Options

When you load the Visual Builder, Divi automatically adds a **[Section](https://intercom.help/elegantthemes/en/articles/9996489-the-divi-regular-section)**.

1. Click the **Green Plus** icon ![](https://downloads.intercomcdn.com/i/o/hrpt54hy/1233840290/14e0b902982fdead446dfe547be6/add-row-icon.png?expires=1778166000&signature=ec70fcc812d3b56fa3dbf50956f36514e0b9c3ea7663a2ddccbddab770c76358&req=dSIkFcF6nYNWWfMW3Hu4gSfLZuvkMXWourhm1LfIokgrPW%2FC47%2FckgsaRM3%2B%0Abw%3D%3D%0A) to insert a **[Row](https://intercom.help/elegantthemes/en/articles/10316106-the-divi-row)**.
2. Click the **Gray Plus** icon ![](https://downloads.intercomcdn.com/i/o/hrpt54hy/1233840526/11cf2c3a95fcaced3ad5ad5667e1/add-module-icon.png?expires=1778166000&signature=4106b8792d0c8df35a0f56bb5541fb0de5d8a55a5e522b9ede89f31c759ceb81&req=dSIkFcF6nYRdX%2FMW3Hu4gfE8Rzqs58PYF4hNVCtbpIgXzqiEFMTEzshLcbEp%0AiQ%3D%3D%0A) inside the Row, which will show the list of all available Divi modules.
3. Find the **Accordion module** and click on it to load it. Alternatively, you can use the Search option to find it.

[![Divi 5 - Add the Breadcrumbs Module](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340235015/6745a8951c5e8b38433577eaeaf8/219_add-breadcrumbs-module.gif?expires=1778077800&signature=3479092f9681710214a6bb4126b42f92977d3d850a00d36a0968af64a6e975c7&req=diMjFst9mIFeXPMW1HO4zdOx2P5fCY9ynmhDJ9OCdIYGjb%2FwPAvnzP88wZZY%0AA%2FdqRZ2jyDFevmvxnEM%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340235015/6745a8951c5e8b38433577eaeaf8/219_add-breadcrumbs-module.gif?expires=1778077800&signature=3479092f9681710214a6bb4126b42f92977d3d850a00d36a0968af64a6e975c7&req=diMjFst9mIFeXPMW1HO4zdOx2P5fCY9ynmhDJ9OCdIYGjb%2FwPAvnzP88wZZY%0AA%2FdqRZ2jyDFevmvxnEM%3D%0A)

# The Breadcrumbs Module Use Cases

- **Site-wide navigation aid**: Place the module inside a **[Theme Builder](https://help.elegantthemes.com/en/articles/12022773-build-custom-templates-using-the-theme-builder-in-divi-5)** header so every page on your site shows the same breadcrumb trail.
- **Deep content hierarchies**: Use breadcrumbs on blogs, knowledge bases, or documentation sites where visitors land on pages several levels below the home page.
- **Accessibility and SEO**: Give visitors a visible content trail and search engines a structured navigation path that mirrors your site's information architecture.

# Breadcrumbs Module Settings Breakdown

Once you've added the Breadcrumbs Module, its settings panel opens automatically. The settings are organized into three tabs:

- **Content**
- **Design**
- **Advanced**

## The Content Tab

The Content tab is where you set the home item's text and link, choose a separator, and configure background, link, and other shared options.

[![Divi 5 - Breadcrumbs Module Module's Content tab](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340251070/2ed82bf14b41a6a6c1b6ad858606/01_content-tab.png?expires=1778077800&signature=dd84dcc448b565d533a4ea13c531e03104e5682ed816f1eada29958596190252&req=diMjFst7nIFYWfMW1HO4zbllKpCVbl%2F8nDkD2nbKYyFILbRDgx871eGqJP4u%0ArGG5%2BUx%2FB5noNQr7hNo%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340251070/2ed82bf14b41a6a6c1b6ad858606/01_content-tab.png?expires=1778077800&signature=dd84dcc448b565d533a4ea13c531e03104e5682ed816f1eada29958596190252&req=diMjFst7nIFYWfMW1HO4zbllKpCVbl%2F8nDkD2nbKYyFILbRDgx871eGqJP4u%0ArGG5%2BUx%2FB5noNQr7hNo%3D%0A)

1. **Content** - Configure the text and starting link for the breadcrumb trail.

- **Home Text** - The label for the first item in the trail. Defaults to "Home." Supports **[Dynamic Content](https://help.elegantthemes.com/en/articles/13627810-advanced-content-management-using-dynamic-content-in-divi-5)**.
   - **Home URL** - The destination URL for the first item. Defaults to your site's home page. Supports **[Dynamic Content](https://help.elegantthemes.com/en/articles/13627810-advanced-content-management-using-dynamic-content-in-divi-5)**.
   - **Separator** - The character or symbol that appears between each item in the trail (for example, **/**, **>**, or **|**).
2. **[Link](https://help.elegantthemes.com/en/articles/10066994)** - Make the entire Breadcrumbs Module clickable, sending visitors to a page, section, or external URL when they click anywhere on the module.
3. **[Elements](https://help.elegantthemes.com/en/articles/12672584-nested-module-in-divi-5)** - Toggle on or off any optional pieces of the breadcrumb trail.
4. **[Background](https://help.elegantthemes.com/en/articles/10063358)** - Choose the Breadcrumbs Module's background color, gradient, image, video, or pattern.
5. **[Loop](https://help.elegantthemes.com/en/articles/11863867-loop-builder-in-divi-5)** - Enable the Loop Builder to repeat the module across a set of items.
6. **[Meta](https://help.elegantthemes.com/en/articles/10066900-understanding-the-meta-option-group-in-divi-5)** - Set the module's label inside the Visual Builder and force its visibility while editing.

---

## The Design Tab

All the design styles for the **Breadcrumbs Module** live on this tab.

The Breadcrumbs Module breaks the trail into four sub-elements:

- the **Breadcrumb** wrapper,
- the clickable **Breadcrumb link** items,
- the **Home link**,
- and the **Separator** between items.

Each sub-element exposes its own **Background**, **Text**, **Sizing**, **Spacing**, **Border**, and **Box Shadow** option groups through Divi 5's **[Composable Settings](https://help.elegantthemes.com/en/articles/14332889-composable-settings-in-divi-5)**. If one of those option groups isn't visible inside a sub-element, hover over the sub-element and click the **Toggle Options** icon to enable it.

[![Divi 5 - Breadcrumbs Module Module's Design tab](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340251709/8de37627f7d0cccdb9f99514e855/02_design-tab.png?expires=1778077800&signature=6830fb8e2735c188fc2eebd82136e7ab528d2d1ce69c78100e922205e003e75a&req=diMjFst7nIZfUPMW1HO4zf9E%2BetPBxoNjN25ZpzueYQ2Wx1aroD%2F8cBEkvOP%0AehLbZ2rIt2IfrfF7s1w%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340251709/8de37627f7d0cccdb9f99514e855/02_design-tab.png?expires=1778077800&signature=6830fb8e2735c188fc2eebd82136e7ab528d2d1ce69c78100e922205e003e75a&req=diMjFst7nIZfUPMW1HO4zf9E%2BetPBxoNjN25ZpzueYQ2Wx1aroD%2F8cBEkvOP%0AehLbZ2rIt2IfrfF7s1w%3D%0A)

1. **Layout** - Choose the visual style for the breadcrumb trail and how items align inside the module.
2. **Breadcrumb** - Style the wrapper that contains the entire trail. Available sub-options: **[Background](https://help.elegantthemes.com/en/articles/10063358), [Text](https://help.elegantthemes.com/en/articles/10101904-understanding-the-text-option-group-in-divi-5), [Sizing](https://help.elegantthemes.com/en/articles/10102469-understanding-the-sizing-option-group-in-divi-5), [Spacing](https://help.elegantthemes.com/en/articles/10102490-understanding-the-spacing-option-group-in-divi-5), [Border](https://help.elegantthemes.com/en/articles/10102574-understanding-the-border-option-group-in-divi-5),** and **[Box Shadow](https://help.elegantthemes.com/en/articles/10102594-understanding-the-box-shadow-option-group-in-divi-5).**
3. **Breadcrumb link** - Style every clickable item in the trail except the home item. Available sub-options: **[Background](https://help.elegantthemes.com/en/articles/10063358), [Text](https://help.elegantthemes.com/en/articles/10101904-understanding-the-text-option-group-in-divi-5), [Sizing](https://help.elegantthemes.com/en/articles/10102469-understanding-the-sizing-option-group-in-divi-5), [Spacing](https://help.elegantthemes.com/en/articles/10102490-understanding-the-spacing-option-group-in-divi-5), [Border](https://help.elegantthemes.com/en/articles/10102574-understanding-the-border-option-group-in-divi-5),** and **[Box Shadow](https://help.elegantthemes.com/en/articles/10102594-understanding-the-box-shadow-option-group-in-divi-5).**
4. **Home link** - Style only the first item in the trail (the one set by **Home Text** and **Home URL**). Available sub-options: **[Background](https://help.elegantthemes.com/en/articles/10063358), [Text](https://help.elegantthemes.com/en/articles/10101904-understanding-the-text-option-group-in-divi-5), [Sizing](https://help.elegantthemes.com/en/articles/10102469-understanding-the-sizing-option-group-in-divi-5), [Spacing](https://help.elegantthemes.com/en/articles/10102490-understanding-the-spacing-option-group-in-divi-5), [Border](https://help.elegantthemes.com/en/articles/10102574-understanding-the-border-option-group-in-divi-5),** and **[Box Shadow](https://help.elegantthemes.com/en/articles/10102594-understanding-the-box-shadow-option-group-in-divi-5).**
5. **Separator** - Style the symbol or icon that sits between each item. Available sub-options: **[Background](https://help.elegantthemes.com/en/articles/10063358), [Text](https://help.elegantthemes.com/en/articles/10101904-understanding-the-text-option-group-in-divi-5), [Sizing](https://help.elegantthemes.com/en/articles/10102469-understanding-the-sizing-option-group-in-divi-5), [Spacing](https://help.elegantthemes.com/en/articles/10102490-understanding-the-spacing-option-group-in-divi-5), [Border](https://help.elegantthemes.com/en/articles/10102574-understanding-the-border-option-group-in-divi-5),** and **[Box Shadow](https://help.elegantthemes.com/en/articles/10102594-understanding-the-box-shadow-option-group-in-divi-5).**
6. **[Sizing](https://help.elegantthemes.com/en/articles/10102469)** - Set the Breadcrumbs Module's overall width, height, and alignment.
7. **[Spacing](https://help.elegantthemes.com/en/articles/10102490)** - Adjust the module's outer margin and inner padding.
8. **[Border](https://help.elegantthemes.com/en/articles/10102574)** - Add or style the module's border and rounded corners.
9. **[Box Shadow](https://help.elegantthemes.com/en/articles/10102594)** - Apply a shadow around the module.
10. **[Filters](https://help.elegantthemes.com/en/articles/10102602)** - Apply visual filters such as hue shifts, saturation changes, and blending modes.
11. **[Transform](https://help.elegantthemes.com/en/articles/10102613)** - Scale, rotate, skew, or translate the module.
12. **[Animation](https://help.elegantthemes.com/en/articles/10102631)** - Add an entrance or hover animation to the module.

**Note**: Save a styled Breadcrumbs Module as a Preset using **[Option Group Presets](https://help.elegantthemes.com/en/articles/10725144-how-to-use-option-group-presets-in-divi-5)** so the same Composable Settings stay enabled everywhere you reuse it.

---

## The Advanced Tab

The Advanced tab gives experienced designers extra control - custom CSS, semantic HTML, conditions, interactions, visibility, transitions, position, and scroll effects.

[![Divi 5 - Breadcrumbs Module Module's Advanced tab](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340252462/efc71303dcc512c5a7c88480d340/03_advanced-tab.png?expires=1778077800&signature=b10e707dd0b49ccc2f41a7e74bb2aae2e08a936be6fd0a527e14425af6a8489b&req=diMjFst7n4VZW%2FMW1HO4ze8ybLVMMSOjdZ5KzD2Wev0oecafsbFD2edo%2FvIy%0AsN9%2FJ5PQPyGN5f76h5c%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340252462/efc71303dcc512c5a7c88480d340/03_advanced-tab.png?expires=1778077800&signature=b10e707dd0b49ccc2f41a7e74bb2aae2e08a936be6fd0a527e14425af6a8489b&req=diMjFst7n4VZW%2FMW1HO4ze8ybLVMMSOjdZ5KzD2Wev0oecafsbFD2edo%2FvIy%0AsN9%2FJ5PQPyGN5f76h5c%3D%0A)

1. **[Attributes](https://help.elegantthemes.com/en/articles/10102722-understanding-the-custom-css-options-in-divi-5)** - Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the module.
2. **[CSS](https://help.elegantthemes.com/en/articles/10102722-understanding-the-custom-css-options-in-divi-5)** - Add custom CSS to fine-tune the Breadcrumbs Module beyond the built-in design options.
3. **[HTML](https://help.elegantthemes.com/en/articles/13284097-semantic-elements-custom-html-wrappers-for-divi-5)** - Choose the semantic HTML tag wrapping the module (such as **nav** or **div**).
4. **[Conditions](https://help.elegantthemes.com/en/articles/10102758)** - Show or hide the module based on conditions like logged-in status, post category, or date.
5. **[Interactions](https://help.elegantthemes.com/en/articles/11666517-interactions-in-divi-5)** - Trigger custom behaviors, such as showing or hiding the Breadcrumbs Module when another element is clicked.
6. **[Visibility](https://help.elegantthemes.com/en/articles/10102735)** - Hide the Breadcrumbs Module on phone, tablet, or desktop.
7. **[Transitions](https://help.elegantthemes.com/en/articles/10102770)** - Set how long the module's hover and state animations take.
8. **[Position](https://help.elegantthemes.com/en/articles/10102783)** - Pin the module to a specific spot on the page or relative to its container.
9. **[Scroll Effects](https://help.elegantthemes.com/en/articles/10102792)** - Animate the Breadcrumbs Module as the visitor scrolls.

---

# What's the next step?

## Save your changes and exit the Visual Builder

To save the page design, you can type **`CMD + S` on a Mac** or **`CTRL + S` on a PC**.

You can also:

1. Click on the **Save** button.
2. Click on the **Exit** button.

[![Divi 5 - Save and Exit Visual Builder](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340201609/c03c84940173c4e221b963dcc287/save-and-exit.png?expires=1778077800&signature=efdd4907bf84c058fd3036bf9842a58fa8462f95794702ec6535b28695879326&req=diMjFst%2BnIdfUPMW1HO4zVeyvN5ivr8eTwjK7VvXJWWEsZ7jWKOGIti845%2Bo%0AOM8Sq%2BOA9x3vrJxPtO0%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2340201609/c03c84940173c4e221b963dcc287/save-and-exit.png?expires=1778077800&signature=efdd4907bf84c058fd3036bf9842a58fa8462f95794702ec6535b28695879326&req=diMjFst%2BnIdfUPMW1HO4zVeyvN5ivr8eTwjK7VvXJWWEsZ7jWKOGIti845%2Bo%0AOM8Sq%2BOA9x3vrJxPtO0%3D%0A)

---

Related Articles

[The Divi Post Navigation Module](https://help.elegantthemes.com/en/articles/8643125-the-divi-post-navigation-module)[The Divi Woo Breadcrumbs Module](https://help.elegantthemes.com/en/articles/8679275-the-divi-woo-breadcrumbs-module)[The Menu Module in Divi 5](https://help.elegantthemes.com/en/articles/10353582-the-menu-module-in-divi-5)[The Woo Breadcrumbs Module in Divi 5](https://help.elegantthemes.com/en/articles/12032985-the-woo-breadcrumbs-module-in-divi-5)[The Link Module in Divi 5](https://help.elegantthemes.com/en/articles/13713821-the-link-module-in-divi-5)

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
