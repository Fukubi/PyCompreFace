from typing import TypedDict


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
