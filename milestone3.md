# Milestone 3 — Stress-testing the five targets

The criteria are in [criteria.md](criteria.md). This is the check the milestone
asks for: for each target, **one reason it might turn out too easy and one
reason it might turn out too hard.** No verdict on which is more likely, and no
alternative numbers — moving a number is my call, and I have to be able to
defend it in unit 6 without reading this file.

Setup these all assume: `distilbert-base-uncased`, 200 rows split 70/15/15, so
**140 train / 30 val / 30 test**, 3 epochs, and the target has to hold on all
three seeds.

---

## 1. Accuracy ≥ 0.65, every seed

**Could be too easy:** `reaction` is lexically obvious — jokes and one-liners
are short, use punctuation and slang that nothing else in the data uses, and a
model can nail that class on surface features alone. If `reaction` is 55% of
the data and distilbert gets 90% of it right, that's 0.50 before it has
understood anything, and only a handful of correct `breakdown` calls are needed
to clear 0.65.

**Could be too hard:** 30 test posts means each one is worth 3.3 points, and
the bar is 20 of 30 three times. A seed where two genuinely ambiguous posts
land in test instead of train can cost 7 points on its own. The three-seed
requirement means I need the *worst* of three draws to clear 0.65, not the
average.

---

## 2. No label below 0.50 F1, any seed

**Could be too easy:** F1 at 0.50 is reachable by a model that heavily
over-predicts a label — high recall, mediocre precision still averages out
around there. `breakdown` could clear this bar while being wrong about what
makes something a breakdown, by learning "has digits" and nothing else. That is
the exact failure the taxonomy was designed to prevent, and this criterion
would not catch it.

**Could be too hard:** with ~6 `breakdown` posts in the test split, F1 moves in
steps of roughly 0.08. There is no value between 0.44 and 0.52 the measurement
can even express. Clearing 0.50 on all three seeds means never having two bad
draws on a six-item sample, which is as much luck as skill.

---

## 3. No label above 55%, none below 20%

**Could be too easy:** this one is entirely under my control. It is checked
against `labels.csv`, which I build, so I can meet it by choosing what to
collect. Unlike the other four it cannot be missed by surprise — if it fails it
is because I stopped paying attention, not because the model disappointed me.

**Could be too hard:** it is a constraint on collection, not on the model, and
it fights the community. Hitting 20% `breakdown` out of a natural r/nba pull
means reading well past 200 posts and discarding most of what I find. The
harder version of the risk: if I go hunting specifically for stat-heavy posts
to fill the quota, I bias `breakdown` toward long, number-dense writing and
hand the model an easier distinction than the real one — meeting criterion 3
and quietly inflating criteria 1 and 2 in the process.

---

## 4. Staff agreement ≥ 70% (21 of 30)

**Could be too easy:** the staff taxonomy is written out in full with four
worked decision rules, and I will have spent a week thinking in almost exactly
these categories. Careful application of a well-specified rule on 30 posts
should land in the 70s without heroics — the staff document says so itself.

**Could be too hard:** staff picked several of the 30 *because* they are
ambiguous, so the set is deliberately harder than a random 30. And my own
three-step rule is close enough to the staff rules to interfere: step 3, the
relevance clause, is mine, and applying it where staff applied their simpler
load-bearing test could cost me several posts while I am being internally
consistent and externally wrong.

---

## 5. Mean confidence gap ≥ 0.05 between right and wrong

**Could be too easy:** small transformers fine-tuned for 3 epochs are usually
overconfident, and overconfidence is not the same as uninformative. Softmax
outputs tend to cluster near 1.0 on easy cases, and if the easy cases are also
the ones it gets right, a 0.05 gap can fall out of the arithmetic without the
confidence being useful for anything.

**Could be too hard:** the same overconfidence can flatten the gap instead. If
the model returns 0.97 on nearly everything including its mistakes — common
when training data is thin and the model has memorised rather than generalised
— the two means sit within a point of each other and the criterion misses while
the model is otherwise fine. With only 30 test posts, the "wrong" mean is
computed over maybe 8 to 10 items, so one serenely confident error moves it a
lot.

---

## What I noticed writing these

Both columns are plausible everywhere, which the milestone warned they would
be. The useful thing wasn't the balance — it was that **criterion 3's
too-hard case is a route to faking criteria 1 and 2.** Filling the `breakdown`
quota by hunting for long, stat-dense posts would satisfy the balance rule and
make the classification task easier than the real one, so three criteria pass
together and none of them mean what they say.

Noted here so it is on the record before collection starts: Milestone 4
collects by reading threads in order and labelling what comes, not by searching
for posts that fit a thin label.
