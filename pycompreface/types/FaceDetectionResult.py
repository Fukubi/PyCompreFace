from typing import List, TypedDict


class FaceDetectionAgeResult(TypedDict):
    """Type for the Face Detection response from the age plugin on CompreFace REST API

    Attributes:
        probability (float): The probability of the age being correct
        high (int): The max age value range predicted from the image
        low (int): The min age value range predicted from the image
    """

    probability: float
    high: int
    low: int


class FaceDetectionGenderResult(TypedDict):
    """Type for the Face Detection response from the gender plugin on CompreFace REST API

    Attributes:
        probability (float): The probability of the gender being correct
        value (str): The gender predicted from the image
    """

    probability: float
    value: str


class FaceDetectionMaskResult(TypedDict):
    """Type for the Face Detection response from the mask plugin on CompreFace REST API

    Attributes:
        probability (float): The probability of the mask status being correct
        value (str): The status of the mask
    """

    probability: float
    value: str


class FaceDetectionBoxResult(TypedDict):
    """Type for the Face Detection box result response on CompreFace REST API

    Attributes:
        probability (float): The probability of the box limiting the face being correct
        x_max (int): The upperbound on the x value range for the detection box of the face
        y_max (int): The upperbound on the y value range for the detection box of the face
        x_min (int): The lowerbound on the x value range for the detection box of the face
        y_min (int): The lowerbound on the x value range for the detection box of the face
    """

    probability: float
    x_max: int
    y_max: int
    x_min: int
    y_min: int


class FaceDetectionExecutionTime(TypedDict):
    """Type for the Face Detection execution time response on CompreFace REST API

    Attributes:
        age (float): The time taken for the age plugin if used
        gender (float): The time taken for the gender plugin if used
        detector (float): The time taken for the detector plugin if used
        calculator (float): The time taken for the calculator plugin if used
        mask (float): The time taken for the mask plugin if used
    """

    age: float
    gender: float
    detector: float
    calculator: float
    mask: float


class FaceDetectionResult(TypedDict):
    """Type for the complete Face Detection response from the CompreFace REST API

    Attributes:
        age (FaceDetectionAgeResult): The result from the age plugin if used
        gender (FaceDetectionGenderResult): The result from the gender plugin if used
        mask (FaceDetectionMaskResult): The result from the mask plugin if used
        embedding (List[float]): The result from the calculator plugin if used
        box (FaceDetectionBoxResult): The bounding box of the detected face
        landmarks (List[List[float]): The result from the landmarks plugin if used
        execution_time (FaceDetectionExecutionTime): The execution time of all plugins
    """

    age: FaceDetectionAgeResult
    gender: FaceDetectionGenderResult
    mask: FaceDetectionMaskResult
    embedding: List[float]
    box: FaceDetectionBoxResult
    landmarks: List[List[float]]
    execution_time: FaceDetectionExecutionTime
