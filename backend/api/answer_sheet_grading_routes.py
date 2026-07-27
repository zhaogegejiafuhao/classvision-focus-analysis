"""答题卡重批改路由（从原 answer_sheet_grading_routes.py 拆分）

拆分后的模块：
- answer_sheet_grading_routes.py：人工补录答案、大题/作文 LLM 重批改、重批改历史查询
- answer_sheet_export_routes.py：单份/批量 Excel 报告导出
"""
import json
import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import RegisteredPerson, Exam, Question

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/answer-sheet", tags=["answer-sheet"])


@router.post("/submissions/{submission_id}/questions/{question_id}/manual-input")
def manual_input_answer(
    submission_id: int,
    question_id: int,
    student_answer: str = Form(...),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """教师人工补录学生答案并重新判分（D 方案）

    场景：当 OCR 双引擎均失败 needs_manual_input=True、或 OCR 置信度过低
    导致 is_correct=None 时，教师查看扫描件后手动输入学生答案，
    系统重新调 auto_grade 判分并更新 Answer 表 + Submission 总分。

    权限：仅教师/管理员（且必须是该 submission 所属考试的教师）

    流程：
    1. 校验 submission 存在 + 当前用户是该考试的教师
    2. 校验 question 存在 + 属于该考试
    3. 调 auto_grade(question, student_answer) 重新判分
       - 填空题：会走 A+B 方案（多空拆分 + 数值/单位容差）
       - 选择/判断题：常规精确匹配
       - 大题：返回 (0, False)，大题应走 LLM 重批改接口
    4. 更新或新建 Answer 记录（content/score/is_correct）
    5. 重新计算 submission 总分（所有 answers 的 score 之和）
    6. 更新 submission.graded_at
    7. 返回更新后的批改结果
    """
    from datetime import datetime
    from backend.models.tables import ExamSubmission, Answer

    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可调用此接口")

    # 1. 校验 submission
    submission = db.query(ExamSubmission).filter(ExamSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(404, f"提交 {submission_id} 不存在")

    # 2. 校验当前用户是该 submission 所属考试的教师
    exam = db.query(Exam).filter(Exam.id == submission.exam_id).first()
    if not exam:
        raise HTTPException(404, "提交关联的考试不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权操作此提交（仅该考试的教师可操作）")

    # 3. 校验 question 存在 + 属于该考试
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(404, f"题目 {question_id} 不存在")
    if question.exam_id != submission.exam_id:
        raise HTTPException(400, "题目不属于该提交对应的考试")

    # 4. 大题不支持人工补录（应走 LLM 重批改）
    if question.type == "essay":
        raise HTTPException(
            400,
            "大题/作文不支持人工补录答案，请使用 LLM 重批改接口"
        )

    # 5. 规范化输入
    student_answer = (student_answer or "").strip()
    if not student_answer:
        raise HTTPException(400, "学生答案不能为空")

    # 6. 调 auto_grade 重新判分（填空题会走 A+B 方案）
    from backend.services.exam_service import auto_grade
    score, is_correct = auto_grade(question, student_answer)

    # 7. 更新或新建 Answer（先捕获 before 值用于历史记录）
    answer = db.query(Answer).filter(
        Answer.submission_id == submission_id,
        Answer.question_id == question_id,
    ).first()

    # F 方案：捕获重批改前的状态用于历史记录
    before_score = answer.score if answer else None
    before_is_correct = answer.is_correct if answer else None
    before_total_score = submission.score

    if answer:
        answer.content = student_answer
        answer.score = score
        answer.is_correct = is_correct
    else:
        answer = Answer(
            submission_id=submission_id,
            question_id=question_id,
            content=student_answer,
            score=score,
            is_correct=is_correct,
        )
        db.add(answer)

    # 8. 重新计算 submission 总分
    all_answers = db.query(Answer).filter(Answer.submission_id == submission_id).all()
    total_score = sum((a.score or 0) for a in all_answers)
    submission.score = total_score
    submission.graded_at = datetime.now()
    if submission.status != "graded":
        submission.status = "graded"

    # 9. F 方案：写入重批改历史记录（与 Answer 同事务提交）
    from backend.models.tables import AnswerRegradeHistory
    history = AnswerRegradeHistory(
        submission_id=submission_id,
        question_id=question_id,
        operator_id=current_user.id,
        regrade_method="manual_input",
        input_mode=None,
        force_essay=False,
        before_score=before_score,
        after_score=float(score),
        before_is_correct=before_is_correct,
        after_is_correct=is_correct,
        max_score=float(question.score),
        before_total_score=before_total_score,
        after_total_score=float(total_score),
        student_text=student_answer,
        is_essay=False,
        model_key=None,
        grading_method=None,
        error_cause=None,
        knowledge_points_json=None,
        grading_json=None,
        writing_attribution_json=None,
        comment=None,
    )
    db.add(history)

    db.commit()

    logger.info(
        f"[ManualInput] teacher={current_user.id} submission={submission_id} "
        f"question={question_id} answer={student_answer!r} → score={score}/{question.score}"
    )

    return {
        "submission_id": submission_id,
        "question_id": question_id,
        "student_answer": student_answer,
        "standard_answer": question.answer,
        "score": score,
        "max_score": question.score,
        "is_correct": is_correct,
        "total_score": total_score,
        "manual_input": True,
        "graded_at": submission.graded_at.isoformat() if submission.graded_at else None,
    }


@router.post("/submissions/{submission_id}/questions/{question_id}/regrade-essay")
async def regrade_essay(
    submission_id: int,
    question_id: int,
    student_text: Optional[str] = Form(None),
    image_file: Optional[UploadFile] = File(None),
    force_essay: bool = Form(False),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """大题/作文 LLM 重批改接口

    场景：scan_and_grade 完成后，教师对某道大题想重新触发 LLM 批改：
    - 上次 OCR 误识别 → 教师直接输入学生答案文字（student_text），跳过 OCR
    - 上次 LLM 评分不准 → 重新上传图片（image_file），重新走 OCR + LLM
    - 想换路由判定 → force_essay=True 强制按作文批改（默认按 _is_essay_question 自动路由）

    入参（student_text 和 image_file 二选一，至少一个）：
    - student_text: 教师直接输入的学生答案文字（跳过 OCR，confidence=1.0）
    - image_file: 重新上传的图片，重新走 OCR + LLM
    - force_essay: True 强制按作文批改；False（默认）按 _is_essay_question 自动路由

    权限：仅教师/管理员（且必须是该 submission 所属考试的教师）

    流程：
    1. 权限校验 + 参数校验（student_text/image_file 至少一个）
    2. 校验 submission/question 存在 + 题目属于该考试 + 必须是大题（type==essay）
    3. 准备学生答案文字：
       - student_text 模式：直接用，confidence=1.0
       - image_file 模式：调 ocr_service.recognize，OCR 失败返回 400 提示改用 student_text
    4. 路由：force_essay 或 _is_essay_question → grade_essay；否则 grade_math
    5. 调 grading_service.grade_essay/grade_math（复用 scan_and_grade 中的 LLM 链路）
    6. 作文场景调 writing_kg 做错因→维度/节点/建议归因
    7. 更新或新建 Answer 表（content/score/is_correct）
    8. 重新计算 submission 总分 + status='graded'
    9. 返回完整批改详情（含 grading/error_cause/knowledge_points/writing_attribution）
    """
    from datetime import datetime
    from backend.models.tables import ExamSubmission, Answer
    from backend.services.grader import grading_service
    from backend.services.answer_sheet import _is_essay_question
    from backend.services.writing_graph import writing_kg

    # 0. 权限校验
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可调用此接口")

    # 1. 参数校验：student_text 和 image_file 至少一个
    # 注意：FastAPI File(None) 默认值在直接调用时是 File 对象（非 None），
    # 用 hasattr(image_file, 'read') 区分真实 UploadFile 与默认值占位
    has_text = bool(student_text and student_text.strip())
    has_image = image_file is not None and hasattr(image_file, 'read')
    if not has_text and not has_image:
        raise HTTPException(400, "必须提供 student_text 或 image_file（二选一）")

    # 2. 校验 submission
    submission = db.query(ExamSubmission).filter(ExamSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(404, f"提交 {submission_id} 不存在")

    # 3. 校验当前用户是该 submission 所属考试的教师
    exam = db.query(Exam).filter(Exam.id == submission.exam_id).first()
    if not exam:
        raise HTTPException(404, "提交关联的考试不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权操作此提交（仅该考试的教师可操作）")

    # 4. 校验 question
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(404, f"题目 {question_id} 不存在")
    if question.exam_id != submission.exam_id:
        raise HTTPException(400, "题目不属于该提交对应的考试")

    # 5. 必须是大题（type==essay）
    if question.type != "essay":
        raise HTTPException(
            400,
            "该接口仅支持大题/作文重批改，其他题型请使用 manual-input 接口"
        )

    # 6. 准备学生答案文字 + 图片字节
    image_bytes = None
    if has_image:
        image_bytes = await image_file.read()
        if not image_bytes:
            raise HTTPException(400, "图片内容为空")

    if has_text:
        raw_text = student_text.strip()
        confidence = 1.0  # 教师手输，置信度满分
    else:
        # image_file 模式：走 OCR
        from backend.services.ocr import ocr_service
        try:
            ocr_result = await ocr_service.recognize(image_bytes)
        except Exception as e:
            logger.exception(f"[RegradeEssay] OCR 异常: {e}")
            raise HTTPException(500, f"OCR 调用失败: {type(e).__name__}: {e}")
        raw_text = ocr_result.text or ""
        confidence = float(ocr_result.confidence or 0.0)
        if ocr_result.needs_manual_input or (not raw_text.strip() and confidence < 0.4):
            raise HTTPException(
                400,
                f"OCR 识别失败或置信度过低 (confidence={confidence:.2f})，"
                f"请改用 student_text 直接输入学生答案"
            )

    # 7. 路由：作文 vs 数学
    # 注意：FastAPI Form(False) 默认值在直接调用时是 Form 对象（truthy），
    # 用 `force_essay is True` 严格判断，避免测试/直接调用场景下误路由
    is_essay = (force_essay is True) or _is_essay_question(question.content)
    logger.info(
        f"[RegradeEssay] submission={submission_id} question={question_id} "
        f"is_essay={is_essay} force_essay={force_essay!r} "
        f"content_head={question.content[:30]!r}"
    )

    # 8. 调 LLM 批改（复用 grading_service）
    try:
        if is_essay:
            llm_result = await grading_service.grade_essay(
                question=question.content,
                standard_answer=question.answer or "",
                student_answer_ocr=raw_text,
                total_score=int(question.score),
                confidence=confidence,
                image_bytes=image_bytes,
            )
        else:
            llm_result = await grading_service.grade_math(
                question=question.content,
                standard_answer=question.answer or "",
                student_answer_ocr=raw_text,
                total_score=int(question.score),
                confidence=confidence,
                image_bytes=image_bytes,
            )
    except Exception as e:
        logger.exception(f"[RegradeEssay] LLM 批改异常: {e}")
        raise HTTPException(500, f"LLM 批改失败: {type(e).__name__}: {e}")

    # 9. 提取结果
    suggested_score = float(llm_result.get("suggested_score", 0) or 0)
    max_score = float(llm_result.get("max_score", question.score) or question.score)
    grading = llm_result.get("grading", {}) or {}
    comment = llm_result.get("comment", "") or ""
    error_cause = grading.get("error_cause", "none")
    knowledge_points = grading.get("knowledge_points", []) or []
    model_key = llm_result.get("model_key", "standard")
    grading_method = grading.get("grading_method", "llm")
    ratio = suggested_score / max_score if max_score > 0 else 0
    is_correct = ratio >= 0.8

    # 10. 写作能力归因（仅作文场景，且有错因）
    writing_attribution = None
    if is_essay and error_cause and error_cause != "none":
        try:
            dimension = writing_kg.map_error_cause_to_dimension(error_cause)
            fine_nodes = writing_kg.map_error_cause_to_nodes(error_cause)
            suggestion = writing_kg.get_error_cause_suggestion(error_cause)
            writing_attribution = {
                "error_cause": error_cause,
                "dimension": dimension,
                "fine_nodes": fine_nodes,
                "knowledge_points": knowledge_points,
                "suggestion": suggestion,
            }
            if suggestion:
                comment = f"{comment}\n\n【改进建议】{suggestion}"
        except Exception as e:
            logger.warning(f"[RegradeEssay] 写作归因失败: {type(e).__name__}: {e}")

    # 11. 更新或新建 Answer（先捕获 before 值用于历史记录）
    answer = db.query(Answer).filter(
        Answer.submission_id == submission_id,
        Answer.question_id == question_id,
    ).first()

    # F 方案：捕获重批改前的状态用于历史记录
    before_score = answer.score if answer else None
    before_is_correct = answer.is_correct if answer else None
    before_total_score = submission.score

    if answer:
        answer.content = raw_text
        answer.score = suggested_score
        answer.is_correct = is_correct
    else:
        answer = Answer(
            submission_id=submission_id,
            question_id=question_id,
            content=raw_text,
            score=suggested_score,
            is_correct=is_correct,
        )
        db.add(answer)

    # 12. 重新计算 submission 总分
    all_answers = db.query(Answer).filter(Answer.submission_id == submission_id).all()
    total_score = sum((a.score or 0) for a in all_answers)
    submission.score = total_score
    submission.graded_at = datetime.now()
    if submission.status != "graded":
        submission.status = "graded"

    # 13. F 方案：写入重批改历史记录（与 Answer 同事务提交，保证审计一致性）
    from backend.models.tables import AnswerRegradeHistory
    history = AnswerRegradeHistory(
        submission_id=submission_id,
        question_id=question_id,
        operator_id=current_user.id,
        regrade_method="regrade_essay",
        input_mode="text" if has_text else "image",
        force_essay=(force_essay is True),  # 严格判断，避开 Form(False) 默认值陷阱
        before_score=before_score,
        after_score=suggested_score,
        before_is_correct=before_is_correct,
        after_is_correct=is_correct,
        max_score=max_score,
        before_total_score=before_total_score,
        after_total_score=total_score,
        student_text=raw_text,
        is_essay=is_essay,
        model_key=model_key,
        grading_method=grading_method,
        error_cause=error_cause,
        knowledge_points_json=json.dumps(knowledge_points, ensure_ascii=False) if knowledge_points else None,
        grading_json=json.dumps(llm_result, ensure_ascii=False),
        writing_attribution_json=json.dumps(writing_attribution, ensure_ascii=False) if writing_attribution else None,
        comment=comment,
    )
    db.add(history)

    db.commit()

    logger.info(
        f"[RegradeEssay] teacher={current_user.id} submission={submission_id} "
        f"question={question_id} is_essay={is_essay} → score={suggested_score}/{max_score} "
        f"model={model_key} error_cause={error_cause}"
    )

    return {
        "submission_id": submission_id,
        "question_id": question_id,
        "student_answer": raw_text,
        "standard_answer": question.answer,
        "score": suggested_score,
        "max_score": max_score,
        "is_correct": is_correct,
        "total_score": total_score,
        "regrade": True,
        "is_essay": is_essay,
        "model_key": model_key,
        "grading_method": grading_method,
        "comment": comment,
        "grading": grading,
        "error_cause": error_cause,
        "knowledge_points": knowledge_points,
        "writing_attribution": writing_attribution,
        "graded_at": submission.graded_at.isoformat() if submission.graded_at else None,
    }


@router.get("/submissions/{submission_id}/questions/{question_id}/regrade-history")
def list_regrade_history(
    submission_id: int,
    question_id: int,
    detail: bool = False,
    limit: int = 100,
    offset: int = 0,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取某题的重批改历史记录（按 created_at DESC 排序）

    权限：仅教师/管理员（且必须是该 submission 所属考试的教师，admin 可读任意）
    入参：
    - detail: true 时返回完整 grading_json/writing_attribution_json/student_text
    - limit: 最多返回条数（默认 100，上限 500）
    - offset: 分页偏移

    返回：{submission_id, question_id, total, limit, offset, records: [...]}
    """
    from backend.models.tables import ExamSubmission, AnswerRegradeHistory

    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可调用此接口")

    # 1. 校验 submission
    submission = db.query(ExamSubmission).filter(ExamSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(404, f"提交 {submission_id} 不存在")

    # 2. 校验当前用户是该 submission 所属考试的教师
    exam = db.query(Exam).filter(Exam.id == submission.exam_id).first()
    if not exam:
        raise HTTPException(404, "提交关联的考试不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权查看此提交的历史（仅该考试的教师可查看）")

    # 3. 校验 question 存在 + 属于该考试
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(404, f"题目 {question_id} 不存在")
    if question.exam_id != submission.exam_id:
        raise HTTPException(400, "题目不属于该提交对应的考试")

    # 4. 查询历史记录（按 created_at DESC 排序）
    query = db.query(AnswerRegradeHistory).filter(
        AnswerRegradeHistory.submission_id == submission_id,
        AnswerRegradeHistory.question_id == question_id,
    ).order_by(AnswerRegradeHistory.created_at.desc())

    total = query.count()
    safe_limit = max(1, min(int(limit), 500))
    safe_offset = max(0, int(offset))
    records = query.offset(safe_offset).limit(safe_limit).all()

    return {
        "submission_id": submission_id,
        "question_id": question_id,
        "total": total,
        "limit": safe_limit,
        "offset": safe_offset,
        "records": [_serialize_regrade_history(r, detail=detail) for r in records],
    }


def _serialize_regrade_history(r, detail: bool = False) -> dict:
    """序列化重批改历史记录

    detail=False（列表模式）：省略 grading_json/writing_attribution_json/完整 student_text，
                              仅返回 student_text_head 前 100 字 + knowledge_points 反序列化
    detail=True（详情模式）：返回完整字段
    """
    item = {
        "id": r.id,
        "operator_id": r.operator_id,
        "operator_name": r.operator.name if r.operator else None,
        "operator_role": r.operator.role if r.operator else None,
        "regrade_method": r.regrade_method,
        "input_mode": r.input_mode,
        "force_essay": r.force_essay,
        "before_score": r.before_score,
        "after_score": r.after_score,
        "before_is_correct": r.before_is_correct,
        "after_is_correct": r.after_is_correct,
        "max_score": r.max_score,
        "before_total_score": r.before_total_score,
        "after_total_score": r.after_total_score,
        "is_essay": r.is_essay,
        "model_key": r.model_key,
        "grading_method": r.grading_method,
        "error_cause": r.error_cause,
        "comment": r.comment,
        "created_at": r.created_at.isoformat() if r.created_at else None,
    }

    # 列表模式：student_text 截前 100 字，knowledge_points 反序列化
    item["student_text_head"] = (r.student_text or "")[:100]
    if r.knowledge_points_json:
        try:
            item["knowledge_points"] = json.loads(r.knowledge_points_json)
        except Exception:
            item["knowledge_points"] = []
    else:
        item["knowledge_points"] = []

    if detail:
        # 详情模式：返回完整字段
        item["student_text"] = r.student_text
        item["grading_json"] = json.loads(r.grading_json) if r.grading_json else None
        item["writing_attribution_json"] = (
            json.loads(r.writing_attribution_json) if r.writing_attribution_json else None
        )
        item["knowledge_points_json_raw"] = r.knowledge_points_json

    return item


# 注意：Excel 报告导出（单份 /export/excel/{submission_id}、批量 /export/excel-batch）
# 已迁移至 backend.api.answer_sheet_export_routes 模块。
