"""答题卡错题归因回写（从 answer_sheet.py 抽取）

把批改结果交给归因服务，写入 KnowledgeAnalysis 表：
- 数学错题 → knowledge_attribution_service（基于 knowledge_graph）
- 作文错题 → writing_attribution_service（基于 writing_graph）

原为 AnswerSheetOrchestrator._attribute_and_persist_weakness 方法，
因体积较大（~200 行）且职责独立，抽取为模块级 async 函数。
"""
from __future__ import annotations

import json
import logging
from datetime import date as date_cls
from typing import Optional

from sqlalchemy.orm import Session

from backend.services.answer_sheet_models import QuestionResult

logger = logging.getLogger(__name__)


async def attribute_and_persist_weakness(
    db: Session,
    student_id: int,
    question_results: list[QuestionResult],
) -> dict:
    """错题归因回写：把批改结果交给归因服务，写入 KnowledgeAnalysis 表

    流程：
    1. 收集错题（is_correct=False 或部分得分），按 region_type 分组：
       - bubble/fill 数学错题 → knowledge_attribution_service（基于 knowledge_graph）
       - essay 作文错题 → writing_attribution_service（基于 writing_graph）
    2. 数学题：用 ErrorMapper.map_by_keywords(question_content) 把题目映射到 KG 节点
    3. 作文题：用 error_cause 直接映射到写作 DAG 节点
    4. 调归因服务的 analyze 方法，得到雷达图 + 薄弱点
    5. 序列化写入 KnowledgeAnalysis 表（math/writing 各一条）

    Returns:
        归因回写摘要 {math_report_saved: bool, writing_report_saved: bool, ...}
    """
    from backend.models.tables import KnowledgeAnalysis

    today = date_cls.today()
    result_summary = {
        "math_report_saved": False,
        "writing_report_saved": False,
        "math_error_count": 0,
        "writing_error_count": 0,
        "error": None,
    }

    # 收集错题
    math_error_texts: list[tuple[str, str, float]] = []  # (question_content, error_cause, weight)
    writing_errors: list[tuple[str, str, float]] = []  # (essay_title, error_cause, weight)

    for r in question_results:
        # 跳过未批改或全对的题
        if r.is_correct is True:
            continue
        # 计算错误权重：完全错=1.0, 部分对=0.5
        if r.is_correct is False:
            weight = 1.0
        else:  # None（未批改）
            continue

        # 得分率 < 0.5 视为完全错，0.5-0.8 视为部分错
        if r.max_score > 0:
            ratio = r.score / r.max_score
            if ratio >= 0.5:
                weight = 0.5

        # 获取 error_cause 和 grading_detail
        grading_detail = r.grading_detail or {}
        error_cause = grading_detail.get("error_cause", "") or ""

        if r.region_type == "essay":
            # 作文题：检查 is_essay 标记
            is_essay = grading_detail.get("is_essay", False)
            if is_essay and error_cause and error_cause != "none":
                writing_errors.append((r.question_content, error_cause, weight))
        else:
            # 数学/选择/填空题：用题目内容做关键词匹配
            # 只对有 LLM 批改结果（含 error_cause）的题做归因
            if error_cause and error_cause != "none":
                math_error_texts.append((r.question_content, error_cause, weight))
            elif r.region_type in ("bubble", "fill"):
                # 选择/填空题没有 LLM 错因，用题目内容做关键词匹配后归因
                math_error_texts.append((r.question_content, "知识缺失", weight))

    result_summary["math_error_count"] = len(math_error_texts)
    result_summary["writing_error_count"] = len(writing_errors)

    # 数学题归因
    if math_error_texts:
        try:
            from backend.services.attribution import (
                knowledge_attribution_service, ErrorEvent,
            )
            # 用 ErrorMapper 把题目内容映射到 KG 节点
            error_events: list[ErrorEvent] = []
            for content, cause, weight in math_error_texts:
                node_ids = knowledge_attribution_service.error_mapper.map_by_keywords(content)
                if not node_ids:
                    # 关键词未命中，跳过该题（避免慢速 LLM 调用）
                    continue
                # 一个题目可能匹配多个节点，分摊权重
                per_node_weight = weight / len(node_ids)
                for nid in node_ids:
                    error_events.append(ErrorEvent(
                        knowledge_node_id=nid,
                        error_weight=per_node_weight,
                        timestamp=today,
                        question_content=content[:80],
                        error_cause=cause,
                    ))

            if error_events:
                report = await knowledge_attribution_service.analyze(
                    errors=error_events,
                    reference_date=today,
                )
                # 序列化写入 KnowledgeAnalysis 表
                radar_json = json.dumps(report.radar, ensure_ascii=False)
                weak_points_data = [
                    {
                        "knowledge_id": wp.knowledge_id,
                        "knowledge_name": wp.knowledge_name,
                        "weakness_score": wp.weakness_score,
                        "error_count": wp.error_count,
                        "suggestion": wp.suggestion,
                        "error_cause_distribution": wp.error_cause_distribution,
                    }
                    for wp in report.weak_points
                ]
                weak_points_json = json.dumps(weak_points_data, ensure_ascii=False)
                correction_status_json = json.dumps(report.correction_status, ensure_ascii=False)

                ka = KnowledgeAnalysis(
                    student_id=student_id,
                    analysis_type="math",
                    radar_json=radar_json,
                    weak_points_json=weak_points_json,
                    correction_status_json=correction_status_json,
                )
                db.add(ka)
                db.commit()
                result_summary["math_report_saved"] = True
                logger.info(
                    f"[AnswerSheet] 数学归因完成: student_id={student_id}, "
                    f"error_events={len(error_events)}, weak_points={len(report.weak_points)}"
                )
        except Exception as e:
            logger.warning(f"[AnswerSheet] 数学归因失败: {type(e).__name__}: {e}")
            result_summary["error"] = f"math: {type(e).__name__}: {e}"

    # 作文题归因
    if writing_errors:
        try:
            from backend.services.attribution import (
                writing_attribution_service, WritingErrorEvent,
            )
            writing_events = [
                WritingErrorEvent(
                    error_cause=cause,
                    error_weight=weight,
                    timestamp=today,
                    essay_title=title[:50],
                )
                for title, cause, weight in writing_errors
            ]
            report = await writing_attribution_service.analyze(
                writing_errors=writing_events,
                student_id=str(student_id),
                reference_date=today,
            )
            # 序列化写入 KnowledgeAnalysis 表
            radar_json = json.dumps(report.radar, ensure_ascii=False)
            weak_dims_data = [
                {
                    "dimension_id": wd.dimension_id,
                    "dimension_name": wd.dimension_name,
                    "weakness_score": wd.weakness_score,
                    "sub_weaknesses": wd.sub_weaknesses,
                    "error_causes": wd.error_causes,
                    "suggestion": wd.suggestion,
                }
                for wd in report.weak_dimensions
            ]
            weak_points_json = json.dumps({
                "weak_dimensions": weak_dims_data,
                "error_cause_distribution": report.error_cause_distribution,
                "overall_suggestion": report.overall_suggestion,
            }, ensure_ascii=False)

            ka = KnowledgeAnalysis(
                student_id=student_id,
                analysis_type="writing",
                radar_json=radar_json,
                weak_points_json=weak_points_json,
                correction_status_json=None,
            )
            db.add(ka)
            db.commit()
            result_summary["writing_report_saved"] = True
            logger.info(
                f"[AnswerSheet] 写作归因完成: student_id={student_id}, "
                f"writing_errors={len(writing_events)}, weak_dims={len(report.weak_dimensions)}"
            )
        except Exception as e:
            logger.warning(f"[AnswerSheet] 写作归因失败: {type(e).__name__}: {e}")
            prev = result_summary.get("error") or ""
            result_summary["error"] = f"{prev}writing: {type(e).__name__}: {e}".strip()

    return result_summary
