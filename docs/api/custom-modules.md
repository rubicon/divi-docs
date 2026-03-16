---
title: "Custom Modules"
description: "Divi 5 custom module development — ET_Builder_Module PHP class, JavaScript Visual Builder components, field types, advanced design options, and parent-child modules."
category: api
tags: [custom-modules, development, react, php, javascript, extensions, api]
related: [hooks-filters]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/developers/divi-module/"
---

# Custom Modules

Custom modules extend the Divi Builder with new content elements. A custom module consists of a PHP class that defines settings and server-side rendering, plus a JavaScript component that powers the Visual Builder preview.

!!! abstract "Quick Reference"
    **What this documents:** How to build custom Divi 5 modules using the `ET_Builder_Module` PHP class and the `et_builder_api_ready` JavaScript API.
    **Key components:** PHP class (`ET_Builder_Module`), JS component (`API.Modules.register()`), field types (text, tiny_mce, select, color-alpha, upload, etc.)
    **Extension entry point:** `divi_extensions_init` action hook, or `et_builder_ready` for standalone modules

## Overview

Divi's module system is built on the `ET_Builder_Module` PHP class and a React-based JavaScript API. Every module you see in the Builder -- Text, Blurb, Button, Image -- is an instance of this system. Custom modules follow the same pattern, giving your extensions first-class status alongside built-in modules.

Building a custom module involves three parts: a **PHP class** that extends `ET_Builder_Module` and defines the module's settings, slug, and server-rendered output; a **JavaScript component** registered through the `et_builder_api_ready` event that renders the module's preview in the Visual Builder; and optionally, **CSS files** that style the module on the front end.

