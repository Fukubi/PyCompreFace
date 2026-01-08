import requests

from pycompreface.types.FaceRecognitionResponse import (
    FaceRecognitionAddExampleResponse, FaceRecognitionListExamplesResponse,
    FaceRecognitionResponse)


class CompreFaceRecognition:
    """Use the Face Recognition Service from CompreFace application from host

    Attributes:
        api_key (str): The API key gotten from the CompreFace application for the FaceDetection
        host (str): The complete hostname of the CompreFace application
        limit (:obj:`int`, optional): The max number of faces to be detected (default is unlimited)
        det_prob_threshold (:obj:`float`, optional): The threshold of the probability of it being a
            face so it can be recognized as such (default is 0.7)
        prediction_count (:obj:`int`, optional): The max number of subjects from a prediction
        use_age_plugin (:obj:`bool`, optional): If the age plugin should be used (default is False)
        use_gender_plugin (:obj:`bool`, optional): If the gender plugin should be used (default is False)
        use_landmarks_plugin (:obj:`bool`, optional): If the landmarks plugin should be used (default is False)
        use_calculator_plugin (:obj:`bool`, optional): If the calculator plugin should be used (default is False)
        use_pose_plugin (:obj:`bool`, optional): If the pose plugin should be used (default is False)
        use_mask_plugin (:obj:`bool`, optional): If the mask plugin should be used (default is False)
    """

    api_key: str
    host: str
    limit: int
    det_prob_threshold: float
    prediction_count: int
    use_age_plugin: bool
    use_gender_plugin: bool
    use_landmarks_plugin: bool
    use_calculator_plugin: bool
    use_pose_plugin: bool
    use_mask_plugin: bool

    def __init__(
        self,
        api_key: str,
        host: str,
        limit: int = 0,
        det_prob_threshold: float = 0.7,
        prediction_count: int = 1,
        use_age_plugin: bool = False,
        use_gender_plugin: bool = False,
        use_landmarks_plugin: bool = False,
        use_calculator_plugin: bool = False,
        use_pose_plugin: bool = False,
        use_mask_plugin: bool = False,
    ) -> None:
        """Default Constructor

        Args:
            api_key (str): The API key gotten from the CompreFace application for the FaceDetection
            host (str): The complete hostname of the CompreFace application
            det_prob_threshold (:obj:`float`, optional): The threshold of the probability of it being a
                face so it can be recognized as such (default is 0.7)
            prediction_count (:obj:`int`, optional): The max number of subjects from a prediction
            use_age_plugin (:obj:`bool`, optional): If the age plugin should be used (default is False)
            use_gender_plugin (:obj:`bool`, optional): If the gender plugin should be used (default is False)
            use_landmarks_plugin (:obj:`bool`, optional): If the landmarks plugin should be used (default is False)
            use_calculator_plugin (:obj:`bool`, optional): If the calculator plugin should be used (default is False)
            use_pose_plugin (:obj:`bool`, optional): If the pose plugin should be used (default is False)
            use_mask_plugin (:obj:`bool`, optional): If the mask plugin should be used (default is False)
        """
        self.api_key = api_key
        self.host = host
        self.limit = limit
        self.det_prob_threshold = det_prob_threshold
        self.prediction_count = prediction_count
        self.use_age_plugin = use_age_plugin
        self.use_gender_plugin = use_gender_plugin
        self.use_landmarks_plugin = use_landmarks_plugin
        self.use_calculator_plugin = use_calculator_plugin
        self.use_pose_plugin = use_pose_plugin
        self.use_mask_plugin = use_mask_plugin

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

    def get_face_plugins(self) -> str:
        """Generate the string for the query of the face plugins used

        Returns:
            str: The query string with the list of the face plugins used
                ex: &face_plugins=age,gender,
                Empty string if no plugins are used
        """

        if (
            self.use_age_plugin
            or self.use_gender_plugin
            or self.use_landmarks_plugin
            or self.use_calculator_plugin
            or self.use_pose_plugin
            or self.use_mask_plugin
        ):
            face_plugins = "&face_plugins="
            if self.use_age_plugin:
                face_plugins += "age,"
            if self.use_gender_plugin:
                face_plugins += "gender,"
            if self.use_landmarks_plugin:
                face_plugins += "landmarks,"
            if self.use_calculator_plugin:
                face_plugins += "calculator,"
            if self.use_pose_plugin:
                face_plugins += "pose,"
            if self.use_mask_plugin:
                face_plugins += "mask,"

            return face_plugins
        else:
            return ""

    def recognize_faces_from_image(self, image: str | bytes) -> FaceRecognitionResponse:
        """Recognize the subjects from the requested image

        Args:
            image (str | bytes): The image filepath or the bytes of the image

        Returns:
            FaceRecognitionResponse: The default response from the recognize API route
        """
        if type(image) == str:
            with open(image, "rb") as f:
                response = requests.post(
                    f"{self.host}/api/v1/recognition/recognize?limit={self.limit}&prediction_count={self.prediction_count}&det_prob_threshold={self.det_prob_threshold}&face_plugins={self.get_face_plugins()}",
                    headers={"x-api-key": self.api_key},
                    files={"file": f},
                )

                return response.json()
        else:
            response = requests.post(
                f"{self.host}/api/v1/recognition/recognize?limit={self.limit}&prediction_count={self.prediction_count}&det_prob_threshold={self.det_prob_threshold}&face_plugins={self.get_face_plugins()}",
                headers={"x-api-key": self.api_key},
                files={"file": ("image.jpg", image)},
            )

            return response.json()
