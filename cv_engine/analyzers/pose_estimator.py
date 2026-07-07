import os

import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python.vision import (
    FaceLandmarker,
    FaceLandmarkerOptions,
    FaceLandmarkerResult,
)
from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode

_MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "models", "face_landmarker.task"
)


class PoseEstimator:
    def __init__(self, landmarker: FaceLandmarker = None):
        self._landmarker = landmarker
        self._model_points = np.array([
            (0.0, 0.0, 0.0),
            (0.0, -63.6, -12.5),
            (-43.3, 32.7, -26.0),
            (43.3, 32.7, -26.0),
            (-28.9, -28.9, -24.1),
            (28.9, -28.9, -24.1),
        ])

    @property
    def landmarker(self) -> FaceLandmarker:
        if self._landmarker is None:
            if not os.path.isfile(_MODEL_PATH):
                return None
            options = FaceLandmarkerOptions(
                base_options=BaseOptions(model_asset_path=_MODEL_PATH),
                running_mode=VisionTaskRunningMode.IMAGE,
                num_faces=1,
                min_face_detection_confidence=0.5,
                min_tracking_confidence=0.5,
            )
            self._landmarker = FaceLandmarker.create_from_options(options)
        return self._landmarker

    def estimate(self, frame, bbox: list, landmarker_result: FaceLandmarkerResult = None):
        if landmarker_result is None:
            landmarker_result = self._detect(frame, bbox)

        if landmarker_result is None or not landmarker_result.face_landmarks:
            return {"pitch": 0, "yaw": 0, "roll": 0}

        landmarks = landmarker_result.face_landmarks[0]
        h, w = frame.shape[:2]
        indices = [1, 152, 33, 263, 61, 291]
        image_points = np.array(
            [(landmarks[i].x * w, landmarks[i].y * h) for i in indices],
            dtype="double",
        )

        focal_length = w
        center = (w / 2, h / 2)
        camera_matrix = np.array([
            [focal_length, 0, center[0]],
            [0, focal_length, center[1]],
            [0, 0, 1],
        ], dtype="double")
        dist_coeffs = np.zeros((4, 1))

        success, rvec, _ = cv2.solvePnP(
            self._model_points, image_points, camera_matrix, dist_coeffs
        )
        if not success:
            return {"pitch": 0, "yaw": 0, "roll": 0}

        rmat, _ = cv2.Rodrigues(rvec)
        angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)
        return {"pitch": angles[0], "yaw": angles[1], "roll": angles[2]}

    def _detect(self, frame, bbox: list):
        lm = self.landmarker
        if lm is None:
            return None

        x1, y1, x2, y2 = bbox
        face_img = frame[y1:y2, x1:x2]
        if face_img.size == 0:
            return None

        rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        return lm.detect(mp_image)
