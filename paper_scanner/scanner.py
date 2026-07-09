"""扫描主编排器：串联透视矫正、OCR、评分。"""

import base64
import logging

import cv2
import numpy as np
from io import BytesIO
from PIL import Image

from paper_scanner.perspective import correct_perspective
from paper_scanner.ocr_engine import ocr_engine
from paper_scanner.template import PaperTemplate, extract_region
from paper_scanner.grader import grade_objective, grade_subjective

logger = logging.getLogger(__name__)


def decode_base64_image(image_data: str) -> np.ndarray:
    """base64 JPEG → BGR numpy 数组。"""
    img_bytes = base64.b64decode(image_data)
    pil_image = Image.open(BytesIO(img_bytes))
    frame = np.array(pil_image)
    # PIL 是 RGB，转 BGR
    return frame[:, :, ::-1].copy()


def encode_image_to_base64(image: np.ndarray) -> str:
    """BGR numpy 数组 → base64 JPEG 字符串。"""
    _, buffer = cv2.imencode('.jpg', image)
    return base64.b64encode(buffer).decode('utf-8')


def scan_paper(
    image_data: str,
    template: PaperTemplate,
    grade_subjective_answers: bool = True,
) -> dict:
    """完整扫描+评分流水线。

    步骤：
    1. 解码 base64 图像
    2. 透视矫正
    3. 逐题裁剪 + OCR
    4. 客观题自动评分
    5. 主观题 AI 评分（可选）
    6. 计算自动总分

    返回 {
        "corrected_image": base64 | None,
        "corners": list | None,
        "answers": [{question_index, question_type, ocr_text, standard_answer, max_score, auto_score, ai_suggestion, correct}],
        "total_auto_score": float,
    }
    """
    # 1. 解码图像
    image = decode_base64_image(image_data)

    # 2. 透视矫正
    corrected, corners = correct_perspective(image)

    # 3. 逐题处理
    answers = []
    total_score = 0.0

    for q in template.questions:
        # 裁剪答题区域
        region_img = extract_region(corrected, q)

        # OCR 识别
        ocr_text = ocr_engine.recognize_text(region_img)

        answer = {
            "question_index": q.question_index,
            "question_type": q.question_type,
            "ocr_text": ocr_text,
            "standard_answer": q.standard_answer,
            "max_score": q.max_score,
            "auto_score": 0,
            "ai_suggestion": None,
            "correct": None,
        }

        if q.question_type == "objective":
            # 客观题自动匹配
            result = grade_objective(ocr_text, q.standard_answer)
            answer["correct"] = result["correct"]
            answer["auto_score"] = q.max_score if result["correct"] else 0
            answer["ai_suggestion"] = None
        elif q.question_type == "subjective" and grade_subjective_answers:
            # 主观题 AI 评分
            result = grade_subjective(
                question=f"题目{q.question_index}",
                standard_answer=q.standard_answer,
                student_answer=ocr_text,
                max_score=q.max_score,
            )
            answer["auto_score"] = result["score"]
            answer["ai_suggestion"] = result["suggestion"]
            answer["correct"] = None
        elif q.question_type == "subjective":
            # 跳过 AI 评分，待手动触发
            answer["auto_score"] = 0
            answer["ai_suggestion"] = None

        total_score += answer["auto_score"]
        answers.append(answer)

    # 编码矫正后的图像用于前端预览
    corrected_base64 = encode_image_to_base64(corrected) if corrected is not None else None

    return {
        "corrected_image": corrected_base64,
        "corners": corners,
        "answers": answers,
        "total_auto_score": round(total_score, 1),
    }
