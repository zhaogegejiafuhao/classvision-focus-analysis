"""答题卡试卷模板管理路由（从 answer_sheet_routes.py 拆分）"""
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

# 题型 → 区域类型映射（用于自动生成模板时分发到 bubble/fill/essay 区域）
_QTYPE_TO_REGION_TYPE = {
    "single": "bubble", "multi": "bubble", "judge": "bubble",
    "fill": "fill", "essay": "essay",
}

# 支持的预设布局：name → (列数, 描述)
_PRESET_LAYOUTS = {
    "standard_5col": (5, "5列布局（默认，每列10题，最多50题）"),
    "standard_4col": (4, "4列布局（每列10题，最多40题）"),
    "standard_3col": (3, "3列布局（每列10题，最多30题）"),
    "standard_2col": (2, "2列布局（适合大题，最多20题）"),
    "single_col":   (1, "单列布局（适合纯大题卷，最多20题）"),
}


@router.post("/templates")
async def create_template(
    exam_id: int = Form(...),
    blank_file: UploadFile = File(...),
    regions_json: str = Form(...),
    anchor_points_json: Optional[str] = Form(None),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建/更新试卷模板

    参数：
    - exam_id: 考试 ID
    - blank_file: 空白卷图片
    - regions_json: JSON 字符串，区域列表 [{"question_id", "region_type", "bbox": {x,y,w,h}, "order"}]
    - anchor_points_json: 可选，4 个角点坐标 JSON（用于透视校正）
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可创建模板")

    # 校验考试存在且属于当前教师
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, f"考试 {exam_id} 不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权为该考试创建模板")

    # 读取空白卷图片
    blank_bytes = await blank_file.read()
    if not blank_bytes:
        raise HTTPException(400, "空白卷图片为空")

    # 解析 regions JSON
    try:
        regions = json.loads(regions_json)
        if not isinstance(regions, list):
            raise ValueError("regions 必须是数组")
    except (json.JSONDecodeError, ValueError) as e:
        raise HTTPException(400, f"regions_json 格式错误: {e}")

    # 校验 regions 字段
    for i, r in enumerate(regions):
        if not all(k in r for k in ("question_id", "region_type", "bbox")):
            raise HTTPException(400, f"第 {i+1} 个 region 缺少必要字段（question_id/region_type/bbox）")
        if r["region_type"] not in ("bubble", "fill", "essay"):
            raise HTTPException(400, f"第 {i+1} 个 region_type 无效: {r['region_type']}")
        bbox = r["bbox"]
        if not all(k in bbox for k in ("x", "y", "w", "h")):
            raise HTTPException(400, f"第 {i+1} 个 bbox 缺少字段（x/y/w/h）")

    # 解析 anchor_points
    anchor_points = None
    if anchor_points_json:
        try:
            anchor_points = json.loads(anchor_points_json)
        except json.JSONDecodeError as e:
            raise HTTPException(400, f"anchor_points_json 格式错误: {e}")

    # 调用服务创建模板
    try:
        template_id = paper_template_service.create_template(
            db=db,
            exam_id=exam_id,
            teacher_id=current_user.id,
            blank_image_bytes=blank_bytes,
            filename=blank_file.filename or "blank.png",
            regions=regions,
            anchor_points=anchor_points,
        )
    except Exception as e:
        logger.exception(f"[AnswerSheetRoute] create_template 异常: {e}")
        raise HTTPException(500, f"创建模板失败: {e}")

    return {"template_id": template_id, "exam_id": exam_id, "regions_count": len(regions)}



@router.get("/templates/{exam_id}")
def get_template(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取试卷模板"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可查看模板")

    # 校验考试归属
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, f"考试 {exam_id} 不存在")
    assert_owner_or_admin(exam.teacher_id, current_user)

    template_info = paper_template_service.get_template(db, exam_id)
    if not template_info:
        raise HTTPException(404, f"考试 {exam_id} 未配置试卷模板")

    return {
        "id": template_info.id,
        "exam_id": template_info.exam_id,
        "blank_image_url": template_info.blank_image_url,
        "blank_image_size": template_info.blank_image_size,
        "regions": template_info.regions,
    }



