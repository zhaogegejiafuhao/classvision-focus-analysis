#!/usr/bin/env python3
"""
TAL-SCQ5K 中文数学竞赛题库导入脚本

将 HuggingFace TAL-SCQ5K-CN 数据集导入 ClassVision 的 question_bank 表。

数据格式：
  - 题型: single_choice (映射为 "single")
  - 知识点: knowledge_point_routes 字段
  - 难度: 0-4 (映射为 1-5)
  - 选项: answer_option_list
  - 答案: answer_value
  - 解析: answer_analysis

用法：
  cd D:\ClassVision
  set PYTHONPATH=D:\ClassVision
  .venv\Scripts\python.exe -m backend.import_tal_scq5k
"""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from backend.core.database import Base
from backend.models.tables import QuestionBank, RegisteredPerson

DB_PATH = PROJECT_ROOT / "backend" / "classvision.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"


# 知识点路由 → 简短分类名
def extract_category(knowledge_routes: list[str]) -> str:
    """从知识点路由提取简短分类名"""
    if not knowledge_routes:
        return "数学"
    route = knowledge_routes[0]
    # "知识标签->拓展思维->计算模块->小数->小数乘除->小数乘法运算"
    parts = route.split("->")
    # 取倒数第2层作为分类
    if len(parts) >= 3:
        return parts[2]  # "计算模块"
    elif len(parts) >= 2:
        return parts[1]
    return "数学"


# 知识点路由 → 标签字符串
def extract_tags(knowledge_routes: list[str]) -> str:
    """从知识点路由提取标签（逗号分隔）"""
    if not knowledge_routes:
        return ""
    route = knowledge_routes[0]
    parts = [p.strip() for p in route.split("->") if p.strip()]
    # 取最后2-3层作为标签
    return ",".join(parts[-3:])


def main():
    engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})
    Session = sessionmaker(bind=engine)
    db = Session()

    # 查找 admin 用户作为题目的 teacher_id
    admin = db.query(RegisteredPerson).filter(RegisteredPerson.role == "admin").first()
    teacher_id = admin.id if admin else 1

    imported = 0
    skipped = 0

    for split in ("train", "test"):
        filepath = PROJECT_ROOT / "data" / "question_banks" / "TAL-SCQ5K-CN" / f"{split}.jsonl"
        if not filepath.exists():
            print(f"⚠️  文件不存在: {filepath}，跳过")
            continue

        print(f"📂 处理 {split}.jsonl ...")
        with open(filepath, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                try:
                    item = json.loads(line.strip())
                except json.JSONDecodeError:
                    skipped += 1
                    continue

                # 提取字段
                problem = item.get("problem", "").strip()
                if not problem:
                    skipped += 1
                    continue

                # 选项
                options_raw = item.get("answer_option_list", [])
                options = []
                for opt_group in options_raw:
                    if isinstance(opt_group, list):
                        for opt in opt_group:
                            content = opt.get("content", "").strip()
                            if content:
                                options.append(content)
                    elif isinstance(opt_group, dict):
                        content = opt_group.get("content", "").strip()
                        if content:
                            options.append(content)

                answer = item.get("answer_value", "")
                knowledge_routes = item.get("knowledge_point_routes", [])
                difficulty_raw = item.get("difficulty", "0")

                # 难度映射: 0-4 → 1-5
                try:
                    difficulty = int(difficulty_raw) + 1
                except (ValueError, TypeError):
                    difficulty = 3

                category = extract_category(knowledge_routes)
                tags = extract_tags(knowledge_routes)

                # 解析
                analysis_parts = item.get("answer_analysis", [])
                analysis = " ".join(
                    a.strip() if isinstance(a, str) else str(a)
                    for a in analysis_parts
                ).strip()

                # 分数：根据难度和题型
                score = {1: 3, 2: 5, 3: 8, 4: 10, 5: 12}.get(difficulty, 5)

                # 去重检查（基于题目内容前100字符）
                content_key = problem[:100]
                exists = db.query(QuestionBank).filter(
                    QuestionBank.content.contains(content_key)
                ).first()
                if exists:
                    skipped += 1
                    continue

                q = QuestionBank(
                    teacher_id=teacher_id,
                    type="single",
                    content=problem,
                    options=json.dumps(options, ensure_ascii=False) if options else None,
                    answer=answer,
                    score=score,
                    category=category,
                    tags=tags,
                    difficulty=difficulty,
                    source=f"TAL-SCQ5K-CN/{split}",
                    analysis=analysis if analysis else None,
                )
                db.add(q)
                imported += 1

                # 每 500 条提交一次
                if imported % 500 == 0:
                    db.commit()
                    print(f"  已导入 {imported} 条...")

    db.commit()
    db.close()

    print(f"\n✅ 导入完成！新增 {imported} 条，跳过 {skipped} 条")
    print(f"   数据来源: TAL-SCQ5K-CN (好未来数学竞赛题库, 5000题)")


if __name__ == "__main__":
    main()
