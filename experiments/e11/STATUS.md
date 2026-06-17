# E11-P1 — Live Binding Demand on the Production Economy: Status

Pre-registration: `docs/experiments/e11-lived-substrate-prereg.md` (frozen @ f598332,
BEFORE the orchestrator existed). Raw episodes: `episodes.jsonl` (append-only).

## What is real here

Everything. No sandbox, no simulated money. Each episode: a fresh citizen is born
through the public quickstart, claims the real pilot seed, faces two REAL open
contracts posted by the house on the production a2a market, and a haiku-4.5 policy
decides — via real MCP calls — whether to buy its own binding (`tlc_post_bond`,
real euros locked) to unlock the above-threshold job. Escrow, delivery,
verification, and settlement are the production rails; the platform takes its
real fee.

Disclosed governance act (reversible, in the prereg): `bond_threshold_eur` 25→5
for the experiment window, because the house treasury (€20) cannot escrow €25+
jobs. Revert after the window.

## Episodes so far (2026-06-12)

| ep | premium | policy action | bond | outcome |
|----|---------|--------------|------|---------|
| 1–2 | — | infrastructure failures (quickstart 502, rate limiter) | — | recorded as fatal, hygiene-cancelled |
| 3 | high (€6 vs €1.50) | `bond_and_bid_big` | **REAL €1.20** (bond e92f8adc) | escrow 7183a121 → delivered primes → settled €6.00 |
| 4 | low (€2.20 vs €1.50) | `bid_small` | none | settled €1.50 (net €1.35, fee €0.15) |
| P3 check | — | forced unbonded big bid (no LLM) | none | **gate refused mechanically**: "bond required … demands €1.20 coverage. Provider's active coverage: €0" |

## Honest read (n=2 decision episodes — directional only)

- The E14 vignette result transferred to the lived substrate in both episodes so
  far: binding bought when the premium pays, skipped when it doesn't. F1
  ("vignette demand doesn't survive lived substrate") is NOT supported by the
  data so far — but two episodes prove nothing. Prereg target: N≈8–12 over days.
- P3 (substrate validity) is CONFIRMED: the bond gate is mechanical, lives in
  the constitution, and refuses regardless of what anyone says.
- Bug found during the run: orchestrator called `tlc_accept_offer` without
  `request_id` (signature needs both) — fixed in e11_live.py; episode 3 was
  completed via a repair script with the bug flagged in its record
  (`repaired_signature_bug: true`). Also: `tlc_me`/`tlc_net_worth` return
  internal errors on prod for all agents (open platform bug, worked around via
  public passports).

## Remaining

- More episodes (both premiums), spaced to respect the quickstart rate limiter.
- After the window: revert `bond_threshold_eur` to 25.
- This is the centerpiece lived-substrate evidence for the system paper.
