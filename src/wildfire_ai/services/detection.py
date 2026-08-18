from wildfire_ai.schemas.detection import DetectionResponse


class DetectionService:
    def detect(self, filename: str) -> DetectionResponse:
        return DetectionResponse(
            filename=filename,
            detections=[],
            inference_time_ms=0.0,
        )