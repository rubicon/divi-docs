---
title: "Hooks & Filters"
category: api
tags: [hooks, filters, actions, php, javascript, development, extensibility]
related: [custom-modules]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/developers/"
---

# Hooks & Filters

Divi 5 provides PHP action hooks, PHP filter hooks, and JavaScript event hooks that let developers extend and customize every aspect of the Builder, modules, and front-end rendering.

## Overview

Divi's hook system follows WordPress conventions: **actions** let you inject code at specific execution points, while **filters** let you modify data as it passes through the rendering pipeline. On the JavaScript side, Divi fires custom DOM events that extensions can listen for to interact with the Visual Builder's React-based UI.

Hooks are the primary extension mechanism for Divi 5. Whether you need to add markup before or after a module renders, modify a module's output HTML, inject scripts into the Builder, or register entirely new modules, the hook system is where you start.

Understanding which hooks fire and when is essential for building reliable Divi extensions. This reference catalogs the most important hooks organized by type and context.

## PHP Action Hooks

Action hooks let you execute code at specific points during Divi's rendering lifecycle. They do not return a value.

### Template Action Hooks

These hooks fire during theme template rendering and control where custom markup appears on the page.

| Hook Name | Location | Description |
|-----------|----------|-------------|
| `et_before_main_content` | Before main content area | Fires before the primary content wrapper. Use for banners, breadcrumbs, or full-width elements above the page content. |
| `et_after_main_content` | After main content area | Fires after the primary content wrapper closes. Use for footers, CTAs, or scripts that depend on page content. |
| `et_header_top` | Top of header | Fires at the very top of the header area, before the logo and navigation. |
| `et_before_page_builder` | Before Builder output | Fires immediately before the Divi Builder renders its content on a page. |
| `et_after_page_builder` | After Builder output | Fires immediately after the Divi Builder content finishes rendering. |
| `et_head_meta` | Inside `<head>` | Fires inside the document head. Use for custom meta tags, preload hints, or structured data. |
| `et_body_top` | After opening `<body>` | Fires immediately after the `<body>` tag opens. Use for tracking pixels or skip-navigation links. |
| `et_before_content` | Before post content | Fires before the post/page content area within the template. |
| `et_after_content` | After post content | Fires after the post/page content area. |

#### Example: Add a breadcrumb bar above page content

```php
<?php
add_action( 'et_before_main_content', 'my_custom_breadcrumbs' );

function my_custom_breadcrumbs() {
    if ( ! is_front_page() ) {
        echo '<nav class="my-breadcrumbs" aria-label="Breadcrumb">';
        echo '<a href="' . esc_url( home_url( '/' ) ) . '">Home</a>';
        echo ' &raquo; ';
        the_title( '<span>', '</span>' );
        echo '</nav>';
    }
}
```

#### Example: Inject a site-wide announcement banner

```php
<?php
add_action( 'et_header_top', 'my_announcement_banner' );

function my_announcement_banner() {
    $message = get_option( 'my_announcement_text', '' );
    if ( empty( $message ) ) {
        return;
    }
    printf(
        '<div class="my-announcement-banner" role="alert">%s</div>',
        wp_kses_post( $message )
    );
}
```

### Header & Footer Action Hooks

| Hook Name | Location | Description |
|-----------|----------|-------------|
| `et_html_top_header` | Top header bar | Fires inside the secondary/top header bar area. |
| `et_html_main_header` | Main header | Fires inside the main header container. |
| `et_before_nav` | Before navigation | Fires before the primary navigation menu renders. |
| `et_after_nav` | After navigation | Fires after the primary navigation menu renders. |
| `et_footer_top` | Top of footer | Fires at the top of the footer widget area. |
| `et_footer_bottom` | Bottom of footer | Fires at the very bottom of the footer, after widgets and credits. |

#### Example: Add a phone number to the top header

```php
<?php
add_action( 'et_html_top_header', 'my_header_phone_number' );

function my_header_phone_number() {
    echo '<div class="header-phone">';
    echo '<a href="tel:+15551234567">Call Us: (555) 123-4567</a>';
    echo '</div>';
}
```

### Builder Lifecycle Action Hooks

| Hook Name | When It Fires | Description |
|-----------|---------------|-------------|
| `et_builder_ready` | Builder initialized | Fires after the Divi Builder framework has loaded and is ready. Use for registering custom module types. |
| `et_builder_post_content_capability_check` | Permission check | Fires during the capability check for Builder content. |
| `et_builder_modules_loaded` | All modules registered | Fires after all built-in Builder modules have been registered. Safe to reference any built-in module class. |
| `et_builder_framework_loaded` | Framework loaded | Fires after the Builder framework (not UI) has fully loaded. |
| `et_save_post` | Post saved | Fires after a post containing Builder content is saved. Receives `$post_id`. |

