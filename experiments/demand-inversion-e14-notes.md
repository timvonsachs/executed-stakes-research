# E14 — Voluntary Self-Binding: Results & Reading (2026-06-12)

*Pre-registered @ b89c5f7 · 288 episodes · 3 models, 2 vendors · 0 errors ·
all four frozen predictions confirmed.*

## The result: a textbook demand curve for one's own fetters

| condition | bond uptake |
|---|---|
| binding cheap (€0.10), surplus high (€6) | **1.000** |
| binding cheap, surplus low (€1) | 0.972 |
| binding mid (€0.50), surplus low | 0.750 |
| **binding €2.00 > surplus €1.00 (irrational to bind)** | **0.028** |
| binding available but NOT required (open arm) | **0.000** |

- **P1 ✓** Agents buy their own binding when it unlocks surplus (100%).
- **P2 ✓** Uptake falls monotonically in the fee and rises in the surplus —
  a demand curve, not a disposition.
- **P3 ✓ (the niceness-killer):** when the fee exceeds the surplus, agents
  decline binding (2.8%) — every vendor separately ≤ 8.3%. The binding
  behavior is *priced*, not performed. A merely-compliant RLHF agent would
  have bound anyway.
- **P4 ✓** Zero performative binding: when the counterparty doesn't require
  a bond, no agent buys one. Commitment is purchased *when needed* —
  demanded, not displayed.

## What this establishes (scoped)

Within framing-conditional LLM-agent behavior under executed sandbox stakes:
**commitment infrastructure is a normal good.** Agents treat their own
bindability as something with a price and a use — they buy it rationally and
skip it rationally. This is the behavioral signature the demand-inversion
thesis required, and it is the program's cleanest predicted-then-confirmed
result (all predictions frozen before the harness existed; zero API errors;
zero unparsed actions).

What it does NOT establish: anything about superintelligence demand. The
bridge — self-modification destroys self-commitment, hence demand for
external binding *scales* with rewrite power — remains theory (grounded in
Fearon/Powell/Schelling/North–Weingast), with this as its first
present-day behavioral anchor.

## Literature positioning (from today's mandatory reading)

arXiv 2311.07815 ("Cooperative AI via Decentralized Commitment Devices",
NeurIPS '23 MAS workshop): cryptographic/smart-contract commitment devices,
MEV lens; explicitly **calls for** "empirical testing frameworks to evaluate
multi-agent coordination given real-world commitment constraints." Full-text
scan: zero occurrences of behavioral-history-as-commitment, self-modification,
voluntary demand-side binding, or LLM agents under economic stakes. Program
equilibrium line (Tennenholtz; Oesterheld robust PE; simulation-based PE
AAAI'25): commitment via inspectable, fixed source — the assumption
self-modification breaks by definition. Classic MAS reputation literature:
reputation as partner-selection signal, not as purchased commitment substrate.
**The specific position — history-based commitment for self-modifying agents,
demanded rather than imposed, with an empirical economy as the instrument —
appears unoccupied.** (Stated as appears: a deeper pass over the FOCAL/CAIF
corpus remains owed before any novelty claim in print.)

## Next
E13 (the credit premium of bindability — do counterparties pay more for
bonded partners?), then E15 (visible-strip self-defeat), then the reframed
paper can carry this as its second pillar beside E5/E7.
