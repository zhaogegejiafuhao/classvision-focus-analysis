"""错题本路由（从 correction_routes.py 拆分）

拆分后的模块：
- correction_routes.py：订正提交、订正对比、个性化订正（订正闭环工作流）
- mistake_book_routes.py：错题列表、错题详情、相似题生成（错题本浏览与练习）

本模块包含：
- GET  /api/correction/list                       错题列表（作业+考试，分页+知识点过滤）
- GET  /api/correction/{grading_id}               错题详情（原题+批改+订正历史）
- POST /api/correction/{grading_id}/generate-similar  从错题一键生成相似题
"""
import json
import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Answer,
    CorrectionRecord,
    Exam,
    ExamSubmission,
    GradingResult,
    Homework,
    HomeworkSubmission,
    Question,
    RegisteredPerson,
    SimilarQuestion,
)
from backend.models.schemas import (
    GenerateSimilarRequest,
    MistakeDetail,
    MistakeCorrectionRecord,
    MistakeListItem,
    MistakeListResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/correction", tags=["correction"])


def _parse_kp_list(raw: str | None) -> list[str]:
    """安全解析 knowledge_points JSON 字段为 list[str]"""
    if not raw:
        return []
    try:
        v = json.loads(raw)
        if isinstance(v, list):
            return [str(x) for x in v]
        if isinstance(v, str):
            return [v]
    except Exception:
        pass
    return []


@router.get("/list")
def list_mistakes(
    student_id: int | None = None,
    kp: str | None = None,
    page: int = 1,
    page_size: int = 20,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict:
    """错题本列表：从 GradingResult + 考试 Answer 筛选错题

    - 学生角色：强制只能看自己的错题（student_id 被忽略）
    - 教师/管理员：可通过 student_id 指定学生，缺省则取自己
    - kp：知识点关键词，对 knowledge_points JSON 做 LIKE 过滤
    - 分页：page 从 1 开始，page_size 默认 20
    """
    # 角色权限控制
    if current_user.role == "student":
        target_student_id = current_user.id
    else:
        target_student_id = student_id or current_user.id

    if not target_student_id:
        raise HTTPException(400, "缺少 student_id 参数")

    items: list[dict] = []

    # ---- 1. 作业错题：从 GradingResult 筛选 error_type 非空的记录 ----
    hw_query = (
        db.query(GradingResult, HomeworkSubmission, Homework)
        .join(HomeworkSubmission, GradingResult.submission_id == HomeworkSubmission.id)
        .outerjoin(Homework, HomeworkSubmission.homework_id == Homework.id)
        .filter(
            GradingResult.error_type.isnot(None),
            GradingResult.error_type != "none",
            HomeworkSubmission.student_id == target_student_id,
        )
    )
    if kp:
        hw_query = hw_query.filter(GradingResult.knowledge_points.like(f'%"{kp}"%'))

    for grading, submission, homework in hw_query.all():
        items.append(
            {
                "grading_id": grading.id,
                "submission_id": grading.submission_id,
                "score": grading.score,
                "max_score": grading.max_score,
                "error_type": grading.error_type,
                "error_cause": grading.error_cause,
                "knowledge_points": _parse_kp_list(grading.knowledge_points),
                "created_at": grading.created_at,
                "homework_id": homework.id if homework else None,
                "homework_title": homework.title if homework else "",
                "source": "homework",
            }
        )

    # ---- 2. 考试错题：从 Answer 筛选 is_correct=False 的记录 ----
    exam_wrong_answers = (
        db.query(Answer, ExamSubmission, Exam, Question)
        .join(ExamSubmission, Answer.submission_id == ExamSubmission.id)
        .join(Exam, ExamSubmission.exam_id == Exam.id)
        .join(Question, Answer.question_id == Question.id)
        .filter(
            ExamSubmission.student_id == target_student_id,
            Answer.is_correct == False,  # noqa: E712
        )
        .all()
    )
    for answer, exam_sub, exam, question in exam_wrong_answers:
        items.append(
            {
                "grading_id": None,
                "submission_id": exam_sub.id,
                "score": answer.score or 0,
                "max_score": question.score,
                "error_type": "exam_wrong",
                "error_cause": None,
                "knowledge_points": _parse_kp_list(question.knowledge_points) if hasattr(question, 'knowledge_points') and question.knowledge_points else [],
                "created_at": exam_sub.submitted_at or exam_sub.created_at,
                "homework_id": None,
                "homework_title": "",
                "source": "exam",
                "exam_id": exam.id,
                "exam_title": exam.title,
                "question_id": question.id,
                "question_content": question.content[:100] if question.content else "",
                "student_answer": answer.content[:200] if answer.content else "",
                "correct_answer": question.answer[:200] if question.answer else "",
            }
        )

    # 按时间倒序排序
    items.sort(key=lambda x: x["created_at"] or datetime.min, reverse=True)

    total = len(items)
    offset = (page - 1) * page_size
    paged_items = items[offset: offset + page_size]

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "items": paged_items,
    }


@router.get("/{grading_id}")
def get_mistake_detail(
    grading_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict:
    """错题详情：聚合原题+标准答案+学生作答+批改详情+订正历史"""
    grading = db.query(GradingResult).filter(GradingResult.id == grading_id).first()
    if not grading:
        raise HTTPException(404, "批改记录不存在")

    submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == grading.submission_id).first()
    if not submission:
        raise HTTPException(404, "提交记录不存在")

    # 学生只能看自己的错题
    if current_user.role == "student" and submission.student_id != current_user.id:
        raise HTTPException(403, "无权访问该错题")
    # IDOR 防护：教师只能查看自己作业下的错题
    if current_user.role == "teacher":
        hw = db.query(Homework).filter(Homework.id == submission.homework_id).first()
        if hw and hw.teacher_id != current_user.id:
            raise HTTPException(403, "无权访问其他教师的错题")

    homework = (
        db.query(Homework).filter(Homework.id == submission.homework_id).first()
        if submission.homework_id
        else None
    )

    # 订正历史（按时间倒序）
    correction_records = (
        db.query(CorrectionRecord)
        .filter(CorrectionRecord.submission_id == submission.id)
        .order_by(CorrectionRecord.created_at.desc())
        .all()
    )

    # 解析 JSON 字段
    try:
        rubric = json.loads(grading.rubric_json) if grading.rubric_json else None
    except Exception:
        rubric = None
    try:
        grading_data = json.loads(grading.grading_json) if grading.grading_json else None
    except Exception:
        grading_data = None

    return {
        "grading_id": grading.id,
        "submission_id": grading.submission_id,
        "homework_id": homework.id if homework else None,
        "homework_title": homework.title if homework else "",
        "question_text": homework.title if homework else "",
        "standard_answer": homework.description if homework else "",
        "student_answer_ocr": submission.content or "",
        "rubric": rubric,
        "grading": grading_data,
        "score": grading.score,
        "max_score": grading.max_score,
        "comment": grading.comment or "",
        "error_type": grading.error_type,
        "error_cause": grading.error_cause,
        "knowledge_points": _parse_kp_list(grading.knowledge_points),
        "created_at": grading.created_at,
        "correction_records": [
            {
                "correction_id": cr.id,
                "correction_score": cr.correction_score,
                "original_score": cr.original_score,
                "improved": cr.improved,
                "created_at": cr.created_at,
            }
            for cr in correction_records
        ],
    }


@router.post("/{grading_id}/generate-similar")
async def generate_similar_from_mistake(
    grading_id: int,
    data: GenerateSimilarRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """从错题一键生成相似题并持久化

    取 GradingResult → Homework 题目/标准答案 → knowledge_points →
    调 similar_question_service 生成 → 批量插入 SimilarQuestion
    """
    grading = db.query(GradingResult).filter(GradingResult.id == grading_id).first()
    if not grading:
        raise HTTPException(404, "批改记录不存在")

    submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == grading.submission_id).first()
    if not submission:
        raise HTTPException(404, "提交记录不存在")

    # 学生只能给自己的错题生成
    if current_user.role == "student" and submission.student_id != current_user.id:
        raise HTTPException(403, "无权操作该错题")
    # IDOR 防护：教师只能给自己作业下的错题生成相似题
    if current_user.role == "teacher":
        hw = db.query(Homework).filter(Homework.id == submission.homework_id).first()
        if hw and hw.teacher_id != current_user.id:
            raise HTTPException(403, "无权操作其他教师的错题")

    # 确定目标学生
    target_student_id = submission.student_id or current_user.id

    # 取原题信息
    homework = db.query(Homework).filter(Homework.id == submission.homework_id).first() if submission.homework_id else None
    question_text = homework.title if homework else ""
    standard_answer = homework.description if homework else ""
    knowledge_points = _parse_kp_list(grading.knowledge_points)

    # 知识点标准化：用 ErrorMapper 映射到标准节点 ID
    knowledge_point_ids = []
    if knowledge_points:
        try:
            from backend.services.attribution import ErrorMapper
            mapper = ErrorMapper()
            for kp_text in knowledge_points:
                ids = await mapper.map_error(kp_text)
                knowledge_point_ids.extend(ids)
            knowledge_point_ids = list(set(knowledge_point_ids))  # 去重
        except Exception as e:
            logger.warning(f"ErrorMapper 标准化失败: {e}, 使用原始知识点")

    # 调用相似题服务
    from backend.services.similar_question import similar_question_service
    generated = await similar_question_service.generate_similar_questions(
        question=question_text,
        knowledge_points=knowledge_points,
        error_type=grading.error_type or "",
        tier=data.tier,
        count=data.count,
        standard_answer=standard_answer,
        knowledge_point_ids=knowledge_point_ids,
    )

    # 持久化
    persisted_items = []
    for q in generated:
        sq = SimilarQuestion(
            student_id=target_student_id,
            source_grading_id=grading_id,
            question_text=q.get("question_text", ""),
            standard_answer=q.get("standard_answer", ""),
            rubric_suggestion=json.dumps(q.get("rubric_suggestion", {}), ensure_ascii=False) if q.get("rubric_suggestion") else None,
            difficulty=q.get("difficulty", "中等"),
            variant_type=q.get("variant_type", "同类变式"),
            tier=data.tier,
            knowledge_point_ids=json.dumps(knowledge_point_ids or knowledge_points, ensure_ascii=False) if (knowledge_point_ids or knowledge_points) else None,
            mastery_status="pending",
        )
        db.add(sq)
        db.flush()  # 获取 id
        persisted_items.append({
            "similar_id": sq.id,
            "question_text": sq.question_text,
            "variant_type": sq.variant_type,
        })

    db.commit()

    logger.info(f"[generate-similar] grading_id={grading_id}, generated={len(persisted_items)}")

    return {
        "generated": len(persisted_items),
        "items": persisted_items,
    }
