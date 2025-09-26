from fastapi import FastAPI
from app.core.config import settings
from app.core.health import router as health_router
from app.api.routes import router as api_router

app = FastAPI(title=settings.app_name)

app.include_router(health_router)
app.include_router(api_router)
