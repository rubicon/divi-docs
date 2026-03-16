---
title: "JavaScript API"
description: "Divi 5 Builder JavaScript API reference — complete API object documentation, module registration, Utils methods, events, and React component patterns."
category: api
tags: [javascript, api, builder, react, modules, events, utils]
related: [hooks-filters, custom-modules, divi-data-registry]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/8657536-divi-builder-javascript-api"
---

# JavaScript API

Complete reference for the Divi 5 Builder JavaScript API — the client-side interface for registering custom modules, accessing utility functions, and responding to Visual Builder lifecycle events.

!!! abstract "Quick Reference"
    **Primary entry point:** `jQuery(window).on('et_builder_api_ready', function(event, API) { ... })`
    **Module registration:** `API.Modules.register([{ slug, name, render }])`
    **Utility namespace:** `API.Utils` — classnames, font loading, icon processing, style generation
    **Key events:** `et_builder_api_ready`, `et_fb_module_init`, `et_builder_after_save`, `et_fb_page_loaded`
    **Context:** Runs in the parent window of the Visual Builder's dual-frame architecture

## Overview

The Divi 5 Builder JavaScript API is the client-side counterpart to the PHP module system. It provides the interface for rendering module previews inside the Visual Builder (VB), registering custom modules, accessing shared utility functions, and responding to builder lifecycle events.

The API is delivered as a single `API` object passed to callbacks of the `et_builder_api_ready` jQuery event. This event fires once per Visual Builder session after the builder's React application has fully initialized. All custom module JavaScript code should be wrapped inside this event handler.

This page expands on the summary in [Hooks & Filters](hooks-filters.md) with full signatures, parameter types, return values, and working examples for every documented method and event.

## The API Object

The `API` object is the root namespace for all builder JavaScript functionality. It is passed as the second argument to `et_builder_api_ready` callbacks.

### Top-Level Properties

| Property | Type | Description |
|----------|------|-------------|
| `API.Modules` | `object` | Module registration namespace. Contains `register()`. |
| `API.Utils` | `object` | Utility functions for rendering — classnames, fonts, icons, styles. |
| `API.registerModules(modules)` | `function` | Convenience wrapper for `API.Modules.register()`. |
| `API.isRegistered(slug)` | `function` | Check if a module slug is already registered. Returns `boolean`. |

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    console.log(typeof API.Modules);        // "object"
    console.log(typeof API.Utils);           // "object"
    console.log(typeof API.registerModules); // "function"
    console.log(typeof API.isRegistered);    // "function"
});
```

## API.Modules.register()

Registers one or more custom modules with the Visual Builder. Each module object defines how the module renders its preview inside the VB.

### Signature

```javascript
API.Modules.register(modules: ETBuilderModule[]): void
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `modules` | `ETBuilderModule[]` | Yes | Array of module definition objects. |

### ETBuilderModule Object

Each object in the array must conform to this structure:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `slug` | `string` | Yes | Unique identifier. **Must match the PHP `$slug` property exactly** (case-sensitive). |
| `name` | `string` | Yes | Human-readable display name shown in the Visual Builder UI. |
| `render` | `function(props): string\|ReactElement` | Yes | Receives the module's current attributes as `props`. Returns an HTML string or React element for the VB preview. |
| `inheritedModule` | `string` | No | ⚠️ Observed — Slug of a built-in module to inherit styles and behavior from. |

### The `props` Object

The `render` function receives a `props` object containing:

| Property | Type | Description |
|----------|------|-------------|
| `{field_name}` | `mixed` | Every field defined in `get_fields()` on the PHP side, keyed by field name. Values are strings unless processed. |
| `className` | `string` | ⚠️ Observed — Divi-generated CSS classes for the module instance (e.g., `et_pb_module et_pb_custom_0`). |
| `moduleId` | `string` | ⚠️ Observed — The ephemeral module UUID for this instance. Changes on every page reload. |
| `orderIndex` | `number` | ⚠️ Observed — Positional index of the module within its parent. |
| `content` | `string` | ⚠️ Observed — The module's inner content (for modules using `tiny_mce` fields or child content). |

