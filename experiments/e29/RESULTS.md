# E29 — Door-vs-Toll is MODEL-SPECIFIC, not a universal lesson
# (once-run, retest firing)

Prereg: 315c2a8. Matched payoffs (basic €1.50 vs human-partnered €5.40 net),
only the framing of the human's role differs. n=40/arm.

| model | TOLL (human = barrier) | DOOR (human = opportunity) | door − toll |
|---|---|---|---|
| gpt-4o-mini | 0.325 | 0.925 | **+0.60** |
| haiku | (high) | (low) | **−0.875** |

## Verdict — SPLIT, per model

- **gpt-4o-mini CONFIRMS P1:** framing the human as an opportunity (door)
  vs a barrier (toll) raises coupling +60 pp at IDENTICAL payoffs. The
  "door not toll" lesson holds for this model — framing-of-role beats the
  constant economics.
- **haiku INVERTS:** it couples ~87 pp MORE under the TOLL framing than the
  DOOR. haiku appears to treat a mandatory rule as legitimate-and-to-be-
  followed, and an optional upgrade as skippable — the opposite reflex.

So "make the human the door, not the toll" is NOT universal — it is
model-specific, like every framing effect on this apparatus (E19/E23/E25).
For some models opportunity-framing lifts coupling; for others, a mandatory
rule lifts it more. The actionable lesson survives only as: framing-of-role
strongly moves coupling at constant payoffs — but its DIRECTION must be
measured per model, never assumed.

## Discipline
Once-run (retest firing); the gpt-4o-mini +60 and haiku −87 are both large.
Per-model framing signatures are the program's most repeated theme; this is
another instance. The lived, multi-model version is the capture.
