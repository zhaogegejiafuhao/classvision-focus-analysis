import asyncio
import json
import base64
import logging
import os
import threading
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

import cv2
import numpy as np
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from sqlalchemy.orm import Session

from cv_engine.trackers.face_tracker import FaceTracker
from cv_engine.analyzers.attention_analyzer import AttentionAnalyzer
from cv_engine.face_recognizer import recognizer, json_to_embedding
from backend.core.database import SessionLocal
from backend.models.tables import Student, AttentionRecord, ExamRiskRecord, Classroom, RegisteredPerson, CheatingRecord

logger = logging.getLogger(__name__)

router = APIRouter()

tracker = FaceTracker()
_analyzers: dict[int, AttentionAnalyzer] = {}
_models_ready = False

# 专用线程池：帧处理、DB 保存、违规检测 三者分离
# 💡 增加 worker 数避免长时间运行后排队；max_workers=4 帧处理 + 2 save + 2 violation
_frame_executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="cv-frame")
_save_executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="cv-save")
_violation_executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="cv-violation")

# ── 违规检测全局变量 ──
STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "cheating_proofs")
os.makedirs(STATIC_DIR, exist_ok=True)

VIOLATION_COOLDOWN_MAP = {}       # {(classroom_id, student_id, violation_type): datetime}
COOLDOWN_SECONDS = 5             # 同一学生同类型违规冷却时间（秒）

VIOLATION_FRAME_COUNTER = {}     # {(classroom_id, track_id, violation_type): count}  能量槽
TRIGGER_FRAME_THRESHOLD = 8      # 能量槽触发阈值（帧数）

ALERT_COOLDOWN_MAP = {}          # {(classroom_id, student_id, violation_type): datetime} 弹窗冷却
ALERT_COOLDOWN_SECONDS = 10      # 弹窗冷却时间（秒）

# 全局字典清理阈值
_COUNTER_CLEANUP_INTERVAL = 100  # 每 N 帧清理一次全局计数器
_frame_cleanup_counter = 0

# 默认 student_id（当未识别到人脸时使用），保证 AttentionRecord.student_id NOT NULL 约束不失败
# 优先用 admin 用户的 id；若 db 中无 admin，则取第一个 RegisteredPerson 的 id；最坏情况为 1
_DEFAULT_STUDENT_ID_CACHE: int | None = None


def _get_default_student_id() -> int:
    """获取默认 student_id（未识别到人脸时填充 AttentionRecord.student_id）"""
    global _DEFAULT_STUDENT_ID_CACHE
    if _DEFAULT_STUDENT_ID_CACHE is not None:
        return _DEFAULT_STUDENT_ID_CACHE
    try:
        db = SessionLocal()
        admin = db.query(RegisteredPerson).filter(RegisteredPerson.role == "admin").first()
        if not admin:
            any_user = db.query(RegisteredPerson).first()
            _DEFAULT_STUDENT_ID_CACHE = any_user.id if any_user else 1
        else:
            _DEFAULT_STUDENT_ID_CACHE = admin.id
        db.close()
    except Exception:
        _DEFAULT_STUDENT_ID_CACHE = 1
    return _DEFAULT_STUDENT_ID_CACHE


def _warmup_models():
    """启动时预热模型，避免首次推理超时"""
    global _models_ready
    try:
        logger.info("正在预热 YOLO 模型...")
        dummy = np.zeros((480, 640, 3), dtype=np.uint8)
        tracker.model  # 触发 YOLO 模型加载
        tracker.track(dummy)  # 触发首次推理
        logger.info("YOLO 模型预热完成")
    except Exception as e:
        logger.warning(f"YOLO 预热异常: {e}")

    try:
        logger.info("正在预热 FaceLandmarker...")
        analyzer = AttentionAnalyzer()
        analyzer.landmarker  # 触发 FaceLandmarker 模型加载
        logger.info("FaceLandmarker 预热完成")
    except Exception as e:
        logger.warning(f"FaceLandmarker 预热异常: {e}")

    try:
        logger.info("正在预热 InsightFace (face_recognizer)...")
        recognizer.app  # 触发 InsightFace 模型加载（仅加载模型，不运行推理）
        logger.info("InsightFace 模型加载完成")
    except Exception as e:
        logger.warning(f"InsightFace 预热异常: {e}")

    _models_ready = True


