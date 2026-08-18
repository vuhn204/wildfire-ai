from fastapi import APIRouter, File, UploadFile

from wildfire_ai.api.validators.image import validate_image
from wildfire_ai.schemas.detection import DetectionResponse

router = APIRouter()


@router.post("/detect", response_model=DetectionResponse)
async def detect_image(file: UploadFile = File(...)):
    file = validate_image(file)

    return DetectionResponse(
        filename=file.filename,
        detections=[],
        inference_time_ms=0.0,
    )