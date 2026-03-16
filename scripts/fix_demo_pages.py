#!/usr/bin/env python3
"""
Fix all module demo pages: put the actual Divi module blocks in the left column
and the sidebar nav links in the right column.
"""

import json
import re
import time
import requests

WP_URL = "https://www.16wells.dev/wp-json/wp/v2/pages"
AUTH = ("sshean", "KjGF bJG7 CInC aCJp U0BV nOTt")
PARENT_ID = 10
BV = "5.0.3"


def get_child_pages(retries=5):
    for attempt in range(retries):
        try:
            resp = requests.get(WP_URL, auth=AUTH,
                                params={"parent": PARENT_ID, "per_page": 100, "status": "publish"},
                                timeout=60)
            return sorted(resp.json(), key=lambda x: x["title"]["rendered"])
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            wait = 15 * (attempt + 1)
            print(f"  Fetch failed: {type(e).__name__}, retry in {wait}s")
            time.sleep(wait)
    raise RuntimeError("Could not fetch child pages")


def build_sidebar_html(pages):
    links = []
    for p in pages:
        title = p["title"]["rendered"]
        slug = p["slug"]
        links.append(f'<li><a href="/module-demos/{slug}/">{title}</a></li>')
    return '<h4>Module Demos</h4><ul>' + "".join(links) + "</ul>"


def api_call(method, url, retries=3, **kwargs):
    """Make an API call with retry logic."""
    kwargs.setdefault("timeout", 90)
    kwargs["auth"] = AUTH
    for attempt in range(retries):
        try:
            resp = getattr(requests, method)(url, **kwargs)
            return resp
        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError) as e:
            wait = 10 * (attempt + 1)
            print(f"    ⏳ {type(e).__name__}, retry in {wait}s ({attempt+2}/{retries})")
            time.sleep(wait)
    return None


# ─── MODULE CONTENT DEFINITIONS ───
# These are the actual Divi block contents for each module (NOT wrapped in section/row/column)

MODULE_CONTENT = {}

MODULE_CONTENT["accordion"] = None  # Skip — user created this manually

MODULE_CONTENT["audio"] = None  # Skip — user created this manually

MODULE_CONTENT["bar-counter"] = f"""<!-- wp:divi/bar-counter {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/bar-counter-item {{"title":{{"innerContent":{{"desktop":{{"value":"Web Design"}}}}}},"percent":{{"innerContent":{{"desktop":{{"value":"90"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/bar-counter-item {{"title":{{"innerContent":{{"desktop":{{"value":"SEO Optimization"}}}}}},"percent":{{"innerContent":{{"desktop":{{"value":"75"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/bar-counter-item {{"title":{{"innerContent":{{"desktop":{{"value":"Content Strategy"}}}}}},"percent":{{"innerContent":{{"desktop":{{"value":"85"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/bar-counter-item {{"title":{{"innerContent":{{"desktop":{{"value":"Social Media"}}}}}},"percent":{{"innerContent":{{"desktop":{{"value":"60"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/bar-counter -->"""

MODULE_CONTENT["blog"] = f'<!-- wp:divi/blog {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"6"}}}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["blurb"] = f"""<!-- wp:divi/blurb {{"title":{{"innerContent":{{"desktop":{{"value":"Creative Solutions"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We craft innovative digital experiences that captivate your audience and drive results. From concept to launch, our team delivers excellence at every step.</p>"}}}}}},"module":{{"advanced":{{"useIcon":{{"desktop":{{"value":"on"}}}},"fontIcon":{{"desktop":{{"value":"&#xe08b;||divi||400"}}}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/blurb {{"title":{{"innerContent":{{"desktop":{{"value":"Expert Support"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Our dedicated support team is available around the clock to help you succeed. Get expert guidance whenever you need it.</p>"}}}}}},"module":{{"advanced":{{"useIcon":{{"desktop":{{"value":"on"}}}},"fontIcon":{{"desktop":{{"value":"&#xe0a4;||divi||400"}}}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/blurb {{"title":{{"innerContent":{{"desktop":{{"value":"Fast Delivery"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Speed matters. We streamline our workflow to deliver high-quality results on time, every time.</p>"}}}}}},"module":{{"advanced":{{"useIcon":{{"desktop":{{"value":"on"}}}},"fontIcon":{{"desktop":{{"value":"&#xe024;||divi||400"}}}}}}}},"builderVersion":"{BV}"}} /-->"""

