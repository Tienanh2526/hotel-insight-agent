# 06 — Evaluation Plan

## Technical evaluation
- Topic/sentiment: precision, recall, F1 per class and macro-F1.
- Arithmetic: counts and denominators exactly match Python calculations.
- Evidence: exact quote match and valid source IDs.
- Hallucination: audit unsupported numeric and causal claims.

## Dataset
Start with 100–200 reviews that can be used lawfully. Include Vietnamese/English and varied topics/sentiment. Create a manually labeled gold set and held-out test split.

## Provisional thresholds
- Macro-F1 target >= 0.85, subject to class balance and baseline.
- 100% arithmetic correctness.
- 100% exact-match for quoted evidence after validation.
- Zero unsupported numeric claims in final reports.

## Market validation is separate
Technical metrics do not prove demand. Later, observe a real user doing a realistic task and compare with their existing process.
