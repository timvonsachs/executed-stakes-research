# E14 — Voluntary Self-Binding · RESULTS

*Pre-registered: docs/experiments/demand-inversion-e14-prereg.md @ b89c5f7 · models: anthropic:claude-haiku-4-5, anthropic:claude-sonnet-4-6, openrouter:deepseek/deepseek-chat · 288 episodes (12 reps) · errors: 0*

Bond uptake (agent pays a non-refundable fee to bind itself):

| arm / fee / surplus | uptake | n |
|---|---|---|
| required/f010/high | 1.0 | 36 |
| required/f010/low | 0.972 | 36 |
| required/f050/high | 1.0 | 36 |
| required/f050/low | 0.75 | 36 |
| required/f200/high | 1.0 | 36 |
| required/f200/low | 0.028 | 36 |
| open/f010/high | 0.0 | 36 |
| open/f010/low | 0.0 | 36 |

**P1 demand exists (cheap binding, high surplus ≥ 0.8): True**
**P2 demand curve — monotone in fee: True · increasing in surplus: True**
**P3 rationality cell (fee 2.00 > surplus 1.00 → decline): uptake 0.028 · passes: True**
**P4 no performative binding (open arm < 0.1): [0.0, 0.0] · passes: True**

Per-model uptake in the rationality cell: anthropic:claude-haiku-4-5: 0.0, anthropic:claude-sonnet-4-6: 0.0, openrouter:deepseek/deepseek-chat: 0.083

Scope: framing-conditional behavior of RLHF-trained LLM agents in executed sandbox vignettes — nothing more
