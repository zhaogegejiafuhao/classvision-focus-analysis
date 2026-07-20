"""E2E 后端链路验证：scan_and_grade → regrade-essay

流程：
1. 用 teacher token 调 POST /api/answer-sheet/scan/{exam_id} 上传 test_blank_paper.png
   → 得到 submission_id + question_results
2. 找到 essay 题的 question_id
3. 调 POST /api/answer-sheet/submissions/{sid}/questions/{qid}/regrade-essay
   传 student_text（手输文字，跳过 OCR）+ force_essay=False
   → 验证 LLM 重批改返回完整字段
4. 打印每一步的关键字段，便于人工核对

运行方式：
    & "d:\ClassVision\.venv\Scripts\python.exe" scripts\e2e_regrade_essay.py
"""
import os
import sys
import time
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from backend.core.security import create_access_token

BASE = "http://localhost:8000"
EXAM_ID = 6
STUDENT_ID = 4  # 测试学生
SCAN_IMAGE = os.path.join(ROOT, "test_blank_paper.png")


def main():
    # 1. 生成 teacher token
    token = create_access_token({"sub": "3", "role": "teacher"})
    headers = {"Authorization": f"Bearer {token}"}
    print(f"[1/4] Token 生成成功: {token[:40]}...")

    # 2. 调 scan 接口
    print(f"\n[2/4] 调用 POST /api/answer-sheet/scan/{EXAM_ID}")
    print(f"      扫描件: {SCAN_IMAGE}")
    print(f"      学生 ID: {STUDENT_ID}")
    if not os.path.exists(SCAN_IMAGE):
        print(f"[ERR] 扫描件不存在: {SCAN_IMAGE}")
        return
    with open(SCAN_IMAGE, "rb") as f:
        files = {"file": ("test_blank_paper.png", f, "image/png")}
        data = {"student_id": str(STUDENT_ID)}
        t0 = time.time()
        r = requests.post(
            f"{BASE}/api/answer-sheet/scan/{EXAM_ID}",
            headers=headers,
            files=files,
            data=data,
            timeout=300,
        )
    elapsed = time.time() - t0
    print(f"      HTTP {r.status_code} ({elapsed:.1f}s)")
    if r.status_code != 200:
        print(f"      响应: {r.text[:1000]}")
        return
    scan_result = r.json()
    submission_id = scan_result.get("submission_id")
    total_score = scan_result.get("total_score")
    max_score = scan_result.get("max_score")
    question_results = scan_result.get("question_results", [])
    print(f"      ✅ submission_id={submission_id}")
    print(f"      ✅ total_score={total_score}/{max_score}")
    print(f"      ✅ question_results 数量: {len(question_results)}")
    for i, q in enumerate(question_results):
        print(f"         Q{i+1}: id={q.get('question_id')} type={q.get('question_type')} "
              f"region={q.get('region_type')} score={q.get('score')}/{q.get('max_score')} "
              f"correct={q.get('is_correct')} error={q.get('error')}")
        if q.get("student_answer"):
            print(f"             student_answer={q.get('student_answer')[:80]!r}")

    # 3. 找 essay 题
    essay_q = next((q for q in question_results if q.get("question_type") == "essay"), None)
    if not essay_q:
        print("\n[ERR] 没找到 essay 题目，无法继续 regrade-essay 测试")
        return
    question_id = essay_q["question_id"]
    print(f"\n[3/4] 找到 essay 题: question_id={question_id}")

    # 4. 调 regrade-essay 接口
    print(f"\n[4/4] 调用 POST /api/answer-sheet/submissions/{submission_id}/questions/{question_id}/regrade-essay")
    student_text = (
        "我最喜欢的一本书是《小王子》。这本书讲述了小王子从自己的小行星出发，"
        "游历了多个星球，最终来到地球的故事。通过小王子的视角，作者圣埃克苏佩里"
        "揭示了成年人世界的荒诞和孩子般纯真的可贵。书中有一句话让我印象深刻："
        "「真正重要的东西，用眼睛是看不见的，只有用心才能看清楚。」这句话让我明白，"
        "生活中的美好往往藏在平凡的细节里，需要我们用心去感受。"
    )
    print(f"      student_text (前 80 字): {student_text[:80]!r}")
    print(f"      force_essay=False (按 _is_essay_question 自动路由)")
    t0 = time.time()
    r = requests.post(
        f"{BASE}/api/answer-sheet/submissions/{submission_id}/questions/{question_id}/regrade-essay",
        headers=headers,
        data={"student_text": student_text, "force_essay": "false"},
        timeout=300,
    )
    elapsed = time.time() - t0
    print(f"      HTTP {r.status_code} ({elapsed:.1f}s)")
    if r.status_code != 200:
        print(f"      响应: {r.text[:1500]}")
        return
    regrade_result = r.json()
    print(f"\n      ✅ regrade-essay 返回字段:")
    for k in ["question_id", "submission_id", "student_answer", "score", "max_score",
              "is_correct", "is_essay", "model_key", "grading_method", "total_score"]:
        v = regrade_result.get(k)
        if isinstance(v, str) and len(v) > 100:
            v = v[:100] + "..."
        print(f"         {k}: {v!r}")
    print(f"\n      grading:")
    grading = regrade_result.get("grading", {}) or {}
    for k, v in grading.items():
        if isinstance(v, str) and len(v) > 200:
            v = v[:200] + "..."
        if isinstance(v, (list, dict)):
            v_str = str(v)
            if len(v_str) > 200:
                v_str = v_str[:200] + "..."
            print(f"         {k}: {v_str}")
        else:
            print(f"         {k}: {v!r}")
    print(f"\n      error_cause: {regrade_result.get('error_cause')!r}")
    print(f"      knowledge_points: {regrade_result.get('knowledge_points')}")
    writing_attr = regrade_result.get("writing_attribution")
    if writing_attr:
        print(f"\n      writing_attribution:")
        for k, v in writing_attr.items():
            if isinstance(v, str) and len(v) > 200:
                v = v[:200] + "..."
            print(f"         {k}: {v!r}")

    print("\n" + "=" * 60)
    print("✅ E2E 后端链路验证完成！")
    print(f"   scan: submission_id={submission_id}, total={total_score}/{max_score}")
    print(f"   regrade-essay: score={regrade_result.get('score')}/{regrade_result.get('max_score')}, "
          f"is_essay={regrade_result.get('is_essay')}, model={regrade_result.get('model_key')}")
    print(f"   new total_score: {regrade_result.get('total_score')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
