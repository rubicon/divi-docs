---
title: "Block JSON Reference"
description: "Divi 5 block JSON schema — attribute structure, responsive format, module-specific schemas for Text, Blurb, Button, Image, and Accordion modules."
category: api
tags: [block-json, schema, attributes, json, content-storage, responsive]
related: [rest-api, hooks-filters, custom-modules]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://developer.wordpress.org/block-editor/reference-guides/block-api/"
---

# Block JSON Reference

Complete JSON attribute schema reference for Divi 5 blocks.

!!! abstract "Quick Reference"
    **Block wrapper:** `<!-- wp:divi/{module} {JSON} /-->` (leaf) or `<!-- wp:divi/{module} {JSON} -->...<!-- /wp:divi/{module} -->` (container)
    **Top-level keys:** `module` (meta, decoration, advanced), `content` (innerContent), `builderVersion`
    **Responsive format:** `{ "desktop": { "value": ... }, "tablet": { "value": ... }, "phone": { "value": ... } }`
    **Content encoding:** HTML in `innerContent` uses literal unicode escapes: `\u003c` (`<`), `\u003e` (`>`), `\u0022` (`"`)
    **Last verified:** 2026-03-16

## Block Wrapper Structure

Divi 5 stores content as WordPress block comments in the `post_content` database field. There are two block types:

### Leaf Blocks (Self-Closing)

Modules that contain no child blocks use self-closing syntax:

```html
<!-- wp:divi/text {"module":{"meta":{...},"decoration":{...},"advanced":{...}},"content":{...},"builderVersion":"5.0.0-public-beta.1"} /-->
```

Examples: `divi/text`, `divi/button`, `divi/image`, `divi/blurb`, `divi/testimonial`

### Container Blocks (Opening/Closing)

Structural elements that contain child blocks use paired tags:

```html
<!-- wp:divi/section {"module":{...},"builderVersion":"5.0.0-public-beta.1"} -->
  <!-- wp:divi/row {"module":{...},"builderVersion":"5.0.0-public-beta.1"} -->
    <!-- wp:divi/column {"module":{...},"builderVersion":"5.0.0-public-beta.1"} -->
      <!-- wp:divi/text {...} /-->
    <!-- /wp:divi/column -->
  <!-- /wp:divi/row -->
<!-- /wp:divi/section -->
```

Examples: `divi/placeholder`, `divi/section`, `divi/row`, `divi/column`, `divi/accordion`

### Full Page Hierarchy

```
<!-- wp:divi/placeholder -->
  <!-- wp:divi/section {JSON} -->
    <!-- wp:divi/row {JSON} -->
      <!-- wp:divi/column {JSON} -->
        <!-- wp:divi/text {JSON} /-->
        <!-- wp:divi/button {JSON} /-->
      <!-- /wp:divi/column -->
    <!-- /wp:divi/row -->
  <!-- /wp:divi/section -->
<!-- /wp:divi/placeholder -->
```

The `divi/placeholder` wrapper is the outermost container for all Divi content on a page. See [Block Comment Format](../internals/block-format.md) for the complete structural documentation.

## Top-Level JSON Structure

Every block's JSON attribute object has these top-level keys:

```json
{
  "module": {
    "meta": { },
    "decoration": { },
    "advanced": { }
  },
  "content": {
    "innerContent": { }
  },
  "builderVersion": "5.0.0-public-beta.1"
}
```

| Key | Type | Description |
|-----|------|-------------|
| `module` | `object` | All module configuration — metadata, visual styling, and advanced settings |
| `module.meta` | `object` | Administrative metadata: `adminLabel`, `conditions`, `visibility` |
| `module.decoration` | `object` | Visual styling rendered as CSS on the module root element: `layout`, `spacing`, `sizing`, `background`, `border`, `boxShadow` |
| `module.advanced` | `object` | Inner element styling and advanced options: `text`, `htmlAttributes`, `css` |
| `content` | `object` | Module content data |
| `content.innerContent` | `object` | The module's HTML content (text blocks, blurb body, etc.) |
| `builderVersion` | `string` | The Divi Builder version that created/last modified this block |

