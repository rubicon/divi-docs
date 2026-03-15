#!/usr/bin/env python3
"""
Create Divi 5 module demo pages on 16wells.dev via WP REST API.
Each page is a child of the "Module Demos" parent page (ID 10),
uses Divi 5 block editor format, and contains realistic demo content.
"""

import json
import requests
import time
import sys

WP_URL = "https://www.16wells.dev/wp-json/wp/v2/pages"
AUTH = ("sshean", "KjGF bJG7 CInC aCJp U0BV nOTt")
PARENT_ID = 10
BUILDER_VERSION = "5.0.3"

def wrap_in_section(inner_content):
    """Wrap module content in a Divi section > row > column structure."""
    return f"""<!-- wp:divi/placeholder --><!-- wp:divi/section {{"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/row {{"module":{{"advanced":{{"flexColumnStructure":{{"desktop":{{"value":"equal-columns_1"}}}}}},"decoration":{{"layout":{{"desktop":{{"value":{{"flexWrap":"nowrap"}}}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/column {{"module":{{"decoration":{{"sizing":{{"desktop":{{"value":{{"flexType":"24_24"}}}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} -->
{inner_content}
<!-- /wp:divi/column -->
<!-- /wp:divi/row -->
<!-- /wp:divi/section --><!-- /wp:divi/placeholder -->"""

def text_module(text):
    content_html = text.replace('"', '\\"')
    return f'<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"{content_html}"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'

def e(s):
    """Escape for JSON inside block comments."""
    return s.replace('"', '\\"').replace('\n', '\\n')


# ─── MODULE DEFINITIONS ───

MODULES = {}

# ACCORDION (already exists, skip)
# AUDIO (already exists but empty, let's update it)

