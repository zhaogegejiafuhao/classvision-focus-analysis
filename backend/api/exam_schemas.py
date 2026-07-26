"""考试相关 Pydantic 模型（从 exam_routes.py 抽取）

集中放置避免路由文件之间相互导入，也便于前端类型对照。
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# ===== 题目 / 考试 =====
class QuestionCreate(BaseModel):
    type: str  # single/multi/judge/fill/essay
    content: str
    options: Optional[list[str]] = None  # 选择题选项
    answer: str
    score: float = 10.0
    knowledge_points: Optional[list[str]] = None  # 知识点标签


class ExamCreate(BaseModel):
    title: str
    description: str = ""
    classroom_id: Optional[int] = None
    duration: int = 60
    total_score: float = 100.0
    exam_type: str = "computer"  # computer(机试)/paper(笔试)
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    questions: list[QuestionCreate] = []


class ExamOut(BaseModel):
    id: int
    title: str
    description: str
    classroom_id: Optional[int]
    classroom_name: Optional[str]
    teacher_id: int
    teacher_name: str
    duration: int
    total_score: float
    status: str
    exam_type: str = "computer"
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    question_count: int

    class Config:
        from_attributes = True


class QuestionOut(BaseModel):
    id: int
    type: str
    content: str
    options: Optional[list[str]]
    score: float
    order: int
    knowledge_points: Optional[list[str]] = None

    class Config:
        from_attributes = True


class ExamDetailOut(ExamOut):
    questions: list[QuestionOut]


# ===== 答案 / 提交 =====
class AnswerSubmit(BaseModel):
    question_id: int
    content: str = ""
    image_urls: list[str] = []  # 图片URL列表


class SubmissionOut(BaseModel):
    id: int
    exam_id: int
    student_id: int
    student_name: str
    score: Optional[float]
    status: str
    started_at: datetime
    submitted_at: Optional[datetime]

    class Config:
        from_attributes = True


class AnswerGrade(BaseModel):
    answer_id: int
    score: float
    is_correct: Optional[bool] = None


# ===== AI 批改确认 =====
class ConfirmAnswerRequest(BaseModel):
    teacher_score: Optional[float] = None
    teacher_comment: Optional[str] = None
    adopt_ai_score: bool = False  # True 时忽略 teacher_score，直接采用 ai_score


class ConfirmBatchRequest(BaseModel):
    answer_ids: list[int]
    adopt_ai_score: bool = True  # 默认采用 AI 分
    teacher_scores: Optional[dict[int, float]] = None  # adopt_ai_score=False 时使用
