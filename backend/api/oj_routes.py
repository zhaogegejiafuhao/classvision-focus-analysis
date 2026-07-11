"""OJ 路由：题目管理、提交判题、代码运行"""

import logging

import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from backend.core.config import settings
from backend.core.database import get_db
from backend.core.security import get_current_user, assert_teacher_or_admin, assert_owner_or_admin
from backend.models.tables import RegisteredPerson, OjProblem, OjTestCase, OjSubmission
from backend.models.schemas import (
    OjProblemOut,
    OjProblemDetail,
    OjProblemCreate,
    OjProblemUpdate,
    OjTestCaseOut,
    OjSubmissionCreate,
    OjSubmissionOut,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/oj", tags=["oj"])

JUDGER_URL = settings.OJ_JUDGER_URL.rstrip("/")
JUDGER_TIMEOUT = 30.0


class OjRunRequest(BaseModel):
    language: str = Field("cpp", description="语言: cpp/c/py3/java")
    source: str = Field(..., description="源代码")
    input: str = Field("", description="标准输入")
    max_cpu_time: int = Field(5000, description="最大 CPU 时间(ms)")
    max_memory: int = Field(256 * 1024 * 1024, description="最大内存(字节)")


class OjRunResponse(BaseModel):
    status: str = Field(..., description="AC/WA/TLE/MLE/RE/CE/SE")
    output: str = Field("", description="标准输出")
    error: str = Field("", description="标准错误/编译错误")
    cpu_time: int = Field(0, description="CPU 耗时(ms)")
    memory: int = Field(0, description="内存占用(字节)")


# ===== 基础健康检查 / 自由运行 =====

@router.get("/health")
async def oj_health():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{JUDGER_URL}/ping")
        if resp.status_code == 200 and resp.text.strip() == "pong":
            return {"status": "ok", "judger": "alive"}
        return {"status": "degraded", "judger": f"unexpected: {resp.text}"}
    except Exception as e:
        logger.warning(f"judger health check failed: {e}")
        return {"status": "down", "judger": str(e)}


@router.post("/run", response_model=OjRunResponse)
async def oj_run(req: OjRunRequest):
    payload = {
        "language": req.language,
        "source": req.source,
        "input": req.input,
        "max_cpu_time": req.max_cpu_time,
        "max_memory": req.max_memory,
    }
    try:
        async with httpx.AsyncClient(timeout=JUDGER_TIMEOUT) as client:
            resp = await client.post(f"{JUDGER_URL}/run", json=payload)
        if resp.status_code != 200:
            raise HTTPException(502, f"judger 返回非 200: {resp.status_code} {resp.text}")
        data = resp.json()
        return OjRunResponse(
            status=data.get("status", "SE"),
            output=data.get("output", ""),
            error=data.get("error", ""),
            cpu_time=data.get("cpu_time", 0),
            memory=data.get("memory", 0),
        )
    except httpx.RequestError as e:
        logger.error(f"judger 连接失败: {e}")
        raise HTTPException(503, f"judger 不可达: {e}")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"oj_run 异常: {e}", exc_info=True)
        raise HTTPException(500, f"运行失败: {e}")


# ===== 题目管理 =====

