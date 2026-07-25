#!/usr/bin/env python3
"""
ClassVision 测试数据填充脚本
填充所有表的数据，让每个功能模块都有可测试的数据。

用法：
  cd D:\ClassVision
  set PYTHONPATH=D:\ClassVision
  .venv\Scripts\python.exe -m backend.seed_data
"""

import sys
import os
import random
from datetime import datetime, timedelta
from pathlib import Path

# 确保项目根目录在 sys.path 中
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker

from backend.core.database import Base
from backend.models.tables import (
    Department, RegisteredPerson, Classroom, ClassroomMember, Student,
    AttentionRecord, ExamRiskRecord, Report, ChatMessage,
    KnowledgeDocument, KnowledgeChunk,
    OjProblem, OjTestCase, OjSubmission,
    RagConversation, RagMessage,
    Notification, NotificationReadStatus,
    Attendance, CheckinSession,
    Homework, HomeworkAttachment, HomeworkSubmission, SubmissionAttachment,
    Exam, Question, ExamSubmission, Answer,
    QuestionBank, CourseMaterial, GradeConfig, UsualScore,
    TeachingPlan, ExtensionRequest, LeaveRequest,
    Experiment, ExperimentReport,
    GradingResult, KnowledgeAnalysis, CorrectionRecord, SimilarQuestion,
    PaperTemplate, QuestionRegion,
    AnswerRegradeHistory,
)
from backend.core.security import hash_password

# ─── 配置 ───────────────────────────────────────────────
# 数据库路径：与 config.py 保持一致，使用根目录的 classvision.db
DB_PATH = PROJECT_ROOT / "classvision.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

CLEAR_FIRST = True  # True = 先清空再插入；False = 追加

# ─── 伪随机种子（保证每次运行结果一致）─────────────────
random.seed(42)

# ─── 工具函数 ───────────────────────────────────────────
def rand_dt(days_ago=30):
    """随机 datetime，在 N 天前到现在之间"""
    delta = random.randint(0, days_ago * 86400)
    return datetime.now() - timedelta(seconds=delta)

def rand_float(a, b, n=2):
    return round(random.uniform(a, b), n)


