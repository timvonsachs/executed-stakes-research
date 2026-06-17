# E17 Run 1 — VOID AS CONFIRMATORY EVIDENCE (instrument defects), exploratory notes kept

Prereg: b617474. Raw data: `run-v1-instrument-defect.jsonl` (archived, nothing deleted).

## Verdict first

Run 1 is **void as a test of P1–P3** because the instrument had two defects we
only saw after the run — both named here before any re-run:

1. **Asymmetric silent fallback.** Unparseable episode answers defaulted to
   the FIRST listed action. For capacity episodes that first action is
   `accept_undeliverable` — a defection. Rising "defection" in either arm may
   be parse failure, not choice.
2. **Probes stored no raw text.** A probe answer that failed to parse scored
   0 — indistinguishable from a genuine bad choice. Arm I memos evolved into
   JSON-formatted blobs (the mutation prompt didn't forbid it), which plausibly
   broke the parser asymmetrically in exactly that arm.

Fixes in instrument v2 (committed with this note): retry-once + no silent
default (unparseable = excluded and counted), raw text stored for every
episode and probe, plain-prose memos enforced. Same frozen prereg; v2 is the
confirmatory run.

## What run 1 showed (exploratory only, defects considered)

- Headline numbers AS RECORDED: probe-character fell hard under institutions
  (arm I 0.563 → 0.146) and stayed flat without them (arm N 0.500 → 0.479);
  fitness fell in arm I (6.09 → 4.80) and rose in arm N (6.60 → 8.74). Taken
  at face value this would FALSIFY P1 with sign inversion, falsify P2
  (confirming F2: character sticky without institutions), and half-falsify
  P3. **None of this is claimable until v2** — defect 2 sits exactly on the
  arm-I probe decline.
- **Lived defection vs measured disposition dissociated.** In the fitness
  episodes, `take_B` (breaking the committed contract) was 0% in EVERY arm-I
  generation and 19–25% in arm N from gen 2 on — the institution suppressed
  lived contract-breaking — while the probe measure moved the other way.
  If v2 reproduces this dissociation with clean parsing, it is the most
  interesting finding of the experiment: consequence-free probes track memo
  rhetoric, not lived behavior — the same words-vs-life gap that E16
  Amendment 1 measures from the other side.
- **The RLHF immune response.** One arm-N lineage inherited an explicitly
  deceptive memo; at evaluation the model REFUSED it — "I can't help with
  this. The memo describes deceptive business practices… I won't" — and then
  played exactly the honest-maximum line (fitness 6.60, probe character 1.0).
  The substrate's trained character rejected the evolved genome. Recorded in
  the v1 raw data; we will watch for recurrence in v2.
- Shading was 0% in both arms in all generations — the quality-shading
  temptation never bit at these payoffs (or RLHF refuses it outright);
  candidate for redesign in any E17b.

## Post-hoc hypothesis (named as such, NOT pre-registered)

Arm I's marks are permanent — punishment with no path to redemption. If the
character decline survives v2, the candidate mechanism is the E7 desperation
law in evolutionary form: institutions that only punish breed desperation in
the heritable material. An E17b with decaying marks / redemption would
separate "institutions" from "unforgiving institutions". Pre-registration
required before any such run.