MODULES["audio"] = {
    "title": "Audio",
    "update_id": 20,  # existing page to update
    "content": wrap_in_section(
        f'<!-- wp:divi/audio {{"title":{{"innerContent":{{"desktop":{{"value":"Sample Audio Track"}}}}}},"artist":{{"innerContent":{{"desktop":{{"value":"Demo Artist"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["bar-counter"] = {
    "title": "Bar Counter",
    "content": wrap_in_section(
        f"""<!-- wp:divi/bar-counter {{"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/bar-counter-item {{"title":{{"innerContent":{{"desktop":{{"value":"Web Design"}}}}}},"percent":{{"innerContent":{{"desktop":{{"value":"90"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/bar-counter-item {{"title":{{"innerContent":{{"desktop":{{"value":"SEO Optimization"}}}}}},"percent":{{"innerContent":{{"desktop":{{"value":"75"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/bar-counter-item {{"title":{{"innerContent":{{"desktop":{{"value":"Content Strategy"}}}}}},"percent":{{"innerContent":{{"desktop":{{"value":"85"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/bar-counter-item {{"title":{{"innerContent":{{"desktop":{{"value":"Social Media"}}}}}},"percent":{{"innerContent":{{"desktop":{{"value":"60"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- /wp:divi/bar-counter -->"""
    )
}

MODULES["blog"] = {
    "title": "Blog",
    "content": wrap_in_section(
        f'<!-- wp:divi/blog {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"6"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["blurb"] = {
    "title": "Blurb",
    "content": wrap_in_section(
        f"""<!-- wp:divi/blurb {{"title":{{"innerContent":{{"desktop":{{"value":"Creative Solutions"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We craft innovative digital experiences that captivate your audience and drive results. From concept to launch, our team delivers excellence at every step.</p>"}}}}}},"module":{{"advanced":{{"useIcon":{{"desktop":{{"value":"on"}}}},"fontIcon":{{"desktop":{{"value":"&#xe08b;||divi||400"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/blurb {{"title":{{"innerContent":{{"desktop":{{"value":"Expert Support"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Our dedicated support team is available around the clock to help you succeed. Get expert guidance whenever you need it, no question too small.</p>"}}}}}},"module":{{"advanced":{{"useIcon":{{"desktop":{{"value":"on"}}}},"fontIcon":{{"desktop":{{"value":"&#xe0a4;||divi||400"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/blurb {{"title":{{"innerContent":{{"desktop":{{"value":"Fast Delivery"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Speed matters. We streamline our workflow to deliver high-quality results on time, every time. Your deadlines are our deadlines.</p>"}}}}}},"module":{{"advanced":{{"useIcon":{{"desktop":{{"value":"on"}}}},"fontIcon":{{"desktop":{{"value":"&#xe024;||divi||400"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["button"] = {
    "title": "Button",
    "content": wrap_in_section(
        f"""<!-- wp:divi/button {{"content":{{"innerContent":{{"desktop":{{"value":"Get Started Today"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/button {{"content":{{"innerContent":{{"desktop":{{"value":"Learn More"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/button {{"content":{{"innerContent":{{"desktop":{{"value":"Contact Us"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["call-to-action"] = {
    "title": "Call to Action",
    "content": wrap_in_section(
        f'<!-- wp:divi/call-to-action {{"title":{{"innerContent":{{"desktop":{{"value":"Ready to Transform Your Business?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Join thousands of companies that have already taken the leap. Start your free 14-day trial today and see the difference for yourself.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Start Free Trial"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["circle-counter"] = {
    "title": "Circle Counter",
    "content": wrap_in_section(
        f"""<!-- wp:divi/circle-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Customer Satisfaction"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"95"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/circle-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Project Completion"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"87"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/circle-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Team Efficiency"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"92"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["code"] = {
    "title": "Code",
    "content": wrap_in_section(
        f'<!-- wp:divi/code {{"content":{{"innerContent":{{"desktop":{{"value":"<pre><code>&lt;div class=\\"container\\"&gt;\\n  &lt;h1&gt;Hello, World!&lt;/h1&gt;\\n  &lt;p&gt;This is a code module example.&lt;/p&gt;\\n  &lt;button onclick=\\"alert(\'Clicked!\');\\"&gt;Click Me&lt;/button&gt;\\n&lt;/div&gt;</code></pre>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["comments"] = {
    "title": "Comments",
    "content": wrap_in_section(
        f'<!-- wp:divi/comments {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["contact-form"] = {
    "title": "Contact Form",
    "content": wrap_in_section(
        f"""<!-- wp:divi/contact-form {{"title":{{"innerContent":{{"desktop":{{"value":"Get In Touch"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/contact-field {{"fieldId":{{"innerContent":{{"desktop":{{"value":"Name"}}}}}},"fieldTitle":{{"innerContent":{{"desktop":{{"value":"Name"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/contact-field {{"fieldId":{{"innerContent":{{"desktop":{{"value":"Email"}}}}}},"fieldTitle":{{"innerContent":{{"desktop":{{"value":"Email Address"}}}}}},"fieldType":{{"innerContent":{{"desktop":{{"value":"email"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/contact-field {{"fieldId":{{"innerContent":{{"desktop":{{"value":"Message"}}}}}},"fieldTitle":{{"innerContent":{{"desktop":{{"value":"Message"}}}}}},"fieldType":{{"innerContent":{{"desktop":{{"value":"text"}}}}}},"fullwidth":{{"innerContent":{{"desktop":{{"value":"on"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- /wp:divi/contact-form -->"""
    )
}

MODULES["countdown-timer"] = {
    "title": "Countdown Timer",
    "content": wrap_in_section(
        f'<!-- wp:divi/countdown-timer {{"title":{{"innerContent":{{"desktop":{{"value":"Big Launch Coming Soon!"}}}}}},"dateTime":{{"innerContent":{{"desktop":{{"value":"2027-01-01 00:00"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["divider"] = {
    "title": "Divider",
    "content": wrap_in_section(
        f"""<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"<p>Content above the divider.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/divider {{"module":{{"advanced":{{"showDivider":{{"desktop":{{"value":"on"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"<p>Content below the divider.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["email-optin"] = {
    "title": "Email Optin",
    "content": wrap_in_section(
        f'<!-- wp:divi/email-optin {{"title":{{"innerContent":{{"desktop":{{"value":"Subscribe to Our Newsletter"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Get the latest news, tips, and exclusive offers delivered straight to your inbox. No spam, ever.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["gallery"] = {
    "title": "Gallery",
    "content": wrap_in_section(
        f'<!-- wp:divi/gallery {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"8"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["icon"] = {
    "title": "Icon",
    "content": wrap_in_section(
        f"""<!-- wp:divi/icon {{"module":{{"advanced":{{"fontIcon":{{"desktop":{{"value":"&#xe08b;||divi||400"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/icon {{"module":{{"advanced":{{"fontIcon":{{"desktop":{{"value":"&#xe0a4;||divi||400"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/icon {{"module":{{"advanced":{{"fontIcon":{{"desktop":{{"value":"&#xe024;||divi||400"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["image"] = {
    "title": "Image",
    "content": wrap_in_section(
        f'<!-- wp:divi/image {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["login"] = {
    "title": "Login",
    "content": wrap_in_section(
        f'<!-- wp:divi/login {{"title":{{"innerContent":{{"desktop":{{"value":"Member Login"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Welcome back! Please log in to access your account and exclusive member content.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["map"] = {
    "title": "Map",
    "content": wrap_in_section(
        f'<!-- wp:divi/map {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["menu"] = {
    "title": "Menu",
    "content": wrap_in_section(
        f'<!-- wp:divi/menu {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["number-counter"] = {
    "title": "Number Counter",
    "content": wrap_in_section(
        f"""<!-- wp:divi/number-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Happy Clients"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"1250"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/number-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Projects Completed"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"340"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/number-counter {{"title":{{"innerContent":{{"desktop":{{"value":"Awards Won"}}}}}},"number":{{"innerContent":{{"desktop":{{"value":"15"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["person"] = {
    "title": "Person",
    "content": wrap_in_section(
        f"""<!-- wp:divi/person {{"name":{{"innerContent":{{"desktop":{{"value":"Sarah Johnson"}}}}}},"position":{{"innerContent":{{"desktop":{{"value":"Creative Director"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Sarah brings 15 years of design expertise and a passion for creating beautiful, user-centered experiences.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/person {{"name":{{"innerContent":{{"desktop":{{"value":"Michael Chen"}}}}}},"position":{{"innerContent":{{"desktop":{{"value":"Lead Developer"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Michael is a full-stack developer with a knack for building scalable, performant web applications.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["pricing-table"] = {
    "title": "Pricing Table",
    "content": wrap_in_section(
        f"""<!-- wp:divi/pricing-tables {{"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/pricing-table {{"title":{{"innerContent":{{"desktop":{{"value":"Basic"}}}}}},"subtitle":{{"innerContent":{{"desktop":{{"value":"For individuals"}}}}}},"perMonth":{{"innerContent":{{"desktop":{{"value":"mo"}}}}}},"sum":{{"innerContent":{{"desktop":{{"value":"$19"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Sign Up"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<ul><li>5 Projects</li><li>10 GB Storage</li><li>Email Support</li><li>Basic Analytics</li></ul>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/pricing-table {{"title":{{"innerContent":{{"desktop":{{"value":"Professional"}}}}}},"subtitle":{{"innerContent":{{"desktop":{{"value":"For teams"}}}}}},"perMonth":{{"innerContent":{{"desktop":{{"value":"mo"}}}}}},"sum":{{"innerContent":{{"desktop":{{"value":"$49"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Sign Up"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<ul><li>Unlimited Projects</li><li>100 GB Storage</li><li>Priority Support</li><li>Advanced Analytics</li><li>API Access</li></ul>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/pricing-table {{"title":{{"innerContent":{{"desktop":{{"value":"Enterprise"}}}}}},"subtitle":{{"innerContent":{{"desktop":{{"value":"For organizations"}}}}}},"perMonth":{{"innerContent":{{"desktop":{{"value":"mo"}}}}}},"sum":{{"innerContent":{{"desktop":{{"value":"$99"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Contact Us"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<ul><li>Unlimited Everything</li><li>1 TB Storage</li><li>Dedicated Support</li><li>Custom Integrations</li><li>SLA Guarantee</li></ul>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- /wp:divi/pricing-tables -->"""
    )
}

MODULES["search"] = {
    "title": "Search",
    "content": wrap_in_section(
        f'<!-- wp:divi/search {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["sidebar"] = {
    "title": "Sidebar",
    "content": wrap_in_section(
        f'<!-- wp:divi/sidebar {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["slider"] = {
    "title": "Slider",
    "content": wrap_in_section(
        f"""<!-- wp:divi/slider {{"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Welcome to Our Platform"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Discover powerful tools designed to help you build, grow, and succeed online.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Get Started"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Built for Performance"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Lightning-fast load times and optimized code ensure your site runs at peak performance.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Learn More"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"24/7 Expert Support"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Our team of experts is always here to help you make the most of your website.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Contact Us"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- /wp:divi/slider -->"""
    )
}

MODULES["social-media-follow"] = {
    "title": "Social Media Follow",
    "content": wrap_in_section(
        f"""<!-- wp:divi/social-media-follow {{"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"facebook"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://facebook.com"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"twitter"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://twitter.com"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"instagram"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://instagram.com"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/social-media-follow-network {{"socialNetwork":{{"innerContent":{{"desktop":{{"value":"linkedin"}}}}}},"url":{{"innerContent":{{"desktop":{{"value":"https://linkedin.com"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- /wp:divi/social-media-follow -->"""
    )
}

MODULES["tabs"] = {
    "title": "Tabs",
    "content": wrap_in_section(
        f"""<!-- wp:divi/tabs {{"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/tab {{"title":{{"innerContent":{{"desktop":{{"value":"Features"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Our platform includes drag-and-drop editing, real-time previews, responsive design controls, and over 200 design elements to choose from. Build exactly what you envision without writing a single line of code.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/tab {{"title":{{"innerContent":{{"desktop":{{"value":"Pricing"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Choose from flexible plans starting at just $19/month. All plans include core features, regular updates, and access to our support team. Annual billing saves you 20%.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/tab {{"title":{{"innerContent":{{"desktop":{{"value":"Support"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Get help when you need it with our comprehensive documentation, video tutorials, and responsive support team. Premium plans include priority support with guaranteed response times.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- /wp:divi/tabs -->"""
    )
}

MODULES["testimonial"] = {
    "title": "Testimonial",
    "content": wrap_in_section(
        f"""<!-- wp:divi/testimonial {{"author":{{"innerContent":{{"desktop":{{"value":"Jennifer Martinez"}}}}}},"jobTitle":{{"innerContent":{{"desktop":{{"value":"CEO, Bright Ideas Co."}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>This platform completely transformed how we build and manage our web presence. The intuitive design tools and outstanding support team made the transition seamless.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/testimonial {{"author":{{"innerContent":{{"desktop":{{"value":"David Park"}}}}}},"jobTitle":{{"innerContent":{{"desktop":{{"value":"Marketing Director, TechFlow"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We saw a 40% increase in conversions after redesigning our site. The performance optimizations and design flexibility are unmatched in the industry.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["text"] = {
    "title": "Text",
    "content": wrap_in_section(
        f"""<!-- wp:divi/text {{"content":{{"innerContent":{{"desktop":{{"value":"<h2>The Art of Web Design</h2><p>Great web design is more than just aesthetics — it's about creating experiences that guide visitors naturally toward their goals. Every color choice, every spacing decision, and every interaction matters.</p><p>When done well, design becomes invisible. Users don't think about the interface; they simply accomplish what they came to do. That's the standard we hold ourselves to on every project.</p><h3>Our Approach</h3><p>We start with research, move to wireframes, iterate on prototypes, and deliver pixel-perfect results. Every step is collaborative, transparent, and focused on your business objectives.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["toggle"] = {
    "title": "Toggle",
    "content": wrap_in_section(
        f"""<!-- wp:divi/toggle {{"title":{{"innerContent":{{"desktop":{{"value":"What makes your service different?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We combine cutting-edge technology with personalized attention. Every project gets a dedicated team, custom strategy, and ongoing optimization to ensure long-term success.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/toggle {{"title":{{"innerContent":{{"desktop":{{"value":"How quickly can I get started?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Most clients are up and running within 48 hours. Our streamlined onboarding process gets you from signup to live site in record time, with full support every step of the way.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->

<!-- wp:divi/toggle {{"title":{{"innerContent":{{"desktop":{{"value":"Do you offer a money-back guarantee?"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Absolutely. We offer a 30-day no-questions-asked money-back guarantee. If you're not completely satisfied, we'll refund your investment in full.</p>"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->"""
    )
}

MODULES["video"] = {
    "title": "Video",
    "content": wrap_in_section(
        f'<!-- wp:divi/video {{"src":{{"innerContent":{{"desktop":{{"value":"https://www.youtube.com/watch?v=FkQuawiGWUw"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["video-slider"] = {
    "title": "Video Slider",
    "content": wrap_in_section(
        f"""<!-- wp:divi/video-slider {{"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/video-slider-item {{"src":{{"innerContent":{{"desktop":{{"value":"https://www.youtube.com/watch?v=FkQuawiGWUw"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- /wp:divi/video-slider -->"""
    )
}

# Fullwidth modules
MODULES["fullwidth-header"] = {
    "title": "Fullwidth Header",
    "content": wrap_in_section(
        f'<!-- wp:divi/fullwidth-header {{"title":{{"innerContent":{{"desktop":{{"value":"Welcome to Our Website"}}}}}},"subhead":{{"innerContent":{{"desktop":{{"value":"Building beautiful digital experiences since 2010"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>We help businesses grow with stunning websites, powerful marketing tools, and world-class support. Start your journey today.</p>"}}}}}},"buttonOneText":{{"innerContent":{{"desktop":{{"value":"Get Started"}}}}}},"buttonTwoText":{{"innerContent":{{"desktop":{{"value":"Learn More"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["fullwidth-map"] = {
    "title": "Fullwidth Map",
    "content": wrap_in_section(
        f'<!-- wp:divi/fullwidth-map {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["fullwidth-menu"] = {
    "title": "Fullwidth Menu",
    "content": wrap_in_section(
        f'<!-- wp:divi/fullwidth-menu {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["fullwidth-slider"] = {
    "title": "Fullwidth Slider",
    "content": wrap_in_section(
        f"""<!-- wp:divi/fullwidth-slider {{"builderVersion":"{BUILDER_VERSION}"}} -->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Fullwidth Slide One"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>A beautiful fullwidth slider showcasing your most important content with impact.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Explore"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- wp:divi/slide {{"heading":{{"innerContent":{{"desktop":{{"value":"Fullwidth Slide Two"}}}}}},"content":{{"innerContent":{{"desktop":{{"value":"<p>Capture attention with stunning visuals and compelling calls to action.</p>"}}}}}},"buttonText":{{"innerContent":{{"desktop":{{"value":"Discover"}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->
<!-- /wp:divi/fullwidth-slider -->"""
    )
}

# Portfolio/blog-like modules (these pull dynamic content)
MODULES["portfolio"] = {
    "title": "Portfolio",
    "content": wrap_in_section(
        f'<!-- wp:divi/portfolio {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"8"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["filterable-portfolio"] = {
    "title": "Filterable Portfolio",
    "content": wrap_in_section(
        f'<!-- wp:divi/filterable-portfolio {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"8"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["fullwidth-portfolio"] = {
    "title": "Fullwidth Portfolio",
    "content": wrap_in_section(
        f'<!-- wp:divi/fullwidth-portfolio {{"module":{{"advanced":{{"postsNumber":{{"desktop":{{"value":"8"}}}}}}}},"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["post-slider"] = {
    "title": "Post Slider",
    "content": wrap_in_section(
        f'<!-- wp:divi/post-slider {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["post-navigation"] = {
    "title": "Post Navigation",
    "content": wrap_in_section(
        f'<!-- wp:divi/post-navigation {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["post-title"] = {
    "title": "Post Title",
    "content": wrap_in_section(
        f'<!-- wp:divi/post-title {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}

MODULES["shop"] = {
    "title": "Shop",
    "content": wrap_in_section(
        f'<!-- wp:divi/shop {{"builderVersion":"{BUILDER_VERSION}"}} /-->'
    )
}


# ─── CREATE / UPDATE PAGES ───

def get_existing_pages():
    """Get all existing child pages of Module Demos."""
    pages = {}
    page_num = 1
    while True:
        resp = requests.get(
            WP_URL,
            auth=AUTH,
            params={"parent": PARENT_ID, "per_page": 100, "page": page_num, "status": "publish,draft"},
            timeout=30
        )
        if resp.status_code != 200:
            break
        data = resp.json()
        if not data:
            break
        for p in data:
            pages[p["slug"]] = p["id"]
        page_num += 1
    return pages


def create_or_update_page(slug, module_data, existing_pages, retries=3):
    """Create a new page or update existing one, with retry logic."""
    payload = {
        "title": module_data["title"],
        "slug": slug,
        "content": module_data["content"],
        "status": "publish",
        "parent": PARENT_ID,
    }

    page_id = module_data.get("update_id") or existing_pages.get(slug)

    for attempt in range(retries):
        try:
            if page_id:
                resp = requests.post(
                    f"{WP_URL}/{page_id}",
                    auth=AUTH,
                    json=payload,
                    timeout=60
                )
                action = "UPDATED"
            else:
                resp = requests.post(
                    WP_URL,
                    auth=AUTH,
                    json=payload,
                    timeout=60
                )
                action = "CREATED"

            if resp.status_code in (200, 201):
                data = resp.json()
                print(f"  ✅ {action}: {module_data['title']} (ID: {data['id']}, slug: {data['slug']})")
                return True
            else:
                print(f"  ❌ FAILED: {module_data['title']} — {resp.status_code}: {resp.text[:200]}")
                return False

        except requests.exceptions.Timeout:
            if attempt < retries - 1:
                wait = 5 * (attempt + 1)
                print(f"  ⏳ Timeout on {module_data['title']}, retrying in {wait}s... (attempt {attempt+2}/{retries})")
                time.sleep(wait)
            else:
                print(f"  ❌ TIMEOUT: {module_data['title']} after {retries} attempts")
                return False
        except requests.exceptions.ConnectionError:
            if attempt < retries - 1:
                wait = 10 * (attempt + 1)
                print(f"  ⏳ Connection error on {module_data['title']}, retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"  ❌ CONNECTION ERROR: {module_data['title']} after {retries} attempts")
                return False


def main():
    print("Fetching existing pages...")
    existing = get_existing_pages()
    print(f"Found {len(existing)} existing pages under Module Demos: {list(existing.keys())}\n")

    # Skip accordion — already done with good content
    skip = {"accordion"}

    total = 0
    success = 0
    failed = 0
    skipped_existing = 0

    for slug, module_data in sorted(MODULES.items()):
        if slug in skip:
            print(f"  ⏭  SKIP: {module_data['title']} (already complete)")
            continue

        # Skip if already exists and not flagged for update
        if slug in existing and "update_id" not in module_data:
            print(f"  ⏭  SKIP: {module_data['title']} (already exists, ID: {existing[slug]})")
            skipped_existing += 1
            continue

        total += 1
        if create_or_update_page(slug, module_data, existing):
            success += 1
        else:
            failed += 1

        time.sleep(2)  # Rate limiting — be gentle on the server

    print(f"\n{'='*50}")
    print(f"DONE: {success} succeeded, {failed} failed, out of {total} total")
    print(f"Skipped: {list(skip)}")

    # List modules NOT included (need manual setup or special content)
    all_module_slugs = set()
    import pathlib
    for f in pathlib.Path("docs/modules").glob("*.md"):
        if f.name != "index.md":
            all_module_slugs.add(f.stem)

    covered = set(MODULES.keys()) | skip
    uncovered = sorted(all_module_slugs - covered)
    if uncovered:
        print(f"\nNOT YET COVERED (need manual setup or WooCommerce):")
        for s in uncovered:
            print(f"  - {s}")


if __name__ == "__main__":
    main()
