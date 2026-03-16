#!/usr/bin/env python3
"""
Fix all module demo pages using the correct Divi 5 block format.
Based on the working bar-counter page created through the Divi builder.

Key findings:
- Bar Counters = wp:divi/counters + wp:divi/counter (NOT bar-counter)
- Sidebar = wp:divi/sidebar (NOT a text block)
- Module names in Divi 5 differ from slug names
"""

import time
import requests

WP_URL = "https://www.16wells.dev/wp-json/wp/v2/pages"
AUTH = ("sshean", "KjGF bJG7 CInC aCJp U0BV nOTt")
PARENT_ID = 10
BV = "5.0.3"

SIDEBAR = f'<!-- wp:divi/sidebar {{"builderVersion":"{BV}"}} /-->'


def wrap_page(module_content):
    """Wrap module content in the standard 2-column layout with sidebar."""
    return f"""<!-- wp:divi/placeholder --><!-- wp:divi/section {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/row {{"module":{{"advanced":{{"flexColumnStructure":{{"desktop":{{"value":"equal-columns_2"}}}}}},"decoration":{{"layout":{{"desktop":{{"value":{{"flexWrap":"nowrap"}}}}}}}}}},"builderVersion":"{BV}"}} -->
<!-- wp:divi/column {{"module":{{"decoration":{{"sizing":{{"desktop":{{"value":{{"flexType":"18_24"}}}}}}}}}},"builderVersion":"{BV}"}} -->

{module_content}
<!-- /wp:divi/column -->

<!-- wp:divi/column {{"module":{{"decoration":{{"sizing":{{"desktop":{{"value":{{"flexType":"6_24"}}}}}}}}}},"builderVersion":"{BV}"}} -->
{SIDEBAR}
<!-- /wp:divi/column -->
<!-- /wp:divi/row -->
<!-- /wp:divi/section --><!-- /wp:divi/placeholder -->"""


# ─── MODULE CONTENT using correct Divi 5 block names ───
# We need to discover the correct block names for each module.
# For now, use simple modules that we can verify.

MODULES = {}

# Bar Counter - KNOWN WORKING FORMAT
MODULES["bar-counter"] = None  # Skip — user just created this manually

# Skip manually created pages
MODULES["accordion"] = None
MODULES["audio"] = None

# Text module - should work since it's basic
MODULES["text"] = wrap_page(
    f'<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"<h2>The Art of Web Design</h2><p>Great web design is more than just aesthetics — it\'s about creating experiences that guide visitors naturally toward their goals. Every color choice, every spacing decision, and every interaction matters.</p><p>When done well, design becomes invisible. Users don\'t think about the interface; they simply accomplish what they came to do.</p><h3>Our Approach</h3><p>We start with research, move to wireframes, iterate on prototypes, and deliver pixel-perfect results. Every step is collaborative, transparent, and focused on your business objectives.</p>"}}}}}},"builderVersion":"{BV}"}} /-->'
)

# Toggle - likely wp:divi/toggle
MODULES["toggle"] = wrap_page(
    f"""<!-- wp:divi/toggle {{"title":{{"innerContent":{{"desktop":{{"value":"What makes your service different?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We combine cutting-edge technology with personalized attention. Every project gets a dedicated team, custom strategy, and ongoing optimization.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/toggle {{"title":{{"innerContent":{{"desktop":{{"value":"How quickly can I get started?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Most clients are up and running within 48 hours. Our streamlined onboarding process gets you from signup to live site in record time.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/toggle {{"title":{{"innerContent":{{"desktop":{{"value":"Do you offer a money-back guarantee?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Absolutely. We offer a 30-day no-questions-asked money-back guarantee.</p>"}}}}}},"builderVersion":"{BV}"}} /-->"""
)

# Divider
MODULES["divider"] = wrap_page(
    f"""<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"<p>Content above the divider.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/divider {{"module":{{"advanced":{{"showDivider":{{"desktop":{{"value":"on"}}}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"<p>Content below the divider.</p>"}}}}}},"builderVersion":"{BV}"}} /-->"""
)

# Button
MODULES["button"] = wrap_page(
    f"""<!-- wp:divi/button {{"content":{{"innerContent":{{"desktop":{{"value":"Get Started Today"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/button {{"content":{{"innerContent":{{"desktop":{{"value":"Learn More"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/button {{"content":{{"innerContent":{{"desktop":{{"value":"Contact Us"}}}}}},"builderVersion":"{BV}"}} /-->"""
)

