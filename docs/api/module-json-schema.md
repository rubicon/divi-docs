---
title: "Module JSON Schema"
description: "Divi 5 module.json schema reference — root properties, settings definition, field types, advanced fields, child modules, and Divi 4 to 5 conversion configuration."
category: api
tags: [module-json, schema, module-development, configuration, field-types]
related: [custom-modules, module-lifecycle, hooks-filters, javascript-api]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://github.com/elegantthemes/d5-dev-tool"
---

# Module JSON Schema

The configuration schema that defines a Divi 5 module's identity, settings fields, advanced design controls, and parent-child relationships.

!!! abstract "Quick Reference"
    **What this documents:** The structure and properties of Divi 5 module configuration — the PHP class properties, `get_fields()` return schema, `advanced_fields` array, toggle/tab organization, child module wiring, and Divi 4-to-5 conversion keys.
    **Relationship to custom-modules.md:** The [Custom Modules](../api/custom-modules.md) page is a tutorial on *how to build* a module. This page is the *schema reference* — what every property and field key means.
    **Key entry points:** `ET_Builder_Module` class properties, `init()`, `get_fields()`, `get_advanced_fields_config()`, `get_custom_css_fields_config()`

## Overview

Every Divi 5 module — built-in or custom — is defined by a PHP class extending `ET_Builder_Module`. The class exposes its configuration through properties and methods that follow a consistent schema. This page documents that schema exhaustively: root-level class properties, the field definition array returned by `get_fields()`, the advanced fields system, toggle/tab organization, child module wiring, and Divi 4-to-5 conversion configuration.

For a step-by-step guide to building a module using this schema, see [Custom Modules](../api/custom-modules.md).

## Root-Level Module Properties

