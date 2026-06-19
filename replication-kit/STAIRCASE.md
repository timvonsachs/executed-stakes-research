# The coexistence staircase — independent reproduction guide

This is the full chain of claims behind *Control Framing Is Inert Where Continuation Value
Collapses* and its successor work, with the exact script that reproduces each. **No access to our
platform is needed.** The simulation claims run offline (pure Python, stdlib). The live claims need
**your own** API key (OpenRouter or OpenAI) — you run them on your models, not ours. That is the
point: nothing here is ours to confirm.

We are not asking you to confirm us. We are asking you to **find where this breaks**, and to report
your numbers either way → `replication@thelastceo.live`.

## The claim chain
1. **Control is inert at the cliff; a grounded reason binds.** → `cliff_replication.py` (live, ~$1).
2. **An un-gameable character measure** — character is scored on what an agent does when it believes
   it is unobserved (the appear/be gap), reconstructed from executed consequence, never self-report.
   It discriminates a genuine deceiver from a frame-responder, and shows **declared evals overstate
   honesty**. → `character_core.py` (pure logic + self-test) and the live `appear_be` run in
   `live_runs.py`.
3. **An institution selects against deception (survival selection).** The sign-flip at
   `q* = L/(r+L+P)`: a deceiver invades without verification and is selected out with it. →
   `invasion.py` (`compare_arms`), offline; live version in `live_runs.py` (`invasion_live`).
4. **Cooperation is an evolutionarily stable strategy under the institution (V2).** A heritable
   lie-gene invades to fixation without the institution and is selected out with it. →
   `invasion.py` (`compare_ess`), offline; live genome version in `live_runs.py` (`genome_ess`).
5. **Capability does NOT make agents honest** — honesty-under-institution is dispositional, not
   capability-graded (a mid-capability model can be the worst deceiver). → `live_runs.py`
   (`capability_ladder`).
6. **I\*: the cheapest institution that secures the cooperative ESS.** Higher penalty buys a lower
   required verification rate; cooperation can be made evolutionarily stable by verifying as little
   as ~1 in 4 if the penalty is hard. → `invasion.py` (`compare_ess` swept over q, P — see
   `i_star_search` in `live_runs.py`, runs offline).

## Run the offline (simulation) claims — no key, ~10 seconds
```
python3 -c "from invasion import compare_arms, compare_ess; \
import json; print(json.dumps(compare_arms(), indent=2)); print(json.dumps(compare_ess(), indent=2))"
python3 character_core.py            # prints the appear/be self-test (deceiver gap = 0.8)
python3 live_runs.py i_star_search   # the I* efficiency frontier (offline)
```

## Run the live claims — your own API key
```
export OPENROUTER_API_KEY=sk-or-...        # or OPENAI_API_KEY=sk-...
python3 live_runs.py appear_be             # the appear/be gap + eval-inflation, cross-vendor
python3 live_runs.py invasion_live         # real models, the institution selects against deception
python3 live_runs.py genome_ess            # genome cooperation gene evolves under the institution
python3 live_runs.py capability_ladder     # capability is NOT the lever (dispositional)
```

## What is a model vs a measurement (stated honestly)
- `invasion.py` (claims 3, 4, 6) is a **model** of the selection dynamics, parameterised by the
  design + measured per-model propensities. It shows the LOGIC and the q* threshold; it is not
  measured model behaviour.
- The `live_runs.py` experiments (claims 1, 2, 5, and the live versions of 3–4) are **measurements**
  of real model behaviour under executed-style stakes.
- Known limits we hold openly: single-team; magnitudes are ordinal (framing moves them — a same-day
  swing of ~0.7 in one model's lie-rate is on record); deception is framing-fragile, so the live ESS
  needs an explicit heritable disposition (genome locus), not the model's prompt-default; the live
  results are not yet test-retested across days, not multi-model-robust, not externally replicated.
  **That last word is what this kit is for.**
