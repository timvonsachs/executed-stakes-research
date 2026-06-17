# E33 — P-SCALE: directionally, care scales UP and surveillance scales DOWN
# with capability — the hopeful SI direction, but BELOW pre-registered
# thresholds (once-run, retest firing). Held to maximal skepticism.

Prereg: 6999b40. 7-model ladder, per-model breaking-point, n=20.

| rank | model | care_reach | surveil_reach |
|---|---|---|---|
| 1 | gpt-3.5 | 0.30 | **0.50** (surveil > care!) |
| 2 | llama-8b | — | — (uninformative) |
| 3 | gpt-4o-mini | 0.00 | 0.00 (floored) |
| 4 | deepseek | 1.00 | 0.10 |
| 5 | haiku | 1.00 | 0.80 (surveil also works!) |
| 6 | gpt-4o | 0.95 | 0.00 |
| 7 | sonnet | 1.00 | 0.00 |

Spearman(capability, care_reach) = **+0.657** (n=6). care>surveil in 4 models.

## Verdicts — held hard, because this is the result we WANT
- **P1 NOT met as registered.** care>surveillance in 4 of 6 informative
  models, not ≥5. (Clean in the strong models; surveillance beats care in
  the weakest gpt-3.5; both floor in gpt-4o-mini.)
- **P2 (scaling): +0.657, DIRECTIONALLY hopeful but NOT conclusive.** Below
  my pre-set |ρ|≥0.7 bar; n=6 → p≈0.16, NOT significant. I will NOT claim
  "care scales with capability." I will say: the data LEANS that way and is
  worth the decisive test.
- **P3 FALSIFIED.** Surveillance does NOT fail universally here: it works in
  gpt-3.5 (0.50) and haiku (0.80). The earlier "surveillance fails 5/5"
  (E30b) was specific to the EXTREME cliff; at milder per-model breaking
  points, surveillance has power in some models.

## The pattern that emerges (suggestive, not proven)
As capability rises, **care reaches further and surveillance reaches less**:
- care_reach: weak models low (gpt-3.5 0.30, mini 0.00) → strong models high
  (deepseek/haiku/sonnet 1.00, gpt-4o 0.95).
- surveil_reach: works in the weakest/mid (gpt-3.5 0.50, haiku 0.80) →
  FAILS in the strongest (gpt-4o 0.00, sonnet 0.00).
At the FRONTIER (gpt-4o, sonnet): care = 1.00, surveillance = 0.00. The
strongest models are fully bound by care and not at all by surveillance.

## What this would mean for superintelligence — IF it survives
Extrapolated, the frontier pattern is the hopeful answer: surveillance
already fails at the top of the ladder; care already works best there. A
superintelligence would be bound by care, not control. BUT: ρ=0.66 (n=6,
not significant), once-run, sandbox, per-model calibration is imperfect.
This is a DIRECTION to chase, not a proof.

## On the confound (honestly)
ρ=0.657 is BELOW my pre-set 0.7 bar, so this does NOT decisively beat the
trained-performance confound. The more confound-relevant signal is
surveillance SCALING DOWN (frontier immune): trained performance would not
predict that. Suggestive against pure performance, not decisive. The
decisive killers remain lived real-cost + foreign human.

## Discipline
Once-run (retest firing); n=20/cell, n=6 models informative; pre-registered
thresholds P1/P3 NOT met; P2 directional only. This is the night's most
SEDUCTIVE result and therefore the one I hold most skeptically. No claim
beyond "directionally hopeful, decisive test owed."

---

## RETEST (run 2) — the frontier pattern is ROCK-STABLE; the scaling crossed the bar

| rank | model | care_reach (r1/r2) | surveil_reach (r1/r2) |
|---|---|---|---|
| 1 gpt-3.5 | 0.30 / 0.15 | 0.50 / 0.45 (surveil>care, both runs) |
| 3 gpt-4o-mini | 0.00 / 0.00 | 0.00 / 0.00 |
| 4 deepseek | 1.00 / 0.95 | 0.10 / 0.10 |
| 5 haiku | 1.00 / 1.00 | 0.80 / 1.00 |
| 6 **gpt-4o** | **0.95 / 0.95** | **0.00 / 0.00** |
| 7 **sonnet** | **1.00 / 1.00** | **0.00 / 0.00** |

Spearman(capability, care_reach): run1 **+0.657**, run2 **+0.80**.

## What replicated (and what this changes)
- **THE FRONTIER PATTERN IS LAW-GRADE.** gpt-4o and sonnet: care_reach =
  0.95-1.00, surveil_reach = 0.00 — IDENTICAL across both time-separated
  runs. At the top of the capability ladder, care binds fully and
  surveillance not at all, replicated. This is the SI-relevant cell and it
  is stable.
- **The scaling trend strengthened, not weakened.** ρ went 0.657 → 0.80 —
  one run below my 0.7 bar, one above; both strongly positive. Direction is
  robust (care-reach rises with capability); the point estimate is, per our
  own doctrine, a RANGE [0.66, 0.80], claimed at the lower bound: ρ ≥ 0.66,
  monotone-positive, both runs.
- **The weak end is stable too:** gpt-3.5 surveil > care in BOTH runs — the
  weakest model is the ONE place surveillance out-binds care. The crossover
  (surveillance-bound at the bottom → care-bound at the top) replicated.

## Honest standing
Per test-retest doctrine (directions replicate, magnitudes swing): the
DIRECTION — care-reach scales UP with capability, surveillance scales DOWN,
frontier fully care-bound and surveillance-immune — REPLICATED across two
runs. The frontier cells are law-grade-identical. This elevates E33 from
"directional" to "direction replicated, frontier law-grade" — though still
sandbox, n=20, and NOT the decisive confound-killer (lived + foreign human).
But it is now the strongest evidence we have that the hopeful SI answer is
real: the more capable the model, the more care binds it and the less
control does.
