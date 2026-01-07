from typing import Dict, List, TypedDict

from pycompreface.types.FaceDetectionResult import FaceDetectionResult


class FaceDetectionResponse(TypedDict):
    result: List[FaceDetectionResult]
    plugins_versions: Dict