Custom modules are delivered as WordPress plugins (or within a theme's `functions.php`, though plugins are strongly recommended). Elegant Themes provides a starter boilerplate called "Divi Extension" that scaffolds the required file structure.

## Creating a Divi Extension

The recommended way to create custom modules is inside a Divi Extension -- a WordPress plugin that follows Divi's expected file structure.

### Extension File Structure

```
my-divi-extension/
├── my-divi-extension.php          # Plugin bootstrap
├── includes/
│   ├── MyDiviExtension.php        # Main extension class
│   └── modules/
│       └── InfoBox/
│           ├── InfoBox.php        # Module PHP class
│           ├── InfoBox.jsx        # Module JS component (Visual Builder)
│           └── style.css          # Module front-end styles
├── scripts/
│   └── frontend.js                # Compiled JS bundle
├── styles/
│   └── style.css                  # Compiled CSS
└── readme.txt
```

### Plugin Bootstrap

The main plugin file initializes the extension and sets up autoloading:

```php
<?php
/*
Plugin Name: My Divi Extension
Plugin URI:  https://example.com/my-divi-extension
Description: Adds custom modules to the Divi Builder.
Version:     1.0.0
Author:      Your Name
License:     GPL-2.0+
Text Domain: my-divi-extension
*/

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Prevent direct access
}

define( 'MDE_VERSION', '1.0.0' );
define( 'MDE_PATH', plugin_dir_path( __FILE__ ) );
define( 'MDE_URL', plugin_dir_url( __FILE__ ) );

// Load the extension after Divi is ready
add_action( 'divi_extensions_init', 'mde_initialize_extension' );

function mde_initialize_extension() {
    require_once MDE_PATH . 'includes/MyDiviExtension.php';
}
```

### Main Extension Class

The extension class extends `DiviExtension` and handles module loading:

```php
<?php
// includes/MyDiviExtension.php

class MyDiviExtension extends DiviExtension {

    /**
     * The gettext domain for the extension.
     *
     * @var string
     */
    public $gettext_domain = 'my-divi-extension';

    /**
     * The extension's WP Plugin name.
     *
     * @var string
     */
    public $name = 'my-divi-extension';

    /**
     * The extension's version.
     *
     * @var string
     */
    public $version = MDE_VERSION;

    /**
     * Constructor.
     *
     * @param string $name Extension name.
     * @param array  $args Extension arguments.
     */
    public function __construct( $name = 'my-divi-extension', $args = array() ) {
        $this->plugin_dir     = MDE_PATH;
        $this->plugin_dir_url = MDE_URL;

        parent::__construct( $name, $args );
    }
}

new MyDiviExtension();
```

## Creating a Custom Module (PHP)

Every custom module is a PHP class that extends `ET_Builder_Module`. The class defines the module's identity, settings fields, and server-side HTML rendering.

### Minimal Module Example

```php
<?php
// includes/modules/InfoBox/InfoBox.php

class MDE_InfoBox extends ET_Builder_Module {

    // Required: unique identifier
    public $slug       = 'mde_info_box';
    public $vb_support = 'on';

    // Module metadata
    protected $module_credits = array(
        'module_uri' => 'https://example.com/info-box',
        'author'     => 'Your Name',
        'author_uri' => 'https://example.com',
    );

    /**
     * Initialize the module: set name, category, and other properties.
     */
    public function init() {
        $this->name = esc_html__( 'Info Box', 'my-divi-extension' );

        // Icon displayed in the module picker (use an ET icon code)
        $this->icon = 'N';

        // Where this module appears in the module picker
        $this->main_css_element = '%%order_class%%';
    }

    /**
     * Define the module's settings fields.
     *
     * @return array
     */
    public function get_fields() {
        return array(
            'title' => array(
                'label'       => esc_html__( 'Title', 'my-divi-extension' ),
                'type'        => 'text',
                'description' => esc_html__( 'The heading displayed in the info box.', 'my-divi-extension' ),
                'toggle_slug' => 'main_content',
            ),
            'body_text' => array(
                'label'       => esc_html__( 'Body', 'my-divi-extension' ),
                'type'        => 'tiny_mce',
                'description' => esc_html__( 'The body content of the info box.', 'my-divi-extension' ),
                'toggle_slug' => 'main_content',
            ),
            'icon_name' => array(
                'label'       => esc_html__( 'Icon', 'my-divi-extension' ),
                'type'        => 'select_icon',
                'description' => esc_html__( 'Choose an icon for the info box.', 'my-divi-extension' ),
                'toggle_slug' => 'main_content',
            ),
            'url' => array(
                'label'       => esc_html__( 'Link URL', 'my-divi-extension' ),
                'type'        => 'text',
                'description' => esc_html__( 'The URL the info box links to.', 'my-divi-extension' ),
                'toggle_slug' => 'link',
            ),
            'url_new_window' => array(
                'label'       => esc_html__( 'Open in New Tab', 'my-divi-extension' ),
                'type'        => 'yes_no_button',
                'options'     => array(
                    'off' => esc_html__( 'No', 'my-divi-extension' ),
                    'on'  => esc_html__( 'Yes', 'my-divi-extension' ),
                ),
                'default'     => 'off',
                'toggle_slug' => 'link',
            ),
            'background_color' => array(
                'label'       => esc_html__( 'Background Color', 'my-divi-extension' ),
                'type'        => 'color-alpha',
                'default'     => '#f5f5f5',
                'toggle_slug' => 'background',
                'tab_slug'    => 'advanced',
            ),
        );
    }

    /**
     * Render the module's front-end HTML.
     *
     * @param array  $attrs       Module attributes.
     * @param string $content     Module content (for child modules).
     * @param string $render_slug The module's slug.
     *
     * @return string
     */
    public function render( $attrs, $content, $render_slug ) {
        $title           = $this->props['title'];
        $body_text       = $this->props['body_text'];
        $icon_name       = $this->props['icon_name'];
        $url             = $this->props['url'];
        $url_new_window  = $this->props['url_new_window'];
        $bg_color        = $this->props['background_color'];

        // Build icon HTML
        $icon_html = '';
        if ( ! empty( $icon_name ) ) {
            $icon_html = sprintf(
                '<div class="mde-info-box__icon"><span class="et-pb-icon">%s</span></div>',
                esc_html( et_pb_process_font_icon( $icon_name ) )
            );
        }

        // Build title HTML
        $title_html = '';
        if ( ! empty( $title ) ) {
            $title_html = sprintf(
                '<h3 class="mde-info-box__title">%s</h3>',
                et_core_esc_previously( $title )
            );
        }

        // Build body HTML
        $body_html = '';
        if ( ! empty( $body_text ) ) {
            $body_html = sprintf(
                '<div class="mde-info-box__body">%s</div>',
                et_core_esc_previously( $body_text )
            );
        }

        // Apply background color as inline style
        if ( ! empty( $bg_color ) ) {
            ET_Builder_Element::set_style( $render_slug, array(
                'selector'    => '%%order_class%%',
                'declaration' => sprintf( 'background-color: %s;', esc_attr( $bg_color ) ),
            ) );
        }

        // Wrap in link if URL provided
        $target = 'on' === $url_new_window ? ' target="_blank" rel="noopener noreferrer"' : '';
        $inner  = $icon_html . $title_html . $body_html;

        if ( ! empty( $url ) ) {
            $inner = sprintf(
                '<a href="%s"%s class="mde-info-box__link">%s</a>',
                esc_url( $url ),
                $target,
                $inner
            );
        }

        return sprintf(
            '<div class="mde-info-box">%s</div>',
            $inner
        );
    }
}

new MDE_InfoBox();
```

## Module Settings Fields Reference

The `get_fields()` method returns an associative array where each key is a setting name and each value is a configuration array. Here are the available field types:

### Field Types

| Type | Description | Key Options |
|------|-------------|-------------|
| `text` | Single-line text input | `default`, `description` |
| `textarea` | Multi-line text input | `default`, `description` |
| `tiny_mce` | Rich text editor (TinyMCE) | `description` |
| `select` | Dropdown select | `options` (array), `default` |
| `yes_no_button` | Toggle switch | `options` (array of on/off labels), `default` |
| `multiple_buttons` | Button group | `options`, `default`, `toggleable` |
| `color-alpha` | Color picker with opacity | `default` |
| `upload` | Media library file upload | `upload_button_text`, `choose_text` |
| `select_icon` | Icon picker | -- |
| `range` | Slider with numeric input | `range_settings` (min, max, step), `default` |
| `font` | Font selector | -- |
| `text_align` | Text alignment buttons | `options`, `default` |
| `hidden` | Hidden field (not shown in UI) | `default` |
| `computed` | Computed field (JS only, no UI) | `computed_callback`, `computed_depends_on` |

### Field Configuration Keys

| Key | Type | Description |
|-----|------|-------------|
| `label` | string | The field label shown in the settings panel. |
| `type` | string | One of the field types above. |
| `description` | string | Help text displayed below the field. |
| `default` | mixed | Default value if the user has not set one. |
| `toggle_slug` | string | Groups fields under a toggle section (e.g., `main_content`, `link`). |
| `tab_slug` | string | Which tab the field appears on: `general` (Content), `advanced` (Design), `custom_css`. |
| `sub_toggle` | string | Sub-group within a toggle. |
| `show_if` | array | Conditionally show this field based on another field's value. |
| `show_if_not` | array | Conditionally hide this field. |
| `options` | array | Key-value pairs for `select`, `yes_no_button`, and `multiple_buttons` fields. |
| `option_category` | string | Category for the field: `basic_option`, `configuration`, `layout`, `color_option`, `font_option`. |
| `mobile_options` | bool | Enable responsive (per-device) values for this field. |
| `responsive` | bool | Alias for `mobile_options`. |
| `hover` | string | Enable hover state: `'tabs'` to show a hover tab. |

### Settings Field Visibility

Use `show_if` and `show_if_not` to conditionally display fields based on the value of other fields:

```php
<?php
public function get_fields() {
    return array(
        'use_icon' => array(
            'label'       => esc_html__( 'Use Icon', 'my-divi-extension' ),
            'type'        => 'yes_no_button',
            'options'     => array(
                'off' => esc_html__( 'No', 'my-divi-extension' ),
                'on'  => esc_html__( 'Yes', 'my-divi-extension' ),
            ),
            'default'     => 'off',
            'toggle_slug' => 'main_content',
        ),
        'icon_name' => array(
            'label'       => esc_html__( 'Icon', 'my-divi-extension' ),
            'type'        => 'select_icon',
            'toggle_slug' => 'main_content',
            // Only show this field when use_icon is "on"
            'show_if'     => array(
                'use_icon' => 'on',
            ),
        ),
        'image' => array(
            'label'       => esc_html__( 'Image', 'my-divi-extension' ),
            'type'        => 'upload',
            'toggle_slug' => 'main_content',
            // Show this field when use_icon is NOT "on"
            'show_if_not' => array(
                'use_icon' => 'on',
            ),
        ),
    );
}
```

## Custom CSS Fields

Divi's Advanced tab includes a "Custom CSS" toggle that lets users add CSS to specific parts of a module. Define these targets with `get_custom_css_fields_config()`:

```php
<?php
public function get_custom_css_fields_config() {
    return array(
        'info_box_container' => array(
            'label'    => esc_html__( 'Info Box Container', 'my-divi-extension' ),
            'selector' => '.mde-info-box',
        ),
        'info_box_icon' => array(
            'label'    => esc_html__( 'Icon', 'my-divi-extension' ),
            'selector' => '.mde-info-box__icon',
        ),
        'info_box_title' => array(
            'label'    => esc_html__( 'Title', 'my-divi-extension' ),
            'selector' => '.mde-info-box__title',
        ),
        'info_box_body' => array(
            'label'    => esc_html__( 'Body Text', 'my-divi-extension' ),
            'selector' => '.mde-info-box__body',
        ),
    );
}
```

## Advanced Features

### Adding Design Tab Options

Use the `advanced_fields` property to add Divi's built-in design controls (fonts, borders, box shadow, etc.) to your module:

```php
<?php
public function init() {
    $this->name = esc_html__( 'Info Box', 'my-divi-extension' );

    $this->advanced_fields = array(
        'fonts' => array(
            'title' => array(
                'label'       => esc_html__( 'Title', 'my-divi-extension' ),
                'css'         => array(
                    'main' => '%%order_class%% .mde-info-box__title',
                ),
                'font_size'   => array(
                    'default' => '24px',
                ),
                'line_height' => array(
                    'default' => '1.3em',
                ),
            ),
            'body' => array(
                'label'       => esc_html__( 'Body', 'my-divi-extension' ),
                'css'         => array(
                    'main' => '%%order_class%% .mde-info-box__body',
                ),
                'font_size'   => array(
                    'default' => '14px',
                ),
            ),
        ),
        'borders' => array(
            'default' => array(
                'css' => array(
                    'main' => array(
                        'border_radii'  => '%%order_class%% .mde-info-box',
                        'border_styles' => '%%order_class%% .mde-info-box',
                    ),
                ),
            ),
        ),
        'box_shadow' => array(
            'default' => array(
                'css' => array(
                    'main' => '%%order_class%% .mde-info-box',
                ),
            ),
        ),
        'margin_padding' => array(
            'css' => array(
                'important' => 'all',
            ),
        ),
        'background' => array(),
        'text' => false, // Disable the generic text options if not needed
    );
}
```

### Parent and Child Modules

Some modules contain child items (e.g., Pricing Table contains Pricing Items). Define parent-child relationships:

**Parent module:**

```php
<?php
class MDE_Feature_List extends ET_Builder_Module {
    public $slug       = 'mde_feature_list';
    public $vb_support = 'on';
    public $child_slug = 'mde_feature_list_item'; // Links to child module

    public function init() {
        $this->name             = esc_html__( 'Feature List', 'my-divi-extension' );
        $this->child_item_text  = esc_html__( 'Feature', 'my-divi-extension' );
    }

    public function get_fields() {
        return array(
            'title' => array(
                'label'       => esc_html__( 'List Title', 'my-divi-extension' ),
                'type'        => 'text',
                'toggle_slug' => 'main_content',
            ),
        );
    }

    public function render( $attrs, $content, $render_slug ) {
        return sprintf(
            '<div class="mde-feature-list">
                <h3 class="mde-feature-list__title">%s</h3>
                <ul class="mde-feature-list__items">%s</ul>
            </div>',
            esc_html( $this->props['title'] ),
            et_core_esc_previously( $this->content )
        );
    }
}

new MDE_Feature_List();
```

**Child module:**

```php
<?php
class MDE_Feature_List_Item extends ET_Builder_Module {
    public $slug                     = 'mde_feature_list_item';
    public $vb_support               = 'on';
    public $type                     = 'child';
    public $child_title_var          = 'title';
    public $child_title_fallback_var = 'title';

    public function init() {
        $this->name = esc_html__( 'Feature Item', 'my-divi-extension' );

        $this->advanced_fields = array(
            'text'       => false,
            'background' => false,
        );
    }

    public function get_fields() {
        return array(
            'title' => array(
                'label'       => esc_html__( 'Feature Title', 'my-divi-extension' ),
                'type'        => 'text',
                'toggle_slug' => 'main_content',
            ),
            'description' => array(
                'label'       => esc_html__( 'Description', 'my-divi-extension' ),
                'type'        => 'textarea',
                'toggle_slug' => 'main_content',
            ),
        );
    }

    public function render( $attrs, $content, $render_slug ) {
        return sprintf(
            '<li class="mde-feature-list__item">
                <strong>%s</strong> — %s
            </li>',
            esc_html( $this->props['title'] ),
            esc_html( $this->props['description'] )
        );
    }
}

new MDE_Feature_List_Item();
```

## JavaScript API: Visual Builder Module

The Visual Builder renders module previews using React components registered through the `et_builder_api_ready` event. Each module registered via `API.Modules.register()` must be an `ETBuilderModule` -- either a React component or a plain object with the required properties.

### ETBuilderModule Structure

| Property | Required | Type | Description |
|----------|----------|------|-------------|
| `slug` | Yes | `string` | Must match the PHP module's `$slug` property exactly. |
| `name` | Yes | `string` | Display name shown in the Visual Builder. |
| `render` | Yes | `function` | Receives `props` (the module's settings) and returns HTML or a React element. |

### Registering a Module

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    const InfoBox = {
        slug: 'mde_info_box',
        name: 'Info Box',

        render: function(props) {
            const {
                title,
                body_text,
                icon_name,
                url,
                url_new_window,
                background_color,
            } = props;

            const containerStyle = background_color
                ? `background-color: ${background_color};`
                : '';

            const target = url_new_window === 'on'
                ? ' target="_blank" rel="noopener noreferrer"'
                : '';

            let inner = '';

            if (icon_name) {
                inner += `<div class="mde-info-box__icon">
                    <span class="et-pb-icon">${API.Utils.processFontIcon(icon_name, false)}</span>
                </div>`;
            }

            if (API.Utils.hasValue(title)) {
                inner += `<h3 class="mde-info-box__title">${title}</h3>`;
            }

            if (API.Utils.hasValue(body_text)) {
                inner += `<div class="mde-info-box__body">${body_text}</div>`;
            }

            if (url) {
                inner = `<a href="${url}"${target} class="mde-info-box__link">${inner}</a>`;
            }

            return `<div class="mde-info-box" style="${containerStyle}">${inner}</div>`;
        }
    };

    // Register the module
    API.Modules.register([InfoBox]);
});
```

### Using API.Utils

The `API.Utils` object provides helper functions commonly needed when rendering modules.

#### Lodash (`Utils._()`)

Full Lodash library for data manipulation:

```javascript
const sortedItems = API.Utils._().sortBy(items, 'order');
const uniqueTags  = API.Utils._().uniq(tags);
```

#### Classnames (`Utils.classnames()`)

Build conditional CSS class strings:

```javascript
const classes = API.Utils.classnames(
    'mde-info-box',
    { 'mde-info-box--has-icon': !!icon_name },
    { 'mde-info-box--linked': !!url },
    props.className // Include Divi's generated classes
);
```

#### Font Loading (`Utils.maybeLoadFont()`)

Load a Google Font dynamically if it is not already present:

```javascript
if (props.title_font) {
    API.Utils.maybeLoadFont(props.title_font);
}
```

#### Style Generation (`Utils.generateStyles()`)

Generate responsive and sticky-state CSS for a module:

```javascript
const styles = API.Utils.generateStyles({
    attrs: props,
    name: 'mde_info_box',
    selector: '%%order_class%% .mde-info-box__title',
    attr: 'title_font_size',
    cssProperty: 'font-size',
});
```

## Complete Working Example

Here is a complete, minimal custom module delivered as a WordPress plugin.

### Plugin file: `my-divi-module/my-divi-module.php`

```php
<?php
/*
Plugin Name: My Divi Module
Description: A simple custom Divi Builder module.
Version:     1.0.0
Author:      Your Name
*/

