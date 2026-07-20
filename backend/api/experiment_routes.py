"""实验报告管理 API"""
import os
import uuid
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import Experiment, ExperimentReport, RegisteredPerson, Classroom, Student, Notification

router = APIRouter(prefix="/api/experiments", tags=["experiments"])

UPLOAD_DIR = "uploads/experiments"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class ExperimentCreate(BaseModel):
    title: str
    description: str = ""
    requirements: Optional[str] = None
    classroom_id: Optional[int] = None
    deadline: Optional[datetime] = None
    total_score: float = 100.0


class ExperimentOut(BaseModel):
    id: int
    title: str
    description: str
    requirements: Optional[str]
    classroom_id: Optional[int]
    classroom_name: Optional[str]
    teacher_id: int
    teacher_name: str
    deadline: Optional[datetime]
    total_score: float
    status: str
    report_count: int = 0
    created_at: datetime

    class Config:
        from_attributes = True


class ReportOut(BaseModel):
    id: int
    experiment_id: int
    student_id: int
    student_name: str
    content: str
    file_name: Optional[str]
    score: Optional[float]
    feedback: str
    status: str
    submitted_at: datetime
    graded_at: Optional[datetime]

    class Config:
        from_attributes = True


class ReportGrade(BaseModel):
    score: float
    feedback: str = ""