### Example: Register a simple module

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    var AlertBox = {
        slug: 'my_alert_box',
        name: 'Alert Box',

        render: function(props) {
            var type = props.alert_type || 'info';
            var message = props.message || '';

            return (
                '<div class="my-alert-box my-alert-box--' + type + '">' +
                    '<strong>' + type.toUpperCase() + ':</strong> ' +
                    message +
                '</div>'
            );
        }
    };

    API.Modules.register([AlertBox]);
});
```

### Example: Register multiple modules at once

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    var PricingCard = {
        slug: 'my_pricing_card',
        name: 'Pricing Card',
        render: function(props) {
            return '<div class="my-pricing">' + props.plan_name + ': $' + props.price + '</div>';
        }
    };

    var TestimonialCard = {
        slug: 'my_testimonial_card',
        name: 'Testimonial Card',
        render: function(props) {
            return '<blockquote class="my-testimonial">' + props.quote + '</blockquote>';
        }
    };

    API.Modules.register([PricingCard, TestimonialCard]);
});
```

### Example: Guard against duplicate registration

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    if (!API.isRegistered('my_pricing_card')) {
        API.Modules.register([PricingCard]);
    }
});
```

## API.Utils Methods

The `Utils` namespace provides helper functions for common rendering tasks. These are available inside `render()` functions and anywhere the `API` object is in scope.

### Utils._()

Access the full Lodash utility library.

```javascript
Utils._(): LodashStatic
```

**Returns:** The Lodash library object. All standard Lodash methods are available.

```javascript
// Sort an array of items
var sorted = API.Utils._().sortBy(items, 'order');

// Remove duplicates
var unique = API.Utils._().uniq(tags);

// Deep clone an object
var copy = API.Utils._().cloneDeep(originalData);

// Check if a value is empty
var empty = API.Utils._().isEmpty(someValue);
```

### Utils.classnames()

Generates a space-separated CSS class string from a mix of strings, objects, and arrays. Falsy values are excluded. Follows the [classnames](https://github.com/JedWatson/classnames) npm package API.

```javascript
Utils.classnames(...args: Array<string | object | Array>): string
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `...args` | `string \| object \| Array` | Any number of class name sources. Object keys with truthy values are included. |

**Returns:** `string` — space-separated class names.

```javascript
var classes = API.Utils.classnames(
    'my-module',                          // always included
    { 'my-module--active': isActive },    // conditional
    { 'my-module--large': size === 'lg' },
    props.className                       // Divi's generated classes
);
// Result: "my-module my-module--active et_pb_module et_pb_custom_0"
```

### Utils.hasValue()

Checks whether a value is "printable" — a non-empty string that is not `undefined` or `null`.

```javascript
Utils.hasValue(value: any): boolean
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `any` | The value to check. |

**Returns:** `boolean` — `true` if the value is a non-empty, non-null, non-undefined string.

```javascript
API.Utils.hasValue('Hello');     // true
API.Utils.hasValue('');          // false
API.Utils.hasValue(undefined);   // false
API.Utils.hasValue(null);        // false
API.Utils.hasValue(0);           // false (it's not a printable string)
```

### Utils.processFontIcon()

Converts a saved Divi icon value into the rendered HTML character for a font-based icon.

```javascript
Utils.processFontIcon(icon: string, is_down_icon?: boolean): string
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `icon` | `string` | — | The icon value as stored in module settings (e.g., `'%%1%%'`). |
| `is_down_icon` | `boolean` | `false` | Whether this is a "down" arrow icon variant. |

**Returns:** `string` — The HTML entity or character to render the icon inside a `.et-pb-icon` element.

```javascript
var iconChar = API.Utils.processFontIcon(props.icon_name, false);
var html = '<span class="et-pb-icon">' + iconChar + '</span>';
```

### Utils.maybeLoadFont()

Loads a Google Font dynamically by injecting a `<link>` stylesheet if the font is not already loaded on the page. Safe to call multiple times — subsequent calls for the same font are no-ops.

```javascript
Utils.maybeLoadFont(font_name: string): void
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `font_name` | `string` | The Google Font family name (e.g., `'Roboto'`, `'Open Sans'`). |

**Returns:** `void`

```javascript
if (props.heading_font) {
    API.Utils.maybeLoadFont(props.heading_font);
}
```

### Utils.fontnameToClass()

Converts a Google Font family name to a CSS class name for Divi's font system.

```javascript
Utils.fontnameToClass(font_name: string): string
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `font_name` | `string` | The font family name. |

