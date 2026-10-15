# Milestone 4 — Collection protocol

The data is not here yet. This is the protocol it gets collected under, written
down first because [milestone3.md](milestone3.md) turned up a way to satisfy
criterion 3 and corrupt criteria 1 and 2 in the same motion.

Run `python check_labels.py` as you go. **At 60 rows, not at 200.**

---

## The rule that matters

**Read threads in order and label what comes. Do not search for posts that fit
a thin label.**

`breakdown` will be the thin one, and the tempting fix is to go looking for
stat-heavy comments until it hits 20%. That meets criterion 3 and quietly
breaks the project: it biases `breakdown` toward long, number-dense writing,
hands the model a distinction far easier than the real one, and inflates
criteria 1 and 2 at the same time. Three criteria pass and none mean what they
say.

**If `breakdown` runs thin, change where you read, not what you pick up.**
Daily Discussion Threads and the morning-after threads carry more argument than
a live Post Game Thread does. Widen the source; keep taking posts in order.

---

## Passes

**1. Collect (~45 min).** Top-level comments only — replies argue with the
comment above them and are the posts you will least be able to defend. Keep
whole posts; do not trim them. One file, unsplit — the notebook does 70/15/15,
and splitting twice is how test examples leak into training.

**2. The cold twenty (~15 min).** First, alone, no tools, no AI, just the
three-step rule in the README. Mark these `cold` in the note column.

This is the honesty check, and unit 6's agreement report leans on it. It is
also the only read you will ever get on whether your own decision rule is
usable by a human under time pressure — which is exactly the thing criterion 4
claims to measure.

**3. The rest (~40 min).** Pre-labelling with an AI tool is allowed and
expected. Give it the definitions and the three-step rule, then **read and
correct every single row.** Mark them `pre-labelled, checked`.

Skimming here produces a model that learned your skimming. Disclose the
workflow in the README — disclosure costs nothing, omitting it is the problem.

**4. Hard cases.** Keep the list as you go, not afterwards. Any post that made
you pause: what it was, which two labels, what you chose and why. Three
minimum, in the README. They are worth more than the easy 190, and in unit 6
they are what lets you tell a labelling problem from a model problem.

**5. Count (~5 min).** `python check_labels.py`.

---

## What the checker enforces

| Check | Source |
|---|---|
| 200 rows | the brief |
| No label above 70% | the brief |
| No label above 55%, none below 20% | criteria.md 3 |
| At least ~6 of each label in the projected test split | criteria.md 2 |
| 20 rows marked `cold` | this milestone |
| Duplicate posts, blank text, misspelled labels | leakage and noise |

Label spellings are checked against `label_definitions.txt`, so a `Breakdown`
or a `break_down` is caught here rather than in the notebook.

---

## Stop rule

Behind at ninety minutes: stop collecting, label what you have down to 150, and
write in the README how many you got and why. A smaller set described honestly
beats 200 rushed rows — and leaves you something real to diagnose next unit.
