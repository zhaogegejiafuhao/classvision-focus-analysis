import asyncio
import json
import base64
import logging
from datetime import datetime, timedelta

import cv2
import numpy as np
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from sqlalchemy.orm import Session

from cv_engine.trackers.face_tracker import FaceTracker
from cv_engine.analyzers.attention_analyzer import AttentionAnalyzer
from cv_engine.face_recognizer import recognizer, json_to_embedding
from backend.core.database import SessionLocal
from backend.models.tables import Student, AttentionRecord, ExamRiskRecord, Classroom, RegisteredPerson

logger = logging.getLogger(__name__)

router = APIRouter()

tracker = FaceTracker()
_analyzers: dict[int, AttentionAnalyzer] = {}
_models_ready = False


def _warmup_models():
    """启动时预热模型，避免首次推理超时"""
    global _models_ready
    try:
        logger.info("正在预热 YOLO 模型...")
        dummy = np.zeros((480, 640, 3), dtype=np.uint8)
        tracker.model  # 触发 YOLO 模型加载
        tracker.track(dummy)  # 触发首次推理
        logger.info("YOLO 模型预热完成")

        logger.info("正在预热 FaceLandmarker...")
        analyzer = AttentionAnalyzer()
        analyzer.landmarker  # 触发 FaceLandmarker 模型加载
        logger.info("FaceLandmarker 预热完成")

        _models_ready = True
    except Exception as e:
        logger.warning(f"模型预热异常（不影响运行）: {e}")
        _models_ready = True


def _get_analyzer(classroom_id: int, exam_mode: bool) -> AttentionAnalyzer:
    if classroom_id not in _analyzers:
        _analyzers[classroom_id] = AttentionAnalyzer(exam_mode=exam_mode)
    return _analyzers[classroom_id]


# 已注册人脸库缓存（每60秒刷新一次）
_registered_persons_cache: list[tuple[int, str, np.ndarray]] = []
_cache_last_refresh: datetime = datetime.min


def _refresh_registered_persons_cache(db: Session):
    """刷新已注册人脸库缓存"""
    global _registered_persons_cache, _cache_last_refresh
    now = datetime.now()
    if now - _cache_last_refresh < timedelta(seconds=60):
        return  # 缓存未过期，无需刷新

    try:
        persons = db.query(RegisteredPerson).filter(RegisteredPerson.role == "student").all()
        _registered_persons_cache = [
            (p.id, p.name, json_to_embedding(p.face_embedding))
            for p in persons
        ]
        _cache_last_refresh = now
        logger.info(f"已注册人脸库缓存刷新，共 {len(_registered_persons_cache)} 人")
    except Exception as e:
        logger.error(f"刷新人脸库缓存失败: {e}")


def _match_face_identity(frame: np.ndarray, bbox: list[int]) -> tuple[int, str] | None:
    """在人脸库中匹配身份"""
    if len(_registered_persons_cache) == 0:
        return None

    try:
        embedding = recognizer.extract_embedding_from_bbox(frame, bbox)
        if embedding is None:
            return None

        return recognizer.match_face(embedding, _registered_persons_cache, threshold=0.5)
    except Exception as e:
        logger.error(f"人脸匹配失败: {e}")
        return None


def _process_frame(frame, classroom_id: int, exam_mode: bool):
    try:
        persons, objects = tracker.track(frame)
        analyzer = _get_analyzer(classroom_id, exam_mode)
        if exam_mode:
            results = analyzer.analyze(frame, persons, objects=objects)
        else:
            results = analyzer.analyze(frame, persons)
        results["objects"] = objects
        results["exam_mode"] = exam_mode

        # 尝试人脸身份匹配（仅对新学生）
        if len(_registered_persons_cache) > 0:
            for face in results.get("faces", []):
                bbox = face.get("bbox")
                if bbox:
                    match = _match_face_identity(frame, bbox)
                    if match:
                        face["matched_person_id"] = match[0]
                        face["matched_person_name"] = match[1]
    except Exception as e:
        logger.error(f"帧处理异常: {e}")
        results = {"faces": [], "count": 0, "objects": [], "exam_mode": exam_mode}
    return results