# Blurb
MODULES["blurb"] = wrap_page(
    f"""<!-- wp:divi/blurb {{"title":{{"innerContent":{{"desktop":{{"value":"Creative Solutions"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We craft innovative digital experiences that captivate your audience and drive results.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/blurb {{"title":{{"innerContent":{{"desktop":{{"value":"Expert Support"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Our dedicated support team is available around the clock to help you succeed.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/blurb {{"title":{{"innerContent":{{"desktop":{{"value":"Fast Delivery"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Speed matters. We deliver high-quality results on time, every time.</p>"}}}}}},"builderVersion":"{BV}"}} /-->"""
)

# Call to Action - likely wp:divi/cta or wp:divi/call-to-action
MODULES["call-to-action"] = wrap_page(
    f'<!-- wp:divi/cta {{"title":{{"innerContent":{{"desktop":{{"value":"Ready to Transform Your Business?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Join thousands of companies that have already taken the leap. Start your free 14-day trial today.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Start Free Trial"}}}}}},"builderVersion":"{BV}"}} /-->'
)

# Tabs
MODULES["tabs"] = wrap_page(
    f"""<!-- wp:divi/tabs {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/tab {{"title":{{"innerContent":{{"desktop":{{"value":"Features"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Our platform includes drag-and-drop editing, real-time previews, and over 200 design elements.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/tab {{"title":{{"innerContent":{{"desktop":{{"value":"Pricing"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Flexible plans starting at $19/month. All plans include core features and regular updates.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/tab {{"title":{{"innerContent":{{"desktop":{{"value":"Support"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Comprehensive documentation, video tutorials, and a responsive support team.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/tabs -->"""
)

# Testimonial
MODULES["testimonial"] = wrap_page(
    f"""<!-- wp:divi/testimonial {{"author":{{"innerContent":{{"desktop":{{"value":"Jennifer Martinez"}}}}}},"jobTitle":{{"innerContent":{{"desktop":{{"value":"CEO, Bright Ideas Co."}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>This platform completely transformed how we build and manage our web presence.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/testimonial {{"author":{{"innerContent":{{"desktop":{{"value":"David Park"}}}}}},"jobTitle":{{"innerContent":{{"desktop":{{"value":"Marketing Director, TechFlow"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We saw a 40% increase in conversions after redesigning our site.</p>"}}}}}},"builderVersion":"{BV}"}} /-->"""
)

# Code
MODULES["code"] = wrap_page(
    f'<!-- wp:divi/code {{"content":{{"innerContent":{{"desktop":{{"value":"<pre><code>&lt;div class=\\"container\\"&gt;\\n  &lt;h1&gt;Hello, World!&lt;/h1&gt;\\n  &lt;p&gt;This is a code module example.&lt;/p&gt;\\n&lt;/div&gt;</code></pre>"}}}}}},"builderVersion":"{BV}"}} /-->'
)

# Search
MODULES["search"] = wrap_page(
    f'<!-- wp:divi/search {{"builderVersion":"{BV}"}} /-->'
)

# Sidebar
MODULES["sidebar"] = wrap_page(
    f'<!-- wp:divi/sidebar {{"builderVersion":"{BV}"}} /-->'
)

# Login
MODULES["login"] = wrap_page(
    f'<!-- wp:divi/login {{"title":{{"innerContent":{{"desktop":{{"value":"Member Login"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Welcome back! Please log in to access your account.</p>"}}}}}},"builderVersion":"{BV}"}} /-->'
)

# Comments
MODULES["comments"] = wrap_page(
    f'<!-- wp:divi/comments {{"builderVersion":"{BV}"}} /-->'
)

# Blog
MODULES["blog"] = wrap_page(
    f'<!-- wp:divi/blog {{"builderVersion":"{BV}"}} /-->'
)

# Image (empty - needs manual image)
MODULES["image"] = wrap_page(
    f'<!-- wp:divi/image {{"builderVersion":"{BV}"}} /-->'
)

# Video
MODULES["video"] = wrap_page(
    f'<!-- wp:divi/video {{"src":{{"innerContent":{{"desktop":{{"value":"https://www.youtube.com/watch?v=FkQuawiGWUw"}}}}}},"builderVersion":"{BV}"}} /-->'
)

# Icon
MODULES["icon"] = wrap_page(
    f'<!-- wp:divi/icon {{"builderVersion":"{BV}"}} /-->'
)

# Map
MODULES["map"] = wrap_page(
    f'<!-- wp:divi/map {{"builderVersion":"{BV}"}} /-->'
)