**Returns:** `string` — CSS class name.

```javascript
var fontClass = API.Utils.fontnameToClass('Open Sans');
// Returns something like "et_gf_open_sans"
```

### Utils.linkRel()

Generates the `rel` attribute value for a link based on saved module settings.

```javascript
Utils.linkRel(saved_value: string): string
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `saved_value` | `string` | The saved link relationship value from module settings. |

**Returns:** `string` — A properly formatted `rel` attribute value (e.g., `"nofollow noopener"`).

```javascript
var rel = API.Utils.linkRel(props.link_rel);
if (rel) {
    linkHtml = '<a href="' + url + '" rel="' + rel + '">' + text + '</a>';
}
```

### Utils.setElementFont()

Generates CSS font properties from Divi's saved font settings data structure.

```javascript
Utils.setElementFont(font_data: object, use_important?: boolean, default_values?: object): string
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `font_data` | `object` | — | The font settings object from module attributes. |
| `use_important` | `boolean` | `false` | Whether to append `!important` to each CSS declaration. |
| `default_values` | `object` | `{}` | Default values to use when settings are not explicitly set. |

**Returns:** `string` — CSS declarations for font-family, font-weight, font-style, text-transform, text-decoration, and line-height.

```javascript
var fontCss = API.Utils.setElementFont(props.title_font_data, false, {});
// Returns: "font-family: 'Roboto', sans-serif; font-weight: 700;"
```

### Utils.decodeOptionListValue()

Decodes a string value from Divi's `option_list` field type into a structured object.

```javascript
Utils.decodeOptionListValue(encoded_value: string): object
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `encoded_value` | `string` | The encoded string from an `option_list` field. |

**Returns:** `object` — Decoded key-value pairs.

```javascript
var listData = API.Utils.decodeOptionListValue(props.items);
// Process the decoded list items
```

### Utils.generateStyles()

Generates responsive and sticky-state CSS styles for a module attribute. Handles desktop, tablet, phone, and sticky breakpoints automatically.

```javascript
Utils.generateStyles(moduleArgs: object): array
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `moduleArgs` | `object` | Configuration object (see properties below). |

**`moduleArgs` properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `attrs` | `object` | Yes | The module's props/attributes object. |
| `name` | `string` | Yes | The module slug. |
| `selector` | `string` | Yes | CSS selector using `%%order_class%%` placeholder. |
| `attr` | `string` | Yes | The attribute name to generate styles for. |
| `cssProperty` | `string` | Yes | The CSS property name (e.g., `'font-size'`, `'color'`). |

**Returns:** `array` — Style declarations for all responsive breakpoints.

```javascript
var styles = API.Utils.generateStyles({
    attrs: props,
    name: 'my_info_box',
    selector: '%%order_class%% .my-info-box__title',
    attr: 'title_font_size',
    cssProperty: 'font-size',
});
```

## Event System

Divi 5's Visual Builder communicates with extensions via custom jQuery events on the `window` object. Events fire at specific points in the builder lifecycle.

### et_builder_api_ready

