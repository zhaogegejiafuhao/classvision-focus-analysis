"""模板坐标系统：定义答题卡区域布局。

坐标为百分比 (0.0-1.0)，与分辨率无关。
"""

import json
from dataclasses import dataclass, asdict
from typing import Literal

import numpy as np


@dataclass
class QuestionRegion:
    """单个答题区域，使用百分比坐标。"""
    question_index: int
    question_type: Literal["objective", "subjective"]
    x: float          # 左上角 x (0-1)
    y: float          # 左上角 y (0-1)
    w: float          # 宽度 (0-1)
    h: float          # 高度 (0-1)
    max_score: float
    standard_answer: str


@dataclass
class PaperTemplate:
    """答题卡模板：题目区域集合。"""
    name: str
    questions: list[QuestionRegion]

    def to_json(self) -> str:
        return json.dumps(
            [asdict(q) for q in self.questions],
            ensure_ascii=False,
        )

    @staticmethod
    def from_json(name: str, json_str: str) -> "PaperTemplate":
        data = json.loads(json_str)
        questions = [QuestionRegion(**q) for q in data]
        return PaperTemplate(name=name, questions=questions)


def extract_region(image: np.ndarray, region: QuestionRegion) -> np.ndarray:
    """从矫正后的图像中按百分比坐标裁剪区域。"""
    h, w = image.shape[:2]
    x1 = max(0, int(region.x * w))
    y1 = max(0, int(region.y * h))
    x2 = min(w, int((region.x + region.w) * w))
    y2 = min(h, int((region.y + region.h) * h))

    if x2 <= x1 or y2 <= y1:
        return image

    return image[y1:y2, x1:x2]


def crop_all_regions(image: np.ndarray, template: PaperTemplate) -> dict[int, np.ndarray]:
    """裁剪模板中所有题目区域。返回 {question_index: image_crop}。"""
    return {q.question_index: extract_region(image, q) for q in template.questions}
