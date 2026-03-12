#!/usr/bin/env python3
"""Bulk scrape Elegant Themes module docs and generate structured Markdown pages."""

import requests
from bs4 import BeautifulSoup
import re
import os
import time
import json
import yaml

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs', 'modules')

# Modules to skip (already have real content or not actual modules)
SKIP_URLS = {
    'https://www.elegantthemes.com/documentation/divi/blurb/',
    'https://www.elegantthemes.com/documentation/divi/text/',
    'https://www.elegantthemes.com/documentation/divi/blog/',
    'https://www.elegantthemes.com/documentation/divi/modules/adding-custom-fields-to-the-divi-email-optin-module/',
    'https://www.elegantthemes.com/documentation/divi/divi-woocommerce-modules/',
}

# Module URL -> (slug, display_name, category)
MODULE_MAP = {
    'https://www.elegantthemes.com/documentation/divi/accordion/': ('accordion', 'Accordion', 'content'),
    'https://www.elegantthemes.com/documentation/divi/audio/': ('audio', 'Audio', 'content'),
    'https://www.elegantthemes.com/documentation/divi/bar-counter/': ('bar-counter', 'Bar Counter', 'content'),
    'https://www.elegantthemes.com/documentation/divi/button/': ('button', 'Button', 'content'),
    'https://www.elegantthemes.com/documentation/divi/cta/': ('call-to-action', 'Call to Action', 'content'),
    'https://www.elegantthemes.com/documentation/divi/circle-counter/': ('circle-counter', 'Circle Counter', 'content'),
    'https://www.elegantthemes.com/documentation/divi/code/': ('code', 'Code', 'content'),
    'https://www.elegantthemes.com/documentation/divi/comments/': ('comments', 'Comments', 'interactive'),
    'https://www.elegantthemes.com/documentation/divi/contact/': ('contact-form', 'Contact Form', 'interactive'),
    'https://www.elegantthemes.com/documentation/divi/countdown/': ('countdown-timer', 'Countdown Timer', 'content'),
    'https://www.elegantthemes.com/documentation/divi/divider/': ('divider', 'Divider', 'content'),
    'https://www.elegantthemes.com/documentation/divi/newsletter/': ('email-optin', 'Email Optin', 'interactive'),
    'https://www.elegantthemes.com/documentation/divi/filterable-portfolio/': ('filterable-portfolio', 'Filterable Portfolio', 'content'),
    'https://www.elegantthemes.com/documentation/divi/gallery/': ('gallery', 'Gallery', 'content'),
    'https://www.elegantthemes.com/documentation/divi/icon/': ('icon', 'Icon', 'content'),
    'https://www.elegantthemes.com/documentation/divi/image/': ('image', 'Image', 'content'),
    'https://www.elegantthemes.com/documentation/divi/login/': ('login', 'Login', 'interactive'),
    'https://www.elegantthemes.com/documentation/divi/map/': ('map', 'Map', 'content'),
    'https://www.elegantthemes.com/documentation/divi/number-counter/': ('number-counter', 'Number Counter', 'content'),
    'https://www.elegantthemes.com/documentation/divi/person/': ('person', 'Person', 'content'),
    'https://www.elegantthemes.com/documentation/divi/portfolio/': ('portfolio', 'Portfolio', 'content'),
    'https://www.elegantthemes.com/documentation/divi/post-navigation/': ('post-navigation', 'Post Navigation', 'content'),
    'https://www.elegantthemes.com/documentation/divi/post-slider/': ('post-slider', 'Post Slider', 'content'),
    'https://www.elegantthemes.com/documentation/divi/post-title/': ('post-title', 'Post Title', 'content'),
    'https://www.elegantthemes.com/documentation/divi/pricing-tables/': ('pricing-table', 'Pricing Table', 'content'),
    'https://www.elegantthemes.com/documentation/divi/search/': ('search', 'Search', 'interactive'),
    'https://www.elegantthemes.com/documentation/divi/ecommerce-divi/': ('shop', 'Shop', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/sidebar-divi/': ('sidebar', 'Sidebar', 'content'),
    'https://www.elegantthemes.com/documentation/divi/slider/': ('slider', 'Slider', 'content'),
    'https://www.elegantthemes.com/documentation/divi/social-follow/': ('social-media-follow', 'Social Media Follow', 'content'),
    'https://www.elegantthemes.com/documentation/divi/tab/': ('tabs', 'Tabs', 'content'),
    'https://www.elegantthemes.com/documentation/divi/testimonial/': ('testimonial', 'Testimonial', 'content'),
    'https://www.elegantthemes.com/documentation/divi/toggle/': ('toggle', 'Toggle', 'content'),
    'https://www.elegantthemes.com/documentation/divi/video/': ('video', 'Video', 'content'),
    'https://www.elegantthemes.com/documentation/divi/video-slider/': ('video-slider', 'Video Slider', 'content'),
    # Menu module
    'https://www.elegantthemes.com/documentation/divi/menu/': ('menu', 'Menu', 'content'),
    # Fullwidth modules
    'https://www.elegantthemes.com/documentation/divi/fullwidth-header-new/': ('fullwidth-header', 'Fullwidth Header', 'fullwidth'),
    'https://www.elegantthemes.com/documentation/divi/fullwidth-map/': ('fullwidth-map', 'Fullwidth Map', 'fullwidth'),
    'https://www.elegantthemes.com/documentation/divi/fullwidth-menu/': ('fullwidth-menu', 'Fullwidth Menu', 'fullwidth'),
    'https://www.elegantthemes.com/documentation/divi/fullwidth-portfolio/': ('fullwidth-portfolio', 'Fullwidth Portfolio', 'fullwidth'),
    'https://www.elegantthemes.com/documentation/divi/slider-fullwidth/': ('fullwidth-slider', 'Fullwidth Slider', 'fullwidth'),
    # Woo modules
    'https://www.elegantthemes.com/documentation/divi/woo-related-products/': ('woo-related-products', 'Woo Related Products', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-products-module/': ('woo-products', 'Woo Products', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-title-module/': ('woo-product-title', 'Woo Product Title', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/divi-woo-product-tabs-module/': ('woo-product-tabs', 'Woo Product Tabs', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-stock-module/': ('woo-product-stock', 'Woo Product Stock', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-reviews-module/': ('woo-product-reviews', 'Woo Product Reviews', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-rating-module/': ('woo-product-rating', 'Woo Product Rating', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-price-module/': ('woo-product-price', 'Woo Product Price', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-information-module/': ('woo-product-information', 'Woo Product Information', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-images-module/': ('woo-product-images', 'Woo Product Images', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-product-description-module/': ('woo-product-description', 'Woo Product Description', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-breadcrumbs-module/': ('woo-breadcrumbs', 'Woo Breadcrumbs', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/woo-cart-products/': ('woo-cart-products', 'Woo Cart Products', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-cart-totals-module/': ('woo-cart-totals', 'Woo Cart Totals', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-checkout-billing-module/': ('woo-checkout-billing', 'Woo Checkout Billing', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-checkout-details-module/': ('woo-checkout-details', 'Woo Checkout Details', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-checkout-information-module/': ('woo-checkout-information', 'Woo Checkout Information', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-checkout-payment-module/': ('woo-checkout-payment', 'Woo Checkout Payment', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-checkout-shipping-module/': ('woo-checkout-shipping', 'Woo Checkout Shipping', 'woo'),
    'https://www.elegantthemes.com/documentation/divi/the-divi-woo-cross-sells-module/': ('woo-cross-sells', 'Woo Cross Sells', 'woo'),
}

# Related modules mapping
RELATED = {
    'accordion': ['toggle', 'tabs'],
    'audio': ['video', 'video-slider'],
    'bar-counter': ['circle-counter', 'number-counter'],
    'button': ['call-to-action', 'icon'],
    'call-to-action': ['button', 'blurb'],
    'circle-counter': ['bar-counter', 'number-counter'],
    'code': ['text'],
    'comments': ['blog', 'post-title'],
    'contact-form': ['email-optin', 'login'],
    'countdown-timer': ['number-counter', 'circle-counter'],
    'divider': ['text', 'code'],
    'email-optin': ['contact-form', 'login'],
    'filterable-portfolio': ['portfolio', 'gallery', 'fullwidth-portfolio'],
    'gallery': ['image', 'filterable-portfolio', 'portfolio'],
    'icon': ['blurb', 'button'],
    'image': ['gallery', 'blurb', 'fullwidth-header'],
    'login': ['contact-form', 'email-optin'],
    'map': ['fullwidth-map'],
    'menu': ['fullwidth-menu', 'sidebar'],
    'number-counter': ['bar-counter', 'circle-counter'],
    'person': ['testimonial', 'blurb'],
    'portfolio': ['filterable-portfolio', 'gallery', 'fullwidth-portfolio'],
    'post-navigation': ['post-title', 'blog'],
    'post-slider': ['slider', 'blog', 'fullwidth-slider'],
    'post-title': ['post-navigation', 'blog'],
    'pricing-table': ['call-to-action', 'button'],
    'search': ['sidebar', 'menu'],
    'shop': ['woo-products', 'woo-product-price'],
    'sidebar': ['menu', 'search'],
    'slider': ['post-slider', 'video-slider', 'fullwidth-slider'],
    'social-media-follow': ['person', 'icon'],
    'tabs': ['accordion', 'toggle'],
    'testimonial': ['person', 'slider'],
    'toggle': ['accordion', 'tabs'],
    'video': ['audio', 'video-slider'],
    'video-slider': ['video', 'slider', 'post-slider'],
    'fullwidth-header': ['image', 'call-to-action', 'slider'],
    'fullwidth-map': ['map'],
    'fullwidth-menu': ['menu'],
    'fullwidth-portfolio': ['portfolio', 'filterable-portfolio'],
    'fullwidth-slider': ['slider', 'post-slider', 'fullwidth-header'],
}


def fetch_page(url):
    """Fetch a page and return BeautifulSoup object."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return BeautifulSoup(resp.text, 'html.parser')
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
    return None


def extract_content(soup):
    """Extract main content from an ET documentation page."""
    content = {
        'title': '',
        'description': '',
        'paragraphs': [],
        'settings': [],
        'headings': [],
    }

    # Get title
    h1 = soup.find('h1')
    if h1:
        content['title'] = h1.get_text(strip=True)

    # Get main content area
    article = soup.find('article') or soup.find('div', class_='entry-content') or soup.find('main')
    if not article:
        # Fallback: find the biggest text block
        article = soup.find('body')

    if not article:
        return content

    # Extract paragraphs
    for p in article.find_all('p'):
        text = p.get_text(strip=True)
        if text and len(text) > 20:
            content['paragraphs'].append(text)

    # Extract headings for structure
    for h in article.find_all(['h2', 'h3', 'h4']):
        content['headings'].append({
            'level': int(h.name[1]),
            'text': h.get_text(strip=True)
        })

    # Extract any lists that might contain settings info
    for ul in article.find_all(['ul', 'ol']):
        for li in ul.find_all('li', recursive=False):
            text = li.get_text(strip=True)
            if text:
                content['settings'].append(text)

    return content


def get_tags(name, category):
    """Generate relevant tags for a module."""
    tags = ['modules']
    name_lower = name.lower()

    if category == 'fullwidth':
        tags.append('fullwidth')
    elif category == 'woo':
        tags.extend(['woocommerce', 'ecommerce'])
    elif category == 'interactive':
        tags.append('forms')

    # Content-specific tags
    if 'slider' in name_lower:
        tags.append('slider')
    if 'counter' in name_lower:
        tags.append('animation')
    if 'portfolio' in name_lower:
        tags.append('portfolio')
    if any(w in name_lower for w in ['image', 'gallery', 'video', 'audio']):
        tags.append('media')
    if any(w in name_lower for w in ['form', 'contact', 'login', 'optin', 'search']):
        tags.append('interactive')
    if any(w in name_lower for w in ['blog', 'post', 'comment']):
        tags.append('blog')
    if any(w in name_lower for w in ['menu', 'navigation', 'sidebar']):
        tags.append('navigation')
    if any(w in name_lower for w in ['checkout', 'cart']):
        tags.append('checkout')
    if any(w in name_lower for w in ['product']):
        tags.append('product')

    return list(dict.fromkeys(tags))  # dedupe preserving order


def get_css_class(slug, name):
    """Get the likely CSS class for a module."""
    # Most Divi modules follow et_pb_{slug} pattern
    css_slug = slug.replace('-', '_')
    if slug.startswith('fullwidth-'):
        css_slug = 'fullwidth_' + slug.replace('fullwidth-', '').replace('-', '_')
    elif slug.startswith('woo-'):
        css_slug = 'wc_' + slug.replace('woo-', '').replace('-', '_')
    return f'.et_pb_{css_slug}'


def generate_doc_page(slug, name, source_url, content, category):
    """Generate a complete documentation page."""
    tags = get_tags(name, category)
    related = RELATED.get(slug, [])
    css_class = get_css_class(slug, name)

    # Build overview from scraped paragraphs
    overview_paragraphs = content.get('paragraphs', [])[:3]
    if not overview_paragraphs:
        overview_paragraphs = [f"The {name} module allows you to add {name.lower()} elements to your Divi 5 pages using the Visual Builder."]

    overview = '\n\n'.join(overview_paragraphs)

    # Build settings info from scraped data
    settings_items = content.get('settings', [])

    # Parse settings into table rows if possible
    content_settings = []
    design_settings = []
    for item in settings_items:
        # Try to detect setting names from list items
        if ':' in item:
            parts = item.split(':', 1)
            setting_name = parts[0].strip()
            desc = parts[1].strip()
            if len(setting_name) < 50:
                content_settings.append((setting_name, 'text', '—', desc))

    # Generate the Markdown
    related_links = '\n'.join([f'- [{r.replace("-", " ").title()}]({r}.md)' for r in related])
    related_frontmatter = json.dumps(related) if related else '[]'

    doc = f"""---
title: "{name}"
category: modules
tags: {json.dumps(tags)}
related: {related_frontmatter}
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "{source_url}"
---

# {name}

The {name} module is a Divi 5 content element used in the Visual Builder.

## Overview

{overview}

![{name} module overview](../assets/screenshots/modules/{slug}/overview.png){{ loading=lazy }}
*The {name} module as it appears in the Divi 5 Visual Builder.*

## Settings & Options

### Content Tab

<!-- TODO: Verify all Content tab settings for {name} module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
"""

    if content_settings:
        for setting_name, stype, default, desc in content_settings[:10]:
            doc += f'| {setting_name} | {stype} | {default} | {desc} |\n'
    else:
        doc += f'| <!-- TODO: Document Content settings --> | | | |\n'

    doc += f"""
![{name} Content tab settings](../assets/screenshots/modules/{slug}/settings-content.png){{ loading=lazy }}

### Design Tab

<!-- TODO: Verify all Design tab settings for {name} module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO: Document Design settings --> | | | |

![{name} Design tab settings](../assets/screenshots/modules/{slug}/settings-design.png){{ loading=lazy }}

### Advanced Tab

<!-- TODO: Verify all Advanced tab settings for {name} module -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| CSS ID | text | — | Assign a unique CSS ID to the module |
| CSS Class | text | — | Assign CSS classes to the module |
| Custom CSS | code | — | Add custom CSS directly to the module's elements |
| Visibility | toggle | Show on all devices | Control device visibility (desktop, tablet, phone) |
| Transition | select | Default | Animation transition style for hover effects |

## Code Examples

### Custom CSS

```css
/* Style the {name} module */
{css_class} {{
    /* Add your custom styles */
    margin-bottom: 30px;
}}

/* Responsive adjustments */
@media (max-width: 980px) {{
    {css_class} {{
        padding: 20px;
    }}
}}
```

### PHP Hooks

```php
/* Filter the {name} module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {{
    if ('{css_class.replace(".", "et_pb_")}' !== $render_slug) {{
        return $output;
    }}
    // Modify $output as needed
    return $output;
}}, 10, 2);
```

## Common Patterns

<!-- TODO: Add 2-3 real-world usage patterns with screenshots -->

1. **Basic Usage** — Add the {name} module to any row in the Visual Builder and configure its settings.

2. **Styled Variation** — Use the Design tab to customize fonts, colors, and spacing to match your site's design system.

3. **Dynamic Content** — Use dynamic content fields to pull data from custom fields or post meta.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the {name} module doesn't appear on the front end, verify that:

    - The module is not inside a disabled section or row
    - Visibility settings aren't hiding it on the current device
    - Any required fields (like URLs or content) are filled in

<!-- TODO: Add module-specific troubleshooting items -->

## Related

{related_links if related_links else '<!-- TODO: Add related module links -->'}
"""

    return doc


def main():
    """Main scraping and generation loop."""
    generated = []
    skipped = []
    errors = []

    total = len(MODULE_MAP)
    for i, (url, (slug, name, category)) in enumerate(sorted(MODULE_MAP.items(), key=lambda x: x[1][1]), 1):
        filepath = os.path.join(DOCS_DIR, f'{slug}.md')

        # Skip if already exists (manual content)
        if os.path.exists(filepath):
            print(f"[{i}/{total}] SKIP (exists): {name} -> {slug}.md")
            skipped.append(slug)
            continue

        print(f"[{i}/{total}] Scraping: {name} ({url})")

        soup = fetch_page(url)
        if soup:
            content = extract_content(soup)
        else:
            content = {'paragraphs': [], 'settings': [], 'headings': []}
            errors.append(slug)

        doc = generate_doc_page(slug, name, url, content, category)

        with open(filepath, 'w') as f:
            f.write(doc)

        generated.append(slug)
        print(f"  -> Generated {slug}.md")

        # Be polite to the server
        time.sleep(0.5)

    print(f"\n=== SUMMARY ===")
    print(f"Generated: {len(generated)} modules")
    print(f"Skipped (existing): {len(skipped)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print(f"Error modules: {', '.join(errors)}")

    return generated


if __name__ == '__main__':
    main()
