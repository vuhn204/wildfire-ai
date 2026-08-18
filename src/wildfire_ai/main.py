from fastapi import FastAPI

from wildfire_ai.api.routes.health import router as health_router
from wildfire_ai.api.routes.detection import router as detection_router
from wildfire_ai.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health_router)
app.include_router(detection_router)