### decoration vs advanced

This is a key architectural distinction for targeting CSS:

| Namespace | Targets | CSS Selector | Examples |
|-----------|---------|-------------|----------|
| `module.decoration.*` | Module root element | `.et_pb_text_N` | layout, spacing, sizing, background, border |
| `module.advanced.text.text.*` | Inner text element | `.et_pb_text_N .et_pb_text_inner` | text orientation, color |

See [JSON Attribute Map — Key Distinction](../internals/json-attribute-map.md) for how these render to CSS.

## Responsive Attribute Format

All value-carrying attributes use a responsive wrapper. Each breakpoint has its own `value` key:

### Single Breakpoint (Desktop Only)

```json
{
  "desktop": {
    "value": "center"
  }
}
```

### All Breakpoints

```json
{
  "desktop": {
    "value": "center"
  },
  "tablet": {
    "value": "left"
  },
  "phone": {
    "value": "left"
  }
}
```

### Nested Object Values

When the value itself is an object (e.g., padding with multiple sides):

```json
{
  "desktop": {
    "value": {
      "padding": {
        "top": "60px",
        "right": "20px",
        "bottom": "60px",
        "left": "20px"
      }
    }
  },
  "tablet": {
    "value": {
      "padding": {
        "top": "30px",
        "right": "15px",
        "bottom": "30px",
        "left": "15px"
      }
    }
  }
}
```

