# Claude skills (references)

This folder does **not** contain full skill definitions. Skills used by or recommended for this project live in separate repositories so they can be updated and versioned independently.

## Referenced skills

| Skill | Repo | Purpose |
|-------|------|---------|
| **Divi Variables From Style Guide** | [16wells/divi-styleguide-variables](https://github.com/16wells/divi-styleguide-variables) | Generate Divi 5 Global Variables import JSON from style guides or design tokens. |

## Installing or updating a skill

1. Clone or download the skill from its repo (e.g. `git clone https://github.com/16wells/divi-styleguide-variables.git`).
2. Install in **Claude.ai**: Settings → Capabilities/Skills → Upload skill → select the folder that contains `SKILL.md`.
3. Install in **Claude Code**: Copy that folder into your Claude Code skills directory (see your settings for the path).

To pull updates for a skill you already cloned, `git pull` in the skill’s directory; then re-upload or re-add the skill in Claude if needed.
