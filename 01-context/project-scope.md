# Project Scope — Divi 5 Technical Documentation Program

## The Goal

- Maintain a reliable Divi 5 technical docs site that stays current with upstream changes.
- Expand coverage where official documentation is thin or unclear.
- Standardize cross-session memory so work can continue cleanly across Claude surfaces.

## Investment Structure

Internal productized documentation workflow (not a client-billed engagement):

- Time is allocated by priority queue: urgent fixes, high-impact missing coverage, then maintenance/audit tasks.
- Weekly cadence emphasizes shipping validated docs updates, not accumulating drafts.
- Effort is balanced between new content creation and quality upkeep (links, screenshots, nav consistency, and changelog-aware updates).

## Project Timeline

| Phase | Window | Notes |
|---|---|---|
| Foundation | Completed | MkDocs site, deployment, and baseline workflows are established. |
| Expansion | Active | Add/refresh pages based on known coverage gaps and upstream Divi changes. |
| Maintenance | Ongoing | Run monitor checks, external link checks, and periodic structural audits. |

## Deliverables and Architecture

Primary deliverables are markdown documentation pages, screenshot assets, monitoring reports, and navigation/config updates. Operational memory artifacts in `01-context/` support continuity and decision tracking across Claude surfaces.

## Platform / Technical Decisions

- Publishing stack: MkDocs Material + GitHub Pages.
- Source of truth: repository markdown and config (no external CMS in scope).
- Migration/replatforming is out of scope unless explicitly initiated.

## Governance and Inputs Needed

- Confirm missing historical details (e.g., canonical project start date if needed for recordkeeping).
- Review and approve substantive strategic/process changes.
- Set tie-breakers when trade-offs emerge between content depth, speed, and coverage breadth.

**Track what's in vs. still outstanding in `01-context/decisions-log.md`.**
