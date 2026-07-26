"""考试业务逻辑公共服务

从 exam_routes.py 抽取的辅助函数，供多个路由模块共享。
避免路由文件之间的循环依赖。
"""

import json
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from backend.models.tables import Answer, ExamSubmission, Question


def is_subjective_answer(ans: Answer, question: Question) -> bool:
    """判断是否为主观题答案（essay 或 fill 带图）"""
    if question.type == "essay":
        return True
    if question.type == "fill" and ans.image_urls:
        try:
            urls = json.loads(ans.image_urls)
            return bool(urls)
        except (json.JSONDecodeError, TypeError):
            return False
    return False


def normalize_choice_answer(answer: str, option_count: int = 0) -> str:
    """将选择题答案统一为索引格式（"0","1","2"...）

    兼容多种格式：
    - 字母格式: "A","B","C","D" → "0","1","2","3"
    - 索引格式: "0","1","2","3" → 不变
    - 1-based: "1","2","3","4" → "0","1","2","3"（仅当 option_count 可用时）
    """
    a = (answer or "").strip()
    if not a:
        return a
    # 单个字母 A-Z → 转为索引
    if len(a) == 1 and a.isalpha() and a.isupper():
        idx = ord(a) - ord('A')
        return str(idx)
    return a


def auto_grade(question: Question, answer_content: str) -> tuple[float, Optional[bool]]:
    """自动评判客观题（single/multi/judge/fill）。

    返回 (score, is_correct)；简答题返回 (0, False) 等待人工/AI 批改。
    """
    if question.type == "single":
        # 单选题：兼容字母格式（A/B/C/D）和索引格式（0/1/2/3）
        student = normalize_choice_answer(answer_content)
        correct = normalize_choice_answer(question.answer or "", len(question.options or []))
        is_correct = student == correct
        return (question.score if is_correct else 0), is_correct

    elif question.type == "multi":
        # 多选题：兼容字母格式和索引格式
        student_parts = set(normalize_choice_answer(a) for a in answer_content.split(",") if a.strip())
        correct_parts = set(normalize_choice_answer(a) for a in (question.answer or "").split(",") if a.strip())
        is_correct = student_parts == correct_parts
        return (question.score if is_correct else 0), is_correct

    elif question.type == "judge":
        # 判断题：答案为 "true" 或 "false"
        is_correct = answer_content.strip().lower() == (question.answer or "").strip().lower()
        return (question.score if is_correct else 0), is_correct

    elif question.type == "fill":
        # 填空题：多空拆分匹配 + 数值/单位容差（A+B 方案）
        # auto_grade 只返回 (score, is_correct)；详细 detail 由调用方按需获取
        from backend.services.fill_grader import grade_fill_answer
        score, is_correct, _detail = grade_fill_answer(
            answer_content, question.answer or "", question.score
        )
        return score, is_correct

    else:
        # 简答题：需要人工/AI 批改
        return 0, False


def check_submission_completion(db: Session, submission: ExamSubmission) -> None:
    """检查 submission 的所有主观题是否都已确认，如是则锁定为 graded。

    计算最终分数：客观题 score + 主观题 teacher_score（或 ai_score 兜底）。
    """
    subjective_answers = []
    for ans in submission.answers:
        q = ans.question
        if q and is_subjective_answer(ans, q):
            subjective_answers.append(ans)

    if not subjective_answers:
        return  # 没有主观题，无需处理

    all_confirmed = all(a.teacher_confirmed for a in subjective_answers)
    if all_confirmed:
        total = 0.0
        for ans in submission.answers:
            q = ans.question
            if not q:
                continue
            if is_subjective_answer(ans, q):
                # 主观题：优先 teacher_score，其次 ai_score
                total += ans.teacher_score if ans.teacher_score is not None else (ans.ai_score or 0)
            else:
                # 客观题：直接用 score
                total += ans.score or 0
        submission.score = total
        submission.status = "graded"
        submission.graded_at = datetime.now()
        db.commit()
