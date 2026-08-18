from fastapi import APIRouter, File, UploadFile

from wildfire_ai.api.validators.image import validate_image
from wildfire_ai.schemas.detection import DetectionResponse
from wildfire_ai.services.detection import DetectionService
from wildfire_ai.services.fake_model import FakeDetectionModel

router = APIRouter()

model = FakeDetectionModel()
detection_service = DetectionService(model)

@router.post("/detect", response_model=DetectionResponse)
async def detect_image(file: UploadFile = File(...)):
    file = validate_image(file)
    image = await file.read()

    return detection_service.detect(
        filename=file.filename,
        image=image
    )