"""作业系统共享 Pydantic 模型（从 homework_routes.py 拆分）"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class HomeworkCreate(BaseModel):
    title: str
    description: str = ""
    classroom_id: Optional[int] = None
    deadline: Optional[datetime] = None
    total_score: float = 100.0


class HomeworkUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    total_score: Optional[float] = None
    status: Optional[str] = None


class HomeworkOut(BaseModel):
    id: int
    title: str
    description: str
    classroom_id: Optional[int]
    classroom_name: Optional[str]
    teacher_id: int
    teacher_name: str
    deadline: Optional[datetime]
    total_score: float
    status: str
    created_at: datetime
    submission_count: int = 0

    class Config:
        from_attributes = True


class SubmissionCreate(BaseModel):
    content: str = ""


class SubmissionGrade(BaseModel):
    score: float
    feedback: str = ""


class SubmissionOut(BaseModel):
    id: int
    homework_id: int
    student_id: int
    student_name: str
    content: str
    score: Optional[float]
    feedback: str
    status: str
    submitted_at: datetime
    graded_at: Optional[datetime]

    class Config:
        from_attributes = True


# ===== 延期申请模型 =====
class ExtensionRequestCreate(BaseModel):
    homework_id: int
    reason: str
    requested_deadline: datetime


class ExtensionRequestOut(BaseModel):
    id: int
    homework_id: int
    homework_title: str
    student_id: int
    student_name: str
    reason: str
    original_deadline: Optional[datetime]
    requested_deadline: datetime
    status: str
    teacher_feedback: Optional[str]
    created_at: datetime
    reviewed_at: Optional[datetime]

    class Config:
        from_attributes = True


class ExtensionReview(BaseModel):
    status: str  # approved/rejected
    feedback: str = ""
