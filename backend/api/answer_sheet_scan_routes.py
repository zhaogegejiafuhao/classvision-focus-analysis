"""答题卡扫描识别路由（从 answer_sheet_routes.py 拆分）"""
import os
import json
import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import func as sa_func
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_owner_or_admin
from backend.models.tables import RegisteredPerson, Exam, Question
from backend.services.answer_sheet import answer_sheet_orchestrator
from backend.services.paper_template import paper_template_service
from cv_engine.detectors.answer_card_detector import answer_card_detector

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/answer-sheet", tags=["answer-sheet"])

SCAN_UPLOAD_DIR = "uploads/answer_sheets"
os.makedirs(SCAN_UPLOAD_DIR, exist_ok=True)

# 单批最大扫描文件数（防止一次性上传过多导致 OOM/超时）
_MAX_BATCH_FILES = 50

# 允许的图片扩展名
_ALLOWED_IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".bmp", ".webp")


@router.post("/scan/{exam_id}")
async def scan_paper(
    exam_id: int,
    file: UploadFile = File(...),
    student_id: int = Form(...),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """扫描整卷 → 按模板切分 → 自动批改 → 返回报告

    权限：仅教师/管理员可调用（教师代学生上传答卷）
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可调用此接口")

    # 校验考试存在且属于当前教师
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, f"考试 {exam_id} 不存在")
    assert_owner_or_admin(exam.teacher_id, current_user)

    # 读取图片
    image_bytes = await file.read()
    if not image_bytes:
        raise HTTPException(400, "图片内容为空")

    # 校验图片格式
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in (".png", ".jpg", ".jpeg", ".bmp", ".webp"):
        raise HTTPException(400, f"不支持的图片格式: {ext}")

    # 调用编排器
    try:
        result = await answer_sheet_orchestrator.scan_and_grade(
            db=db,
            exam_id=exam_id,
            student_id=student_id,
            paper_image_bytes=image_bytes,
        )
    except ValueError as e:
        raise HTTPException(400, str(e))
    except Exception as e:
        logger.exception(f"[AnswerSheetRoute] scan_paper 异常: {e}")
        raise HTTPException(500, f"扫描批改失败: {e}")

    # 序列化结果
    return _serialize_scan_result(result)



@router.post("/detect-bubbles")
async def detect_bubbles_only(
    file: UploadFile = File(...),
    template_type: str = Form("standard_5x10x4"),
    current_user: RegisteredPerson = Depends(get_current_user),
):
    """独立气泡检测（调试用）

    上传一张答题卡图片，返回检测到的答案 + 调试可视化图
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可调用")

    image_bytes = await file.read()
    if not image_bytes:
        raise HTTPException(400, "图片内容为空")

    result = answer_card_detector.detect(image_bytes, template_type=template_type)

    if result.error:
        raise HTTPException(400, f"检测失败: {result.error}")

    return {
        "template_type": result.template_type,
        "skew_angle": result.skew_angle,
        "bubbles_count": len(result.bubbles),
        "filled_count": sum(1 for b in result.bubbles if b.filled),
        "answers": {str(k): v for k, v in result.answers.items()},
        "bubbles": [
            {
                "question_index": b.question_index,
                "option_index": b.option_index,
                "filled": b.filled,
                "fill_ratio": round(b.fill_ratio, 3),
                "center": b.center,
                "radius": b.radius,
            }
            for b in result.bubbles
        ],
        "debug_image_b64": result.debug_image_b64,
    }



@router.post("/scan-batch/{exam_id}")
async def scan_batch(
    exam_id: int,
    files: list[UploadFile] = File(...),
    student_ids: str = Form(...),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """A. 多学生批量扫描批改

    教师一次上传 N 份答卷 + 对应的 student_id 列表，系统顺序调用 scan_and_grade，
    单个学生失败不阻塞其他学生，最终返回汇总结果。

    Args:
        exam_id: 考试 ID
        files: 多份答卷图片（PNG/JPG/JPEG/BMP/WEBP），顺序与 student_ids 对应
        student_ids: 逗号分隔的学生 ID 列表（RegisteredPerson.id），与 files 顺序一一对应

    Returns:
        {
            exam_id, total, success, failed,
            results: [{student_id, student_name, submission_id?, total_score?,
                       max_score?, success, error?, file_name}]
        }
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可批量扫描批改")

    # 校验文件数
    if not files:
        raise HTTPException(400, "未上传任何文件")
    if len(files) > _MAX_BATCH_FILES:
        raise HTTPException(400, f"单批最多 {_MAX_BATCH_FILES} 份答卷，当前 {len(files)} 份")

    # 解析 student_ids
    try:
        sid_list = [int(s.strip()) for s in student_ids.split(",") if s.strip()]
    except ValueError:
        raise HTTPException(400, "student_ids 格式错误，需为逗号分隔的整数列表")

    if len(sid_list) != len(files):
        raise HTTPException(
            400,
            f"文件数 ({len(files)}) 与学生数 ({len(sid_list)}) 不一致"
        )

    # 校验考试存在 + 归属
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, f"考试 {exam_id} 不存在")
    assert_owner_or_admin(exam.teacher_id, current_user)

    # 预加载学生姓名（避免循环内反复查询）
    from backend.models.tables import RegisteredPerson as _RP
    students_map = {
        s.id: s.name
        for s in db.query(_RP).filter(_RP.id.in_(sid_list)).all()
    }

    # 顺序处理每份答卷
    results: list[dict] = []
    success_count = 0
    failed_count = 0

    for idx, (file, sid) in enumerate(zip(files, sid_list), start=1):
        file_name = file.filename or f"file_{idx}"
        student_name = students_map.get(sid, f"用户#{sid}")
        result_entry: dict = {
            "index": idx,
            "student_id": sid,
            "student_name": student_name,
            "file_name": file_name,
            "success": False,
        }

        # 校验 student_id 存在
        if sid not in students_map:
            result_entry["error"] = f"学生 ID {sid} 不存在"
            results.append(result_entry)
            failed_count += 1
            continue

        # 校验图片格式
        ext = os.path.splitext(file_name)[1].lower()
        if ext not in _ALLOWED_IMAGE_EXTS:
            result_entry["error"] = f"不支持的图片格式: {ext}"
            results.append(result_entry)
            failed_count += 1
            continue

        # 读取图片
        try:
            image_bytes = await file.read()
        except Exception as e:
            result_entry["error"] = f"读取文件失败: {type(e).__name__}: {e}"
            results.append(result_entry)
            failed_count += 1
            continue

        if not image_bytes:
            result_entry["error"] = "图片内容为空"
            results.append(result_entry)
            failed_count += 1
            continue

        # 调用编排器（失败不阻塞下一个学生）
        try:
            scan_result = await answer_sheet_orchestrator.scan_and_grade(
                db=db,
                exam_id=exam_id,
                student_id=sid,
                paper_image_bytes=image_bytes,
            )
            result_entry.update({
                "success": True,
                "submission_id": scan_result.submission_id,
                "total_score": scan_result.total_score,
                "max_score": scan_result.max_score,
                "question_count": len(scan_result.question_results),
                "attribution": scan_result.attribution,
            })
            success_count += 1
        except ValueError as e:
            # 业务校验失败（如模板未配置、试卷切分失败）
            db.rollback()
            result_entry["error"] = f"业务错误: {e}"
            results.append(result_entry)
            failed_count += 1
            logger.warning(
                f"[AnswerSheetRoute] 批量批改失败 exam={exam_id} student={sid} file={file_name}: {e}"
            )
            continue
        except Exception as e:
            # 其他异常（OCR/LLM/DB）
            db.rollback()
            result_entry["error"] = f"{type(e).__name__}: {e}"
            results.append(result_entry)
            failed_count += 1
            logger.exception(
                f"[AnswerSheetRoute] 批量批改异常 exam={exam_id} student={sid} file={file_name}: {e}"
            )
            continue

        results.append(result_entry)

    logger.info(
        f"[AnswerSheetRoute] 批量扫描批改完成: exam_id={exam_id}, "
        f"total={len(results)}, success={success_count}, failed={failed_count}"
    )

    return {
        "exam_id": exam_id,
        "exam_title": exam.title,
        "total": len(results),
        "success": success_count,
        "failed": failed_count,
        "results": results,
    }



def _serialize_scan_result(result) -> dict:
    """把 PaperScanResult dataclass 序列化为 JSON 可序列化字典"""
    return {
        "submission_id": result.submission_id,
        "exam_id": result.exam_id,
        "student_id": result.student_id,
        "student_name": result.student_name,
        "total_score": result.total_score,
        "max_score": result.max_score,
        "question_results": [
            {
                "question_id": r.question_id,
                "question_type": r.question_type,
                "question_content": r.question_content,
                "region_type": r.region_type,
                "student_answer": r.student_answer,
                "standard_answer": r.standard_answer,
                "score": r.score,
                "max_score": r.max_score,
                "is_correct": r.is_correct,
                "comment": r.comment,
                "confidence": r.confidence,
                "ocr_text": r.ocr_text,
                "error": r.error,
                "grading_detail": r.grading_detail,
            }
            for r in result.question_results
        ],
        "summary": result.summary,
        "debug_image_b64": result.debug_image_b64,
        "attribution": result.attribution,
    }

