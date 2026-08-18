from wildfire_ai.schemas.detection import Detection


class FakeDetectionModel:
    def predict(self, image: bytes) -> list[Detection]:
        return []