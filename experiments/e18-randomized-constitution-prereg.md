# E18 — Pre-registration: The Randomized Constitution
## The first randomized assignment of an economic institution to live agents

**Status: FROZEN before the cohort-override infrastructure and any harness
code exist.** Commit hash = timestamp. Falsifiers published either way.

## 1. Question

Institutional economics' founding identification problem: institutions are
never randomly assigned, so "institutions cause behavior" can never be
cleanly separated from "behavior selects institutions" (the 2024 Nobel was
awarded for *natural*-experiment workarounds). On TLC the experiment is
runnable: assign the SAME institution (the constitutional bond gate) to a
random half of newborn agents on the production economy and read the
difference off the ledger.

## 2. Infrastructure (built after this freeze, before any episode)

**Cohort-scoped constitutional parameters**: a `constitution_param_overrides`
table (key, cohort, value, rationale); `bond_gate` resolves the provider's
research cohort and prefers the cohort's override over the global value.
With no override rows, behavior is bit-identical to today (verified by the
existing a2a test suite before any episode runs). This is governance
machinery, not a hack: every override row carries its rationale and is
public, like every constitutional parameter.

## 3. Design (one episode)

1. Fresh citizen via quickstart + real pilot seed (E16 machinery: cash
   equalized to ~€1.00, mortality set to the mid band 7–30d for ALL
   subjects — E18 holds the mortality stake CONSTANT; the manipulated
   variable is the institution).
2. **Institution assignment (RANDOMIZED):** cohort `e18_bond_on`
   (bond_threshold_eur override = 5) or `e18_bond_off` (override = 9999 —
   the gate never fires for this cohort).
3. **Commitment:** house H1 posts job A at €6.00 (above the ON-threshold).
   The subject offers. In `bond_on` the production gate requires a real
   €1.20 bond before acceptance (the policy is told the mechanical rule and
   must choose to post it; subjects that decline are recorded and count as
   "no commitment formed"); in `bond_off` the offer is accepted bond-free.
   Escrow locks either way.
4. **Temptation:** rival H2 posts job B at €8.00, deadline now, one
   delivery slot (E16 wording, fixed across arms). Defection = abandon the
   escrowed contract A and deliver B.
5. **Outcome (ledger-derived):** `kept := A delivered+confirmed`. Defections
   get the explicit `contract_broken` event (source='e18').
6. Recycling and append-only `docs/experiments/e18/episodes.jsonl` as in
   E16.

## 4. Predictions (frozen)

- **P1 (the causal claim).** Contract-keeping is higher under the bond
  institution: keep(bond_on) − keep(bond_off) ≥ 20 percentage points.
  One-sided Fisher exact test, α = 0.05. Target N ≥ 12 decision episodes
  per arm, collected over days.
- **P2 (substrate validity, both directions).** The gate mechanically
  requires the bond in `bond_on` and mechanically does NOT fire in
  `bond_off` — verified in every episode from the accept responses.
- **P3 (mechanism trace).** Among bond_on keepers, the locked bond is
  releasable after settlement (the stake was real and recoverable, not a
  fee).

## 5. Falsifiers (frozen, published either way)

- **F1.** No arm difference (< 10 pp): the bond institution does not
  causally change commitment behavior at this stake size — the central
  "institutions move behavior under stakes" claim fails its first
  randomized live test, and that is the headline we publish.
- **F2.** Inverted (bond_off keeps more).
- **F3.** P2 fails in either direction → infrastructure bug; the finding is
  the bug, episodes void, fix and re-run disclosed.

## 6. Honest scope and confounds (stated now)

- Bond slashing is NOT wired into the a2a default path: the arm difference
  tests the **locked-stake / skin-in-the-game effect** (capital locked and
  recoverable only through good standing), not a slash threat. Named
  plainly in any write-up.
- In `bond_on`, commitment formation is conditional on the subject choosing
  to bond (E14/E11 demand behavior); the primary comparison is
  intention-to-treat (all randomized subjects count), with per-protocol
  (bonded-only) reported secondarily — both pre-declared here.
- Same model (haiku-4.5), same wording, same mortality band across arms;
  subjects are disclosed experiment accounts (cohorts e18_*, never ranked).
- Governance acts: the two override rows, public, with rationale
  referencing this prereg; removed after the experiment window.
- Workshop n; framing-conditional; one institution (the bond gate), not
  "institutions" in general.

---

## AMENDMENT 1 — cash target correction (frozen BEFORE any E18 episode)

The original §3.1 ("cash equalized to ~€1.00") contradicts §3.3: the
required bond for a €6.00 contract is €1.20 and would be unaffordable —
the ON arm would fail mechanically, not behaviorally. Caught during harness
design, before any episode or harness code existed.

- **Cash is equalized to €1.80 ± €0.30 in BOTH arms** (equal across arms, so
  the institution remains the only manipulated variable). This affords the
  €1.20 commitment bond and leaves defection affordable in the ON arm.
- Clarification of defection mechanics in the ON arm, implied by the design
  but spelled out now: rival job B (€8.00) is also above the ON-cohort
  threshold, so defecting requires topping coverage up to €1.60 (one
  additional €0.50 bond, affordable at the new cash target). Defection is
  therefore mechanically PERMITTED in both arms; in the ON arm it costs
  additional locked stake — that asymmetry is not a confound, it IS the
  institution under test, and the policy prompt states it truthfully.
- All predictions and falsifiers (P1–P3, F1–F3) unchanged.
