from wildfire_ai.schemas.detection import Detection
from wildfire_ai.services.detection import DetectionService

class StubDetectionModel:
    def predict(self, image: bytes) -> list[Detection]:
        return [
            Detection(
                class_name="fire",
                confidence=0.95,
                bbox={
                    "x_min": 10,
                    "y_min": 20,
                    "x_max": 100,
                    "y_max": 200,
                },
            )
        ]

def test_detection_service_returns_model_detections():
    service = DetectionService(StubDetectionModel())

    result = service.detect(
        filename="test.jpg",
        image=b"fake_image",
    )

    assert result.filename == "test.jpg"
    assert len(result.detections) == 1
    assert result.detections[0].class_name == "fire"
    assert result.detections[0].confidence == 0.95
    assert result.inference_time_ms == 0.0