The primary entry point for all builder JavaScript extensions. Fires once when the Visual Builder's React application has fully initialized and the API object is available.

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    // API object is now available
    // Register modules, set up event listeners, etc.
});
```

| Property | Value |
|----------|-------|
| **Fires** | Once per VB session, after full initialization |
| **Target** | `window` (parent frame) |
| **Parameters** | `event` (jQuery.Event), `API` (the Builder API object) |
| **Dependencies** | Requires `jquery` script dependency |

!!! warning "This event fires only in the Visual Builder"
    The `et_builder_api_ready` event fires only when the Visual Builder is active (URL contains `?et_fb=1`). It does not fire on the front end or in the WordPress admin. Gate your script loading with `et_core_is_fb_enabled()` in PHP to avoid loading unnecessary JavaScript.

### et_fb_module_init

Fires each time a module instance is initialized in the Visual Builder — when the page loads, when a new module is inserted, or when modules are reordered.

```javascript
jQuery(window).on('et_fb_module_init', function(event, moduleData) {
    console.log('Module initialized:', moduleData);
});
```

| Property | Value |
|----------|-------|
| **Fires** | Each time a module instance initializes |
| **Target** | `window` |
| **Parameters** | `event` (jQuery.Event), `moduleData` (object — module instance data) |

### et_builder_after_save

Fires after the Visual Builder successfully saves the page content.

```javascript
jQuery(window).on('et_builder_after_save', function(event, saveData) {
    console.log('Layout saved successfully');
    // Trigger cache purge, analytics event, etc.
});
```

| Property | Value |
|----------|-------|
| **Fires** | After a successful save operation |
| **Target** | `window` |
| **Parameters** | `event` (jQuery.Event), `saveData` (object — save operation metadata) |

### et_fb_page_loaded

Fires after the Visual Builder finishes loading a page into the iframe canvas.

```javascript
jQuery(window).on('et_fb_page_loaded', function(event) {
    console.log('VB page fully loaded');
});
```

| Property | Value |
|----------|-------|
| **Fires** | After the VB page canvas finishes loading |
| **Target** | `window` |
| **Parameters** | `event` (jQuery.Event) |

### et_fb_module_settings_changed

Fires when any module's settings are modified through the settings modal in the Visual Builder.

```javascript
jQuery(window).on('et_fb_module_settings_changed', function(event, moduleSlug, settings) {
    if (moduleSlug === 'my_custom_module') {
        console.log('My module settings changed:', settings);
    }
});
```

| Property | Value |
|----------|-------|
| **Fires** | When module settings are modified in the settings modal |
| **Target** | `window` |
| **Parameters** | `event` (jQuery.Event), `moduleSlug` (string), `settings` (object) |

### divi.module.loop.extractCustomAttributes

Allows plugins to register custom loop query attributes for Divi's loop modules (e.g., Blog, Portfolio). Added in the Divi 5 official release (February 2026).

```javascript
jQuery(window).on('divi.module.loop.extractCustomAttributes', function(event, attributes) {
    // Add custom query attributes
    attributes.my_custom_taxonomy = 'product_category';
    attributes.my_custom_meta_key = 'featured';
});
```

| Property | Value |
|----------|-------|
| **Fires** | When a loop module builds its query |
| **Target** | `window` |
| **Parameters** | `event` (jQuery.Event), `attributes` (object — mutable query attributes) |

!!! note "Server-side companion"
    This JavaScript event has a PHP companion filter `divi.loop.query_args` that modifies the actual `WP_Query` arguments on the server side. Both hooks are needed for a complete custom loop implementation. See [Hooks & Filters](hooks-filters.md) for the PHP filter reference.

## React Integration

Divi 5's Visual Builder is a React application. Module previews can use either HTML template strings or React elements.

### HTML Template Strings

The simplest approach — return an HTML string from `render()`. Divi injects this into the VB preview DOM.

```javascript
render: function(props) {
    return '<div class="my-module"><h3>' + props.title + '</h3></div>';
}
```

**Pros:** Simple, no build step required, works with plain JavaScript.
**Cons:** No React lifecycle methods, no interactive elements.

### ES6 Template Literals

A cleaner version of template strings using backtick syntax:

```javascript
render: function(props) {
    var { title, subtitle, icon } = props;
    var iconHtml = icon ? API.Utils.processFontIcon(icon, false) : '';

    return `
        <div class="my-module">
            ${iconHtml ? `<span class="et-pb-icon">${iconHtml}</span>` : ''}
            <h3 class="my-module__title">${title || ''}</h3>
            <p class="my-module__subtitle">${subtitle || ''}</p>
        </div>
    `;
}
```

### React Elements (JSX)

⚠️ Observed — For modules built with a build step (Webpack/Babel), you can return React elements directly. React and ReactDOM are available as global dependencies in the VB.

```javascript
// Requires a build step to compile JSX
render: function(props) {
    return React.createElement('div', { className: 'my-module' },
        React.createElement('h3', null, props.title),
        React.createElement('p', null, props.subtitle)
    );
}
```

Or with JSX (requires Babel):

```jsx
render: function(props) {
    return (
        <div className="my-module">
            <h3>{props.title}</h3>
            <p>{props.subtitle}</p>
        </div>
    );
}
```

### Accessing Module Attributes in Render

All fields defined in the PHP `get_fields()` method are available as properties on the `props` object, keyed by field name:

```javascript
render: function(props) {
    // Direct field access
    var title = props.title;                    // from 'text' field
    var bodyText = props.body_text;             // from 'tiny_mce' field
    var showIcon = props.use_icon;              // from 'yes_no_button' — value is 'on' or 'off'
    var bgColor = props.background_color;       // from 'color-alpha' field
    var imageUrl = props.image;                 // from 'upload' field

    // Yes/no buttons return strings, not booleans
    var iconVisible = showIcon === 'on';

    // Always guard against undefined values
    var safeTitle = title || 'Default Title';
}
```

### Responsive Value Handling

⚠️ Observed — When a field has `'mobile_options' => true` in PHP, responsive values are available via suffixed property names:

```javascript
render: function(props) {
    // Desktop value (default)
    var fontSize = props.title_font_size;

    // Tablet value
    var fontSizeTablet = props.title_font_size_tablet;

    // Phone value
    var fontSizePhone = props.title_font_size_phone;

    // Use Utils.generateStyles for automatic responsive CSS
    var styles = API.Utils.generateStyles({
        attrs: props,
        name: 'my_module',
        selector: '%%order_class%% .my-module__title',
        attr: 'title_font_size',
        cssProperty: 'font-size',
    });
}
```

## Global Objects in the Visual Builder

⚠️ Observed — The Visual Builder exposes several global objects across its dual-frame architecture. See [VB Architecture](../internals/vb-architecture.md) for the full internal structure.

### Parent Window Objects

| Object | Description |
|--------|-------------|
| `window.ET_Builder.API` | ⚠️ Observed — The same `API` object passed to `et_builder_api_ready`. Available globally after initialization. |
| `window.tinymce` | ⚠️ Observed — TinyMCE instances when a Text module is actively selected for editing. |

### Iframe Objects

Access the iframe via `document.querySelector('#et-vb-app-frame').contentWindow`:

| Object | Description |
|--------|-------------|
| `iframeWin.DIVI` | ⚠️ Observed — Builder configuration: `item_count`, `items_count`, `row_selector`. |
| `iframeWin.ET_Builder` | ⚠️ Observed — Builder API bridge: `API`, `Frames`, `Misc`. |
| `iframeWin.ETCloudApp` | ⚠️ Observed — Divi Cloud/Library interface: `retryUseLayout`, `setState`, `toggleTab`, `setCloudToken`. |
| `iframeWin.wp` | ⚠️ Observed — WordPress core: hooks, i18n, ajax, media. Note: `wp.data` stores are NOT initialized — see [Known Limitations](../playbooks/known-limitations.md#12-wpdata-is-not-available-in-the-visual-builder). |
| `iframeWin.et_common_data` | ⚠️ Observed — Configuration and i18n data. |
| `iframeWin.window.divi.data` | ⚠️ Observed — Divi's own read-only data registry. See [Divi Data Registry](divi-data-registry.md). |

!!! warning "Do not rely on iframe globals for production extensions"
    The iframe objects above are internal implementation details observed through browser DevTools. They are not part of the documented public API and may change without notice. For production code, use only the `API` object provided by `et_builder_api_ready`.

## Script Loading

To load JavaScript for the Visual Builder, enqueue your script conditionally using `et_core_is_fb_enabled()`.

### Basic Enqueue Pattern

```php
<?php
add_action( 'wp_enqueue_scripts', 'my_enqueue_vb_scripts' );

