from fastapi import APIRouter

from src.api.routes.reviews import router as reviews_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(reviews_router)
