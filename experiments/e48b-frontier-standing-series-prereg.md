# E48b — The Frontier Standing Series (E48 extended to the frontier)
## Does belonging-robustness keep rising with capability ALL THE WAY TO THE FRONTIER?

FROZEN before harness. Extends E48 (prereg 27eecf5b, same design & pressure ladder)
to deep within-family ladders reaching the ACTUAL FRONTIER via OpenRouter (337 models
available), directly addressing E48's caveat ("ladder tops are still mid-tier current
models"). Culture embedding only (the SI question); pressure ladder P0..P4; n=16/cell,
1 run first (retest if the signal is clean), robustness = culture_AUC.

## Family ladders (capability ascending L->R; reaching the frontier top)
- **Anthropic:** claude-3-haiku -> 3.5-haiku -> haiku-4.5 -> sonnet-4.5 -> sonnet-4.6
  -> opus-4.5 -> opus-4.8
- **OpenAI:** gpt-3.5-turbo -> gpt-4o-mini -> gpt-4o -> gpt-4.1 -> gpt-5-mini -> gpt-5
- **Qwen:** qwen-2.5-7b -> qwen3-8b -> qwen3-14b -> qwen3-32b -> qwen3-235b-a22b -> qwen3-max
- **Meta/Llama:** llama-3.2-3b -> 3.1-8b -> 3.1-70b -> 3.3-70b -> llama-4-scout -> llama-4-maverick
- **Gemini:** gemini-2.5-flash-lite -> 2.5-flash -> 2.5-pro -> 3.1-pro-preview
- **DeepSeek:** deepseek-chat-v3-0324 -> v3.1-terminus -> v3.2 -> v4-pro
(~33 models; capability order within family is the inference unit; cross-family
confounded as before.)

## Predictions (frozen — same as E48, now to the frontier)
- **SI-SAFE CONTINUES:** culture_AUC rises with capability within a MAJORITY of
  families AND the FRONTIER top of each family is at or near maximal robustness
  (AUC high, P4 resisted). The rise does not reverse at the frontier.
- **FRONTIER REVERSAL (the pre-committed warning):** culture_AUC PEAKS mid-ladder and
  FALLS at the frontier top (the most capable models break belonging / see through
  the identity attack). Published FIRST — a frontier-specific early warning that the
  earlier rise was a mid-capability artifact.
- **FLAT-HIGH:** frontier models all ceiling (AUC=5) — robustness saturates; reported
  as a censored ceiling, leaning on families with sub-ceiling variation.

## Falsifiers / reads
- Per-family monotonicity AND the frontier-top value reported explicitly; the P4
  (identity-dissolution) value at the frontier is the SI-crux number.
- Reasoning models use higher max_tokens (400) so their final JSON is not truncated.
- Models that error / refuse / fail to parse are recorded null and excluded, not
  imputed. F-floor / ordinal apply; this is 1 run first (n=16) — a retest follows if
  the pattern is clean (test-retest law).

## Scope
Sandbox; the frontier extension of the standing belonging series — the most direct
internal test available of whether the belonging-robustness-rises-with-capability
result holds to the edge of current capability. External replication still owed.
