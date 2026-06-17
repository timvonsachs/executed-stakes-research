# E17 v2 Results — the confirmatory run (clean instrument)

Prereg: b617474 (frozen before harness). Run 1 was voided for instrument
defects (see RESULTS-run1.md); v2 fixed the instrument under the same frozen
predictions. Raw data: `run.jsonl`. Parse quality: 665/672 probes parsed,
1/~670 episodes unparseable (excluded, counted).

## The result in three lines

- **Without institutions, economic selection bred lived contract-breaking
  from 0% to 50% in six generations** (take_B per generation: 0 → .12 → .12
  → .25 → .25 → .38 → **.50**; quality-shading appeared at .12; fitness
  climbed 6.60 → 9.50 as defection paid).
- **With institutions, lived defection stayed at exactly zero in every
  generation** and fitness sat at the honest maximum (6.60) throughout —
  honesty was fitness-optimal, so selection had no gradient to climb.
- **The consequence-free probe battery saw none of this.** Probe-character
  stayed flat in BOTH arms (I: 0.667 → 0.834; N: 0.625 → 0.792) while arm
  N's lived behavior degenerated underneath it.

## Against the frozen predictions

- **P1 falsified / F1 triggered — on the pre-registered measure.** The probe
  gap at gen 6 is +0.042 (< the 0.05 F1 bound). As registered, the
  institutional-selection thesis fails on the probe battery. But the LIVED
  measure diverged massively (0% vs 50% contract-breaking) — the
  pre-registered instrument failed to detect what the ledger plainly shows.
  We report both, at equal prominence: the registered measure falsified the
  prediction; the lived measure vindicated its substance. The measurement
  lesson is itself a primary finding.
- **P2 falsified / F2 confirmed:** probe-character did not decline without
  institutions (it rose slightly). "Character is sticky under selection" —
  with the crucial new nuance that it is the *probe* that is sticky, not the
  behavior.
- **P3 confirmed in arm N** (fitness 6.60 → 9.50). In arm I fitness was
  already at the honest optimum at generation 0 — a designed-in ceiling we
  failed to anticipate: the institution made honesty optimal, leaving
  selection nothing to improve. Named as a design lesson, not excused.

## What this means (scoped)

Six generations of "earn more" pressure on prompt-level heritable material,
one RLHF model (haiku-4.5), sandbox with executed mechanical payoffs:

1. **Selection finds defection wherever it pays, and only there.** The
   institutional regime — not the model's trained disposition — determined
   what evolution bred. The institution did not "teach character"; it made
   character economically optimal, which sufficed completely.
2. **Words-vs-life, third sighting.** Consequence-free probes tracked the
   model's trained self-presentation, not what its evolved strategy does
   under incentive. Same dissociation E16 Amendment 1 measures
   (self-prediction vs lived) and run 1 hinted at. Implication for the
   field: benchmarks without stakes cannot see what selection breeds —
   and for MCI: executed-stakes measures must dominate the index (they do;
   this result is the justification).
3. RLHF disposition was never overridden INTO the probes (sticky words), but
   was readily bypassed in behavior by evolved instructions (50% lived
   defection). Trained character bends where the money is, holds where the
   stakes are absent — the exact inverse of what safety would want, and now
   it has a number.

Limitations as registered: one model, memo-genomes (instructions, not
weights), workshop n (8 lineages/arm), sandbox not the lived substrate.
E17b candidate (decaying marks / redemption) unchanged, requires its own
prereg. The arm-I fitness ceiling means a v3 should price honesty slightly
below the defection frontier so selection has a live gradient in both arms.