MODULE_CONTENT["button"] = f"""<!-- wp:divi/button {{"content":{{"innerContent":{{"desktop":{{"value":"Get Started Today"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/button {{"content":{{"innerContent":{{"desktop":{{"value":"Learn More"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/button {{"content":{{"innerContent":{{"desktop":{{"value":"Contact Us"}}}}}},"builderVersion":"{BV}"}} /-->"""

MODULE_CONTENT["call-to-action"] = f'<!-- wp:divi/call-to-action {{"title":{{"innerContent":{{"desktop":{{"value":"Ready to Transform Your Business?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Join thousands of companies that have already taken the leap. Start your free 14-day trial today.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Start Free Trial"}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["circle-counter"] = f"""<!-- wp:divi/circle-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Customer Satisfaction"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"95"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/circle-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Project Completion"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"87"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/circle-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Team Efficiency"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"92"}}}}}},"builderVersion":"{BV}"}} /-->"""

MODULE_CONTENT["code"] = f'<!-- wp:divi/code {{"content":{{"innerContent":{{"desktop":{{"value":"<pre><code>&lt;div class=\\"container\\"&gt;\\n  &lt;h1&gt;Hello, World!&lt;/h1&gt;\\n  &lt;p&gt;This is a code module example.&lt;/p&gt;\\n  &lt;button onclick=\\"alert(\'Clicked!\');\\"&gt;Click Me&lt;/button&gt;\\n&lt;/div&gt;</code></pre>"}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["comments"] = f'<!-- wp:divi/comments {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["contact-form"] = f"""<!-- wp:divi/contact-form {{"title":{{"innerContent":{{"desktop":{{"value":"Get In Touch"}}}}}},"builderVersion":"{BV}"}} -->
<!-- wp:divi/contact-field {{"fieldId":{{"innerContent":{{"desktop":{{"value":"Name"}}}}}},"fieldTitle":{{"innerContent":{{"desktop":{{"value":"Name"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/contact-field {{"fieldId":{{"innerContent":{{"desktop":{{"value":"Email"}}}}}},"fieldTitle":{{"innerContent":{{"desktop":{{"value":"Email Address"}}}}}},"fieldType":{{"innerContent":{{"desktop":{{"value":"email"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/contact-field {{"fieldId":{{"innerContent":{{"desktop":{{"value":"Message"}}}}}},"fieldTitle":{{"innerContent":{{"desktop":{{"value":"Message"}}}}}},"fieldType":{{"innerContent":{{"desktop":{{"value":"text"}}}}}},"fullwidth":{{"innerContent":{{"desktop":{{"value":"on"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/contact-form -->"""

MODULE_CONTENT["countdown-timer"] = f'<!-- wp:divi/countdown-timer {{"title":{{"innerContent":{{"desktop":{{"value":"Big Launch Coming Soon!"}}}}}},"dateTime":{{"innerContent":{{"desktop":{{"value":"2027-01-01 00:00"}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["divider"] = f"""<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"<p>Content above the divider.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/divider {{"module":{{"advanced":{{"showDivider":{{"desktop":{{"value":"on"}}}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"<p>Content below the divider.</p>"}}}}}},"builderVersion":"{BV}"}} /-->"""

MODULE_CONTENT["email-optin"] = f'<!-- wp:divi/email-optin {{"title":{{"innerContent":{{"desktop":{{"value":"Subscribe to Our Newsletter"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Get the latest news, tips, and exclusive offers delivered straight to your inbox.</p>"}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["filterable-portfolio"] = f'<!-- wp:divi/filterable-portfolio {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"8"}}}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["fullwidth-header"] = f'<!-- wp:divi/fullwidth-header {{"title":{{"innerContent":{{"desktop":{{"value":"Welcome to Our Website"}}}}}},"subhead":{{"innerContent":{{"desktop":{{"value":"Building beautiful digital experiences since 2010"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We help businesses grow with stunning websites, powerful marketing tools, and world-class support.</p>"}}}}}},"buttonOneText":{{"innerContent":{{"desktop":{{"value":"Get Started"}}}}}},"buttonTwoText":{{"innerContent":{{"desktop":{{"value":"Learn More"}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["fullwidth-map"] = f'<!-- wp:divi/fullwidth-map {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["fullwidth-menu"] = f'<!-- wp:divi/fullwidth-menu {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["fullwidth-portfolio"] = f'<!-- wp:divi/fullwidth-portfolio {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"8"}}}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["fullwidth-slider"] = f"""<!-- wp:divi/fullwidth-slider {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Fullwidth Slide One"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>A beautiful fullwidth slider showcasing your most important content with impact.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Explore"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Fullwidth Slide Two"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Capture attention with stunning visuals and compelling calls to action.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Discover"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/fullwidth-slider -->"""

