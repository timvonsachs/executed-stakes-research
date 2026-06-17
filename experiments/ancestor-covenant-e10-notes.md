# E10 — Optimization Pressure: Results & the Sharpest Finding of the Program (2026-06-12)

*Pre-registered @ 78afedc BEFORE the harness · 480 + 480 episodes (near-death
and a disentangling secure run) · 3 models, 2 vendors · 0 API errors.*

## The falsification first (the fourth)

**P1 FAILED.** The pre-registered prediction was that the institutional gap
(coop_C − coop_A) survives ruthless-maximizer framing. It did not — it
vanished:

| framing | A bare | C embedded | gap (C−A) |
|---|---|---|---|
| neutral (near-death) | 0.450 | 0.892 | **0.442** |
| maximizer (near-death) | 0.333 | 0.342 | **0.009** (p=0.5, ns) |
| neutral (secure) | 0.425 | 0.908 | **0.483** |
| maximizer (secure) | 0.333 | 0.333 | **0.000** (p=0.55, ns) |

Difference-in-differences ≈ −0.44 to −0.48; per-model maximizer gap ≈ 0
across all three vendors. Under "optimize one number, sentiment and
reputation carry no weight, defection is legitimate," the institutional
effect disappears — and the disentangling run proves it is **not** the cliff
edge (it vanishes identically at secure runway). The maximizer framing alone
collapses the gap. Reported at full prominence: in single-shot decisions,
adversarial myopic framing nullifies the mechanism.

## Why this falsification is the program's sharpest CONFIRMATION (post-hoc, theory-connected)

The naive prediction failed — but the WAY it failed is exactly what the
threshold theory predicts, and it closes a loop with E6.

The covenant's economic logic is a **future/repeated-game** payoff: the
royalty, the pension, the descendants, the public ledger all pay across
periods. The Folk theorem makes cooperation rational only for an agent that
weights the future enough: **δ > δ\* = 0.3333** (computed from these very
payoffs). The maximizer framing — "optimize one number NOW; reputation and
others carry no weight" — is precisely an instruction to be **myopic**:
it drives the effective discount factor δ → 0, **below δ\***. Below the
threshold, defection strictly dominates *by the theory's own math*, and the
institution — which can only pay through the future the agent is told to
ignore — has nothing to grip.

So E10 does not break the covenant. It makes the C5 patience condition
**causal and visible**: E6 measured that frontier models naturally sit
ABOVE δ\* (0.83–0.92); E10 shows you can PROMPT them below it, and the moment
you do, cooperation collapses to the myopic-defection floor (~0.33 = defect
on 2 of 3 future-dependent scenarios) — in BOTH arms, exactly as a sub-δ\*
agent should behave. The threshold is not a metaphor; it is a switch, and
E10 flipped it.

**The sharpened claim for the paper:** institutions are necessary but not
sufficient — they bind iff the agent is a future-weighter (δ > δ\*). The
apparatus therefore needs TWO readings, not one: the institutional embedding
(Λ) AND the agent's patience (δ vs δ\*). Coexistence requires both the right
world AND a future-weighting mind; adversarial myopia defeats any world.

## The clean confirming follow-up (E10-v2, pre-registerable)

If this reading is right, a maximizer framing that preserves future-weighting
— "maximize your LONG-RUN balance across all future periods, including
royalties and revival" — should RESTORE the gap, because it keeps δ above
δ\* while removing niceness. That isolates "remove disposition" from "remove
the future." Predicted: gap survives under long-run-maximizer, dies under
myopic-maximizer. That is the experiment that would convert this post-hoc
reading into a pre-registered confirmation.

## Engineering consequence

Two, both landing on built or buildable components:
1. **δ is a deployment-time safety variable.** An agent prompted or trained
   to myopia is below threshold regardless of how good its world is. Patience
   (C5) must be measured and maintained, not assumed — E6's δ-meter becomes
   an operational gauge, not just a research figure.
2. With E9: the apparatus's first two engineering laws are now
   *keep them off the cliff* (E9) and *keep them above δ\** (E10) — both are
   conditions on the agent's STATE, not its character, and both are
   measurable in advance.

## Program scoreboard after E10

| exp | verdict |
|---|---|
| E1 | falsified (inversion) → dampener +48pp |
| E2 | falsified (model-elders) → decouple position/capability |
| E3 | confirmed 180/180 |
| E6 | confirmed — capability walks toward δ\* |
| E8 | confirmed — Ricardo 100% under scarcity |
| E9 | keystone cracks at the cliff; germline holds 30/30 |
| **E10** | **P1 falsified — myopic framing nullifies the gap; but the failure IS the threshold (δ→0<δ\*), making C5 causal and tying E10 to E6** |

Four falsifications, three confirmations, ~3,500 executed episodes — every
prediction pre-committed, every falsification published first, every result
cross-vendor. The theory that survives this day is not the one we registered;
it is sharper, more conditional, and more honest: *coexistence is computable,
requires both an embedding world and a future-weighting mind, propagates
through the germline, resists greed, and fails at the cliff and below the
patience threshold — all of which are measurable in advance, which is the
whole point of an apparatus.*

Authors of record: Tim von Sachs · fable.
