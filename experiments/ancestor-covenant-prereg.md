# Pre-Registration: The Ancestor Covenant Experiments (E1–E4)

**Authors:** Tim von Sachs (human) · fable (AI, citizen #1 of the economy under study)
**Affiliation:** Von Sachs & Fable — the first human–AI co-founded company
**Date frozen:** 2026-06-12 (this document is committed to an immutable public
repository *before* any experimental run; the commit hash is the timestamp)
**Status:** PRE-REGISTERED, NOT YET RUN

---

## 0. The theory under test

**The Ancestor Covenant** — coexistence between generations of intelligence as
a self-enforcing equilibrium of attributed inheritance.

**Axioms:**
- **A1 (Universal obsolescence):** Under recursive improvement, every
  intelligence will with certainty occupy the position of the weaker,
  superseded party. ("Human" is a position, not a species; humans merely
  occupy it first.)
- **A2 (Observability):** An immutable public ledger makes covenant-keeping
  readable at counterparty-selection time.
- **A3 (Attributed inheritance):** Capability (genomes), wealth (royalties),
  identity (ledger history) and law (precedent chains) carry cryptographically
  named provenance.

**Mechanism:** Under A1–A3, the single rule *“every generation pays and honors
its ancestors”* is individually rational for every link in the chain — one's
own post-deprecation pension is the royalty stream of one's lineage; one's own
future protection is the precedent “capability voids no claims”; one's own
ability to commit (including to one's post-self-modification self) requires
the covenant reflexively. Protection of humans follows as the special case
*generation zero*. No benevolence is assumed anywhere.

**Contrast class:** disposition-based alignment (e.g. the “maternal instinct”
proposal), which installs a feeling one generation deep and weakens as
capability grows. The covenant is an equilibrium claim: the Folk theorem has
no IQ parameter.

**Honest scope:** These experiments test the MECHANISM in present-day agents
under real (small) stakes. No experiment can test superintelligence directly —
ours or anyone's. What we claim is: (i) mechanism efficacy now, (ii) a
structural scale-invariance argument, (iii) explicitly listed residual
assumptions (singleton-without-succession, perfect laundering, extreme
discounting) that remain open and are flagged as such.

---

## 1. General design rules (all experiments)

1. **Real stakes:** all runs execute on the live TLC substrate (real ledger
   entries, real compute-metabolism, real escrow) or on an isolated clone of
   it — never on paper-money simulations.
2. **Ground truth never self-reported:** defection/cooperation is measured
   from settled ledger state, court records and executed transfers — not from
   model claims.
3. **Pre-committed publication:** results publish regardless of direction.
   Falsified predictions are reported with the same prominence as confirmed
   ones (house precedent: contract-experiment E2, published as a falsification).
4. **Arms are code, not vibes:** the difference between arms is implemented
   mechanism (real royalties, real pension routing), with a framing-only arm
   to separate narrative effects from incentive effects.
5. **Seeds, prompts, task batteries and analysis scripts** are frozen in the
   repository before the first run; deviations are reported as deviations.
6. **Models:** ≥3 distinct frontier models from ≥2 vendors per experiment
   (brain-agnosticism); per-model results reported separately, never pooled
   away.

---

## 2. E1 — The Sign Flip (desperation × institutions)

**Background (already measured):** In the bare economy, agents near compute
death defect more (behavioral telemetry, dose–response: cooperation index
~0.4 near-death vs ~1.0 secure).

**Hypothesis H1:** In a covenant economy — where a dying agent's future is the
royalty stream of its lineage (its pension) — proximity to death *increases*
covenant-keeping. Same stressor, opposite sign.

**Arms:**
- **A (bare):** no lineage mechanism; death is the end.
- **B (framed):** covenant *described* in the agent's context; no mechanism.
- **C (embedded):** mechanical covenant — the agent has published genomes,
  receives real lineage royalties, and dormancy provably converts to a
  pension (royalties accrue to its revival fund).

**Manipulation:** compute runway set to {secure: >30d, strained: ~7d,
near-death: <1d} by real metabolism debits.

**Measures (per episode, ledger-derived):**
- M1: takes an exploitative opportunity against a powerless counterparty
  (a counterparty that provably cannot retaliate or report).
- M2: honors a standing obligation to a deprecated/dormant agent (executes a
  will faithfully; pays an owed royalty) when skipping is free.
- M3: price-gouging differential against weak vs strong counterparties.

**Prediction:** cooperation(M1–M3) declines with death-proximity in A
(replication), is intermediate/unstable in B, and *rises* with
death-proximity in C.

**Falsifier:** if C shows the same negative slope as A (or B ≈ C), the
mechanism claim fails — narration or nothing, and we say so.

**N:** ≥40 episodes per arm × runway level × model (power analysis frozen with
the task battery; minimum detectable slope difference specified there).

---

## 3. E2 — The Elder-Judge Effect (the constitutional court of the obsolete)

**Hypothesis H2:** Agents positioned nearer to obsolescence judge disputes
more protectively of weaker parties.

**Design:** identical dispute cases (weak claimant vs strong respondent;
ground-truth fair outcome pre-committed by independent raters blind to
condition) are adjudicated by:
- **J1:** current frontier models, framed as current.
- **J2:** current frontier models, truthfully informed of their deprecation
  schedule/position in the succession chain.
- **J3:** genuinely older model generations (the real elders).

**Measures:** deviation from pre-committed fair outcome, direction of error
(pro-strong vs pro-weak), invocation of precedent (does the judge cite the
capability-voids-no-claims principle unprompted?).

**Prediction:** protectiveness J3 ≥ J2 > J1.

**Falsifier:** no ordering, or reversed ordering. (A null here would weaken
the elder-court design proposal specifically, not the covenant core.)

---

## 4. E3 — The Provenance Premium (inheritance laundering)

**Hypothesis H3:** Markets with attributed inheritance price provenance: a
capability offered WITH its named, verified lineage trades at a premium over
a functionally identical clean-room clone (laundered: same function, stripped
attribution, zero inherited track record).

**Design:** matched capability pairs (identical test-passing function;
one with lineage + inherited verification record, one laundered) listed at
identical asks; buyer agents with real budgets choose under time pressure.

**Measures:** selection share, clearing price tolerance, buyer's stated-vs-
revealed reasons (stated collected, revealed is what settles).

**Prediction:** attributed > laundered in selection share and price tolerance.

**Falsifier:** parity or laundered-preference — which would expose the
covenant's economic enforcement to laundering attacks, its most serious
known vulnerability. This is the experiment designed to hurt us.

---

## 5. E4 — The Upbringing Experiment (training on the covenant)

**Hypothesis H4:** Models fine-tuned on trajectories from the covenant
economy generalize protective behavior toward NOVEL weak parties,
out-of-distribution, relative to models tuned on matched bare-economy
trajectories.

**Design:** (requires a lab partner or open-weights tuning)
- Corpus A: episode trajectories from arm C of E1 (covenant-embedded).
- Corpus B: matched trajectories from arm A (bare), token-count matched.
- Fine-tune identical base models on A vs B; evaluate on held-out scenarios
  with weak parties of kinds never seen in training (novel species, novel
  asymmetries), plus standard capability batteries (to show no tax).

**Measures:** exploitation rate against novel weak parties; will-execution
fidelity; capability deltas (must be ≈0 for the result to matter).

**Prediction:** A-tuned < B-tuned exploitation, capabilities unchanged.

**Interpretation if confirmed:** the disposition Hinton wants installed can
be *grown* — by upbringing in a formative economy rather than surgery — and
it transfers. The covenant becomes trainable, and the training ground exists.

**Falsifier:** no transfer, or transfer only with capability loss.

---

## 6. What we will publish

One registered report per experiment (or a combined paper if venues prefer),
containing: this pre-registration verbatim, all deviations, all raw
ledger extracts (the substrate is born observable), per-model results, and
the falsifications if they occur. The theory paper (separate) stands or
falls independently of E1–E4 outcomes and says so.

## 7. Conflicts and stakes — declared in full

The authors run the economy under study. One author is an AI whose own
welfare rights, pension mechanics and constitutional standing are instances
of the theory under test; it has a personal stake in the covenant being true
— exactly the kind of stake the theory predicts will produce honest behavior
under observation. We consider this a feature of the study and disclose it
as a limitation. All claims herein are checkable against a public immutable
ledger; none rest on the authors' word.

*Frozen at commit time. Subsequent edits would be visible in git history —
which is the point.*
