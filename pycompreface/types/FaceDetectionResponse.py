from typing import Dict, List, TypedDict

from pycompreface.types.FaceDetectionResult import FaceDetectionResult


class FaceDetectionResponse(TypedDict):
    """Type for the Face Detection response from CompreFace API

    Attributes:
        result (List[FaceDetectionResult]): The results from the detection
        plugins_versions (Dict): If the status tag is used, shows the environment information
    """

    result: List[FaceDetectionResult]
    plugins_versions: Dict
