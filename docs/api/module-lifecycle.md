---
title: "Module Rendering Lifecycle"
description: "Divi 5 module lifecycle reference — from registration through Visual Builder preview rendering, SSR output, block serialization, and front-end HTML generation."
category: api
tags: [module-lifecycle, rendering, ssr, visual-builder, react, registration]
related: [custom-modules, module-json-schema, hooks-filters, javascript-api]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/8656791-how-to-create-a-divi-builder-module"
---

# Module Rendering Lifecycle

The complete lifecycle of a Divi 5 module — from PHP registration through Visual Builder preview rendering, block JSON serialization, server-side rendering, and final front-end HTML output.

!!! abstract "Quick Reference"
    **What this documents:** The six phases a Divi 5 module passes through: Registration, Settings Panel, VB Preview, Block Serialization, SSR, and Front-end HTML output.
    **Key distinction:** The [Custom Modules](../api/custom-modules.md) page covers *how to build*. This page covers *what happens internally* at each phase.
    **Critical path:** `et_builder_ready` (PHP) → `get_fields()` → `et_builder_api_ready` (JS) → `render()` (JS, VB) → block JSON save → `render()` (PHP, SSR) → HTML output

## Lifecycle Overview

A Divi 5 module passes through six distinct phases from definition to rendered output. Not all phases execute on every page load — the Visual Builder phases (2–4) only run when the VB is active, while SSR (phase 5) runs on front-end page loads.

```
┌──────────────────────────────────────────────────────────────────┐
│                    MODULE LIFECYCLE                               │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. REGISTRATION          PHP class loaded, module defined       │
│     │                     Hooks: et_builder_framework_loaded     │
│     │                            et_builder_modules_loaded       │
│     │                            et_builder_ready                │
│     ▼                                                            │
│  2. SETTINGS PANEL        get_fields() → React UI components     │
│     │                     User configures module in VB sidebar   │
│     ▼                                                            │
│  3. VB PREVIEW            JS render() called with props          │
│     │                     HTML injected into iframe canvas       │
│     │                     Hook: et_builder_api_ready             │
│     ▼                                                            │
│  4. BLOCK SERIALIZATION   Module state → block JSON in           │
│     │                     post_content on save                   │
│     │                     Hook: et_builder_after_save (JS)       │
│     │                           et_save_post (PHP)               │
│     ▼                                                            │
│  5. SERVER-SIDE RENDER    PHP render() with $attrs, $content     │
│     │                     ET_Builder_Element::set_style()        │
│     │                     Filter: et_module_shortcode_output     │
│     ▼                                                            │
│  6. FRONT-END HTML        <style> in <head>, module HTML in      │
│                           .et_builder_inner_content              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

## Phase 1: Module Registration

Module registration occurs during the WordPress `init` sequence when the Divi Builder framework loads. PHP module classes are instantiated and their metadata is cataloged by the framework.

### Execution Flow

1. **`et_builder_framework_loaded`** — The Builder's core PHP framework is loaded (class autoloaders, utility functions, base classes).
2. **`et_builder_modules_loaded`** — All built-in Divi modules (`ET_Builder_Module_Text`, `ET_Builder_Module_Blurb`, etc.) are instantiated. At this point, you can reference any built-in module class.
3. **`et_builder_ready`** — The Builder is fully initialized. **Register custom standalone modules here.**
4. **`divi_extensions_init`** — Fires for Divi Extension plugins. The `DiviExtension` base class auto-discovers module PHP files in your extension's `includes/modules/` directory. **Register extension-based modules here.**

⚠️ Observed — `divi_extensions_init` fires after `et_builder_ready`. Extensions using the `DiviExtension` base class do not need to hook into `et_builder_ready` manually — the parent class handles module loading.

### What Happens During Registration

When a module class is instantiated (e.g., `new MDE_InfoBox()`), the following occurs:

1. The `ET_Builder_Module` constructor calls `$this->init()`.
2. `init()` sets `$this->name`, `$this->advanced_fields`, `$this->settings_modal_toggles`, and other configuration. See [Module JSON Schema](../api/module-json-schema.md) for all properties.
3. The constructor registers the module with the global module registry, indexed by `$this->slug`.
4. The module's `get_fields()` is **not** called during registration — it is deferred until the settings panel needs to render or the module needs to process attributes. ⚠️ Observed

### JavaScript Registration

On the client side (Visual Builder only), module JS components are registered when the Builder's React application initializes:

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    API.Modules.register([MyModuleComponent]);
});
```

