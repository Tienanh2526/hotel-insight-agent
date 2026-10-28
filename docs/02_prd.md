# 02 — PRD (FastAPI MVP)

## Objective
Expose review validation and analysis through a versioned REST API. Start with validation before adding LLM functionality.

## API design
### `GET /health`
Returns service status.

### `POST /api/v1/reviews/validate`
Accepts one CSV upload using multipart form data. Returns total rows, valid rows, invalid rows, detected columns, and row-level issues (row number and reason; avoid echoing review text).

### Later: `POST /api/v1/analyses`
Runs classification, aggregation, evidence retrieval, and report generation.

### Later: `GET /api/v1/analyses/{analysis_id}`
Retrieves a previous analysis. Persistence is an open design decision.

## Functional requirements
- Required CSV columns: `review_id`, `review_text`.
- Support UTF-8 and UTF-8 with BOM.
- Flag empty IDs/text and duplicate IDs.
- Report invalid optional date/rating; do not fabricate values.
- Preserve original review text for evidence quotes.
- Compute aggregate counts in Python.
- Validate LLM output against schemas.
- Verify report numeric claims against computed aggregates.
- Initial file-size target: 10 MB.
- Return clear 4xx errors for invalid input.

## Non-functional requirements
- Python 3.11+
- FastAPI, Pydantic v2, pandas, pytest, HTTPX
- Secrets only in environment variables / ignored `.env`
- Unit and API tests
- OpenAPI docs through Swagger UI
- No external side effects in MVP

## Acceptance criteria
- `/health` returns HTTP 200 and JSON status `ok`.
- Validation endpoint distinguishes valid and invalid rows.
- Missing required columns returns a clear 4xx response.
- Aggregation math is deterministic.
- Findings link to exact source reviews.
- Tests pass locally.
- No LLM key required for Sprint 1.

## Open questions
- Should large analyses use background jobs?
- Is persistence needed, and what is the retention policy?
- What real hotel workflow does this improve? This remains unvalidated.
