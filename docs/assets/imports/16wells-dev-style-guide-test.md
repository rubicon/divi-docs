# Test style guide — 16wells.dev / Divi Docs

Use this with the **Divi Variables From Style Guide** Claude skill to generate a Global Variables import file. Paste the token table (or this whole file) when the skill asks for style guide text or tokens.

## Brand

- **Brand name:** 16wells-dev (or "Divi Docs" for labels)
- **Use case:** Example Divi docs site at 16wells.dev

## Token table (copy into Claude)

| name | type | value | notes |
|------|------|-------|-------|
| `color.brand.primary` | `colors` | `#2176ff` | Primary / links |
| `color.brand.dark` | `colors` | `#1a2332` | Headers, dark bg |
| `color.neutral.text` | `colors` | `#374151` | Body text |
| `font.heading.family` | `fonts` | `Inter` | Headings |
| `font.body.family` | `fonts` | `Inter` | Body |
| `type.h1.size` | `numbers` | `48px` | H1 desktop |
| `type.body.size` | `numbers` | `16px` | Body text |
| `space.2` | `numbers` | `16px` | Spacing |
| `space.4` | `numbers` | `32px` | Spacing |
| `radius.sm` | `numbers` | `4px` | Buttons, inputs |
| `layout.container.max` | `numbers` | `1200px` | Content width |
| `link.site` | `links` | `https://16wells.dev` | Site URL |

## Prose (alternative input)

If you prefer prose instead of the table:

- Brand Primary: #2176ff
- Brand Dark: #1a2332
- Body text color: #374151
- Heading and body font: Inter
- H1 size: 48px. Body size: 16px.
- Spacing: 16px, 32px. Border radius: 4px.
- Max content width: 1200px.
- Site URL: https://16wells.dev
