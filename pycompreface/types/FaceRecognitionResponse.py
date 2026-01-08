from typing import List, TypedDict

from pycompreface.types.FaceDetectionResult import (FaceDetectionAgeResult,
                                                    FaceDetectionBoxResult,
                                                    FaceDetectionExecutionTime,
                                                    FaceDetectionGenderResult,
                                                    FaceDetectionMaskResult)


class FaceRecognitionAddExampleResponse(TypedDict):
    """Type for the response of a add example to subject operation

    Attributes:
        image_id (str): The ID of the added image
        subject (str): The name of the subject added
    """

    image_id: str
    subject: str


class FaceRecognitionListExamplesResponse(TypedDict):
    """Type for the list all examples from subject(s)

    Attributes:
        faces (FaceRecognitionAddExampleResponse): The examples listed
        page_number (int): The number of the page searched
        page_size (int): The size of the page
        total_pages (int): The total of pages that can be searched
        total_elements (int): The total of elements in all the pages
    """

    faces: list[FaceRecognitionAddExampleResponse]
    page_number: int
    page_size: int
    total_pages: int
    total_elements: int


class FaceRecognitionResponse(TypedDict):
    """The default response from the FaceRecognition

    Attributes:
        similarity (float): How similar it is to the subject
        subject (str): Subject name
    """

    similarity: float
    subject: str


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
    subjects: List[FaceRecognitionResponse]
    execution_time: FaceDetectionExecutionTime
