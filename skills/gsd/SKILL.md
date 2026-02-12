---
name: gsd
description: Dispatcher for GSD phase workflow. Use when users say /gsd style commands or need routing to the correct gsd-* phase skill.
---

# GSD Dispatcher

Route to the correct phase skill, then execute.

## Routing Table

- `new-project` requests: use `$gsd-new-project`
- `discuss-phase` requests: use `$gsd-discuss-phase`
- `plan-phase` requests: use `$gsd-plan-phase`
- `execute-phase` requests: use `$gsd-execute-phase`
- `verify-work` requests: use `$gsd-verify-work`
- `audit-milestone` requests: use `$gsd-audit-milestone`
- `complete-milestone` requests: use `$gsd-complete-milestone`
- `new-milestone` requests: use `$gsd-new-milestone`
- `progress` requests: use `$gsd-progress`
- `help` requests: use `$gsd-help`
- `update` requests: use `$gsd-update`
- `join-discord` requests: use `$gsd-join-discord`
- `map-codebase` requests: use `$gsd-map-codebase`
- `add-phase` requests: use `$gsd-add-phase`
- `insert-phase` requests: use `$gsd-insert-phase`
- `remove-phase` requests: use `$gsd-remove-phase`
- `list-phase-assumptions` requests: use `$gsd-list-phase-assumptions`
- `plan-milestone-gaps` requests: use `$gsd-plan-milestone-gaps`
- `pause-work` requests: use `$gsd-pause-work`
- `resume-work` requests: use `$gsd-resume-work`
- `settings` requests: use `$gsd-settings`
- `set-profile` requests: use `$gsd-set-profile`
- `add-todo` requests: use `$gsd-add-todo`
- `check-todos` requests: use `$gsd-check-todos`
- `debug` requests: use `$gsd-debug`
- `quick` requests: use `$gsd-quick`

## Rules

1. Pick the narrowest matching phase skill.
2. If ambiguous, start with `$gsd-discuss-phase`.
3. Execute using the selected phase skill behavior.
4. End by naming selected skill and suggested next skill.
