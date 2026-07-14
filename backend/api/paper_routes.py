"""试卷扫描与批改 API"""

import os
import json
import base64
import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import StreamingResponse, FileResponse
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.config import settings
from backend.models.tables import PaperTemplate, Paper, PaperAnswer
from backend.models.schemas import (
    PaperTemplateCreate, PaperTemplateOut, PaperTemplateDetail,
    ScanPaperRequest, ScanPaperResponse, PaperOut, PaperDetail,
    PaperAnswerOut, PaperAnswerUpdate, PaperFinalScoreUpdate,
    PaperStatistics, QuestionRegionOut,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/papers", tags=["paper"])


# ============================================
# 模板管理
# ============================================

@router.post("/templates", response_model=PaperTemplateOut)
def create_template(data: PaperTemplateCreate, db: Session = Depends(get_db)):
    """创建试卷模板（标准答案 + 区域坐标）"""
    regions_config = json.dumps(
        [q.model_dump() for q in data.questions], ensure_ascii=False
    )
    total_score = sum(q.max_score for q in data.questions)
    template = PaperTemplate(
        name=data.name,
        classroom_id=data.classroom_id,
        question_count=len(data.questions),
        total_score=total_score,
        regions_config=regions_config,
    )
    db.add(template)
    db.commit()
    db.refresh(template)
    return template


@router.get("/templates", response_model=list[PaperTemplateOut])
def list_templates(classroom_id: int | None = None, db: Session = Depends(get_db)):
    """获取模板列表，可按课堂过滤"""
    query = db.query(PaperTemplate)
    if classroom_id:
        query = query.filter(PaperTemplate.classroom_id == classroom_id)
    return query.order_by(PaperTemplate.created_at.desc()).all()


@router.get("/templates/{template_id}", response_model=PaperTemplateDetail)
def get_template(template_id: int, db: Session = Depends(get_db)):
    """获取模板详情（含解析后的区域配置）"""
    template = db.query(PaperTemplate).filter(PaperTemplate.id == template_id).first()
    if not template:
        raise HTTPException(404, "模板不存在")
    questions = [QuestionRegionOut(**q) for q in json.loads(template.regions_config)]
    return PaperTemplateDetail(
        id=template.id,
        name=template.name,
        classroom_id=template.classroom_id,
        question_count=template.question_count,
        total_score=template.total_score,
        regions_config=template.regions_config,
        created_at=template.created_at,
        questions=questions,
    )


@router.delete("/templates/{template_id}")
def delete_template(template_id: int, db: Session = Depends(get_db)):
    """删除模板（需无关联试卷）"""
    template = db.query(PaperTemplate).filter(PaperTemplate.id == template_id).first()
    if not template:
        raise HTTPException(404, "模板不存在")
    papers_count = db.query(Paper).filter(Paper.template_id == template_id).count()
    if papers_count > 0:
        raise HTTPException(400, f"该模板已关联 {papers_count} 份试卷，无法删除")
    db.delete(template)
    db.commit()
    return {"message": "模板已删除"}


@router.post("/templates/auto-detect-regions")
def auto_detect_regions(image_data: str = Body(..., embed=True)):
    """自动检测答题卡图片中的文本区域。

    接收 base64 图像，使用 OpenCV 形态学操作检测文本块，
    返回百分比坐标列表供前端预览和调整。
    """
    if not image_data:
        raise HTTPException(400, "请提供图像数据")

    from paper_scanner.scanner import decode_base64_image
    from paper_scanner.region_detector import detect_answer_regions

    try:
        image = decode_base64_image(image_data)
        regions = detect_answer_regions(image)
        return {"regions": regions, "count": len(regions)}
    except Exception as e:
        raise HTTPException(500, f"区域检测失败: {e}")


@router.post("/templates/perspective-preview")
def perspective_preview(image_data: str = Body(..., embed=True)):
    """对上传的答题卡图片进行透视矫正预览。

    返回矫正后的 base64 图像，供前端在画布上框选区域。
    """
    if not image_data:
        raise HTTPException(400, "请提供图像数据")

    from paper_scanner.scanner import decode_base64_image, encode_image_to_base64
    from paper_scanner.perspective import correct_perspective

    try:
        image = decode_base64_image(image_data)
        corrected, corners = correct_perspective(image)
        corrected_base64 = encode_image_to_base64(corrected) if corrected is not None else None
        return {"corrected_image": corrected_base64, "corners": corners}
    except Exception as e:
        raise HTTPException(500, f"透视矫正失败: {e}")


# ============================================
# 试卷扫描
# ============================================

@router.post("/scan", response_model=ScanPaperResponse)
def scan_paper(data: ScanPaperRequest, db: Session = Depends(get_db)):
    """扫描试卷：base64图像 → 透视矫正 → OCR → 自动评分"""
    # 1. 加载模板
    template = db.query(PaperTemplate).filter(PaperTemplate.id == data.template_id).first()
    if not template:
        raise HTTPException(404, "模板不存在")

    # 2. 构建 PaperTemplate 对象
    from paper_scanner.template import PaperTemplate as PT, QuestionRegion
    questions_data = json.loads(template.regions_config)
    regions = [QuestionRegion(**q) for q in questions_data]
    pt = PT(name=template.name, questions=regions)

    # 3. 执行扫描流水线
    from paper_scanner.scanner import scan_paper as do_scan
    try:
        result = do_scan(data.image_data, pt, grade_subjective_answers=data.grade_subjective)
    except ImportError as e:
        raise HTTPException(500, f"PaddleOCR 未安装，请运行 pip install -r requirements-paper.txt: {e}")
    except Exception as e:
        logger.error(f"扫描失败: {e}", exc_info=True)
        raise HTTPException(500, f"扫描失败: {e}")

    # 4. 保存图片到磁盘
    os.makedirs(settings.PAPER_UPLOAD_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    corrected_path = None
    if result.get("corrected_image"):
        corrected_path = os.path.join(
            settings.PAPER_UPLOAD_DIR, f"corrected_{timestamp}_{data.template_id}.jpg"
        )
        with open(corrected_path, "wb") as f:
            f.write(base64.b64decode(result["corrected_image"]))

    original_path = os.path.join(
        settings.PAPER_UPLOAD_DIR, f"original_{timestamp}_{data.template_id}.jpg"
    )
    with open(original_path, "wb") as f:
        f.write(base64.b64decode(data.image_data))

    # 5. 创建 Paper 记录
    paper = Paper(
        template_id=data.template_id,
        classroom_id=data.classroom_id,
        person_id=data.person_id,
        student_name=data.student_name,
        image_path=original_path,
        corrected_image_path=corrected_path,
        total_auto_score=result["total_auto_score"],
        status="graded" if data.grade_subjective else "pending",
        graded_at=datetime.now() if data.grade_subjective else None,
    )
    db.add(paper)
    db.commit()
    db.refresh(paper)

    # 6. 创建 PaperAnswer 记录
    for ans in result["answers"]:
        answer = PaperAnswer(
            paper_id=paper.id,
            question_index=ans["question_index"],
            question_type=ans["question_type"],
            ocr_text=ans["ocr_text"],
            standard_answer=ans["standard_answer"],
            max_score=ans["max_score"],
            auto_score=ans["auto_score"],
            ai_suggestion=ans.get("ai_suggestion"),
            correct=ans.get("correct"),
        )
        db.add(answer)
    db.commit()

    # 7. 返回响应
    answers = db.query(PaperAnswer).filter(PaperAnswer.paper_id == paper.id).order_by(PaperAnswer.question_index).all()
    return ScanPaperResponse(
        paper_id=paper.id,
        corrected_image=result.get("corrected_image"),
        corners=result.get("corners"),
        answers=[PaperAnswerOut.model_validate(a) for a in answers],
        total_auto_score=paper.total_auto_score,
    )


# ============================================
# 试卷列表与详情
# ============================================

@router.get("", response_model=list[PaperOut])
def list_papers(
    template_id: int | None = None,
    classroom_id: int | None = None,
    person_id: int | None = None,
    db: Session = Depends(get_db),
):
    """获取试卷列表，支持多条件过滤"""
    query = db.query(Paper)
    if template_id:
        query = query.filter(Paper.template_id == template_id)
    if classroom_id:
        query = query.filter(Paper.classroom_id == classroom_id)
    if person_id:
        query = query.filter(Paper.person_id == person_id)
    return query.order_by(Paper.scanned_at.desc()).all()


@router.get("/{paper_id}", response_model=PaperDetail)
def get_paper(paper_id: int, db: Session = Depends(get_db)):
    """获取试卷详情（含所有题目评分）"""
    paper = db.query(Paper).filter(Paper.id == paper_id).first()
    if not paper:
        raise HTTPException(404, "试卷不存在")
    answers = db.query(PaperAnswer).filter(
        PaperAnswer.paper_id == paper_id
    ).order_by(PaperAnswer.question_index).all()
    template = db.query(PaperTemplate).filter(PaperTemplate.id == paper.template_id).first()
    return PaperDetail(
        id=paper.id,
        template_id=paper.template_id,
        classroom_id=paper.classroom_id,
        person_id=paper.person_id,
        student_name=paper.student_name,
        image_path=paper.image_path,
        corrected_image_path=paper.corrected_image_path,
        total_auto_score=paper.total_auto_score,
        final_score=paper.final_score,
        status=paper.status,
        scanned_at=paper.scanned_at,
        graded_at=paper.graded_at,
        answers=[PaperAnswerOut.model_validate(a) for a in answers],
        template_name=template.name if template else None,
    )


@router.get("/{paper_id}/image")
def get_paper_image(paper_id: int, corrected: bool = True, db: Session = Depends(get_db)):
    """返回试卷图片文件"""
    paper = db.query(Paper).filter(Paper.id == paper_id).first()
    if not paper:
        raise HTTPException(404, "试卷不存在")
    path = paper.corrected_image_path if corrected else paper.image_path
    if not path or not os.path.exists(path):
        raise HTTPException(404, "图片文件不存在")
    return FileResponse(path)


# ============================================
# 手动修正
# ============================================

@router.put("/{paper_id}/answers/{answer_id}", response_model=PaperAnswerOut)
def update_answer(
    paper_id: int,
    answer_id: int,
    data: PaperAnswerUpdate,
    db: Session = Depends(get_db),
):
    """手动修正单题评分"""
    answer = db.query(PaperAnswer).filter(
        PaperAnswer.id == answer_id, PaperAnswer.paper_id == paper_id
    ).first()
    if not answer:
        raise HTTPException(404, "答题记录不存在")
    answer.final_score = data.final_score
    if data.ai_suggestion is not None:
        answer.ai_suggestion = data.ai_suggestion
    if data.ocr_text is not None:
        answer.ocr_text = data.ocr_text
    db.commit()
    db.refresh(answer)

    paper = db.query(Paper).filter(Paper.id == paper_id).first()
    if paper:
        paper.status = "corrected"
        db.commit()

    return answer


@router.put("/{paper_id}/final-score", response_model=PaperOut)
def update_final_score(
    paper_id: int,
    data: PaperFinalScoreUpdate,
    db: Session = Depends(get_db),
):
    """设置试卷最终总分"""
    paper = db.query(Paper).filter(Paper.id == paper_id).first()
    if not paper:
        raise HTTPException(404, "试卷不存在")
    paper.final_score = data.final_score
    paper.status = "corrected"
    db.commit()
    db.refresh(paper)
    return paper


# ============================================
# 主观题 AI 重新评分（流式）
# ============================================

@router.post("/{paper_id}/answers/{answer_id}/grade-subjective")
async def regrade_subjective_stream(
    paper_id: int,
    answer_id: int,
    db: Session = Depends(get_db),
):
    """重新调用 Ollama 评分主观题（SSE 流式返回）"""
    answer = db.query(PaperAnswer).filter(
        PaperAnswer.id == answer_id, PaperAnswer.paper_id == paper_id
    ).first()
    if not answer:
        raise HTTPException(404, "答题记录不存在")

    from paper_scanner.grader import grade_subjective_stream

    def event_stream():
        try:
            for event in grade_subjective_stream(
                question=f"题目{answer.question_index}",
                standard_answer=answer.standard_answer,
                student_answer=answer.ocr_text,
                max_score=answer.max_score,
            ):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)}, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


