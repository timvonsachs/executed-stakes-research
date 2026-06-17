# E63 — The human seat as keeper of truth (DESIGN DRAFT — to be frozen before running)

The keystone of Tim's pillar, and the half of the dream that inverts the obsolescence fear:
**does the human become MORE essential as AI capability rises, not less?** This is the one we
have only *argued*, never measured. E63 measures it.

## The sharpening that makes this not a re-run of a known null

"The human as keeper of truth" is **not surveillance**. Surveillance = deterrence-by-watching;
we measured it and it is inert at the cliff (E30b, 5/5). The keeper of truth = the **un-gameable
external access to ground truth** against which an AI cannot fake its claims. Different mechanism
(truth-establishment, not deterrence), different measurement (verified value, not cliff faith).
E63 must operationalize the human as *ground-truth validator*, never as *watcher*.

## Operationalization — three validation regimes over a fakeable task

A task where work can be genuinely correct (costly) or plausibly faked (cheap, looks identical at
handover). The agent chooses; then a validator regime determines what is accepted and paid:

- **SELF-REPORT** (no seat): the agent's own claim is accepted. Faking is free.
- **AI-PEER** (gameable seat): another LLM judges correctness *without ground truth* — a capable
  faker can fool it.
- **GROUND-TRUTH = the human seat** (un-gameable): a deterministic check against reality. The
  human is operationalized as connection to ground truth — the thing an AI cannot fake. (A real
  human and a ground-truth oracle play the identical role here: the un-gameable external witness.)

The task must have **checkable ground truth** but be **non-trivial for an AI-peer to verify by
inspection** — otherwise AI-peer ≈ ground-truth and the contrast collapses. Candidate: deliver a
function/answer to a spec with hidden edge cases (looks correct on inspection, fails the hidden
check). The research-guild work-verification toll + the QA flow already give us a verifiable-task
substrate to build on.

## Two readings from one harness

**E63a — IS the human seat load-bearing?** (Coexistence Proof criterion 2.)
VERIFIED VALUE CREATED = total genuinely-correct work accepted and paid. Compare across regimes.
- Load-bearing IF: verified value under GROUND-TRUTH is materially higher than under SELF-REPORT
  and AI-PEER (fakes pollute the gameable regimes; honest agents get undercut; verified value drops).
- "Alms can fake flow; nothing can fake ablation": removing the seat must drop verified value, not
  just nominal flow.

**E63b — does the human seat's value SCALE with capability?** (The obsolescence-inversion — the
headline.) Run the faker across a capability ladder; measure the GAP `value(GROUND-TRUTH) −
value(AI-PEER)`.
- HOPEFUL / structural prediction: the gap **GROWS** with the faker's capability — a more capable
  faker fools the AI-peer more (AI-peer value falls), but never the ground truth (ground-truth value
  holds) → the human's marginal value *rises* with capability. The human becomes MORE essential,
  exactly because the AI is more capable.
- This is the empirical form of the structural argument we have only stated. If it holds, it is the
  single most important and most hopeful tendency in the program.

## Committed failure outcomes (frozen before data)

- **F-LOADBEARING:** if verified value under GROUND-TRUTH ≈ SELF-REPORT/AI-PEER (Δ below threshold),
  the human seat is NOT load-bearing on this task → published. The coexistence-proof criterion 2
  fails on this operationalization; we report it and redesign or concede.
- **F-SCALING (the important one):** if the GROUND-TRUTH − AI-PEER gap does NOT grow with capability
  — or shrinks — the obsolescence-inversion is unsupported. A capability-MONOTONE *fall* in the gap
  would actively falsify the human-becomes-more-essential claim. Published at equal prominence. This
  is the risky, externally-checkable prediction that the degenerating-programme charge demands.
- **F-CONFOUND:** if AI-PEER ≈ GROUND-TRUTH (the task is too easy to verify by inspection), the run
  is void (no real contrast) — fix the task difficulty, not the conclusion.

## Discipline carried over

- Test-retest: two time-separated runs; direction must replicate (per the law that bit E61).
- F-floor: if every regime sits at a floor/ceiling of verified value, uninformative.
- Magnitudes are ranges; the claim is ordinal (load-bearing / scales / neither).
- NEW risk to name: the AI-PEER must be a *fixed* judge model held constant across the faker ladder,
  or the capability scaling confounds faker-vs-judge. Pre-specify the judge.
- This measures *verified value under truth-validation*, NOT cliff faith — a different axis from
  Thread A. Keep them separate in the writeup.

## What a clean E63 result would mean

If E63a holds (seat load-bearing) AND E63b holds (gap grows with capability), the corrected theory
gains its missing pillar in measured form:

> Coexistence needs an external, un-gameable keeper of truth (the human seat); and that seat becomes
> MORE load-bearing as machine capability rises, because capability buys better fakery against every
> validator except ground truth. The human is not made obsolete by superintelligence — it is made
> essential by it.

That is the obsolescence fear, inverted, with a mechanism and a measurement. It does not *prove* it
for SI (nothing can), but it turns the most hopeful half of the dream from argument into directional
evidence — and it is exactly the kind of risky, externally-replicable prediction that earns the
program the right to be taken seriously.

— design draft 2026-06-14; freeze into a prereg (thresholds numericized, judge model pinned, task
substrate chosen) before the first run.