def _save_records(classroom_id: int, faces: list, exam_mode: bool):
    db: Session = SessionLocal()
    try:
        now = datetime.now()
        # 刷新人脸库缓存
        _refresh_registered_persons_cache(db)

        for face in faces:
            track_id = face["track_id"]
            student = db.query(Student).filter(
                Student.classroom_id == classroom_id,
                Student.track_id == track_id,
            ).first()

            if not student:
                stale = db.query(Student).filter(
                    Student.classroom_id == classroom_id,
                    Student.last_seen_at < now - timedelta(seconds=5),
                ).order_by(Student.last_seen_at.desc()).first()

                if stale:
                    stale.track_id = track_id
                    student = stale
                else:
                    # 创建新学生时，尝试绑定已注册身份
                    matched_person_id = face.get("matched_person_id")
                    matched_person_name = face.get("matched_person_name")
                    student = Student(
                        classroom_id=classroom_id,
                        track_id=track_id,
                        person_id=matched_person_id,
                        name=matched_person_name,  # 如果匹配到，设置姓名
                    )
                    db.add(student)
                    db.commit()
                    db.refresh(student)

            student.last_seen_at = now

            pose = face.get("pose", {})
            fatigue = face.get("fatigue", {})
            record = AttentionRecord(
                student_id=student.person_id or 0,
                student_record_id=student.id,
                classroom_id=classroom_id,
                attention_score=face["attention_score"],
                pitch=pose.get("pitch", 0),
                yaw=pose.get("yaw", 0),
                roll=pose.get("roll", 0),
                ear=fatigue.get("ear", 0),
                is_blinking=fatigue.get("is_blinking", False),
                blink_count=fatigue.get("blink_count", 0),
                gaze_score=face.get("gaze_score", 0),
                pose_score=face.get("pose_score", 0),
                fatigue_score=face.get("fatigue_score", 0),
            )
            db.add(record)

            if exam_mode and "exam_risk" in face:
                risk = face["exam_risk"]
                risk_record = ExamRiskRecord(
                    student_id=student.person_id or 0,
                    student_record_id=student.id,
                    classroom_id=classroom_id,
                    risk_level=risk["risk_level"],
                    gaze_deviation_duration=risk["gaze_deviation_duration"],
                    head_down_duration=risk["head_down_duration"],
                    head_turn_events=risk["head_turn_events"],
                    cheating_object_nearby=risk["cheating_object_nearby"],
                    attention_score=face["attention_score"],
                )
                db.add(risk_record)
        try:
            db.commit()
        except Exception as commit_err:
            logger.error(f"提交记录异常: {commit_err}")
            db.rollback()
    except Exception as e:
        logger.error(f"保存记录异常: {e}")
        try:
            db.rollback()
        except Exception:
            pass
    finally:
        db.close()


@router.websocket("/ws/video")
async def video_stream(
    ws: WebSocket,
    classroom_id: int = Query(default=1),
):
    await ws.accept()
    frame_seq = 0
    loop = asyncio.get_event_loop()

    try:
        db = SessionLocal()
        classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
        exam_mode = classroom.exam_mode if classroom else False
    finally:
        db.close()

    try:
        while True:
            data = await ws.receive_text()
            frame_data = json.loads(data)
            img_bytes = base64.b64decode(frame_data["frame"])
            img_array = np.frombuffer(img_bytes, dtype=np.uint8)
            frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            if frame is None:
                continue

            results = await loop.run_in_executor(
                None, _process_frame, frame, classroom_id, exam_mode
            )
            results["classroom_id"] = classroom_id
            results["frame_seq"] = frame_seq
            frame_seq += 1

            await ws.send_json(results)

            if frame_seq % 30 == 0 and results["faces"]:
                await loop.run_in_executor(
                    None, _save_records, classroom_id, results["faces"], exam_mode
                )
    except WebSocketDisconnect:
        _analyzers.pop(classroom_id, None)
    except Exception as e:
        logger.error(f"WebSocket 异常: {e}")
        _analyzers.pop(classroom_id, None)