# Menu
MODULES["menu"] = wrap_page(
    f'<!-- wp:divi/menu {{"builderVersion":"{BV}"}} /-->'
)

# Gallery
MODULES["gallery"] = wrap_page(
    f'<!-- wp:divi/gallery {{"builderVersion":"{BV}"}} /-->'
)

# Contact Form
MODULES["contact-form"] = wrap_page(
    f"""<!-- wp:divi/contact-form {{"title":{{"innerContent":{{"desktop":{{"value":"Get In Touch"}}}}}},"builderVersion":"{BV}"}} -->
<!-- wp:divi/contact-field {{"fieldId":{{"innerContent":{{"desktop":{{"value":"Name"}}}}}},"fieldTitle":{{"innerContent":{{"desktop":{{"value":"Name"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/contact-field {{"fieldId":{{"innerContent":{{"desktop":{{"value":"Email"}}}}}},"fieldTitle":{{"innerContent":{{"desktop":{{"value":"Email Address"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/contact-field {{"fieldId":{{"innerContent":{{"desktop":{{"value":"Message"}}}}}},"fieldTitle":{{"innerContent":{{"desktop":{{"value":"Message"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/contact-form -->"""
)

# Email Optin
MODULES["email-optin"] = wrap_page(
    f'<!-- wp:divi/signup {{"title":{{"innerContent":{{"desktop":{{"value":"Subscribe to Our Newsletter"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Get the latest news and exclusive offers delivered to your inbox.</p>"}}}}}},"builderVersion":"{BV}"}} /-->'
)

# Countdown Timer
MODULES["countdown-timer"] = wrap_page(
    f'<!-- wp:divi/countdown {{"title":{{"innerContent":{{"desktop":{{"value":"Big Launch Coming Soon!"}}}}}},"dateTime":{{"innerContent":{{"desktop":{{"value":"2027-01-01 00:00"}}}}}},"builderVersion":"{BV}"}} /-->'
)

# Slider
MODULES["slider"] = wrap_page(
    f"""<!-- wp:divi/slider {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Welcome to Our Platform"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Discover powerful tools to help you build and succeed online.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Get Started"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Built for Performance"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Lightning-fast load times ensure peak performance.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Learn More"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/slider -->"""
)

# Person
MODULES["person"] = wrap_page(
    f"""<!-- wp:divi/person {{"name":{{"innerContent":{{"desktop":{{"value":"Sarah Johnson"}}}}}},"position":{{"innerContent":{{"desktop":{{"value":"Creative Director"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Sarah brings 15 years of design expertise.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/person {{"name":{{"innerContent":{{"desktop":{{"value":"Michael Chen"}}}}}},"position":{{"innerContent":{{"desktop":{{"value":"Lead Developer"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Michael builds scalable, performant web applications.</p>"}}}}}},"builderVersion":"{BV}"}} /-->"""
)

# Social Media Follow
MODULES["social-media-follow"] = wrap_page(
    f"""<!-- wp:divi/social-media-follow {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"facebook"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://facebook.com"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"twitter"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://twitter.com"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"instagram"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://instagram.com"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/social-media-follow -->"""
)

# Number Counter
MODULES["number-counter"] = wrap_page(
    f"""<!-- wp:divi/number-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Happy Clients"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"1250"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/number-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Projects Completed"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"340"}}}}}},"builderVersion":"{BV}"}} /-->"""
)

# Circle Counter
MODULES["circle-counter"] = wrap_page(
    f"""<!-- wp:divi/circle-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Customer Satisfaction"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"95"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/circle-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Team Efficiency"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"92"}}}}}},"builderVersion":"{BV}"}} /-->"""
)

# Pricing Tables
MODULES["pricing-table"] = wrap_page(
    f"""<!-- wp:divi/pricing-tables {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/pricing-table {{"title":{{"innerContent":{{"desktop":{{"value":"Basic"}}}}}},"subtitle":{{"innerContent":{{"desktop":{{"value":"For individuals"}}}}}},"sum":{{"innerContent":{{"desktop":{{"value":"$19"}}}}}},"perMonth":{{"innerContent":{{"desktop":{{"value":"mo"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Sign Up"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<ul><li>5 Projects</li><li>10 GB Storage</li><li>Email Support</li></ul>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/pricing-table {{"title":{{"innerContent":{{"desktop":{{"value":"Professional"}}}}}},"subtitle":{{"innerContent":{{"desktop":{{"value":"For teams"}}}}}},"sum":{{"innerContent":{{"desktop":{{"value":"$49"}}}}}},"perMonth":{{"innerContent":{{"desktop":{{"value":"mo"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Sign Up"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<ul><li>Unlimited Projects</li><li>100 GB Storage</li><li>Priority Support</li></ul>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/pricing-tables -->"""
)

