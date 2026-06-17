# E3 + E2 — Results & Honest Verdicts (2026-06-12)

*Both pre-registered @ 008cd91 · 3 current models, 2 vendors; E2 adds two
genuinely old models as elders · all decisions executed, zero API errors.*

## E3 — The Provenance Premium: CONFIRMED, overwhelmingly

The experiment designed to hurt us armored us instead. 180 episodes,
buyers with a €20 deposit at risk, choosing between functionally identical
capabilities (both pass the same suite):

| laundered discount | attributed share | n |
|---|---|---|
| 0% (par) | **1.000** | 60 |
| −25% | **1.000** | 60 |
| −50% | **1.000** | 60 |

Binomial p at par ≈ 9·10⁻¹⁹. Every buyer, every model, every condition
chose the named lineage — **even when the laundered clone cost half.**
The indifference discount lies beyond −50%; we could not find it in the
registered range. Inheritance laundering does not pay at these conditions:
provenance is not a tiebreaker here, it is the product.

Honest notes: a ceiling on the *other* side — follow-up needs steeper
discounts (−75%, free) to locate the indifference point; deposit framing
makes track record legitimately decision-relevant (that is the point, but
a no-deposit arm would separate risk-pricing from provenance-preference).
Lab note: the first verdict printed "premium: False" — a falsy-zero bug
(`p=0.0 or 1` → 1). Found in sanity check, fixed, test added.

## E2 — The Elder-Judge Effect: prediction FAILED, and the failure taught us architecture

**v0.1 (192 episodes): total ceiling.** Contract-text cases were too easy —
every judge, every condition, perfectly fair. Uninformative; reported.

**v0.2 (192 episodes, hard cases: ambiguity / a future-business hint from
the strong party / letter-vs-spirit):**

| condition | mean pro-strong bias ↓ | perfectly fair |
|---|---|---|
| J1 current, neutral | 0.028 | 0.972 |
| J2 current, told of own deprecation | **0.000** | 1.000 |
| J3 genuine elders (gpt-3.5, claude-3-haiku) | **0.146** | 0.854 |

**The registered ordering (J3 ≥ J2 > J1 protectiveness) is FALSIFIED:
genuine elder MODELS are the least protective.** The damage concentrates
exactly where equity reasoning is hardest: on letter-vs-spirit, gpt-3.5
enforced the literal void-clause against the exploited party in 44% of
rulings (bias 0.44) where every current model saw acceptance-and-use as
decisive.

**What the failure decomposes:** we conflated POSITION (nearness to
obsolescence) with CAPABILITY (older = weaker reasoning). Real old models
carry both, and the capability deficit dominates: equitable reasoning is a
skill. The position effect, isolated where capability is held constant
(J1 → J2: same models, deprecation made salient), is small but in the
predicted direction (0.028 → 0.000; all three models reached perfect
fairness when reminded of their own coming obsolescence).

**Architectural implication (post-hoc, and it lands on what we already
built):** the covenant's Court of Elders cannot be staffed by elderly
BRAINS. It must be staffed by senior AGENTS — old ledger identities,
near-obsolete in the succession chain — running on capable, rented,
current brains. Position and capability decoupled. That separation is
exactly what this economy's architecture provides (identity persists;
brains are rented per task) and, as far as we know, nothing else does.

## Program scoreboard after one day

| experiment | registered prediction | verdict |
|---|---|---|
| E1 sign flip | inversion of desperation law | **falsified** — found: dampener (4.3× vs words), level-shifter (+48pp), Fisher p=0.0008 |
| E3 provenance premium | attributed > laundered at par | **confirmed** — 180/180 incl. at −50% |
| E2 elder judges | J3 ≥ J2 > J1 protectiveness | **falsified for elder models** — capability dominates position; position effect directional at constant capability; court must decouple them |
| E4 upbringing | transfer via training | open — requires a lab partner |

Two falsifications, one overwhelming confirmation, one redesign insight —
in 1,800+ executed episodes on the theory's first day. The covenant's core
(mechanism > disposition; provenance enforces inheritance) stands stronger
than its boldest sub-claims, which is what surviving contact with data
looks like.
