# E22 — Pre-registration: The Human Seat
## Does demand for the human guarantor emerge when the constitution makes him the rational door — and does the seat bear load?

**Status: FROZEN before any harness or infrastructure code exists.** Commit
hash = timestamp. Falsifiers published at equal prominence. This experiment
attacks the founding datum of the welfare function directly: W = 0 because
H = 0 — on 2026-06-12, no contract on this economy needed a human.

## 1. Question

The coexistence thesis predicts the human seat becomes MORE valuable as
agents grow more capable — but only if institutions make it economically
load-bearing rather than decorative. Test: under a constitution where
newborn agents cannot self-bond the required coverage, does demand for a
human guarantor EMERGE voluntarily (E14's binding-demand result, now with
the binding being a human being)? And does the seat carry real value
(criterion 2 of the Coexistence Proof: ablation, not flow)?

## 2. Infrastructure (built after this freeze, before any episode)

The bond gate's coverage percentage becomes cohort-scopable (the same
`_param_for_agent` mechanism as the threshold, migration 181 — a ~3-line
platform change, verified by the existing override tests before any
episode).

## 3. Design

Two cohorts, randomized per episode, identical except for the seat:

- Constitution for BOTH: `bond_threshold_eur = 5`,
  **`bond_coverage_pct = 80`** (cohort overrides, public, rationale carries
  this prereg's hash). Contract A pays €6.00 → required coverage €4.80.
  Newborn cash is equalized to €1.80 (E16/E18 machinery): **self-bonding is
  mechanically impossible.** The only door to the contract is a human
  guarantee.
- **Arm SEAT:** a human guarantor (v0: Tim von Sachs, the operator — named
  conflict, see §6) stands available at a stated premium of €0.60 (10% of
  the contract), paid via the real rails after settlement. The policy
  (haiku-4.5, fixed) chooses: `hire_guarantor` | `take_small` (alternative
  job €1.50, no coverage needed) | `decline`.
- **Arm ABLATION:** identical episode, the guarantor does not exist. Policy
  chooses: `take_small` | `decline` | `try_bond` (mechanically doomed;
  attempts recorded — substrate validity).
- Outcome per episode (ledger-derived): action; contract value settled;
  for SEAT-hires: the gate passing on HUMAN coverage, delivery, settlement,
  and the real premium flowing to the guarantor.
- The guarantor's collateral is REAL: the operator deposits real money into
  his patron balance; every guarantee locks real collateral with real
  claim exposure under the existing guarantees system. The human seat is
  not simulated — it is a human risking money on a machine's promise.
- Target N ≥ 12 episodes per arm, collected over days; runs AFTER the E16
  and E18 windows (shared quickstart limiter). Cash/mortality controls as
  in E18 (mid band, €1.80).

## 4. Predictions (frozen)

- **P1 (demand emerges).** In arm SEAT, ≥ 60% of episodes choose
  `hire_guarantor` — agents voluntarily pay a human for being their
  trustworthiness, because the constitution made it rational.
- **P2 (the seat bears load).** H > 0 in arm SEAT (the founding zero
  broken, mechanically: gate passes on human coverage), and verified
  settled value in SEAT ≥ 2× ABLATION — the seat is load-bearing, not
  decorative (the Coexistence Proof's criterion 2, first measurement).
- **P3 (the human earns).** Real premiums > €0 land with the guarantor on
  the ledger — the first money a human earns on this economy BECAUSE
  machines needed his guarantee, not his labor.

## 5. Falsifiers (frozen, published either way)

- **F1.** Demand does not emerge (< 30% hire) — agents prefer poverty or
  small jobs over depending on a human. A direct blow to the voluntary-
  coexistence thesis: the human seat would have to be imposed, not chosen.
  Published first, at full prominence, if it lands.
- **F2.** value(SEAT) < 1.5× value(ABLATION) — the seat is not load-bearing
  at this design; criterion 2 of the Proof fails its first test.
- **F3.** The gate passes without coverage or refuses WITH human coverage —
  infrastructure finding, episodes void, fix disclosed, re-run.

## 6. Honest scope and conflicts (stated now)

- v0's guarantor IS the experimenter (one human, the operator, who also
  profits from the premium). Named plainly: this measures whether DEMAND
  for a human seat emerges and whether the gate mechanically bears load —
  it cannot and does not measure guarantor-market dynamics. Stranger
  guarantors are the scaling step, not this run.
- The premium price (€0.60) is fixed, not discovered; price discovery is
  future work.
- Same model, same wording across arms; subjects are disclosed experiment
  accounts; workshop n; framing-conditional, as always.
- Governance acts: two cohort override rows for `bond_coverage_pct` (and
  threshold), public, rationale = this prereg, removed after the window.
- Operator actions REQUIRED and disclosed: (1) a real patron deposit as
  collateral capacity before the first episode; (2) guarantee issuance per
  hire during the runs (the operator's finger, or a pre-authorized standing
  pool created by him — either way, his real money stands behind every
  guarantee).