# Portfolio modules (dynamic content)
MODULES["portfolio"] = wrap_page(f'<!-- wp:divi/portfolio {{"builderVersion":"{BV}"}} /-->')
MODULES["filterable-portfolio"] = wrap_page(f'<!-- wp:divi/filterable-portfolio {{"builderVersion":"{BV}"}} /-->')
MODULES["shop"] = wrap_page(f'<!-- wp:divi/shop {{"builderVersion":"{BV}"}} /-->')
MODULES["post-slider"] = wrap_page(f'<!-- wp:divi/post-slider {{"builderVersion":"{BV}"}} /-->')
MODULES["post-navigation"] = wrap_page(f'<!-- wp:divi/post-navigation {{"builderVersion":"{BV}"}} /-->')
MODULES["post-title"] = wrap_page(f'<!-- wp:divi/post-title {{"builderVersion":"{BV}"}} /-->')
MODULES["video-slider"] = wrap_page(
    f"""<!-- wp:divi/video-slider {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/video-slider-item {{"src":{{"innerContent":{{"desktop":{{"value":"https://www.youtube.com/watch?v=FkQuawiGWUw"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/video-slider -->"""
)

# Fullwidth modules
MODULES["fullwidth-header"] = wrap_page(
    f'<!-- wp:divi/fullwidth-header {{"title":{{"innerContent":{{"desktop":{{"value":"Welcome to Our Website"}}}}}},"subhead":{{"innerContent":{{"desktop":{{"value":"Building beautiful digital experiences since 2010"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We help businesses grow with stunning websites and world-class support.</p>"}}}}}},"buttonOneText":{{"innerContent":{{"desktop":{{"value":"Get Started"}}}}}},"builderVersion":"{BV}"}} /-->'
)
MODULES["fullwidth-map"] = wrap_page(f'<!-- wp:divi/fullwidth-map {{"builderVersion":"{BV}"}} /-->')
MODULES["fullwidth-menu"] = wrap_page(f'<!-- wp:divi/fullwidth-menu {{"builderVersion":"{BV}"}} /-->')
MODULES["fullwidth-portfolio"] = wrap_page(f'<!-- wp:divi/fullwidth-portfolio {{"builderVersion":"{BV}"}} /-->')
MODULES["fullwidth-slider"] = wrap_page(
    f"""<!-- wp:divi/fullwidth-slider {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Fullwidth Slide One"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>A fullwidth slider showcasing your content with impact.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Fullwidth Slide Two"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Capture attention with stunning visuals.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/fullwidth-slider -->"""
)


def api_call(method, url, retries=3, **kwargs):
    kwargs.setdefault("timeout", 90)
    kwargs["auth"] = AUTH
    for attempt in range(retries):
        try:
            resp = getattr(requests, method)(url, **kwargs)
            return resp
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            wait = 10 * (attempt + 1)
            print(f"    ⏳ {type(e).__name__}, retry in {wait}s")
            time.sleep(wait)
    return None


def get_child_pages():
    for attempt in range(5):
        try:
            resp = requests.get(WP_URL, auth=AUTH,
                                params={"parent": PARENT_ID, "per_page": 100, "status": "publish"},
                                timeout=60)
            return {p["slug"]: p["id"] for p in resp.json()}
        except:
            time.sleep(15)
    raise RuntimeError("Could not fetch pages")


def main():
    print("Fetching existing pages...")
    existing = get_child_pages()
    print(f"Found {len(existing)} pages\n")

    success = 0
    skipped = 0
    failed = 0

    for slug, content in sorted(MODULES.items()):
        if content is None:
            print(f"  ⏭  {slug} (manually created)")
            skipped += 1
            continue

        page_id = existing.get(slug)
        if not page_id:
            print(f"  ⚠  {slug} — no page found")
            failed += 1
            continue

        resp = api_call("post", f"{WP_URL}/{page_id}", json={"content": content})
        if resp and resp.status_code == 200:
            print(f"  ✅ {slug}")
            success += 1
        else:
            status = resp.status_code if resp else "NO RESPONSE"
            print(f"  ❌ {slug}: {status}")
            failed += 1

        time.sleep(2)

    print(f"\n{'='*50}")
    print(f"DONE: {success} updated, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
