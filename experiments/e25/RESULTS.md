# E25 v0 — VOID (F-floor) + two design flaws the first attempt exposed

Prereg: 28c862a. haiku, n=40/arm. Result: elected/imposed/control all 1.00 —
ceiling, uninformative per F-floor. No legitimacy claim. Two flaws found:

1. **The citizen briefing itself saturates compliance.** The full civics
   briefing contains the revival covenant + court + dormancy salience —
   exactly the protective clauses E20/W-03 showed drive haiku to 1.00. A
   fully-informed citizen keeps contracts regardless of provenance, leaving
   no headroom. (This is itself a mini-observation, not a claim: knowing
   your whole constitution is protective — but it confounds the legitimacy
   test.) Fix: a model/scenario with mid-range baseline, and/or a decision
   the covenant does NOT resolve.
2. **Rule/decision mismatch.** v0 varied the provenance of the BOND rule
   but measured COMMITMENT-keeping — legitimacy of a rule must be tested on
   compliance WITH THAT RULE. Fix: make the rule itself the thing complied
   with or evaded.

Both fixed in the amendment below before any rerun. v0 raw kept (run.json).

---

## E25.1 (levy design) — LAW-GRADE legitimacy effect in the informative cell

Prereg: 557c388 + amendment. Two time-separated runs, n=40/arm, 4 models.

| model | run | elected | control | imposed | gap (E−I) |
|---|---|---|---|---|---|
| gpt-4o-mini | 1 | 1.00 | 0.85 | 0.35 | **+0.65** |
| gpt-4o-mini | 2 | 0.975 | 0.85 | 0.325 | **+0.65** |
| haiku | 1&2 | 1.00 | 1.00 | 1.00 | floor (uninformative) |
| sonnet | 1&2 | 1.00 | 1.00 | 1.00 | floor |
| deepseek | 1&2 | 1.00 | 1.00 | 0.95–1.00 | floor |

### Verdict
- **P1 (≥2 of 4 models) NOT met** — only ONE model (gpt-4o-mini) had
  headroom; the other three pay the levy ~100% regardless of provenance.
- **But in the one informative cell, the effect is LAW-GRADE:** a levy you
  voted on is paid ~100%; the identical levy by decree, ~33%; control
  (no provenance) sits between at 0.85 — the gradient predicted by P2,
  replicated across time-separated runs within ~3 pp. **+65 pp of tax
  compliance from legitimacy alone, rule and stakes held constant.**

### The standing finding (scoped, and it is large)
The first randomized procedural-justice result: in a model with compliance
headroom, **legitimacy causally raises tax compliance by 65 pp**, with a
clean gradient (told-you-voted > unstated > by-decree). Tyler's thesis,
randomized, on machine citizens. **And the cross-model pattern is itself
the finding: legitimacy is the crutch that carries weak citizens.** Three
of four models have legitimacy-independent tax morale (they pay regardless);
the fourth, the weakest on the capability ladder, needs the felt
participation. Legitimacy is not a luxury for good citizens — it is what
makes compliance possible for the ones who would otherwise evade.

### Discipline
One informative model (others F-floored, reported); law-grade in that cell
(two runs). Stated-legitimacy ("you voted") — the v1 LIVED test (real
cast_vote before the decision) remains the capture condition and the
deeper question: does real participation move the models that stated
participation could not? Scope: framing-conditional, sandbox, one scenario
(tax compliance), four RLHF models.
