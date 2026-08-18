from pydantic import BaseModel, Field

class BoundingBox(BaseModel):
    x_min: float
    y_min: float
    x_max: float
    y_max: float

class Detection(BaseModel):
    class_name: str
    confidence: float = Field(ge=0.0, le=1.0)
    bbox: BoundingBox

class DetectionResponse(BaseModel):
    filename: str
    detections: list[Detection]
    inference_time_ms: float = Field(ge=0.0)
