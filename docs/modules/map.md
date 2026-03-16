---
title: "Map"
category: modules
tags: ["modules", "map", "google-maps", "location", "interactive", "embed"]
related: ["fullwidth-map"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10353411-the-map-module-in-divi-5"
---

# Map

The Map module embeds an interactive Google Map with custom pin locations directly into your Divi 5 layout.

## Overview

The Map module lets you display a fully interactive Google Map on any page built with Divi 5. You can define a center address, set the zoom level, and place multiple custom pins at specific locations, each with its own title and description that appear in an info window when clicked. This makes the module an effective way to show your business location, office addresses, store branches, event venues, or any set of geographic points of interest.

Google Maps integration in Divi 5 requires a valid Google Maps API key, which you configure in the Divi Theme Options panel. Once the API key is set, every Map module on your site will render a live, draggable, zoomable map that visitors can interact with. The module supports standard Google Maps controls including zoom buttons, street view access, and map type switching between roadmap, satellite, terrain, and hybrid views.

The Design tab provides controls for the map container styling, while the map pins themselves can be individually configured with titles and descriptions. For locations that require a larger map display, consider the [Fullwidth Map](fullwidth-map.md) module, which spans the entire browser width. The standard Map module fits within a column and can be placed alongside other modules in multi-column rows, making it suitable for contact pages, location directories, and about sections.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10353411-the-map-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/map/)

![Map module](../assets/screenshots/modules/map/element.png){ loading=lazy }
*The Map module displaying an interactive Google Map with a location pin.*

## Use Cases

1. **Business Contact Page** — Display your office or storefront location on a contact page alongside your address, phone number, and contact form. Add a pin with your business name and a brief description so visitors can identify the location at a glance.

2. **Multi-Location Directory** — Add multiple pins to a single map to show all of your branches, franchises, or service areas. Each pin can have a unique title and description, helping visitors find the nearest location and view relevant details in the info window.

3. **Event Venue Map** — Embed a map on an event page to show attendees exactly where the venue is located. Set the zoom level to show nearby landmarks, parking areas, and transit options so visitors can plan their trip.

## How to Add the Map Module

1. **Open the Visual Builder** — Navigate to the page where you want the map and activate the Divi 5 Visual Builder. Click the plus icon in the section and row where the map should appear.

2. **Select the Map Module** — Search for "Map" in the module picker or browse the module list. Click to insert it into your chosen column.

3. **Configure the Map** — Enter a center address and adjust the zoom level in the Content tab. Add one or more pins by clicking the "Add New Pin" button, then enter the address, title, and description for each pin. Adjust the map height and styling in the Design tab.

## Settings & Options

### Content Tab

The Content tab controls the map configuration, pin locations, and general module settings.

| Setting | Type | Description |
|---------|------|-------------|
| Add New Pin | button | Opens the pin configuration panel where you add individual map markers. Each pin has its own title, content description, and address fields. The address is geocoded to place the pin at the correct coordinates on the map. |
| Map | group | Contains the core map configuration settings — the center map address (the location the map is initially centered on), the zoom level (which controls how close or far the initial view is), and the map type. |
| Link | group | Configure a link URL applied to the module wrapper element. Includes link target settings for same window or new tab behavior. |
| Background | group | Apply a background color, gradient, or image behind the module container. This is visible if the map container has padding or if the map fails to load. |
| Loop | toggle | When used inside a dynamic layout such as a Theme Builder template, this controls whether the module repeats for each item in a post loop. |
| Order | select | Determines the display order of the module relative to sibling modules within the same container. |
| Meta | group | Contains the admin label field for assigning a custom name to this module instance in the Visual Builder layers panel. |

### Design Tab

The Design tab provides visual customization for the map container and the controls displayed on the map.

| Setting | Type | Description |
|---------|------|-------------|
| Controls | group | Toggle the visibility of Google Maps UI controls such as the zoom buttons, map type selector, street view pegman, and fullscreen button. Disabling controls creates a cleaner presentation but limits interactivity. |
| Map | group | Configure the map container appearance including the map height, which determines how tall the embedded map is in pixels. Also includes options for the draggable state and mouse wheel zoom behavior. |
| Sizing | group | Set the width, max-width, height, and min-height of the module container. These values constrain the overall dimensions of the map element within the page layout. |
| Spacing | group | Margin and padding controls for the module container. Set values per side and configure responsive overrides for desktop, tablet, and phone breakpoints. |
| Border | group | Apply border width, color, style, and border radius to the map container. Border radius rounds the corners of the map, and all four corners can be set independently. |
| Box Shadow | group | Add a shadow effect behind the map module with configurable horizontal offset, vertical offset, blur radius, spread radius, and color. |
| Filters | group | CSS filter controls applied to the entire module — hue rotate, saturate, brightness, contrast, invert, sepia, opacity, and blur. Adjusting these filters affects the map appearance, which can be used to create a muted or stylized map look. |
| Transform | group | CSS transform controls including scale, translate, rotate, skew, and transform origin. Transforms apply to the module container. |
| Animation | group | Entrance animation played when the module scrolls into the viewport. Options include fade, slide, bounce, zoom, flip, fold, and roll with direction, duration, delay, and intensity controls. |

### Advanced Tab

The Advanced tab provides HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

