---
title: "Divi 5 FAQ"
category: troubleshooting
tags: ["troubleshooting", "faq", "general"]
related: ["visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/9857697"
---

# Divi 5 FAQ

Answers to the most common questions about upgrading to and using Divi 5.

## Overview

Divi 5 is a major rewrite of the Divi theme. This FAQ addresses concerns about cost, compatibility, migration, and feature availability.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/9857697).

## General Questions

??? question "Is Divi 5 free for existing subscribers?"
    Yes. Divi 5 is included at no additional charge with any active Elegant Themes subscription. There is no separate license or upgrade fee.

??? question "Is it safe to use Divi 5 on a live site?"
    Yes, but take precautions. Before updating a production site:

    1. Test on a staging environment first.
    2. Create a full backup (database and files).
    3. Run the **Readiness System** to identify any legacy modules that may need attention.

    Divi 5 offers improved performance and stability over Divi 4, but testing in your specific environment is always recommended.

??? question "Can I roll back to Divi 4 if something goes wrong?"
    Yes. Elegant Themes provides a rollback process. Follow the instructions in their documentation if you need to revert after upgrading.

## Feature Compatibility

??? question "Are all Divi 4 features available in Divi 5?"
    Most core features carry over. However, a few lesser-used features have been deprecated:

    - **Quick Action** -- removed
    - **Split Testing** -- removed

    Full Site Editing support is planned for post-launch releases.

??? question "Do third-party Divi modules work in Divi 5?"
    Divi 5 includes a **backward compatibility mode** that allows legacy third-party modules to function. However, pages using legacy modules will not benefit from Divi 5's performance improvements. The legacy Divi 4 framework must load alongside Divi 5 to support these modules.

??? question "What does the orange warning indicator mean?"
    The orange indicator appears when the legacy Divi 4 framework loads on a page. This happens when a page contains unconverted Divi 4 modules. It is informational only -- not an error. It signals that the page is running in backward compatibility mode and may have reduced performance.

## Migration

??? question "How does the migration from Divi 4 to Divi 5 work?"
    Divi 5 includes an automatic **Migrator System** that:

    1. Scans your existing content for Divi 4 shortcodes.
    2. Converts them to the Divi 5 block format.
    3. Creates a backup of the original post content.
    4. Leaves incompatible modules unconverted (they run in backward compatibility mode).

    Migration happens automatically when you update. No manual action is required.

??? question "Do I need to manually convert my pages?"
    No. The migrator handles conversion automatically. Pages with modules that cannot be converted will continue to work through backward compatibility mode. You can update them manually over time as third-party developers release Divi 5-compatible versions.

## Related

- [Visual Builder](../builder/visual-builder.md)
- [Fix Display Issues After Updating](fix-display-issues-after-update.md)
- [Report a Bug](report-bug.md)
