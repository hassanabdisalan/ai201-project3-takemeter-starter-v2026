# Milestone 2 — Boundary stress test

The taxonomy lives in [README.md](README.md). This file is the stress test that
produced its final wording.

**All eight posts below are AI-generated for this test.** They are not real
r/nba comments and none of them go in `labels.csv`. Their job is to sit on the
boundaries and see whether the definitions hold.

---

## The definitions as first written

- `breakdown` — makes a claim about basketball and rests it on at least one
  specific, checkable detail the claim would not survive without.
- `take` — asserts a general evaluation, offering no support it depends on.
- `reaction` — responds to the moment; the writer's experience, a joke, an
  exclamation, no evaluative claim.

Decision rule v1: **the deletion test.** Delete the specifics; if the claim
still stands as written, it's a `take`.

---

## The eight

| # | Post | Boundary | v1 verdict | Clean? |
|---|---|---|---|---|
| 1 | "Jokic is the best passer in league history and it's not close." | take / breakdown | `take` | ✅ |
| 2 | "Jokic had 14 assists tonight. Best passer in league history, not close." | take / breakdown | `take` | ✅ |
| 3 | "Wemby blocked three in a row and I put my phone down and just sat there." | reaction / breakdown | **`breakdown`** | ❌ |
| 4 | "That no-call at 1:48 was a foul — he got him across the wrist before the ball left his hand." | take / breakdown | **`take`** | ❌ |
| 5 | "31% from three since the break and they still run him off two screens a possession. That's the offense problem." | breakdown / take | `breakdown` | ✅ |
| 6 | "This ref crew is the worst in the league." | take / reaction | `take` | ✅ |
| 7 | "I am so tired of this team." | take / reaction | `reaction` | ⚠️ |
| 8 | "Everyone in here is overreacting to one game in October." | take / reaction | `take` | ⚠️ |

Three clean, two broken, two defensible-either-way. The two breaks are the
useful part.

---

## Break 1 — post 3: the deletion test ran when it shouldn't have

*"Wemby blocked three in a row and I put my phone down and just sat there."*

This is a man describing his evening. It is `reaction` by any reading. But it
contains a specific, checkable detail ("three in a row"), so the deletion test
grabs it and calls it `breakdown`.

The bug is **ordering**. v1 reaches for the stat first, and anything with a
number in it gets pulled toward `breakdown` — which is the exact failure the
taxonomy was built to avoid, just arriving from the other direction.

**Fix — the rules are ordered now.** Ask first whether the post makes an
evaluative claim about basketball at all. If it doesn't, it is `reaction` and
the deletion test never runs on it.

## Break 2 — post 4: deletion is the wrong instrument for a narrow claim

*"That no-call at 1:48 was a foul — he got him across the wrist before the ball
left his hand."*

Delete the specifics and you get *"that no-call was a foul"* — a claim that
stands exactly as written. v1 says `take`. That's wrong, and it's wrong in the
expensive direction: this is the single most argued post type in a game thread.

The problem is that deletion measures the wrong thing. Both post 2 and post 4
reduce to a bare assertion. What separates them isn't whether a claim survives
deletion — it's whether the detail was ever **about** the claim. "14 assists
tonight" gives nobody a reason to believe "best passer ever". "Across the wrist
before the ball left his hand" is precisely what makes something a foul.

**Fix — add the relevance clause.** After deleting, ask: *would someone who
disagreed have to answer that detail?* If yes, it was load-bearing and the post
is `breakdown`, however short the claim is.

- Post 2: a disputer says "assists tonight say nothing about all-time" and
  walks away. Not load-bearing → `take`.
- Post 4: a disputer has to argue about the wrist. Load-bearing → `breakdown`.

## The two ⚠️ cases

Posts 7 and 8 are defensible either way and stay that way — this is what the
tie-break exists for.

Post 7, *"I am so tired of this team"*, is grammatically about the writer, so
rule 2 sends it to `reaction`. Someone arguing `take` is reading the implied
verdict, and they aren't wrong. Rule 2 decides it, consistently, and the cost
of that consistency is that a few posts get a label a reasonable person would
dispute. That is the correct trade — **a rule I apply the same way every time
beats a rule that is right more often and applied two ways.**

Post 8 is a claim about the thread, not about basketball. Ordering sends it to
`reaction` (no basketball claim), the words send it to `take`. Called `take`:
"overreacting to one game" is an evaluation of a basketball opinion, and
treating meta-commentary as basketball commentary keeps `reaction` from
becoming a bucket for everything hard.

---

## What changed in the README

1. The rules are **ordered**. `take`/`reaction` first, deletion test second.
2. The deletion test gained the **relevance clause** — the detail has to be
   something a disputer would have to answer.
3. Tie-break kept: most words wins.

---

## One thing to watch in Milestone 4

The imbalance risk is `reaction`, and it isn't close. A straight pull from a
Post Game Thread is mostly jokes, one-liners and venting — plausibly 70%+ on
its own, which breaks the "no label above 70%" requirement before any
labelling judgement is involved.

Collecting from Daily Discussion Threads alongside game threads should push the
mix toward argument. **Check the counts at 60 posts, not at 200.**