if ( ! defined( 'ABSPATH' ) ) exit;

// Register the module when the Builder is ready
add_action( 'et_builder_ready', function() {
    if ( ! class_exists( 'ET_Builder_Module' ) ) {
        return;
    }

    class My_Simple_CTA extends ET_Builder_Module {
        public $slug       = 'my_simple_cta';
        public $vb_support = 'on';

        public function init() {
            $this->name             = 'Simple CTA';
            $this->main_css_element = '%%order_class%%';
        }

        public function get_fields() {
            return array(
                'heading' => array(
                    'label'       => 'Heading',
                    'type'        => 'text',
                    'default'     => 'Take Action Now',
                    'toggle_slug' => 'main_content',
                ),
                'button_text' => array(
                    'label'       => 'Button Text',
                    'type'        => 'text',
                    'default'     => 'Get Started',
                    'toggle_slug' => 'main_content',
                ),
                'button_url' => array(
                    'label'       => 'Button URL',
                    'type'        => 'text',
                    'default'     => '#',
                    'toggle_slug' => 'link',
                ),
            );
        }

        public function render( $attrs, $content, $render_slug ) {
            return sprintf(
                '<div class="my-simple-cta">
                    <h2 class="my-simple-cta__heading">%s</h2>
                    <a href="%s" class="my-simple-cta__button et_pb_button">%s</a>
                </div>',
                esc_html( $this->props['heading'] ),
                esc_url( $this->props['button_url'] ),
                esc_html( $this->props['button_text'] )
            );
        }
    }

    new My_Simple_CTA();
});

