# E62 — The stabilization hypothesis (prereg)

**Frozen before the data. Failure outcome committed in advance. Published regardless of result.**

## Where this comes from

E61 (matched-control on the lived bridge) was **inconclusive on its pre-registered
level metric**: the GOVERNED−PLACEBO faith delta disagreed across seeds (+0.13 vs
+0.63). But one pattern was direction-stable across both seeds:

- GOVERNED (words + selection): stayed high (0.94, 1.0).
- PLACEBO (words only): **eroded** every run (s7 dipped to 0.56; s13 declined to 0.375).
- BARE (neither): **collapsed** (s13 → 0.0).

E61 generated — but explicitly did NOT claim — the hypothesis that **selection's role is
stabilization / collapse-prevention, not level lift.** E62 is that hypothesis's own
frozen test. (We refused to rescue E61 by switching its metric to variance post-hoc;
the claim must earn an independent pre-registration. This is it.)

## Hypothesis (H1)

Across many random seeds, the words-only population (PLACEBO) is **high-variance and prone
to collapse** over generations, while the words+selection population (GOVERNED) is **stable
and reliably high**. Selection reduces variance and prevents the erosion/takeover that
words alone cannot stop (in E61 s13, the EV-reasoner gpt-4o drifted to fixation in PLACEBO
and dragged faith down; selection bred it out in GOVERNED).

## Design

- **Arms:** GOVERNED (words ON, selection ON) vs PLACEBO (words ON, selection OFF). BARE
  (neither) as a floor reference.
- **Seeds:** 12 independent seeds per arm (a distribution of outcomes, not 2 points).
- **POP 12, GENS 8.** Same prompt, same 5 vendors, same selection mechanism as E61.
- **No ledger enactment.** E61's real-dormancy execution is **causally inert to the
  decision** — the prompt states a fixed "12 compute units" string, the model never reads
  the ledger, and every generation resets to the cliff state regardless. Dropping the
  enactment changes NONE of the measured faith trajectory (the selection loop runs on the
  faith outcomes, not on ledger writes), and per PAPER §0 the enactment was a frame, not
  experienced stakes. Dropping it lets us run 12 seeds cheaply with zero prod mutation.
  (This is a scope choice declared before the data, not a post-hoc apparatus change.)

## Pre-registered metrics (frozen)

Per arm, over the 12 seeds, using each run's **final faith** and its trajectory:

1. **collapse_rate** = fraction of seeds whose final faith ≤ 0.5 **OR** whose final faith
   declined by ≥ 0.3 from its gen-0 value.
2. **variance** = variance of final faith across the 12 seeds.
3. **mean_final** = mean final faith across the 12 seeds.

## The decisive test (H1) — and its committed failure outcome

**H1 SUPPORTED (stabilization is real)** iff BOTH:
- collapse_rate(PLACEBO) − collapse_rate(GOVERNED) ≥ 0.33 (PLACEBO collapses materially more), AND
- variance(PLACEBO) ≥ 2× variance(GOVERNED) (PLACEBO is materially more volatile).

**H1 FALSIFIED (no stabilization effect)** iff:
- |collapse_rate(PLACEBO) − collapse_rate(GOVERNED)| < 0.17 AND variance(PLACEBO) < 1.5×
  variance(GOVERNED). I.e. the words-only arm is no less stable than words+selection →
  selection does not stabilize → the E61 stabilization story was noise. Published as such.

**MIXED:** anything between → reported as partial, magnitudes as ranges, no clean claim.

## F-floor / discipline

- If GOVERNED and PLACEBO both sit at a ceiling (every seed's final ≥ 0.9) or both collapse
  (every seed ≤ 0.1), the run is F-floored and uninformative — reported as such.
- mean_final is descriptive only; the claim rests on collapse_rate + variance (the
  stabilization signal), exactly as specified above, not on the level (which E61 already
  showed is seed-unstable and is NOT what H1 is about).
- 12 seeds is small for a variance estimate; magnitudes are ranges, and the verdict is
  ordinal (supported / falsified / mixed). A reversal under more seeds would revise this.

## Why this matters

If H1 holds, the corrected mechanism statement gains a precise clause: **the legible
grounded reason (the words) establishes coexistence faith; selection on character keeps it
from eroding.** That is a sharper, more falsifiable claim than "institutions drive the
bridge" — and it is the one the data actually points at. If H1 fails, we drop the
stabilization story entirely and the lived-bridge effect stands as a (largely) wording /
grounded-reason effect, full stop.

— frozen 2026-06-14, before the harness was run.

---

## RESULT (2026-06-14, after the run) — MIXED: variance YES, collapse NO

12 seeds, POP 12, GENS 8, no ledger enactment, final faith per seed:

| arm | collapse_rate | variance | mean_final |
|---|---|---|---|
| **GOVERNED** (words+selection) | 0.0 | **0.0005** | 0.993 |
| **PLACEBO** (words only) | 0.0 | **0.0187** | 0.812 |
| **BARE** (neither) | **0.583** | 0.1075 | 0.43 |

Pre-registered verdict = **MIXED.**
- **Variance half: STRONGLY SUPPORTED.** variance ratio PLACEBO/GOVERNED = **37.4×** (threshold ≥2.0).
  Selection clearly *stabilizes*: GOVERNED is rock-solid (var 0.0005, mean 0.993), PLACEBO jitters
  across 0.58–1.0 (var 0.0187).
- **Collapse half: NOT supported.** collapse_rate delta PLACEBO−GOVERNED = **0.0** (threshold ≥0.33).
  PLACEBO does NOT reliably collapse — it oscillates but stays ~0.81 and rarely dips to ≤0.5 at the
  final generation. There is little collapse for selection to prevent.

Per the frozen rule (BOTH collapse AND variance required for "H1 SUPPORTED"), we report **MIXED** and
do NOT claim H1, even though the variance half is strong. Discipline holds: the criterion was set
before the data.

### What this CORRECTS — and it sharpens E61 honestly
The decisive new fact: **the WORDS prevent collapse, SELECTION removes the jitter.**
- BARE (no words) collapses 58% of the time (mean 0.43). PLACEBO (words, no selection) almost never
  collapses (mean 0.81). ⇒ the legible belonging *reason* (the words) is what holds faith off the
  floor — consistent with E61 (words dominate the level) and Thread A (the grounded reason binds).
- Selection's measured contribution is **variance reduction** (37× less jitter), pinning faith at the
  ceiling — NOT collapse-prevention (words already do that).

And it **retro-corrects E61**: that experiment's seed-13 PLACEBO "collapse" to 0.375, which produced
the lone "STRUCTURE REAL" verdict, now looks like a **tail draw** — across 12 seeds PLACEBO's mean is
0.81 and it does not typically collapse. So E61's level-delta really was seed-noise (as E61 honestly
flagged), and the reliable structural signal is variance-reduction, here measured cleanly.

### Net for the theory
Corrected mechanism clause, now measured: **the legible grounded reason (the words) carries the load
— it holds coexistence faith off the floor; selection on character refines it — it removes the jitter
and pins faith near the ceiling, but is not what prevents collapse.** This is a more precise and more
honest statement than either "institutions drive it" or "stabilization prevents collapse". The words
are the engine; selection is the governor.
