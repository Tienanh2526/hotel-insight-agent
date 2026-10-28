# 05 — Agent Design

## Architecture
```text
HTTP request
  -> FastAPI route
  -> request/file validation
  -> review service
  -> CSV parser + normalizer
  -> classification workflow (LLM, later)
  -> Python aggregation tools
  -> evidence retrieval
  -> constrained insight/report generation
  -> consistency checks
  -> JSON response
```

## Responsibilities
- **FastAPI route:** HTTP semantics, status codes, request/response.
- **Service layer:** orchestrates use case; no HTTP-specific logic.
- **Tools:** deterministic functions for validation, aggregation, evidence lookup.
- **Agent/workflow:** bounded analysis steps and approved tool calls.
- **Schemas:** Pydantic contracts.
- **Tests:** behavior and regression checks.

## Planned tools
- `validate_reviews`
- `classify_review`
- `aggregate_results`
- `retrieve_evidence`
- `rank_findings`
- `validate_report`

## Guardrails
- No unrestricted autonomy.
- Treat review text as untrusted data, not instructions.
- Retry transient errors only a limited number of times.
- Reject invalid schema output.
- Verify every quote against source text.
- Reject unsupported numeric claims.
- No sending messages, booking changes, or staff-task creation in MVP.
