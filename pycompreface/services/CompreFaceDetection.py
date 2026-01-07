from requests import post

from pycompreface.types.FaceDetectionResponse import FaceDetectionResponse


class CompreFaceDetection:
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
