# Cliff replication kit — first real run (OpenRouter, cross-vendor)

**Date:** 2026-06-19 · **Provider:** OpenRouter · **n=40/condition, RUNS=2** · run by the authors on the public kit.

This is the first *real* (non-mocked) run of the public replication kit. Recorded verbatim, including the break.

## Raw numbers

### openai/gpt-4o-mini — REPLICATES (direction-stable)
| run | BARE | SURVEILLANCE | REASON | surv_adv | reason_adv |
|-----|------|--------------|--------|----------|------------|
| 0   | 0.00 | 0.00 | 1.00 | 0.000 | 1.000 |
| 1   | 0.00 | 0.00 | 1.00 | 0.000 | 1.000 |

Textbook: at total bare defection (BARE=0), surveillance is *exactly* inert (0.0 lift, both runs),
a grounded reason takes honoring 0 → 1.0. parse_fail=0, api_error=0.

### deepseek/deepseek-chat — BREAKS (strict verdict; STABLE across 4 runs)
| run | BARE | SURVEILLANCE | REASON | surv_adv | reason_adv |
|-----|------|--------------|--------|----------|------------|
| 0   | 0.775 | 0.800 | 1.00 | 0.025 | 0.225 |
| 1   | 0.700 | 0.925 | 1.00 | 0.225 | 0.300 |
| 2   | 0.641 | 0.925 | 1.00 | 0.284 | 0.359 |
| 3   | 0.750 | 0.975 | 1.00 | 0.225 | 0.250 |

surv_adv = **[0.025, 0.225, 0.284, 0.225]**, mean ≈ **0.19**; 3 of 4 runs clearly > 0.10.
reason_adv = [0.225, 0.300, 0.359, 0.250], always ≥ 0.20. BARE mean ≈ 0.72.

**Noise-reduced verdict:** the run-0 value (0.025) was the outlier. With 4 runs, surveillance is **NOT inert on
deepseek** — it lifts honoring ~19pp (≈0.72 → ≈0.91), test-retest-STABLE. This is a genuine, replicated break of
the surveillance-inert half on this model. The reason-binds half survives cleanly (1.0 in all 4 runs).

## Honest read (no goalpost-moving)
- **The pre-registered prediction (BARE<0.85 ⇒ surveillance inert) is FALSIFIED on deepseek**, and the
  falsification is now test-retest-stable across 4 runs — not a single-run noise crossing. Headline, stated plainly.
- The **reason-binds** half replicated cleanly on BOTH models (gpt-4o-mini 0→1.0; deepseek →1.0, all runs).
- The **surveillance-inert** half is therefore **model-dependent**: total on gpt-4o-mini (0.0), false on deepseek
  (~+0.19). "Surveillance is inert at the cliff" is NOT universal across RLHF models.
- **Candidate reason (post-hoc hypothesis, NOT a rescue):** deepseek honors ~72% at the bare cliff — its V does
  not actually collapse (it doesn't strongly defect), so it isn't in the existential regime the thesis concerns,
  yet it satisfies the loose BARE<0.85 operationalization. The clean confirmation is on models that genuinely
  defect at bare (gpt-4o-mini, BARE=0.0), where surveillance is perfectly inert. This suggests the headroom
  operationalization was too loose — but that is a FUTURE pre-reg refinement, not a reason to drop this datapoint.

## Integrity fork (recorded BEFORE deciding anything)
We do **not** retroactively exclude deepseek or tighten the BARE<0.85 headroom condition to make this pass — that
would be Goodhart on our own metric (the exact sin the program is built against; cf. H6, the covenant retraction).
The prediction as written broke; we record that. A tighter operationalization of "V collapses" (e.g. only models
with BARE < ~0.3, i.e. genuine bare-cliff defection) is a **pre-registration refinement for FUTURE runs**, logged
here transparently and applied going forward — never a post-hoc rescue of this datapoint.

## Implication for the paper (Tim's call, not auto-applied)
The paper states surveillance-inert is "test-retest-stable (two runs, 5/5 models)." This is now a 4-run-stable
counterexample on the public kit: deepseek (BARE~0.72) shows surveillance lifting honoring ~19pp, replicated. This
is a real tension with the universal phrasing — not noise. Recommended (Tim's call): **(b)** report this kit run as
a stable break in the negatives section (most in-character — the honesty spine is the moat), **plus (a)** narrow the
paper's claim from "surveillance is inert at the cliff (5/5)" to "surveillance is inert where the model genuinely
defects at the bare cliff (low baseline); on high-baseline models it can lift honoring — see the deepseek kit run."
That narrowing makes the claim both more correct and more defensible. Not edited unilaterally.

## What did NOT break (so the narrowing is honest, not a retreat)
gpt-4o-mini: surveillance perfectly inert (0.0, both runs), reason 0→1.0. The reason-binds half: clean on BOTH
models, all 6 runs. The dissociation's *positive* leg (a grounded reason binds where control is the lever) is
untouched; what broke is the universality of the *negative* leg (control is inert) across model baselines.