def main():
    engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})
    # 启用外键
    from sqlalchemy import event
    @event.listens_for(engine, "connect")
    def _fk(dbapi_connection, _):
        dbapi_connection.cursor().execute("PRAGMA foreign_keys=ON")

    # 先建表
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    db = Session()

    if CLEAR_FIRST:
        print("🗑️  清空旧数据...")
        # 按依赖逆序删除
        for tbl in [
            "answer_regrade_history", "question_region", "paper_template",
            "similar_question", "correction_record", "knowledge_analysis",
            "grading_result", "experiment_report", "experiment",
            "leave_request", "extension_request", "teaching_plan",
            "usual_score", "grade_config", "course_material", "question_bank",
            "answer", "exam_submission", "question", "exam",
            "submission_attachment", "homework_submission", "homework_attachment", "homework",
            "attendance", "checkin_session",
            "notification_read_status", "notification",
            "rag_message", "rag_conversation",
            "oj_submission", "oj_test_case", "oj_problem",
            "knowledge_chunk", "knowledge_document",
            "exam_risk_record", "attention_record", "chat_message", "report",
            "student", "classroom_member",
            "classroom", "registered_person", "department",
        ]:
            try:
                db.execute(text(f"DELETE FROM {tbl}"))
            except Exception:
                pass
        db.commit()
        print("  ✅ 旧数据已清空")

    # ─── 1. Department ─────────────────────────────────
    print("📦 插入 Department...")
    depts = [
        Department(name="计算机科学系", type="department"),
        Department(name="数学系", type="department"),
        Department(name="物理系", type="department"),
        Department(name="2024级1班", type="class"),
        Department(name="2024级2班", type="class"),
        Department(name="2024级3班", type="class"),
    ]
    db.add_all(depts)
    db.flush()
    dept_cs, dept_math, dept_phys = depts[0], depts[1], depts[2]
    dept_c1, dept_c2, dept_c3 = depts[3], depts[4], depts[5]

    # ─── 2. RegisteredPerson ──────────────────────────
    print("📦 插入 RegisteredPerson...")
    # 管理员
    admin = RegisteredPerson(
        name="管理员", role="admin", username="admin",
        password_hash=hash_password("123456"),
        employee_id="T000001", department_id=dept_cs.id,
        email="admin@classvision.cn", phone="13800000000",
    )
    db.add(admin)
    db.flush()

    # 教师
    teachers = []
    teacher_data = [
        ("张老师", "zhang", "T001001", dept_cs.id, "zhang@cv.cn"),
        ("李老师", "li", "T001002", dept_math.id, "li@cv.cn"),
        ("王老师", "wang", "T001003", dept_phys.id, "wang@cv.cn"),
    ]
    for name, uname, eid, did, email in teacher_data:
        t = RegisteredPerson(
            name=name, role="teacher", username=uname,
            password_hash=hash_password("123456"),
            employee_id=eid, department_id=did, email=email,
        )
        db.add(t)
        teachers.append(t)
    db.flush()

    # 学生
    students = []
    student_names = [
        "陈思远", "林雨桐", "赵明轩", "刘诗涵", "黄子涵",
        "吴佳怡", "郑浩然", "孙语嫣", "杨博文", "周心怡",
        "许睿泽", "何欣怡", "罗天宇", "谢雨萱", "韩宇轩",
        "唐梦瑶", "冯子墨", "曹嘉欣", "邓浩宇", "肖雨彤",
    ]
    for i, name in enumerate(student_names):
        dept = [dept_c1, dept_c2, dept_c3][i % 3]
        s = RegisteredPerson(
            name=name, role="student", username=f"stu{i+1:02d}",
            password_hash=hash_password("123456"),
            employee_id=f"S2024{i+1:03d}", department_id=dept.id,
            major="计算机科学与技术" if i % 3 == 0 else ("数学" if i % 3 == 1 else "物理学"),
            email=f"stu{i+1:02d}@cv.cn",
        )
        db.add(s)
        students.append(s)
    db.flush()
    print(f"  ✅ 1 admin + {len(teachers)} teachers + {len(students)} students")

    # ─── 3. Classroom ─────────────────────────────────
    print("📦 插入 Classroom...")
    now = datetime.now()
    classrooms = [
        Classroom(
            name="高等数学 A", teacher=teachers[1].name, teacher_person_id=teachers[1].id,
            course_code="MATH101", is_public=True, invite_code="MATH1012024A",
            started_at=now - timedelta(days=15, hours=2), ended_at=now - timedelta(days=15),
            duration=90, avg_attention=72.5, total_students=8,
        ),
        Classroom(
            name="数据结构与算法", teacher=teachers[0].name, teacher_person_id=teachers[0].id,
            course_code="CS201", is_public=True, invite_code="CS2012024A",
            started_at=now - timedelta(days=7, hours=1), ended_at=None,
            duration=0, avg_attention=68.3, total_students=7,
        ),
        Classroom(
            name="大学物理 B", teacher=teachers[2].name, teacher_person_id=teachers[2].id,
            course_code="PHYS102", is_public=True, invite_code="PHYS1022024B",
            started_at=now - timedelta(days=3, hours=1, minutes=30), ended_at=now - timedelta(days=3),
            duration=90, avg_attention=65.0, total_students=5,
        ),
        Classroom(
            name="Python 程序设计", teacher=teachers[0].name, teacher_person_id=teachers[0].id,
            course_code="CS101", is_public=True, invite_code="CS1012024A",
            started_at=None, ended_at=None,
            duration=0, avg_attention=0, total_students=0,  # 未开始
        ),
    ]
    db.add_all(classrooms)
    db.flush()
    cls_math, cls_algo, cls_phys, cls_py = classrooms

    # ─── 4. ClassroomMember ───────────────────────────
    print("📦 插入 ClassroomMember...")
    members = []
    # 高等数学: 学生 0-7
    for s in students[:8]:
        members.append(ClassroomMember(classroom_id=cls_math.id, person_id=s.id))
    # 数据结构: 学生 3-9
    for s in students[3:10]:
        members.append(ClassroomMember(classroom_id=cls_algo.id, person_id=s.id))
    # 大学物理: 学生 10-14
    for s in students[10:15]:
        members.append(ClassroomMember(classroom_id=cls_phys.id, person_id=s.id))
    # Python: 学生 0-4
    for s in students[:5]:
        members.append(ClassroomMember(classroom_id=cls_py.id, person_id=s.id))
    db.add_all(members)

    # ─── 5. Student（课堂内学生跟踪记录）───────────────
    print("📦 插入 Student...")
    stu_records = []
    for s in students[:8]:
        stu_records.append(Student(classroom_id=cls_math.id, track_id=len(stu_records)+1, name=s.name, person_id=s.id))
    for s in students[3:10]:
        stu_records.append(Student(classroom_id=cls_algo.id, track_id=len(stu_records)+1, name=s.name, person_id=s.id))
    for s in students[10:15]:
        stu_records.append(Student(classroom_id=cls_phys.id, track_id=len(stu_records)+1, name=s.name, person_id=s.id))
    db.add_all(stu_records)
    db.flush()

    # ─── 6. AttentionRecord ───────────────────────────
    print("📦 插入 AttentionRecord...")
    att_records = []
    for sr in stu_records[:8]:  # 高等数学课堂
        for j in range(5):
            att_records.append(AttentionRecord(
                student_id=sr.person_id, student_record_id=sr.id,
                classroom_id=cls_math.id, timestamp=rand_dt(15),
                attention_score=rand_float(40, 100), pitch=rand_float(-15, 15),
                yaw=rand_float(-15, 15), roll=rand_float(-10, 10),
                ear=rand_float(0.2, 0.4), gaze_score=rand_float(0.5, 1.0),
                pose_score=rand_float(0.5, 1.0), fatigue_score=rand_float(0, 0.5),
            ))
    for sr in stu_records[8:15]:  # 数据结构课堂
        for j in range(5):
            att_records.append(AttentionRecord(
                student_id=sr.person_id, student_record_id=sr.id,
                classroom_id=cls_algo.id, timestamp=rand_dt(7),
                attention_score=rand_float(30, 95), pitch=rand_float(-20, 20),
                yaw=rand_float(-20, 20), roll=rand_float(-10, 10),
                ear=rand_float(0.15, 0.45), gaze_score=rand_float(0.3, 1.0),
                pose_score=rand_float(0.3, 1.0), fatigue_score=rand_float(0, 0.7),
            ))
    db.add_all(att_records)

    # ─── 7. ExamRiskRecord ────────────────────────────
    print("📦 插入 ExamRiskRecord...")
    risk_records = []
    for sr in stu_records[8:15]:
        for j in range(3):
            risk_level = random.choice(["low", "medium", "high"])
            risk_records.append(ExamRiskRecord(
                student_id=sr.person_id, student_record_id=sr.id,
                classroom_id=cls_algo.id, timestamp=rand_dt(7),
                risk_level=risk_level,
                gaze_deviation_duration=rand_float(0, 30) if risk_level != "low" else 0,
                head_down_duration=rand_float(0, 20) if risk_level == "high" else 0,
                head_turn_events=random.randint(0, 5) if risk_level != "low" else 0,
                cheating_object_nearby=risk_level == "high" and random.random() > 0.5,
                attention_score=rand_float(30, 90),
            ))
    db.add_all(risk_records)

    # ─── 8. Report ────────────────────────────────────
    print("📦 插入 Report...")
    reports = [
        Report(classroom_id=cls_math.id, content="## 高等数学 A 课堂分析报告\n\n本次课堂整体注意力水平良好，平均注意力 72.5 分。\n\n- 出勤率: 100%\n- 高注意力(≥80): 3人\n- 中等注意力(60-80): 4人\n- 低注意力(<60): 1人\n\n### 建议\n1. 加强课堂互动环节\n2. 适当增加小组讨论"),
        Report(classroom_id=cls_phys.id, content="## 大学物理 B 课堂分析报告\n\n课堂注意力偏低，部分学生疲劳度较高。\n\n- 出勤率: 100%\n- 平均注意力: 65.0\n- 疲劳人次: 3"),
    ]
    db.add_all(reports)

    # ─── 9. ChatMessage ───────────────────────────────
    print("📦 插入 ChatMessage...")
    chats = [
        ChatMessage(classroom_id=cls_math.id, role="user", content="这节课的出勤情况怎么样？", timestamp=rand_dt(14)),
        ChatMessage(classroom_id=cls_math.id, role="assistant", content="本次课堂共8名学生出席，出勤率100%。其中3人注意力较高，4人中等，1人偏低。", timestamp=rand_dt(14)),
        ChatMessage(classroom_id=cls_algo.id, role="user", content="哪些学生需要重点关注？", timestamp=rand_dt(6)),
        ChatMessage(classroom_id=cls_algo.id, role="assistant", content="根据课堂行为分析，以下学生需要关注：\n1. 林雨桐 - 注意力持续偏低\n2. 黄子涵 - 频繁低头\n3. 吴佳怡 - 疲劳指标较高", timestamp=rand_dt(6)),
    ]
    db.add_all(chats)

    # ─── 10. KnowledgeDocument + KnowledgeChunk ───────
    print("📦 插入 KnowledgeDocument + KnowledgeChunk...")
    docs = [
        KnowledgeDocument(filename="高等数学教材.pdf", file_path="data/knowledge/math.pdf",
                         file_type="pdf", total_chunks=3, indexed=True, uploaded_by=teachers[1].id, visibility="public"),
        KnowledgeDocument(filename="数据结构讲义.md", file_path="data/knowledge/ds.md",
                         file_type="md", total_chunks=2, indexed=True, uploaded_by=teachers[0].id, visibility="staff"),
        KnowledgeDocument(filename="物理实验指南.pdf", file_path="data/knowledge/physics.pdf",
                         file_type="pdf", total_chunks=2, indexed=True, uploaded_by=teachers[2].id, visibility="private"),
    ]
    db.add_all(docs)
    db.flush()

    chunks = [
        KnowledgeChunk(document_id=docs[0].id, chunk_index=0, content="微积分基本定理：若f在[a,b]上连续，F是f的一个原函数，则∫[a,b]f(x)dx = F(b)-F(a)。", embedding_stored=True, is_parent=True),
        KnowledgeChunk(document_id=docs[0].id, chunk_index=1, content="定积分的换元法：设f(x)在[a,b]上连续，x=φ(t)在[α,β]上单调且有连续导数，则∫[a,b]f(x)dx = ∫[α,β]f(φ(t))φ'(t)dt。", embedding_stored=True, is_parent=False, parent_chunk_id=None),
        KnowledgeChunk(document_id=docs[0].id, chunk_index=2, content="洛必达法则：对于0/0或∞/∞型未定式，若lim f'(x)/g'(x)存在，则lim f(x)/g(x) = lim f'(x)/g'(x)。", embedding_stored=True, is_parent=False, parent_chunk_id=None),
        KnowledgeChunk(document_id=docs[1].id, chunk_index=0, content="二叉树的前序遍历：根→左→右。中序遍历：左→根→右。后序遍历：左→右→根。", embedding_stored=True, is_parent=True),
        KnowledgeChunk(document_id=docs[1].id, chunk_index=1, content="哈希表冲突解决方法：开放寻址法（线性探测、二次探测）、链地址法、再哈希法。", embedding_stored=True, is_parent=False, parent_chunk_id=None),
        KnowledgeChunk(document_id=docs[2].id, chunk_index=0, content="牛顿第二定律：F=ma，物体加速度与合外力成正比，与质量成反比。", embedding_stored=True, is_parent=True),
        KnowledgeChunk(document_id=docs[2].id, chunk_index=1, content="动量守恒定律：当系统不受外力或外力之和为零时，系统总动量保持不变。", embedding_stored=True, is_parent=False, parent_chunk_id=None),
    ]
    db.add_all(chunks)

    # ─── 11. OjProblem + OjTestCase + OjSubmission ────
    print("📦 插入 OjProblem + OjTestCase + OjSubmission...")
    oj_problems = [
        OjProblem(title="两数之和", description="给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。",
                  input_format="第一行输入 n 和 target，第二行输入 n 个整数", output_format="输出两个下标（从0开始），用空格分隔",
                  sample_input="4 9\n2 7 11 15", sample_output="0 1",
                  hint="你可以假设每种输入只会对应一个答案", difficulty="简单", created_by=teachers[0].id),
        OjProblem(title="反转链表", description="给你单链表的头节点 head，请你反转链表，并返回反转后的链表。",
                  input_format="第一行输入 n，第二行输入 n 个整数", output_format="输出反转后的链表",
                  sample_input="5\n1 2 3 4 5", sample_output="5 4 3 2 1",
                  hint="递归或迭代均可", difficulty="中等", created_by=teachers[0].id),
        OjProblem(title="爬楼梯", description="假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？",
                  input_format="一个整数 n", output_format="一个整数表示方法数",
                  sample_input="3", sample_output="3",
                  hint="动态规划", difficulty="简单", created_by=teachers[0].id),
    ]
    db.add_all(oj_problems)
    db.flush()

    oj_cases = [
        OjTestCase(problem_id=oj_problems[0].id, input="4 9\n2 7 11 15", expected_output="0 1", is_sample=True),
        OjTestCase(problem_id=oj_problems[0].id, input="3 6\n3 2 4", expected_output="1 2", is_sample=False),
        OjTestCase(problem_id=oj_problems[1].id, input="5\n1 2 3 4 5", expected_output="5 4 3 2 1", is_sample=True),
        OjTestCase(problem_id=oj_problems[2].id, input="3", expected_output="3", is_sample=True),
        OjTestCase(problem_id=oj_problems[2].id, input="5", expected_output="8", is_sample=False),
    ]
    db.add_all(oj_cases)

    oj_subs = [
        OjSubmission(user_id=students[0].id, problem_id=oj_problems[0].id, language="python",
                     source_code="class Solution:\n    def twoSum(self, nums, target):\n        d = {}\n        for i, n in enumerate(nums):\n            if target - n in d:\n                return [d[target-n], i]\n            d[n] = i",
                     status="Accepted", cpu_time=52, memory=16384),
        OjSubmission(user_id=students[1].id, problem_id=oj_problems[0].id, language="python",
                     source_code="# 暴力法\ndef twoSum(nums, target):\n    for i in range(len(nums)):\n        for j in range(i+1,len(nums)):\n            if nums[i]+nums[j]==target:\n                return [i,j]",
                     status="Accepted", cpu_time=120, memory=16384),
        OjSubmission(user_id=students[0].id, problem_id=oj_problems[2].id, language="python",
                     source_code="def climbStairs(n):\n    a, b = 1, 1\n    for _ in range(n):\n        a, b = b, a+b\n    return a",
                     status="Accepted", cpu_time=28, memory=8192),
        OjSubmission(user_id=students[2].id, problem_id=oj_problems[1].id, language="python",
                     source_code="def reverseList(head):\n    # TODO", status="Compile Error",
                     error_message="SyntaxError: incomplete input", cpu_time=0, memory=0),
    ]
    db.add_all(oj_subs)

    # ─── 12. RagConversation + RagMessage ─────────────
    print("📦 插入 RagConversation + RagMessage...")
    rag_convs = [
        RagConversation(user_id=teachers[1].id, title="微积分提问", state="idle"),
        RagConversation(user_id=teachers[0].id, title="数据结构讨论", state="idle"),
        RagConversation(user_id=students[0].id, title="高数复习", state="idle"),
    ]
    db.add_all(rag_convs)
    db.flush()

    rag_msgs = [
        RagMessage(conversation_id=rag_convs[0].id, role="user", content="请解释牛顿-莱布尼茨公式", is_followup=False),
        RagMessage(conversation_id=rag_convs[0].id, role="assistant", content="牛顿-莱布尼茨公式（微积分基本定理）建立了定积分与不定积分之间的联系：∫[a,b]f(x)dx = F(b)-F(a)，其中F是f的一个原函数。", is_followup=False, retrieved_chunks='[{"chunk_id": 1, "score": 0.92}]'),
        RagMessage(conversation_id=rag_convs[1].id, role="user", content="哈希冲突怎么解决？", is_followup=False),
        RagMessage(conversation_id=rag_convs[1].id, role="assistant", content="常见的哈希冲突解决方法有：1. 开放寻址法 2. 链地址法 3. 再哈希法。其中链地址法是最常用的方案。", is_followup=False),
        RagMessage(conversation_id=rag_convs[2].id, role="user", content="洛必达法则怎么用？", is_followup=False),
        RagMessage(conversation_id=rag_convs[2].id, role="assistant", content="洛必达法则适用于0/0或∞/∞型未定式，通过对分子分母分别求导来求极限。", is_followup=False),
    ]
    db.add_all(rag_msgs)

    # ─── 13. Notification + NotificationReadStatus ───
    print("📦 插入 Notification + NotificationReadStatus...")
    notifs = [
        Notification(title="新作业发布", content="高等数学A第3次作业已发布，截止日期为下周五", type="homework", sender_id=teachers[1].id, classroom_id=cls_math.id, is_read=False),
        Notification(title="考试通知", content="数据结构期中考试将于下周三举行", type="exam", sender_id=teachers[0].id, classroom_id=cls_algo.id, is_read=False),
        Notification(title="签到提醒", content="大学物理B课堂签到已开始", type="attendance", sender_id=teachers[2].id, classroom_id=cls_phys.id, is_read=True),
        Notification(title="系统维护通知", content="系统将于本周六凌晨2:00-4:00进行维护升级", type="system", sender_id=None, is_read=False),
        Notification(title="作业截止提醒", content="数据结构第2次作业将于明天截止，请尽快提交", type="homework", sender_id=teachers[0].id, receiver_id=students[3].id, classroom_id=cls_algo.id, is_read=False),
    ]
    db.add_all(notifs)
    db.flush()

    read_statuses = [
        NotificationReadStatus(notification_id=notifs[2].id, user_id=students[10].id),
        NotificationReadStatus(notification_id=notifs[2].id, user_id=students[11].id),
    ]
    db.add_all(read_statuses)

    # ─── 14. CheckinSession + Attendance ──────────────
    print("📦 插入 CheckinSession + Attendance...")
    checkins = [
        CheckinSession(classroom_id=cls_math.id, teacher_id=teachers[1].id, type="normal", status="closed",
                       start_time=now - timedelta(days=15, hours=2), end_time=now - timedelta(days=15, hours=1, minutes=50)),
        CheckinSession(classroom_id=cls_math.id, teacher_id=teachers[1].id, type="encrypted", code="836742", status="closed",
                       start_time=now - timedelta(days=10, hours=1), end_time=now - timedelta(days=10, minutes=50)),
        CheckinSession(classroom_id=cls_algo.id, teacher_id=teachers[0].id, type="normal", status="active",
                       start_time=now - timedelta(minutes=10)),
    ]
    db.add_all(checkins)
    db.flush()

    attendances = []
    # 高数第1次签到
    for s in students[:8]:
        attendances.append(Attendance(
            classroom_id=cls_math.id, student_id=s.id, checkin_session_id=checkins[0].id,
            status="present", checkin_time=now - timedelta(days=15, hours=2, minutes=random.randint(1, 10)),
        ))
    # 高数加密签到
    for s in students[:7]:
        attendances.append(Attendance(
            classroom_id=cls_math.id, student_id=s.id, checkin_session_id=checkins[1].id,
            status="present", checkin_time=now - timedelta(days=10, hours=1, minutes=random.randint(1, 5)),
            checkin_code="836742",
        ))
    attendances.append(Attendance(
        classroom_id=cls_math.id, student_id=students[7].id, checkin_session_id=checkins[1].id,
        status="absent", note="未签到",
    ))
    # 数据结构签到
    for s in students[3:8]:
        attendances.append(Attendance(
            classroom_id=cls_algo.id, student_id=s.id, checkin_session_id=checkins[2].id,
            status="present", checkin_time=now - timedelta(minutes=random.randint(1, 10)),
        ))
    db.add_all(attendances)

    # ─── 15. Homework + HomeworkAttachment + HomeworkSubmission ─
    print("📦 插入 Homework + HomeworkSubmission...")
    hws = [
        Homework(title="微积分习题集 第三章", description="完成教材P45-P50的习题，重点关注定积分换元法", classroom_id=cls_math.id, teacher_id=teachers[1].id,
                 deadline=now + timedelta(days=7), total_score=100, status="open"),
        Homework(title="链表操作实现", description="实现单链表的反转、合并、排序功能", classroom_id=cls_algo.id, teacher_id=teachers[0].id,
                 deadline=now + timedelta(days=5), total_score=100, status="open"),
        Homework(title="牛顿力学计算", description="计算3道牛顿力学综合题", classroom_id=cls_phys.id, teacher_id=teachers[2].id,
                 deadline=now - timedelta(days=2), total_score=100, status="closed"),
        Homework(title="Python 基础练习", description="完成10道Python基础编程题", classroom_id=cls_py.id, teacher_id=teachers[0].id,
                 deadline=now + timedelta(days=14), total_score=100, status="open"),
    ]
    db.add_all(hws)
    db.flush()

    hw_attaches = [
        HomeworkAttachment(homework_id=hws[0].id, filename="习题模板.pdf", file_path="uploads/hw/math_template.pdf", file_size=256000),
        HomeworkAttachment(homework_id=hws[1].id, filename="链表框架代码.py", file_path="uploads/hw/linkedlist_skeleton.py", file_size=2048),
    ]
    db.add_all(hw_attaches)

    hw_subs = []
    # 高数作业提交
    for s in students[:8]:
        score = rand_float(60, 100) if random.random() > 0.3 else None
        hw_subs.append(HomeworkSubmission(
            homework_id=hws[0].id, student_id=s.id,
            content=f"{s.name}的微积分作业，已完成第三章所有习题。",
            score=score, feedback="完成度良好" if score else "",
            status="graded" if score else "submitted",
        ))
    # 数据结构作业提交
    for s in students[3:10]:
        hw_subs.append(HomeworkSubmission(
            homework_id=hws[1].id, student_id=s.id,
            content=f"{s.name}的链表实现代码", status="submitted",
        ))
    # 物理作业已截止
    for s in students[10:15]:
        score = rand_float(55, 98)
        hw_subs.append(HomeworkSubmission(
            homework_id=hws[2].id, student_id=s.id,
            content=f"{s.name}的力学计算题解答",
            score=score, feedback="计算过程正确", status="graded",
            graded_at=rand_dt(3),
        ))
    db.add_all(hw_subs)
    db.flush()

    sub_attaches = [
        SubmissionAttachment(submission_id=hw_subs[0].id, filename="作业.pdf", file_path="uploads/sub/math_stu01.pdf", file_size=512000),
        SubmissionAttachment(submission_id=hw_subs[8].id, filename="linkedlist.py", file_path="uploads/sub/ds_stu04.py", file_size=4096),
    ]
    db.add_all(sub_attaches)

    # ─── 16. Exam + Question + ExamSubmission + Answer ─
    print("📦 插入 Exam + Question + ExamSubmission + Answer...")
    exams = [
        Exam(title="高等数学期中考试", description="覆盖微积分前四章", classroom_id=cls_math.id, teacher_id=teachers[1].id,
             duration=90, total_score=100, status="closed",
             start_time=now - timedelta(days=8, hours=2), end_time=now - timedelta(days=8, minutes=30)),
        Exam(title="数据结构随堂测验", description="链表与树的基础", classroom_id=cls_algo.id, teacher_id=teachers[0].id,
             duration=30, total_score=50, status="published",
             start_time=now + timedelta(days=2)),
        Exam(title="Python 编程测试", description="基础语法与数据类型", classroom_id=cls_py.id, teacher_id=teachers[0].id,
             duration=60, total_score=100, status="draft"),
    ]
    db.add_all(exams)
    db.flush()

    questions = [
        # 高数期中题目
        Question(exam_id=exams[0].id, type="single", content="∫x²dx = ?",
                 options='["x³/3+C","x³+C","3x³+C","x³/2+C"]', answer="x³/3+C", score=5, order=1, knowledge_points='["微积分","不定积分"]'),
        Question(exam_id=exams[0].id, type="single", content="lim(x→0) sinx/x = ?",
                 options='["0","1","∞","不存在"]', answer="1", score=5, order=2, knowledge_points='["极限","重要极限"]'),
        Question(exam_id=exams[0].id, type="judge", content="连续函数一定可导", answer="错", score=5, order=3),
        Question(exam_id=exams[0].id, type="fill", content="f(x)=x³在x=1处的导数值为___", answer="3", score=5, order=4, knowledge_points='["导数","求导法则"]'),
        Question(exam_id=exams[0].id, type="essay", content="请用极限的定义证明lim(x→2)(3x-1)=5", answer="对于任意ε>0，取δ=ε/3，当0<|x-2|<δ时，|3x-1-5|=3|x-2|<3δ=ε", score=15, order=5, knowledge_points='["极限","ε-δ定义"]'),
        # 数据结构测验题目
        Question(exam_id=exams[1].id, type="single", content="单链表插入节点的时间复杂度为？",
                 options='["O(1)","O(n)","O(n²)","O(logn)"]', answer="O(n)", score=10, order=1),
        Question(exam_id=exams[1].id, type="multi", content="以下哪些是树的遍历方式？",
                 options='["前序遍历","中序遍历","后序遍历","层次遍历"]', answer="前序遍历,中序遍历,后序遍历,层次遍历", score=10, order=2),
        Question(exam_id=exams[1].id, type="judge", content="二叉搜索树的中序遍历结果是有序的", answer="对", score=5, order=3),
    ]
    db.add_all(questions)
    db.flush()

    exam_subs = []
    answers = []
    # 高数期中考试提交
    for s in students[:8]:
        sub = ExamSubmission(exam_id=exams[0].id, student_id=s.id,
                           status="graded", score=rand_float(50, 95),
                           started_at=now - timedelta(days=8, hours=2),
                           submitted_at=now - timedelta(days=8, hours=1, minutes=random.randint(0, 30)),
                           graded_at=now - timedelta(days=7))
        exam_subs.append(sub)
    db.add_all(exam_subs)
    db.flush()

    for sub in exam_subs:
        for q in questions[:5]:  # 高数5题
            if q.type in ("single", "judge", "fill"):
                is_correct = random.random() > 0.3
                ans_text = q.answer if is_correct else ("错" if q.answer == "对" else "随机答案")
            else:
                is_correct = None
                ans_text = "根据极限定义，对于任意ε>0..." if random.random() > 0.5 else "略"
            answers.append(Answer(
                submission_id=sub.id, question_id=q.id,
                content=ans_text,
                score=rand_float(0, q.score) if is_correct is not None else rand_float(5, q.score),
                is_correct=is_correct,
            ))
    db.add_all(answers)

    # ─── 17. QuestionBank ────────────────────────────
    print("📦 插入 QuestionBank...")
    qbank = [
        QuestionBank(teacher_id=teachers[1].id, type="single", content="不定积分∫sinxdx=?",
                     options='["-cosx+C","cosx+C","sinx+C","-sinx+C"]', answer="-cosx+C", score=5,
                     category="微积分", tags="积分,三角函数", difficulty=2),
        QuestionBank(teacher_id=teachers[0].id, type="single", content="栈的特点是？",
                     options='["先进先出","先进后出","随机存取","顺序存取"]', answer="先进后出", score=5,
                     category="数据结构", tags="栈,基本概念", difficulty=1),
        QuestionBank(teacher_id=teachers[0].id, type="judge", content="队列是一种先进先出的数据结构",
                     answer="对", score=5, category="数据结构", tags="队列", difficulty=1),
        QuestionBank(teacher_id=teachers[2].id, type="fill", content="光在真空中的速度约为___m/s",
                     answer="3×10⁸", score=5, category="物理", tags="光学,常数", difficulty=1),
        QuestionBank(teacher_id=teachers[1].id, type="essay", content="请简述泰勒展开的意义及应用",
                     answer="泰勒展开用多项式逼近函数，在近似计算、极限求解中有广泛应用", score=10,
                     category="微积分", tags="泰勒,近似", difficulty=4),
    ]
    db.add_all(qbank)

    # ─── 18. CourseMaterial ───────────────────────────
    print("📦 插入 CourseMaterial...")
    materials = [
        CourseMaterial(teacher_id=teachers[1].id, classroom_id=cls_math.id, title="微积分课件-第三章",
                      description="定积分与不定积分", file_path="uploads/materials/math_ch3.pdf",
                      file_name="微积分第三章.pdf", file_size=4500000, file_type="pdf"),
        CourseMaterial(teacher_id=teachers[0].id, classroom_id=cls_algo.id, title="链表与树 PPT",
                      description="数据结构第4-5章", file_path="uploads/materials/ds_ch45.pptx",
                      file_name="链表与树.pptx", file_size=3200000, file_type="pptx"),
        CourseMaterial(teacher_id=teachers[2].id, classroom_id=cls_phys.id, title="力学实验指导",
                      description="实验报告模板与操作步骤", file_path="uploads/materials/physics_lab.docx",
                      file_name="力学实验.docx", file_size=1800000, file_type="docx"),
    ]
    db.add_all(materials)

    # ─── 19. GradeConfig + UsualScore ─────────────────
    print("📦 插入 GradeConfig + UsualScore...")
    grade_configs = [
        GradeConfig(classroom_id=cls_math.id, homework_weight=0.3, exam_weight=0.4, attendance_weight=0.1, usual_weight=0.2),
        GradeConfig(classroom_id=cls_algo.id, homework_weight=0.25, exam_weight=0.45, attendance_weight=0.1, usual_weight=0.2),
        GradeConfig(classroom_id=cls_phys.id, homework_weight=0.3, exam_weight=0.35, attendance_weight=0.15, usual_weight=0.2),
    ]
    db.add_all(grade_configs)

    usual_scores = []
    for s in students[:8]:
        usual_scores.append(UsualScore(classroom_id=cls_math.id, person_id=s.id, score=rand_float(70, 95)))
    for s in students[3:10]:
        usual_scores.append(UsualScore(classroom_id=cls_algo.id, person_id=s.id, score=rand_float(65, 90)))
    db.add_all(usual_scores)

    # ─── 20. TeachingPlan ────────────────────────────
    print("📦 插入 TeachingPlan...")
    plans = [
        TeachingPlan(teacher_id=teachers[1].id, classroom_id=cls_math.id, title="微积分教学计划",
                    objectives="掌握一元函数微积分的基本概念与计算方法",
                    chapters='[{"chapter":"极限与连续","hours":6},{"chapter":"导数与微分","hours":8},{"chapter":"积分","hours":10}]',
                    schedule='[{"week":"第1-3周","content":"极限与连续"},{"week":"第4-7周","content":"导数"},{"week":"第8-12周","content":"积分"}]',
                    status="published"),
        TeachingPlan(teacher_id=teachers[0].id, classroom_id=cls_algo.id, title="数据结构教学计划",
                    objectives="掌握基本数据结构及其算法实现",
                    chapters='[{"chapter":"线性表","hours":4},{"chapter":"栈与队列","hours":4},{"chapter":"树","hours":6},{"chapter":"图","hours":6}]',
                    status="draft"),
    ]
    db.add_all(plans)

    # ─── 21. ExtensionRequest ─────────────────────────
    print("📦 插入 ExtensionRequest...")
    extensions = [
        ExtensionRequest(homework_id=hws[0].id, student_id=students[2].id, reason="近期身体不适，申请延期3天",
                        original_deadline=hws[0].deadline, requested_deadline=hws[0].deadline + timedelta(days=3),
                        status="approved", teacher_feedback="同意延期，注意休息"),
        ExtensionRequest(homework_id=hws[1].id, student_id=students[5].id, reason="参加竞赛，时间冲突",
                        original_deadline=hws[1].deadline, requested_deadline=hws[1].deadline + timedelta(days=2),
                        status="pending"),
    ]
    db.add_all(extensions)

    # ─── 22. LeaveRequest ────────────────────────────
    print("📦 插入 LeaveRequest...")
    leaves = [
        LeaveRequest(student_id=students[4].id, classroom_id=cls_math.id,
                    start_date=now - timedelta(days=5), end_date=now - timedelta(days=4),
                    leave_type="sick", reason="感冒发烧", status="approved",
                    teacher_feedback="注意身体", reviewed_at=now - timedelta(days=5)),
        LeaveRequest(student_id=students[7].id, classroom_id=cls_algo.id,
                    start_date=now + timedelta(days=1), end_date=now + timedelta(days=2),
                    leave_type="personal", reason="家中有事", status="pending"),
        LeaveRequest(student_id=students[12].id, classroom_id=cls_phys.id,
                    start_date=now - timedelta(days=2), end_date=now - timedelta(days=1),
                    leave_type="official", reason="参加学科竞赛", status="approved",
                    teacher_feedback="祝取得好成绩"),
    ]
    db.add_all(leaves)

    # ─── 23. Experiment + ExperimentReport ────────────
    print("📦 插入 Experiment + ExperimentReport...")
    experiments = [
        Experiment(teacher_id=teachers[2].id, classroom_id=cls_phys.id, title="单摆测重力加速度",
                  description="用单摆测量当地重力加速度", requirements="需要秒表、米尺、铁架台",
                  deadline=now + timedelta(days=10), total_score=100, status="open"),
        Experiment(teacher_id=teachers[0].id, classroom_id=cls_algo.id, title="排序算法性能对比",
                  description="实现并对比冒泡排序、快速排序、归并排序的性能",
                  deadline=now + timedelta(days=7), total_score=100, status="open"),
    ]
    db.add_all(experiments)
    db.flush()

    exp_reports = [
        ExperimentReport(experiment_id=experiments[0].id, student_id=students[10].id,
                        content="实验数据记录与误差分析", score=88, feedback="数据分析完整",
                        status="graded", graded_at=now - timedelta(days=1)),
        ExperimentReport(experiment_id=experiments[0].id, student_id=students[11].id,
                        content="单摆实验报告", status="submitted"),
        ExperimentReport(experiment_id=experiments[1].id, student_id=students[3].id,
                        content="排序算法对比实验", status="submitted"),
    ]
    db.add_all(exp_reports)

    # ─── 24. GradingResult + CorrectionRecord + SimilarQuestion ─
    print("📦 插入 GradingResult + CorrectionRecord + SimilarQuestion...")
    grading_results = [
        GradingResult(submission_id=hw_subs[0].id, score=85, max_score=100,
                     comment="解题思路清晰，部分计算有误",
                     model_key="standard", grading_method="llm", confidence=0.88,
                     error_type="calculation", error_cause="符号计算错误",
                     knowledge_points='["微积分","定积分"]', confirmed=True, confirmed_score=85),
        GradingResult(submission_id=hw_subs[1].id, score=72, max_score=100,
                     comment="基础概念掌握，但缺少关键步骤",
                     model_key="standard", grading_method="llm", confidence=0.82,
                     error_type="incomplete", error_cause="遗漏中间步骤",
                     knowledge_points='["极限","ε-δ定义"]'),
    ]
    db.add_all(grading_results)
    db.flush()

    corrections = [
        CorrectionRecord(submission_id=hw_subs[0].id, original_score=85, correction_score=90,
                        improved=True, remaining_errors="步骤3仍有小错误",
                        knowledge_update='{"微积分": "improved", "定积分": "mastered"}'),
    ]
    db.add_all(corrections)
    db.flush()

    similar_qs = [
        SimilarQuestion(student_id=students[0].id, source_grading_id=grading_results[0].id,
                       question_text="求∫₀¹ (3x²+2x)dx 的值", standard_answer="2",
                       difficulty="简单", variant_type="同类变式", tier="中等生",
                       knowledge_point_ids='["微积分","定积分"]', mastery_status="passed",
                       student_answer="2", practice_score=100),
        SimilarQuestion(student_id=students[0].id, source_grading_id=grading_results[1].id,
                       question_text="用ε-δ定义证明lim(x→3)(2x+1)=7", standard_answer="取δ=ε/2",
                       rubric_suggestion='{"criteria": ["正确取δ", "推导过程完整"]}',
                       difficulty="中等", variant_type="条件变式", tier="优等生",
                       knowledge_point_ids='["极限","ε-δ定义"]', mastery_status="pending"),
        SimilarQuestion(student_id=students[1].id, source_correction_id=corrections[0].id,
                       question_text="求∫(2x+1)dx", standard_answer="x²+x+C",
                       difficulty="简单", variant_type="同类变式", tier="中等生",
                       mastery_status="failed", student_answer="x²+C", practice_score=50),
    ]
    db.add_all(similar_qs)

    # ─── 25. KnowledgeAnalysis ───────────────────────
    print("📦 插入 KnowledgeAnalysis...")
    analyses = [
        KnowledgeAnalysis(student_id=students[0].id, analysis_type="math",
                         radar_json='{"计算能力":85,"推理能力":72,"空间想象":60,"应用能力":78,"抽象思维":70}',
                         weak_points_json='[{"point":"ε-δ证明","level":"weak"},{"point":"级数判敛","level":"medium"}]'),
        KnowledgeAnalysis(student_id=students[1].id, analysis_type="math",
                         radar_json='{"计算能力":90,"推理能力":80,"空间想象":65,"应用能力":85,"抽象思维":75}',
                         weak_points_json='[{"point":"多元积分","level":"medium"}]'),
    ]
    db.add_all(analyses)

    # ─── 26. PaperTemplate + QuestionRegion ──────────
    print("📦 插入 PaperTemplate + QuestionRegion...")
    paper_tmpl = PaperTemplate(
        exam_id=exams[0].id, teacher_id=teachers[1].id,
        blank_image_path="uploads/templates/math_midterm_blank.png",
        anchor_points='[{"x":50,"y":50},{"x":750,"y":50},{"x":750,"y":1050},{"x":50,"y":1050}]',
    )
    db.add(paper_tmpl)
    db.flush()

    regions = [
        QuestionRegion(template_id=paper_tmpl.id, question_id=questions[0].id, region_type="bubble",
                      bbox='{"x":50,"y":100,"w":700,"h":80}', order=1),
        QuestionRegion(template_id=paper_tmpl.id, question_id=questions[1].id, region_type="bubble",
                      bbox='{"x":50,"y":200,"w":700,"h":80}', order=2),
        QuestionRegion(template_id=paper_tmpl.id, question_id=questions[3].id, region_type="fill",
                      bbox='{"x":50,"y":400,"w":700,"h":60}', order=3),
        QuestionRegion(template_id=paper_tmpl.id, question_id=questions[4].id, region_type="essay",
                      bbox='{"x":50,"y":600,"w":700,"h":400}', order=4),
    ]
    db.add_all(regions)

    # ─── 27. AnswerRegradeHistory ────────────────────
    print("📦 插入 AnswerRegradeHistory...")
    regrade = AnswerRegradeHistory(
        submission_id=exam_subs[0].id, question_id=questions[4].id, operator_id=teachers[1].id,
        regrade_method="regrade_essay", input_mode="text", force_essay=False,
        before_score=8.0, after_score=12.0, before_is_correct=False, after_is_correct=None,
        max_score=15.0, before_total_score=68.0, after_total_score=72.0,
        student_text="根据极限定义证明...",
        is_essay=True, model_key="standard", grading_method="llm",
        comment="证明过程部分正确，给予部分分",
    )
    db.add(regrade)

    # ─── 提交所有数据 ──────────────────────────────────
    db.commit()
    print()
    print("✅ 测试数据填充完成！")
    print()
    print("📋 数据概览：")
    print(f"  部门/班级:  {len(depts)}")
    print(f"  用户:       1 admin + {len(teachers)} teachers + {len(students)} students")
    print(f"  课堂:       {len(classrooms)}")
    print(f"  课堂成员:   {len(members)}")
    print(f"  学生记录:   {len(stu_records)}")
    print(f"  注意力记录: {len(att_records)}")
    print(f"  考试风险:   {len(risk_records)}")
    print(f"  课堂报告:   {len(reports)}")
    print(f"  对话消息:   {len(chats)}")
    print(f"  知识库文档: {len(docs)}")
    print(f"  知识库分块: {len(chunks)}")
    print(f"  OJ题目:     {len(oj_problems)}")
    print(f"  OJ测试用例: {len(oj_cases)}")
    print(f"  OJ提交:     {len(oj_subs)}")
    print(f"  RAG对话:    {len(rag_convs)}")
    print(f"  RAG消息:    {len(rag_msgs)}")
    print(f"  通知:       {len(notifs)}")
    print(f"  签到场次:   {len(checkins)}")
    print(f"  考勤记录:   {len(attendances)}")
    print(f"  作业:       {len(hws)}")
    print(f"  作业提交:   {len(hw_subs)}")
    print(f"  考试:       {len(exams)}")
    print(f"  题目:       {len(questions)}")
    print(f"  考试提交:   {len(exam_subs)}")
    print(f"  答题:       {len(answers)}")
    print(f"  题库:       {len(qbank)}")
    print(f"  课件:       {len(materials)}")
    print(f"  成绩配置:   {len(grade_configs)}")
    print(f"  平时分:     {len(usual_scores)}")
    print(f"  教学计划:   {len(plans)}")
    print(f"  延期申请:   {len(extensions)}")
    print(f"  请假申请:   {len(leaves)}")
    print(f"  实验项目:   {len(experiments)}")
    print(f"  实验报告:   {len(exp_reports)}")
    print(f"  批改结果:   {len(grading_results)}")
    print(f"  订正记录:   {len(corrections)}")
    print(f"  相似题:     {len(similar_qs)}")
    print(f"  知识分析:   {len(analyses)}")
    print(f"  试卷模板:   1")
    print(f"  题目区域:   {len(regions)}")
    print(f"  重批改历史: 1")
    print()
    print("🔑 登录账号：")
    print("  admin    / 123456  (管理员)")
    print("  zhang    / 123456  (教师)")
    print("  li       / 123456  (教师)")
    print("  wang     / 123456  (教师)")
    print("  stu01    / 123456  (学生)")
    print("  stu02    / 123456  (学生)")
    print("  ...      / 123456  (stu01~stu20)")

    db.close()


if __name__ == "__main__":
    main()
