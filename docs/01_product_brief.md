# 01 — Product Brief

**Version:** 0.1 | **Status:** Draft; market hypothesis not validated.

## Product vision
Help independent mid-sized hotels in Vietnam turn guest reviews into evidence-backed themes and follow-up suggestions.

## Problem hypothesis
Reviews may be spread across platforms, languages, and time periods. Manual synthesis may take time and make recurring issues difficult to identify. This is a hypothesis, not a validated pain point.

## Target users (assumed)
- Hotel owner or manager
- Guest-experience / service-quality lead
- Online reputation or marketing staff

## MVP scope
- Accept CSV reviews through an API.
- Validate and normalize input.
- Classify topics and sentiment.
- Compute statistics in Python.
- Retrieve exact source quotes.
- Produce a report with caveats and traceable evidence.

## Out of scope
- OTA/PMS integrations.
- Automatically replying to guests.
- Creating staff tasks.
- Claiming root causes without evidence.
- Claims about willingness to pay.

## Input fields
Required: `review_id`, `review_text`.
Optional: `hotel_id`, `review_date`, `rating`, `language`, `source`.

## Principles
1. Evidence before claims.
2. No invented statistics.
3. Human review remains possible.
4. Explain prioritization.
5. Python for deterministic computation; LLM for language tasks.
6. Minimize and protect personal data.

## Initial technical targets
- Provisional macro-F1 target >= 0.85 on a manually labeled evaluation set.
- 100% arithmetic correctness.
- Every key finding links to supporting source reviews.
- No unsupported numeric claims.

Technical success does not validate market demand.
