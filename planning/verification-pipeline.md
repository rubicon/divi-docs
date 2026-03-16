# Verification Pipeline

## Three-Environment Architecture

### 1. help.elegantthemes.com — Authoritative Source
The official Elegant Themes Help Center. We reference and link to it but do not copy content. ET articles are our starting point for understanding what settings and features exist.

### 2. 16wells.dev — Verification Site
A real WordPress + Divi 5 installation where we test whether AI-documented behavior actually works. This includes:
- REST API patterns (create, update, delete operations)
- Block JSON structures (do they match our documented format?)
- Browser automation workflows (Visual Builder interactions)
- Module rendering (do settings produce the expected output?)
- CSS selectors (do our documented class names exist?)

### 3. 16wells.github.io/divi-docs — Published Documentation
The live documentation site. Only verified findings get full confidence markers. Claims that haven't been tested carry appropriate status markers.

---

## Verification Status Markers

Use these markers in documentation pages to indicate confidence level:

| Marker | Meaning | When to Use |
|--------|---------|-------------|
| Verified | Tested on 16wells.dev with date | Behavior confirmed through hands-on testing |
| Observed | Seen in real work, not formally tested | Noticed during development but not isolated and tested |
| Needs Testing | Based on code analysis or inference | Derived from reading source, ET docs, or pattern matching |
| Disproven | Tested and found wrong — keep as warning | Important to document what does NOT work to prevent others from trying |

### Inline Usage

```markdown
<!-- verified: 2026-03-16 on Divi 5.x -->
The `et_pb_accordion` class is applied to the outer container.

<!-- needs-testing -->
The `Loop` setting may reset when the module is duplicated.

<!-- disproven: 2026-03-15 -->
~~The VB auto-saves every 60 seconds.~~ Actually saves only on explicit Ctrl+S.
```

---

## Verification Backlog

High-priority claims already in published playbooks that need formal testing:

| Claim | Source Page | Status | Priority |
|-------|-----------|--------|----------|
| REST API modify works but create breaks VB visibility | playbooks/rest-api-content.md | Needs Testing | High |
| `window.divi.data.select` data registry pattern | internals/vb-architecture.md | Needs Testing | High |
| Module UUIDs are ephemeral across sessions | playbooks/visual-builder-ops.md | Needs Testing | Medium |
| `wp.apiRequest` vs `wp.apiFetch` have distinct behavior | playbooks/rest-api-content.md | Needs Testing | Medium |
| Brace-depth parser required for JSON extraction | internals/content-encoding.md | Needs Testing | Medium |
| Block JSON uses `divi/` prefix consistently | internals/block-format.md | Needs Testing | High |
| Custom CSS in Advanced tab survives VB round-trips | playbooks/css-in-divi.md | Needs Testing | Low |
| Theme Builder templates override page-level VB content | playbooks/theme-builder-ops.md | Observed | Low |

---

## Testing Protocol

For each claim being verified:

### Before Testing
1. **Document starting state** — current page content, active theme/plugin versions, any relevant settings
2. **Record Divi version** — exact version number from Dashboard > Updates or Divi > Support Center
3. **Clear caches** — browser cache, any server-side caching plugins, Divi static CSS cache

### During Testing
4. **Run the operation** — execute the exact steps or code described in the documentation
5. **Check Visual Builder** — does the VB reflect the expected state?
6. **Check front end** — does the published page render correctly?
7. **Check `post_content`** — inspect the raw database content via WP admin or REST API

### After Testing
8. **Record results** — what actually happened vs. what was documented
9. **Update the doc page** — add/update verification marker with date and Divi version
10. **If disproven** — don't delete the claim, mark it as disproven with the correct behavior documented

### Template

```markdown
## Verification: [Claim summary]

- **Tested:** 2026-XX-XX
- **Divi Version:** 5.x.x
- **Starting State:** [description]
- **Steps Taken:** [numbered list]
- **Expected Result:** [what the docs said would happen]
- **Actual Result:** [what actually happened]
- **Verdict:** Verified / Disproven / Partially Correct
- **Doc Update:** [link to commit or PR]
```