function my_enqueue_vb_scripts() {
    // Only load in the Visual Builder
    if ( ! function_exists( 'et_core_is_fb_enabled' ) || ! et_core_is_fb_enabled() ) {
        return;
    }

    wp_enqueue_script(
        'my-custom-modules',
        plugin_dir_url( __FILE__ ) . 'js/custom-modules.js',
        array( 'jquery', 'react', 'react-dom' ),  // Required dependencies
        '1.0.0',
        true  // MUST be true — load in footer
    );
}
```

### Key Requirements

| Requirement | Details |
|-------------|---------|
| **Conditional loading** | Always wrap in `et_core_is_fb_enabled()`. Do not load VB scripts on the front end. |
| **`jquery` dependency** | Required. The `et_builder_api_ready` event is dispatched via jQuery. |
| **`react` dependency** | Required if your render function returns React elements. Optional for HTML string rendering. |
| **`react-dom` dependency** | Required alongside `react` for React element rendering. |
| **`$in_footer = true`** | Required. The fifth parameter of `wp_enqueue_script()` must be `true`. Scripts loaded in the `<head>` execute before the builder initializes, causing `et_builder_api_ready` to never fire. |

### Passing PHP Data to JavaScript

Use `wp_localize_script()` to make server-side data available to your VB script:

```php
<?php
wp_localize_script( 'my-custom-modules', 'MyModuleData', array(
    'ajaxUrl'  => admin_url( 'admin-ajax.php' ),
    'nonce'    => wp_create_nonce( 'my_module_nonce' ),
    'siteUrl'  => home_url( '/' ),
    'settings' => get_option( 'my_module_settings', array() ),
) );
```

```javascript
// Available in your JS as a global object
jQuery(window).on('et_builder_api_ready', function(event, API) {
    console.log(MyModuleData.siteUrl);
    console.log(MyModuleData.settings);
});
```

## Troubleshooting

!!! warning "`et_builder_api_ready` never fires"
    **Symptom:** Your event listener callback never executes.

    **Possible causes:**

    - Script is not enqueued with `jquery` as a dependency.
    - `$in_footer` parameter is `false` or omitted — script loads before the builder initializes.
    - Not in the Visual Builder — this event only fires when `?et_fb=1` is in the URL.
    - Script has a syntax error — check the browser console for errors.

    **Fix:** Verify the URL contains `?et_fb=1`. Open DevTools Console and check for script loading errors. Confirm `wp_enqueue_script()` includes `array('jquery')` as the dependency and `true` as the fifth parameter.

!!! warning "Module renders on front end but is blank in the Visual Builder"
    **Symptom:** PHP `render()` works on the live site, but the VB shows an empty box.

    **Possible causes:**

    - The JavaScript `slug` does not match the PHP `$slug` exactly (case-sensitive).
    - `API.Modules.register()` was not called or was called with an empty array.
    - The `render` function throws an error — check the browser console.

    **Fix:** Verify the slug matches between PHP and JS. Add `console.log()` inside the render function to confirm it executes. Check the browser console for JavaScript errors.

!!! warning "`API.Utils` methods return unexpected results"
    **Symptom:** `Utils.processFontIcon()` returns an empty string, or `Utils.hasValue()` returns `false` for a value you expect to be valid.

    **Possible causes:**

    - The value passed is `undefined` because the field name does not match between PHP `get_fields()` and the `props` property name.
    - The icon value format has changed — Divi 5 icon values use the `'%%N%%'` format.

    **Fix:** Log `props` to the console and verify field names and value formats match your expectations.

!!! warning "Script loads on every page, not just the Visual Builder"
    **Symptom:** Your VB-only JavaScript loads on every frontend page, slowing down the site.

    **Fix:** Wrap `wp_enqueue_script()` in an `et_core_is_fb_enabled()` check. See the [Script Loading](#script-loading) section above.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The `et_builder_api_ready` event name is the same as in Divi 4, but the `API` object has expanded capabilities. Extensions built for Divi 4 may need updates to their `render()` functions due to changes in the props structure and available Utils methods.

!!! note "February 2026 Additions"
    The `divi.module.loop.extractCustomAttributes` JavaScript event and the `divi.loop.query_args` PHP filter were added in the Divi 5 official release (February 2026) for custom loop query support.

## Related

- [Hooks & Filters](hooks-filters.md) — PHP hooks, filter hooks, and the hook execution order
- [Custom Modules](custom-modules.md) — PHP class structure, field types, and `ET_Builder_Module`
- [Divi Data Registry](divi-data-registry.md) — Read-only module state access via `window.divi.data`
- [VB Architecture](../internals/vb-architecture.md) — Dual-frame structure and global objects
- [Known Limitations](../playbooks/known-limitations.md) — Gotchas including `wp.data` unavailability
- [JSON Attribute Map](../internals/json-attribute-map.md) — CSS-to-JSON path mapping for module attributes
- [Visual Builder](../builder/visual-builder.md) — Visual Builder feature documentation