Divi 5 uses desktop-first (`max-width`) breakpoints. If only `desktop` is specified, that value applies to all screen sizes. See [Known Limitations — Rule #11](../playbooks/known-limitations.md).

## CSS Property to JSON Path Mapping

| CSS Property | JSON Path | Example Value | Rendered On |
|---|---|---|---|
| `text-align` | `module.advanced.text.text.desktop.value.orientation` | `"center"` | `.et_pb_text_inner` |
| `color` | `module.advanced.text.text.desktop.value.color` | `"#ffffff"` | `.et_pb_text_inner` |
| `max-width` | `module.decoration.sizing.desktop.value.maxWidth` | `"900px"` | Root element |
| `width` | `module.decoration.sizing.desktop.value.width` | `"80%"` | Root element |
| `padding` | `module.decoration.spacing.desktop.value.padding` | `{"top":"60px","right":"20px","bottom":"60px","left":"20px"}` | Root element |
| `margin` | `module.decoration.spacing.desktop.value.margin` | `{"top":"0px","bottom":"20px","left":"auto","right":"auto","syncVertical":"off","syncHorizontal":"off"}` | Root element |
| `background-color` | `module.decoration.background.desktop.value.color` | `"#037d87"` | Root element |
| `display` | `module.decoration.layout.desktop.value.display` | `"block"` | Root element |
| `border-radius` | `module.decoration.border.desktop.value.radius` | `{"topLeft":"10px","topRight":"10px","bottomRight":"10px","bottomLeft":"10px"}` | Root element 🔬 Needs Testing |
| `box-shadow` | `module.decoration.boxShadow.desktop.value` | `{"horizontal":"0px","vertical":"4px","blur":"12px","spread":"0px","color":"rgba(0,0,0,0.1)","position":"outer"}` | Root element 🔬 Needs Testing |

!!! note "CSS Output Details"
    `margin` and `padding` are rendered with `!important`. `max-width` and `text-align` are not. `color` on `.et_pb_text_inner` gets `!important`. See [JSON Attribute Map — CSS Rendering](../internals/json-attribute-map.md).

### Margin Sync Properties

The margin object supports sync flags that control whether linked values are used:

```json
{
  "margin": {
    "top": "0px",
    "right": "auto",
    "bottom": "20px",
    "left": "auto",
    "syncVertical": "off",
    "syncHorizontal": "off"
  }
}
```

| Property | Values | Description |
|----------|--------|-------------|
| `syncVertical` | `"on"` / `"off"` | When `"on"`, top and bottom share one value 🔬 Needs Testing |
| `syncHorizontal` | `"on"` / `"off"` | When `"on"`, left and right share one value 🔬 Needs Testing |

## Module-Specific Schemas

### Text Module (`divi/text`)

The most common module. Content is unicode-encoded HTML in `innerContent`.

```json
{
  "module": {
    "meta": {
      "adminLabel": { "desktop": { "value": "text" } }
    },
    "decoration": {
      "spacing": {
        "desktop": {
          "value": {
            "margin": { "bottom": "20px" }
          }
        }
      }
    },
    "advanced": {
      "text": {
        "text": {
          "desktop": {
            "value": {
              "orientation": "center",  // text-align
              "color": "#333333"
            }
          }
        }
      }
    }
  },
  "content": {
    "innerContent": {
      "desktop": {
        "value": "\\u003ch2\\u003eHeading Text\\u003c/h2\\u003e\\u003cp\\u003eParagraph content here.\\u003c/p\\u003e"
      }
    }
  },
  "builderVersion": "5.0.0-public-beta.1"
}
```

!!! warning "Content Encoding"
    HTML inside `innerContent` MUST use literal 6-character unicode escape strings: `\u003c` for `<`, `\u003e` for `>`, `\u0022` for `"`. These are literal backslash-u sequences in the JSON string, not JavaScript unicode escapes. See [Content Encoding](../internals/content-encoding.md).

### Blurb Module (`divi/blurb`)

Blurbs combine an icon or image with a title and body text.

```json
{
  "module": {
    "meta": {
      "adminLabel": { "desktop": { "value": "blurb" } }
    },
    "decoration": {
      "background": {
        "desktop": { "value": { "color": "#f5f5f5" } }
      },
      "spacing": {
        "desktop": {
          "value": {
            "padding": { "top": "30px", "right": "30px", "bottom": "30px", "left": "30px" }
          }
        }
      }
    }
  },
  "content": {
    "module": {
      "title": {
        "desktop": { "value": "Feature Title" }
      },
      "image": {
        "desktop": { "value": "https://example.com/wp-content/uploads/icon.png" }
      }
    },
    "innerContent": {
      "desktop": {
        "value": "\\u003cp\\u003eDescription of this feature goes here.\\u003c/p\\u003e"
      }
    }
  },
  "builderVersion": "5.0.0-public-beta.1"
}
```

⚠️ Observed — the `content.module.title` and `content.module.image` paths are based on observed block output. The exact schema may vary by Divi version.

### Button Module (`divi/button`)

```json
{
  "module": {
    "meta": {
      "adminLabel": { "desktop": { "value": "button" } }
    },
    "decoration": {
      "spacing": {
        "desktop": {
          "value": {
            "margin": { "top": "20px" }
          }
        }
      }
    }
  },
  "content": {
    "module": {
      "text": {
        "desktop": { "value": "Learn More" }
      },
      "url": {
        "desktop": { "value": "https://example.com/about" }
      },
      "urlNewWindow": {
        "desktop": { "value": "off" }
      }
    }
  },
  "builderVersion": "5.0.0-public-beta.1"
}
```

| Content Field | Type | Description |
|---------------|------|-------------|
| `content.module.text` | responsive string | Button label text |
| `content.module.url` | responsive string | Button link URL |
| `content.module.urlNewWindow` | responsive `"on"` / `"off"` | Open in new tab 🔬 Needs Testing |

### Image Module (`divi/image`)

```json
{
  "module": {
    "meta": {
      "adminLabel": { "desktop": { "value": "image" } }
    },
    "decoration": {
      "sizing": {
        "desktop": {
          "value": {
            "maxWidth": "100%",
            "alignment": "center"
          }
        }
      }
    }
  },
  "content": {
    "module": {
      "src": {
        "desktop": { "value": "https://example.com/wp-content/uploads/photo.jpg" }
      },
      "alt": {
        "desktop": { "value": "Description of the image" }
      },
      "url": {
        "desktop": { "value": "" }
      }
    }
  },
  "builderVersion": "5.0.0-public-beta.1"
}
```

| Content Field | Type | Description |
|---------------|------|-------------|
| `content.module.src` | responsive string | Image source URL |
| `content.module.alt` | responsive string | Alt text for accessibility |
| `content.module.url` | responsive string | Optional link URL when image is clicked 🔬 Needs Testing |

### Accordion Module (`divi/accordion`)

Accordions are container blocks with child `divi/accordion-item` blocks.

```html
<!-- wp:divi/accordion {"module":{...},"builderVersion":"5.0.0-public-beta.1"} -->
  <!-- wp:divi/accordion-item {"module":{...},"content":{"module":{"title":{"desktop":{"value":"First Question"}}},"innerContent":{"desktop":{"value":"\\u003cp\\u003eAnswer here.\\u003c/p\\u003e"}}},"builderVersion":"5.0.0-public-beta.1"} /-->
  <!-- wp:divi/accordion-item {"module":{...},"content":{"module":{"title":{"desktop":{"value":"Second Question"}}},"innerContent":{"desktop":{"value":"\\u003cp\\u003eAnother answer.\\u003c/p\\u003e"}}},"builderVersion":"5.0.0-public-beta.1"} /-->
<!-- /wp:divi/accordion -->
```

Each `accordion-item` has:

```json
{
  "content": {
    "module": {
      "title": {
        "desktop": { "value": "Question Text" }
      }
    },
    "innerContent": {
      "desktop": {
        "value": "\\u003cp\\u003eAnswer text with unicode-encoded HTML.\\u003c/p\\u003e"
      }
    }
  }
}
```

⚠️ Observed — accordion items may use self-closing or paired tags depending on whether they contain nested modules.

### Section (`divi/section`)

```json
{
  "module": {
    "meta": {
      "adminLabel": { "desktop": { "value": "Hero Section" } }
    },
    "decoration": {
      "background": {
        "desktop": {
          "value": {
            "color": "#037d87"
          }
        }
      },
      "spacing": {
        "desktop": {
          "value": {
            "padding": { "top": "100px", "bottom": "100px" }
          }
        }
      },
      "sizing": {
        "desktop": {
          "value": {
            "width": "100%"
          }
        }
      },
      "layout": {
        "desktop": {
          "value": {
            "display": "block"
          }
        }
      }
    }
  },
  "builderVersion": "5.0.0-public-beta.1"
}
```

!!! warning "Background Images"
    Divi 5 SSR does not reliably render background images set via section JSON attributes. Use a solid `color` in the JSON and inline CSS in a text block for actual background images. See [SSR Rendering — Background Image Gap](../internals/ssr-rendering.md) and [Known Limitations — Rule #4](../playbooks/known-limitations.md).

## Column Type Values

Columns use a `type` field indicating their width fraction within a row:

| Type Value | Width | Common Combination |
|------------|-------|-------------------|
| `4_4` | 100% | Single column layout |
| `1_2` | 50% | `1_2` + `1_2` = two equal columns |
| `1_3` | 33.33% | `1_3` + `1_3` + `1_3` = three equal |
| `2_3` | 66.67% | `2_3` + `1_3` = main + sidebar |
| `1_4` | 25% | `1_4` + `3_4` = sidebar + main |
| `3_4` | 75% | `3_4` + `1_4` = main + sidebar |

See [Block Comment Format — Column Type Values](../internals/block-format.md) for the complete table.

## Preset References

Modules can reference presets (saved attribute templates) instead of inline values. When a preset is applied, the block JSON includes a preset reference: 🔬 Needs Testing

```json
{
  "module": {
    "meta": {
      "preset": {
        "desktop": { "value": "preset-id-here" }
      }
    }
  }
}
```

The preset ID maps to a preset definition stored in Divi's preset system. When the preset is updated, all blocks referencing it inherit the changes. See [Presets](../builder/presets.md) for the builder documentation.

## Design Variable References

Divi 5 supports design variables (global tokens) that can be referenced in block attributes. When a field is connected to a variable, the value appears as a variable reference: 🔬 Needs Testing

```json
{
  "module": {
    "decoration": {
      "spacing": {
        "desktop": {
          "value": {
            "padding": {
              "top": "var(--divi-spacing-section-vertical)",
              "bottom": "var(--divi-spacing-section-vertical)"
            }
          }
        }
      }
    }
  }
}
```

See [Design Variables](../builder/design-variables.md) and [Global Variables](../builder/global-variables.md) for the builder documentation.

## Content Encoding Rules

HTML content inside `innerContent` values uses literal unicode escape strings. These are 6-character strings in the JSON — they are NOT JavaScript unicode escapes processed at parse time.

| Escape String | Character | Usage |
|---------------|-----------|-------|
| `\u003c` | `<` | Opening HTML tags |
| `\u003e` | `>` | Closing HTML tags |
| `\u0022` | `"` | Attribute quotes in HTML |

### Encoding Example

The HTML:
```html
<h2>Hello World</h2><p>Welcome to <a href="https://example.com">our site</a>.</p>
```

Becomes this `innerContent` value:
```
\u003ch2\u003eHello World\u003c/h2\u003e\u003cp\u003eWelcome to \u003ca href=\u0022https://example.com\u0022\u003eour site\u003c/a\u003e.\u003c/p\u003e
```

!!! warning "Testimonial Exception"
    Testimonial `innerContent` is plain text, NOT HTML. Appending unicode-encoded HTML tags results in literal escape sequences displayed on the page. See [Known Limitations — Rule #3](../playbooks/known-limitations.md) and [Content Encoding — Testimonial Exception](../internals/content-encoding.md).

See [Content Encoding](../internals/content-encoding.md) for the full reference.

## Registered Block Types

Divi 5 registers 76+ block types with WordPress. All are `is_dynamic: true` (server-side rendered). ⚠️ Observed

Common block type names:

| Block Name | Type | Self-Closing |
|------------|------|-------------|
| `divi/placeholder` | Container | No |
| `divi/section` | Container | No |
| `divi/row` | Container | No |
| `divi/column` | Container | No |
| `divi/text` | Leaf | Yes |
| `divi/blurb` | Leaf | Yes |
| `divi/button` | Leaf | Yes |
| `divi/image` | Leaf | Yes |
| `divi/testimonial` | Leaf | Yes |
| `divi/accordion` | Container | No |
| `divi/accordion-item` | Leaf | Yes |
| `divi/slider` | Container | No |
| `divi/slide` | Leaf | Yes |
| `divi/tabs` | Container | No |
| `divi/tab` | Leaf | Yes |

## Version Notes

!!! note "Divi 5 Only"
    This page documents the Divi 5 block JSON format. Divi 4 used a completely different shortcode-based system (`[et_pb_section]...[/et_pb_section]`). The JSON block format is a fundamental architectural change in Divi 5.

!!! info "Schema Stability"
    The block JSON schema is not officially documented by Elegant Themes as of March 2026. All schemas on this page are derived from observed block output in Divi 5 public beta. Field names, nesting, and available properties may change. ⚠️ Observed

## Related

- [REST API Integration](rest-api.md) — reading and modifying block JSON via REST API
- [WP-CLI Integration](wp-cli.md) — command-line tools for searching and modifying block content
- [Hooks & Filters](hooks-filters.md) — PHP and JavaScript hooks for extending modules
- [Custom Modules](custom-modules.md) — building custom Divi 5 modules
- [Block Comment Format](../internals/block-format.md) — outer block comment structure
- [JSON Attribute Map](../internals/json-attribute-map.md) — CSS-to-JSON path mapping with brace-depth parser
- [Content Encoding](../internals/content-encoding.md) — unicode encoding rules
- [SSR Rendering](../internals/ssr-rendering.md) — how blocks render on the frontend
- [Known Limitations](../playbooks/known-limitations.md) — critical rules for Divi 5 development
