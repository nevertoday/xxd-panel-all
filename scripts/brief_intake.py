#!/usr/bin/env python3
"""Check a new Soldier's source brief with the installed xxd-dna validator.

Advisory only: it never edits the brief, because the brief is the user's
authoritative text. It reports what the current xxd-dna rules would flag so the
user can decide whether to rewrite the brief before the Soldier is built.

  python3 scripts/brief_intake.py ~/Downloads/355.md
  python3 scripts/brief_intake.py --root .. --panel 355
  python3 scripts/brief_intake.py --strict brief.md   # exit 1 when anything fails

Briefs not written in the xxd-dna format are skipped. If xxd-dna is not
installed, the check is skipped with exit 0. Point at another copy with
--dna DIR or the XXD_DNA_DIR environment variable.
"""
from __future__ import annotations

import argparse
import importlib.util
import os
import sys
from pathlib import Path

DNA_CANDIDATES = (
    Path.home() / ".claude/skills/xxd-dna",
    Path.home() / ".codex/skills/xxd-dna",
    Path.home() / ".agents/skills/xxd-dna",
)
# The first words of the xxd-dna shell; briefs that start differently come from another source.
DNA_OPENING = "请将我上传的每一张照片分别制作成一张独立的高级设计海报"
SHELL_PREFIX = "第 "


def find_dna(explicit: Path | None) -> Path | None:
    env = os.environ.get("XXD_DNA_DIR")
    for candidate in ([explicit] if explicit else []) + ([Path(env)] if env else []) + list(DNA_CANDIDATES):
        if candidate and (candidate / "scripts/validate_dna.py").is_file():
            return candidate
    return None


def load_validator(dna: Path):
    spec = importlib.util.spec_from_file_location("validate_dna", dna / "scripts/validate_dna.py")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(dna / "scripts"))
    spec.loader.exec_module(module)
    return module


def strip_admin_heading(text: str) -> str:
    """Drop a first Markdown heading that only labels the archive, as the runtime does."""
    first, _, rest = text.lstrip().partition("\n")
    return rest.lstrip() if first.startswith("#") else text


def check(text: str, validator) -> tuple[list[str], list[str], list[str]]:
    """Return (shell notes, errors, warnings) for one brief."""
    errors = validator.validate(text)
    shell = [e for e in errors if e.startswith(SHELL_PREFIX) and "shell.md" in e]
    rest = [e for e in errors if e not in shell]
    return shell, rest, validator.warnings(text)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Advisory xxd-dna check for a new Soldier's source brief.")
    ap.add_argument("brief", nargs="?", type=Path, help="brief file (Markdown)")
    ap.add_argument("--root", type=Path, help="family root, used with --panel")
    ap.add_argument("--panel", type=int, help="check xxd-panel-NNN/references/original-prompt/zh-CN.md")
    ap.add_argument("--dna", type=Path, help="xxd-dna skill directory")
    ap.add_argument("--strict", action="store_true", help="exit 1 when the brief has failures")
    a = ap.parse_args(argv)

    if a.panel is not None:
        root = a.root or Path(__file__).resolve().parents[2]
        path = root / f"xxd-panel-{a.panel:03d}/references/original-prompt/zh-CN.md"
    elif a.brief is not None:
        path = a.brief.expanduser()
    else:
        ap.error("give a brief file or --panel")
    if not path.is_file():
        print(f"FAIL missing {path}")
        return 1

    text = strip_admin_heading(path.read_text(encoding="utf-8"))
    if not text.startswith(DNA_OPENING):
        print(f"SKIP {path}: not an xxd-dna brief; nothing to check")
        return 0
    dna = find_dna(a.dna)
    if dna is None:
        print("SKIP xxd-dna is not installed; pass --dna DIR or set XXD_DNA_DIR to check this brief")
        return 0

    shell, errors, warns = check(text, load_validator(dna))
    if shell:
        print("NOTE the shell differs from the current xxd-dna shell (written with an older xxd-dna)")
    for e in errors:
        print("FAIL", e)
    for w in warns:
        print("WARN", w)
    if not errors and not warns:
        print(f"OK {path}")
    else:
        print("These are advisory. The brief is the user's text: report them and let the user decide; never edit it.")
    return 1 if a.strict and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
