#!/usr/bin/env python3
"""
Builds prompts/INDEX.md with a table of all prompt files.
Run from repo root:  python scripts/build_index.py
"""

import pathlib, re, textwrap
from urllib.parse import quote
import subprocess

PROMPTS_DIR = pathlib.Path("prompts")
INDEX_FILE  = PROMPTS_DIR / "INDEX.md"



def git_commit_changes():
    try:
        subprocess.run(['git', 'add', str(INDEX_FILE)], check=True)
        subprocess.run(['git', 'commit', '-m', 'Update INDEX.md'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Changes to INDEX.md committed and pushed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit changes: {e}")

def extract_title(path: pathlib.Path) -> str:
    """Grab first non‑empty heading line or fallback to filename."""
    for line in path.read_text(encoding="utf‑8").splitlines():
        if m := re.match(r"#\s*(.+)", line):
            return m.group(1).strip()
    return path.stem.replace("_", " ")

def main() -> None:
    files = sorted(PROMPTS_DIR.rglob("*.md"))
    rows  = []
    for f in files:
        if f.name == "INDEX.md":
            continue
        rel_path = f.relative_to(PROMPTS_DIR).as_posix()
        url      = quote(rel_path, safe="/")     # “ ” → %20, “/” untouched
        rows.append(f"| [{rel_path}]({url}) | {extract_title(f)} |")

    header = textwrap.dedent("""\
        <!--- AUTO‑GENERATED: do not edit manually.  Run scripts/build_index.py -->
        # Prompt Index

        | Path | Title |
        |------|-------|
    """)
    INDEX_FILE.write_text(header + "\n".join(rows) + "\n", encoding="utf‑8")
    print(f"Generated {INDEX_FILE} with {len(rows)} entries")
    
    # Uncomment the following line to enable auto-commit
    git_commit_changes()

if __name__ == "__main__":
    main()
