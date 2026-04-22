---
title: "Spam Protection Options"
description: "Divi 5 Spam Protection options group — Google reCAPTCHA v3 integration and basic math captcha for contact form bot prevention."
category: options-groups
tags: ["options-groups", "spam-protection"]
related: ["fields", "email"]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/10273044"
---

# Spam Protection Options

Configures bot prevention and spam filtering for the Contact Form module using reCAPTCHA or a basic math captcha.

!!! abstract "Quick Reference"
    **What it controls:** Google reCAPTCHA v3 credentials, minimum score threshold, and basic math captcha toggle
    **Where to find it:** Content Tab → Spam Protection
    **Available on:** Contact Form module only
    **Responsive:** No — spam protection is not device-dependent
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10273044)

## Overview

The Spam Protection options group provides settings to prevent automated bot submissions on your contact forms. It supports two approaches: Google reCAPTCHA v3 integration for invisible, score-based bot detection, and a simple built-in math captcha that requires visitors to solve a basic arithmetic problem.

These settings are found in the Content tab of the Contact Form module settings panel. When you enable the spam protection service, you will need to provide your Google reCAPTCHA v3 credentials (site key and secret key), which can be obtained from the Google reCAPTCHA admin console. The minimum score setting lets you control how strict the bot detection is, with scores closer to 1.0 indicating likely human interaction and scores closer to 0.0 indicating suspected bots.

The basic captcha option provides a simpler alternative that does not require any external service. It adds a math challenge question to the form that legitimate visitors can easily answer but automated bots typically cannot. Both protection methods can be used independently to suit your needs.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10273044).

## Settings Reference

| Setting | Type | Description |
|---------|------|-------------|
| Use A Spam Protection Service | Toggle | Enables Google reCAPTCHA v3 for invisible bot detection on the form. |
| Service Provider | Dropdown | Selects the spam protection service. Currently only Google reCAPTCHA is available. |
| Account Name | Text input | Stores a label for the reCAPTCHA v3 account to identify the configuration. |
| Site Key (v3) | Text input | The public site key from your Google reCAPTCHA v3 account. |
| Secret Key (v3) | Text input | The private secret key from your Google reCAPTCHA v3 account. |
| Minimum Score | Number input | Sets the threshold for determining valid submissions. Range is 0 to 1, with 0.5 as the default. Higher values require more human-like interaction patterns. |
| Use Basic Captcha | Toggle | Enables a simple math-based captcha challenge as an alternative to reCAPTCHA. |

## Which Elements Use This

The Spam Protection options group is used exclusively by the Contact Form module in Divi 5. It protects form submissions from automated bot abuse.

## Code Examples

```php
// reCAPTCHA v3 verification on the server side (conceptual)
$response = wp_remote_post('https://www.google.com/recaptcha/api/siteverify', [
    'body' => [
        'secret'   => $secret_key,
        'response' => $recaptcha_token,
    ],
]);

$result = json_decode(wp_remote_retrieve_body($response), true);
if ($result['score'] >= 0.5) {
    // Process form submission
}
```

## Related

- [Form field design](fields.md) — Input / Checkbox / Radio groups and styling
- [Email Options](email.md) -- Notification email format settings