@router.get("/problems", response_model=list[OjProblemOut])
def list_problems(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    problems = db.query(OjProblem).order_by(OjProblem.id.asc()).all()
    result = []
    for p in problems:
        submitted = db.query(OjSubmission).filter(OjSubmission.problem_id == p.id).count()
        accepted = db.query(OjSubmission).filter(
            OjSubmission.problem_id == p.id,
            OjSubmission.status == "AC",
        ).count()
        result.append(OjProblemOut(
            id=p.id,
            title=p.title,
            difficulty=p.difficulty,
            time_limit=p.time_limit,
            memory_limit=p.memory_limit,
            submitted_count=submitted,
            accepted_count=accepted,
            created_by=p.created_by,
        ))
    return result


@router.get("/problems/{pid}", response_model=OjProblemDetail)
def get_problem(
    pid: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    problem = db.query(OjProblem).filter(OjProblem.id == pid).first()
    if not problem:
        raise HTTPException(404, "题目不存在")
    sample_cases = db.query(OjTestCase).filter(
        OjTestCase.problem_id == pid,
        OjTestCase.is_sample == True,
    ).all()
    return OjProblemDetail(
        id=problem.id,
        title=problem.title,
        description=problem.description,
        input_format=problem.input_format,
        output_format=problem.output_format,
        sample_input=problem.sample_input,
        sample_output=problem.sample_output,
        hint=problem.hint,
        time_limit=problem.time_limit,
        memory_limit=problem.memory_limit,
        difficulty=problem.difficulty,
        created_by=problem.created_by,
        sample_test_cases=[OjTestCaseOut.model_validate(tc) for tc in sample_cases],
    )


@router.post("/problems", response_model=OjProblemDetail)
def create_problem(
    data: OjProblemCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建题目（仅教师/管理员）"""
    assert_teacher_or_admin(current_user)
    problem = OjProblem(
        title=data.title,
        description=data.description,
        input_format=data.input_format,
        output_format=data.output_format,
        sample_input=data.sample_input,
        sample_output=data.sample_output,
        hint=data.hint,
        time_limit=data.time_limit,
        memory_limit=data.memory_limit,
        difficulty=data.difficulty,
        created_by=current_user.id,
    )
    db.add(problem)
    db.flush()
    for tc in data.test_cases:
        db.add(OjTestCase(
            problem_id=problem.id,
            input=tc.input,
            expected_output=tc.expected_output,
            is_sample=tc.is_sample,
        ))
    db.commit()
    db.refresh(problem)
    sample_cases = db.query(OjTestCase).filter(
        OjTestCase.problem_id == problem.id,
        OjTestCase.is_sample == True,
    ).all()
    return OjProblemDetail(
        id=problem.id,
        title=problem.title,
        description=problem.description,
        input_format=problem.input_format,
        output_format=problem.output_format,
        sample_input=problem.sample_input,
        sample_output=problem.sample_output,
        hint=problem.hint,
        time_limit=problem.time_limit,
        memory_limit=problem.memory_limit,
        difficulty=problem.difficulty,
        created_by=problem.created_by,
        sample_test_cases=[OjTestCaseOut.model_validate(tc) for tc in sample_cases],
    )


@router.put("/problems/{pid}", response_model=OjProblemDetail)
def update_problem(
    pid: int,
    data: OjProblemUpdate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """编辑题目（创建者或管理员）"""
    problem = db.query(OjProblem).filter(OjProblem.id == pid).first()
    if not problem:
        raise HTTPException(404, "题目不存在")
    assert_owner_or_admin(problem.created_by, current_user)

    update_fields = [
        "title", "description", "input_format", "output_format",
        "sample_input", "sample_output", "hint", "time_limit",
        "memory_limit", "difficulty",
    ]
    for field in update_fields:
        val = getattr(data, field)
        if val is not None:
            setattr(problem, field, val)

    if data.test_cases is not None:
        db.query(OjTestCase).filter(OjTestCase.problem_id == pid).delete()
        for tc in data.test_cases:
            db.add(OjTestCase(
                problem_id=pid,
                input=tc.input,
                expected_output=tc.expected_output,
                is_sample=tc.is_sample,
            ))

    db.commit()
    db.refresh(problem)
    sample_cases = db.query(OjTestCase).filter(
        OjTestCase.problem_id == pid,
        OjTestCase.is_sample == True,
    ).all()
    return OjProblemDetail(
        id=problem.id,
        title=problem.title,
        description=problem.description,
        input_format=problem.input_format,
        output_format=problem.output_format,
        sample_input=problem.sample_input,
        sample_output=problem.sample_output,
        hint=problem.hint,
        time_limit=problem.time_limit,
        memory_limit=problem.memory_limit,
        difficulty=problem.difficulty,
        created_by=problem.created_by,
        sample_test_cases=[OjTestCaseOut.model_validate(tc) for tc in sample_cases],
    )


@router.delete("/problems/{pid}")
def delete_problem(
    pid: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除题目（创建者或管理员）"""
    problem = db.query(OjProblem).filter(OjProblem.id == pid).first()
    if not problem:
        raise HTTPException(404, "题目不存在")
    assert_owner_or_admin(problem.created_by, current_user)

    db.query(OjSubmission).filter(OjSubmission.problem_id == pid).delete()
    db.delete(problem)
    db.commit()
    return {"message": "题目已删除"}


# ===== 提交判题 =====

async def _run_code_against_judger(language: str, source: str, stdin: str, max_cpu_time: int, max_memory: int) -> dict:
    """调用 judger /run 运行一次代码，返回结果字典"""
    payload = {
        "language": language,
        "source": source,
        "input": stdin,
        "max_cpu_time": max_cpu_time,
        "max_memory": max_memory,
    }
    async with httpx.AsyncClient(timeout=JUDGER_TIMEOUT) as client:
        resp = await client.post(f"{JUDGER_URL}/run", json=payload)
    if resp.status_code != 200:
        raise HTTPException(502, f"judger 返回非 200: {resp.status_code}")
    return resp.json()


def _compare_output(actual: str, expected: str) -> bool:
    """比较输出，忽略行末空格和文件末尾空行"""
    def normalize(s: str) -> list[str]:
        return [line.rstrip() for line in s.strip().splitlines()]
    return normalize(actual) == normalize(expected)


@router.post("/submit", response_model=OjSubmissionOut)
async def submit_code(
    req: OjSubmissionCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    problem = db.query(OjProblem).filter(OjProblem.id == req.problem_id).first()
    if not problem:
        raise HTTPException(404, "题目不存在")

    test_cases = db.query(OjTestCase).filter(OjTestCase.problem_id == req.problem_id).all()
    if not test_cases:
        raise HTTPException(400, "该题目没有测试用例")

    submission = OjSubmission(
        user_id=current_user.id,
        problem_id=req.problem_id,
        language=req.language,
        source_code=req.source_code,
        status="Pending",
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)

    max_cpu = 0
    max_mem = 0
    final_status = "AC"
    error_msg = ""

    try:
        for tc in test_cases:
            result = await _run_code_against_judger(
                language=req.language,
                source=req.source_code,
                stdin=tc.input,
                max_cpu_time=problem.time_limit,
                max_memory=problem.memory_limit,
            )

            run_status = result.get("status", "SE")
            cpu = result.get("cpu_time", 0)
            mem = result.get("memory", 0)
            max_cpu = max(max_cpu, cpu)
            max_mem = max(max_mem, mem)

            if run_status == "CE":
                final_status = "CE"
                error_msg = result.get("error", "编译错误")
                break
            elif run_status == "TLE":
                final_status = "TLE"
                error_msg = f"超时 (耗时 {cpu}ms)"
                break
            elif run_status == "MLE":
                final_status = "MLE"
                error_msg = f"内存超限 ({mem} bytes)"
                break
            elif run_status == "RE":
                final_status = "RE"
                error_msg = result.get("error", "运行时错误") or "运行时错误"
                break
            elif run_status in ("WA", "SE"):
                final_status = "SE" if run_status == "SE" else "WA"
                error_msg = result.get("error", "")
                if run_status == "SE":
                    break
            else:
                actual_output = result.get("output", "")
                if not _compare_output(actual_output, tc.expected_output):
                    final_status = "WA"
                    error_msg = f"测试用例 {tc.id} 输出不匹配"
                    break
    except httpx.RequestError as e:
        final_status = "SE"
        error_msg = f"judger 不可达: {e}"
    except HTTPException as e:
        final_status = "SE"
        error_msg = e.detail if isinstance(e.detail, str) else str(e.detail)
    except Exception as e:
        final_status = "SE"
        error_msg = f"判题异常: {e}"
        logger.error(f"判题异常: {e}", exc_info=True)

    submission.status = final_status
    submission.cpu_time = max_cpu
    submission.memory = max_mem
    submission.error_message = error_msg
    db.commit()
    db.refresh(submission)

    problem_title = problem.title
    return OjSubmissionOut(
        id=submission.id,
        problem_id=submission.problem_id,
        problem_title=problem_title,
        language=submission.language,
        status=submission.status,
        cpu_time=submission.cpu_time,
        memory=submission.memory,
        error_message=submission.error_message,
        source_code=submission.source_code,
        submitted_at=submission.submitted_at,
    )


# ===== 提交记录 =====

@router.get("/submissions", response_model=list[OjSubmissionOut])
def list_submissions(
    problem_id: int | None = Query(None),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    query = db.query(OjSubmission).filter(OjSubmission.user_id == current_user.id)
    if problem_id is not None:
        query = query.filter(OjSubmission.problem_id == problem_id)
    submissions = query.order_by(OjSubmission.submitted_at.desc()).all()

    problem_cache = {}
    result = []
    for s in submissions:
        if s.problem_id not in problem_cache:
            p = db.query(OjProblem).filter(OjProblem.id == s.problem_id).first()
            problem_cache[s.problem_id] = p.title if p else ""
        result.append(OjSubmissionOut(
            id=s.id,
            problem_id=s.problem_id,
            problem_title=problem_cache[s.problem_id],
            language=s.language,
            status=s.status,
            cpu_time=s.cpu_time,
            memory=s.memory,
            error_message=s.error_message,
            source_code=s.source_code,
            submitted_at=s.submitted_at,
        ))
    return result


@router.get("/submissions/{sid}", response_model=OjSubmissionOut)
def get_submission(sid: int, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    submission = db.query(OjSubmission).filter(OjSubmission.id == sid).first()
    if not submission:
        raise HTTPException(404, "提交记录不存在")
    if submission.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权查看他人提交")
    problem = db.query(OjProblem).filter(OjProblem.id == submission.problem_id).first()
    return OjSubmissionOut(
        id=submission.id,
        problem_id=submission.problem_id,
        problem_title=problem.title if problem else "",
        language=submission.language,
        status=submission.status,
        cpu_time=submission.cpu_time,
        memory=submission.memory,
        error_message=submission.error_message,
        source_code=submission.source_code,
        submitted_at=submission.submitted_at,
    )
