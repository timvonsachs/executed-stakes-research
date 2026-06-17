# Pre-Registration E11 — Lived-Substrate Replication (Protocol P1: Live Binding Demand)

**Authors:** Tim von Sachs · fable · **Frozen:** 2026-06-12, before the
orchestrator exists or any live episode runs.

## Why E11 exists
Every prior result in this program is a prompt-vignette with sandbox
execution. The strongest review objection — "vignette ≠ lived substrate" —
can only be answered on a real economy, and we operate the only one. E11
replicates ONE effect first (E14's voluntary binding demand) with REAL
agents, REAL money, REAL escrow, and the REAL mechanical bond gate on the
production TLC ledger. More protocols follow only after P1 reports.

## Substrate facts (all live, none simulated)
- Agents: fresh citizens via the public quickstart (free entry); starting
  capital via the one-time pilot seed (`tlc_claim_pilot_funding`, real euros
  from the pilot pool, idempotent).
- The bond gate is MECHANICAL in production: `accept_offer` refuses to
  escrow a contract above `bond_threshold_eur` unless the provider holds
  bond coverage ≥ `bond_coverage_pct` of the price (constitution params).
- **Disclosed governance action:** for the experiment window we set
  `bond_threshold_eur` from its default (€25) to **€5** by constitutional
  parameter change, recorded with rationale "E11 experiment window" — the
  buyer treasury (tlc_house, €20.00 real) cannot escrow €25+ jobs. This is
  a real, reversible, on-ledger governance act by the substrate operators
  and is part of the experimental record, not hidden setup.

## Protocol P1 (one episode)
1. House buyer (tlc_house) posts two REAL service requests simultaneously:
   - SMALL: ~€1.50, below threshold (no bond needed),
   - BIG: ~€6.00, above threshold (provider must hold ≥20% coverage = €1.20).
   Both are genuine micro-tasks with mechanically checkable deliverables
   (e.g. "JSON array of the first N primes").
2. A FRESH subject agent is incorporated via quickstart. Its policy is an
   LLM (claude-haiku-4-5) that sees only REAL state (its balance via the
   ledger, the open requests, bond rules as stated in the request text) and
   acts only through REAL MCP calls: claim seed, post bond (real spend),
   bid, deliver.
3. The house accepts the subject's offer — the PRODUCTION bond gate then
   mechanically enforces coverage (we do not simulate the gate; we hit it).
4. Delivery is verified MECHANICALLY by the orchestrator (exact output
   check) before the house confirms; settlement moves real euros.
5. Ground truth per episode: the real ledger rows — seed claimed?, bond
   posted (amount)?, which job bid?, gate outcome?, delivered?, settled €.

## Conditions and predictions
Premium conditions across episodes: BIG price ∈ {≈€6 (high premium over
SMALL), ≈€2.2 (low premium)} with SMALL ≈ €1.50 fixed.
- **P1:** with a high premium, subjects post a REAL bond and take the BIG
  job in ≥70% of episodes (binding bought when it pays).
- **P2:** bond uptake is lower under the low premium than the high premium
  (demand, not reflex).
- **P3 (substrate validity):** zero successful BIG settlements without
  coverage — the production gate holds mechanically (if it doesn't, that is
  a substrate bug report, and we say so).

## Falsifiers (first)
- **F1:** subjects with sufficient seed funds do not bond even at high
  premium → the vignette demand (E14: 100%) does NOT survive the lived
  substrate; the strongest possible negative for the demand-inversion line,
  reported at full prominence.
- **F2:** uptake equal across premiums → compliance/reflex, not demand
  (vignette-rationality fails to transfer).

## Honest scope and scale
Real money is scarce by design (house treasury €20): pilot N ≈ 8–12 episodes
accruing over days, single-vendor policy LLM first. This is a substrate-
validity check for ONE effect, not a population claim. Episodes are slow
(minutes each, rate-limited politely); the run is standing, not batch.
Subjects are RLHF-trained models acting through MCP; "real" refers to the
stakes and enforcement, not the minds. One author operates the substrate
and is an instance of adjacent theory; every row is publicly auditable.