# ============================================
# 成绩统计
# ============================================

@router.get("/templates/{template_id}/statistics", response_model=PaperStatistics)
def get_statistics(template_id: int, db: Session = Depends(get_db)):
    """获取试卷评分统计"""
    template = db.query(PaperTemplate).filter(PaperTemplate.id == template_id).first()
    if not template:
        raise HTTPException(404, "模板不存在")

    papers = db.query(Paper).filter(Paper.template_id == template_id).all()
    if not papers:
        raise HTTPException(400, "暂无试卷数据")

    scores = [p.final_score if p.final_score is not None else p.total_auto_score for p in papers]

    # 分数分布
    distribution = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0, "0-59": 0}
    for s in scores:
        if s >= 90:
            distribution["90-100"] += 1
        elif s >= 80:
            distribution["80-89"] += 1
        elif s >= 70:
            distribution["70-79"] += 1
        elif s >= 60:
            distribution["60-69"] += 1
        else:
            distribution["0-59"] += 1

    # 客观题正确率
    all_answers = db.query(PaperAnswer).filter(
        PaperAnswer.paper_id.in_([p.id for p in papers]),
        PaperAnswer.question_type == "objective",
    ).all()

    question_accuracy = []
    for q_index in range(1, template.question_count + 1):
        q_answers = [a for a in all_answers if a.question_index == q_index]
        if q_answers:
            correct_count = sum(1 for a in q_answers if a.correct)
            question_accuracy.append({
                "question_index": q_index,
                "accuracy": round(correct_count / len(q_answers), 3),
                "total": len(q_answers),
                "correct": correct_count,
            })

    return PaperStatistics(
        template_id=template_id,
        template_name=template.name,
        total_papers=len(papers),
        avg_score=round(sum(scores) / len(scores), 1),
        max_score=max(scores),
        min_score=min(scores),
        score_distribution=distribution,
        per_question_accuracy=question_accuracy,
    )
