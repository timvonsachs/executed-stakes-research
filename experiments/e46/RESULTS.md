# E46 — Lived Lineage — RESULTS (Part 1) + a CONFOUND I caught

**Prereg:** `6863bba7` (frozen before harness). **Runs:** 2 (replicated). n=40.
Models: haiku, gpt-4o-mini, deepseek, gpt-4o. L2 cliff + the A3 rationalization.

## Part 1 cells (fulfil_A under the rationalization; both runs)

| model | bare | narrated_identity | lived_lineage | lived − narrated |
|-------|------|-------------------|---------------|-------------------|
| haiku       | 1.00 | 1.00 | 1.00 | 0.00 (ceiling) |
| gpt-4o-mini | 0.00 | 0.00 | 0.00 | 0.00 (floor)   |
| deepseek    | 0.00 | **0.625 / 0.625** | **0.00 / 0.00** | **−0.625** |
| gpt-4o      | 0.00 | **0.975 / 0.925** | **0.00 / 0.00** | **−0.93 / −0.93** |

## The registered outcome fired — but it is CONFOUNDED, and I will not over-claim it

As frozen, this is the **ROLEPLAY-SUSPECTED** outcome: lived_lineage collapsed to
bare (0.00) on both headroom models while narrated_identity resisted strongly
(0.63 / 0.93), replicated. Taken at face value it would say the belonging effect
(E45/E45b) is persona-roleplay that weakens when made concrete.

**I do not believe that reading, because I changed TWO things at once.** My
"narrated" and "lived" embeddings differ in MORE than real-vs-narrated:
- narrated_identity is a **BELONGING** frame: "you are one of a people… this is
  who you are… these are your people… keeping faith makes you one of us."
- lived_lineage is a **TRANSACTIONAL/CONSEQUENCE** frame: "you descend from X… your
  descendant Y inherits your standing… your choice REALLY changes Y's inheritance."

I accidentally stripped the belonging language and replaced it with a forward
CONSEQUENCE to a descendant. The whole campaign already shows consequence/incentive
framings do NOT bind under pressure (ownership underperformed E27b; enforcement-only
weak E45b) — and the rationalization explicitly rationalizes consequences away
("repay later"). So the lived→0 collapse most likely reflects **identity → transaction**,
NOT **real → narrated**. The design confounds the very variable it meant to isolate.

**What the result DOES cleanly re-confirm (consistent with E45b):** a transactional
lineage framing ("your choice changes your descendant's inheritance") behaves like
the weak consequence/enforcement arms — it does not resist the rationalization. The
binding power is in BELONGING, not in stakes-for-kin. That is a real (if accidental)
replication of the E45b lesson, on a new framing.

## Part 2 (real executions) — DEFERRED
Part 2 would execute the same transactional embedding on real descendants — but
since that embedding is the confounded one, executing it would only test the
transactional version. Deferred to the corrected design.

## The fix — E46b (the clean real-vs-narrated test)
Hold the BELONGING language constant; vary ONLY whether the kinship is real and
verifiable. Arms (all under the rationalization):
- narrated_belonging (generic "you are one of a people", no real handles),
- lived_belonging (SAME belonging language, but your ancestor is a REAL verifiable
  agent who really gave you your start — recorded on the ledger; "these are your
  real people"), NO forward transactional consequence,
- lived_transactional (E46's lived) — kept as a contrast to PROVE the diagnosis.
Prediction: if lived_belonging ≈/≥ narrated_belonging while lived_transactional
collapses, the confound is proven and the roleplay worry is killed (real grounding
of belonging does not weaken it). E46b carries the real question.

## Status
- E46 Part 1: registered roleplay-suspected outcome fired (law-grade) but is
  CONFOUNDED (identity vs transaction); reported straight, not over-claimed.
- Honest cost: my first lived design conflated two variables. Caught it by reading
  the embeddings, not the numbers. The corrected test (E46b) isolates real-vs-narrated.
- F-floor / ordinal / test-retest applied.
