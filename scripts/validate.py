#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"


def fail(msg: str) -> None:
    print(msg, file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not SKILLS.exists():
        fail("skills/ directory missing")

    skill_dirs = [p for p in SKILLS.iterdir() if p.is_dir()]
    if not skill_dirs:
        fail("No skills found")

    for d in skill_dirs:
        skill_md = d / "SKILL.md"
        openai_yaml = d / "agents" / "openai.yaml"
        if not skill_md.exists():
            fail(f"Missing {skill_md}")
        if not openai_yaml.exists():
            fail(f"Missing {openai_yaml}")

        txt = skill_md.read_text()
        if not txt.startswith("---\n"):
            fail(f"Missing frontmatter in {skill_md}")
        if "\nname:" not in txt or "\ndescription:" not in txt:
            fail(f"Missing name/description in {skill_md}")

        yaml_txt = openai_yaml.read_text()
        if "interface:" not in yaml_txt:
            fail(f"Missing interface in {openai_yaml}")
        for key in ["display_name:", "short_description:", "default_prompt:"]:
            if key not in yaml_txt:
                fail(f"Missing {key} in {openai_yaml}")

    print(f"Validated {len(skill_dirs)} skills")


if __name__ == "__main__":
    main()