@router.delete("/templates/{exam_id}")
def delete_template(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除试卷模板"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可删除模板")

    # 校验考试归属
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, f"考试 {exam_id} 不存在")
    assert_owner_or_admin(exam.teacher_id, current_user)

    success = paper_template_service.delete_template(db, exam_id)
    if not success:
        raise HTTPException(404, f"考试 {exam_id} 未配置试卷模板")

    return {"success": True, "exam_id": exam_id}



@router.put("/regions/{region_id}")
def update_region(
    region_id: int,
    bbox: dict,
    region_type: Optional[str] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """更新某题区域坐标"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可更新区域")

    # 通过 region → template → exam 校验归属
    from backend.models.tables import PaperTemplate, QuestionRegion
    region = db.query(QuestionRegion).filter(QuestionRegion.id == region_id).first()
    if not region:
        raise HTTPException(404, f"区域 {region_id} 不存在")
    template = db.query(PaperTemplate).filter(PaperTemplate.id == region.template_id).first()
    if not template:
        raise HTTPException(404, "区域关联的模板不存在")
    exam = db.query(Exam).filter(Exam.id == template.exam_id).first()
    if not exam:
        raise HTTPException(404, "区域关联的考试不存在")
    assert_owner_or_admin(exam.teacher_id, current_user)

    success = paper_template_service.update_region(db, region_id, bbox, region_type)
    if not success:
        raise HTTPException(404, f"区域 {region_id} 不存在")

    return {"success": True, "region_id": region_id}



def _compute_auto_layout_bboxes(
    img_w: int,
    img_h: int,
    n_questions: int,
    cols: int,
    top_margin_ratio: float = 0.05,
    bottom_margin_ratio: float = 0.03,
    side_margin_ratio: float = 0.03,
) -> list[dict]:
    """根据预设布局计算每个题位的 bbox（纯函数，便于单元测试）

    Args:
        img_w: 空白卷图片宽度（像素）
        img_h: 空白卷图片高度（像素）
        n_questions: 题目数量
        cols: 列数（来自 _PRESET_LAYOUTS）
        top_margin_ratio: 顶部留白比例
        bottom_margin_ratio: 底部留白比例
        side_margin_ratio: 左右留白比例

    Returns:
        [{"x", "y", "w", "h"}, ...] 长度为 n_questions
    """
    rows = (n_questions + cols - 1) // cols  # 向上取整
    effective_w = img_w * (1 - 2 * side_margin_ratio)
    effective_h = img_h * (1 - top_margin_ratio - bottom_margin_ratio)
    col_w = effective_w / cols
    row_h = effective_h / rows
    x_offset = img_w * side_margin_ratio
    y_offset = img_h * top_margin_ratio

    bboxes = []
    for i in range(n_questions):
        col_idx = i % cols
        row_idx = i // cols
        bboxes.append({
            "x": int(round(x_offset + col_idx * col_w)),
            "y": int(round(y_offset + row_idx * row_h)),
            "w": int(round(col_w)),
            "h": int(round(row_h)),
        })
    return bboxes



@router.post("/templates/{exam_id}/auto-generate")
async def auto_generate_template(
    exam_id: int,
    blank_file: UploadFile = File(...),
    layout: str = Form("standard_5col"),
    question_ids_json: Optional[str] = Form(None),
    top_margin_ratio: float = Form(0.05),
    bottom_margin_ratio: float = Form(0.03),
    side_margin_ratio: float = Form(0.03),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """B. 试卷模板预设一键生成

    教师只需上传空白卷 + 选择布局，系统自动按布局为 exam 所有题目生成 regions，
    免去手工逐题拖框。

    Args:
        exam_id: 考试 ID
        blank_file: 空白卷扫描件（PNG/JPG）
        layout: 预设布局名，见 _PRESET_LAYOUTS（默认 5 列）
        question_ids_json: 可选，JSON 数组，按指定顺序使用题目；不传则按 Question.order 自动排序
        top_margin_ratio: 顶部留白比例（0-0.3，默认 0.05）
        bottom_margin_ratio: 底部留白比例（0-0.3，默认 0.03）
        side_margin_ratio: 左右留白比例（0-0.2，默认 0.03）

    Returns:
        {template_id, exam_id, regions_count, layout, image_size}
    """
    import cv2 as _cv2
    import numpy as _np

    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可生成模板")

    # 校验考试存在 + 权限
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, f"考试 {exam_id} 不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权为该考试生成模板")

    # 校验布局
    if layout not in _PRESET_LAYOUTS:
        raise HTTPException(
            400,
            f"不支持的布局 '{layout}'，可选: {list(_PRESET_LAYOUTS.keys())}"
        )
    cols, layout_desc = _PRESET_LAYOUTS[layout]

    # 校验留白比例
    for name, val in [("top", top_margin_ratio), ("bottom", bottom_margin_ratio), ("side", side_margin_ratio)]:
        if not 0 <= val <= 0.3:
            raise HTTPException(400, f"{name}_margin_ratio 必须在 [0, 0.3] 之间，当前 {val}")

    # 读取空白卷图片
    blank_bytes = await blank_file.read()
    if not blank_bytes:
        raise HTTPException(400, "空白卷图片为空")

    # 解码获取尺寸
    try:
        img_array = _np.frombuffer(blank_bytes, dtype=_np.uint8)
        img = _cv2.imdecode(img_array, _cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("图像解码失败")
        img_h, img_w = img.shape[:2]
    except Exception as e:
        raise HTTPException(400, f"空白卷图片解析失败: {e}")

    # 加载题目列表
    if question_ids_json:
        try:
            q_ids = json.loads(question_ids_json)
            if not isinstance(q_ids, list) or not q_ids:
                raise ValueError("question_ids_json 必须是非空数组")
        except (json.JSONDecodeError, ValueError) as e:
            raise HTTPException(400, f"question_ids_json 格式错误: {e}")
        questions = db.query(Question).filter(Question.id.in_(q_ids)).all()
        # 按用户指定顺序排序
        questions.sort(key=lambda q: q_ids.index(q.id))
    else:
        questions = db.query(Question).filter(Question.exam_id == exam_id).order_by(Question.order).all()

    if not questions:
        raise HTTPException(400, f"考试 {exam_id} 没有题目，无法生成模板")

    # 计算行列布局
    n = len(questions)
    rows = (n + cols - 1) // cols  # 向上取整

    # 计算每个 region 的 bbox（基于原图像素坐标，调用纯函数）
    bboxes = _compute_auto_layout_bboxes(
        img_w=img_w,
        img_h=img_h,
        n_questions=n,
        cols=cols,
        top_margin_ratio=top_margin_ratio,
        bottom_margin_ratio=bottom_margin_ratio,
        side_margin_ratio=side_margin_ratio,
    )

    regions = []
    for i, q in enumerate(questions):
        # 类型映射（未知类型默认 essay）
        region_type = _QTYPE_TO_REGION_TYPE.get(q.type, "essay")
        regions.append({
            "question_id": q.id,
            "region_type": region_type,
            "bbox": bboxes[i],
            "order": q.order if q.order is not None else (i + 1),
        })

    # 调用现有服务一次性创建模板（已支持"已存在则更新"）
    try:
        template_id = paper_template_service.create_template(
            db=db,
            exam_id=exam_id,
            teacher_id=current_user.id,
            blank_image_bytes=blank_bytes,
            filename=blank_file.filename or "blank.png",
            regions=regions,
        )
    except Exception as e:
        logger.exception(f"[AnswerSheetRoute] auto_generate_template 异常: {e}")
        raise HTTPException(500, f"生成模板失败: {e}")

    logger.info(
        f"[AnswerSheetRoute] 自动生成模板成功: exam_id={exam_id}, template_id={template_id}, "
        f"layout={layout}, questions={n}, rows={rows}, cols={cols}"
    )

    return {
        "template_id": template_id,
        "exam_id": exam_id,
        "regions_count": len(regions),
        "layout": layout,
        "layout_desc": layout_desc,
        "image_size": {"width": img_w, "height": img_h},
        "grid": {"rows": rows, "cols": cols},
        "regions": regions,  # 返回生成的 bbox 供前端预览/微调
    }



@router.put("/templates/{exam_id}/regions/batch")
def batch_update_regions(
    exam_id: int,
    regions_json: str = Form(...),
    delete_missing: bool = Form(False),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """C. 模板区域批量更新（事务内 upsert）

    教师在前端批量调整 region 坐标后，一次提交所有 regions，避免逐个调用
    PUT /regions/{region_id}。

    Args:
        exam_id: 考试 ID
        regions_json: JSON 数组，每项 {"region_id"?, "question_id", "region_type", "bbox", "order"}
                      - 含 region_id 则更新现有 region
                      - 不含 region_id 则新增 region
        delete_missing: True 时删除不在列表中的现有 region（默认 False，避免误删）

    Returns:
        {success, updated, inserted, deleted, total}
    """
    from backend.models.tables import PaperTemplate, QuestionRegion

    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可批量更新区域")

    # 校验模板存在
    template = db.query(PaperTemplate).filter(PaperTemplate.exam_id == exam_id).first()
    if not template:
        raise HTTPException(404, f"考试 {exam_id} 未配置试卷模板")

    # 校验考试归属
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, f"考试 {exam_id} 不存在")
    assert_owner_or_admin(exam.teacher_id, current_user)

    # 解析 regions_json
    try:
        regions = json.loads(regions_json)
        if not isinstance(regions, list):
            raise ValueError("regions_json 必须是数组")
    except (json.JSONDecodeError, ValueError) as e:
        raise HTTPException(400, f"regions_json 格式错误: {e}")

    # 字段校验
    valid_region_types = {"bubble", "fill", "essay"}
    for i, r in enumerate(regions):
        if not isinstance(r, dict):
            raise HTTPException(400, f"第 {i+1} 项不是对象")
        if "question_id" not in r or "bbox" not in r:
            raise HTTPException(400, f"第 {i+1} 项缺少 question_id 或 bbox")
        if r.get("region_type") and r["region_type"] not in valid_region_types:
            raise HTTPException(400, f"第 {i+1} 项 region_type 无效: {r['region_type']}")
        bbox = r["bbox"]
        if not all(k in bbox for k in ("x", "y", "w", "h")):
            raise HTTPException(400, f"第 {i+1} 项 bbox 缺少 x/y/w/h")

    # 事务内 upsert
    updated_count = 0
    inserted_count = 0
    seen_region_ids: set[int] = set()

    try:
        for r in regions:
            region_id = r.get("region_id")
            if region_id:
                # 更新现有 region
                region = db.query(QuestionRegion).filter(
                    QuestionRegion.id == region_id,
                    QuestionRegion.template_id == template.id,
                ).first()
                if not region:
                    raise HTTPException(404, f"region_id {region_id} 不属于该模板")
                region.bbox = json.dumps(r["bbox"])
                if r.get("region_type"):
                    region.region_type = r["region_type"]
                if "order" in r:
                    region.order = r["order"]
                # question_id 一般不变，但允许更新
                if "question_id" in r:
                    region.question_id = r["question_id"]
                seen_region_ids.add(region_id)
                updated_count += 1
            else:
                # 新增 region
                new_region = QuestionRegion(
                    template_id=template.id,
                    question_id=r["question_id"],
                    region_type=r.get("region_type", "essay"),
                    bbox=json.dumps(r["bbox"]),
                    order=r.get("order", 1),
                )
                db.add(new_region)
                inserted_count += 1

        # 删除缺失项
        deleted_count = 0
        if delete_missing:
            existing_regions = db.query(QuestionRegion).filter(
                QuestionRegion.template_id == template.id
            ).all()
            for er in existing_regions:
                if er.id not in seen_region_ids:
                    db.delete(er)
                    deleted_count += 1

        db.commit()
    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        db.rollback()
        logger.exception(f"[AnswerSheetRoute] batch_update_regions 异常: {e}")
        raise HTTPException(500, f"批量更新失败: {e}")

    logger.info(
        f"[AnswerSheetRoute] 批量更新区域成功: exam_id={exam_id}, "
        f"updated={updated_count}, inserted={inserted_count}, deleted={deleted_count}"
    )

    return {
        "success": True,
        "exam_id": exam_id,
        "template_id": template.id,
        "updated": updated_count,
        "inserted": inserted_count,
        "deleted": deleted_count,
        "total": updated_count + inserted_count,
    }

