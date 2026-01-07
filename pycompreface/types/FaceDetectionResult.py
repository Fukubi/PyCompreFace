from typing import List, TypedDict


class FaceDetectionAgeResult(TypedDict):
    probability: float
    high: int
    low: int


class FaceDetectionGenderResult(TypedDict):
    probability: float
    value: str


class FaceDetectionMaskResult(TypedDict):
    probability: float
    value: str


class FaceDetectionBoxResult(TypedDict):
    probability: float
    x_max: int
    y_max: int
    x_min: int
    y_min: int


class FaceDetectionExecutionTime(TypedDict):
    age: float
    gender: float
    detector: float
    calculator: float
    mask: float


class FaceDetectionResult(TypedDict):
    age: FaceDetectionAgeResult
    gender: FaceDetectionGenderResult
    mask: FaceDetectionMaskResult
    embedding: List[float]
    box: FaceDetectionBoxResult
    landmarks: List[List[float]]
    execution_time: FaceDetectionExecutionTime
