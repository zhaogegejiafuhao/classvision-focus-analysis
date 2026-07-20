"""代码查重 API（简化版：基于文本相似度）"""
import difflib

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import HomeworkSubmission, RegisteredPerson

router = APIRouter(prefix="/api/plagiarism", tags=["plagiarism"])


class PlagiarismCheckRequest(BaseModel):
    homework_id: int


@router.post("/check")
def check_plagiarism(
    data: PlagiarismCheckRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """检测作业提交之间的相似度（代码/文本查重）"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以查重")

    submissions = db.query(HomeworkSubmission).filter(
        HomeworkSubmission.homework_id == data.homework_id,
    ).all()

    if len(submissions) < 2:
        return {"total": len(submissions), "pairs": []}

    # 计算所有提交对之间的相似度
    pairs = []
    for i in range(len(submissions)):
        for j in range(i + 1, len(submissions)):
            s1 = submissions[i]
            s2 = submissions[j]
            if not s1.content or not s2.content:
                continue

            # 使用 difflib 计算文本相似度
            ratio = difflib.SequenceMatcher(None, s1.content, s2.content).ratio()
            if ratio >= 0.5:  # 只报告相似度>=50%的
                pairs.append({
                    "student_1": s1.student.name if hasattr(s1, 'student') and s1.student else f"学生{s1.student_id}",
                    "student_2": s2.student.name if hasattr(s2, 'student') and s2.student else f"学生{s2.student_id}",
                    "similarity": round(ratio * 100, 1),
                    "level": "high" if ratio >= 0.8 else "medium" if ratio >= 0.6 else "low",
                })

    # 按相似度排序
    pairs.sort(key=lambda x: x["similarity"], reverse=True)

    return {
        "total": len(submissions),
        "suspicious_pairs": len(pairs),
        "pairs": pairs,
    }
