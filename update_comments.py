#!/usr/bin/env python3
"""Update the explanatory comments at the top of every exercise WITHOUT
touching the student's work.

What it changes : only the comment block at the top of each exercise file
                  (and of its reset copy in .pythonlings/originals).
What it keeps   : all the student's code, the "# I AM NOT DONE" marker
                  (or its absence) and .pythonlings/state.json (progress).

Usage (run from the folder that contains python_practice/ and learn-python/):
    python3 update_comments.py --dry-run     # show what would change
    python3 update_comments.py               # do it (makes a backup first)
    python3 update_comments.py python_practice   # only one workspace

Needs comment_updates.json next to this script.
"""
import json
import re
import shutil
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
MARK = "# I AM NOT DONE"
PREFIX = {"python_practice": "pp:", "learn-python": "lp:"}


def split_file(text):
    """Return (header_lines, attached_comment_lines, rest_lines)."""
    lines = text.split("\n")
    i = 0
    while i < len(lines) and (lines[i].startswith("#") or lines[i].strip() == ""):
        i += 1
    run, rest = lines[:i], lines[i:]
    attached = []
    if run and run[-1].strip() != "":  # comments glued to the code underneath
        j = len(run)
        while j > 0 and run[j - 1].strip() != "":
            j -= 1
        if j > 0:
            attached, run = run[j:], run[:j]
    while run and run[-1].strip() == "":
        run.pop()
    return run, attached, rest


def build(text, body):
    run, attached, rest = split_file(text)
    out = [run[0]]
    if MARK in run:
        out.append(MARK)
    out.append("#")
    out += [("# " + l) if l.strip() else "#" for l in body]
    out.append("")
    return "\n".join(out + attached + rest)


def norm(run):
    return [l for l in run if l.strip() and l.strip() != "#" and l != MARK
            and not re.fullmatch(r"#\s*-+", l)]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    sections = json.loads((HERE / "comment_updates.json").read_text(encoding="utf-8"))
    workspaces = args or [w for w in PREFIX if (HERE / w).is_dir()]
    stamp = time.strftime("%Y%m%d-%H%M%S")
    changed = skipped = 0

    for ws in workspaces:
        root = HERE / ws
        if ws not in PREFIX or not (root / "exercises").is_dir():
            print(f"skipping {ws}: not a known workspace")
            continue
        if not dry:
            shutil.copytree(root / "exercises", root / f".comment_update_backup_{stamp}")
        for ex in sorted((root / "exercises").rglob("*.py")):
            key = PREFIX[ws] + ex.stem
            if key not in sections:
                continue
            orig = root / ".pythonlings" / "originals" / ex.relative_to(root / "exercises")
            otxt = orig.read_text(encoding="utf-8") if orig.exists() else None
            etxt = ex.read_text(encoding="utf-8")
            if not etxt.startswith("# Exercise:"):
                print(f"  SKIPPED (no standard header): {ws}/{ex.relative_to(root)}")
                skipped += 1
                continue
            new_e = build(etxt, sections[key])
            # Safety: only replace a header that is still the untouched one
            # (old or already-new). If the student wrote their own notes in
            # it, leave that file alone.
            ok = {tuple(norm(split_file(new_e)[0]))}
            if otxt is not None:
                ok.add(tuple(norm(split_file(otxt)[0])))
            # The reset copy is always pristine, so always refresh it.
            if otxt is not None and not dry:
                orig.write_text(build(otxt, sections[key]), encoding="utf-8")
            if tuple(norm(split_file(etxt)[0])) not in ok:
                print(f"  SKIPPED (header was edited): {ws}/{ex.relative_to(root)}")
                skipped += 1
                continue
            assert split_file(new_e)[2] == split_file(etxt)[2]  # code identical
            if new_e != etxt:
                changed += 1
                if not dry:
                    ex.write_text(new_e, encoding="utf-8")

    print(("DRY RUN: would update " if dry else "Updated ") + f"{changed} files; skipped {skipped}.")
    if not dry:
        print("A backup of the old exercises is in .comment_update_backup_<time>/ "
              "inside each workspace. Delete it once you're happy.")


if __name__ == "__main__":
    main()
