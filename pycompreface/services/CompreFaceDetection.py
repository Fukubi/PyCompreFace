from requests import post

from pycompreface.types.FaceDetectionResponse import FaceDetectionResponse


class CompreFaceDetection:
    """Use the Face Detection Service from CompreFace application in a host

    Attributes:
        api_key (str): The API key gotten from the CompreFace application for the FaceDetection
        host (str): The complete hostname of the CompreFace application
        limit (:obj:`int`, optional): The max number of faces to be detected (default is unlimited)
        det_prob_threshold (:obj:`float`, optional): The threshold of the probability of it being a
            face so it can be recognized as such (default is 0.7)
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
        use_age_plugin: bool = False,
        use_gender_plugin: bool = False,
        use_landmarks_plugin: bool = False,
        use_calculator_plugin: bool = False,
        use_pose_plugin: bool = False,
        use_mask_plugin: bool = False,
    ) -> None:
        """Default constructor

        Args:
            api_key (str): The API key gotten from the CompreFace application for the FaceDetection
            host (str): The complete hostname of the CompreFace application
            limit (:obj:`int`, optional): The max number of faces to be detected (default is unlimited)
            det_prob_threshold (:obj:`float`, optional): The threshold of the probability of it being a
                face so it can be recognized as such (default is 0.7)
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
        self.use_age_plugin = use_age_plugin
        self.use_gender_plugin = use_gender_plugin
        self.use_landmarks_plugin = use_landmarks_plugin
        self.use_calculator_plugin = use_calculator_plugin
        self.use_pose_plugin = use_pose_plugin
        self.use_mask_plugin = use_mask_plugin

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

    def face_detection_image(self, image: str | bytes) -> FaceDetectionResponse:
        """Detect faces from the image using the parameters from this class

        Args:
            image (str | bytes): The image filepath or the bytes of the image that the faces will be detected on

        Returns:
            FaceDetectionResponse: The detection and plugins result from the detection on the image above
        """

        url_string = f"{self.host}/api/v1/detection/detect?limit={self.limit}&det_prob_threshold={self.det_prob_threshold}{self.get_face_plugins()}"

        if type(image) == str:
            with open(image, "rb") as f:
                detection_response = post(
                    url_string,
                    headers={"x-api-key": self.api_key},
                    files={"file": f},
                )

                return detection_response.json()
        else:
            detection_response = post(
                url_string,
                headers={"x-api-key": self.api_key},
                files={"file": ("image.jpg", image)},
            )

            return detection_response.json()