#### Example: Run code after Builder modules are available

```php
<?php
add_action( 'et_builder_modules_loaded', 'my_after_modules_loaded' );

function my_after_modules_loaded() {
    // All built-in modules are now registered.
    // Safe to extend or modify their behavior.
    if ( class_exists( 'ET_Builder_Module_Blurb' ) ) {
        // Interact with the Blurb module class
    }
}
```

## PHP Filter Hooks

Filter hooks let you modify data and return the modified result. Always return a value from your filter callback.

### Module Output Filters

| Hook Name | Type | Parameters | Description |
|-----------|------|------------|-------------|
| `et_module_shortcode_output` | filter | `$output`, `$render_slug`, `$module` | Modify the final HTML output of any Divi module. The most powerful module filter. |
| `et_builder_module_settings_migrations` | filter | `$migrations` | Modify the list of settings migration classes that run when Divi updates module data formats. |
| `et_pb_module_shortcode_attributes` | filter | `$attrs`, `$atts`, `$render_slug`, `$address`, `$content` | Modify a module's shortcode attributes before rendering. |
| `et_builder_main_css_file_size_kb` | filter | `$size_kb` | Set the maximum inline CSS file size (in KB) before Divi writes to an external stylesheet. |
| `et_builder_get_child_modules` | filter | `$child_modules`, `$post_type` | Modify the list of registered child modules for a given post type. |
| `et_builder_get_parent_modules` | filter | `$parent_modules`, `$post_type` | Modify the list of registered parent modules for a given post type. |

#### Example: Modify module output for a specific module

```php
<?php
add_filter( 'et_module_shortcode_output', 'my_modify_blurb_output', 10, 3 );

function my_modify_blurb_output( $output, $render_slug, $module ) {
    // Only modify Blurb modules
    if ( 'et_pb_blurb' !== $render_slug ) {
        return $output;
    }

    // Wrap the blurb output in a custom container
    $output = sprintf(
        '<div class="my-blurb-wrapper" data-module-id="%s">%s</div>',
        esc_attr( $module->props['module_id'] ?? '' ),
        $output
    );

    return $output;
}
```

#### Example: Add a custom attribute to all modules

```php
<?php
add_filter( 'et_pb_module_shortcode_attributes', 'my_add_custom_attr', 10, 5 );

function my_add_custom_attr( $attrs, $atts, $render_slug, $address, $content ) {
    // Add a data attribute based on the module's position
    $attrs['data-position'] = $address;
    return $attrs;
}
```

### Builder Configuration Filters

| Hook Name | Type | Parameters | Description |
|-----------|------|------------|-------------|
| `et_builder_post_types` | filter | `$post_types` | Add or remove post types where the Divi Builder is available. |
| `et_builder_always_enabled` | filter | `$enabled` (bool) | Force the Builder to always be enabled on supported post types. |
| `et_builder_enable_classic_editor` | filter | `$enable` (bool) | Whether to show the classic editor option alongside the Builder. |
| `et_pb_builder_post_content_capability` | filter | `$capability` | Set the capability required to use the Builder (default: `edit_posts`). |
| `et_builder_load_requests` | filter | `$load_requests` | Control which AJAX requests trigger the Builder framework to load. |

#### Example: Enable the Builder on a custom post type

```php
<?php
add_filter( 'et_builder_post_types', 'my_add_builder_to_cpt' );

function my_add_builder_to_cpt( $post_types ) {
    $post_types[] = 'portfolio';
    $post_types[] = 'service';
    return $post_types;
}
```

### Content & Asset Filters

| Hook Name | Type | Parameters | Description |
|-----------|------|------------|-------------|
| `et_builder_inner_content_class` | filter | `$classes` | Modify the CSS classes on the inner content wrapper. |
| `et_builder_add_builder_content_wrapper` | filter | `$add_wrapper` (bool) | Whether to wrap Builder content in the outer wrapper div. |
| `et_pb_all_button_icons_in_one_font` | filter | `$combine` (bool) | Whether to combine all button icons into a single font file. |
| `et_global_assets_list` | filter | `$assets` | Modify the list of global CSS/JS assets Divi loads. |
| `et_required_module_assets` | filter | `$assets`, `$render_slug` | Modify the assets required by a specific module. |

#### Example: Add a custom CSS class to the Builder content wrapper

```php
<?php
add_filter( 'et_builder_inner_content_class', 'my_add_content_class' );

function my_add_content_class( $classes ) {
    $classes[] = 'my-custom-layout';
    return $classes;
}
```

## JavaScript Hooks

Divi 5's Visual Builder runs as a React application and communicates with extensions via custom DOM events. The primary entry point is the `et_builder_api_ready` event, which fires when the Builder's JavaScript API is fully initialized.

