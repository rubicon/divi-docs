# Claude skills (references)

This folder does **not** contain full skill definitions. Skills used by or recommended for this project live in separate repositories so they can be updated and versioned independently.

## Referenced skills

| Skill | Repo | Purpose |
|-------|------|---------|
| **Divi Variables From Style Guide** | [16wells/divi-styleguide-variables](https://github.com/16wells/divi-styleguide-variables) | Generate Divi 5 Global Variables import JSON from style guides or design tokens. |

## Installing or updating a skill

### In Cursor

Cursor reads skills from `~/.cursor/skills/`. Each skill must live in its own folder with a `SKILL.md` at the root.

**Install (one-time):**

```bash
git clone https://github.com/16wells/divi-styleguide-variables.git ~/.cursor/skills/divi-styleguide-variables
```

**Update later:**

```bash
cd ~/.cursor/skills/divi-styleguide-variables && git pull
```

Restart Cursor or start a new chat so the skill is picked up.

### In Claude.ai

Settings → Capabilities/Skills → Upload skill → select the folder that contains `SKILL.md`.

### In Claude Code

Copy the skill folder into your Claude Code skills directory (see your settings for the path).