@router.get("", response_model=list[ExperimentOut])
def list_experiments(
    classroom_id: Optional[int] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取实验列表"""
    query = db.query(Experiment)
    if current_user.role == "teacher":
        query = query.filter(Experiment.teacher_id == current_user.id)
    elif current_user.role == "student":
        student = db.query(Student).filter(Student.person_id == current_user.id).first()
        if student:
            query = query.filter(
                (Experiment.classroom_id == student.classroom_id) | (Experiment.classroom_id.is_(None))
            )
        else:
            return []
    if classroom_id:
        query = query.filter(Experiment.classroom_id == classroom_id)
    query = query.order_by(Experiment.created_at.desc())

    result = []
    for exp in query.all():
        result.append(ExperimentOut(
            id=exp.id, title=exp.title, description=exp.description,
            requirements=exp.requirements, classroom_id=exp.classroom_id,
            classroom_name=exp.classroom.name if exp.classroom else None,
            teacher_id=exp.teacher_id, teacher_name=exp.teacher.name,
            deadline=exp.deadline, total_score=exp.total_score,
            status=exp.status, report_count=len(exp.reports), created_at=exp.created_at,
        ))
    return result


@router.post("", response_model=ExperimentOut)
def create_experiment(
    data: ExperimentCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建实验项目"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建实验")
    
    # 权限检查：教师只能为自己创建的课堂创建实验
    if data.classroom_id and current_user.role == "teacher":
        classroom = db.query(Classroom).filter(Classroom.id == data.classroom_id).first()
        if not classroom or classroom.teacher_person_id != current_user.id:
            raise HTTPException(403, "只能为自己创建的课堂创建实验")

    exp = Experiment(
        teacher_id=current_user.id,
        classroom_id=data.classroom_id,
        title=data.title,
        description=data.description,
        requirements=data.requirements,
        deadline=data.deadline,
        total_score=data.total_score,
    )
    db.add(exp)
    db.commit()
    db.refresh(exp)

    return ExperimentOut(
        id=exp.id, title=exp.title, description=exp.description,
        requirements=exp.requirements, classroom_id=exp.classroom_id,
        classroom_name=exp.classroom.name if exp.classroom else None,
        teacher_id=exp.teacher_id, teacher_name=current_user.name,
        deadline=exp.deadline, total_score=exp.total_score,
        status=exp.status, report_count=0, created_at=exp.created_at,
    )


@router.get("/{experiment_id}", response_model=ExperimentOut)
def get_experiment(
    experiment_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取实验详情"""
    exp = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not exp:
        raise HTTPException(404, "实验不存在")
    
    # 权限检查
    if current_user.role == "teacher":
        if exp.teacher_id != current_user.id and current_user.role != "admin":
            raise HTTPException(403, "无权查看此实验")
    elif current_user.role == "student":
        student = db.query(Student).filter(Student.person_id == current_user.id).first()
        if not student or (exp.classroom_id and student.classroom_id != exp.classroom_id):
            raise HTTPException(403, "无权查看此实验")

    return ExperimentOut(
        id=exp.id, title=exp.title, description=exp.description,
        requirements=exp.requirements, classroom_id=exp.classroom_id,
        classroom_name=exp.classroom.name if exp.classroom else None,
        teacher_id=exp.teacher_id, teacher_name=exp.teacher.name,
        deadline=exp.deadline, total_score=exp.total_score,
        status=exp.status, report_count=len(exp.reports), created_at=exp.created_at,
    )


@router.delete("/{experiment_id}")
def delete_experiment(
    experiment_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除实验"""
    exp = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not exp:
        raise HTTPException(404, "实验不存在")
    if exp.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权删除")
    # 级联删除实验报告
    db.query(ExperimentReport).filter(ExperimentReport.experiment_id == experiment_id).delete()
    db.delete(exp)
    db.commit()
    return {"success": True}


@router.get("/{experiment_id}/reports", response_model=list[ReportOut])
def list_reports(
    experiment_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取实验报告列表"""
    exp = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not exp:
        raise HTTPException(404, "实验不存在")
    
    # 权限检查：教师只能看自己实验的报告
    if current_user.role == "teacher" and exp.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权查看此实验报告")
    
    query = db.query(ExperimentReport).filter(ExperimentReport.experiment_id == experiment_id)
    # 学生只能看自己的报告
    if current_user.role == "student":
        query = query.filter(ExperimentReport.student_id == current_user.id)

    result = []
    for rep in query.all():
        result.append(ReportOut(
            id=rep.id, experiment_id=rep.experiment_id,
            student_id=rep.student_id, student_name=rep.student.name,
            content=rep.content, file_name=rep.file_name,
            score=rep.score, feedback=rep.feedback, status=rep.status,
            submitted_at=rep.submitted_at, graded_at=rep.graded_at,
        ))
    return result


@router.post("/{experiment_id}/submit", response_model=ReportOut)
async def submit_report(
    experiment_id: int,
    content: str = Form(""),
    file: UploadFile = File(None),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """提交实验报告"""
    exp = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not exp:
        raise HTTPException(404, "实验不存在")
    
    # 权限检查：学生只能提交自己课堂的实验
    if current_user.role == "student":
        student = db.query(Student).filter(Student.person_id == current_user.id).first()
        if not student or (exp.classroom_id and student.classroom_id != exp.classroom_id):
            raise HTTPException(403, "无权提交此实验报告")

    file_path = None
    file_name = None
    if file:
        file_id = str(uuid.uuid4())
        ext = os.path.splitext(file.filename)[1]
        save_path = os.path.join(UPLOAD_DIR, f"{file_id}{ext}")
        content_bytes = await file.read()
        with open(save_path, "wb") as f:
            f.write(content_bytes)
        file_path = save_path
        file_name = file.filename

    existing = db.query(ExperimentReport).filter(
        ExperimentReport.experiment_id == experiment_id,
        ExperimentReport.student_id == current_user.id,
    ).first()

    if existing:
        existing.content = content
        if file_path:
            existing.file_path = file_path
            existing.file_name = file_name
        existing.status = "submitted"
        existing.submitted_at = datetime.now()
        db.commit()
        db.refresh(existing)
        report = existing
    else:
        report = ExperimentReport(
            experiment_id=experiment_id,
            student_id=current_user.id,
            content=content,
            file_path=file_path,
            file_name=file_name,
        )
        db.add(report)
        db.commit()
        db.refresh(report)

    return ReportOut(
        id=report.id, experiment_id=report.experiment_id,
        student_id=report.student_id, student_name=current_user.name,
        content=report.content, file_name=report.file_name,
        score=report.score, feedback=report.feedback, status=report.status,
        submitted_at=report.submitted_at, graded_at=report.graded_at,
    )


@router.post("/reports/{report_id}/grade")
def grade_report(
    report_id: int,
    data: ReportGrade,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """批改实验报告"""
    report = db.query(ExperimentReport).filter(ExperimentReport.id == report_id).first()
    if not report:
        raise HTTPException(404, "报告不存在")

    if report.experiment.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权批改")

    report.score = data.score
    report.feedback = data.feedback
    report.status = "graded"
    report.graded_at = datetime.now()

    notification = Notification(
        title=f"实验报告已批改：{report.experiment.title}",
        content=f"您的实验报告已批改，得分：{data.score}/{report.experiment.total_score}",
        type="homework",
        sender_id=current_user.id,
        receiver_id=report.student_id,
    )
    db.add(notification)
    db.commit()
    return {"success": True}


@router.post("/reports/{report_id}/return")
def return_report(
    report_id: int,
    data: dict = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """打回实验报告"""
    report = db.query(ExperimentReport).filter(ExperimentReport.id == report_id).first()
    if not report:
        raise HTTPException(404, "报告不存在")

    if report.experiment.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权打回")

    feedback = (data or {}).get("feedback", "请重做")
    report.status = "returned"
    report.feedback = feedback
    report.graded_at = datetime.now()
    db.commit()
    return {"success": True}


@router.get("/reports/{report_id}/download")
def download_report(
    report_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """下载实验报告附件"""
    report = db.query(ExperimentReport).filter(ExperimentReport.id == report_id).first()
    if not report:
        raise HTTPException(404, "报告不存在")
    
    # 权限检查：教师只能下载自己实验的报告，学生只能下载自己的报告
    if current_user.role == "teacher":
        if report.experiment.teacher_id != current_user.id and current_user.role != "admin":
            raise HTTPException(403, "无权下载此报告")
    elif current_user.role == "student":
        if report.student_id != current_user.id:
            raise HTTPException(403, "无权下载此报告")
    
    if not report.file_path or not os.path.exists(report.file_path):
        raise HTTPException(404, "文件不存在")

    return FileResponse(report.file_path, filename=report.file_name)
