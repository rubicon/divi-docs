"""
MkDocs hook: Auto-inject 'new' page status for recently updated pages.

Reads the `last_updated` field from each page's YAML frontmatter and sets
`status: new` if the page was updated within the last 30 days. The badge
appears in the navigation sidebar automatically via MkDocs Material's
built-in page status feature.

No manual tagging or removal required — the badge expires on its own
when the page ages past 30 days at the next site build.

Installation:
  1. Place this file at hooks/new_badge.py in the repo root
  2. Add to mkdocs.yml:
       hooks:
         - hooks/new_badge.py
  3. Add status config to mkdocs.yml (see README or mkdocs.yml diff)

Configuration:
  - NEW_BADGE_DAYS: Number of days a page keeps the 'new' badge (default: 30)
  - Set to 0 to disable the hook without removing it
"""

import logging
from datetime import date, datetime

# How many days after last_updated the "new" badge stays visible
NEW_BADGE_DAYS = 30

log = logging.getLogger("mkdocs.hooks.new_badge")


def on_page_markdown(markdown: str, *, page, config, files) -> str:
    """
    Fires for every page during the build. If the page has a `last_updated`
    frontmatter field and it falls within NEW_BADGE_DAYS of today, inject
    `status: new` into the page metadata so MkDocs Material renders the badge.

    Does NOT overwrite an existing status — if the author manually set a
    different status (e.g., 'deprecated'), we respect that.
    """
    if NEW_BADGE_DAYS <= 0:
        return markdown

    meta = page.meta or {}

    # Don't overwrite a manually-set status
    if meta.get("status"):
        return markdown

    last_updated_raw = meta.get("last_updated")
    if not last_updated_raw:
        return markdown

    # Parse the date — frontmatter YAML dates can come in as date objects
    # or strings depending on the YAML parser
    try:
        if isinstance(last_updated_raw, date):
            last_updated = last_updated_raw
        elif isinstance(last_updated_raw, datetime):
            last_updated = last_updated_raw.date()
        elif isinstance(last_updated_raw, str):
            last_updated = datetime.strptime(last_updated_raw, "%Y-%m-%d").date()
        else:
            log.debug(
                f"new_badge: Unrecognized last_updated type on {page.file.src_path}: "
                f"{type(last_updated_raw)}"
            )
            return markdown
    except (ValueError, TypeError) as e:
        log.warning(
            f"new_badge: Could not parse last_updated on {page.file.src_path}: "
            f"{last_updated_raw!r} — {e}"
        )
        return markdown

    days_old = (date.today() - last_updated).days

    if 0 <= days_old <= NEW_BADGE_DAYS:
        page.meta["status"] = "new"
        log.info(
            f"new_badge: Marked '{page.file.src_path}' as new "
            f"({days_old} days old, threshold: {NEW_BADGE_DAYS})"
        )

    return markdown
