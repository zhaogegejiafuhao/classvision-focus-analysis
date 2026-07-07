import asyncio
import json
import base64
from datetime import datetime, timedelta

import cv2
import numpy as np
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from sqlalchemy.orm import Session

from cv_engine.trackers.face_tracker import FaceTracker
from cv_engine.analyzers.attention_analyzer import AttentionAnalyzer
from backend.core.database import SessionLocal
from backend.models.tables import Student, AttentionRecord

router = APIRouter()

tracker = FaceTracker()
analyzer = AttentionAnalyzer()


def _process_frame(frame):
    tracked = tracker.track(frame)
    results = analyzer.analyze(frame, tracked)
    return tracked, results


def _save_records(classroom_id: int, faces: list):
    db: Session = SessionLocal()
    try:
        now = datetime.now()
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
                    student = Student(classroom_id=classroom_id, track_id=track_id)
                    db.add(student)
                    db.commit()
                    db.refresh(student)

            student.last_seen_at = now

            pose = face.get("pose", {})
            fatigue = face.get("fatigue", {})
            record = AttentionRecord(
                student_id=student.id,
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
        db.commit()
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
        while True:
            data = await ws.receive_text()
            frame_data = json.loads(data)
            img_bytes = base64.b64decode(frame_data["frame"])
            img_array = np.frombuffer(img_bytes, dtype=np.uint8)
            frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            if frame is None:
                continue

            tracked, results = await loop.run_in_executor(
                None, _process_frame, frame
            )
            results["classroom_id"] = classroom_id
            results["frame_seq"] = frame_seq
            frame_seq += 1

            await ws.send_json(results)

            if frame_seq % 30 == 0 and results["faces"]:
                await loop.run_in_executor(
                    None, _save_records, classroom_id, results["faces"]
                )
    except WebSocketDisconnect:
        pass
