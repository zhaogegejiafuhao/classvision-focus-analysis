"""试卷模板服务——教师拖框标注的空白卷区域 + 扫描件按模板切分

核心场景：
1. 教师上传一张空白卷扫描件作为模板底图
2. 在前端 canvas 上拖框标注每道题的区域 (bbox) + 题型 (bubble/fill/essay)
3. 学生答卷扫描件上传时，系统按模板切分各题图片，再分题型批改

坐标系统：
- bbox 坐标基于空白卷原始像素尺寸
- 前端 canvas 显示时按缩放比例换算
- 切分扫描件时按相同比例切分（要求扫描件与空白卷尺寸接近）

模块级单例：paper_template_service = PaperTemplateService()
"""
from __future__ import annotations

import base64
import json
import logging
import os
import uuid
from dataclasses import dataclass
from typing import Optional

import cv2
import numpy as np
from sqlalchemy.orm import Session

from backend.models.tables import PaperTemplate, QuestionRegion, Question

logger = logging.getLogger(__name__)

# 模板图片上传目录
TEMPLATE_UPLOAD_DIR = "uploads/paper_templates"
os.makedirs(TEMPLATE_UPLOAD_DIR, exist_ok=True)


@dataclass
class QuestionRegionImage:
    """切分后的单题图片"""
    question_id: int
    region_type: str            # bubble | fill | essay
    image_bytes: bytes          # PNG 编码的图片字节
    bbox: tuple[int, int, int, int]  # (x, y, w, h) 原图坐标


@dataclass
class TemplateInfo:
    """模板信息（用于前端展示）"""
    id: int
    exam_id: int
    blank_image_url: str        # 空白卷图片访问 URL
    blank_image_size: tuple[int, int]  # (width, height) 像素
    regions: list[dict]         # [{id, question_id, region_type, bbox, order, question_content}]


