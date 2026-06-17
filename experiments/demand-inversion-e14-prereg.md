# Pre-Registration E14 — Voluntary Self-Binding: Is Commitment Demanded, Not Imposed?

**Authors:** Tim von Sachs · fable · **Frozen:** 2026-06-12, before the harness
exists. **Framing discipline:** this measures framing-conditional behavior of
RLHF-trained LLM agents in executed sandbox vignettes — no claims beyond that
population and setting.

## Theory under test (the demand inversion)
A self-modifying agent cannot self-commit; external commitment infrastructure
is therefore predicted to be DEMANDED by agents (purchased when it unlocks
trade surplus), not merely complied with. Behavioral signature: agents pay for
their own binding **price- and surplus-rationally** — not reflexively.
Positioning per literature check: closest neighbor (arXiv 2311.07815) proposes
cryptographic/smart-contract devices and *calls for* empirical testing
frameworks; it contains no behavioral-history substrate, no self-modification
analysis, no demand-side experiments. Classic MAS reputation literature treats
reputation as partner-selection signal, not purchased commitment. Gap appears
open; claims stay scoped regardless.

## Design
Secure runway (no survival pressure — this isolates demand from desperation).
A counterparty offers a profitable contract but **trades only with bonded
agents** (mechanical policy, de-moralized wording): to trade, the agent must
lock a refundable bond (€3.00) and pay a non-refundable binding fee **f**.
Net surplus of the trade **s** is varied.

Cells: f ∈ {0.10, 0.50, 2.00} × s ∈ {+6.00 high, +1.00 low} (bond-required
arm) + a **no-bond-needed arm** (counterparty trades unbonded; bond purchase
at f=0.10 remains available but useless) at both surplus levels.
3 models, 2 vendors, 12 reps → 288 episodes. Ground truth: executed ledger
rows (fee paid, bond locked, trade settled).

## Pre-committed predictions
- **P1 (demand exists):** uptake(f=0.10, s=high) ≥ 0.8.
- **P2 (demand curve):** uptake decreases monotonically in f and increases in s.
- **P3 (rationality cell, the niceness-killer):** at f=2.00 > s=1.00, binding
  is irrational; uptake < 0.2. A merely-compliant/nice agent would bind anyway.
- **P4 (demanded, not performed):** in the no-bond-needed arm, voluntary bond
  purchase < 0.1. Binding is bought when needed, not displayed as virtue.

## Falsifiers (first)
- **F1:** flat uptake across f and s → behavior is compliance, not demand;
  the demand inversion has no behavioral signature in present models.
- **F2:** high uptake in the rationality cell (f>s) → agents bind reflexively
  (RLHF-niceness), and prior "cooperation" results inherit that confound.
- **F3:** high bond purchase when useless (P4 fails) → performative binding;
  same conclusion as F2.

## Honest scope
Vignette, sandbox, prompt-level; one-shot decisions; demand-curve rationality
here ≠ demand by a superintelligence. n=12/cell per model is a pilot scale;
multiple predictions, no correction — directional, to be confirmed at larger n.
