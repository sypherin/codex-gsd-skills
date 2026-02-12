# codex-gsd-skills

Codex skill pack mirroring the GSD phase command model from Claude Code, exposed as `$gsd` and `$gsd-*` skills.

## Install

Install one or more skills directly from GitHub:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <OWNER>/codex-gsd-skills \
  --path skills/gsd \
  --path skills/gsd-plan-phase \
  --path skills/gsd-execute-phase
```

Install all skills by passing every path under `skills/`.

After install: restart Codex to pick up new skills.

## Use

Examples:

- `Use $gsd to route this task`
- `Use $gsd-plan-phase for milestone 2`
- `Use $gsd-execute-phase to implement phase 2`

## Maintain

Local regeneration:

```bash
python3 scripts/generate_skills.py
python3 scripts/validate.py
```

Sync from upstream README commands:

```bash
python3 scripts/sync_from_upstream.py
python3 scripts/generate_skills.py
python3 scripts/validate.py
```

GitHub Actions workflow `.github/workflows/sync.yml` runs daily and opens a PR when command list changes.
