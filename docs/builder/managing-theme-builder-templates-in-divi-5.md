---
title: "Managing Theme Builder Templates in Divi 5"
category: builder
tags: ["builder", "theme-builder", "templates", "import", "export", "organization"]
related: ["getting-started-with-divi-5-theme-builder", "building-templates-for-your-website-with-theme-builder-in-divi-5"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/10616952-managing-theme-builder-templates-in-divi-5"
---

# Managing Theme Builder Templates in Divi 5

Once you've built templates with Theme Builder, you'll want to manage, organize, and share them efficiently. Divi 5 provides tools for exporting, importing, duplicating, and organizing your templates across projects.

## Overview

Template management in Divi 5 covers:

- **Organizing templates** by naming and categorizing
- **Duplicating templates** to save time on similar designs
- **Saving to Divi Library** to reuse across sites
- **Saving to Divi Cloud** for cloud-based backup and sync
- **Exporting & Importing** to move templates between sites or share with team members

## Accessing Template Management

1. Navigate to **Divi → Theme Builder** in your WordPress dashboard
2. You'll see all your templates displayed as cards
3. Each card has action buttons (edit, duplicate, delete, etc.)

## Organizing Your Templates

### Naming Templates Clearly

Use descriptive names that clearly indicate the template's purpose:

- ✓ Good: "Blog Post - Dark Theme", "Landing Page - Webinar", "Product Page - WooCommerce"
- ✗ Poor: "Template 1", "Header 2", "New Design"

Clear naming makes it easier to find and manage templates later.

### Using Tags and Categories

When saving templates to Divi Cloud or Library, add tags and categories:

1. Open template settings
2. Add **Categories** (e.g., "Landing Pages", "Blog Templates", "Service Pages")
3. Add **Tags** (e.g., "minimal", "dark-mode", "conversion-focused")
4. Use consistent tag naming across all templates

### Template Organization Strategy

Group your templates by:

- **Content Type**: Blog Post, Page, Product, Archive
- **Purpose**: Landing Page, Lead Gen, Sales, Blog
- **Style**: Dark Mode, Light Mode, Minimal, Full Width
- **Industry**: E-commerce, SaaS, Agency, Nonprofit

## Duplicating Templates

Duplicating is useful when you want to create a template based on an existing one.

### Quick Duplicate

1. From the Theme Builder screen, find the template card
2. Click the **Duplicate** button (copy icon)
3. A new template is created with the same design
4. Rename it to reflect its new purpose
5. Edit as needed

### Duplicate Benefits

- Save time on similar designs
- Maintain design consistency across template variations
- Quickly create a backup before making major changes
- Experiment with variations without affecting the original

## Saving Templates to Divi Library

Divi Library stores templates locally on your site for reuse across pages and posts. Templates saved to the library can be used when building any page or post.

### Save a Full Theme Builder Set to Library

A Theme Builder Set includes your global header, footer, and custom templates.

1. From the Theme Builder screen, click the **Portability** icon (box with arrow) in the Header section
2. Click **Theme Builder Set**
3. Complete the **Save Theme Builder Set** form:
   - **Name**: Give your set a descriptive name
   - **Templates to Save**: Check which templates to include (Header, Footer, custom templates)
   - **Categories**: Add categories for organization
   - **Tags**: Add tags for searchability
4. Click **Save to Divi Library**

Your set is now available to import on other sites.

### Save Individual Templates to Library

1. From the Theme Builder screen, click the **Portability** icon on the specific template
2. Click **Save to Divi Library**
3. Complete the **Save Theme Builder Template** form:
   - **Name**: Descriptive name for the template
   - **Category**: Choose or create a category
   - **Tags**: Add searchable tags
4. Click **Save to Divi Library**

The template is now available to insert into pages/posts on this site.

## Saving Templates to Divi Cloud

Divi Cloud is Elegant Themes' cloud storage service that lets you save, backup, and sync templates across multiple sites.

### Requirements

- Active Elegant Themes account
- Divi Cloud enabled in your site settings

### Save a Theme Builder Set to Divi Cloud

1. From the Theme Builder screen, click the **Portability** icon in the Header section
2. Click **Theme Builder Set**
3. Complete the **Save Theme Builder Set** form
4. Check **Save to Divi Cloud**
5. Click **Save to Divi Cloud**

Your set is now backed up and accessible from other sites using your Elegant Themes account.

### Benefits of Divi Cloud

- **Cloud Backup**: Your templates are automatically backed up
- **Cross-Site Sync**: Access templates across all your sites
- **Team Collaboration**: Share templates with team members (if using team features)
- **Version History**: Keep historical versions of your templates

## Importing Templates

### Import from Divi Library

1. From the Theme Builder screen, click the **+** button in the section where you want to add a template
2. Click **Add From Library**
3. Browse your saved templates in the Divi Library
4. Click the template to import it
5. Name the template if needed
6. Click **Create Template**

The template is now imported and ready to use/edit.

### Import from Divi Cloud

1. From the Theme Builder screen, click the **Portability** icon
2. Click **Import tab**
3. Select **Import Divi Theme Builder Templates** from the Divi Cloud option
4. Choose the template or set to import from your cloud library
5. Click **Import Divi Theme Builder Templates**

The template(s) are now imported into your site.

### Import from File

1. From the Theme Builder screen, click the **Portability** icon
2. Click **Import tab**
3. Select **Import From File**
4. Upload the .json file of your exported template
5. Click **Import Divi Theme Builder Templates**

The template is now imported into your site.

## Exporting Templates

Exporting creates a portable .json file of your template that can be moved to another site, shared with team members, or stored as a backup.

### Export a Single Template

1. From the Theme Builder screen, click the **Portability** icon on the template you want to export
2. Click **Export tab**
3. Set a name for the export file (defaults to template name)
4. Click **Export Divi Theme Builder Templates**
5. The .json file downloads to your computer

### Export a Full Theme Builder Set

1. From the Theme Builder screen, click the **Portability** icon in the Header section
2. Click **Theme Builder Set**
3. Click **Export tab**
4. Select which templates to include in the export
5. Set a name for the export file
6. Click **Export Divi Theme Builder Templates**
7. The .json file downloads

### What's Included in an Export

An exported template includes:

- All design elements and layout
- All styling (colors, fonts, spacing, effects)
- Global Variables used in the template
- Element Presets referenced in the template
- All media files referenced in the template

Exported templates do NOT include:

- Post/page content (only the template structure)
- WordPress plugins or custom code
- Database content outside the template

## Sharing Templates

### Share with Team Members

1. Export your template(s) using the export process above
2. Send the .json file to your team member
3. They import the file into their Divi Library
4. They can now use/modify the template on their site

### Share Publicly

1. Export your template
2. Host the .json file on a web server or file sharing service
3. Share the download link with the public
4. Others can import the file into their Divi Library

Consider hosting exported templates on:
- Your personal website
- GitHub (for open-source templates)
- Gumroad or similar platform (for selling templates)

## Common Management Tasks

### Delete a Template

1. From the Theme Builder screen, hover over the template card
2. Click the **Delete** button
3. Confirm the deletion

!!! warning
    Deleted templates cannot be recovered unless you have an export or Divi Cloud backup.

### Rename a Template

1. Click the template card to edit it
2. In the Visual Builder, look for the template name field at the top
3. Click to edit the name
4. Save your changes

### Change Template Assignment

1. From the Theme Builder screen, click the template to edit it
2. Look for the **Assignment** or **Applies To** section
3. Modify which content the template applies to
4. Save your changes

### Create Template Variations

1. Duplicate an existing template
2. Name it with a descriptive suffix (e.g., "Blog Post - Dark Mode")
3. Edit only the elements that differ from the original
4. Save

This approach makes it easy to manage similar templates.

## Best Practices for Template Management

### Backup Regularly

- Export important templates quarterly
- Save exports to cloud storage (Google Drive, Dropbox, etc.)
- Version your exports (e.g., `blog-template-2026-05.json`)

### Use Consistent Naming

- Prefix templates with their type (e.g., "Post:", "Page:", "Global:")
- Include style descriptors (e.g., "Dark", "Minimal", "Full-Width")
- Avoid abbreviations that aren't instantly clear

### Document Your Templates

- Keep a spreadsheet listing all templates, their purpose, and when they were created
- Note which templates are used on which pages
- Document any custom styling or variables used

### Clean Up Unused Templates

- Regularly review the Template list
- Delete templates no longer in use
- Archive templates by exporting them before deletion
- Keep the Template list organized and manageable

### Version Your Exports

- Include the date in export filenames: `header-global-2026-05-06.json`
- Keep old versions for at least 3 months
- Note major design changes in a changelog file

## Troubleshooting

!!! warning "Can't Import a Template"
    If importing fails:
    1. Verify the .json file is from a Divi template export
    2. Check that the file isn't corrupted (open it in a text editor)
    3. Ensure you have write permissions in the WordPress uploads folder
    4. Try importing from a different source (file vs. cloud)
    5. Check for PHP errors in the WordPress error log

!!! warning "Missing Elements After Import"
    If some elements don't appear after importing:
    1. Check if custom plugins or extensions are active on the source site but not the destination
    2. Verify that referenced media files are available
    3. Check that Global Variables referenced in the template exist on your site
    4. Manually add missing elements if necessary

!!! warning "Export File Too Large"
    If your export file is larger than expected:
    1. Check if the template includes large images; export those separately
    2. Export only necessary templates instead of the entire set
    3. Compress images before building the template
    4. Remove unused images from the Media Library

!!! warning "Can't Find a Saved Template"
    If you can't find a template in your Library:
    1. Search by template name or tag in the Library browser
    2. Check if it was saved to Divi Cloud instead of local Library
    3. Verify the template isn't archived or hidden
    4. Check your export folder if the template was exported

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 template management features. Divi 4's export/import process was different.

## Related

- [Getting Started with Divi 5 Theme Builder](getting-started-with-divi-5-theme-builder.md)
- [Building Templates for Your Website with Theme Builder in Divi 5](building-templates-for-your-website-with-theme-builder-in-divi-5.md)
- [Exploring Divi 5's New Features](exploring-divi-5-s-new-features.md)
