---
title: "WP-CLI Integration"
description: "Divi 5 WP-CLI reference — searching Divi content, bulk block operations, cache management, and database queries for programmatic site management."
category: api
tags: [wp-cli, command-line, database, bulk-operations, search]
related: [rest-api, block-json-reference, hooks-filters]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://developer.wordpress.org/cli/commands/"
---

# WP-CLI Integration

Command-line tools for searching, exporting, and bulk-modifying Divi 5 content.

!!! abstract "Quick Reference"
    **Search for Divi pages:** `wp db query "SELECT ID, post_title FROM wp_posts WHERE post_content LIKE '%wp:divi/%' AND post_status='publish'"`
    **Export page content:** `wp post get {id} --field=content > page.txt`
    **Check builder flag:** `wp post meta get {id} _et_pb_use_builder`
    **Bulk find/replace:** `wp search-replace 'old-string' 'new-string' wp_posts --include-columns=post_content --dry-run`
    **Clear caches:** `wp cache flush && wp transient delete --all`
    **Last verified:** 2026-03-16

!!! warning "The Create vs. Modify Rule Applies"
    The same limitation from the REST API applies here: content CREATED via WP-CLI or direct database writes renders on the frontend but is invisible in the Visual Builder. Only MODIFY existing VB-created blocks. See [REST API Integration — Create vs. Modify Rule](rest-api.md) and [Known Limitations — Rule #1](../playbooks/known-limitations.md).

## Searching for Divi Content

### Find All Pages Using Divi Blocks

```bash
wp db query "SELECT ID, post_title, post_type, post_status
FROM wp_posts
WHERE post_content LIKE '%wp:divi/%'
AND post_status = 'publish'
ORDER BY post_type, post_title"
```

### Find Pages Using a Specific Module

```bash
# Find all pages containing a text module
wp db query "SELECT ID, post_title
FROM wp_posts
WHERE post_content LIKE '%wp:divi/text%'
AND post_status = 'publish'"
```

```bash
# Find all pages containing an accordion
wp db query "SELECT ID, post_title
FROM wp_posts
WHERE post_content LIKE '%wp:divi/accordion%'
AND post_status = 'publish'"
```

### Find Pages with Specific Content

```bash
# Find pages containing a specific text string inside Divi blocks
wp db query "SELECT ID, post_title
FROM wp_posts
WHERE post_content LIKE '%wp:divi/%'
AND post_content LIKE '%Contact Us Today%'
AND post_status = 'publish'"
```

### Count Divi Blocks Per Page

```bash
# Count how many text blocks exist on each page
wp db query "SELECT ID, post_title,
  (LENGTH(post_content) - LENGTH(REPLACE(post_content, 'wp:divi/text', ''))) / LENGTH('wp:divi/text') AS text_block_count
FROM wp_posts
WHERE post_content LIKE '%wp:divi/text%'
AND post_status = 'publish'
ORDER BY text_block_count DESC"
```

🔬 Needs Testing — the LENGTH/REPLACE counting method works for approximate counts but may over-count if `wp:divi/text` appears in JSON string values.

## Exporting Divi Content

### Export a Single Page's Block Content

```bash
# Export raw block content to a file
wp post get 42 --field=content > page-42-content.txt
```

### Export with Metadata

```bash
# Get page info and content together
wp post get 42 --fields=ID,post_title,post_status,post_modified --format=json
wp post get 42 --field=content > page-42-content.txt
wp post meta get 42 _et_pb_use_builder
```

### Bulk Export All Divi Pages

```bash
#!/bin/bash
# Export all published Divi pages to individual files
# Creates one file per page: exports/page-{ID}-{slug}.txt

mkdir -p exports

wp db query "SELECT ID FROM wp_posts WHERE post_content LIKE '%wp:divi/%' AND post_status='publish' AND post_type='page'" --skip-column-names | while read -r page_id; do
    slug=$(wp post get "$page_id" --field=post_name)
    wp post get "$page_id" --field=content > "exports/page-${page_id}-${slug}.txt"
    echo "Exported page $page_id ($slug)"
done

echo "Export complete. Files in exports/"
```

## Bulk Find and Replace

### Preview Changes (Dry Run)

Always run with `--dry-run` first:

```bash
# Preview: replace a color value across all post content
wp search-replace '#037d87' '#1a5276' wp_posts \
  --include-columns=post_content \
  --dry-run
```

### Execute Replacement

```bash
# Replace an old URL across all Divi content
wp search-replace 'https://old-domain.com' 'https://new-domain.com' wp_posts \
  --include-columns=post_content \
  --precise \
  --report-changed-only
```

### Replace a CSS Class in Block JSON

```bash
# Replace a CSS class name used in Divi block attributes
wp search-replace 'my-old-class' 'my-new-class' wp_posts \
  --include-columns=post_content \
  --dry-run
```

!!! warning "JSON-Safe Replacements Only"
    `wp search-replace` does plain string replacement. This is safe for simple substitutions (URLs, color hex values, class names) but dangerous for structural JSON changes. For JSON attribute modifications, use the REST API approach described in [REST API Integration](rest-api.md). Never replace strings that could break JSON syntax (quotes, braces, colons).

### Replace Across Specific Post Types

```bash
# Replace only in pages (not posts, not library layouts)
wp db query "UPDATE wp_posts
SET post_content = REPLACE(post_content, '#037d87', '#1a5276')
WHERE post_type = 'page'
AND post_content LIKE '%#037d87%'"
```

🔬 Needs Testing — direct SQL UPDATE bypasses WordPress hooks and caches. Always run `wp cache flush` afterward.

## Post Meta Management

### Check the Builder Flag

The `_et_pb_use_builder` post meta must be `"on"` for Divi SSR to render a page. See [SSR Rendering — Post Meta Requirements](../internals/ssr-rendering.md).

```bash
# Check if a page uses the Divi Builder
wp post meta get 42 _et_pb_use_builder
# Returns: "on" or empty
```

### Set the Builder Flag

```bash
# Enable Divi Builder for a page
wp post meta update 42 _et_pb_use_builder "on"
```

### Find Pages Missing the Builder Flag

```bash
# Find pages with Divi blocks but missing the builder meta flag
wp db query "SELECT p.ID, p.post_title
FROM wp_posts p
LEFT JOIN wp_postmeta pm ON p.ID = pm.post_id AND pm.meta_key = '_et_pb_use_builder'
WHERE p.post_content LIKE '%wp:divi/%'
AND p.post_status = 'publish'
AND (pm.meta_value IS NULL OR pm.meta_value != 'on')"
```

### Bulk Set Builder Flag

```bash
#!/bin/bash
# Set _et_pb_use_builder = "on" for all pages containing Divi blocks

wp db query "SELECT ID FROM wp_posts WHERE post_content LIKE '%wp:divi/%' AND post_status='publish'" --skip-column-names | while read -r page_id; do
    current=$(wp post meta get "$page_id" _et_pb_use_builder)
    if [ "$current" != "on" ]; then
        wp post meta update "$page_id" _et_pb_use_builder "on"
        echo "Set builder flag for page $page_id"
    fi
done
```

## Cache Clearing

### Standard WordPress Caches

```bash
# Flush the WordPress object cache
wp cache flush

# Delete all transients
wp transient delete --all

# Delete expired transients only
wp transient delete --expired
```

### Divi-Specific Caches

```bash
# Clear Divi's static CSS cache files
# Divi generates CSS files in wp-content/et-cache/
wp eval 'if (function_exists("et_core_clear_cache")) { et_core_clear_cache(); echo "Divi cache cleared."; } else { echo "et_core_clear_cache not found."; }'
```

🔬 Needs Testing — `et_core_clear_cache()` is the Divi 4 cache function. Divi 5 may use a different mechanism.

```bash
# Delete Divi's static CSS cache directory directly
rm -rf wp-content/et-cache/*
echo "Divi static cache files deleted."
```

🔬 Needs Testing — verify the `et-cache` directory path is correct for your installation.

```bash
# Clear rewrite rules (useful if Divi CPTs are not appearing in REST API)
wp rewrite flush
```

### Combined Cache Clear

```bash
# Full cache clear: WordPress + Divi + rewrite rules
wp cache flush && \
wp transient delete --all && \
wp eval 'if (function_exists("et_core_clear_cache")) { et_core_clear_cache(); }' && \
wp rewrite flush && \
echo "All caches cleared."
```

## Library Management

Divi Library layouts are stored as the `et_pb_layout` custom post type.

### List Library Layouts

```bash
# List all library layouts
wp post list --post_type=et_pb_layout --fields=ID,post_title,post_status,post_date --format=table
```

### Export a Library Layout

```bash
# Export a library layout's block content
wp post get 123 --field=content > layout-123.txt
```

### Search Library Layouts

```bash
# Find library layouts containing a specific module
wp db query "SELECT ID, post_title
FROM wp_posts
WHERE post_type = 'et_pb_layout'
AND post_content LIKE '%wp:divi/blurb%'
AND post_status = 'publish'"
```

### Library Layout Metadata

```bash
# Check layout type (section, row, module, or full page)
wp post meta list 123 --format=table
```

🔬 Needs Testing — the specific meta keys Divi 5 uses for layout type classification may differ from Divi 4 (`_et_pb_predefined_layout`, `_et_pb_layout_type`, etc.).

## Theme Builder Templates

Divi Theme Builder templates are stored as the `et_template` custom post type.

### List Theme Builder Templates

```bash
# List all Theme Builder templates
wp post list --post_type=et_template --fields=ID,post_title,post_status --format=table
```

🔬 Needs Testing — the `et_template` CPT name is based on Divi 4/5 observed behavior.

### Export a Template

```bash
wp post get 456 --field=content > template-456.txt
```

### Find Template Assignments

```bash
# Check template meta for assignment rules
wp post meta list 456 --format=table
```

🔬 Needs Testing — Theme Builder template assignment metadata structure in Divi 5 is not publicly documented.

## Example Scripts

### Bulk Export All Divi Pages with Metadata

```bash
#!/bin/bash
# Exports each Divi page as a JSON file with metadata and content

mkdir -p divi-export

wp db query "SELECT ID FROM wp_posts WHERE post_content LIKE '%wp:divi/%' AND post_status='publish' AND post_type='page'" --skip-column-names | while read -r page_id; do
    slug=$(wp post get "$page_id" --field=post_name)
    title=$(wp post get "$page_id" --field=post_title)
    modified=$(wp post get "$page_id" --field=post_modified)
    builder_flag=$(wp post meta get "$page_id" _et_pb_use_builder 2>/dev/null || echo "not set")
    content=$(wp post get "$page_id" --field=content)

    cat > "divi-export/${page_id}-${slug}.json" <<JSONEOF
{
  "id": ${page_id},
  "title": "$(echo "$title" | sed 's/"/\\"/g')",
  "slug": "${slug}",
  "modified": "${modified}",
  "builder_flag": "${builder_flag}",
  "content": $(echo "$content" | python3 -c "import sys, json; print(json.dumps(sys.stdin.read()))")
}
JSONEOF

    echo "Exported: ${page_id} - ${title}"
done

echo "Export complete. Files in divi-export/"
```

### Find Pages Containing a Specific Module Type

```bash
#!/bin/bash
# Find all pages using a specific Divi module
# Usage: ./find-module.sh button

MODULE_NAME="${1:?Usage: $0 <module-name>}"

echo "Searching for divi/${MODULE_NAME} blocks..."
echo "---"

wp db query "SELECT ID, post_title, post_type
FROM wp_posts
WHERE post_content LIKE '%wp:divi/${MODULE_NAME}%'
AND post_status = 'publish'
ORDER BY post_type, post_title" --skip-column-names | while IFS=$'\t' read -r id title type; do
    # Count occurrences
    count=$(wp post get "$id" --field=content | grep -o "wp:divi/${MODULE_NAME}" | wc -l | tr -d ' ')
    echo "[$type] Page $id: $title ($count instances)"
done
```

### Batch Update a CSS Class Across All Pages

```bash
#!/bin/bash
# Replace a CSS class name in all Divi page content
# Usage: ./replace-class.sh old-class new-class

OLD_CLASS="${1:?Usage: $0 <old-class> <new-class>}"
NEW_CLASS="${2:?Usage: $0 <old-class> <new-class>}"

echo "Replacing '${OLD_CLASS}' with '${NEW_CLASS}' across all content..."
echo ""

# Dry run first
echo "=== DRY RUN ==="
wp search-replace "$OLD_CLASS" "$NEW_CLASS" wp_posts \
  --include-columns=post_content \
  --dry-run \
  --report-changed-only

echo ""
read -p "Proceed with replacement? (y/N): " confirm
if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
    wp search-replace "$OLD_CLASS" "$NEW_CLASS" wp_posts \
      --include-columns=post_content \
      --precise \
      --report-changed-only

    # Clear caches after modification
    wp cache flush
    wp transient delete --all
    echo "Replacement complete. Caches cleared."
else
    echo "Cancelled."
fi
```

### Validate Divi Content Integrity

```bash
#!/bin/bash
# Check all Divi pages for common content issues

echo "Validating Divi content integrity..."
echo "==================================="
errors=0

wp db query "SELECT ID FROM wp_posts WHERE post_content LIKE '%wp:divi/%' AND post_status='publish'" --skip-column-names | while read -r page_id; do
    title=$(wp post get "$page_id" --field=post_title)
    content=$(wp post get "$page_id" --field=content)

    # Check for double comments
    double_comments=$(echo "$content" | grep -c '<!--[[:space:]]*<!--' || true)
    if [ "$double_comments" -gt 0 ]; then
        echo "ERROR: Page $page_id ($title) - Double comment pattern found ($double_comments instances)"
        errors=$((errors + 1))
    fi

    # Check for builder flag
    builder_flag=$(wp post meta get "$page_id" _et_pb_use_builder 2>/dev/null)
    if [ "$builder_flag" != "on" ]; then
        echo "WARNING: Page $page_id ($title) - _et_pb_use_builder is not 'on' (value: '$builder_flag')"
    fi

    # Check for balanced section tags
    opens=$(echo "$content" | grep -o 'wp:divi/section' | wc -l | tr -d ' ')
    closes=$(echo "$content" | grep -o '/wp:divi/section' | wc -l | tr -d ' ')
    if [ "$opens" != "$closes" ]; then
        echo "ERROR: Page $page_id ($title) - Unbalanced sections: $opens opens, $closes closes"
        errors=$((errors + 1))
    fi
done

echo ""
echo "Validation complete."
```

🔬 Needs Testing — these scripts are based on standard WP-CLI patterns applied to Divi 5 block content. Test on a staging site before running on production.

## Troubleshooting

!!! warning "WP-CLI not found"
    **Symptom:** `wp: command not found`

    **Fix:** Install WP-CLI: `curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && chmod +x wp-cli.phar && sudo mv wp-cli.phar /usr/local/bin/wp`

!!! warning "Database table prefix differs"
    **Symptom:** SQL queries return empty results despite Divi content existing.

    **Fix:** The examples use `wp_posts` and `wp_postmeta`. Your site may use a different prefix. Check `wp-config.php` for `$table_prefix` and adjust queries accordingly. You can also use `wp db prefix` to get the current prefix.

!!! warning "search-replace modifies serialized data"
    **Symptom:** After `wp search-replace`, some options or widgets are broken.

    **Fix:** Always use `--include-columns=post_content` to limit replacement scope. The `--precise` flag handles serialized data correctly but is slower. For Divi block content (which is not serialized), either flag works.

!!! warning "Content changes not visible on frontend"
    **Symptom:** `wp search-replace` reports changes but the frontend shows old content.

    **Fix:** Clear all caches after modification:
    ```bash
    wp cache flush && wp transient delete --all
    ```
    Also clear any server-level caches (Varnish, Redis, page cache plugins).

!!! warning "Pages render blank after database modification"
    **Symptom:** A page shows nothing after direct SQL content changes.

    **Fix:** Check `_et_pb_use_builder` meta is set to `"on"`. Verify section tags are balanced. Run the content integrity validator script above. See [SSR Rendering — Section Validation Checklist](../internals/ssr-rendering.md).

## Version Notes

!!! note "Divi 5 Only"
    This page documents WP-CLI usage with Divi 5 block content (`wp:divi/*` comments with JSON attributes). Divi 4 stored content as shortcodes (`[et_pb_section]`) which required different search patterns.

!!! info "WP-CLI Compatibility"
    All commands on this page use standard WP-CLI core commands. No Divi-specific WP-CLI package exists as of March 2026. 🔬 Needs Testing — Elegant Themes may release a Divi CLI extension in the future.

## Related

- [REST API Integration](rest-api.md) — reading and modifying content via HTTP endpoints
- [Block JSON Reference](block-json-reference.md) — the JSON attribute schema inside block comments
- [Hooks & Filters](hooks-filters.md) — PHP and JavaScript extension hooks
- [Block Comment Format](../internals/block-format.md) — block comment structure in `post_content`
- [SSR Rendering](../internals/ssr-rendering.md) — server-side rendering and the builder flag requirement
- [Content Encoding](../internals/content-encoding.md) — unicode encoding rules for HTML in JSON
- [Known Limitations](../playbooks/known-limitations.md) — critical rules including the create-vs-modify limitation
