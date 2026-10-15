# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

TakeMeter sorts top-level comments from r/nba into three kinds of post:
`breakdown`, `take`, and `reaction`. The distinction it is built around is not
quality — it is **what the writer offers in support of what they claim.** A
`breakdown` rests on a specific checkable detail the claim would not survive
without; a `take` asserts a general evaluation and offers nothing; a `reaction`
is not making a claim about basketball at all.

The community was chosen because a single Post Game Thread holds all three
within a few comments of each other, and because the hard boundary there is a
genuine one: r/nba writes takes with statistics attached. *"Lakers are cooked,
they're 3-7 in their last 10"* names a checkable number and is still a verdict
the writer reached before the number. A classifier that keys on the presence of
a stat gets that post wrong, which is exactly the failure the taxonomy and its
three-step decision rule exist to prevent.

What it is for: triage. The model is small enough to run on every comment in a
thread, so the useful output is a shortlist of the posts worth reading rather
than a verdict on any single one.


---

## Stretch Features — declared before building

Declared here before the work was done, as the brief requires.

**Attempting: a second training run with one hyperparameter changed.**

The plan is to run sections 1–5 twice on the same `labels.csv` and the same
seed, changing `EPOCHS` from 3 to 5 and nothing else, then record which numbers
moved and by how much against the first run.

Why this one: it needs no additional labelling, so it cannot disturb the
balance that criterion 3 depends on. The Milestone 5 rehearsal is also a
reason to expect it to be informative rather than decorative — on 42 practice
examples, three epochs left the model close to uniform output (mean confidence
0.365 when right, 0.358 when wrong, against a 0.333 floor for three labels).
If 140 examples behave similarly, more epochs is the obvious first thing to
move, and criterion 5 is the number most likely to respond.

**Not attempting:** a fourth label, or 50 extra examples for the thinnest
label. Both mean collecting more `breakdown`-adjacent text, which is the one
thing `milestone4.md` rules out — going hunting for stat-dense posts to fill a
quota biases the label toward long, number-heavy writing and makes the task
easier than the real one.

---

## Label Taxonomy

Three labels, for top-level comments on r/nba game and discussion threads.

<!-- ⚠️ Examples below are still placeholders. Each needs two REAL posts
     pasted from the reading in Milestone 1. -->

### `breakdown`

**Definition:** Makes a claim about basketball and rests it on at least one
specific, checkable detail — a stat, a minute, a play, a quote, a named
comparison — that the claim would not survive without.

**Example 1:**
>

**Example 2:**
>

### `take`

**Definition:** Asserts a general evaluation of a player, team, or decision,
offering no support that the evaluation depends on.

**Example 1:**
>

**Example 2:**
>

### `reaction`

**Definition:** Responds to the moment rather than arguing about it — the
writer's own experience of watching, a joke, or an exclamation that makes no
evaluative claim about basketball.

**Example 1:**
>

**Example 2:**
>

### The hardest boundary

**Which two labels:** `breakdown` vs. `take`.

Not because they look alike — because r/nba writes takes with statistics
attached. *"Lakers are cooked, they're 3-7 in their last 10"* names a checkable
number and is still a verdict the writer reached before the number. A
definition that says "has a stat" labels that `breakdown` and teaches the model
to detect digits.

**The decision rule I used every time.** Three steps, in this order. The order
matters — see [milestone2.md](milestone2.md), where applying them out of order
sent a post about a man putting his phone down to `breakdown`.

> **Step 1 — Is there an evaluative claim about basketball at all?**
> If no, it's `reaction`, and steps 2 and 3 never run. A post can be full of
> numbers and still stop here.
>
> **Step 2 — The deletion test.** Delete every specific detail and read what's
> left. If the claim still stands exactly as written, lean `take`.
>
> **Step 3 — The relevance clause.** Would someone who disagreed have to
> *answer* that detail? If yes, it was load-bearing and the post is
> `breakdown`, however short the claim.

Worked through:

