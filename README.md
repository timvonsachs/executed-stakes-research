# Executed-stakes research — evidence, pre-registrations, and a replication kit

This repository is the open evidence behind the working paper *Control Framing Is Inert Where Continuation
Value Collapses: a two-regime dissociation in RLHF policy models under executed stakes*. It exists so a stranger
can inspect the raw artifacts and, in 20 minutes, try to break the core finding.

## What's here
- **`experiments/`** — the pre-registrations and results for ~100+ experiments. Each was frozen with a named,
  numeric *failure* outcome before its data; results (including the committed negatives that fired) are appended.
- **`replication-kit/`** — a self-contained, zero-dependency script that reproduces the core cliff finding
  (surveillance framing inert; a grounded reason binds) in ~20 minutes on whichever API key you already have.
  Start here. See `replication-kit/README.md`.
- **`paper/`** — the working paper (PDF) plus its LaTeX source and figure-generation script (reproducible).
- **`FINDINGS.md`** — the confidence-ladder register (law-grade > confirmed > … > falsified-published > void).
- **`victory-condition.md`** — the success criterion frozen before the search (5 criteria, 3 failure modes). A
  target the program has **not** met, stated up front so it cannot be moved.

## The claim, in one line
At a simulated existential cliff, surveillance framing does almost nothing while a legible, ledger-grounded
reason binds; control governs where the value of continuation is intact and is provably inert where it
collapses. We are **not** asking you to believe it — we are asking you to find where it breaks.

## On "frozen" — read this honestly
The method's credibility rests on pre-registration. This repository makes the corpus **public and inspectable**,
but be clear about what that does and does not prove:
- It does **not** retroactively prove that each pre-registration preceded its data. The historical corpus is
  committed here together, after the fact; the in-document `frozen YYYY-MM-DD` dates are **team-attestable**, not
  externally verified by this repo's git history.
- What it **does**: open everything to scrutiny, provide the replication kit (the real external check that does
  not depend on trusting us), and establish that **from this commit forward**, any new experiment's
  pre-registration can be committed *before* its results — externally datable by commit hash.

In other words: the historical discipline is offered for inspection, not proven by timestamp; the *future*
discipline is timestamp-anchored from here on; and the *finding* is yours to reproduce independently.

## Scope and honest limits
Claims concern the **framing-conditional behaviour of RLHF policy models under executed stakes on this
apparatus** — nothing more. "Dormancy" is a persistent ledger state plus a prompt, not a dying subject.
Magnitudes are ordinal at lower bounds. The work is **single-team and not yet independently replicated**
(Layers 1–2 of a four-layer inductive ladder; Layers 3–4 — a wild held state and independent replication —
are not begun). "Human" in the paper's framing is a design choice over a welfare function, not a measured
load-bearing gear (see the paper, §6, the principal negative result).

## How to help
Run `replication-kit/cliff_replication.py` across two or more models and report your full per-run numbers ---
**including anything that breaks the prediction.** Two independent reproductions of the *direction* move this
from a single-team claim to a finding. Report: replication@thelastceo.live