| Setting | Type | Description |
|---------|------|-------------|
| Attributes | group | Set the CSS ID and CSS class for the module. The ID must be unique on the page and can be used for anchor links or JavaScript targeting. Multiple CSS classes can be separated by spaces. |
| CSS | group | Write custom CSS targeting specific elements within the module such as the map container, pin info windows, or the module wrapper. Styles are scoped to this module instance. |
| HTML | group | Add custom HTML attributes to the module wrapper element for data attributes, ARIA labels, or other custom properties. |
| Conditions | group | Set display conditions that control when the module is visible based on criteria such as user role, logged-in status, date/time, post type, or custom logic. |
| Interactions | group | Configure click, hover, and scroll-based interactions that trigger animations or state changes on this or other elements on the page. |
| Visibility | toggle | Control whether the module appears on desktop, tablet, and phone. Hidden modules are removed from the page output on the excluded device types. |
| Transitions | group | Configure the CSS transition duration, delay, and easing curve for hover-state changes on the module. |
| Position | group | Set the CSS position property (relative, absolute, fixed, sticky) and offset values for precise placement. |
| Scroll Effects | group | Apply scroll-driven animations such as parallax movement, fading, scaling, rotating, or blurring as the user scrolls past the module. |

## Code Examples

### Custom CSS — Rounded Map Container

```css
/* Apply rounded corners and shadow to the map */
.et_pb_map_container {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}
```

### Custom CSS — Grayscale Map Style

```css
/* Desaturate the map for a muted, modern look */
.et_pb_map_container iframe,
.et_pb_map_container .gm-style {
    filter: grayscale(100%);
    transition: filter 0.3s ease;
}

/* Restore color on hover */
.et_pb_map_container:hover iframe,
.et_pb_map_container:hover .gm-style {
    filter: grayscale(0%);
}
```

### Custom CSS — Custom Map Height Per Device

```css
/* Adjust map height for different screen sizes */
.et_pb_map_container {
    height: 450px;
}

@media (max-width: 980px) {
    .et_pb_map_container {
        height: 350px;
    }
}

@media (max-width: 767px) {
    .et_pb_map_container {
        height: 250px;
    }
}
```

### PHP — Filter Map Module Output

```php
/* Add a caption below every Map module */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_map' !== $render_slug) {
        return $output;
    }

    $caption = '<p class="map-caption">Click the map to explore. Use pins for location details.</p>';
    return $output . $caption;
}, 10, 2);
```

### JavaScript — Custom Map Styling via Google Maps API

```javascript
/* Apply a custom map style after the map loads */
document.addEventListener('DOMContentLoaded', function() {
    const checkMap = setInterval(function() {
        const maps = document.querySelectorAll('.et_pb_map');
        if (maps.length > 0) {
            clearInterval(checkMap);
            // Access the Google Map instance through Divi's API
            // to apply custom JSON styling for colors, labels, etc.
        }
    }, 500);
});
```

## Common Patterns

### 1. Contact Page with Map and Form

Place the Map module in a two-column row alongside a contact form or a column containing your address, phone number, and email. Set a single pin at your business location with your company name as the title and your full address in the description. This gives visitors both a visual reference and a way to reach you.

### 2. Multi-Location Store Finder

Add multiple pins to the map, one for each branch or service location. Give each pin a descriptive title (such as the branch name or city) and include the address, hours, or phone number in the pin description. Set the zoom level wide enough to show all locations simultaneously, and consider placing the map in a fullwidth section for maximum visibility.

### 3. Styled Minimal Map

Apply the grayscale CSS filter to the map for a muted, monochromatic appearance that blends with modern, minimalist page designs. Use the hover color-restore technique so the map comes to life when visitors interact with it. Round the container corners with border radius and add a subtle box shadow to frame the map as a design element rather than a utilitarian embed.

## Saving Your Work

After configuring the Map module and adding your pins, click the green checkmark button at the bottom of the settings panel to apply your changes. Save the page using the save button in the Visual Builder toolbar or press Ctrl+S (Cmd+S on Mac). Preview the page on the front end to verify the map loads correctly and all pins appear at the expected locations.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Map Not Displaying"
    If the Map module shows a blank area or an error message instead of the map:

    - Verify that a valid Google Maps API key is entered in Divi Theme Options under the Integration tab. The API key must have the Maps JavaScript API and Geocoding API enabled in the Google Cloud Console.
    - Check the browser console for API error messages such as "ApiNotActivatedMapError" or "InvalidKeyMapError" — these indicate configuration issues with the API key.
    - Ensure the Google Cloud project associated with the API key has billing enabled, as Google requires an active billing account for Maps API usage.
    - Clear your browser cache and any page caching plugins to load the latest version of the page.

!!! warning "Pins Not Appearing at Correct Locations"
    If map pins are misplaced or not showing at all:

    - Double-check the address entered for each pin. The Geocoding API converts addresses to coordinates, so an incomplete or ambiguous address may resolve to an unexpected location.
    - Try entering the full address including street number, city, state/province, and country for the most accurate pin placement.
    - If a pin does not appear, open the pin settings and verify that the address field is not empty and that the pin has not been accidentally deleted.

!!! warning "Map Loads Slowly or Causes Layout Shift"
    If the map takes a long time to appear or pushes content around as it loads:

    - Set an explicit height on the map container using the Design tab sizing controls. This reserves space in the layout before the map loads, preventing content shift.
    - Consider lazy-loading the map by placing it lower on the page so it only initializes when the user scrolls near it.
    - If the page has multiple maps, each one makes additional API calls — consolidate locations into a single map with multiple pins where possible.

## Related

- [Fullwidth Map](fullwidth-map.md) — Display a Google Map that spans the entire browser width
