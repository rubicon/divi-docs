# Verification Pipeline

*Created: 2026-03-16*

## Three Environments

| Environment | URL | Purpose |
|---|---|---|
| **help.elegantthemes.com** | ET Help Center | Authoritative source — we reference and link to it |
| **16wells.dev** | Dev/verification site | Test whether AI-documented behavior actually works on a real Divi 5 install |
| **16wells.github.io/divi-docs** | Published docs | Only verified findings get full confidence markers |

## Content Flow

```
ET Help Center article
    ↓
Claude restructures into developer-formatted reference page
(Settings tables, element hierarchy, code examples)
    ↓
AI Interaction Notes added with claims about programmatic behavior
(Block JSON structure, REST API patterns, browser automation needs)
    ↓
Claims tested on 16wells.dev
(Actual Divi 5 install, real Visual Builder, real REST API calls)
    ↓
Findings marked with verification status
    ↓
Published to divi-docs
```

## Verification Status Markers

Every claim in AI Interaction Notes sections gets one of these:

| Marker | Meaning | When to Use |
|---|---|---|
| ✅ **Verified** | Tested and confirmed on 16wells.dev | Behavior reproduced with date stamp |
| ⚠️ **Observed** | Seen during development but not formally tested | Behavior noted in real projects, not isolated |
| 🔬 **Needs Testing** | Based on code analysis or inference | Claims from JSON parsing or pattern inference |
| ❌ **Disproven** | Tested and found wrong or outdated | Keep as warning — "we thought X but actually Y" |

## Template for AI Interaction Notes

```markdown
## AI Interaction Notes

!!! warning "Create vs. Modify — ✅ Verified 2026-01-15"
    Modifying existing content via REST API works reliably.
    **Creating new modules via REST API** produces content that
    does not appear in the Visual Builder layer view.

    *Tested on 16wells.dev — Divi 5.x.x*

**Block identifier:** `divi/module-name` — 🔬 *Needs verification*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | ✅ Verified | Brace-depth parser confirmed |
| Modify existing | `wp.apiFetch` PATCH | ✅ Verified | Title, body, settings update |
| Create new | REST API POST | ❌ Breaks VB | Use browser automation |
| Batch modify | Sequential REST chaining | ⚠️ Observed | Not isolated test |
```

## Verification Backlog

### High Priority — Core Claims in Published Playbooks

| Claim | Location | Status | Test Plan |
|---|---|---|---|
| REST modify works, create breaks VB visibility | playbooks/rest-api-content.md | ⚠️ Observed | Create test page, modify via REST, verify in VB |
| `window.divi.data.select` data registry pattern | internals/vb-architecture.md | ⚠️ Observed | Open VB on 16wells.dev, run in console |
| Module UUIDs are ephemeral across sessions | playbooks/visual-builder-ops.md | ⚠️ Observed | Load VB twice, compare UUIDs |
| `wp.apiRequest` vs `wp.apiFetch` distinct behavior | playbooks/rest-api-content.md | ⚠️ Observed | Run both against same endpoint |
| Brace-depth parser required for JSON extraction | internals/content-encoding.md | ⚠️ Observed | Fetch raw post_content, test JSON.parse vs. custom |
| Block JSON uses `divi/` prefix for block names | internals/block-format.md | ⚠️ Observed | Pull post_content from multiple pages |

### Medium Priority — New Divi 5 Features

| Feature | What to Test | Why It Matters for AI |
|---|---|---|
| Group module nesting | Can REST API modify content inside a Group? | Groups are the new container |
| Flexbox layout attributes | Do flex-direction, gap persist via REST modify? | Core to page composition |
| Nested modules | Block JSON structure for modules inside modules? | Block Format internals |
| Option Group Presets | Preset assignments readable/modifiable in post_content? | Design system manipulation |
| Design Variables | Stored in post_content or wp_options? | REST modification path |
| Loop Builder output | Block JSON for looped content? | Dynamic content docs |

### Lower Priority — Edge Cases

| Feature | What to Test |
|---|---|
| Canvases (off-canvas) | Where is canvas content stored? Can AI modify? |
| Interactions | Interaction definitions in block JSON or separate? |
| Conditions | How are conditional display rules stored? |
| Stacked/Nested Presets | JSON when presets are layered? |

## Testing Protocol

For each claim verified on 16wells.dev:

1. **Document starting state** — What's on the page before the test
2. **Run the operation** — REST API call, browser automation step, or console command
3. **Check VB** — Does the Visual Builder see the change?
4. **Check front end** — Does it render correctly?
5. **Check post_content** — What does the raw stored content look like?
6. **Record Divi version** — Behavior may change between releases
7. **Update doc page** — Change status marker, add date, note surprises

## Integration with Content Phases

Every phase includes a verification step:

- **Phase 1 (Options Groups + Layout):** Test flex/grid attributes on 16wells.dev
- **Phase 2 (Module Deep-Fill):** Test block JSON for new modules (Group, Hero, Heading)
- **Phase 3 (WooCommerce):** Test Woo module block JSON
- **Phase 4 (Features):** Test presets, variables, nested modules
- **Phase 6 (AI Bridge Playbooks):** Synthesize all verified findings