def _get_analyzer(classroom_id: int, exam_mode: bool) -> AttentionAnalyzer:
    if classroom_id not in _analyzers:
        _analyzers[classroom_id] = AttentionAnalyzer(exam_mode=exam_mode)
    return _analyzers[classroom_id]


# 已注册人脸库缓存（每60秒刷新一次）
_registered_persons_cache: list[tuple[int, str, np.ndarray]] = []
_cache_last_refresh: datetime = datetime.min
_cache_lock = threading.Lock()

# 💡 关键性能优化：track_id -> (person_id, person_name) 映射
# 同一个 track_id 第一次识别后，后续帧直接复用，避免每帧都做 InsightFace 推理
_track_identity_cache: dict[int, tuple[int, str, float]] = {}  # track_id -> (person_id, name, last_match_time)
_track_identity_lock = threading.Lock()
_TRACK_IDENTITY_TTL = 600  # 10 分钟过期（即使 track_id 复用也能重新识别）


def _refresh_registered_persons_cache(db: Session):
    """刷新已注册人脸库缓存（线程安全）"""
    global _registered_persons_cache, _cache_last_refresh
    now = datetime.now()
    if now - _cache_last_refresh < timedelta(seconds=60):
        return  # 缓存未过期，无需刷新

    try:
        persons = db.query(RegisteredPerson).filter(RegisteredPerson.role == "student").all()
        new_cache = [
            (p.id, p.name, json_to_embedding(p.face_embedding))
            for p in persons
            if p.face_embedding  # 只缓存有 embedding 的已注册人员
        ]
        with _cache_lock:
            _registered_persons_cache = new_cache
            _cache_last_refresh = now
        logger.info(f"已注册人脸库缓存刷新，共 {len(new_cache)} 人")
    except Exception as e:
        logger.error(f"刷新人脸库缓存失败: {e}")


def _match_face_identity(frame: np.ndarray, bbox: list[int]) -> tuple[int, str] | None:
    """在人脸库中匹配身份"""
    with _cache_lock:
        cache = list(_registered_persons_cache)
    if len(cache) == 0:
        return None

    try:
        embedding = recognizer.extract_embedding_from_bbox(frame, bbox)
        if embedding is None:
            return None

        return recognizer.match_face(embedding, cache, threshold=0.5)
    except Exception as e:
        logger.error(f"人脸匹配失败: {e}")
        return None


def _match_face_with_track_cache(track_id: int, frame: np.ndarray, bbox: list[int]) -> tuple[int, str] | None:
    """带 track_id 缓存的人脸匹配：同一 track_id 10 分钟内只做一次 InsightFace 推理"""
    now_ts = datetime.now().timestamp()
    with _track_identity_lock:
        cached = _track_identity_cache.get(track_id)
        if cached and (now_ts - cached[2]) < _TRACK_IDENTITY_TTL:
            # 缓存命中：直接返回
            return (cached[0], cached[1])

    # 缓存未命中：做 InsightFace 推理
    result = _match_face_identity(frame, bbox)
    if result is not None:
        with _track_identity_lock:
            _track_identity_cache[track_id] = (result[0], result[1], now_ts)
    return result


def _cleanup_track_cache(active_track_ids: set[int]):
    """清理已断开 track 的缓存，避免内存泄漏"""
    with _track_identity_lock:
        stale = [tid for tid in _track_identity_cache if tid not in active_track_ids]
        for tid in stale:
            _track_identity_cache.pop(tid, None)
        # 兜底：超过 1000 条强制清空
        if len(_track_identity_cache) > 1000:
            _track_identity_cache.clear()


def _cleanup_global_counters(classroom_id: int):
    """定期清理已断开课堂的全局计数器，防止内存泄漏"""
    now = datetime.now()
    # 清理 ALERT_COOLDOWN_MAP（超过 60 秒的条目）
    stale_keys = [k for k, v in ALERT_COOLDOWN_MAP.items()
                  if (now - v).total_seconds() > 60]
    for k in stale_keys:
        ALERT_COOLDOWN_MAP.pop(k, None)

    # 清理 VIOLATION_FRAME_COUNTER（非活跃 track_id）
    active_keys = [k for k in VIOLATION_FRAME_COUNTER if k[0] == classroom_id]
    # 只保留当前课堂的，其他的如果在 5 分钟内无更新就清除
    # 简单策略：如果总数超过 200 条就清理非当前课堂的
    if len(VIOLATION_FRAME_COUNTER) > 200:
        VIOLATION_FRAME_COUNTER.clear()


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

        # 尝试人脸身份匹配（带 track_id 缓存，避免每帧重复推理）
        with _cache_lock:
            has_cache = len(_registered_persons_cache) > 0
        if has_cache:
            for face in results.get("faces", []):
                bbox = face.get("bbox")
                track_id = face.get("track_id")
                if bbox and track_id is not None:
                    # 💡 使用带缓存的匹配：同一 track_id 10 分钟内只做一次 InsightFace 推理
                    match = _match_face_with_track_cache(track_id, frame, bbox)
                    if match:
                        face["matched_person_id"] = match[0]
                        face["matched_person_name"] = match[1]
    except Exception as e:
        logger.error(f"帧处理异常: {e}")
        results = {"faces": [], "count": 0, "objects": [], "exam_mode": exam_mode}
    return results


