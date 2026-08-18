from fastapi import APIRouter, File, UploadFile

from wildfire_ai.api.validators.image import validate_image

router = APIRouter()


@router.post("/detect")
async def detect_image(file: UploadFile = File(...)):
    file = validate_image(file)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }