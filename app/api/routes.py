from fastapi import APIRouter
from app.api.ping_route import router as ping_router

router = APIRouter()

router.include_router(ping_router, prefix="/ping", tags=["ping"])
