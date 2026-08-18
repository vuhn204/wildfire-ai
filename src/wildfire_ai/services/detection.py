from wildfire_ai.schemas.detection import DetectionResponse
from wildfire_ai.services.model import DetectionModel


class DetectionService:
    def __init__(self, model: DetectionModel):
        self.model = model

    def detect(self, filename: str, image: bytes) -> DetectionResponse:
        detections = self.model.predict(image)

        return DetectionResponse(
            filename=filename,
            detections=detections,
            inference_time_ms=0.0,
        )