> *"Jokic had 14 assists tonight. Best passer in league history, not close."*
> Step 1: yes, a claim. Step 2: delete the 14 and the claim is untouched. Step
> 3: a disputer says "one night says nothing about all-time" and never engages
> the number. → `take`

> *"That no-call at 1:48 was a foul — he got him across the wrist before the
> ball left his hand."*
> Step 1: yes. Step 2: deleting the specifics leaves "that was a foul", which
> stands — so step 2 alone says `take`. Step 3 overrules it: a disputer has to
> argue about the wrist. → `breakdown`

**Second boundary — `take` vs. `reaction`:** both are short and unsupported.
Does the post assert anything evaluative about basketball beyond the writer's
own experience? *"I can't watch this anymore"* → `reaction`. *"This team is
unwatchable"* → `take`. This is step 1 above, stated as its own rule because it
decides more posts than anything else in a game thread.

**Tie-break:** when two labels are still defensible after all three steps, pick
the one the post spends most of its words on. A tie-break, not a licence.

---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

**Counts per label:**

| Label | Count | Share |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
| **Total** |  | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**2.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**3.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

I used Claude heavily on this project, across every milestone. The two moments
below are the ones that changed the work rather than tidied it. The scope
disclosure is at the bottom and it is broader than two moments.

**Moment 1 — stress-testing the taxonomy before labelling anything**

- *What I asked for:* eight posts that sit exactly on the boundaries of my
  three definitions, then a classification of each under my decision rule as
  written. Milestone 2 asks for this; the point was to break the rule early.
- *What came back:* the rule broke on two of the eight. My first version was a
  deletion test — remove the specifics, and if the claim still stands it's a
  `take`. It labelled *"Wemby blocked three in a row and I put my phone down"*
  as `breakdown`, because the post contains a number. And it labelled *"that
  no-call at 1:48 was a foul, he got him across the wrist"* as `take`, because
  "that was a foul" survives deletion.
- *What I changed:* two fixes, both in the README. The rules are **ordered**
  now — the `reaction` question runs first, so a post with no basketball claim
  never reaches the deletion test. And the deletion test gained a **relevance
  clause**: would someone who disagreed have to answer that detail? Nobody
  disputing "best passer ever" engages with "14 assists tonight". Anyone
  disputing the foul has to argue about the wrist.

**Moment 2 — arguing against my own acceptance criteria**

- *What I asked for:* for each of my five targets, one reason it might turn out
  too easy and one reason too hard. No recommendation, no alternative numbers —
  Milestone 3 is explicit that a criterion I did not write is one I cannot
  defend, so the numbers had to stay mine.
- *What came back:* both columns were plausible almost everywhere, which is
  what the milestone says to expect. One was not symmetric: the too-hard case
  for criterion 3 is that hitting a 20% floor for `breakdown` means hunting for
  stat-dense posts — which would satisfy the balance rule *and* hand the model
  an easier distinction than the real one, inflating criteria 1 and 2 at the
  same time. Three criteria pass together and none mean what they say.
- *What I changed:* I kept all five numbers. What changed was the collection
  protocol, written down in `milestone4.md` before any data was gathered: read
  threads in order and label what comes, and if `breakdown` runs thin, change
  which threads I read rather than which posts I pick up.

**Pre-labelling disclosure:**

<!-- ⚠️ FILL THIS IN after Milestone 4. State plainly: how many rows were
     labelled cold, how many were pre-labelled by a model and corrected, and
     whether you read every single pre-labelled row or skimmed. Pre-labelling
     is allowed and expected; not disclosing it is the problem. -->

**Scope disclosure:** beyond the two moments above, Claude drafted the
taxonomy wording, the five criteria and their justifications, the collection
protocol, and `check_labels.py`, and ran the Milestone 5 pipeline rehearsal on
the practice data. The 200 posts, the cold twenty, and the hard cases are mine,
and every number in `criteria.md` is one I can argue for without the file open.


<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