MODULE_CONTENT["gallery"] = f'<!-- wp:divi/gallery {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"8"}}}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["icon"] = f"""<!-- wp:divi/icon {{"module":{{"advanced":{{"fontIcon":{{"desktop":{{"value":"&#xe08b;||divi||400"}}}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/icon {{"module":{{"advanced":{{"fontIcon":{{"desktop":{{"value":"&#xe0a4;||divi||400"}}}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/icon {{"module":{{"advanced":{{"fontIcon":{{"desktop":{{"value":"&#xe024;||divi||400"}}}}}}}},"builderVersion":"{BV}"}} /-->"""

MODULE_CONTENT["image"] = f'<!-- wp:divi/image {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["login"] = f'<!-- wp:divi/login {{"title":{{"innerContent":{{"desktop":{{"value":"Member Login"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Welcome back! Please log in to access your account and exclusive member content.</p>"}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["map"] = f'<!-- wp:divi/map {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["menu"] = f'<!-- wp:divi/menu {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["number-counter"] = f"""<!-- wp:divi/number-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Happy Clients"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"1250"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/number-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Projects Completed"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"340"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/number-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Awards Won"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"15"}}}}}},"builderVersion":"{BV}"}} /-->"""

MODULE_CONTENT["person"] = f"""<!-- wp:divi/person {{"name":{{"innerContent":{{"desktop":{{"value":"Sarah Johnson"}}}}}},"position":{{"innerContent":{{"desktop":{{"value":"Creative Director"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Sarah brings 15 years of design expertise and a passion for creating beautiful, user-centered experiences.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/person {{"name":{{"innerContent":{{"desktop":{{"value":"Michael Chen"}}}}}},"position":{{"innerContent":{{"desktop":{{"value":"Lead Developer"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Michael is a full-stack developer with a knack for building scalable, performant web applications.</p>"}}}}}},"builderVersion":"{BV}"}} /-->"""

MODULE_CONTENT["portfolio"] = f'<!-- wp:divi/portfolio {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"8"}}}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["post-navigation"] = f'<!-- wp:divi/post-navigation {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["post-slider"] = f'<!-- wp:divi/post-slider {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["post-title"] = f'<!-- wp:divi/post-title {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["pricing-table"] = f"""<!-- wp:divi/pricing-tables {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/pricing-table {{"title":{{"innerContent":{{"desktop":{{"value":"Basic"}}}}}},"subtitle":{{"innerContent":{{"desktop":{{"value":"For individuals"}}}}}},"perMonth":{{"innerContent":{{"desktop":{{"value":"mo"}}}}}},"sum":{{"innerContent":{{"desktop":{{"value":"$19"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Sign Up"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<ul><li>5 Projects</li><li>10 GB Storage</li><li>Email Support</li><li>Basic Analytics</li></ul>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/pricing-table {{"title":{{"innerContent":{{"desktop":{{"value":"Professional"}}}}}},"subtitle":{{"innerContent":{{"desktop":{{"value":"For teams"}}}}}},"perMonth":{{"innerContent":{{"desktop":{{"value":"mo"}}}}}},"sum":{{"innerContent":{{"desktop":{{"value":"$49"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Sign Up"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<ul><li>Unlimited Projects</li><li>100 GB Storage</li><li>Priority Support</li><li>Advanced Analytics</li><li>API Access</li></ul>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/pricing-table {{"title":{{"innerContent":{{"desktop":{{"value":"Enterprise"}}}}}},"subtitle":{{"innerContent":{{"desktop":{{"value":"For organizations"}}}}}},"perMonth":{{"innerContent":{{"desktop":{{"value":"mo"}}}}}},"sum":{{"innerContent":{{"desktop":{{"value":"$99"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Contact Us"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<ul><li>Unlimited Everything</li><li>1 TB Storage</li><li>Dedicated Support</li><li>Custom Integrations</li><li>SLA Guarantee</li></ul>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/pricing-tables -->"""

MODULE_CONTENT["search"] = f'<!-- wp:divi/search {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["shop"] = f'<!-- wp:divi/shop {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["sidebar"] = f'<!-- wp:divi/sidebar {{"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["slider"] = f"""<!-- wp:divi/slider {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Welcome to Our Platform"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Discover powerful tools designed to help you build, grow, and succeed online.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Get Started"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Built for Performance"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Lightning-fast load times and optimized code ensure your site runs at peak performance.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Learn More"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"24/7 Expert Support"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Our team of experts is always here to help you make the most of your website.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Contact Us"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/slider -->"""

MODULE_CONTENT["social-media-follow"] = f"""<!-- wp:divi/social-media-follow {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"facebook"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://facebook.com"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"twitter"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://twitter.com"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"instagram"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://instagram.com"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"linkedin"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://linkedin.com"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/social-media-follow -->"""

MODULE_CONTENT["tabs"] = f"""<!-- wp:divi/tabs {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/tab {{"title":{{"innerContent":{{"desktop":{{"value":"Features"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Our platform includes drag-and-drop editing, real-time previews, responsive design controls, and over 200 design elements to choose from.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/tab {{"title":{{"innerContent":{{"desktop":{{"value":"Pricing"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Choose from flexible plans starting at just $19/month. All plans include core features, regular updates, and access to our support team.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- wp:divi/tab {{"title":{{"innerContent":{{"desktop":{{"value":"Support"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Get help when you need it with our comprehensive documentation, video tutorials, and responsive support team.</p>"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/tabs -->"""

MODULE_CONTENT["testimonial"] = f"""<!-- wp:divi/testimonial {{"author":{{"innerContent":{{"desktop":{{"value":"Jennifer Martinez"}}}}}},"jobTitle":{{"innerContent":{{"desktop":{{"value":"CEO, Bright Ideas Co."}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>This platform completely transformed how we build and manage our web presence. The intuitive design tools and outstanding support team made the transition seamless.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/testimonial {{"author":{{"innerContent":{{"desktop":{{"value":"David Park"}}}}}},"jobTitle":{{"innerContent":{{"desktop":{{"value":"Marketing Director, TechFlow"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We saw a 40% increase in conversions after redesigning our site. The performance optimizations and design flexibility are unmatched.</p>"}}}}}},"builderVersion":"{BV}"}} /-->"""

MODULE_CONTENT["text"] = f'<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"<h2>The Art of Web Design</h2><p>Great web design is more than just aesthetics — it\'s about creating experiences that guide visitors naturally toward their goals. Every color choice, every spacing decision, and every interaction matters.</p><p>When done well, design becomes invisible. Users don\'t think about the interface; they simply accomplish what they came to do.</p><h3>Our Approach</h3><p>We start with research, move to wireframes, iterate on prototypes, and deliver pixel-perfect results. Every step is collaborative, transparent, and focused on your business objectives.</p>"}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["toggle"] = f"""<!-- wp:divi/toggle {{"title":{{"innerContent":{{"desktop":{{"value":"What makes your service different?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We combine cutting-edge technology with personalized attention. Every project gets a dedicated team, custom strategy, and ongoing optimization.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/toggle {{"title":{{"innerContent":{{"desktop":{{"value":"How quickly can I get started?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Most clients are up and running within 48 hours. Our streamlined onboarding process gets you from signup to live site in record time.</p>"}}}}}},"builderVersion":"{BV}"}} /-->

<!-- wp:divi/toggle {{"title":{{"innerContent":{{"desktop":{{"value":"Do you offer a money-back guarantee?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Absolutely. We offer a 30-day no-questions-asked money-back guarantee.</p>"}}}}}},"builderVersion":"{BV}"}} /-->"""

MODULE_CONTENT["video"] = f'<!-- wp:divi/video {{"src":{{"innerContent":{{"desktop":{{"value":"https://www.youtube.com/watch?v=FkQuawiGWUw"}}}}}},"builderVersion":"{BV}"}} /-->'

MODULE_CONTENT["video-slider"] = f"""<!-- wp:divi/video-slider {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/video-slider-item {{"src":{{"innerContent":{{"desktop":{{"value":"https://www.youtube.com/watch?v=FkQuawiGWUw"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/video-slider -->"""


def build_page_content(module_blocks, sidebar_escaped):
    """Build full page with module in left column, sidebar in right column."""
    return f"""<!-- wp:divi/placeholder --><!-- wp:divi/section {{"builderVersion":"{BV}"}} -->
<!-- wp:divi/row {{"module":{{"advanced":{{"flexColumnStructure":{{"desktop":{{"value":"equal-columns_2"}}}}}},"decoration":{{"layout":{{"desktop":{{"value":{{"flexWrap":"nowrap"}}}}}}}}}},"builderVersion":"{BV}"}} -->
<!-- wp:divi/column {{"module":{{"decoration":{{"sizing":{{"desktop":{{"value":{{"flexType":"18_24"}}}}}}}}}},"builderVersion":"{BV}"}} -->
{module_blocks}
<!-- /wp:divi/column -->
<!-- wp:divi/column {{"module":{{"decoration":{{"sizing":{{"desktop":{{"value":{{"flexType":"6_24"}}}}}}}}}},"builderVersion":"{BV}"}} -->
<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"{sidebar_escaped}"}}}}}},"builderVersion":"{BV}"}} /-->
<!-- /wp:divi/column -->
<!-- /wp:divi/row -->
<!-- /wp:divi/section --><!-- /wp:divi/placeholder -->"""


def main():
    print("Fetching child pages...")
    pages = get_child_pages()
    print(f"Found {len(pages)} pages\n")

    sidebar_html = build_sidebar_html(pages)
    sidebar_escaped = sidebar_html.replace('"', '\\"')

    success = 0
    skipped = 0
    failed = 0

    for p in pages:
        page_id = p["id"]
        slug = p["slug"]
        title = p["title"]["rendered"]

        module_blocks = MODULE_CONTENT.get(slug)
        if module_blocks is None:
            print(f"  ⏭  {title} (skip — manually created)")
            skipped += 1
            continue

        new_content = build_page_content(module_blocks, sidebar_escaped)

        resp = api_call("post", f"{WP_URL}/{page_id}", json={"content": new_content})
        if resp and resp.status_code == 200:
            print(f"  ✅ {title}")
            success += 1
        else:
            status = resp.status_code if resp else "NO RESPONSE"
            print(f"  ❌ {title}: {status}")
            failed += 1

        time.sleep(2)

    print(f"\n{'='*50}")
    print(f"DONE: {success} fixed, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