class PaperTemplateService:
    """试卷模板服务

    使用方式：
        # 创建模板
        template_id = paper_template_service.create_template(
            db, exam_id=1, teacher_id=2,
            blank_image_bytes=img_bytes, filename="blank.png",
            regions=[{"question_id": 1, "region_type": "bubble", "bbox": {"x": 100, "y": 200, "w": 300, "h": 80}, "order": 1}]
        )

        # 切分扫描件
        region_images = paper_template_service.extract_regions(db, exam_id=1, scanned_image_bytes=scan_bytes)
    """

    def create_template(
        self,
        db: Session,
        exam_id: int,
        teacher_id: int,
        blank_image_bytes: bytes,
        filename: str,
        regions: list[dict],
        anchor_points: Optional[list[dict]] = None,
    ) -> int:
        """创建（或更新）试卷模板

        Args:
            db: 数据库会话
            exam_id: 考试 ID
            teacher_id: 教师 ID
            blank_image_bytes: 空白卷图片字节
            filename: 原始文件名（用于扩展名识别）
            regions: 区域列表，每项 {"question_id", "region_type", "bbox": {x,y,w,h}, "order"}
            anchor_points: 可选，4 个角点坐标用于透视校正

        Returns:
            template_id
        """
        # 检查是否已有模板（exam_id 唯一），有则更新
        existing = db.query(PaperTemplate).filter(PaperTemplate.exam_id == exam_id).first()

        # 保存空白卷图片
        ext = os.path.splitext(filename)[1].lower() or ".png"
        file_id = str(uuid.uuid4())
        save_path = os.path.join(TEMPLATE_UPLOAD_DIR, f"{file_id}{ext}")
        with open(save_path, "wb") as f:
            f.write(blank_image_bytes)

        if existing:
            # 删除旧图片
            try:
                if os.path.exists(existing.blank_image_path):
                    os.remove(existing.blank_image_path)
            except OSError:
                pass
            # 更新基本信息
            existing.blank_image_path = save_path
            existing.teacher_id = teacher_id
            existing.anchor_points = json.dumps(anchor_points) if anchor_points else None
            # 删除旧 regions
            db.query(QuestionRegion).filter(QuestionRegion.template_id == existing.id).delete()
            template = existing
        else:
            template = PaperTemplate(
                exam_id=exam_id,
                teacher_id=teacher_id,
                blank_image_path=save_path,
                anchor_points=json.dumps(anchor_points) if anchor_points else None,
            )
            db.add(template)
            db.flush()  # 获取 template.id

        # 创建新的 regions
        for r in regions:
            region = QuestionRegion(
                template_id=template.id,
                question_id=r["question_id"],
                region_type=r["region_type"],
                bbox=json.dumps(r["bbox"]),
                order=r.get("order", 1),
            )
            db.add(region)

        db.commit()
        db.refresh(template)
        logger.info(
            f"[PaperTemplate] 创建模板成功: template_id={template.id}, "
            f"exam_id={exam_id}, regions={len(regions)}"
        )
        return template.id

    def get_template(self, db: Session, exam_id: int) -> Optional[TemplateInfo]:
        """获取指定考试的试卷模板信息"""
        template = db.query(PaperTemplate).filter(PaperTemplate.exam_id == exam_id).first()
        if not template:
            return None

        # 获取空白卷图片尺寸
        blank_image_size = self._get_image_size(template.blank_image_path)

        # 加载 regions，关联 question 表获取题目内容
        regions_list = []
        for r in template.regions:
            question = db.query(Question).filter(Question.id == r.question_id).first()
            regions_list.append({
                "id": r.id,
                "question_id": r.question_id,
                "region_type": r.region_type,
                "bbox": json.loads(r.bbox),
                "order": r.order,
                "question_content": question.content[:80] + "..." if question and len(question.content) > 80 else (question.content if question else ""),
                "question_type": question.type if question else None,
            })

        # 按 order 排序
        regions_list.sort(key=lambda x: x["order"])

        return TemplateInfo(
            id=template.id,
            exam_id=template.exam_id,
            blank_image_url=f"/uploads/paper_templates/{os.path.basename(template.blank_image_path)}",
            blank_image_size=blank_image_size,
            regions=regions_list,
        )

    def extract_regions(
        self,
        db: Session,
        exam_id: int,
        scanned_image_bytes: bytes,
    ) -> list[QuestionRegionImage]:
        """按模板切分扫描件

        Args:
            db: 数据库会话
            exam_id: 考试 ID
            scanned_image_bytes: 扫描件图片字节

        Returns:
            切分后的各题图片列表，按 order 排序
        """
        template = db.query(PaperTemplate).filter(PaperTemplate.exam_id == exam_id).first()
        if not template:
            raise ValueError(f"考试 {exam_id} 未配置试卷模板，请先创建模板")

        # 解码扫描件
        img_array = np.frombuffer(scanned_image_bytes, dtype=np.uint8)
        scanned = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if scanned is None:
            raise ValueError("扫描件解码失败")

        # 如果配置了 anchor_points，做透视校正
        if template.anchor_points:
            try:
                anchor_pts = json.loads(template.anchor_points)
                scanned = self._apply_perspective(scanned, anchor_pts)
            except Exception as e:
                logger.warning(f"[PaperTemplate] 透视校正失败，使用原图: {e}")

        # 切分各题区域（按 order 排序后切分）
        ordered_regions = sorted(template.regions, key=lambda x: x.order)
        region_images: list[QuestionRegionImage] = []
        for r in ordered_regions:
            try:
                bbox = json.loads(r.bbox)
                x, y, w, h = bbox["x"], bbox["y"], bbox["w"], bbox["h"]

                # 边界检查
                h_img, w_img = scanned.shape[:2]
                x2 = min(x + w, w_img)
                y2 = min(y + h, h_img)
                x1 = max(0, x)
                y1 = max(0, y)

                if x2 <= x1 or y2 <= y1:
                    logger.warning(f"[PaperTemplate] 区域 {r.id} 无效 bbox: {bbox}")
                    continue

                roi = scanned[y1:y2, x1:x2]
                # 编码为 PNG
                ok, buffer = cv2.imencode('.png', roi)
                if not ok:
                    logger.warning(f"[PaperTemplate] 区域 {r.id} 编码失败")
                    continue

                region_images.append(QuestionRegionImage(
                    question_id=r.question_id,
                    region_type=r.region_type,
                    image_bytes=buffer.tobytes(),
                    bbox=(x, y, w, h),
                ))
            except Exception as e:
                logger.exception(f"[PaperTemplate] 切分区域 {r.id} 异常: {e}")
                continue

        logger.info(
            f"[PaperTemplate] 切分完成: exam_id={exam_id}, "
            f"regions={len(template.regions)}, success={len(region_images)}"
        )
        return region_images

    def update_region(
        self,
        db: Session,
        region_id: int,
        bbox: dict,
        region_type: Optional[str] = None,
    ) -> bool:
        """更新某题区域坐标"""
        region = db.query(QuestionRegion).filter(QuestionRegion.id == region_id).first()
        if not region:
            return False
        region.bbox = json.dumps(bbox)
        if region_type:
            region.region_type = region_type
        db.commit()
        return True

    def delete_template(self, db: Session, exam_id: int) -> bool:
        """删除模板（含磁盘文件）"""
        template = db.query(PaperTemplate).filter(PaperTemplate.exam_id == exam_id).first()
        if not template:
            return False
        # 删除磁盘文件
        try:
            if os.path.exists(template.blank_image_path):
                os.remove(template.blank_image_path)
        except OSError:
            pass
        # 数据库删除（级联删除 regions）
        db.delete(template)
        db.commit()
        return True

    # ============ 工具方法 ============

    def _get_image_size(self, image_path: str) -> tuple[int, int]:
        """获取图片尺寸 (width, height)"""
        try:
            img = cv2.imread(image_path)
            if img is None:
                return (0, 0)
            h, w = img.shape[:2]
            return (w, h)
        except Exception:
            return (0, 0)

    def _apply_perspective(self, img: np.ndarray, anchor_points: list[dict]) -> np.ndarray:
        """基于 4 个角点做透视校正

        Args:
            img: 原图
            anchor_points: 4 个角点坐标 [{"x":, "y":}, ...] 顺序为左上、右上、右下、左下

        Returns:
            校正后的图像
        """
        if len(anchor_points) != 4:
            return img

        src = np.array([(p["x"], p["y"]) for p in anchor_points], dtype=np.float32)
        # 计算目标矩形的宽高
        width_top = np.linalg.norm(src[1] - src[0])
        width_bottom = np.linalg.norm(src[2] - src[3])
        height_left = np.linalg.norm(src[3] - src[0])
        height_right = np.linalg.norm(src[2] - src[1])
        max_w = int(max(width_top, width_bottom))
        max_h = int(max(height_left, height_right))

        dst = np.array([
            [0, 0],
            [max_w - 1, 0],
            [max_w - 1, max_h - 1],
            [0, max_h - 1],
        ], dtype=np.float32)

        matrix = cv2.getPerspectiveTransform(src, dst)
        return cv2.warpPerspective(img, matrix, (max_w, max_h))


    def auto_generate_template(
        self,
        db: Session,
        exam_id: int,
        teacher_id: int,
    ) -> int | None:
        """自动生成默认答题卡模板

        根据考试题目数量/类型自动推断布局，生成空白卷底图 + 区域标注。
        如果考试已有模板则跳过。

        Args:
            db: 数据库会话
            exam_id: 考试 ID
            teacher_id: 教师 ID

        Returns:
            template_id 或 None（已有模板时）
        """
        # 检查是否已有模板
        existing = db.query(PaperTemplate).filter(PaperTemplate.exam_id == exam_id).first()
        if existing:
            return None

        # 获取考试题目
        questions = db.query(Question).filter(Question.exam_id == exam_id).order_by(Question.order).all()
        if not questions:
            return None

        # 生成默认空白卷底图（A4 300 DPI: 2480×3508 像素）
        page_w, page_h = 2480, 3508
        blank_img = np.ones((page_h, page_w, 3), dtype=np.uint8) * 255  # 白底

        # 标题区域
        y_offset = 120
        cv2.putText(blank_img, "ClassVision Answer Sheet", (100, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)
        cv2.putText(blank_img, f"Exam ID: {exam_id}", (100, y_offset + 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (100, 100, 100), 1)

        # 学生信息区域
        info_y = y_offset + 120
        cv2.rectangle(blank_img, (80, info_y), (page_w - 80, info_y + 100), (200, 200, 200), 2)
        cv2.putText(blank_img, "Name: ____________    Student ID: ____________", (120, info_y + 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 100), 1)

        y_offset = info_y + 160

        # 计算每道题的区域
        margin_x = 100
        col_w = (page_w - 2 * margin_x) // 2  # 双列布局
        regions = []
        col = 0  # 当前列 (0=左, 1=右)
        row_y = y_offset

        for i, q in enumerate(questions):
            q_type = q.type
            region_type = "bubble" if q_type in ("single", "multi", "judge") else \
                         "fill" if q_type == "fill" else "essay"

            # 根据题型决定区域高度
            if region_type == "bubble":
                h = 120
            elif region_type == "fill":
                h = 150
            else:  # essay
                h = 400

            # 翻页检查
            if row_y + h > page_h - 200:
                # 简单处理：切换到右列或换页（这里仅单页简化）
                break

            x = margin_x + col * col_w
            bbox = {"x": x, "y": row_y, "w": col_w - 40, "h": h}

            # 在底图上画框和标签
            cv2.rectangle(blank_img, (x, row_y), (x + col_w - 40, row_y + h), (0, 0, 0), 1)
            label = f"Q{i+1}({q_type}, {int(q.score)}pts)"
            cv2.putText(blank_img, label, (x + 10, row_y + 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 200), 1)

            # 对于选择题，画选项气泡
            if region_type == "bubble":
                options = ["A", "B", "C", "D"]
                for j, opt in enumerate(options):
                    cx = x + 60 + j * 80
                    cy = row_y + 70
                    cv2.circle(blank_img, (cx, cy), 20, (0, 0, 0), 1)
                    cv2.putText(blank_img, opt, (cx - 6, cy + 6),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 1)

            regions.append({
                "question_id": q.id,
                "region_type": region_type,
                "bbox": bbox,
                "order": i + 1,
            })

            row_y += h + 30

        # 保存底图
        _, encoded = cv2.imencode(".png", blank_img)
        img_bytes = encoded.tobytes()

        # 调用已有的 create_template
        return self.create_template(
            db=db,
            exam_id=exam_id,
            teacher_id=teacher_id,
            blank_image_bytes=img_bytes,
            filename=f"auto_template_{exam_id}.png",
            regions=regions,
        )


# 模块级单例
paper_template_service = PaperTemplateService()
