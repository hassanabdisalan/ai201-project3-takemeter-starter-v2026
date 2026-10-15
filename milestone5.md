# Milestone 5 — Pipeline dry run

**This is not the training run.** It is the rehearsal the milestone offers:
`data/practice_labels.csv`, 60 posts from the fictional running forum, run end
to end to prove the pipeline works before the real 200 arrive.

Nothing here goes in the README and none of these numbers are mine. The real
run happens after Milestone 4, on `labels.csv`, and it is the one that writes
`results.json` and `test_split.csv` into this repo.

---

## Environment

`python test.py` — 9 passed, 0 failed, 1 to look at.

| | |
|---|---|
| Python | 3.13.7, Windows |
| torch | 2.14.1+cpu |
| **Device** | **`cpu`** |
| Disk / RAM | 51.1 GB free / 15.8 GB |

The one `[WARN]` is the baseline model, not downloaded yet. Expected in unit 5.
**Run `python baseline.py` once before the unit 6 session** — it pulls 1.6 GB
and that is not how you want to spend a breakout.

> ⚠️ `cpu` is part of the result, not a detail about the laptop. It goes in the
> README beside the three seeds next unit, because the same data and the same
> seed on different hardware gives different numbers.

---

## What the rehearsal proved

The pipeline runs clean: load, check, split, train, evaluate, write. Training
took **50 seconds** on 42 examples. The real run has 140, so expect roughly
**three minutes** — the "few minutes on a laptop CPU" in the brief is accurate.

Both output files were written correctly. `results.json` records `device`,
`device_name`, `torch_version`, `seed`, per-label F1 with support, the
confusion matrix, and the confidence block — everything criteria 1, 2 and 5
need in order to be checkable.

---

## Two things it changed

### 1. `LABELS` was still the starter's taxonomy

The notebook shipped with `LABELS = ["analysis", "hot_take", "reaction"]`.
Mine are `breakdown`, `take`, `reaction`. Section 2's check compares `LABELS`
against the `label` column and would have thrown `[FIX ME]` on every row.

Fixed now, in the notebook. Worth knowing this is *the* most common way the run
fails — the brief lists it second in the stuck-at-thirty-minutes table.

### 2. Criterion 5 may have the failure mode backwards

[milestone3.md](milestone3.md) argued criterion 5 could turn out too easy
because small fine-tuned transformers are usually overconfident. On the
rehearsal the opposite happened:

```
mean confidence when right   0.365
mean confidence when wrong   0.358
```

A gap of 0.007 against a 0.05 target — and both numbers sit just above 0.333,
which is what uniform output across three labels looks like. Three epochs on 42
examples barely moved the model off the prior. It also never predicted
`hot_take` at all, sending all three to `analysis`.

**Not updating the criterion.** This is 42 training examples on someone else's
forum, not 140 on mine, and a target gets revised in unit 6 only if it turns
out unmeasurable — not because a rehearsal made it look hard. Recording it here
so that if criterion 5 misses, the diagnosis already has evidence behind it:
under-confidence from thin data, not the overconfidence I predicted.

---

## The real run, when the data exists

1. Commit `labels.csv` first.
2. Open `takemeter.ipynb` from this repo; kernel is this project's `.venv`.
3. Section 1 — fill in `NAME` and `EMAIL`. Still placeholders.
4. Section 2 — `CSV` stays `"labels.csv"`. `LABELS` is already correct. Clear
   every `[FIX ME]` before going on.
5. Section 3 — read the split sizes. Expect `breakdown` near 6 in the test
   split; note it, because criterion 2 is decided on that handful.
6. Section 4 — about three minutes.
7. Section 5 — writes `results.json` and `test_split.csv`. **Commit both.**
   Next unit's `baseline.py` reads `test_split.csv`.

Don't read the numbers closely. The criteria are already filed, and reading
results now is how a filed standard quietly becomes a negotiated one.

Sections 6 and 7 are unit 6. Nothing here needs them.
