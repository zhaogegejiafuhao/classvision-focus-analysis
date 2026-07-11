import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router as ws_router, _warmup_models
from backend.api.classroom_routes import router as classroom_router
from backend.api.stats_routes import router as stats_router
from backend.api.chat_routes import router as chat_router
from backend.api.person_routes import router as person_router
from backend.api.rag_routes import router as rag_router
from backend.api.oj_routes import router as oj_router
from backend.api.auth_routes import router as auth_router
from backend.core.database import init_db, SessionLocal
from backend.core.security import hash_password
from backend.models import tables  # noqa: F401 — 确保 Base 能发现所有表
from backend.models.tables import RegisteredPerson, OjProblem, OjTestCase


def _create_default_accounts():
    """启动时创建默认测试账号（如不存在）"""
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


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    _create_default_accounts()
    _seed_oj_problems()
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, _warmup_models)
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


app = FastAPI(title="ClassVision API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "ClassVision"}
