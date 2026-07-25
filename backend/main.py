import asyncio
import logging
import os
from contextlib import asynccontextmanager

# 强制 HuggingFace 离线模式：模型已缓存，不联网检查更新（避免网络超时卡住）
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.api.routes import router as ws_router, _warmup_models
from backend.api.classroom_routes import router as classroom_router
from backend.api.stats_routes import router as stats_router
from backend.api.chat_routes import router as chat_router
from backend.api.person_routes import router as person_router
from backend.api.rag_routes import router as rag_router
from backend.api.oj_routes import router as oj_router
from backend.api.auth_routes import router as auth_router
from backend.api.import_routes import router as import_router
from backend.api.notification_routes import router as notification_router
from backend.api.homework_routes import router as homework_router
from backend.api.checkin_routes import router as checkin_router
from backend.api.exam_routes import router as exam_router
from backend.api.question_bank_routes import router as question_bank_router
from backend.api.material_routes import router as material_router
from backend.api.grade_routes import router as grade_router
from backend.api.alert_routes import router as alert_router
from backend.api.teaching_plan_routes import router as teaching_plan_router
from backend.api.leave_routes import router as leave_router
from backend.api.experiment_routes import router as experiment_router
from backend.api.llm_routes import router as llm_router
from backend.api.grading_routes import router as grading_router
from backend.api.attribution_routes import router as attribution_router
from backend.api.correction_routes import router as correction_router
from backend.api.similar_question_routes import router as similar_question_router
from backend.api.answer_sheet_routes import router as answer_sheet_router
from backend.api.exam_compose_routes import template_router, compose_router, review_router
from backend.core.database import init_db, SessionLocal
from backend.core.security import hash_password
from backend.core.config import settings
from backend.models import tables  # noqa: F401 — 确保 Base 能发现所有表
from backend.models.tables import RegisteredPerson, OjProblem, OjTestCase, ExamTemplate

# 配置 RAG 检索链路日志
os.makedirs("logs", exist_ok=True)
_rag_logger = logging.getLogger("rag")
_rag_logger.setLevel(logging.INFO)
_rag_handler = logging.FileHandler("logs/rag_query.log", encoding="utf-8")
_rag_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
_rag_logger.addHandler(_rag_handler)


def _create_default_accounts():
    """启动时创建默认测试账号（如不存在）
    
    生产环境可设置环境变量 CREATE_DEFAULT_ACCOUNTS=false 禁用此功能。
    """
    import os
    if os.getenv("CREATE_DEFAULT_ACCOUNTS", "true").lower() in ("false", "0", "no"):
        return
    
    db = SessionLocal()
    try:
        default_accounts = [
            {"name": "管理员", "role": "admin", "username": "admin", "password": "admin123"},
            {"name": "张老师", "role": "teacher", "username": "teacher", "password": "teacher123"},
            {"name": "李同学", "role": "student", "username": "student", "password": "student123"},
        ]
        for acc in default_accounts:
            existing = db.query(RegisteredPerson).filter(RegisteredPerson.username == acc["username"]).first()
            if not existing:
                person = RegisteredPerson(
                    name=acc["name"],
                    role=acc["role"],
                    username=acc["username"],
                    password_hash=hash_password(acc["password"]),
                    face_embedding="[]",
                )
                db.add(person)
        db.commit()
    finally:
        db.close()


def _preload_reranker():
    """预加载 reranker 模型（避免首次 deep 请求的 7s 加载延迟）"""
    try:
        from backend.core.config import settings
        if not settings.RAG_RERANKER_ENABLED:
            return
        from backend.api.rag_routes import get_rag_service
        svc = get_rag_service()
        svc._get_reranker()
        logging.getLogger("rag").info("reranker_preloaded")
    except Exception as e:
        logging.getLogger("rag").warning("reranker_preload_failed: %s", e)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    _create_default_accounts()
    _seed_oj_problems()
    _seed_builtin_templates()
    # 模型预热改为后台线程，不阻塞服务器启动
    import threading
    threading.Thread(target=_warmup_models, daemon=True, name="model-warmup").start()
    # RAG reranker 也改为后台线程
    threading.Thread(target=_preload_reranker, daemon=True, name="reranker-preload").start()
    yield


