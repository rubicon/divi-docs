---
title: "How to Create the Ken Burns Effect in Divi 5"
category: troubleshooting
tags: [how, to, create, the, ken, burns, effect, in, divi, 5]
related: []
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14663402-how-to-create-the-ken-burns-effect-in-divi-5"
---

# How to Create the Ken Burns Effect in Divi 5

The Ken Burns effect is a slow zoom and pan applied to a still image. It's named after documentary filmmaker Ken Burns, who popularized the technique. The effect adds cinematic motion to a static background and works well in hero sections.

## Overview

This guide walks you through building the effect in Divi 5 using the Hero module, the **[Custom Attributes](https://help.elegantthemes.com/en/articles/12274853-custom-attributes-in-divi-5)** option group, and a small block of custom CSS.

## Before You Begin

- Have a high-resolution image ready. The effect zooms up to 1.5x, so use an image large enough to avoid pixelation.

## Settings & Options

## Add a Section and Hero Module

Open the page in the Visual Builder where you want the effect.

1. Add a regular **[Section](https://help.elegantthemes.com/en/articles/9996489-the-section-in-divi-5)**.
2. Inside the Section, add a **[Row](https://help.elegantthemes.com/en/articles/10316106-the-row-in-divi-5)** with a single column.
3. Add the **[Hero](https://help.elegantthemes.com/en/articles/10369762-the-hero-module-in-divi-5)** module to the column.
4. Set the **Title**, subtitle, and body text as needed.

### Optional steps

1. Edit the **Section** and go to the **Design tab → Spacing.**
2. Set the **Top** and **Bottom** padding to **0**.
3. Edit the **Row** and go to the **Desing tab** → **Sizing**.
4. Set the **Width** and **Max Width** to 100%.
5. Open the **Hero** module's settings and go to the **Design Tab → Layout.**
6. Enable the **Make Fullscreen** option.

## Set the Background Image and Enable Parallax

[![Divi 5 - Hero module enable Parallax effect](https://downloads.intercomcdn.com/i/o/hrpt54hy/2285268526/5d6c1e6d2fadc6c87e5cdef31de4/ken-burn-1.png?expires=1778077800&signature=8181ef9b17b72b7718f045c6f9017ad1161c1eeb1c973a516132d91df0eb9398&req=diIvE8t4lYRdX%2FMW1HO4ze76hEPYkevlMbQEFqVHg48SQZhbJlRBmd2k0aQ6%0A7CDyn7%2BHbjkJfG2f4%2BU%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2285268526/5d6c1e6d2fadc6c87e5cdef31de4/ken-burn-1.png?expires=1778077800&signature=8181ef9b17b72b7718f045c6f9017ad1161c1eeb1c973a516132d91df0eb9398&req=diIvE8t4lYRdX%2FMW1HO4ze76hEPYkevlMbQEFqVHg48SQZhbJlRBmd2k0aQ6%0A7CDyn7%2BHbjkJfG2f4%2BU%3D%0A)

Open the Hero module settings.

1. Go to **Content → Background → Background Image**.
2. Click +**Add Background Image** and choose your image.
3. Find the **Background Image Parallax** toggle and set it to **On**.
4. Set the **Parallax Method** to **CSS**.

## Add a CSS Class as a Custom Attribute

[![Divi 5 - Hero module add CSS class](https://downloads.intercomcdn.com/i/o/hrpt54hy/2285274568/489dfcef9cd1186e6cc3926665bc/ken-burn-2.png?expires=1778077800&signature=166ba3159daf6a5cdea3be6cfdc434c00fa2b1400a5a342df8323a7f4b3c5914&req=diIvE8t5mYRZUfMW1HO4zZoGir89k%2B%2BKkuY6Ik0Gdil5MzgInmuPvLRaSoxC%0AAuI0SuMIFhByE%2FeJYCk%3D%0A)](https://downloads.intercomcdn.com/i/o/hrpt54hy/2285274568/489dfcef9cd1186e6cc3926665bc/ken-burn-2.png?expires=1778077800&signature=166ba3159daf6a5cdea3be6cfdc434c00fa2b1400a5a342df8323a7f4b3c5914&req=diIvE8t5mYRZUfMW1HO4zZoGir89k%2B%2BKkuY6Ik0Gdil5MzgInmuPvLRaSoxC%0AAuI0SuMIFhByE%2FeJYCk%3D%0A)

In Divi 5, CSS classes are added through the **Attributes** option group. Full details are in **[Custom Attributes in Divi 5](https://help.elegantthemes.com/en/articles/12274853-custom-attributes-in-divi-5)**.

1. In the Hero module settings, go to the **Advanced** tab.
2. Expand the **Attributes** option group.
3. Click **+ Add Attribute**.
4. Set the **Target** to **Module**.
5. Set the attribute **Name** to `class`.
6. Set the **Value** to one of the following, depending on the motion you want:

- **kb-zoomin** - zooms in on the image
   - **kb-zoomout** - zooms out from the image
   - **kb-zoomin-right** - zooms in and pans right
   - **kb-zoomout-right** - zooms out and pans right

## Add the Custom CSS

Paste the CSS below into Divi's site-wide custom CSS area. For every place custom CSS can live in Divi 5, see **[Where to Add Custom CSS Code in Divi 5](https://help.elegantthemes.com/en/articles/13480630-where-to-add-custom-css-code-in-divi-5)**.

For this particular example, we recommend adding the CSS code to the **Divi** → **Theme Options → Custom CSS.**

```
.kb-zoomin .et-pb-parallax-wrapper {  
  animation: zoomin 17s forwards;  
}  
  
.kb-zoomout .et-pb-parallax-wrapper {  
  animation: zoomout 17s forwards;  
}  
  
.kb-zoomin-right .et-pb-parallax-wrapper {  
  animation: zoomin-right 17s forwards;  
}  
  
.kb-zoomout-right .et-pb-parallax-wrapper {  
  animation: zoomout-right 17s forwards;  
}  
  
@keyframes zoomin {  
  0% {  
    transform: scale3d(1.1, 1.1, 1.1);  
    animation-timing-function: linear;  
  }  
  
  100% {  
    transform: scale3d(1.5, 1.5, 1.5);  
  }  
}  
  
@keyframes zoomout {  
  0% {  
    transform: scale3d(1.5, 1.5, 1.5);  
    animation-timing-function: linear;  
  }  
  
  100% {  
    transform: scale3d(1.1, 1.1, 1.1);  
  }  
}  
  
@keyframes zoomin-right {  
  0% {  
    transform: scale3d(1.1, 1.1, 1.1) translate3d(0, 0, 0);  
    animation-timing-function: linear;  
  }  
  
  100% {  
    transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0);  
  }  
}  
  
@keyframes zoomout-right {  
  0% {  
    transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0);  
    animation-timing-function: linear;  
  }  
  
  100% {  
    transform: scale3d(1.1, 1.1, 1.1) translate3d(0, 0, 0);  
  }  
}
```

**Note**: Adjust the `17s` duration to speed up or slow down the motion.

## Save the Changes

Click **Save** in the top bar of the Visual Builder, and view the page.

The background image inside the Hero module will zoom or pan based on the class applied.

---

Related Articles

[How to Add Zoom-In Hover Effect to the Image Module](https://help.elegantthemes.com/en/articles/2699953-how-to-add-zoom-in-hover-effect-to-the-image-module)[How to Create and Use the "Ken Burns Effect" in Divi](https://help.elegantthemes.com/en/articles/2717227-how-to-create-and-use-the-ken-burns-effect-in-divi)[The Image Module in Divi 5](https://help.elegantthemes.com/en/articles/10315772-the-image-module-in-divi-5)[The Slider Module in Divi 5](https://help.elegantthemes.com/en/articles/10364612-the-slider-module-in-divi-5)[The Hero Module in Divi 5](https://help.elegantthemes.com/en/articles/10369762-the-hero-module-in-divi-5)

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
