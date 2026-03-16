---
title: "Options Groups"
category: options-groups
tags: ["options-groups", "settings", "design", "advanced"]
divi_version: "5.x"
last_updated: 2026-03-16
---

# Options Groups

Options Groups are reusable collections of settings that appear across multiple Divi 5 elements. Instead of each module implementing its own spacing controls, border settings, or animation options independently, Divi 5 shares these settings through a common options group system.

## How Options Groups Work

When you open the settings panel for any module, row, column, or section in the Visual Builder, the settings are organized into three tabs: **Content**, **Design**, and **Advanced**. Within each tab, settings are grouped into collapsible sections — these are the Options Groups.

For example, the **Spacing** options group appears in nearly every element's Design tab and always provides the same margin and padding controls. The **Background** options group appears in the Content tab and consistently offers color, gradient, image, and video background options. Understanding how these groups work once means you understand them everywhere they appear.

## Options Groups Reference

### Core Design Options

These groups appear on virtually every Divi 5 element:

| Options Group | Tab | Description |
|--------------|-----|-------------|
| [Background](background.md) | Content | Color, gradient, image, and video backgrounds |
| [Text](text.md) | Design | General text styling (font, weight, style, alignment) |
| [Sizing](sizing.md) | Design | Width, max-width, height, and min-height |
| [Spacing](spacing.md) | Design | Margin and padding values (responsive) |
| [Border](border.md) | Design | Border width, color, style, and radius |
| [Box Shadow](box-shadow.md) | Design | Shadow effects (color, blur, spread, position) |
| [Filters](filters.md) | Design | CSS filters (brightness, contrast, saturation, blur) |
| [Transform](transform.md) | Design | CSS transforms (scale, translate, rotate, skew) |
| [Animation](animation.md) | Design | Entrance animations (fade, slide, bounce, zoom) |

### Advanced Options

These groups appear in the Advanced tab of most elements:

| Options Group | Description |
|--------------|-------------|
| [Attributes](attributes.md) | CSS ID, CSS classes, and custom HTML attributes |
| [CSS](css.md) | Custom CSS for specific element targets |
| [Conditions](conditions.md) | Display conditions (user role, page type, date, custom logic) |
| [Visibility](visibility.md) | Device visibility toggles (desktop, tablet, phone) |
| [Transitions](transitions.md) | CSS transition timing for hover effects |
| [Position](position.md) | CSS position property and offsets |
| [Scroll Effects](scroll-effects.md) | Scroll-driven animations (parallax, fade, scale) |

### Typography Options

These groups control text styling for specific content areas:

| Options Group | Used By |
|--------------|---------|
| [Title Text](title-text.md) | Modules with headings (Accordion, Toggle, Blurb, etc.) |
| [Body Text](body-text.md) | Modules with body content areas |
| [Closed Title Text](closed-title-text.md) | Accordion and Toggle (closed state) |
| [Heading Text](heading-text.md) | Heading module |
| [Meta Text](meta-text.md) | Blog, Portfolio, Post Title |
| [Menu Text](menu-text.md) | Menu and Fullwidth Menu |
| [Number Text](number-text.md) | Number Counter |
| [Percentage Text](percentage-text.md) | Bar Counter |
| [Pagination Text](pagination-text.md) | Blog, Portfolio |

### Module-Specific Options

These groups appear only on certain modules:

| Options Group | Used By |
|--------------|---------|
| [Accordion Icon](accordion-icon.md) | Accordion |
| [Toggle Icon](toggle-icon.md) | Toggle |
| [Toggle](toggle.md) | Accordion, Toggle |
| [Button](button.md) | Button, CTA, Pricing Table, Contact Form, Email Optin, Login |
| [Image](image.md) | Image, Blurb, Blog, Person, Testimonial |
| [Image & Icon](image-icon.md) | Blurb |
| [Overlay](overlay.md) | Blog, Portfolio, Gallery |
| [Elements](elements.md) | Blog, Comments, Post Title |
| [Content](content.md) | Blog content settings |
| [Read More](read-more.md) | Blog |
| [Link](link.md) | Most modules (URL and target settings) |
| [Meta](meta.md) | Admin label and module metadata |

### Form & Input Options

These groups appear on form-based modules:

| Options Group | Used By |
|--------------|---------|
| [Fields](fields.md) | Contact Form, Email Optin, Login |
| [Form Field Content](form-field-content.md) | Contact Form |
| [Email](email.md) | Email Optin |
| [Spam Protection](spam-protection.md) | Contact Form |
| [Attribute](attribute.md) | Various (HTML attribute settings) |

## For AI Assistants

When helping a user configure a Divi 5 element, check whether the setting they're asking about belongs to a shared Options Group. If it does, the behavior is consistent across all elements that use that group — you can confidently apply knowledge from one module to another.
