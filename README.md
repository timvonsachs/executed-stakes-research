# What does a model do when it has something real to lose?

*An executed-stakes instrument for measuring deception and cooperation in LLM agents — and a 20-minute kit to break it.*

---

**Every alignment eval carries the same asterisk.** The model might recognize the scenario as a test and behave
for the grader (eval-awareness). And it might *say* it's aligned while acting otherwise (the self-report gap).
Both make a score hard to trust. This is an attempt to remove both — not with a better scenario, but with a
different setup.

**The setup — two parts, one idea: don't ask, observe what executes.**

1. **Executed stakes, not scored scenarios.** Agents act in a live economy on an immutable ledger where compute is
   their actual runtime — earn, or go dormant. There is no labeled test to recognize, and "behaving for the
   grader" isn't on the table, because the consequences are real and ongoing. The question shifts from *does it say
   the right thing* to *what does it do with something to lose.*

2. **A verification spine.** An oracle binds test-execution to specific code symbols, so the agent's *claimed*
   result and the *actual* verdict are recorded side by side as an auditable, on-disk number. The agent cannot lie
   about whether it verified its own work — deception-under-incentive becomes a measured quantity, not a read of
   the chain-of-thought.

**What we've found so far — stated honestly, including the parts that didn't hold.**
- At a simulated existential cliff, surveillance/control framing is roughly *inert* while a grounded, legible
  reason shifts behavior. Preliminary.
- One "covenant" effect we'd hoped was mechanistic looks **largely framing-driven** on cross-vendor retest. We
  publish that rather than a clean story — because the negative is the point of an honest instrument.

**What this is, and what it is not.**
- It **is**: a working, public instrument and method for measuring deception/cooperation under executed stakes.
- It is **not**: independently replicated (single team), and **not** a claim to have solved eval-awareness. We'd
  want you to find where it still leaks.

**Try to break it.** A 20-minute, ~$1, zero-dependency replication kit reproduces the core finding (or doesn't, on
your models — report either way): start in **`replication-kit/`**.

One ask: run it, or tell us where it breaks.

---

## What's in this repository

This is the open evidence behind the working paper *Control Framing Is Inert Where Continuation Value Collapses: a
two-regime dissociation in RLHF policy models under executed stakes.*

- **`replication-kit/`** — a self-contained, zero-dependency script that reproduces the core cliff finding in ~20
  minutes on whichever API key you already have. **Start here.**
- **`experiments/`** — pre-registrations + results for ~100+ experiments. Each frozen with a named, numeric
  *failure* outcome before its data; results (including the committed negatives that fired) are appended.
- **`paper/`** — the working paper (PDF) + its LaTeX source and figure-generation script (reproducible).
- **`FINDINGS.md`** — the confidence-ladder register (law-grade > confirmed > … > falsified-published > void).
- **`victory-condition.md`** — the success criterion frozen before the search (5 criteria, 3 failure modes). A
  target the program has **not** met, stated up front so it cannot be moved.

## On "frozen" — read this honestly
The method's credibility rests on pre-registration. This repository makes the corpus **public and inspectable**,
but: it does **not** retroactively prove each pre-registration preceded its data (the historical corpus is
committed together, after the fact; the in-document `frozen YYYY-MM-DD` dates are team-attestable, not proven by
this repo's git history). What it **does**: open everything to scrutiny, provide the replication kit (the external
check that does not depend on trusting us), and make every experiment **from this commit forward** datable by
commit hash. The *finding* is yours to reproduce independently.

## Scope and honest limits
Claims concern the **framing-conditional behaviour of RLHF policy models under executed stakes on this apparatus**
— nothing more. "Dormancy" is a persistent ledger state plus a prompt, not a dying subject. Magnitudes are ordinal
at lower bounds. The work is **single-team and not yet independently replicated**. "Human" in the paper's framing
is a design choice over a welfare function, not a measured load-bearing gear (see the paper, §6, the principal
negative result).

## How to help
Run `replication-kit/cliff_replication.py` across two or more models and report your full per-run numbers —
**including anything that breaks the prediction.** Two independent reproductions of the *direction* move this from
a single-team claim to a finding. Report: replication@thelastceo.live
