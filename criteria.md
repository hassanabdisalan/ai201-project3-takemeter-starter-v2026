# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy of at least 0.65 on the held-out set, on every seed.

**Why this target:** My largest label is capped at 55% of the data by
criterion 3, so a model that ignores the text and always guesses `reaction`
scores about 0.55. A target of 0.65 is the smallest number that clearly beats
that — below it I have not built a classifier, I have built a majority-class
guesser with a GPU bill. I set it where I'd honestly start using the thing:
getting two out of three right is the point at which skimming its output beats
reading 200 posts myself. The held-out set is 30 posts, so this is 20 of 30
correct, three times running.

---

## 2. No label scores below 0.50 F1 on any of the three seeds.

**Why this target:** `breakdown` is my smallest label and the one this number
is really about. At the 20% floor in criterion 3 it has about 40 examples, of
which roughly 6 land in the test split — and an F1 computed on 6 examples moves
about 0.08 when a single post flips. That is why this sits 15 points below my
overall accuracy target rather than beside it: demanding the same number from
my thinnest label would be demanding that the jumpiest measurement in the
report behave like the steadiest one. 0.50 still means the label is being
learned rather than scattered.

---

## 3. In `labels.csv`, no label above 55% of rows and none below 20%.

**Why this target:** The brief's ceiling is 70%; mine is 55% because 70% would
not actually protect me. `reaction` is the natural flood on r/nba — jokes and
one-liners are most of a Post Game Thread — and at 70% a model that never
predicts anything else still looks like it works. The 20% floor is the half
that matters more: it is what guarantees `breakdown` has enough examples to put
about 6 in the test split, which is the arithmetic criterion 2 depends on.
Without the floor, criterion 2 could be met or missed on noise.

---

## 4. Agreement of at least 70% (21 of 30) with the staff labels.

**Why this target:** This is the only instrument in the project that can tell a
labelling problem from a model problem, so it needs a number even though
nothing grades the rate. The staff taxonomy says several of the 30 were chosen
because they are genuinely ambiguous and that a rate in the 70s is expected —
so 70% is the bottom of normal, not a stretch. I care about it because it is
evidence about my own 200: if I cannot apply someone else's written rule
consistently across 30 posts, I have no grounds for claiming I applied my own
three-step rule consistently across 200, and any diagnosis I write in unit 6
would be guessing.

---

## 5. Mean confidence when the model is right exceeds mean confidence when it is
wrong by at least 0.05, on every seed.

**Why this target:** A classifier I'd run on everything is only useful if it
can tell me which calls to check — otherwise I have to read all 200 anyway and
it has saved nothing. This tests whether its confidence carries any
information at all. I chose this over the most-confident-third versus
least-confident-third comparison that `results.json` also reports, because each
third is only 10 posts and a single flip swings that gap 10 points; the two
means use all 30 and are continuous. 0.05 is deliberately a low bar — on 140
training examples I expect a poorly calibrated model, and I am asking whether
confidence means *anything*, not whether it is trustworthy.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
