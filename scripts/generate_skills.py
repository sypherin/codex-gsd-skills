#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
COMMANDS_FILE = ROOT / "scripts" / "commands.json"


def title_case(slug: str) -> str:
    return " ".join(word.capitalize() for word in slug.split("-"))


def short_desc(slug: str) -> str:
    value = f"Workflow for {slug.replace('-', ' ')}"
    if len(value) < 25:
        value = value + " tasks"
    return value[:64]


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def make_phase_skill(slug: str) -> None:
    skill_name = f"gsd-{slug}"
    title = title_case(slug)
    skill_dir = SKILLS_DIR / skill_name

    skill_md = f"""---
name: {skill_name}
description: Execution-first workflow for GSD command `{slug}`. Use when the user asks for `/{skill_name.replace('gsd-', 'gsd:')}` behavior or equivalent outcomes.
---

# {title}

## Objective

Execute the `{slug}` phase with clear outputs and minimal ceremony.

## Workflow

1. Confirm scope and constraints.
2. Gather only required context.
3. Perform the requested phase action.
4. Add validation checks where applicable.
5. End with next actions.

## Output Contract

Always include:

- Action taken.
- Files or areas touched.
- Validation status.
- Remaining risks or decisions.
"""

    openai_yaml = f"""interface:
  display_name: "GSD {title}"
  short_description: "{short_desc(slug)}"
  default_prompt: "Use ${skill_name} to run the {slug} phase for this request."
"""

    write_file(skill_dir / "SKILL.md", skill_md)
    write_file(skill_dir / "agents" / "openai.yaml", openai_yaml)


def make_dispatcher(slugs: list[str]) -> None:
    lines = []
    for slug in slugs:
        lines.append(f"- `{slug}` requests: use `$gsd-{slug}`")

    routes = "\n".join(lines)

    skill_md = f"""---
name: gsd
description: Dispatcher for GSD phase workflow. Use when users say /gsd style commands or need routing to the correct gsd-* phase skill.
---

# GSD Dispatcher

Route to the correct phase skill, then execute.

## Routing Table

{routes}

## Rules

1. Pick the narrowest matching phase skill.
2. If ambiguous, start with `$gsd-discuss-phase`.
3. Execute using the selected phase skill behavior.
4. End by naming selected skill and suggested next skill.
"""

    openai_yaml = """interface:
  display_name: "GSD Dispatcher"
  short_description: "Route requests to gsd phase skills"
  default_prompt: "Use $gsd to route this request to the right GSD phase skill and execute it."
"""

    write_file(SKILLS_DIR / "gsd" / "SKILL.md", skill_md)
    write_file(SKILLS_DIR / "gsd" / "agents" / "openai.yaml", openai_yaml)


def main() -> None:
    data = json.loads(COMMANDS_FILE.read_text())
    slugs = data["commands"]

    SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    valid_names = {"gsd"}
    for slug in slugs:
        make_phase_skill(slug)
        valid_names.add(f"gsd-{slug}")

    make_dispatcher(slugs)

    for entry in SKILLS_DIR.iterdir():
        if entry.is_dir() and entry.name not in valid_names:
            for path in sorted(entry.rglob("*"), reverse=True):
                if path.is_file():
                    path.unlink()
                elif path.is_dir():
                    path.rmdir()
            entry.rmdir()

    print(f"Generated {len(valid_names)} skills")


if __name__ == "__main__":
    main()
