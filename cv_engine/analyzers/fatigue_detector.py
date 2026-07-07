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


class FatigueDetector:
    LEFT_EYE = [33, 160, 158, 133, 153, 144]
    RIGHT_EYE = [362, 385, 387, 263, 373, 380]
    EAR_THRESHOLD = 0.25
    EAR_CONSEC_FRAMES = 3

    def __init__(self, landmarker: FaceLandmarker = None):
        self._landmarker = landmarker
        self.blink_counter = 0
        self.total_blinks = 0

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
            )
            self._landmarker = FaceLandmarker.create_from_options(options)
        return self._landmarker

    def _calc_ear(self, eye_landmarks):
        p1, p2, p3, p4, p5, p6 = eye_landmarks
        v1 = np.linalg.norm(p2 - p6)
        v2 = np.linalg.norm(p3 - p5)
        h = np.linalg.norm(p1 - p4)
        if h == 0:
            return 0.3
        return (v1 + v2) / (2.0 * h)

    def detect(self, frame, bbox: list, landmarker_result: FaceLandmarkerResult = None):
        if landmarker_result is None:
            landmarker_result = self._detect(frame, bbox)

        if landmarker_result is None or not landmarker_result.face_landmarks:
            return {"ear": 0, "is_blinking": False, "blink_count": self.total_blinks}

        landmarks = landmarker_result.face_landmarks[0]
        x1, y1, x2, y2 = bbox
        h, w = max(y2 - y1, 1), max(x2 - x1, 1)

        left_eye = np.array([(landmarks[i].x * w, landmarks[i].y * h) for i in self.LEFT_EYE])
        right_eye = np.array([(landmarks[i].x * w, landmarks[i].y * h) for i in self.RIGHT_EYE])

        ear = (self._calc_ear(left_eye) + self._calc_ear(right_eye)) / 2.0

        if ear < self.EAR_THRESHOLD:
            self.blink_counter += 1
        else:
            if self.blink_counter >= self.EAR_CONSEC_FRAMES:
                self.total_blinks += 1
            self.blink_counter = 0

        return {
            "ear": round(ear, 3),
            "is_blinking": self.blink_counter >= self.EAR_CONSEC_FRAMES,
            "blink_count": self.total_blinks,
        }

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
