---
title: "Email Options"
category: options-groups
tags: ["options-groups", "email"]
related: ["fields", "spam-protection"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10261161"
---

# Email Options

Configures the format and structure of notification emails sent when a Contact Form module submission is received.

## Overview

The Email options group controls how the data from form submissions is formatted in the notification email you receive. Rather than receiving a generic dump of field values, you can define a custom message pattern that arranges form data in a readable, structured format.

This setting is found in the Content tab of the Contact Form module settings panel. The message pattern uses a template syntax where form field IDs are wrapped in double percent signs (e.g., `%%name%%`, `%%email%%`, `%%message%%`). When a submission arrives, these placeholders are replaced with the actual values the user entered.

Field IDs are set in the individual form field settings within the Contact Form module. They must match exactly (case-sensitive) in the message pattern, and they cannot contain special characters like `! @ # $ % ^ &`. Using descriptive, lowercase field IDs without spaces helps prevent errors and makes the pattern easier to maintain.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10261161).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Message Pattern | Text input | Defines the email body format using `%%fieldid%%` placeholders to insert submitted form data into a custom layout. |

## Which Elements Use This

The Email options group is used exclusively by the Contact Form module in Divi 5. It determines the format of the notification email sent to the site administrator when a visitor submits the form.

## Code Examples

```text
Example message pattern:

New Contact Form Submission
---------------------------
Name: %%name%%
Email: %%email%%
Phone: %%phone%%
Subject: %%subject%%

Message:
%%message%%
```

## Related

- [Fields Options](fields.md) -- Form field configuration and styling
- [Spam Protection Options](spam-protection.md) -- Bot prevention settings for contact forms