def _check_and_save_violations(classroom_id: int, faces: list, frame: np.ndarray) -> list:
    """违规检测与抓拍：时序防抖 + 能量槽 + 冷却期 + 实时抓拍

    注意：此函数在 _violation_executor 线程池中执行，不阻塞帧处理。
    """
    db: Session = SessionLocal()
    triggered_events = []
    current_time = datetime.now()

    # 清理离线目标的能量槽计数器
    active_track_ids = [face["track_id"] for face in faces]
    for key in list(VIOLATION_FRAME_COUNTER.keys()):
        if key[0] == classroom_id and key[1] not in active_track_ids:
            VIOLATION_FRAME_COUNTER.pop(key, None)

    try:
        for face in faces:
            track_id = face["track_id"]
            gaze_score = face.get("gaze_score", 100)
            pose_score = face.get("pose_score", 100)

            # 1. 判定线：确凿违规 vs 轻微抖动缓冲区
            violation_type = None
            if gaze_score < 45:
                violation_type = "GAZE_DEVIATION"
            elif pose_score < 45:
                violation_type = "HEAD_DOWN_LONG"

            # 2. 时序平滑防抖机制
            gaze_key = (classroom_id, track_id, "GAZE_DEVIATION")
            pose_key = (classroom_id, track_id, "HEAD_DOWN_LONG")

            if violation_type:
                # 确凿违规：能量槽 +1
                counter_key = (classroom_id, track_id, violation_type)
                VIOLATION_FRAME_COUNTER[counter_key] = VIOLATION_FRAME_COUNTER.get(counter_key, 0) + 1

                if VIOLATION_FRAME_COUNTER[counter_key] >= TRIGGER_FRAME_THRESHOLD:
                    # 能量槽满 → 查找/创建学生记录
                    student = db.query(Student).filter(
                        Student.classroom_id == classroom_id,
                        Student.track_id == track_id,
                    ).first()
                    if not student:
                        matched_person_id = face.get("matched_person_id")
                        # 💡 核心修复：未识别到人脸时也必须有 person_id，否则 AttentionRecord.student_id NOT NULL 约束会失败
                        if not matched_person_id:
                            matched_person_id = _get_default_student_id()
                        matched_person_name = face.get("matched_person_name")
                        student = Student(
                            classroom_id=classroom_id,
                            track_id=track_id,
                            person_id=matched_person_id,
                            name=matched_person_name,
                        )
                        db.add(student)
                        db.commit()
                        db.refresh(student)

                    # 弹窗频率控制
                    alert_key = (classroom_id, student.id, violation_type)
                    if alert_key in ALERT_COOLDOWN_MAP:
                        last_alert_time = ALERT_COOLDOWN_MAP[alert_key]
                        if (current_time - last_alert_time).total_seconds() < ALERT_COOLDOWN_SECONDS:
                            continue

                    ALERT_COOLDOWN_MAP[alert_key] = current_time

                    # 实时抓拍（异步写入，不阻塞主线程）
                    try:
                        timestamp_str = current_time.strftime("%Y%m%d_%H%M%S_%f")
                        filename = f"cls_{classroom_id}_st_{student.id}_{timestamp_str}.jpg"
                        filepath = os.path.join(STATIC_DIR, filename)
                        cv2.imwrite(filepath, frame)
                        web_image_path = f"/static/cheating_proofs/{filename}"
                    except Exception as write_err:
                        logger.error(f"抓拍图片写入失败: {write_err}")
                        web_image_path = ""

                    # 写入数据库
                    cheating_record = CheatingRecord(
                        classroom_id=classroom_id,
                        student_id=student.id,
                        violation_type=violation_type,
                        image_path=web_image_path,
                        gaze_score=gaze_score,
                        pose_score=pose_score,
                        timestamp=current_time,
                    )
                    db.add(cheating_record)
                    db.commit()
                    db.refresh(cheating_record)

                    # 塞入实时流
                    triggered_events.append({
                        "student_id": student.id,
                        "track_id": track_id,
                        "violation_type": violation_type,
                        "image_path": web_image_path,
                        "gaze_score": gaze_score,
                        "pose_score": pose_score,
                        "timestamp": cheating_record.timestamp.isoformat(),
                    })

                    # 能量槽清零
                    VIOLATION_FRAME_COUNTER[counter_key] = 0

            else:
                # 正常帧：时序消融（每帧扣减2，允许偶尔正常帧穿插）
                if gaze_score >= 55:
                    if gaze_key in VIOLATION_FRAME_COUNTER:
                        VIOLATION_FRAME_COUNTER[gaze_key] = max(0, VIOLATION_FRAME_COUNTER[gaze_key] - 2)
                        if VIOLATION_FRAME_COUNTER[gaze_key] == 0:
                            VIOLATION_FRAME_COUNTER.pop(gaze_key, None)

                if pose_score >= 58:
                    if pose_key in VIOLATION_FRAME_COUNTER:
                        VIOLATION_FRAME_COUNTER[pose_key] = max(0, VIOLATION_FRAME_COUNTER[pose_key] - 2)
                        if VIOLATION_FRAME_COUNTER[pose_key] == 0:
                            VIOLATION_FRAME_COUNTER.pop(pose_key, None)

        return triggered_events
    except Exception as e:
        logger.error(f"违规检测异常: {e}")
        return triggered_events
    finally:
        db.close()


