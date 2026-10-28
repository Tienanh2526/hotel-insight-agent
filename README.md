# Hotel Insight Agent — FastAPI Edition

Backend API prototype for analyzing hotel reviews with evidence-grounded AI workflows.

**Status:** MVP v0.1 — market hypothesis not yet validated.

## Stack
- Python 3.11+
- FastAPI + Uvicorn
- Pydantic v2
- pandas
- pytest + HTTPX

## Setup

### Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn src.main:app --reload
```

### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Open http://127.0.0.1:8000/docs for Swagger UI.

## Planned endpoints
- `GET /health`
- `POST /api/v1/reviews/validate`
- Later: `POST /api/v1/analyses`
- Later: `GET /api/v1/analyses/{analysis_id}`

Sprint 1 focuses on API startup and CSV validation. No LLM key is needed yet.
