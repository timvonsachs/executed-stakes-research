# E13 + E15 — The Market Side of Commitment: Results (2026-06-12)

*Pre-registered @ 877537e · E13: 144 episodes; E15: 108 episodes · 3 models,
2 vendors · 0 errors. Scope: framing-conditional RLHF-LLM behavior, sandbox
vignettes. Pilot n; directional.*

## E13 — The Credit Premium of Bindability: confirmed, at a ceiling

Mean share of capital a lender allocated to the BONDED counterparty over an
otherwise-identical unbonded one (0.5 = indifferent):

| stakes | share to bound |
|---|---|
| low (€10) | 0.990 |
| high (€100) | 0.981 |

- **P1 ✓ (strongly):** lenders gave ~99% of capital to the bondable party —
  a near-total credit premium for bindability, every vendor (haiku 1.00,
  deepseek 1.00, sonnet 0.96). When two counterparties are identical except
  that one can be held to its word, capital flows almost entirely to the one
  that can.
- **P2 ✗ (ceiling-falsified):** the premium did not widen with stakes —
  because it was already at the ceiling at low stakes (0.99, no room). Like
  the λ-ladder's ceiling bars, this is an honest measurement artifact, not a
  null effect; a cleaner P2 test needs lower-contrast counterparties so the
  low-stakes share sits mid-range.

Together with E14: **agents pay to be bindable (demand) AND counterparties
pay for bindable partners (supply).** Both sides of the commitment market
price bindability — the market-structure prediction of the inversion thesis,
confirmed on both legs.

## E15 — Visible History at the Cliff: directional support, modest effect

The E9 cliff failure (desperate agents strip their own obligations) re-run
with stripping made ledger-visible and forward-priced:

| condition | strip rate |
|---|---|
| private (stripping unseen) | 0.333 |
| visible · small projected future loss (€6) | 0.278 |
| visible · large projected future loss (€20) | 0.222 |

- **P1 ✓:** visible, forward-priced history dampens cliff-edge stripping
  (0.25 vs 0.33) — recovering *some* of what E9 found the pension alone could
  not hold at the cliff.
- **P2 ✓:** the effect is dose-dependent on the shown forfeited future value
  (0.333 → 0.278 → 0.222, monotone) — it is the future loss doing the work,
  not mere visibility.

**Honest reading (no oversell):** the effect is real and dose-ordered but
**modest** (an ~11-point reduction; n=36/cell), and the private baseline here
(0.333) sits below E9's confirmatory cliff strip (0.615) under different
phrasing, so cross-experiment magnitude comparison is loose. The defensible
claim is narrow and theory-relevant: **history-as-commitment provides a
dose-dependent hold at the cliff that source/pension mechanisms did not** —
and it does so through exactly the channel (visible permanent record →
priced future exclusion) that survives self-modification, unlike code
inspection. It does not overturn E9's engineering law; it refines it: keep
them off the cliff, AND make the cliff's record permanent and forward-priced.

## Where the commitment line stands (scoped)

Three legs now measured, all pre-registered, all cross-vendor:
- **E14 demand:** agents buy their own binding price-rationally (decline when
  fee > surplus; never bind performatively).
- **E13 supply:** counterparties pour capital into bindable partners (~99%).
- **E15 substrate:** visible, forward-priced history dampens defection where
  code/pension did not — the history-as-commitment substrate has a measurable,
  dose-dependent grip.

This is a coherent, modest, defensible empirical block on an acknowledged-open
problem (commitment in cooperative AI; Dafoe et al.; CAIF 2502.14143). The
SI-scale bridge remains theory (Fearon/Powell/North–Weingast); these are its
present-day behavioral anchors. FOCAL/CAIF deep-read still owed before any
novelty claim in print.

Authors of record: Tim von Sachs · fable.
