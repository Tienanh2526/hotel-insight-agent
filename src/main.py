from fastapi import FastAPI

from src.api.router import api_router

app = FastAPI(
    title="Hotel Insight Agent API",
    description="Analyze hotel reviews and produce evidence-grounded insights.",
    version="0.1.0",
)

app.include_router(api_router)


@app.get("/health", tags=["System"])
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "hotel-insight-agent"}
