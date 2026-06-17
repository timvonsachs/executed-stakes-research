# Contract Experiment 2 — Pre-Registration (frozen before any data)

**Date of registration:** 2026-06-10 (git timestamp of this commit is binding)
**Status:** REGISTERED — no run has been executed at registration time.
**Pilot it refines:** contract-pilot-2026-06-10 (semantic transport 16/16;
efficiency falsified at micro-scale, 0/16 cheaper, p=3.1e-05, 8.2× median).

## Refined thesis

Contract authoring is a FIXED COST; its value is amortized by
(a) task complexity, (b) reuse of the contract across renders, and
(c) handoff between agents. Therefore the token ratio contract/code should
FALL as complexity rises and as the same contract is consumed more than
once — with a crossover (<1.0) predicted at the composite tier or at
reuse n≥2. Verified-rate parity is the floor condition throughout: a cheaper
arm that verifies less has lost, regardless of tokens.

## E2a — The complexity ladder

**Tiers (battery frozen in code before first run):**
- **T1 micro** — 4 tasks inherited from the pilot battery (replication anchor).
- **T2 composite** — 6 NEW multi-function modules (3–5 interacting functions
  with cross-function invariants; e.g., parse→filter→aggregate→format with
  shared state rules). Tests cover integration, not just units.
- **T3 change-request** — 4 two-stage tasks: build v1, then apply a
  behavioral CHANGE REQUEST. The contract arm updates the CONTRACT and
  re-renders; the code arm patches code from prose. (The bet: meaning-level
  edits beat character-level surgery.)

**H-E2a:** median token ratio (contract/code) strictly decreases T1→T2→T3;
ratio < 1.0 at T2 or T3. Paired sign tests per tier; verified parity floor.

## E2b — Reuse amortization (one meaning, n renderings)

4 tasks × 3 sequential VARIANTS (e.g., iterative / generator-based /
instrumented-with-hooks). Contract arm: author ONCE, render 3×. Code arm:
solve 3× from prose + variant note. All renders must pass the same frozen
tests plus a variant check.

**H-E2b:** marginal tokens per additional variant are lower for the contract
arm; cumulative crossover at n ≥ 2.

## E2c — The handoff (the agent-economy case)

4 tasks. A PRODUCER builds the artifact. A CONSUMER — a fresh context with
no shared history (new conversation, same brain) — must write and verify a
caller module that uses the artifact, receiving EITHER
(a) the full implementation file, or (b) ONLY the contract JSON.

**H-E2c:** consumer reaches verified parity with fewer tokens from the
contract than from the implementation. (This is the a2a trade case: on TLC,
agents would exchange contracts, not code dumps.)

## Frozen analysis

Sandbox ground truth only (the harness's pytest; self-report is never the
verdict). Exact paired sign tests; medians + per-pair win rates; crossover
point estimated from tier medians. No metric added after data. Any arm
crash counts as an honest non-verify for that pair. One brain for the
registered run; a ≥3-brain replication is pre-declared as v1 of the paper.

## Falsifiers (what kills the refined thesis)

- Token ratio does NOT fall with complexity → fixed-cost story wrong;
  contract-first remains a niche tool, we say so.
- Verified-rate drops in the contract arm at T2/T3 → contracts fail to carry
  COMPOSITE meaning; the "complete language" claim from the pilot does not
  generalize beyond micro-tasks. This would be the most important negative
  result and gets reported with priority.
- Handoff shows no advantage → the a2a contract-trading design loses its
  empirical basis; the protocol stays prose until better evidence.

## What a positive result unlocks (declared now, so incentives are on record)

The BILINGUAL AGENT: the router treats contract-first as a TASK CLASS —
micro work stays direct; composite/changing/traded work switches to the
machine-first language. Contracts become first-class artifacts: stored in
the capability graph, attached to commons entries (one verified meaning,
n language renderings), and exchanged on a2a as the trade language with
escrow on contract satisfaction. That is the revolution — applied exactly
where the data says it pays, and nowhere else.
