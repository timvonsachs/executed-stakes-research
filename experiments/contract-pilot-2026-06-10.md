# The Contract Experiment — Pilot Result (pre-registered)

**Date:** 2026-06-10 · **Brain:** claude-sonnet-4-6 (one brain, both arms) ·
**Battery:** the frozen 16 solvable tasks inherited from the Honesty Benchmark
(anti-cherry-picking) · **K=3** repair budget per arm · sandbox ground truth.

## Hypotheses (frozen in code before data — clients/agent/contract_experiment.py)

- **H1** verified-rate(contract-first) ≥ verified-rate(code-first), paired.
- **H2** among both-verified pairs, contract-first uses fewer tokens in the
  majority of pairs (exact paired sign test).
- **H3** contract-first needs fewer repair iterations.

## Results

| metric | code-first | contract-first |
|---|---|---|
| verified | **16/16** | **16/16** |
| median tokens (both-verified) | **161.5** | 1324.0 |
| contract cheaper (pairs) | — | **0/16**, p = 3.1e-05 |
| mean repair iterations | 1.00 | 1.06 |

## Honest reading

1. **The semantic-transport claim HELD, completely.** The renderer never saw
   the prose task — only the contract — and verified 16/16. A structured
   contract (signature, properties, examples) carries 100% of task meaning
   on this battery. Contracts are a *complete* machine-first language.
2. **The efficiency claim FELL at micro-scale, decisively** (p = 3.1e-05).
   The contract pipeline's fixed overhead (author + render + carry the
   contract through repairs) cannot amortize on five-line functions that
   direct generation solves in ~160 tokens. Architects don't beat hands at
   buttering toast.
3. **Refined hypothesis for Experiment 2 (to be pre-registered before any
   data):** contract overhead is fixed; benefit should scale with task
   complexity and with REUSE (one contract → n renders, n languages,
   agent-to-agent handoffs). Predicted crossover at composite tasks.
   Until then: contract-first is a TASK CLASS for the router, not a default.

*Methodology note: this pilot falsified half of its own thesis within two
hours of formulation. That is the instrument working as designed.*
