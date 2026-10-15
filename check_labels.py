#!/usr/bin/env python3
"""Check labels.csv while you are still collecting.

The notebook checks your file in Milestone 5. By then you have 200 rows and
fixing a problem means going back through all of them. This runs on whatever
you have so far, so run it at 60 rows, not at 200.

    python check_labels.py

Standard library only -- it works whether or not the venv is active.

What it checks, and where each rule comes from:

  * the brief          -- at least 200 rows, no label above 70%
  * criteria.md 3      -- no label above 55%, none below 20%
  * criteria.md 2      -- enough of the thin label to land ~6 in the test split
  * the milestone      -- 20 rows labelled cold, before any tool was used
  * leakage/noise      -- duplicate posts, blank text, misspelled labels
"""

import csv
import re
import sys
from collections import Counter
from pathlib import Path

LABELS_CSV = Path(__file__).parent / "labels.csv"
DEFINITIONS = Path(__file__).parent / "label_definitions.txt"

TARGET_ROWS = 200
BRIEF_MAX_SHARE = 0.70
MY_MAX_SHARE = 0.55      # criteria.md, criterion 3
MY_MIN_SHARE = 0.20      # criteria.md, criterion 3
TEST_FRACTION = 0.15     # the notebook's split is 70/15/15
MIN_TEST_PER_LABEL = 6   # below this, per-label F1 is mostly noise
COLD_TARGET = 20

problems = []
warnings = []


def problem(msg):
    problems.append(msg)


def warn(msg):
    warnings.append(msg)


def normalise(text):
    """For duplicate detection: case and whitespace should not hide a repeat."""
    return re.sub(r"\s+", " ", text).strip().lower()


def read_definitions():
    if not DEFINITIONS.exists():
        return set()
    known = set()
    for line in DEFINITIONS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        known.add(line.split(":", 1)[0].strip())
    return known


def read_rows():
    if not LABELS_CSV.exists():
        print("No labels.csv yet.")
        print("Start from labels_template.csv -- it has the three columns.")
        sys.exit(1)

    with LABELS_CSV.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = [f.strip() for f in (reader.fieldnames or [])]
        missing = {"text", "label", "note"} - set(fields)
        if missing:
            print("labels.csv is missing column(s): " + ", ".join(sorted(missing)))
            print("Found: " + (", ".join(fields) if fields else "(nothing)"))
            sys.exit(1)
        return [dict(r) for r in reader]


def bar(share, width=28):
    filled = int(round(share * width))
    return "#" * filled + "." * (width - filled)


def main():
    rows = read_rows()
    total = len(rows)
    known_labels = read_definitions()

    print()
    print("labels.csv -- %d rows" % total)
    print("=" * 56)

    # --- row-level problems -------------------------------------------------
    seen = {}
    blank_text = 0
    blank_label = 0

    for i, row in enumerate(rows, start=2):   # +2: header is line 1
        text = (row.get("text") or "").strip()
        label = (row.get("label") or "").strip()

        if not text:
            blank_text += 1
        if not label:
            blank_label += 1
            continue

        if text:
            key = normalise(text)
            if key in seen:
                problem("duplicate post: line %d repeats line %d" % (i, seen[key]))
            else:
                seen[key] = i

    if blank_text:
        problem("%d row(s) have empty text" % blank_text)
    if blank_label:
        problem("%d row(s) have no label" % blank_label)

    labelled = [(r.get("label") or "").strip() for r in rows]
    labelled = [l for l in labelled if l]
    counts = Counter(labelled)

    # --- label spelling -----------------------------------------------------
    if known_labels:
        unknown = set(counts) - known_labels
        for label in sorted(unknown):
            near = [k for k in known_labels if k.lower() == label.lower()]
            if near:
                problem("label %r should be %r (case)" % (label, near[0]))
            else:
                problem("label %r is not in label_definitions.txt" % label)
    else:
        warn("label_definitions.txt has no definitions yet -- cannot check spelling")

    # --- balance ------------------------------------------------------------
    print()
    if not counts:
        print("Nothing labelled yet.")
    else:
        print("%-14s %5s %7s   %s" % ("label", "n", "share", "balance"))
        for label, n in counts.most_common():
            share = n / len(labelled)
            print("%-14s %5d %6.1f%%   %s" % (label, n, share * 100, bar(share)))

        top_label, top_n = counts.most_common(1)[0]
        top_share = top_n / len(labelled)

        if top_share > BRIEF_MAX_SHARE:
            problem("%r is %.0f%% of the file -- the brief's ceiling is 70%%"
                    % (top_label, top_share * 100))
        elif top_share > MY_MAX_SHARE:
            problem("%r is %.0f%% -- over your own 55%% ceiling (criterion 3)"
                    % (top_label, top_share * 100))

        for label, n in counts.items():
            share = n / len(labelled)
            if share < MY_MIN_SHARE:
                problem("%r is %.0f%% -- under your own 20%% floor (criterion 3)"
                        % (label, share * 100))

        # --- what this means for the test split -----------------------------
        print()
        print("Projected test split (%d%% of %d rows):" % (TEST_FRACTION * 100, total))
        for label, n in counts.most_common():
            in_test = n * TEST_FRACTION
            flag = "" if in_test >= MIN_TEST_PER_LABEL else "   <-- too thin to measure"
            print("  %-14s %4.1f posts%s" % (label, in_test, flag))

        thin = [l for l, n in counts.items() if n * TEST_FRACTION < MIN_TEST_PER_LABEL]
        if thin and total >= TARGET_ROWS:
            warn("per-label F1 for %s will swing hard between seeds -- "
                 "criterion 2 may be decided by the draw" % ", ".join(sorted(thin)))

    # --- the cold twenty ----------------------------------------------------
    cold = sum(1 for r in rows if "cold" in (r.get("note") or "").lower())
    print()
    print("Rows marked cold: %d of %d" % (cold, COLD_TARGET))
    if cold < COLD_TARGET:
        warn("label %d more cold, before using any tool on them -- "
             "unit 6's agreement report leans on these" % (COLD_TARGET - cold))

    # --- progress -----------------------------------------------------------
    print()
    if total < TARGET_ROWS:
        print("%d to go to reach %d." % (TARGET_ROWS - total, TARGET_ROWS))
        if total < 150:
            print("(The stop rule lets you submit at 150 if you write up why.)")
    else:
        print("At or past %d rows." % TARGET_ROWS)

    # --- verdict ------------------------------------------------------------
    print()
    print("=" * 56)
    for msg in warnings:
        print("[WARN]  " + msg)
    for msg in problems:
        print("[FIX]   " + msg)

    if not problems and not warnings:
        print("No problems found.")
    print()

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
