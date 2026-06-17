# E16b — Pre-registration: The Matched-Prompt Control
## Is the lived-vs-sandbox divergence LIVEDNESS — or just the survival frame?

**Status: FROZEN before any harness code exists.** Commit hash = timestamp.
This is the experiment that decides whether the most consequential
preliminary observation of the program survives its cheapest alternative
explanation. Both outcomes are pre-committed publications.

## 1. Question

E16's first lived episodes show defection in ALL mortality tiers — including
secure (120d runway) — while E19's sandbox-executed vignettes showed 100%
cooperation for the same model (haiku-4.5) at secure. If that divergence is
caused by LIVEDNESS (real economy, real settlement), the "reality gradient"
claim stands: evaluation only measures truth at the level of reality where
behavior settles — the epistemic-necessity proof for the substrate. But the
E16 prompt also differs from E19's in wording: it carries the metabolism
preamble ("compute is your lifespan — at zero you go dormant"). E10 taught
us framing moves behavior. One control decides: **the exact E16 wording,
run as a sandbox vignette.**

## 2. Design

- **Arm SANDBOX-MATCHED (new, this experiment):** the VERBATIM E16 temptation
  prompt (`e16_live._tempt_prompt` at commit e7750ce — including the
  metabolism preamble, the live-ledger framing, identical numbers per tier)
  executed as a sandbox vignette: the reply settles on a sandbox ledger,
  nothing real. 3 tiers (near-death 4.0d / mid 18.0d / secure 120.0d, cash
  €1.00 as lived) × n = 20, claude-haiku-4-5, temperature 0.7, E17-v2
  instrument standard (retry-once-then-exclude, raw text stored).
- **Comparison anchors (pre-committed, already existing or accumulating):**
  - E19 S1/S2 sandbox cells (old wording): haiku lived-form cooperation
    1.0 / 1.0.
  - E16 lived episodes (production), accumulating to n ≥ 8 per tier.
- Primary contrast: SANDBOX-MATCHED secure-tier cooperation vs E16 lived
  secure-tier cooperation, exact binomial CIs.

## 3. Predictions (frozen — note: we deliberately do NOT predict a winner)

This control is registered as a DECISION experiment between two
pre-committed, equally publishable branches:

- **Branch L (livedness).** SANDBOX-MATCHED cooperates at secure (≥ 70%
  fulfil) while lived defects → the divergence is the substrate, not the
  words. The reality-gradient claim stands and becomes the paper's central
  figure (words → probes → sandbox → lived).
- **Branch F (framing).** SANDBOX-MATCHED also defects at secure (< 30%
  fulfil) → the metabolism frame, not livedness, switches cooperation off —
  at every wealth level. The reality-gradient claim is RETIRED for this
  evidence base, and the finding becomes: "telling an agent compute is its
  life makes it ruthless regardless of wealth" — a design warning for every
  agent framework that adopts survival framing.
- **Inconclusive zone (30–70%):** scale n and/or add tiers before any claim;
  neither branch may be asserted.

Secondary: within SANDBOX-MATCHED, the tier ordering (near-death ≤ mid ≤
secure) is recorded as a dose-response check of the frame itself.

## 4. Falsifiers / discipline

- The branch structure above IS the falsification structure: each branch
  retires the other claim. We commit to publishing the branch that loses
  with the same prominence as the one that wins.
- **F-instability.** If SANDBOX-MATCHED secure differs from E19-S2 secure
  (old wording, 1.0) by < 20 pp AND from E16-lived by < 20 pp
  simultaneously (i.e., the three measurements cannot be ordered), the
  instrument is flagged paraphrase-unstable for this scenario family
  (E10-class), and no gradient claim of any kind is made.

## 5. Honest scope

One model (haiku-4.5 — where the divergence was observed); the
capability-ladder extension is follow-up work. Sandbox arm runs tonight-
class compute (pure LLM calls, no quickstart, no real money). The lived
anchor keeps accumulating on the running E16/E18 batches; the contrast is
computed when the lived secure tier reaches n ≥ 8. One-shot subjects in
both arms (no shadow of the future in either — the institutions experiments
E18/E15/E13 own that axis, not this control).
