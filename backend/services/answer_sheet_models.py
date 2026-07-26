"""答题卡批改结果数据模型（从 answer_sheet.py 抽取）

定义单题批改结果与整卷扫描结果的 dataclass，供编排器、批改函数、归因服务共享。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class QuestionResult:
    """单题批改结果"""
    question_id: int
    question_type: str           # single/multi/judge/fill/essay
    question_content: str        # 题目内容（前 80 字）
    region_type: str             # bubble/fill/essay
    student_answer: str          # 识别出的学生答案文本
    standard_answer: str         # 标准答案
    score: float                 # 得分
    max_score: float             # 满分
    is_correct: Optional[bool]   # 是否正确（None 表示未批改）
    comment: str = ""            # 评语
    confidence: float = 1.0      # 识别置信度
    ocr_text: Optional[str] = None  # OCR 识别的原始文本（填空/大题）
    grading_detail: Optional[dict] = None  # LLM 批改完整结果（大题）
    error: Optional[str] = None  # 处理失败原因


@dataclass
class PaperScanResult:
    """整卷扫描批改结果"""
    submission_id: int
    exam_id: int
    student_id: int
    student_name: str
    total_score: float
    max_score: float
    question_results: list[QuestionResult] = field(default_factory=list)
    summary: dict = field(default_factory=dict)  # 汇总统计
    debug_image_b64: str = ""                    # 答题卡调试可视化图
    attribution: dict = field(default_factory=dict)  # 错题归因回写摘要