These are public properties set on the `ET_Builder_Module` subclass, typically in the constructor or `init()` method.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `$slug` | `string` | Yes | Unique identifier for the module. Must match the JS component's `slug`. Convention: `{prefix}_{module_name}` (e.g., `mde_info_box`). |
| `$name` | `string` | Yes | Human-readable display name shown in the module picker and settings panel. Set in `init()`. |
| `$vb_support` | `string` | Yes | Visual Builder support flag. Set to `"on"` to enable VB preview rendering. |
| `$icon` | `string` | No | Single-character ET icon code displayed in the module picker (e.g., `'N'`). |
| `$main_css_element` | `string` | No | Primary CSS selector for the module. Usually `'%%order_class%%'`. Used as the base selector for advanced fields. |
| `$child_slug` | `string` | No | Slug of the child module (parent modules only). Links the parent to its repeatable child items. |
| `$child_item_text` | `string` | No | Singular label for child items in the UI (e.g., `"Feature"`). |
| `$type` | `string` | No | Set to `'child'` for child modules. Omit for standard (parent/standalone) modules. |
| `$child_title_var` | `string` | No | Field key used as the child item's title in the Layers panel (child modules only). |
| `$child_title_fallback_var` | `string` | No | Fallback field key if `$child_title_var` is empty (child modules only). |
| `$module_credits` | `array` | No | Associative array with `module_uri`, `author`, and `author_uri` keys. Shown in the module's info tooltip. |
| `$settings_modal_toggles` | `array` | No | Defines toggle sections within each tab. See [Toggle Sections](#toggle-sections). 🔬 Needs Testing |
| `$custom_css_fields` | `array` | No | Custom CSS target definitions. Alternative to overriding `get_custom_css_fields_config()`. ⚠️ Observed |

### Properties Set Automatically

These properties are managed by the Builder framework. Do not set them manually.

| Property | Type | Description |
|----------|------|-------------|
| `$props` | `array` | Contains deserialized field values at render time. Access via `$this->props['field_key']`. |
| `$content` | `string` | Rendered child module HTML (parent modules only). Access via `$this->content`. |
| `$module_id()` | `string` | The module's order-based class name (e.g., `et_pb_info_box_0`). ⚠️ Observed |

## Settings Field Schema

The `get_fields()` method returns an associative array. Each key is the field's storage name; each value is a configuration array following this schema.

### Field Definition Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `label` | `string` | — | Display label in the settings panel. Wrap in `esc_html__()` for translation. |
| `type` | `string` | — | Field type. See [Field Types](#field-types). |
| `description` | `string` | `''` | Help text shown below the field input. |
| `default` | `mixed` | `''` | Default value when the user has not set one. Type must match the field type's expected value. |
| `default_on_front` | `mixed` | — | Default used specifically for front-end rendering when no value is saved. ⚠️ Observed |
| `toggle_slug` | `string` | `'main_content'` | Groups this field under a toggle section. See [Toggle Sections](#toggle-sections). |
| `tab_slug` | `string` | `'general'` | Which settings tab this field appears on: `general` (Content), `advanced` (Design), `custom_css` (Advanced). |
| `sub_toggle` | `string` | — | Sub-group within a toggle. Creates a nested grouping. |
| `option_category` | `string` | — | Categorizes the field: `basic_option`, `configuration`, `layout`, `color_option`, `font_option`. Affects search and filtering in the settings panel. ⚠️ Observed |
| `options` | `array` | — | Key-value pairs for `select`, `yes_no_button`, `multiple_buttons`, and `select_icon` fields. |
| `show_if` | `array` | — | Conditional visibility: show this field only when specified fields match given values. See [Conditional Visibility](#conditional-visibility). |
| `show_if_not` | `array` | — | Conditional visibility: hide this field when specified fields match given values. |
| `mobile_options` | `bool` | `false` | Enable per-breakpoint (desktop/tablet/phone) values. Creates `{field}_tablet` and `{field}_phone` variants. |
| `responsive` | `bool` | `false` | Alias for `mobile_options`. |
| `hover` | `string` | — | Set to `'tabs'` to enable a hover-state value tab for this field. |
| `show_if_has_value` | `bool` | — | Only show this field if another referenced field has a non-empty value. 🔬 Needs Testing |
| `computed_callback` | `string` | — | PHP callback method name for `computed` field types. |
| `computed_depends_on` | `array` | — | Array of field keys that trigger recomputation for `computed` fields. |
| `computed_minimum` | `array` | — | Minimum set of fields that must have values before the computed callback runs. 🔬 Needs Testing |
| `range_settings` | `array` | — | For `range` fields: `array('min' => 0, 'max' => 100, 'step' => 1)`. |
| `upload_button_text` | `string` | — | Button label for `upload` fields. |
| `choose_text` | `string` | — | Media library dialog title for `upload` fields. |
| `allowed_units` | `array` | — | Restrict CSS units for numeric fields: `array('%', 'em', 'rem', 'px', 'cm', 'mm', 'in', 'pt', 'pc', 'ex', 'vh', 'vw')`. ⚠️ Observed |
| `validate_unit` | `bool` | — | Whether to validate that the value includes a valid CSS unit. ⚠️ Observed |
| `fixed_unit` | `string` | — | Lock the field to a single CSS unit (e.g., `'px'`). ⚠️ Observed |
| `attr_suffix` | `string` | — | Suffix appended to the attribute name when saved. 🔬 Needs Testing |
| `affects` | `array` | — | Array of field keys that should re-render when this field changes. 🔬 Needs Testing |

### Field Types

| Type | Description | Value Format | Key Configuration |
|------|-------------|-------------|-------------------|
| `text` | Single-line text input | `string` | `default`, `description` |
| `textarea` | Multi-line text input | `string` | `default`, `description` |
| `tiny_mce` | Rich text editor (TinyMCE) | `string` (HTML) | `description` |
| `select` | Dropdown select | `string` | `options` (associative array), `default` |
| `yes_no_button` | Toggle switch (on/off) | `'on'` or `'off'` | `options` (array with `on`/`off` labels), `default` |
| `multiple_buttons` | Button group selector | `string` | `options`, `default`, `toggleable` |
| `color-alpha` | Color picker with opacity | `string` (hex/rgba) | `default` |
| `color` | Color picker without opacity | `string` (hex) | `default`. 🔬 Needs Testing |
| `upload` | Media library file upload | `string` (URL) | `upload_button_text`, `choose_text`, `data_type` |
| `select_icon` | ET icon picker | `string` (icon code) | — |
| `range` | Slider with numeric input | `string` (number + unit) | `range_settings`, `default`, `allowed_units`, `fixed_unit` |
| `font` | Font family selector | `string` | — |
| `text_align` | Text alignment buttons | `string` (`left`, `center`, `right`, `justified`) | `options`, `default` |
| `hidden` | Hidden field (not rendered in UI) | `mixed` | `default` |
| `computed` | Server-computed value (no UI) | `mixed` | `computed_callback`, `computed_depends_on` |
| `custom_margin` | Margin input with per-side values | `string` (`top|right|bottom|left`) | `mobile_options`, `hover` |
| `custom_padding` | Padding input with per-side values | `string` (`top|right|bottom|left`) | `mobile_options`, `hover` |
| `border_radius` | Border radius control | `string` | `default`. 🔬 Needs Testing |
| `box_shadow` | Box shadow controls | `string` | 🔬 Needs Testing |
| `option_list` | Repeatable list of key-value items | `string` (encoded) | Decode with `API.Utils.decodeOptionListValue()` in JS. ⚠️ Observed |
| `tabbed_content` | Multi-tab content editor | `string` | 🔬 Needs Testing |
| `conditional_logic` | Conditional display rules | `string` (JSON) | 🔬 Needs Testing |

### Conditional Visibility

Fields can be shown or hidden based on the current value of other fields. Both `show_if` and `show_if_not` accept an associative array where keys are field names and values are the target values.

```php
<?php
'icon_name' => array(
    'label'       => esc_html__( 'Icon', 'my-ext' ),
    'type'        => 'select_icon',
    'toggle_slug' => 'main_content',
    // Show only when use_icon is "on"
    'show_if'     => array(
        'use_icon' => 'on',
    ),
),
'fallback_image' => array(
    'label'       => esc_html__( 'Fallback Image', 'my-ext' ),
    'type'        => 'upload',
    'toggle_slug' => 'main_content',
    // Hide when use_icon is "on" (show for all other values)
    'show_if_not' => array(
        'use_icon' => 'on',
    ),
),
```

Multiple conditions in a single `show_if` array are evaluated with AND logic — all conditions must be true for the field to appear. ⚠️ Observed

```php
<?php
'advanced_setting' => array(
    'label'       => 'Advanced Setting',
    'type'        => 'text',
    'show_if'     => array(
        'enable_advanced' => 'on',
        'mode'            => 'custom',
    ),
    // Only visible when enable_advanced="on" AND mode="custom"
),
```

### Responsive and Hover Configuration

When `mobile_options` is `true`, the Builder automatically creates breakpoint-specific variants of the field:

- `{field_key}` — Desktop value
- `{field_key}_tablet` — Tablet value
- `{field_key}_phone` — Phone value
- `{field_key}_last_edited` — Tracks which breakpoints have been edited (format: `on|desktop`)

⚠️ Observed — These suffixed field keys are accessible in `$this->props` during rendering.

When `hover` is set to `'tabs'`, the field gains a hover-state variant:

- `{field_key}__hover` — Value applied on hover
- `{field_key}__hover_enabled` — Whether hover state is active

```php
<?php
'title_color' => array(
    'label'          => esc_html__( 'Title Color', 'my-ext' ),
    'type'           => 'color-alpha',
    'default'        => '#333333',
    'tab_slug'       => 'advanced',
    'toggle_slug'    => 'title_style',
    'mobile_options'  => true,
    'hover'          => 'tabs',
),
```

In `render()`, access responsive/hover values:

```php
<?php
public function render( $attrs, $content, $render_slug ) {
    $title_color        = $this->props['title_color'];
    $title_color_tablet = $this->props['title_color_tablet'] ?? '';
    $title_color_phone  = $this->props['title_color_phone'] ?? '';
    $title_color_hover  = $this->props['title_color__hover'] ?? '';

    // Apply desktop style
    ET_Builder_Element::set_style( $render_slug, array(
        'selector'    => '%%order_class%% .title',
        'declaration' => sprintf( 'color: %s;', esc_attr( $title_color ) ),
    ) );

    // Apply hover style
    if ( ! empty( $title_color_hover ) ) {
        ET_Builder_Element::set_style( $render_slug, array(
            'selector'    => '%%order_class%% .title:hover',
            'declaration' => sprintf( 'color: %s;', esc_attr( $title_color_hover ) ),
        ) );
    }

    // ...
}
```

## Advanced Fields Configuration

The `$this->advanced_fields` array (set in `init()`) configures Divi's built-in design controls that are automatically added to the Design tab. Each key activates a category of controls.

### `fonts`

Adds typography controls (font family, size, weight, color, line height, letter spacing, text transform) for specific CSS selectors.

```php
<?php
'fonts' => array(
    'title' => array(
        'label'       => esc_html__( 'Title', 'my-ext' ),
        'css'         => array(
            'main' => '%%order_class%% .my-title',
        ),
        'font_size'   => array( 'default' => '24px' ),
        'line_height' => array( 'default' => '1.3em' ),
    ),
    'body' => array(
        'label'       => esc_html__( 'Body', 'my-ext' ),
        'css'         => array(
            'main' => '%%order_class%% .my-body',
        ),
    ),
),
```

Each font group creates a full set of typography fields in the Design tab: font family, weight/style, size, color, line height, letter spacing, and text transform. The `css.main` selector determines where the generated CSS rules are applied.

### `borders`

Adds border style and border radius controls.

```php
<?php
'borders' => array(
    'default' => array(
        'css' => array(
            'main' => array(
                'border_radii'  => '%%order_class%% .my-container',
                'border_styles' => '%%order_class%% .my-container',
            ),
        ),
    ),
    'image' => array(
        'css' => array(
            'main' => array(
                'border_radii'  => '%%order_class%% .my-image',
                'border_styles' => '%%order_class%% .my-image',
            ),
        ),
        'label_prefix' => esc_html__( 'Image', 'my-ext' ),
    ),
),
```

Multiple named border groups (e.g., `default`, `image`) create separate border control sets in the UI. ⚠️ Observed

### `box_shadow`

Adds box shadow controls with horizontal/vertical offset, blur, spread, color, and position.

```php
<?php
'box_shadow' => array(
    'default' => array(
        'css' => array(
            'main' => '%%order_class%% .my-container',
        ),
    ),
),
```

### `margin_padding`

Adds margin and padding controls with per-side values.

```php
<?php
'margin_padding' => array(
    'css' => array(
        'important' => 'all',  // Add !important to generated rules
    ),
),
```

### `background`

Adds background color, gradient, and image controls. Pass an empty array `array()` for default behavior.

```php
<?php
'background' => array(
    'css' => array(
        'main' => '%%order_class%%',
    ),
    'options' => array(
        'background_color' => array(
            'default' => '#ffffff',
        ),
    ),
),
```

### `text`

Adds text alignment control. Set to `false` to disable.

```php
<?php
'text' => array(
    'css' => array(
        'main' => '%%order_class%%',
    ),
),
// OR disable:
'text' => false,
```

### `animation`

Adds entrance animation controls (fade, slide, bounce, zoom, flip, fold, roll). ⚠️ Observed

```php
<?php
'animation' => array(),  // Enable with defaults
```

### `filters`

Adds CSS filter controls (hue, saturation, brightness, contrast, invert, sepia, opacity, blur, blend mode). ⚠️ Observed

```php
<?php
'filters' => array(
    'css' => array(
        'main' => '%%order_class%%',
    ),
),
```

### `transform`

Adds CSS transform controls (scale, translate, rotate, skew, origin). ⚠️ Observed

```php
<?php
'transform' => array(
    'css' => array(
        'main' => '%%order_class%%',
    ),
),
```

### Disabling Advanced Fields

Set any advanced field group to `false` to prevent it from appearing in the Design tab:

```php
<?php
$this->advanced_fields = array(
    'fonts'          => false,
    'text'           => false,
    'background'     => false,
    'borders'        => false,
    'box_shadow'     => false,
    'margin_padding' => false,
    'animation'      => false,
    'filters'        => false,
    'transform'      => false,
);
```

This is common for child modules that inherit styling from their parent. ⚠️ Observed

## Toggle Sections

Settings fields are organized into tabs and toggles. Tabs are the top-level navigation; toggles are collapsible sections within each tab.

### Tab Slugs

| `tab_slug` Value | Tab Label | Purpose |
|------------------|-----------|---------|
| `general` | Content | Primary content settings (text, images, links) |
| `advanced` | Design | Visual styling (fonts, colors, spacing, borders) |
| `custom_css` | Advanced | Custom CSS, visibility, transitions, position |

### Defining Toggle Sections

Toggle sections are defined via `$this->settings_modal_toggles` in `init()`:

```php
<?php
public function init() {
    $this->name = 'Info Box';

    $this->settings_modal_toggles = array(
        'general' => array(
            'toggles' => array(
                'main_content' => esc_html__( 'Text', 'my-ext' ),
                'image'        => esc_html__( 'Image & Icon', 'my-ext' ),
                'link'         => esc_html__( 'Link', 'my-ext' ),
            ),
        ),
        'advanced' => array(
            'toggles' => array(
                'title_style' => esc_html__( 'Title Text', 'my-ext' ),
                'body_style'  => esc_html__( 'Body Text', 'my-ext' ),
                'layout'      => esc_html__( 'Layout', 'my-ext' ),
            ),
        ),
    );
}
```

Fields reference their toggle via `toggle_slug`:

```php
<?php
'title' => array(
    'label'       => 'Title',
    'type'        => 'text',
    'tab_slug'    => 'general',
    'toggle_slug' => 'main_content',
),
```

### Sub-Toggles

For finer grouping within a toggle, use `sub_toggle`:

```php
<?php
$this->settings_modal_toggles = array(
    'advanced' => array(
        'toggles' => array(
            'header' => array(
                'title'        => esc_html__( 'Header', 'my-ext' ),
                'sub_toggles'  => array(
                    'h1' => array( 'name' => 'H1' ),
                    'h2' => array( 'name' => 'H2' ),
                    'h3' => array( 'name' => 'H3' ),
                ),
                'tabbed_subtoggles' => true,
            ),
        ),
    ),
);
```

🔬 Needs Testing — `tabbed_subtoggles` renders sub-toggles as a tabbed interface rather than stacked sections.

## Child Module Configuration

Parent-child module relationships are defined through class properties. See [Custom Modules — Parent and Child Modules](../api/custom-modules.md#parent-and-child-modules) for complete code examples.

### Parent Module Requirements

| Property | Value | Purpose |
|----------|-------|---------|
| `$child_slug` | Child module's `$slug` | Links the parent to its child type |
| `$child_item_text` | Singular label | UI text for "Add New {Item}" button |

In the parent's `render()`, child module output is available via `$this->content`.

### Child Module Requirements

| Property | Value | Purpose |
|----------|-------|---------|
| `$type` | `'child'` | Marks this module as a child |
| `$child_title_var` | Field key | Field used as the item title in Layers panel |
| `$child_title_fallback_var` | Field key | Fallback title if primary is empty |

Child modules do not appear in the main module picker. They are only available inside their parent module.

### How Child Rendering Works

1. The parent module's `render()` is called.
2. The Builder iterates through child block entries and calls each child module's `render()`.
3. The concatenated child HTML is stored in the parent's `$this->content`.
4. The parent inserts `$this->content` into its own HTML output.

⚠️ Observed — The parent's `render()` is always called after all its children have rendered.

## Divi 4 to Divi 5 Conversion

Divi 5 provides a conversion system for migrating Divi 4 shortcode-based modules to the Divi 5 block format. This is configured through the module class and optionally through conversion configuration files.

### Conversion Entry Points

| Mechanism | Description |
|-----------|-------------|
| `ET_Builder_Module` backward compatibility | Built-in: Divi 5 can render Divi 4 shortcodes by internally converting them to blocks. ⚠️ Observed |
| `et_builder_module_settings_migrations` filter | Register migration classes that transform old attribute names/values to new ones during content load. |
| `d5-dev-tool` conversion workflow | ET's development tool generates Divi 5 block JSON from Divi 4 module definitions. See [d5-dev-tool on GitHub](https://github.com/elegantthemes/d5-dev-tool). 🔬 Needs Testing |

### Settings Migrations

When Divi updates, it may rename fields or change value formats. Migration classes handle this transparently:

```php
<?php
// Register a migration class
add_filter( 'et_builder_module_settings_migrations', function( $migrations ) {
    $migrations['MyMigrationClass'] = plugin_dir_path( __FILE__ ) . 'migrations/MyMigrationClass.php';
    return $migrations;
});
```

🔬 Needs Testing — The migration class API is undocumented. Existing migration classes in Divi core follow a pattern of extending `ET_Builder_Module_Settings_Migration` with `get_modules()`, `get_fields()`, and `migrate()` methods.

### Key Conversion Considerations

- **Shortcode attributes map to block JSON attributes.** The `module.decoration` and `module.meta` JSON structure replaces flat shortcode attributes. See [Block Comment Format](../internals/block-format.md) for the JSON schema.
- **Content encoding changes.** Divi 4 stored rich text as shortcode inner content. Divi 5 stores it in `content.innerContent.desktop.value` with Unicode encoding. See [Content Encoding](../internals/content-encoding.md) if you are converting content programmatically.
- **`builderVersion` field.** The block JSON includes `"builderVersion": "5.0.0-public-beta.1"` (or current version). This indicates the format version and may affect how attributes are interpreted. ⚠️ Observed

## Custom CSS Fields

The `get_custom_css_fields_config()` method defines targetable CSS selectors exposed in the Advanced tab's Custom CSS toggle. Users can write CSS for each target without knowing the internal DOM structure.

```php
<?php
public function get_custom_css_fields_config() {
    return array(
        'container' => array(
            'label'    => esc_html__( 'Container', 'my-ext' ),
            'selector' => '.my-container',
        ),
        'title' => array(
            'label'    => esc_html__( 'Title', 'my-ext' ),
            'selector' => '.my-title',
        ),
    );
}
```

The `selector` value is appended to `%%order_class%%` when generating CSS rules. ⚠️ Observed

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The `ET_Builder_Module` PHP class is largely backward-compatible with Divi 4, but Divi 5 introduces expanded advanced field categories (`filters`, `transform`), the block JSON storage format, and an enhanced JavaScript API. Field types and configuration keys documented here reflect the Divi 5 API surface.

!!! warning "Verification Status"
    Properties and behaviors marked with ⚠️ Observed have been seen in working Divi 5 installations but are not formally documented by Elegant Themes. Properties marked 🔬 Needs Testing are inferred from code analysis or community reports and have not been independently verified.

## Related

- [Custom Modules](../api/custom-modules.md) — step-by-step guide to building a module using this schema
- [Module Rendering Lifecycle](../api/module-lifecycle.md) — what happens from registration through rendered HTML
- [Hooks & Filters](../api/hooks-filters.md) — hook execution order and the Builder API object
- [Block Comment Format](../internals/block-format.md) — how module data is serialized in `post_content`
- [Content Encoding](../internals/content-encoding.md) — Unicode encoding rules for HTML inside block JSON
- [Visual Builder Architecture](../internals/vb-architecture.md) — dual-frame structure and state management
- [d5-dev-tool (GitHub)](https://github.com/elegantthemes/d5-dev-tool) — Elegant Themes' Divi 5 development/conversion tool