def _seed_oj_problems():
    """预置 OJ 题目和测试用例"""
    db = SessionLocal()
    try:
        if db.query(OjProblem).count() > 0:
            return

        problems_data = [
            {
                "title": "A + B 问题",
                "description": "计算两个整数的和。",
                "input_format": "输入包含两个整数 a 和 b，用空格分隔。\n范围：-10^9 ≤ a, b ≤ 10^9",
                "output_format": "输出 a + b 的值。",
                "sample_input": "1 2",
                "sample_output": "3",
                "hint": "使用 scanf/cin 读取两个整数，输出它们的和。",
                "difficulty": "简单",
                "test_cases": [
                    {"input": "1 2", "expected_output": "3", "is_sample": True},
                    {"input": "10 20", "expected_output": "30", "is_sample": False},
                    {"input": "-5 5", "expected_output": "0", "is_sample": False},
                    {"input": "1000000000 1000000000", "expected_output": "2000000000", "is_sample": False},
                    {"input": "0 0", "expected_output": "0", "is_sample": False},
                ],
            },
            {
                "title": "数组求和",
                "description": "计算包含 N 个整数的数组的总和。",
                "input_format": "第一行包含一个整数 N（1 ≤ N ≤ 1000）。\n第二行包含 N 个整数，用空格分隔。\n每个整数的绝对值不超过 10^5。",
                "output_format": "输出 N 个整数的总和。",
                "sample_input": "3\n1 2 3",
                "sample_output": "6",
                "hint": "注意使用 long long 防止溢出。",
                "difficulty": "简单",
                "test_cases": [
                    {"input": "3\n1 2 3", "expected_output": "6", "is_sample": True},
                    {"input": "5\n10 20 30 40 50", "expected_output": "150", "is_sample": False},
                    {"input": "1\n42", "expected_output": "42", "is_sample": False},
                    {"input": "4\n-1 -2 -3 -4", "expected_output": "-10", "is_sample": False},
                ],
            },
            {
                "title": "字符串反转",
                "description": "将给定的字符串反转输出。",
                "input_format": "输入一个字符串（长度不超过 1000，不包含空格）。",
                "output_format": "输出反转后的字符串。",
                "sample_input": "hello",
                "sample_output": "olleh",
                "hint": "可以使用双指针从两端向中间交换，或直接逆序输出。",
                "difficulty": "简单",
                "test_cases": [
                    {"input": "hello", "expected_output": "olleh", "is_sample": True},
                    {"input": "abcde", "expected_output": "edcba", "is_sample": False},
                    {"input": "a", "expected_output": "a", "is_sample": False},
                    {"input": "12345", "expected_output": "54321", "is_sample": False},
                ],
            },
            {
                "title": "寻找最大值",
                "description": "在给定的 N 个整数中找出最大的那个。",
                "input_format": "第一行包含一个整数 N（1 ≤ N ≤ 1000）。\n第二行包含 N 个整数，用空格分隔。\n每个整数的绝对值不超过 10^6。",
                "output_format": "输出最大的整数。",
                "sample_input": "3\n1 5 2",
                "sample_output": "5",
                "hint": "初始化最大值为第一个元素，然后逐个比较。",
                "difficulty": "中等",
                "test_cases": [
                    {"input": "3\n1 5 2", "expected_output": "5", "is_sample": True},
                    {"input": "5\n-10 -5 -3 -20 -1", "expected_output": "-1", "is_sample": False},
                    {"input": "1\n999999", "expected_output": "999999", "is_sample": False},
                    {"input": "4\n100 200 150 175", "expected_output": "200", "is_sample": False},
                ],
            },
            {
                "title": "斐波那契数列",
                "description": "计算第 N 个斐波那契数。斐波那契数列定义：F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)。",
                "input_format": "输入一个非负整数 N（0 ≤ N ≤ 30）。",
                "output_format": "输出第 N 个斐波那契数。",
                "sample_input": "5",
                "sample_output": "5",
                "hint": "使用循环而非递归以避免超时。",
                "difficulty": "中等",
                "test_cases": [
                    {"input": "5", "expected_output": "5", "is_sample": True},
                    {"input": "0", "expected_output": "0", "is_sample": False},
                    {"input": "1", "expected_output": "1", "is_sample": False},
                    {"input": "10", "expected_output": "55", "is_sample": False},
                    {"input": "20", "expected_output": "6765", "is_sample": False},
                ],
            },
        ]

        for p_data in problems_data:
            test_cases = p_data.pop("test_cases")
            admin = db.query(RegisteredPerson).filter(RegisteredPerson.username == "admin").first()
            problem = OjProblem(**p_data, created_by=admin.id if admin else None)
            db.add(problem)
            db.flush()
            for tc in test_cases:
                db.add(OjTestCase(problem_id=problem.id, **tc))
        db.commit()
    finally:
        db.close()


