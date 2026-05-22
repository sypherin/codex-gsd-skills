---
name: gsd
description: Dispatcher for GSD phase workflow. Use when users say /gsd style commands or need routing to the correct gsd-* phase skill.
---

# GSD Dispatcher

Route to the correct phase skill, then execute.

## Routing Table

- `surface` requests: use `$gsd-surface`

## Rules

1. Pick the narrowest matching phase skill.
2. If ambiguous, start with `$gsd-discuss-phase`.
3. Execute using the selected phase skill behavior.
4. End by naming selected skill and suggested next skill.
