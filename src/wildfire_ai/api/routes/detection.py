from fastapi import APIRouter, File, UploadFile

from wildfire_ai.api.validators.image import validate_image
from wildfire_ai.schemas.detection import DetectionResponse
from wildfire_ai.services.detection import DetectionService

router = APIRouter()
detection_service = DetectionService()

@router.post("/detect", response_model=DetectionResponse)
async def detect_image(file: UploadFile = File(...)):
    file = validate_image(file)

    return detection_service.detect(file.filename)