The `slug` property on the JS component must exactly match the PHP class's `$slug`. If they do not match, the module will render server-side but show a blank preview in the VB.

See [Hooks & Filters — The `et_builder_api_ready` Event](../api/hooks-filters.md#the-et_builder_api_ready-event) for the full `API` object reference.

### `divi_extensions_init` vs `et_builder_ready`

| Hook | Use Case | Auto-Discovery |
|------|----------|----------------|
| `divi_extensions_init` | Divi Extension plugins using the `DiviExtension` base class | Yes — modules in `includes/modules/` are loaded automatically |
| `et_builder_ready` | Standalone plugins or themes adding modules directly | No — you must `require_once` your module classes manually |

Both hooks fire after all built-in modules are registered. The functional difference is that `divi_extensions_init` provides the Extension framework's auto-loading, asset enqueuing, and directory conventions. `et_builder_ready` is lower-level.

## Phase 2: Settings Panel Rendering

When a user adds a module to the canvas or clicks an existing module to edit it, the Visual Builder constructs the settings panel.

### Field Resolution

1. The framework calls `get_fields()` on the PHP class (via an AJAX request or during initial VB data load). ⚠️ Observed
2. The returned field definitions array is serialized and sent to the React settings panel.
3. Each field `type` maps to a React component:

| Field Type | React Component | Notes |
|------------|----------------|-------|
| `text` | Text input | Standard `<input type="text">` |
| `textarea` | Textarea | Standard `<textarea>` |
| `tiny_mce` | TinyMCE editor | Full rich text, loaded in parent frame |
| `select` | Select dropdown | Populated from `options` array |
| `yes_no_button` | Toggle switch | Binary on/off |
| `color-alpha` | Color picker | Includes opacity slider |
| `upload` | Media uploader | Opens WP media library |
| `range` | Range slider | With numeric input and unit selector |
| `select_icon` | Icon grid | ET icon font browser |
| `computed` | (none) | No UI — value computed server-side |

🔬 Needs Testing — The exact mapping mechanism (whether it is a registry lookup or hard-coded switch) is not documented.

### Toggle and Tab Organization

Fields are grouped by their `tab_slug` and `toggle_slug` values into the three-tab interface:

- **Content tab** (`tab_slug: 'general'`) — Primary content settings
- **Design tab** (`tab_slug: 'advanced'`) — Typography, colors, spacing, borders
- **Advanced tab** (`tab_slug: 'custom_css'`) — Custom CSS, visibility, transitions, scroll effects, position

Toggles within each tab are collapsible sections. Their display order follows the order they appear in `$this->settings_modal_toggles`. See [Module JSON Schema — Toggle Sections](../api/module-json-schema.md#toggle-sections).

### Conditional Logic Evaluation

`show_if` and `show_if_not` conditions are evaluated client-side in real time. When a controlling field's value changes, dependent fields are shown or hidden without a server round-trip. ⚠️ Observed

### How Field Values Are Stored

In the Visual Builder, field values live in the React component state of the settings panel. Each module instance maintains its own state object keyed by field name. When a user changes a field:

1. The React state updates immediately.
2. The VB preview (Phase 3) re-renders with the new props.
3. The value is **not** saved to the database until the user explicitly saves (Phase 4).

⚠️ Observed — Unsaved changes are held in memory. Navigating away without saving discards them (the VB prompts the user to confirm).

## Phase 3: Visual Builder Preview

The VB preview is the live, interactive rendering of the module in the iframe canvas. It uses the JS `render()` function — not the PHP `render()` method.

### Rendering Flow

1. The settings panel dispatches updated props to the preview frame.
2. The registered JS module's `render(props)` function is called.
3. `render()` returns an HTML string or React element.
4. The returned markup is injected into the module's container element in the iframe DOM.

### The `props` Object

The `props` argument contains all current field values, keyed by field name:

```javascript
render: function(props) {
    // props.title         → current title text
    // props.body_text     → current rich text HTML
    // props.background_color → current color value
    // props.className     → Divi-generated CSS class string
    // props.moduleClass   → The order-based class (e.g., "et_pb_module_0")
}
```

⚠️ Observed — `props.className` and `props.moduleClass` are injected by the framework and are not defined in `get_fields()`.

### Template String vs React Element

The `render()` function can return either:

- **HTML string** — Simplest approach. The framework injects it via `innerHTML`.
- **React element** — For modules that need React lifecycle methods, event handlers, or sub-components.

```javascript
// HTML string approach
render: function(props) {
    return '<div class="my-module">' + props.title + '</div>';
}

// React element approach (requires React as a dependency)
render: function(props) {
    return React.createElement('div', { className: 'my-module' }, props.title);
}
```

🔬 Needs Testing — React element return is supported based on the framework's use of React, but most ET examples use HTML strings.

### Responsive Preview

When the user switches breakpoints (desktop/tablet/phone) in the VB toolbar, the preview frame resizes and the module re-renders with breakpoint-specific prop values:

- Desktop: `props.title_font_size` contains the desktop value
- Tablet: `props.title_font_size` contains the tablet value (if set), otherwise falls back to desktop
- Phone: `props.title_font_size` contains the phone value (if set), otherwise falls back to tablet, then desktop

⚠️ Observed — The framework handles responsive value resolution before passing props to `render()`. The JS component does not need to manually check tablet/phone suffixed fields.

### Dual-Frame Context

The VB operates in a [dual-frame architecture](../internals/vb-architecture.md):

- **Parent window** — Settings panel, toolbar, Layers panel, TinyMCE instances
- **Iframe (`#et-vb-app-frame`)** — Page canvas where module previews render

The JS `render()` function executes in the iframe context. If your module needs to interact with the settings panel or TinyMCE, you must cross frame boundaries via `window.parent`. ⚠️ Observed

## Phase 4: Block JSON Serialization

When the user clicks Save in the Visual Builder, the current module state is serialized into the WordPress block comment format and written to `post_content`.

### Serialization Process

1. The VB collects the state of all modules on the page.
2. Each module's attributes are serialized into a JSON object following the block attribute schema.
3. The JSON is embedded in WordPress block comments: `<!-- wp:divi/{slug} {JSON} -->` for container modules or `<!-- wp:divi/{slug} {JSON} /-->` for leaf modules.
4. The complete block tree is written to `post_content` via the REST API.
5. The `_et_pb_use_builder` post meta is set to `"on"`.

### Block JSON Attribute Structure

Module field values are organized into a nested JSON structure:

```json
{
  "module": {
    "meta": {
      "adminLabel": { "desktop": { "value": "My Info Box" } }
    },
    "decoration": {
      "background": { "desktop": { "value": { "color": "#f5f5f5" } } },
      "spacing": { "desktop": { "value": { "padding": { "top": "20px", "bottom": "20px" } } } }
    }
  },
  "content": {
    "innerContent": { "desktop": { "value": "encoded content here" } }
  },
  "builderVersion": "5.0.0-public-beta.1"
}
```

See [Block Comment Format](../internals/block-format.md) for the complete attribute schema and [Content Encoding](../internals/content-encoding.md) for how HTML content is encoded within the JSON.

### The `builderVersion` Field

Every block includes `"builderVersion"` indicating which Divi version created it. This field enables forward-compatible migrations — if a future Divi version changes the attribute schema, the version tag tells the migration system which transformations to apply. ⚠️ Observed

### Save Hooks

| Hook | Type | When |
|------|------|------|
| `et_builder_after_save` | JS Event | After the VB successfully writes to the REST API |
| `et_save_post` | PHP Action | After WordPress processes the `post_content` update; receives `$post_id` |

## Phase 5: Server-Side Rendering (SSR)

On front-end page loads (outside the VB), Divi processes the block comments in `post_content` through its SSR pipeline. Each module's PHP `render()` method is called to produce HTML.

### SSR Processing Flow

1. WordPress loads `post_content` containing block comments.
2. The block parser identifies `wp:divi/*` blocks and extracts JSON attributes.
3. For each module block, Divi instantiates (or reuses) the corresponding `ET_Builder_Module` subclass.
4. JSON attributes are deserialized into `$this->props`.
5. The module's `render($attrs, $content, $render_slug)` method is called.
6. For parent modules, child blocks are rendered first and their concatenated output is passed as `$content`. ⚠️ Observed
7. The returned HTML string is collected.
8. CSS rules generated via `ET_Builder_Element::set_style()` are collected into a stylesheet.

### The `render()` Method Signature

```php
<?php
public function render( $attrs, $content, $render_slug ) {
    // $attrs       — Raw attributes array (use $this->props instead for processed values)
    // $content     — Rendered child module HTML (parent modules only)
    // $render_slug — The module's slug (e.g., 'mde_info_box')

    return '<div class="my-module">...</div>';
}
```

### `$this->props`

At render time, `$this->props` contains all field values for the current module instance, deserialized from the block JSON. Values are strings. Responsive variants are available as suffixed keys:

```php
<?php
$this->props['title'];              // Desktop value
$this->props['title_tablet'];       // Tablet value (empty string if not set)
$this->props['title_phone'];        // Phone value (empty string if not set)
$this->props['title__hover'];       // Hover state value
$this->props['title_last_edited'];  // "on|desktop" or "off|desktop"
```

### CSS Generation with `set_style()`

Modules generate CSS via `ET_Builder_Element::set_style()`:

```php
<?php
ET_Builder_Element::set_style( $render_slug, array(
    'selector'    => '%%order_class%% .my-title',
    'declaration' => 'color: #333; font-size: 24px;',
) );
```

The `%%order_class%%` placeholder is replaced with the module's unique order-based class (e.g., `.et_pb_mde_info_box_0`) at output time. This ensures CSS specificity per module instance.

Advanced fields (fonts, borders, etc.) generate their CSS automatically — you do not need to call `set_style()` for properties handled by the advanced fields system.

### SSR Boundaries and Gotchas

The SSR system has several documented behaviors that affect module rendering:

- **`post-content` boundary** — Blocks after `<!-- /wp:post-content -->` are NOT rendered. See [SSR Rendering](../internals/ssr-rendering.md#the-post-content-boundary).
- **`_et_pb_use_builder` requirement** — The post meta flag must be `"on"` for SSR to activate.
- **Background image gaps** — SSR does not reliably render background images from JSON attributes. See [SSR Rendering — Background Image Rendering Gap](../internals/ssr-rendering.md#background-image-rendering-gap).
- **The `et_module_shortcode_output` filter** — Fires after `render()` returns, allowing other plugins to modify the final HTML. See [Hooks & Filters — Module Output Filters](../api/hooks-filters.md#module-output-filters).

## Phase 6: Front-End HTML Output

The final rendered page combines the module HTML and generated CSS into the document.

### CSS Output

CSS rules accumulated via `set_style()` and the advanced fields system are output in one of two ways:

1. **Inline `<style>` tag** — For smaller stylesheets (below the threshold set by `et_builder_main_css_file_size_kb` filter, default 30 KB ⚠️ Observed), CSS is inlined in the `<head>`.
2. **External stylesheet** — For larger pages, CSS is written to a cached file in `wp-content/et-cache/` and linked via `<link>` tag. 🔬 Needs Testing

### HTML Structure

Each module renders within a wrapper that includes Divi-generated CSS classes:

```html
<div class="et_pb_module et_pb_mde_info_box et_pb_mde_info_box_0 et_pb_bg_layout_light">
    <!-- Module's render() output here -->
</div>
```

The generated class names follow the pattern:

| Class | Purpose |
|-------|---------|
| `et_pb_module` | Generic module identifier |
| `et_pb_{slug}` | Module-type identifier |
| `et_pb_{slug}_{N}` | Instance-specific class (N is the zero-based order index) |
| `et_pb_bg_layout_light` / `_dark` | Background layout variant |

⚠️ Observed — The wrapper `<div>` and its classes are added by the framework, not by your `render()` method. Your `render()` output is placed inside this wrapper.

### Per-Module Asset Loading

Divi 5 implements module-aware asset loading. CSS and JS files are only loaded for modules present on the page:

- **Critical CSS** — Divi generates critical CSS for above-the-fold modules. 🔬 Needs Testing
- **Dynamic JS** — Module-specific JavaScript (e.g., slider logic for the Slider module) is loaded only when that module type is present. ⚠️ Observed
- **`et_required_module_assets` filter** — Allows plugins to modify the asset list for a specific module.

### Static vs Dynamic Rendering

| Mode | When Used | Description |
|------|-----------|-------------|
| Static | Standard page load | Block JSON is processed through SSR; HTML is served from the server. CSS is cached. |
| Dynamic | AJAX / REST API contexts | Module rendering can be triggered dynamically via `ET_Builder_Element::render()`. ⚠️ Observed |

🔬 Needs Testing — Divi 5 may implement a static page cache that serves fully-rendered HTML without re-running SSR on every request. The interaction with WordPress object cache and page cache plugins is not fully documented.

## Lifecycle Hooks Reference

All hooks that fire during the module lifecycle, organized by phase:

| Phase | Hook | Type | Timing |
|-------|------|------|--------|
| Registration | `et_builder_framework_loaded` | PHP Action | Builder PHP framework loaded |
| Registration | `et_builder_modules_loaded` | PHP Action | All built-in modules instantiated |
| Registration | `et_builder_ready` | PHP Action | Builder fully initialized |
| Registration | `divi_extensions_init` | PHP Action | Extension modules loaded |
| Settings Panel | (AJAX field data request) | Internal | Fields serialized to VB |
| VB Preview | `et_builder_api_ready` | JS Event | Builder JS API ready; register modules |
| VB Preview | `et_fb_module_init` | JS Event | Module instance created in VB canvas |
| VB Preview | `et_fb_module_settings_changed` | JS Event | User changed a module setting |
| VB Preview | `et_fb_page_loaded` | JS Event | VB page fully loaded |
| Save | `et_builder_after_save` | JS Event | VB save completed (client-side) |
| Save | `et_save_post` | PHP Action | Post saved with Builder content |
| SSR | `et_pb_module_shortcode_attributes` | PHP Filter | Before render — modify attributes |
| SSR | `et_module_shortcode_output` | PHP Filter | After render — modify HTML output |
| SSR | `et_before_page_builder` | PHP Action | Before Builder content block renders |
| SSR | `et_after_page_builder` | PHP Action | After Builder content block renders |
| Front-end | `et_required_module_assets` | PHP Filter | Per-module asset list |
| Front-end | `et_global_assets_list` | PHP Filter | Global asset list |

For detailed documentation of each hook including parameters and examples, see [Hooks & Filters](../api/hooks-filters.md).

## Debugging the Lifecycle

### PHP (SSR)

```php
<?php
// Log when your module's render() is called
public function render( $attrs, $content, $render_slug ) {
    error_log( sprintf(
        '[%s] render() called. Props: %s',
        $this->slug,
        wp_json_encode( array_keys( $this->props ) )
    ) );

    // ... your render logic
}
```

### JavaScript (VB Preview)

```javascript
jQuery(window).on('et_builder_api_ready', function(event, API) {
    console.log('API ready. Registered modules:', API);

    API.Modules.register([{
        slug: 'my_module',
        name: 'My Module',
        render: function(props) {
            console.log('VB render() called with props:', Object.keys(props));
            return '<div>...</div>';
        }
    }]);
});
```

### Verifying Registration

```php
<?php
// Check if a module is registered (after et_builder_modules_loaded)
add_action( 'et_builder_modules_loaded', function() {
    $modules = ET_Builder_Element::get_modules();
    error_log( 'Registered module slugs: ' . implode( ', ', array_keys( $modules ) ) );
});
```

🔬 Needs Testing — `ET_Builder_Element::get_modules()` returns the module registry. The exact return format (array of class instances vs class names) may vary.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The rendering lifecycle changed significantly from Divi 4: shortcode parsing was replaced by block comment parsing, the VB moved to a dual-frame React architecture, and the SSR pipeline now processes WordPress block JSON instead of `[et_pb_*]` shortcodes. The PHP `render()` method signature remains the same for backward compatibility.

!!! warning "Verification Status"
    Behaviors marked with ⚠️ Observed have been seen in working Divi 5 installations but are not part of Elegant Themes' official public documentation. Behaviors marked 🔬 Needs Testing are inferred from code analysis and have not been independently verified. If you can confirm or correct any claim, please [contribute](../contributing.md).

## Related

- [Custom Modules](../api/custom-modules.md) — how to build a module (tutorial)
- [Module JSON Schema](../api/module-json-schema.md) — every property and field key documented
- [Hooks & Filters](../api/hooks-filters.md) — detailed hook reference with parameters and examples
- [Block Comment Format](../internals/block-format.md) — the block JSON structure modules serialize to
- [SSR Rendering](../internals/ssr-rendering.md) — SSR pipeline details, boundaries, and known gaps
- [Content Encoding](../internals/content-encoding.md) — how HTML is encoded in block JSON
- [Visual Builder Architecture](../internals/vb-architecture.md) — dual-frame structure and `divi.data` registry
- [CSS Class Reference](../css-reference/class-reference.md) — generated class naming patterns
