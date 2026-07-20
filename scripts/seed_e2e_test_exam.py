"""创建端到端测试用的 Exam + 题目 + PaperTemplate + QuestionRegion

为 teacher_id=3 (username=teacher) 创建：
- 1 个 Exam：含 1 道 single 题 + 1 道 essay 题
- 1 个 PaperTemplate：用 test_blank_paper.png 当空白卷
- 2 个 QuestionRegion：single 题在上方，essay 题在下方

运行方式：
    & "d:\ClassVision\.venv\Scripts\python.exe" scripts\seed_e2e_test_exam.py
"""
import json
import os
import shutil
import sys
from datetime import datetime

# 确保项目根目录在 sys.path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from backend.core.database import SessionLocal
from backend.models.tables import Exam, Question, PaperTemplate, QuestionRegion

# ============ 配置 ============
TEACHER_ID = 3  # 当前前端登录的 teacher
BLANK_SOURCE = os.path.join(ROOT, "test_blank_paper.png")  # 800×1200
BLANK_DEST_DIR = os.path.join(ROOT, "uploads", "paper_templates")
os.makedirs(BLANK_DEST_DIR, exist_ok=True)


def main():
    db = SessionLocal()
    try:
        # 1. 创建 Exam
        exam = Exam(
            title="E2E测试-LLM重批改",
            teacher_id=TEACHER_ID,
            status="published",
            total_score=30,  # 10 (single) + 20 (essay)
            created_at=datetime.now(),
        )
        db.add(exam)
        db.flush()
        print(f"[Seed] 创建 Exam id={exam.id} title={exam.title}")

        # 2. 创建 2 道题目
        q_single = Question(
            exam_id=exam.id,
            type="single",
            content="1+1=?  (A. 1   B. 2   C. 3   D. 4)",
            answer="B",
            score=10,
            order=1,
        )
        q_essay = Question(
            exam_id=exam.id,
            type="essay",
            content="请写一段不少于 100 字的短文，描述你最喜欢的一本书及理由。",
            answer="（主观题，无标准答案，按内容/结构/语言/书写四维度评分）",
            score=20,
            order=2,
        )
        db.add_all([q_single, q_essay])
        db.flush()
        print(f"[Seed] 创建 Q_single id={q_single.id}")
        print(f"[Seed] 创建 Q_essay  id={q_essay.id}")

        # 3. 复制空白卷到 paper_templates 目录
        blank_filename = f"e2e_exam_{exam.id}_blank.png"
        blank_dest = os.path.join(BLANK_DEST_DIR, blank_filename)
        shutil.copy(BLANK_SOURCE, blank_dest)
        print(f"[Seed] 复制空白卷到 {blank_dest}")

        # 4. 创建 PaperTemplate
        template = PaperTemplate(
            exam_id=exam.id,
            teacher_id=TEACHER_ID,
            blank_image_path=blank_dest,
            anchor_points=None,  # 不做透视校正
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        db.add(template)
        db.flush()
        print(f"[Seed] 创建 PaperTemplate id={template.id}")

        # 5. 创建 2 个 QuestionRegion（基于 800×1200 尺寸）
        # single 题：上方区域 (50, 100, 700, 300) - 第 1 题区域
        # essay 题：下方区域 (50, 500, 700, 600) - 第 2 题区域（大题区域更大）
        region_single = QuestionRegion(
            template_id=template.id,
            question_id=q_single.id,
            region_type="bubble",  # single 题走 bubble 检测
            bbox=json.dumps({"x": 50, "y": 100, "w": 700, "h": 300}),
            order=1,
        )
        region_essay = QuestionRegion(
            template_id=template.id,
            question_id=q_essay.id,
            region_type="essay",  # essay 题走 OCR + LLM
            bbox=json.dumps({"x": 50, "y": 500, "w": 700, "h": 600}),
            order=2,
        )
        db.add_all([region_single, region_essay])
        db.flush()
        print(f"[Seed] 创建 Region_single id={region_single.id} bbox=(50,100,700,300)")
        print(f"[Seed] 创建 Region_essay  id={region_essay.id} bbox=(50,500,700,600)")

        db.commit()
        print()
        print("=" * 60)
        print(f"✅ 测试数据创建完成！")
        print(f"   Exam ID: {exam.id}")
        print(f"   Q_single ID: {q_single.id}")
        print(f"   Q_essay  ID: {q_essay.id}")
        print(f"   Template ID: {template.id}")
        print(f"   Teacher ID: {TEACHER_ID} (username=teacher)")
        print("=" * 60)
        print()
        print("下一步：")
        print(f"  1. 在浏览器「答题卡扫描」→「扫描批改」Tab")
        print(f"  2. 选择考试「{exam.title}」")
        print(f"  3. 选择学生（任选一个 student）")
        print(f"  4. 上传真实答题卡扫描件")
        print(f"  5. 在报告页 essay 题上点「重新 LLM 批改」")

    except Exception as e:
        db.rollback()
        print(f"[Seed] 失败: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
