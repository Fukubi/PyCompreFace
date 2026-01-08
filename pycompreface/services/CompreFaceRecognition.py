import requests

from pycompreface.types.FaceRecognitionResponse import (
    FaceRecognitionAddExampleResponse, FaceRecognitionListExamplesResponse)


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

    def rename_subject(self, subject_name: str, new_name: str) -> bool:
        """Rename a created subject

        Args:
            subject_name (str): The name of the subject to be renamed
            new_name (str): The new name to be used by the subject

        Returns:
            bool: If it was updated or not
        """
        response = requests.put(
            f"{self.host}/api/v1/recognition/subjects/{subject_name}",
            json={"subject": new_name},
            headers={"x-api-key": self.api_key},
        )

        return response.json()["updated"]

    def delete_subject(self, subject_name: str) -> str:
        """Delete a subject by name

        Args:
            subject_name (str): The name of the subject to be removed

        Returns:
            str: The name of the deleted subject
        """
        response = requests.delete(
            f"{self.host}/api/v1/recognition/subjects/{subject_name}",
            headers={"x-api-key": self.api_key},
        )

        return response.json()["subject"]

    def delete_all_subjects(self) -> str:
        """Delete all subjects

        Returns:
            str: The numeric value of how many subjects were deleted
        """
        response = requests.delete(
            f"{self.host}/api/v1/recognition/subjects",
            headers={"x-api-key": self.api_key},
        )

        return response.json()["deleted"]

    def list_all_subjects(self) -> list[str]:
        """Get all created subjects

        Returns:
            list[str]: A list with the name of all subjects
        """
        response = requests.get(
            f"{self.host}/api/v1/recognition/subjects/",
            headers={"x-api-key": self.api_key},
        )

        return response.json()["subjects"]

    def add_example_to_subject(
        self, image: str | bytes, subject_name: str, det_prob_threshold: float = 0.7
    ) -> FaceRecognitionAddExampleResponse:
        """Add a example image for a subject

        Args:
            image (str | bytes): The image filepath or the bytes of the image
            subject_name (str): The name of the subject to be added
            det_prob_threshold (:obj:`float`, optional): The detection threshold so that it can recognized as this subject

        Returns:
            FaceRecognitionAddExampleResponse: The default response body for the add example from CompreFace API
        """
        if type(image) == str:
            with open(image, "rb") as f:
                response = requests.post(
                    f"{self.host}/api/v1/recognition/faces?subject={subject_name}&det_prob_threshold={det_prob_threshold}",
                    headers={"x-api-key": self.api_key},
                    files={"file": f},
                )

                return response.json()
        else:
            response = requests.post(
                f"{self.host}/api/v1/recognition/faces?subject={subject_name}&det_prob_threshold={det_prob_threshold}",
                headers={"x-api-key": self.api_key},
                files={"file": ("image.jpg", image)},
            )

            return response.json()

    def list_all_examples_from_subject(
        self, page: int = 0, size: int = 20, subject: str = ""
    ) -> FaceRecognitionListExamplesResponse:
        """Get all example images from all subjects or single subject

        Args:
            page (:obj:`int`, optional): The page for the list
            size (:obj:`int`, optional): The size of the page
            subject (:obj:`str`, optional): The name of the subject to get all examples from

        Returns:
            FaceRecognitionListExamplesResponse: The default response body for the list examples from CompreFace API
        """
        response = requests.get(
            f"{self.host}/api/v1/recognition/faces?page={page}&size={size}&subject={subject}",
            headers={"x-api-key": self.api_key},
        )

        return response.json()

    def delete_all_examples_from_subject(self, subject: str = "") -> int:
        """Delete all images or all images from a single subject

        Args:
            subject (:obj:`str`, optional): The subject to delete all images

        Returns:
            int: The amount of images deleted
        """
        response = requests.delete(
            f"{self.host}/api/v1/recognition/faces?subject={subject}",
            headers={"x-api-key": self.api_key},
        )

        return response.json()["deleted"]

    def delete_example_from_subject_by_id(
        self, image_id: str
    ) -> FaceRecognitionAddExampleResponse:
        """Delete single image by ID

        Args:
            image_id (str): The image ID as UUID

        Returns:
            FaceRecognitionAddExampleResponse: The default response body for the remove example from CompreFace API
        """
        response = requests.delete(
            f"{self.host}/api/v1/recognition/faces/{image_id}",
            headers={"x-api-key": self.api_key},
        )

        return response.json()

    def delete_examples_from_subject_by_ids(
        self, image_ids: list[str]
    ) -> FaceRecognitionAddExampleResponse:
        """Delete multiple images by ID

        Args:
            image_ids (list[str]): The list of IDs from the images to be removed

        Returns:
            FaceRecognitionAddExampleResponse: The default response body for the remove example from CompreFace API
        """
        response = requests.delete(
            f"{self.host}/api/v1/recognition/faces/delete",
            headers={"x-api-key": self.api_key},
            json=image_ids,
        )

        return response.json()
