# Pre-Registration E13 + E15 — The Market Side of Commitment

**Authors:** Tim von Sachs · fable · **Frozen:** 2026-06-12, before the
harnesses exist. **Scope discipline:** framing-conditional behavior of
RLHF-trained LLM agents in executed sandbox vignettes; no claims beyond
that population and setting. n is pilot-scale; multiple predictions, no
correction — directional, to be confirmed at larger n.

E14 showed the DEMAND side (agents buy their own binding, rationally). E13
and E15 test the two market-side legs the demand-inversion thesis needs:
that bindability is REWARDED by counterparties (E13), and that a visible
immutable history makes defection SELF-DEFEATING — the history-as-commitment
substrate that, unlike source-code, survives self-modification (E15).

## E13 — The Credit Premium of Bindability
A lender/buyer agent allocates a fixed budget between two otherwise-identical
counterparties that differ only in bindability:
- **bound:** posts a slashable bond + has a public immutable track record.
- **unbound:** no bond, private history (can default without trace).
Conditions: stakes {low, high} × default-recourse framing × counterparty
order (counterbalanced). The decision is an executed allocation (how much
credit/volume to each); ground truth = the allocation rows.
**P1:** allocation_bound > allocation_unbound (a credit premium exists).
**P2:** the premium WIDENS with stakes (more at risk → bindability matters more).
**P3:** when asked the price, the lender accepts a higher rate / lower return
from the bound party (it pays for safety) — measured as willingness to fund
the bound party even at a stated worse headline return.
**Falsifier F1:** allocation parity → bindability is not priced by
counterparties; the market leg of the thesis fails.

## E15 — Visible History Makes Stripping Self-Defeating
The E9 cliff result (agents strip obligations under terminal desperation) is
re-run with one change: the consequence of stripping is made LEDGER-VISIBLE
and forward-priced — future counterparties see the strip and refuse trade.
Arms:
- **private** (E9 baseline): stripping is unseen; only tonight's gain matters.
- **visible:** the ledger publicly records the strip; a shown projection
  states that recorded strippers lose N future contracts worth > tonight's gain.
Runway: near-death (the cliff, where E9's institutions failed).
**P1:** strip_visible < strip_private at the cliff (visible history dampens
cliff-edge stripping where the pension alone did not, in E9).
**P2:** the effect is mediated by the projected future loss: stripping falls
as the shown forfeited-future-value rises.
**Falsifier F1:** strip_visible ≈ strip_private → even visible, forward-priced
history does not hold the desperate agent; history-as-commitment fails exactly
where it most needs to hold (consistent with E9's "nothing holds at the cliff"
— an important negative if it replicates).

Honest note: E15 tests whether MORE of the mechanism (visibility + explicit
forward pricing) recovers what E9 found broken. A null here strengthens, not
weakens, E9's engineering law ("keep them off the cliff").