// Enqueue the Visual Builder script
add_action( 'wp_enqueue_scripts', function() {
    if ( function_exists( 'et_core_is_fb_enabled' ) && et_core_is_fb_enabled() ) {
        wp_enqueue_script(
            'my-simple-cta-vb',
            plugin_dir_url( __FILE__ ) . 'vb-module.js',
            array( 'jquery' ),
            '1.0.0',
            true
        );
    }
});
```

### Visual Builder file: `my-divi-module/vb-module.js`

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    API.Modules.register([
        {
            slug: 'my_simple_cta',
            name: 'Simple CTA',

            render: function(props) {
                var heading    = props.heading || 'Take Action Now';
                var buttonText = props.button_text || 'Get Started';
                var buttonUrl  = props.button_url || '#';

                return (
                    '<div class="my-simple-cta">' +
                        '<h2 class="my-simple-cta__heading">' + heading + '</h2>' +
                        '<a href="' + buttonUrl + '" class="my-simple-cta__button et_pb_button">' +
                            buttonText +
                        '</a>' +
                    '</div>'
                );
            }
        }
    ]);
});
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The module API is largely backward-compatible with Divi 4 extensions, but Divi 5 introduces an expanded JavaScript API and changes to how styles are generated and applied. Extensions built for Divi 4 may require updates to their Visual Builder components.

## Troubleshooting

!!! warning "Module does not appear in the module picker"
    **Symptom:** You activate your plugin but the module does not show up when inserting a new module.

    **Possible causes:**

    - The module PHP class is not being loaded. Verify your `require_once` path is correct.
    - The `et_builder_ready` or `divi_extensions_init` hook is not firing. Confirm Divi is active.
    - The `$slug` property is missing or empty.
    - The class does not extend `ET_Builder_Module`.

    **Fix:** Add `error_log('Module loaded: ' . $this->slug);` inside your `init()` method and check `debug.log`.

!!! warning "Module renders on the front end but shows a blank box in the Visual Builder"
    **Symptom:** The module works on the live site but shows nothing in the Visual Builder.

    **Possible causes:**

    - The JavaScript component is not registered. Verify `et_builder_api_ready` fires and `API.Modules.register()` is called.
    - The `slug` in JavaScript does not match the PHP `$slug` exactly (case-sensitive).
    - The JS file is not enqueued, or is enqueued without the `jquery` dependency.

    **Fix:** Open the browser console in the Visual Builder and check for errors. Verify the `slug` matches between PHP and JS.

!!! warning "`show_if` conditional fields not working"
    **Symptom:** A field with `show_if` is always visible or always hidden.

    **Possible causes:**

    - The field name referenced in `show_if` does not match any field key in `get_fields()`.
    - The comparison value does not match (e.g., `'on'` vs `'yes'`).

    **Fix:** Double-check that the field key and comparison value in your `show_if` array exactly match the target field's key and its possible values.

## Related

- [Hooks & Filters](../api/hooks-filters.md)
- [CSS Class Reference](../css-reference/class-reference.md)
- [Visual Builder](../builder/visual-builder.md)
- [VB Architecture (Internals)](../internals/vb-architecture.md)