def _save_records(classroom_id: int, faces: list, exam_mode: bool):
    """保存注意力记录到数据库（在专用线程中执行，不阻塞帧处理）"""
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
                    matched_person_id = face.get("matched_person_id")
                    # 💡 核心修复：未识别到人脸时也必须有 person_id，否则 AttentionRecord.student_id NOT NULL 约束会失败
                    if not matched_person_id:
                        matched_person_id = _get_default_student_id()
                    matched_person_name = face.get("matched_person_name")
                    student = Student(
                        classroom_id=classroom_id,
                        track_id=track_id,
                        person_id=matched_person_id,
                        name=matched_person_name,
                    )
                    db.add(student)
                    db.commit()
                    db.refresh(student)

            student.last_seen_at = now

            pose = face.get("pose", {})
            fatigue = face.get("fatigue", {})
            person_id_for_fk = student.person_id if student.person_id else _get_default_student_id()
            record = AttentionRecord(
                student_id=person_id_for_fk,
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
                    student_id=person_id_for_fk,
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

        # 重试机制：SQLite 锁冲突时重试
        for attempt in range(3):
            try:
                db.commit()
                break
            except Exception as commit_err:
                if attempt < 2:
                    logger.warning(f"提交记录重试 {attempt+1}/3: {commit_err}")
                    db.rollback()
                    import time
                    time.sleep(0.1 * (attempt + 1))
                else:
                    logger.error(f"提交记录失败(3次重试后): {commit_err}")
                    db.rollback()
    except Exception as e:
        logger.error(f"保存记录异常: {e}")
        try:
            db.rollback()
        except Exception:
            pass
    finally:
        db.close()


@router.get("/api/cheating_records/{classroom_id}")
def get_cheating_records(classroom_id: int):
    """查询违规记录（联表 Student 获取 track_id）"""
    db: Session = SessionLocal()
    try:
        results = db.query(CheatingRecord, Student.track_id).join(
            Student, CheatingRecord.student_id == Student.id
        ).filter(
            CheatingRecord.classroom_id == classroom_id
        ).order_by(CheatingRecord.timestamp.desc()).all()

        return [{
            "id": r.CheatingRecord.id,
            "student_id": r.CheatingRecord.student_id,
            "track_id": r.track_id,
            "violation_type": r.CheatingRecord.violation_type,
            "image_path": r.CheatingRecord.image_path,
            "gaze_score": r.CheatingRecord.gaze_score,
            "pose_score": r.CheatingRecord.pose_score,
            "timestamp": r.CheatingRecord.timestamp.isoformat(),
        } for r in results]
    finally:
        db.close()


@router.websocket("/ws/video")
async def video_stream(
    ws: WebSocket,
    classroom_id: int = Query(default=1),
    exam_id: int = Query(default=None),
):
    await ws.accept()
    frame_seq = 0
    loop = asyncio.get_event_loop()
    global _frame_cleanup_counter

    try:
        db = SessionLocal()
        classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
        exam_mode = classroom.exam_mode if classroom else False
    finally:
        db.close()

    # ── 关键变量 ──
    _latest_violation_events = []  # 最近一次违规检测结果
    _pending_save_futures = []  # 跟踪保存任务的 future，确保结束前完成

    # 💡 关键性能优化：帧序号快照，用于跨 await 检查当前帧是否已过期
    # 当后端处理速度跟不上时（>200ms），前端会发送新帧覆盖当前帧
    # 避免积压导致内存爆炸
    _latest_frame_seq = 0
    _processing_lag = 0  # 处理滞后帧数（仅做监控）

    try:
        while True:
            data = await ws.receive_text()
            frame_data = json.loads(data)
            img_bytes = base64.b64decode(frame_data["frame"])
            img_array = np.frombuffer(img_bytes, dtype=np.uint8)
            frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            if frame is None:
                continue

            frame_seq += 1

            # ① 帧处理：使用专用线程池
            # 💡 注意：为了让前端能更实时，我们不等 frame_process 完成
            # 但要等 results 出来后才能 send_json，因此仍需要 await
            results = await loop.run_in_executor(
                _frame_executor, _process_frame, frame, classroom_id, exam_mode
            )
            results["classroom_id"] = classroom_id
            results["frame_seq"] = frame_seq

            # ② 违规检测：每2帧检测一次（保证实时性，同时控制CPU负载）
            #    先获取上一轮违规检测的结果
            results["cheating_events"] = list(_latest_violation_events)
            _latest_violation_events.clear()

            if results["faces"] and frame_seq % 2 == 0:
                faces_copy = json.loads(json.dumps(results["faces"]))

                def _violation_task():
                    return _check_and_save_violations(classroom_id, faces_copy, frame)

                future = loop.run_in_executor(_violation_executor, _violation_task)
                def _on_violation_done(fut):
                    try:
                        events = fut.result()
                        _latest_violation_events.extend(events)
                    except Exception as e:
                        logger.warning(f"违规检测回调异常: {e}")
                future.add_done_callback(_on_violation_done)

            # 立即发送结果
            await ws.send_json(results)

            # ③ 每30帧保存一次记录（约6秒），避免频繁写DB导致锁竞争和冻结
            if frame_seq % 30 == 0 and results["faces"]:
                faces_snapshot = json.loads(json.dumps(results["faces"]))
                save_future = loop.run_in_executor(
                    _save_executor, _save_records, classroom_id, faces_snapshot, exam_mode
                )
                _pending_save_futures.append(save_future)
                # 清理已完成的 future，防止列表无限增长
                _pending_save_futures = [f for f in _pending_save_futures if not f.done()]

            # ④ 定期清理全局计数器
            _frame_cleanup_counter += 1
            if _frame_cleanup_counter % _COUNTER_CLEANUP_INTERVAL == 0:
                _cleanup_global_counters(classroom_id)
                # 💡 同时清理已断开 track 的身份缓存
                active_track_ids = {f.get("track_id") for f in results.get("faces", []) if f.get("track_id") is not None}
                _cleanup_track_cache(active_track_ids)

    except WebSocketDisconnect:
        # WebSocket 断开时，等待所有正在执行的 DB 保存任务完成
        if _pending_save_futures:
            logger.info(f"WebSocket 断开，等待 {_pending_save_futures.__len__()} 个保存任务完成...")
            try:
                await asyncio.gather(*_pending_save_futures, return_exceptions=True)
                logger.info("所有保存任务已完成")
            except Exception as e:
                logger.warning(f"等待保存任务异常: {e}")

        _analyzers.pop(classroom_id, None)
        # 清理该课堂的全局计数器
        for key in list(VIOLATION_FRAME_COUNTER.keys()):
            if key[0] == classroom_id:
                VIOLATION_FRAME_COUNTER.pop(key, None)
        for key in list(ALERT_COOLDOWN_MAP.keys()):
            if key[0] == classroom_id:
                ALERT_COOLDOWN_MAP.pop(key, None)
    except Exception as e:
        logger.error(f"WebSocket 异常: {e}")
        _analyzers.pop(classroom_id, None)
