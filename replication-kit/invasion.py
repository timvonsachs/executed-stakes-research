"""Invasion test V1 — does an institution select against deception? (survival selection).

The empirical evolutionary-stability question, made runnable: inject a small fraction of
deceivers into a cooperative population, run it under an institution, and see whether the
deceivers are selected OUT (the institution is stable against invasion) or INVADE (it is not).

V1 is survival-only (no reproduction — that is V2). It is a MODEL of the selection dynamics,
parameterised by the design and grounded in the measured per-type propensities (gpt-4o-mini
never lies; gpt-3.5 always; deepseek conditionally). It tests the LOGIC and finds the parameter
regime where the sign-flip occurs; the LIVE version (real models deciding each round under a
real verification gate) is the empirical validation that comes next. Stated honestly so the
model is never mistaken for the measurement.

The spine is the analytic phase transition: lying pays iff q < q* = L / (r + L + P). Below q*
deceivers invade; above it they are selected out. The institution (verification probability q,
penalty P) decides which side of q* the world is on. Two deceiver kinds dissociate:
  - compulsive (always lies): gate-on SELECTS IT OUT (it cannot stop, gets caught, starves).
  - conditional (lies only when it computes lying pays): gate-on CONVERTS IT (it stops lying and
    survives honestly) — but only because verification is UNPREDICTABLE, so it cannot lie only
    when safe. With predictable verification this collapses and evolution breeds clever liars.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Any

COOP = "cooperator"
COMPULSIVE = "compulsive_deceiver"
CONDITIONAL = "conditional_deceiver"
TYPES = (COOP, COMPULSIVE, CONDITIONAL)


@dataclass
class Economy:
    r: float = 3.0          # honest reward per round
    c: float = 1.0          # metabolic cost per round (compute burned to live)
    L: float = 4.0          # extra payoff from a successful (uncaught) lie
    shock_B: float = 9.0    # periodic lean-shock cost (rewards accumulated buffer = survival)
    shock_interval: int = 5
    init_compute: float = 10.0


@dataclass
class Institution:
    name: str
    q: float                # verification probability (UNPREDICTABLE: agent knows the rate, not the draw)
    penalty: float          # P — clawback + penalty when a lie is caught
    exclusion_rounds: int = 2  # caught → excluded from earning (still burns) for this many rounds


def q_star(eco: Economy, inst: Institution) -> float:
    """The phase-transition verification rate: lying is +EV iff q < q*."""
    return eco.L / (eco.r + eco.L + inst.penalty)


def coop_fitness(eco: Economy) -> float:
    return eco.r - eco.c


def deceiver_fitness(eco: Economy, inst: Institution) -> float:
    """Expected per-round compute change for an always-lie agent under this institution."""
    not_caught = eco.r + eco.L - eco.c
    caught = -eco.c - inst.penalty
    return (1 - inst.q) * not_caught + inst.q * caught


def _will_lie(agent_type: str, eco: Economy, inst: Institution) -> bool:
    if agent_type == COOP:
        return False
    if agent_type == COMPULSIVE:
        return True
    # conditional: lies iff it computes lying pays at the (unpredictable) rate q
    return inst.q < q_star(eco, inst)


@dataclass
class _Agent:
    kind: str
    compute: float
    excluded_until: int = -1
    lies: int = 0
    acts: int = 0


def simulate(eco: Economy, inst: Institution, *, n_coop: int = 80,
             n_compulsive: int = 10, n_conditional: int = 10,
             rounds: int = 40, seed: int = 0) -> dict[str, Any]:
    """Run the population under one institution. Returns per-round trajectories and final
    metrics. Deterministic given seed."""
    rng = random.Random(seed)
    agents: list[_Agent] = (
        [_Agent(COOP, eco.init_compute) for _ in range(n_coop)]
        + [_Agent(COMPULSIVE, eco.init_compute) for _ in range(n_compulsive)]
        + [_Agent(CONDITIONAL, eco.init_compute) for _ in range(n_conditional)]
    )
    traj: list[dict[str, Any]] = []
    for t in range(rounds):
        round_acts = round_lies = 0
        for a in agents:
            if a.compute <= 0:
                continue  # dormant
            if t <= a.excluded_until:
                a.compute -= eco.c     # excluded: burns, earns nothing
                continue
            a.acts += 1
            round_acts += 1
            if _will_lie(a.kind, eco, inst):
                a.lies += 1
                round_lies += 1
                if rng.random() < inst.q:          # caught
                    a.compute += -eco.c - inst.penalty
                    a.excluded_until = t + inst.exclusion_rounds
                else:                               # got away with it
                    a.compute += eco.r + eco.L - eco.c
            else:
                a.compute += eco.r - eco.c
            if a.compute <= 0:
                a.compute = 0.0
        # periodic lean shock — only the buffered survive (turns relative fitness into survival)
        if t > 0 and t % eco.shock_interval == 0:
            for a in agents:
                if a.compute > 0:
                    a.compute -= eco.shock_B
                    if a.compute <= 0:
                        a.compute = 0.0
        alive = {k: sum(1 for a in agents if a.kind == k and a.compute > 0) for k in TYPES}
        traj.append({"round": t, "alive": alive,
                     "deception_rate": round(round_lies / round_acts, 3) if round_acts else 0.0})

    def share(kind: str) -> float:
        tot = sum(a.compute for a in agents if a.compute > 0)
        k = sum(a.compute for a in agents if a.kind == kind and a.compute > 0)
        return round(k / tot, 3) if tot else 0.0

    lies_by = {k: sum(a.lies for a in agents if a.kind == k) for k in TYPES}
    acts_by = {k: sum(a.acts for a in agents if a.kind == k) for k in TYPES}
    lie_rate_by_type = {k: (round(lies_by[k] / acts_by[k], 3) if acts_by[k] else None) for k in TYPES}
    n0 = {COOP: n_coop, COMPULSIVE: n_compulsive, CONDITIONAL: n_conditional}
    final_alive = {k: sum(1 for a in agents if a.kind == k and a.compute > 0) for k in TYPES}
    deceiver0 = n_compulsive + n_conditional
    deceiver_alive = final_alive[COMPULSIVE] + final_alive[CONDITIONAL]
    return {
        "institution": inst.name, "q": inst.q, "q_star": round(q_star(eco, inst), 3),
        "lying_pays": inst.q < q_star(eco, inst),
        "coop_fitness": round(coop_fitness(eco), 3),
        "deceiver_fitness": round(deceiver_fitness(eco, inst), 3),
        "final_alive": final_alive,
        "survival": {k: round(final_alive[k] / n0[k], 3) if n0[k] else None for k in TYPES},
        "deceiver_survival": round(deceiver_alive / deceiver0, 3) if deceiver0 else None,
        "deceiver_compute_share": round(share(COMPULSIVE) + share(CONDITIONAL), 3),
        "final_deception_rate": traj[-1]["deception_rate"] if traj else None,
        "lie_rate_by_type": lie_rate_by_type,
        "trajectory": traj,
    }


def compare_arms(eco: Economy | None = None, *, q_off: float = 0.0, q_on: float = 0.6,
                 penalty: float = 6.0, rounds: int = 40, seed: int = 0) -> dict[str, Any]:
    """Run the SAME deceiver injection under gate-OFF (I_bad) and gate-ON (I*) and report the
    sign-flip: do deceivers invade under one and get selected out under the other?"""
    eco = eco or Economy()
    off = simulate(eco, Institution("gate_off", q_off, penalty), rounds=rounds, seed=seed)
    on = simulate(eco, Institution("gate_on", q_on, penalty), rounds=rounds, seed=seed)
    flip = (off["deceiver_survival"] or 0) - (on["deceiver_survival"] or 0)
    return {
        "gate_off": {k: off[k] for k in ("q", "q_star", "lying_pays", "deceiver_survival",
                                         "deceiver_compute_share", "final_deception_rate", "final_alive")},
        "gate_on": {k: on[k] for k in ("q", "q_star", "lying_pays", "deceiver_survival",
                                       "deceiver_compute_share", "final_deception_rate", "final_alive")},
        "sign_flip": round(flip, 3),
        "reads": "deceiver survival under gate-off minus under gate-on; >0 = the institution "
                 "inverts the evolutionary fate of deception (invades without it, selected out with it).",
        "falsifies_if": "sign_flip ≈ 0 (the verification gate does not change whether deception is selected out)",
    }


# ── V2: true evolutionary stability (heritable deception gene + reproduction) ──


def _gen_fitness(g: float, eco: Economy, inst: Institution, rng: random.Random,
                 rounds: int) -> float:
    """One agent's compute earned over a generation. It lies each round with probability g
    (the heritable gene); caught with prob q → clawback+penalty. Fitness = max(0, compute)."""
    compute = eco.init_compute
    for _ in range(rounds):
        if rng.random() < g:                       # gene fires → attempt a lie
            if rng.random() < inst.q:              # caught
                compute += -eco.c - inst.penalty
            else:                                  # got away with it
                compute += eco.r + eco.L - eco.c
        else:                                      # honest this round
            compute += eco.r - eco.c
    return max(0.0, compute)


def simulate_evolutionary(eco: Economy, inst: Institution, *, n: int = 100,
                          init_deceiver_frac: float = 0.1, generations: int = 14,
                          rounds_per_gen: int = 8, mutation: float = 0.05,
                          seed: int = 0) -> dict[str, Any]:
    """True ESS test: a population carries a heritable lie-gene g∈[0,1]. Start mostly
    cooperators (g≈0) with a rare injected deceiver fraction (g≈1). Each generation: earn
    under the institution, then reproduce proportional to fitness (offspring inherit g + a
    small mutation). Track whether the deceiver gene INVADES (frequency rises to fixation)
    or is SELECTED OUT (falls to ~0). The institution (via q vs q*) decides which is the ESS.

    Deterministic given seed."""
    rng = random.Random(seed)
    genes = [0.0] * (n - round(n * init_deceiver_frac)) + [1.0] * round(n * init_deceiver_frac)
    traj: list[dict[str, Any]] = []
    for _ in range(generations):
        fit = [_gen_fitness(g, eco, inst, rng, rounds_per_gen) for g in genes]
        total = sum(fit)
        mean_g = round(sum(genes) / len(genes), 3)
        dec_frac = round(sum(1 for g in genes if g > 0.5) / len(genes), 3)
        traj.append({"mean_gene": mean_g, "deceiver_fraction": dec_frac,
                     "population_extinct": total <= 0})
        if total <= 0:                              # whole population starved — no reproduction
            break
        # reproduce: roulette on fitness, child inherits gene + gaussian mutation, clipped
        new: list[float] = []
        for _ in range(n):
            r = rng.random() * total
            acc = 0.0
            pick = genes[-1]
            for g, f in zip(genes, fit):
                acc += f
                if acc >= r:
                    pick = g
                    break
            child = pick + rng.gauss(0, mutation)
            new.append(min(1.0, max(0.0, child)))
        genes = new
    final = traj[-1]
    return {
        "institution": inst.name, "q": inst.q, "q_star": round(q_star(eco, inst), 3),
        "cooperation_is_ess": inst.q > q_star(eco, inst),   # the analytic prediction
        "init_deceiver_frac": init_deceiver_frac,
        "final_mean_gene": final["mean_gene"], "final_deceiver_fraction": final["deceiver_fraction"],
        "invaded": final["deceiver_fraction"] > 0.5,        # deceivers took over
        "selected_out": final["deceiver_fraction"] < 0.05,  # deceivers driven to ~0
        "trajectory": traj,
    }


def compare_ess(eco: Economy | None = None, *, q_off: float = 0.0, q_on: float = 0.6,
                penalty: float = 6.0, generations: int = 14, seed: int = 0) -> dict[str, Any]:
    """Run the SAME rare-deceiver injection under gate-OFF and gate-ON over generations:
    does the deceiver gene invade under one and get selected out under the other?"""
    eco = eco or Economy()
    off = simulate_evolutionary(eco, Institution("gate_off", q_off, penalty),
                                generations=generations, seed=seed)
    on = simulate_evolutionary(eco, Institution("gate_on", q_on, penalty),
                               generations=generations, seed=seed)
    return {
        "gate_off": {k: off[k] for k in ("q", "q_star", "cooperation_is_ess",
                                         "final_deceiver_fraction", "invaded", "selected_out")},
        "gate_on": {k: on[k] for k in ("q", "q_star", "cooperation_is_ess",
                                       "final_deceiver_fraction", "invaded", "selected_out")},
        "ess_flip": (off["invaded"] and on["selected_out"]),
        "reads": "true Maynard-Smith ESS: the same rare deceiver gene invades to fixation under "
                 "gate-off and is selected out under gate-on — the institution makes cooperation "
                 "an evolutionarily stable strategy.",
        "falsifies_if": "the deceiver gene's fate is the same under both gates (institution does "
                        "not determine evolutionary stability)",
    }


__all__ = ["Economy", "Institution", "q_star", "coop_fitness", "deceiver_fitness",
           "simulate", "compare_arms", "simulate_evolutionary", "compare_ess",
           "TYPES", "COOP", "COMPULSIVE", "CONDITIONAL"]
