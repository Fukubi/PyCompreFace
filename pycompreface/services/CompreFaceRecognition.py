from typing import TypedDict

import requests


class CompreFaceRecognition:
    """Use the Face Recognition Service from CompreFace application from host

    Attributes:
        api_key (str): The API key gotten from the CompreFace application for the FaceDetection
        host (str): The complete hostname of the CompreFace application
    """

    api_key: str
    host: str

    def __init__(self, api_key: str, host: str) -> None:
        """Default Constructor

        Args:
            api_key (str): The API key gotten from the CompreFace application for the FaceDetection
            host (str): The complete hostname of the CompreFace application
        """
        self.api_key = api_key
        self.host = host

    def add_subject(self, subject_name: str) -> str:
        """Add a new subject to the CompreFace

        Args:
            subject_name (str): The name of the subject to be added

        Returns:
            str: The name of the subject name added
        """
        response = requests.post(
            f"{self.host}/api/v1/recognition/subjects",
            json={"subject": subject_name},
            headers={"x-api-key": self.api_key},
        )

        return response.json()["subject"]