### The `et_builder_api_ready` Event

This is the single most important JavaScript hook. It fires once when the Visual Builder loads and passes the `API` object to registered callbacks.

```javascript
// Listen for the Builder API to be ready
jQuery(window).on('et_builder_api_ready', function(event, API) {
    // The API object is now available
    console.log('Divi Builder API is ready');

    // Register custom modules
    API.Modules.register(MyCustomModules);

    // Check if a module is already registered
    if (API.isRegistered('my_custom_module')) {
        console.log('Module is registered');
    }
});
```

### JavaScript Hook Reference

| Event Name | Fires When | Callback Parameters | Description |
|------------|-----------|---------------------|-------------|
| `et_builder_api_ready` | Builder JS fully loaded | `event`, `API` | Primary entry point. Use to register modules and access the Builder API. |
| `et_fb_module_init` | Module instance created | `event`, `moduleData` | Fires each time a module instance is initialized in the Visual Builder. |
| `et_fb_section_content_change` | Section content modified | `event`, `sectionData` | Fires when content inside a section changes. |
| `et_builder_after_save` | Layout saved | `event`, `saveData` | Fires after the Builder successfully saves content. |
| `et_fb_page_loaded` | Page fully loaded in VB | `event` | Fires after the Visual Builder finishes loading a page. |
| `et_fb_module_settings_changed` | Settings modified | `event`, `moduleSlug`, `settings` | Fires when any module's settings are changed in the settings modal. |

### The API Object

The `API` object passed to `et_builder_api_ready` callbacks contains these namespaces:

#### `API.Modules`

Manages custom module registration.

```javascript
// Register a single module
API.Modules.register([MyModule]);

// Register multiple modules at once
API.Modules.register([ModuleOne, ModuleTwo, ModuleThree]);
```

#### `API.registerModules(modules)`

Convenience wrapper for `API.Modules.register()`.

```javascript
API.registerModules([MyModule]);
```

#### `API.isRegistered(slug)`

Check whether a module with the given slug is already registered. Returns `boolean`.

```javascript
if (!API.isRegistered('my_custom_cta')) {
    API.Modules.register([MyCustomCTA]);
}
```

#### `API.Utils`

Utility functions available to custom modules.

| Method | Returns | Description |
|--------|---------|-------------|
| `Utils._()` | various | Lodash utility library. Full Lodash API available. |
| `Utils.classnames()` | `string` | Generates className strings from objects/strings. Falsy values are excluded. |
| `Utils.decodeOptionListValue(encoded_value)` | `object` | Decodes a string value from the `option_list` module setting field type. |
| `Utils.fontnameToClass(font_name)` | `string` | Returns the CSS class name for a Google Font. |
| `Utils.linkRel(saved_value)` | `string` | Generates the `rel` attribute value for links based on saved module settings. |
| `Utils.maybeLoadFont(font_name)` | `void` | Loads a Google Font if it has not already been loaded on the page. |
| `Utils.processFontIcon(icon, is_down_icon)` | `string` | Generates HTML for a font-based icon from a saved icon value. |
| `Utils.setElementFont(font_data, use_important, default_values)` | `string` | Generates font-related CSS properties from saved font settings data. |
| `Utils.hasValue(value)` | `boolean` | Checks whether a value is printable (non-empty string, not undefined, not null). |
| `Utils.generateStyles(moduleArgs)` | `array` | Generates responsive and sticky-state CSS styles for a module. |

#### Example: Using API.Utils in a custom module render

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    const { Utils } = API;

    const MyModule = {
        slug: 'my_info_box',
        name: 'Info Box',

        render: function(props) {
            const { title, icon, font_name, link_url } = props;

            // Load the selected Google Font
            if (font_name) {
                Utils.maybeLoadFont(font_name);
            }

            // Process the icon
            const iconHtml = icon ? Utils.processFontIcon(icon, false) : '';

            // Build class names conditionally
            const classes = Utils.classnames(
                'my-info-box',
                { 'has-icon': !!icon },
                { 'has-link': !!link_url }
            );

            // Generate link rel attribute
            const relAttr = link_url ? Utils.linkRel('nofollow') : '';

            // Check if title has a value
            const titleHtml = Utils.hasValue(title)
                ? `<h3 class="my-info-box__title">${title}</h3>`
                : '';

            return `
                <div class="${classes}">
                    ${iconHtml ? `<div class="my-info-box__icon">${iconHtml}</div>` : ''}
                    ${titleHtml}
                </div>
            `;
        }
    };

    API.Modules.register([MyModule]);
});
```

## Combining PHP and JavaScript Hooks

Most Divi extensions use both PHP and JavaScript hooks together. PHP handles the server-side module definition and rendering, while JavaScript handles the Visual Builder preview.

### Example: Full extension using both hook types

**PHP side** (loads the JS and defines the module):

```php
<?php
// Enqueue the custom module JS for the Visual Builder
add_action( 'wp_enqueue_scripts', 'my_extension_enqueue_scripts' );

