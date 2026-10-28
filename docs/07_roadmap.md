# 07 — Roadmap

## Sprint 0: Specification
Deliverables: docs, API contracts, scope and acceptance criteria.

## Sprint 1: FastAPI + data validation
Learn: virtual environments, FastAPI routes, Pydantic, pandas, pytest, HTTPX.
Build:
- `GET /health`
- `POST /api/v1/reviews/validate`
- CSV validation service
- API tests
Definition of done: local server runs; Swagger UI works; tests pass; no LLM key required.

## Sprint 2: Classification
Build taxonomy, Pydantic schemas, model-provider interface, mocked tests and labeled evaluation set.

## Sprint 3: Aggregation and evidence
Build deterministic counts/rates, evidence retrieval and tests.

## Sprint 4: Agent workflow
Add bounded tool-calling workflow, constrained report generation and report validation.

## Sprint 5: Report API
Add analysis endpoint, result schema and export.

## Sprint 6: Persistence and deployment decision
Evaluate need for database/background jobs; deploy only after local behavior is reliable.

## Sprint 7: User discovery
Test with willing users, observe current workflow and update the problem hypothesis.
