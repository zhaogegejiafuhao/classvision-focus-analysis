"""知识归因分析 API"""
import json
import logging
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_teacher_or_admin
from backend.models.tables import RegisteredPerson, GradingResult, KnowledgeAnalysis, HomeworkSubmission, Student, Classroom
from backend.models.schemas import KnowledgeAnalysisRequest, KnowledgeAnalysisResponse
from backend.services.attribution import (
    KnowledgeAttributionService, WritingAttributionService,
    ErrorEvent, knowledge_attribution_service, writing_attribution_service,
)
from backend.services.knowledge_graph import math_kg
from backend.services.writing_graph import writing_kg

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/attribution", tags=["attribution"])


@router.post("/analyze", response_model=KnowledgeAnalysisResponse)
async def analyze_knowledge(
    data: KnowledgeAnalysisRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """知识归因分析（数学/写作）"""
    # 权限校验：学生只能分析自己，教师/管理员可分析任意学生
    if current_user.role == "student" and current_user.id != data.student_id:
        raise HTTPException(403, "无权分析他人数据")

    # 获取该学生所有提交的批改结果
    submission_ids = [
        s[0] for s in db.query(HomeworkSubmission.id)
        .filter(HomeworkSubmission.student_id == data.student_id)
        .all()
    ]

    grading_results = db.query(GradingResult).filter(
        GradingResult.submission_id.in_(submission_ids)
    ).all() if submission_ids else []

    if not grading_results:
        # 返回空分析
        return KnowledgeAnalysisResponse(
            student_id=data.student_id,
            analysis_type=data.analysis_type,
            radar={},
            weak_points=[],
            correction_status=None,
        )

    # 构建错误事件列表（使用正确的 ErrorEvent 字段）
    # 使用 ErrorMapper 将自由文本知识点映射到知识图谱标准节点ID
    from backend.services.attribution import ErrorMapper
    active_kg = writing_kg if data.analysis_type == "writing" else math_kg
    error_mapper = ErrorMapper(active_kg)

    error_events = []
    for gr in grading_results:
        if gr.error_cause and gr.error_cause != "none":
            knowledge_points = json.loads(gr.knowledge_points) if gr.knowledge_points else []
            # 将每个知识点通过关键词匹配映射到知识图谱节点
            mapped_node_ids = set()
            for kp in knowledge_points[:3]:  # 最多取3个知识点
                # 先尝试直接作为节点ID查找
                if active_kg.get_node(kp):
                    mapped_node_ids.add(kp)
                else:
                    # 通过关键词匹配映射
                    matched = error_mapper.map_by_keywords(kp)
                    if matched:
                        mapped_node_ids.update(matched[:2])  # 最多取2个匹配节点

            # 为每个映射到的节点创建错误事件
            for node_id in mapped_node_ids:
                error_events.append(ErrorEvent(
                    knowledge_node_id=node_id,
                    error_weight=round(1.0 - gr.score / max(gr.max_score, 1), 2),
                    timestamp=date.today(),
                    question_content=f"批改记录#{gr.id}",
                    error_cause=gr.error_cause or "未分类",
                ))

            # 如果映射后仍无节点，用提交内容尝试匹配
            if not mapped_node_ids:
                submission = db.query(HomeworkSubmission).filter(
                    HomeworkSubmission.id == gr.submission_id
                ).first()
                match_text = submission.content if submission and submission.content else ""
                if match_text:
                    matched = error_mapper.map_by_keywords(match_text)
                    for node_id in matched[:1]:
                        error_events.append(ErrorEvent(
                            knowledge_node_id=node_id,
                            error_weight=round(1.0 - gr.score / max(gr.max_score, 1), 2),
                            timestamp=date.today(),
                            question_content=f"批改记录#{gr.id}",
                            error_cause=gr.error_cause or "未分类",
                        ))
                        mapped_node_ids.add(node_id)

                if not mapped_node_ids:
                    # 最终降级：记录通用错误事件
                    error_events.append(ErrorEvent(
                        knowledge_node_id="unknown",
                        error_weight=round(1.0 - gr.score / max(gr.max_score, 1), 2),
                        timestamp=date.today(),
                        question_content=f"批改记录#{gr.id}",
                        error_cause=gr.error_cause or "未分类",
                    ))

    # 调用归因服务
    if data.analysis_type == "writing":
        service = writing_attribution_service
    else:
        service = knowledge_attribution_service

    try:
        attribution_result = await service.analyze(error_events)
    except Exception as e:
        logger.error(f"归因分析失败: {e}")
        attribution_result = {"radar": {}, "weak_points": [], "correction_status": {}}

    # 保存分析结果
    analysis_record = KnowledgeAnalysis(
        student_id=data.student_id,
        analysis_type=data.analysis_type,
        radar_json=json.dumps(attribution_result.radar if hasattr(attribution_result, 'radar') else attribution_result.get("radar", {}), ensure_ascii=False),
        weak_points_json=json.dumps(
            [{k: v for k, v in wp.__dict__.items()} for wp in attribution_result.weak_points] if hasattr(attribution_result, 'weak_points') else attribution_result.get("weak_points", []),
            ensure_ascii=False, default=str,
        ),
        correction_status_json=json.dumps(
            attribution_result.correction_status if hasattr(attribution_result, 'correction_status') else attribution_result.get("correction_status", {}),
            ensure_ascii=False, default=str,
        ),
    )
    db.add(analysis_record)
    db.commit()

    # 构建响应
    weak_points_data = []
    if hasattr(attribution_result, 'weak_points'):
        for wp in attribution_result.weak_points:
            wp_dict = {k: v for k, v in wp.__dict__.items()}
            weak_points_data.append(wp_dict)
    else:
        weak_points_data = attribution_result.get("weak_points", [])

    correction_status_data = None
    if hasattr(attribution_result, 'correction_status'):
        correction_status_data = attribution_result.correction_status
    else:
        correction_status_data = attribution_result.get("correction_status")

    radar_data = {}
    if hasattr(attribution_result, 'radar'):
        radar_data = attribution_result.radar
    else:
        radar_data = attribution_result.get("radar", {})

    return KnowledgeAnalysisResponse(
        student_id=data.student_id,
        analysis_type=data.analysis_type,
        radar=radar_data,
        weak_points=weak_points_data,
        correction_status=correction_status_data,
    )


@router.get("/report/{student_id}")
def get_student_report(
    student_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取学生学情报告"""
    # 权限校验：学生只能查看自己，教师/管理员可查看任意
    if current_user.role == "student" and current_user.id != student_id:
        raise HTTPException(403, "无权查看他人学情报告")

    analyses = db.query(KnowledgeAnalysis).filter(
        KnowledgeAnalysis.student_id == student_id
    ).order_by(KnowledgeAnalysis.created_at.desc()).all()

    if not analyses:
        return {"student_id": student_id, "analyses": []}

    return {
        "student_id": student_id,
        "analyses": [
            {
                "id": a.id,
                "analysis_type": a.analysis_type,
                "radar": json.loads(a.radar_json) if a.radar_json else {},
                "weak_points": json.loads(a.weak_points_json) if a.weak_points_json else [],
                "created_at": a.created_at.isoformat() if a.created_at else None,
            }
            for a in analyses
        ],
    }


@router.get("/radar/{student_id}")
def get_radar_data(
    student_id: int,
    analysis_type: str = "math",
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取雷达图数据"""
    # 权限校验：学生只能查看自己
    if current_user.role == "student" and current_user.id != student_id:
        raise HTTPException(403, "无权查看他人雷达图数据")

    analysis = db.query(KnowledgeAnalysis).filter(
        KnowledgeAnalysis.student_id == student_id,
        KnowledgeAnalysis.analysis_type == analysis_type,
    ).order_by(KnowledgeAnalysis.created_at.desc()).first()

    if not analysis:
        return {"student_id": student_id, "radar": {}, "analysis_type": analysis_type}

    return {
        "student_id": student_id,
        "analysis_type": analysis_type,
        "radar": json.loads(analysis.radar_json) if analysis.radar_json else {},
    }


@router.get("/graph")
def get_knowledge_graph(analysis_type: str = "math"):
    """获取知识图谱结构"""
    if analysis_type == "writing":
        return {"type": "writing", "graph": writing_kg.to_dict() if hasattr(writing_kg, 'to_dict') else {}}
    return {"type": "math", "graph": math_kg.to_dict() if hasattr(math_kg, 'to_dict') else {}}


@router.get("/me/student-info")
def get_my_student_info(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取当前学生用户关联的所有 Student 记录（一个 person 可能加入多个课堂）。

    用于学生身份在前端「知识归因分析」页面自动获取自己的 student_id。
    教师身份返回空列表（教师需手动选择学生）。
    """
    if current_user.role != "student":
        return {"user_id": current_user.id, "role": current_user.role, "students": []}

    my_students = db.query(Student).filter(Student.person_id == current_user.id).all()
    student_list = []
    for s in my_students:
        classroom = db.query(Classroom).filter(Classroom.id == s.classroom_id).first()
        student_list.append({
            "student_id": s.person_id,  # registered_person.id，与归因分析 API 一致
            "student_record_id": s.id,  # student 表主键（课堂注册记录）
            "student_name": s.name or current_user.name,
            "classroom_id": s.classroom_id,
            "classroom_name": classroom.name if classroom else "",
        })

    return {
        "user_id": current_user.id,
        "role": current_user.role,
        "students": student_list,
    }


@router.get("/classrooms/{classroom_id}/students-for-analysis")
def list_students_for_analysis(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """教师视角：列出指定课堂的所有学生，供归因分析页面下拉选择。

    返回精简字段：student_id / name / classroom_id。
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可调用此接口")

    students = db.query(Student).filter(Student.classroom_id == classroom_id).all()
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if classroom and current_user.role == "teacher" and classroom.teacher_person_id != current_user.id:
        raise HTTPException(403, "只能查看自己课堂的学生")
    return {
        "classroom_id": classroom_id,
        "classroom_name": classroom.name if classroom else "",
        "students": [
            {
                "student_id": s.person_id,  # registered_person.id，与归因分析 API 一致
                "student_record_id": s.id,  # student 表主键（课堂注册记录）
                "name": s.name or f"学生#{s.id}",
                "classroom_id": s.classroom_id,
            }
            for s in students
        ],
    }