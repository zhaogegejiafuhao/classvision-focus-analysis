import os

import cv2
import mediapipe as mp
from mediapipe.tasks.python.vision import (
    FaceLandmarker,
    FaceLandmarkerOptions,
    FaceLandmarkerResult,
)
from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode

from cv_engine.analyzers.pose_estimator import PoseEstimator
from cv_engine.analyzers.fatigue_detector import FatigueDetector
from cv_engine.utils.time_state_machine import ExamStateMachine

_MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "models", "face_landmarker.task"
)


class AttentionAnalyzer:
    W_GAZE = 0.40
    W_POSE = 0.35
    W_FATIGUE = 0.25

    W_GAZE_EXAM = 0.50
    W_POSE_EXAM = 0.35
    W_FATIGUE_EXAM = 0.15

    def __init__(self, exam_mode: bool = False):
        self._landmarker: FaceLandmarker | None = None
        self.pose_estimator = PoseEstimator()
        self.fatigue_detector = FatigueDetector()
        self._blink_states: dict[int, dict] = {}
        self.exam_mode = exam_mode
        self._exam_sm = ExamStateMachine() if exam_mode else None

    @property
    def landmarker(self) -> FaceLandmarker | None:
        if self._landmarker is None:
            if not os.path.isfile(_MODEL_PATH):
                return None
            options = FaceLandmarkerOptions(
                base_options=BaseOptions(model_asset_path=_MODEL_PATH),
                running_mode=VisionTaskRunningMode.IMAGE,
                num_faces=10,
                min_face_detection_confidence=0.5,
                min_tracking_confidence=0.5,
            )
            self._landmarker = FaceLandmarker.create_from_options(options)
            self.pose_estimator._landmarker = self._landmarker
            self.fatigue_detector._landmarker = self._landmarker
        return self._landmarker

    def _detect_landmarks(self, frame, bbox: list) -> FaceLandmarkerResult | None:
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

    def _score_pose(self, pose: dict) -> float:
        pitch = abs(pose.get("pitch", 0))
        yaw = abs(pose.get("yaw", 0))
        pitch_score = max(0, 100 - pitch * 2)
        yaw_score = max(0, 100 - yaw * 2)
        return (pitch_score + yaw_score) / 2

    def _score_fatigue(self, fatigue: dict) -> float:
        ear = fatigue.get("ear", 0.3)
        blink_count = fatigue.get("blink_count", 0)
        ear_score = min(100, ear * 300)
        blink_penalty = min(30, blink_count * 3)
        return max(0, ear_score - blink_penalty)

    def _score_gaze(self, pose: dict) -> float:
        yaw = abs(pose.get("yaw", 0))
        return max(0, 100 - yaw * 2.5)

    def _score_gaze_exam(self, pose: dict) -> float:
        yaw = abs(pose.get("yaw", 0))
        return max(0, 100 - yaw * 3.5)

    def _check_cheating_nearby(self, person_bbox: list, objects: list) -> bool:
        if not objects:
            return False
        px1, py1, px2, py2 = person_bbox
        p_center_x = (px1 + px2) / 2
        p_bottom_y = py2

        for obj in objects:
            if not obj.get("is_cheating_object"):
                continue
            ox1, oy1, ox2, oy2 = obj["bbox"]
            o_center_x = (ox1 + ox2) / 2

            if abs(o_center_x - p_center_x) < 150 and oy1 < p_bottom_y:
                return True
        return False

    def analyze(self, frame, tracked_faces: list, objects: list | None = None) -> dict:
        results = []
        active_ids = set()

        w_gaze = self.W_GAZE_EXAM if self.exam_mode else self.W_GAZE
        w_pose = self.W_POSE_EXAM if self.exam_mode else self.W_POSE
        w_fatigue = self.W_FATIGUE_EXAM if self.exam_mode else self.W_FATIGUE

        for face in tracked_faces:
            bbox = face["bbox"]
            track_id = face["track_id"]
            active_ids.add(track_id)

            blink_state = self._blink_states.get(track_id, {"counter": 0, "total": 0})

            landmarker_result = self._detect_landmarks(frame, bbox)

            pose = self.pose_estimator.estimate(frame, bbox, landmarker_result)
            fatigue = self.fatigue_detector.detect(
                frame, bbox, landmarker_result, blink_state=blink_state
            )
            self._blink_states[track_id] = blink_state

            gaze_score = self._score_gaze_exam(pose) if self.exam_mode else self._score_gaze(pose)
            pose_score = self._score_pose(pose)
            fatigue_score = self._score_fatigue(fatigue)

            attention = (
                w_gaze * gaze_score
                + w_pose * pose_score
                + w_fatigue * fatigue_score
            )

            face_result = {
                "track_id": track_id,
                "bbox": bbox,
                "attention_score": round(attention, 1),
                "pose": pose,
                "fatigue": fatigue,
                "gaze_score": round(gaze_score, 1),
                "pose_score": round(pose_score, 1),
                "fatigue_score": round(fatigue_score, 1),
            }

            if self.exam_mode and self._exam_sm is not None:
                cheating_nearby = self._check_cheating_nearby(bbox, objects or [])
                exam_result = self._exam_sm.update(
                    track_id=track_id,
                    pitch=pose.get("pitch", 0),
                    yaw=pose.get("yaw", 0),
                    fatigue=fatigue,
                    cheating_nearby=cheating_nearby,
                )
                face_result["exam_risk"] = exam_result

            results.append(face_result)

        stale_ids = [tid for tid in self._blink_states if tid not in active_ids]
        for tid in stale_ids:
            del self._blink_states[tid]

        if self._exam_sm is not None:
            self._exam_sm.cleanup(active_ids)

        return {"faces": results, "count": len(results)}
