#!/usr/bin/env python3
"""Prove this clone of design-engineer-skills is intact and portable.

Standard library only. Run from the repo root:  python3 verify.py
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
FAILS = []
ROWS = []

# Every skill and the file count it must have.
MANIFEST = {
    "smh-designer": 1,
    "ui-ux-pro-max": 28,
    "emil-design-eng": 2,
    "border-beam": 2,
    "vgpu": 1,
    "apple-glass": 2,
    "visual-fx-3d": 3,
    "webm-alpha-video": 1,
    "animate-expo": 2,
    "write-swift": 1,
}

# Machine-specific strings that must never survive into a shared clone.
LEAKS = ["file:///", "/home/dlohn", "Sudo_Hatter_Command", "Mr. Hatter"]

SKIP_DIRS = {".git", "__pycache__"}


def walk(exts=None):
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if exts and not fn.endswith(exts):
                continue
            yield os.path.join(dirpath, fn)


def rel(p):
    return os.path.relpath(p, ROOT)


def row(name, ok, detail=""):
    ROWS.append((name, ok, detail))
    if not ok:
        FAILS.append(name)


# --- A + B: no machine-specific paths or operator identity -------------------
hits = []
for path in walk((".md", ".py", ".csv")):
    if rel(path) == "verify.py":
        continue
    try:
        text = open(path, encoding="utf-8").read()
    except (UnicodeDecodeError, OSError):
        continue
    for leak in LEAKS:
        for i, line in enumerate(text.splitlines(), 1):
            if leak in line:
                hits.append(f"{rel(path)}:{i}: {leak}")
row("A/B  no absolute paths or operator identity", not hits,
    hits[0] if hits else "0 hits across all files")

# --- C: every relative markdown link resolves --------------------------------
LINK = re.compile(r"\]\(([^)\s]+)\)")
broken = []
for path in walk((".md",)):
    base = os.path.dirname(path)
    for target in LINK.findall(open(path, encoding="utf-8").read()):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#")[0]
        if not target:
            continue
        if not os.path.exists(os.path.normpath(os.path.join(base, target))):
            broken.append(f"{rel(path)} -> {target}")
row("C    every relative markdown link resolves", not broken,
    broken[0] if broken else "all links resolve")

# --- D: ui-ux-pro-max scripts compile and actually return results ------------
SCRIPTS = os.path.join(ROOT, "skills", "ui-ux-pro-max", "scripts")
py = [f for f in sorted(os.listdir(SCRIPTS)) if f.endswith(".py")]
compiled = subprocess.run(
    [sys.executable, "-m", "py_compile"] + [os.path.join(SCRIPTS, f) for f in py],
    capture_output=True, text=True)
row("D1   ui-ux-pro-max scripts compile", compiled.returncode == 0,
    compiled.stderr.strip()[:160] or f"{len(py)} scripts OK")

run = subprocess.run(
    [sys.executable, "search.py", "dark glass", "--domain", "color"],
    cwd=SCRIPTS, capture_output=True, text=True)
got_results = run.returncode == 0 and "Result 1" in run.stdout
row("D2   search.py returns real results", got_results,
    (run.stderr.strip()[:160] or "no Result 1 in output") if not got_results
    else run.stdout.splitlines()[2].strip())

# --- E: no live hand-off to commands that do not ship ------------------------
ORPHANS = re.compile(r"/(?:smh-quick-dev|smh-quick-fix|cicd-[a-z-]+)")
live = []
for path in walk((".md",)):
    text = open(path, encoding="utf-8").read()
    # Everything from the adaptation section onward is documentation, not a live step.
    cut = text.find("## Adapting to your own lane")
    scope = text if cut == -1 else text[:cut]
    for i, line in enumerate(scope.splitlines(), 1):
        if ORPHANS.search(line):
            live.append(f"{rel(path)}:{i}")
row("E    no live hand-off to non-shipping commands", not live,
    live[0] if live else "0 dangling references")

# --- F: manifest ------------------------------------------------------------
missing = []
for skill, count in MANIFEST.items():
    d = os.path.join(ROOT, "skills", skill)
    if not os.path.isdir(d):
        missing.append(f"{skill}: MISSING")
        continue
    actual = sum(1 for p in walk() if rel(p).startswith(f"skills/{skill}/"))
    if actual != count:
        missing.append(f"{skill}: {actual} files, expected {count}")
row(f"F    all {len(MANIFEST)} skills present at full file count", not missing,
    missing[0] if missing else f"{len(MANIFEST)} skills, {sum(MANIFEST.values())} files")

# --- report -----------------------------------------------------------------
print()
print("  design-engineer-skills — integrity check")
print("  " + "-" * 68)
for name, ok, detail in ROWS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    if detail:
        print(f"        {detail}")
print("  " + "-" * 68)
if FAILS:
    print(f"  {len(FAILS)} CHECK(S) FAILED\n")
    sys.exit(1)
print("  ALL CHECKS PASSED\n")