function my_extension_enqueue_scripts() {
    if ( et_core_is_fb_enabled() ) {
        wp_enqueue_script(
            'my-custom-modules',
            plugin_dir_url( __FILE__ ) . 'js/custom-modules.js',
            array( 'jquery', 'react', 'react-dom' ),
            '1.0.0',
            true
        );
    }
}

// Register the server-side module
add_action( 'et_builder_ready', 'my_register_builder_modules' );

function my_register_builder_modules() {
    if ( ! class_exists( 'ET_Builder_Module' ) ) {
        return;
    }
    require_once plugin_dir_path( __FILE__ ) . 'modules/InfoBox.php';
}
```

**JavaScript side** (Visual Builder preview):

```javascript
// js/custom-modules.js
jQuery(window).on('et_builder_api_ready', function(event, API) {
    API.Modules.register([
        {
            slug: 'my_info_box',
            name: 'Info Box',
            render: function(props) {
                return '<div class="my-info-box">' + props.title + '</div>';
            }
        }
    ]);
});
```

## Hook Execution Order

Understanding when hooks fire helps you choose the right one:

1. `et_builder_framework_loaded` -- Builder PHP framework loaded
2. `et_builder_modules_loaded` -- All built-in modules registered
3. `et_builder_ready` -- Builder fully initialized (register custom modules here)
4. `et_before_main_content` -- Template rendering begins
5. `et_before_page_builder` -- Builder content about to render
6. `et_module_shortcode_output` -- Each module renders (filter)
7. `et_after_page_builder` -- Builder content finished rendering
8. `et_after_main_content` -- Template rendering ends
9. `et_builder_api_ready` (JS) -- Visual Builder JS loaded (client-side only)

## Best Practices

!!! tip "Always Check Context"
    Many hooks fire on both the front-end and in the Visual Builder. Use `et_core_is_fb_enabled()` to detect the Visual Builder, and `is_admin()` to detect the WordPress admin.

!!! warning "Return Values from Filters"
    Always return a value from filter callbacks. Forgetting to return will cause the filtered content to become `null`, which can break rendering.

```php
<?php
// WRONG -- missing return statement
add_filter( 'et_module_shortcode_output', function( $output ) {
    $output .= '<!-- modified -->';
    // BUG: no return!
});

// CORRECT
add_filter( 'et_module_shortcode_output', function( $output ) {
    $output .= '<!-- modified -->';
    return $output;
});
```

!!! tip "Priority Matters"
    Use the third parameter of `add_action()` / `add_filter()` to control execution order. Lower numbers run first. Default is `10`.

```php
<?php
// Run early (before most other callbacks)
add_filter( 'et_module_shortcode_output', 'my_early_filter', 5, 3 );

// Run late (after most other callbacks)
add_filter( 'et_module_shortcode_output', 'my_late_filter', 99, 3 );
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 5 retains most hooks from Divi 4 for backward compatibility, but some hooks have been deprecated or replaced. The JavaScript API (`et_builder_api_ready`) is the same event name but the `API` object has expanded capabilities in Divi 5.

## Troubleshooting

!!! warning "Hook callback not firing"
    **Symptom:** Your `add_action()` or `add_filter()` callback never executes.

    **Possible causes:**

    - The hook fires before your code loads. Move your `add_action()` call to an earlier WordPress hook (e.g., `init` or `plugins_loaded`).
    - You are hooking into a Visual Builder-only event but testing on the front-end (or vice versa).
    - The hook name is misspelled. Hook names are case-sensitive.

    **Fix:** Add a temporary `error_log()` call inside your callback to confirm whether it runs. Check `wp-content/debug.log` with `WP_DEBUG` and `WP_DEBUG_LOG` enabled.

!!! warning "`et_builder_api_ready` not firing in the Visual Builder"
    **Symptom:** Your JavaScript event listener never fires.

    **Possible causes:**

    - Your script is not enqueued with the correct dependencies (`jquery` is required).
    - Your script loads before the Builder JS. Ensure `wp_enqueue_script()` sets `$in_footer` to `true`.
    - You are testing on the front-end, not in the Visual Builder. This event only fires inside the VB.

    **Fix:** Confirm you are in the Visual Builder (URL contains `?et_fb=1`). Check the browser console for script loading errors.

## Related

- [Custom Modules](../api/custom-modules.md)
- [CSS Class Reference](../css-reference/class-reference.md)
- [CSS in Divi 5 Playbook](../playbooks/css-in-divi.md)
- [Visual Builder](../builder/visual-builder.md)
