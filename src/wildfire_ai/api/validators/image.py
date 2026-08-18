from fastapi import HTTPException, UploadFile, status

from wildfire_ai.core.config import settings

def validate_image(file: UploadFile) -> UploadFile:
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No image file was provided.",
        )

    if file.content_type not in settings.allowed_image_types:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsupported image type: {file.content_type}",
        )

    max_size_bytes = settings.max_upload_size_mb * 1024 * 1024

    content = file.file.read()
    file.file.seek(0)

    if len(content) > max_size_bytes:
        raise HTTPException(
            status_code=413,
            detail=(
                f"Image exceeds the maximum allowed size "
                f"of {settings.max_upload_size_mb} MB."
            ),
        )

    return file