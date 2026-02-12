#!/usr/bin/env python3
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMANDS_FILE = ROOT / "scripts" / "commands.json"
UPSTREAM_RAW = "https://raw.githubusercontent.com/gsd-build/get-shit-done/main/README.md"


def fetch_readme() -> str:
    with urllib.request.urlopen(UPSTREAM_RAW, timeout=20) as response:
        return response.read().decode("utf-8")


def parse_commands(readme: str) -> list[str]:
    matches = re.findall(r"/gsd:([a-z0-9-]+)", readme)
    deduped = []
    seen = set()
    for m in matches:
        if m not in seen:
            deduped.append(m)
            seen.add(m)
    return deduped


def main() -> int:
    readme = fetch_readme()
    upstream = parse_commands(readme)
    if not upstream:
        print("No /gsd: commands detected in upstream README", file=sys.stderr)
        return 1

    data = json.loads(COMMANDS_FILE.read_text())
    current = data.get("commands", [])

    if upstream == current:
        print("No command changes")
        return 0

    data["commands"] = upstream
    data["updated_at"] = str(date.today())
    COMMANDS_FILE.write_text(json.dumps(data, indent=2) + "\n")

    added = [c for c in upstream if c not in current]
    removed = [c for c in current if c not in upstream]
    print("Updated commands.json")
    if added:
        print("Added:", ", ".join(added))
    if removed:
        print("Removed:", ", ".join(removed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
