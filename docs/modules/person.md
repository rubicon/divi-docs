---
title: "Person"
category: modules
tags: ["modules", "team", "profile", "social-media", "image", "bio", "staff", "about"]
related: ["blurb", "testimonial", "social-media-follow"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10353818-the-person-module-in-divi-5"
---

# Person

The Person module creates a structured profile card combining a photo, name, job title, biography, and social media links in a single cohesive element.

## Overview

The Person module is purpose-built for showcasing individuals on your Divi 5 website. Whether you are building a team page, an about section, a speaker lineup for an event, or a staff directory, this module brings together all the essential profile components — a portrait image, the person's name, their role or title, a short biography, and links to their social media profiles — into one unified block.

Each profile card is self-contained and highly customizable. The image can be styled with rounded corners, borders, and filters to match your site's visual identity. Typography controls let you style the name, position, and body text independently, so you can create clear visual hierarchy between each element. Social media icons appear beneath the bio text and link directly to the person's individual profiles.

The module works best when placed in multi-column rows to create grid-style team layouts. Three or four Person modules in a row produce a professional team section with minimal configuration. For larger organizations, you can combine the module with Divi 5's Loop Builder to dynamically generate person cards from custom post types, eliminating the need to manually create each profile.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10353818-the-person-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/person/)

![Person module](../assets/screenshots/modules/person/element.png){ loading=lazy }
*The Person module as it appears on the live demo.*

## Use Cases

1. **Team Members Page** — Arrange Person modules in a three- or four-column grid to display company staff with their headshots, titles, and short bios. Link each person's social icons to their LinkedIn or Twitter profiles so visitors can connect directly.

2. **Conference Speaker Lineup** — Use the module on an event landing page to introduce keynote speakers and session leaders. The position field works well for displaying a speaker's company affiliation or talk title alongside their name and headshot.

3. **Client or Partner Showcase** — Repurpose the Person module to highlight key clients, advisors, or business partners. Replace the typical bio with a brief description of the partnership, and use the image field for a professional headshot or company logo.

## How to Add the Person Module

1. **Open the Visual Builder** on the page where you want to add the profile. Click the gray plus icon inside a row to open the module picker, then search for "Person" and click to insert it.

2. **Fill in the profile details** in the Content tab. Enter the person's name, position or job title, and a short biography in the Text group. Upload a headshot in the Image group. Add social media profile URLs for any platforms the person is active on.

3. **Customize the appearance** using the Design tab to adjust image styling, typography for the name, position, and body text, icon colors and sizes, and overall spacing. Save your page when the profile looks the way you want it.

## Settings & Options

### Content Tab

The Content tab holds all the informational fields for the profile, including the person's name, title, biography, image, and social media links.

| Setting | Type | Description |
|---------|------|-------------|
| **Text — Name** | text | Enter the person's full name, displayed as the primary heading on the profile card |
| **Text — Position** | text | Enter the person's job title, role, or other descriptor shown beneath the name |
| **Text — Body** | rich text | Write a short biography or description that appears below the position text |
| **Text — Social Media URLs** | URL fields | Enter profile URLs for social media platforms such as Facebook, Twitter/X, LinkedIn, Instagram, and others; each populated URL generates a clickable icon |
| **Image** | image upload | Upload or select a portrait photo or headshot that appears at the top of the profile card |
| **Link** | URL / toggle | Make the entire module a clickable link and configure the destination URL, target, and rel attributes |
| **Background** | composite | Set background color, gradient, image, or video behind the module |
| **Loop** | toggle | Enable the Loop Builder to render this module dynamically within loop templates |
| **Order** | number | Set the display order of the module inside a Flexbox or CSS Grid layout |
| **Meta — Label** | text | Assign a label for identification in the Visual Builder layer panel |
| **Meta — Force Visibility** | toggle | Keep the module visible in the Visual Builder even when conditions would normally hide it |

### Design Tab

The Design tab provides independent styling controls for every visual component of the profile card, from the image treatment to individual text elements, icons, and an optional button.

| Setting | Type | Description |
|---------|------|-------------|
| **Icon — Font Size** | range | Set the size of the social media icons displayed on the profile card |
| **Icon — Color** | color | Choose the color for social media icons, with optional hover state color |
| **Image — Border Radius** | range | Round the corners of the profile image, up to a full circle |
| **Image — Border Styles** | composite | Add border width, style, and color around the profile image |
| **Image — Box Shadow** | composite | Apply a shadow effect beneath or around the profile image |
| **Image — Image Filters** | composite | Adjust hue, saturation, brightness, contrast, invert, sepia, and opacity on the profile image |
| **Text — Font** | font picker | Set the default font family for all text in the module |
| **Text — Font Weight** | select | Choose the default weight for module text |
| **Text — Font Style** | toggles | Apply italic, uppercase, underline, or strikethrough to all text |
| **Text — Text Color** | color | Set the default text color for the module |
| **Text — Text Size** | range | Adjust the base font size with responsive controls |
| **Text — Letter Spacing** | range | Control spacing between characters |
| **Text — Line Height** | range | Set the vertical line height |
| **Text — Text Shadow** | composite | Apply a shadow behind the text |
| **Text — Text Alignment** | select | Align text to the left, center, or right |
| **Title Text — Font** | font picker | Choose a font family specifically for the person's name |
| **Title Text — Font Weight** | select | Set the weight of the name text |
| **Title Text — Font Style** | toggles | Apply italic, uppercase, underline, or strikethrough to the name |
| **Title Text — Text Color** | color | Override the name text color independently |
| **Title Text — Text Size** | range | Set the font size of the person's name |
| **Title Text — Letter Spacing** | range | Adjust character spacing in the name |
| **Title Text — Line Height** | range | Set the line height for the name |
| **Title Text — Text Shadow** | composite | Add a shadow effect to the name text |
| **Body Text — Font** | font picker | Choose a font family for the biography text |
| **Body Text — Font Weight** | select | Set the weight of the body text |
| **Body Text — Font Style** | toggles | Apply italic, uppercase, underline, or strikethrough to the body |
| **Body Text — Text Color** | color | Set the color of the biography text |
| **Body Text — Text Size** | range | Control the font size of the biography |
| **Body Text — Letter Spacing** | range | Adjust character spacing in the biography |
| **Body Text — Line Height** | range | Set the line height for the biography text |
| **Body Text — Text Shadow** | composite | Apply a shadow behind the biography text |
| **Position Text — Font** | font picker | Choose a font family for the position or job title text |
| **Position Text — Font Weight** | select | Set the weight of the position text |
| **Position Text — Font Style** | toggles | Apply italic, uppercase, underline, or strikethrough to the position |
| **Position Text — Text Color** | color | Set the color of the position or job title text |
| **Position Text — Text Size** | range | Control the font size of the position text |
| **Position Text — Letter Spacing** | range | Adjust character spacing in the position text |
| **Position Text — Line Height** | range | Set the line height for the position text |
| **Position Text — Text Shadow** | composite | Apply a shadow behind the position text |
| **Button** | composite | Style an optional button element including text color, background, border, padding, font, and hover states |
| **Sizing — Width** | range | Set the width of the module |
| **Sizing — Max Width** | range | Define the maximum width the module can reach |
| **Sizing — Min Height** | range | Set a minimum height for the module container |
| **Sizing — Height** | range | Set an explicit height for the module |
| **Sizing — Alignment** | select | Align the module to the left, center, or right within its parent |
| **Spacing — Margin** | range (4 sides) | Add space outside the module on each side |
| **Spacing — Padding** | range (4 sides) | Add space inside the module on each side |
| **Border — Border Width** | range | Set the width of the module border |
| **Border — Border Color** | color | Choose the color for the module border |
| **Border — Border Style** | select | Pick a border style such as solid, dashed, or dotted |
| **Border — Border Radius** | range | Round the corners of the module container |
| **Box Shadow** | composite | Add a shadow effect beneath or around the entire module |
| **Filters — Hue** | range | Shift the hue of the module content |
| **Filters — Saturation** | range | Adjust color saturation |
| **Filters — Brightness** | range | Increase or decrease brightness |
| **Filters — Contrast** | range | Adjust contrast levels |
| **Filters — Invert** | range | Invert the colors |
| **Filters — Sepia** | range | Apply a sepia tone |
| **Filters — Opacity** | range | Control overall opacity |
| **Filters — Blur** | range | Apply a blur effect |
| **Filters — Blend Mode** | select | Set how the module blends with elements behind it |
| **Transform — Scale** | range | Scale the module up or down |
| **Transform — Translate** | range | Move the module along the X and Y axes |
| **Transform — Rotate** | range | Rotate the module by a specified number of degrees |
| **Transform — Skew** | range | Skew the module along the X and Y axes |
| **Transform — Origin** | select | Set the transformation origin point |
| **Animation — Style** | select | Choose an entrance animation such as fade, slide, bounce, or zoom |
| **Animation — Direction** | select | Set the direction from which the animation enters |
| **Animation — Duration** | range | Control how long the animation takes to complete |
| **Animation — Delay** | range | Set a delay before the animation begins |
| **Animation — Intensity** | range | Adjust the strength or distance of the animation effect |
| **Animation — Starting Opacity** | range | Set the opacity at the start of the animation |
| **Animation — Speed Curve** | select | Choose an easing curve such as ease-in, ease-out, or linear |
| **Animation — Repeat** | toggle | Set whether the animation plays once or loops |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, scroll-driven effects, and positioning.

| Setting | Type | Description |
|---------|------|-------------|
| **Attributes — CSS ID** | text | Assign a unique CSS ID to the module for targeting with styles or JavaScript |
| **Attributes — CSS Classes** | text | Add one or more CSS classes, separated by spaces |
| **Attributes — Custom HTML Attributes** | repeater | Add custom data attributes or other HTML attributes to the module wrapper |
| **CSS — Custom CSS** | code editor | Write CSS rules that apply to specific internal elements of the module |
| **HTML — Semantic Tag** | select | Choose the HTML element tag (div, article, section, etc.) used for the module wrapper |
| **Conditions** | rule builder | Define conditions under which the module is displayed, such as user role, page type, or custom field values |
| **Interactions** | action builder | Create interactions that trigger show, hide, or toggle effects on other elements |
| **Visibility — Disable On** | checkboxes | Hide the module on desktop, tablet, or phone viewports |
| **Transitions — Duration** | range | Set the duration of hover and state transition animations |
| **Transitions — Delay** | range | Add a delay before transitions begin |
| **Transitions — Speed Curve** | select | Choose the easing function for transitions |
| **Position — Position** | select | Set positioning mode: default (static), relative, absolute, or fixed |
| **Position — Offsets** | range (4 sides) | Define top, right, bottom, and left offset values for positioned modules |
| **Position — Z-Index** | number | Control the stacking order relative to other positioned elements |
| **Scroll Effects — Vertical Motion** | composite | Move the module vertically as the user scrolls |
| **Scroll Effects — Horizontal Motion** | composite | Move the module horizontally on scroll |
| **Scroll Effects — Fade In/Out** | composite | Fade the module in or out based on scroll position |
| **Scroll Effects — Scaling** | composite | Scale the module up or down as the page scrolls |
| **Scroll Effects — Rotating** | composite | Rotate the module in response to scrolling |
| **Scroll Effects — Blur** | composite | Apply or remove a blur effect based on scroll position |

## Code Examples

### Custom CSS

```css
/* Center-align the entire profile card */
.et_pb_team_member {
    text-align: center;
}

/* Make the profile image circular */
.et_pb_team_member .et_pb_team_member_image img {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    object-fit: cover;
    margin: 0 auto 20px;
}

/* Style the name with brand color */
.et_pb_team_member h4 {
    color: #1e40af;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 4px;
}

/* Subtle styling for the position text */
.et_pb_team_member .et_pb_member_position {
    color: #6b7280;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

/* Add hover effect to social media icons */
.et_pb_team_member .et_pb_member_social_links a {
    color: #9ca3af;
    transition: color 0.3s ease, transform 0.3s ease;
}

.et_pb_team_member .et_pb_member_social_links a:hover {
    color: #1e40af;
    transform: scale(1.2);
}

/* Card-style layout with background and shadow */
.et_pb_team_member {
    background: #ffffff;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    transition: box-shadow 0.3s ease;
}

.et_pb_team_member:hover {
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_team_member .et_pb_team_member_image img {
        width: 120px;
        height: 120px;
    }
}
```

### PHP Hooks

```php
/* Filter the Person module output to add a schema.org markup wrapper */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_team_member' !== $render_slug) {
        return $output;
    }
    // Wrap the person card in schema.org Person markup
    $output = '<div itemscope itemtype="https://schema.org/Person">' . $output . '</div>';
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Card-Style Team Grid** — Place three Person modules in a row with equal column widths. Add a white background, rounded corners, and a subtle box shadow to each module using the Design tab's Border and Box Shadow settings. Center-align the text and use the Image border radius to create circular headshots, producing a clean card-based team layout.

2. **Executive Leadership Section** — Use a two-column row with a larger left column for the CEO or founder and a smaller right column containing a stacked pair of Person modules for other executives. Give the primary profile a larger image and more detailed biography, while the secondary profiles use abbreviated bios and smaller images.

3. **Social-Forward Author Profiles** — On a blog or publication site, place a Person module at the bottom of article templates using the Theme Builder. Populate the name, position (such as "Senior Writer"), a short author bio, and link all relevant social profiles. Style the social icons with a bold accent color so they stand out, encouraging readers to follow the author.

## Saving Your Work

After configuring the Person module, click the green **Save** button at the bottom of the Visual Builder page settings bar. For team page layouts you plan to reuse, right-click the row containing your Person modules and choose **Save to Library** to store the entire team section as a reusable element. Individual person cards can also be saved independently if different pages need different team compositions.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Person module in Divi 5 uses the updated options framework with Flexbox and Grid support, independent typography controls for each text element, conditions, interactions, and scroll effects that are not available in Divi 4. If you are still using Divi 4, consult the legacy Elegant Themes documentation.

## Troubleshooting

!!! warning "Social Media Icons Not Showing"
    If the social media icons do not appear beneath the biography text, verify that you have entered valid URLs in the Social Media URL fields under the Content tab's Text group. Icons only render for platforms that have a URL provided. If the URLs are present but icons are still missing, check the Design tab's Icon settings to ensure the font size is not set to zero and the color is not the same as the background.

!!! warning "Profile Image Not Displaying"
    If the headshot area appears blank, confirm that an image has been uploaded or selected in the Content tab's Image group. Check that the image file exists in your WordPress media library and has not been deleted. If the image is there but invisible, inspect the Design tab's Image Filters to make sure opacity has not been reduced to zero and that no extreme filter values are hiding the image.

!!! warning "Uneven Card Heights in Grid Layouts"
    When placing multiple Person modules side by side, cards may appear at different heights if biographies vary in length. To create uniform heights, set a fixed Min Height in the Design tab's Sizing group, or use CSS to apply `display: flex` and `align-items: stretch` on the parent row. Alternatively, keep biography text to a consistent length across all team members.

## Related

- [Blurb](blurb.md)
- [Testimonial](testimonial.md)
- [Social Media Follow](social-media-follow.md)
