---
title: "Divi AI"
description: "Divi 5 AI — generate text, images, layouts, and full sites using integrated AI directly within the Visual Builder, with context-aware results."
category: builder
tags: ["builder", "ai", "content-generation", "image-generation", "automation"]
related: ["visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10655703"
---

# Divi AI

Generate text, images, layouts, and entire sites using AI directly within the Divi Visual Builder.

!!! abstract "Quick Reference"
    **What it does:** AI-powered generation of text, images, layouts, sections, and full websites from within the builder.
    **Where to find it:** Divi AI icon on text/image fields, Background Image fields, or "Generate Content with AI" button on select modules.
    **Key features:**

    - Full site generation (25 tokens), layout generation (10 tokens), section generation (5 tokens)
    - Text and content generation/improvement in any language (1 token each)
    - Image generation, editing, enhancement, and aspect ratio adjustment
    - Context-aware: draws on site title, tagline, and existing page content

    **ET Docs:** [Divi AI](https://help.elegantthemes.com/en/articles/10655703){:target="_blank"}

## Overview

Divi AI is an integrated artificial intelligence assistant built into the Divi 5 Visual Builder. It can generate website copy, create images, build page layouts, produce full site designs, and write CSS code -- all from within the builder interface. There is nothing to install or activate; the AI features appear automatically on supported elements.

Divi AI learns from your existing website content (site title, tagline, page content, and module content) to produce contextually relevant results that match your site's tone and subject matter. Text generation is powered by large language models and supports any language. Image generation uses diffusion models and requires English-language prompts.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10655703).

## Requirements

| Requirement | Detail |
|-------------|--------|
| Divi membership | Active Elegant Themes subscription required |
| Divi AI access | Included with the Divi Pro Bundle, or available as a separate add-on |
| Free trial | 100 tokens included for new users |

## AI Capabilities

| Feature | Description | Token Cost |
|---------|-------------|------------|
| Full site generation | Creates an entire website with unique layouts, content, and images | 25 tokens |
| Layout generation | Transforms a standard layout into a custom design | 10 tokens |
| Section generation | Adds AI-generated sections with matching design style | 5 tokens |
| Text generation | Writes blog posts, product descriptions, landing page copy | 1 token |
| Content improvement | Enhances and refines existing text | 1 token |
| Image generation | Creates photos, paintings, 3D renders, and sketches | 1 token |
| AI image editor | Modifies and reimagines elements within existing images | 1 token |
| Image enhancement | Upscales resolution, improves detail, contrast, and saturation | 1 token |
| Aspect ratio adjustment | Resizes images for specific layout requirements | 10 tokens |
| Code generation | Writes and optimizes CSS and other code | 1 token |

## How to Access Divi AI

Divi AI is accessible from multiple points within the builder, depending on the element and content type.

| Element Type | Access Method |
|-------------|---------------|
| Text and image modules | Hover over the input field and click the **Divi AI icon** in the top-right corner |
| Structural elements (sections, rows, columns) | Content tab > Background > Background Image > Divi AI icon |
| Select modules with auto-generate | Click the **Generate Content with AI** button at the top of content options |

## Context Awareness

Divi AI draws on your site's existing data to produce on-brand results:

| Data Source | How It Is Used |
|-------------|---------------|
| Website title | Informs the topic and brand name in generated content |
| Tagline / business description | Shapes the tone and purpose of generated text |
| Page content | Provides topical context for section and layout generation |
| Module content | Used as a reference when improving or extending existing text |

## Underlying Technology

| Content Type | Technology |
|-------------|------------|
| Text generation | Large language model (ChatGPT) |
| Image generation | Diffusion model (Stable Diffusion) |

## Language and Licensing

| Aspect | Detail |
|--------|--------|
| Text generation language | Any language supported |
| Image prompt language | English only |
| Image licensing | Royalty-free; generated images may be used commercially |

## Administration

### Disabling Divi AI by Role

1. Go to WordPress Dashboard > Divi Menu > **Role Editor**.
2. Locate the Divi AI toggle for the target user role.
3. Toggle it off to prevent that role from accessing AI features.

### Fair Use

Divi AI usage is subject to Elegant Themes' fair use policy. Excessive automated or bulk generation may result in service restrictions.

## AI Interaction Notes

!!! info "API Surface"
    Divi AI does not currently expose a public REST API or programmatic interface for third-party integrations. All AI features are accessed exclusively through the Visual Builder UI. The underlying AI calls are made server-side by the Divi plugin to Elegant Themes' infrastructure -- there are no client-side API endpoints available for custom scripts or external tools to invoke directly. If Elegant Themes adds a developer-facing API in the future, this section will be updated.

## Tips and Best Practices

- **Provide a detailed site tagline.** The more context Divi AI has about your business, the more relevant its generated content will be.
- **Use content improvement on existing text.** Rather than generating from scratch, paste your draft and let AI refine it for better results.
- **Generate images with specific prompts.** Descriptive English prompts (style, subject, lighting, composition) produce significantly better image results than vague ones.
- **Review all generated content.** AI output should be treated as a draft -- always review for accuracy, tone, and brand fit before publishing.
- **Monitor token usage.** Full site and layout generation consume significantly more tokens than individual text or image operations.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If Divi AI icons are not visible, verify that your Elegant Themes subscription includes Divi AI access and that the feature has not been disabled for your role in the Role Editor.

- **AI generates irrelevant content.** Update your site title and tagline in WordPress Settings > General. Add more page content to give Divi AI better context.
- **Image generation prompt fails.** Image prompts must be in English. Translate your prompt before submitting.
- **Token balance is zero.** Purchase an unlimited Divi AI subscription through your Elegant Themes account, or wait for a token reset if applicable.
- **AI features disabled for a user.** Check the Role Editor (Divi menu) to ensure Divi AI is toggled on for that user's role.

## Related

- [Visual Builder](visual-builder.md)