def _seed_builtin_templates():
    """预置内置试卷模板"""
    import json
    db = SessionLocal()
    try:
        if db.query(ExamTemplate).filter(ExamTemplate.is_builtin == True).count() > 0:
            return  # 已有内置模板，不重复创建

        templates = [
            {
                "name": "高中数学期中考试",
                "description": "标准100分制高中数学期中考试，覆盖代数、几何、概率",
                "total_score": 100,
                "duration": 90,
                "structure": [
                    {"type": "single", "count": 8, "score_per": 5, "knowledge": ["代数", "函数"], "difficulty": 2},
                    {"type": "single", "count": 4, "score_per": 5, "knowledge": ["几何", "三角"], "difficulty": 3},
                    {"type": "fill", "count": 4, "score_per": 5, "knowledge": ["数列", "不等式"], "difficulty": 3},
                    {"type": "essay", "count": 3, "score_per": 10, "knowledge": ["综合"], "difficulty": 4},
                ],
            },
            {
                "name": "初中数学月考",
                "description": "初中数学月考，侧重基础计算与应用",
                "total_score": 100,
                "duration": 60,
                "structure": [
                    {"type": "single", "count": 10, "score_per": 3, "knowledge": ["有理数", "整式", "方程"], "difficulty": 1},
                    {"type": "judge", "count": 5, "score_per": 2, "knowledge": ["基础概念"], "difficulty": 1},
                    {"type": "fill", "count": 5, "score_per": 4, "knowledge": ["计算", "应用题"], "difficulty": 2},
                    {"type": "essay", "count": 3, "score_per": 15, "knowledge": ["证明", "综合"], "difficulty": 3},
                ],
            },
            {
                "name": "随堂小测验",
                "description": "15分钟课堂小测验，快速检测学生掌握情况",
                "total_score": 50,
                "duration": 15,
                "structure": [
                    {"type": "single", "count": 8, "score_per": 4, "knowledge": [], "difficulty": 2},
                    {"type": "judge", "count": 6, "score_per": 3, "knowledge": [], "difficulty": 1},
                ],
            },
            {
                "name": "小学数学竞赛模拟",
                "description": "小学奥数竞赛模拟，强调思维和巧解",
                "total_score": 100,
                "duration": 90,
                "structure": [
                    {"type": "single", "count": 10, "score_per": 4, "knowledge": ["计算", "数论"], "difficulty": 3},
                    {"type": "single", "count": 5, "score_per": 6, "knowledge": ["组合", "逻辑推理"], "difficulty": 4},
                    {"type": "fill", "count": 5, "score_per": 6, "knowledge": ["几何", "应用题"], "difficulty": 3},
                ],
            },
            {
                "name": "大学高数期末考试",
                "description": "大学高等数学期末考试，覆盖极限、微积分、级数",
                "total_score": 100,
                "duration": 120,
                "structure": [
                    {"type": "single", "count": 6, "score_per": 4, "knowledge": ["极限", "连续"], "difficulty": 2},
                    {"type": "single", "count": 4, "score_per": 5, "knowledge": ["微分", "积分"], "difficulty": 3},
                    {"type": "fill", "count": 4, "score_per": 5, "knowledge": ["计算", "级数"], "difficulty": 3},
                    {"type": "essay", "count": 4, "score_per": 10, "knowledge": ["证明", "综合应用"], "difficulty": 4},
                ],
            },
            {
                "name": "全题型综合测试",
                "description": "包含所有题型的综合测试模板，适合自定义需求",
                "total_score": 100,
                "duration": 90,
                "structure": [
                    {"type": "single", "count": 5, "score_per": 4, "knowledge": [], "difficulty": 2},
                    {"type": "multi", "count": 3, "score_per": 6, "knowledge": [], "difficulty": 3},
                    {"type": "judge", "count": 5, "score_per": 2, "knowledge": [], "difficulty": 1},
                    {"type": "fill", "count": 4, "score_per": 5, "knowledge": [], "difficulty": 3},
                    {"type": "essay", "count": 3, "score_per": 13, "knowledge": [], "difficulty": 4},
                ],
            },
        ]

        for t_data in templates:
            t = ExamTemplate(
                name=t_data["name"],
                description=t_data["description"],
                total_score=t_data["total_score"],
                duration=t_data["duration"],
                structure=json.dumps(t_data["structure"], ensure_ascii=False),
                is_builtin=True,
                created_by=None,
            )
            db.add(t)
        db.commit()
        logging.getLogger("uvicorn").info(f"已创建 {len(templates)} 个内置试卷模板")
    finally:
        db.close()


app = FastAPI(title="ClassVision API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ws_router)
app.include_router(classroom_router)
app.include_router(stats_router)
app.include_router(chat_router)
app.include_router(person_router)
app.include_router(rag_router)
app.include_router(oj_router)
app.include_router(auth_router)
app.include_router(import_router)
app.include_router(notification_router)
app.include_router(homework_router)
app.include_router(checkin_router)
app.include_router(exam_router)
app.include_router(question_bank_router)
app.include_router(material_router)
app.include_router(grade_router)
app.include_router(alert_router)
app.include_router(teaching_plan_router)
app.include_router(leave_router)
app.include_router(experiment_router)
app.include_router(llm_router)
app.include_router(grading_router)
app.include_router(attribution_router)
app.include_router(correction_router)
app.include_router(similar_question_router)
app.include_router(answer_sheet_router)
app.include_router(template_router)
app.include_router(compose_router)
app.include_router(review_router)

# 挂载上传目录
os.makedirs("uploads/materials", exist_ok=True)
os.makedirs("uploads/experiments", exist_ok=True)
os.makedirs("uploads/answer_sheets", exist_ok=True)
os.makedirs("uploads/paper_templates", exist_ok=True)
os.makedirs("uploads/exam_answers", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# 挂载违规抓拍图片目录
os.makedirs("backend/static/cheating_proofs", exist_ok=True)
app.mount("/static", StaticFiles(directory="backend/static"), name="static")


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "ClassVision"}
