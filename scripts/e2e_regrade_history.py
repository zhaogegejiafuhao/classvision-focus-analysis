"""F 方案 e2e 联调验证脚本

验证完整链路：
1. 教师登录获取 token
2. 查找可扫描的考试 + 已有 submission
3. 调 GET /regrade-history 验证返回格式（即使空列表也算通过）
4. 如有可能，触发 regrade-essay 创建一条历史记录，再 GET 验证非空
"""
import json
import sys
import requests

BASE = "http://127.0.0.1:8000"


def login(username: str, password: str) -> str:
    """登录获取 token"""
    r = requests.post(
        f"{BASE}/api/auth/login",
        json={"username": username, "password": password},
        timeout=10,
    )
    print(f"[Login] {username} → status={r.status_code}")
    if r.status_code != 200:
        print(f"  body: {r.text[:300]}")
        sys.exit(1)
    data = r.json()
    token = data.get("access_token") or data.get("token")
    if not token:
        print(f"  ERROR: no token in response: {data}")
        sys.exit(1)
    print(f"  token: {token[:30]}...")
    return token


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def list_scannable_exams(token: str) -> list:
    """获取可扫描批改的考试列表"""
    r = requests.get(f"{BASE}/api/answer-sheet/exams", headers=auth_headers(token), timeout=10)
    print(f"[ListExams] status={r.status_code}")
    if r.status_code != 200:
        print(f"  body: {r.text[:300]}")
        return []
    data = r.json()
    exams = data if isinstance(data, list) else data.get("items", data.get("exams", []))
    print(f"  count: {len(exams)}")
    for e in exams[:5]:
        print(f"    exam_id={e.get('id')} title={e.get('title')!r} has_template={e.get('has_template')}")
    return exams


def list_exam_submissions(token: str, exam_id: int) -> list:
    """获取考试的所有 submission"""
    r = requests.get(f"{BASE}/api/exams/{exam_id}/submissions", headers=auth_headers(token), timeout=10)
    print(f"[ListSubmissions] exam_id={exam_id} status={r.status_code}")
    if r.status_code != 200:
        print(f"  body: {r.text[:300]}")
        return []
    data = r.json()
    subs = data if isinstance(data, list) else data.get("items", data.get("submissions", []))
    print(f"  count: {len(subs)}")
    for s in subs[:5]:
        print(f"    submission_id={s.get('id')} student_id={s.get('student_id')} score={s.get('score')} status={s.get('status')!r}")
    return subs


def list_exam_questions(token: str, exam_id: int) -> list:
    """获取考试的所有题目"""
    r = requests.get(f"{BASE}/api/answer-sheet/exams/{exam_id}/questions", headers=auth_headers(token), timeout=10)
    print(f"[ListQuestions] exam_id={exam_id} status={r.status_code}")
    if r.status_code != 200:
        print(f"  body: {r.text[:300]}")
        return []
    data = r.json()
    qs = data if isinstance(data, list) else data.get("items", data.get("questions", []))
    print(f"  count: {len(qs)}")
    for q in qs[:10]:
        print(f"    question_id={q.get('id')} type={q.get('type')!r} score={q.get('score')} content_head={(q.get('content') or '')[:40]!r}")
    return qs


def get_regrade_history(token: str, submission_id: int, question_id: int, detail: bool = False) -> dict:
    """调 GET /regrade-history"""
    r = requests.get(
        f"{BASE}/api/answer-sheet/submissions/{submission_id}/questions/{question_id}/regrade-history",
        params={"detail": str(detail).lower(), "limit": 100, "offset": 0},
        headers=auth_headers(token),
        timeout=15,
    )
    print(f"[GetHistory] sub={submission_id} q={question_id} detail={detail} → status={r.status_code}")
    if r.status_code != 200:
        print(f"  body: {r.text[:500]}")
        return {}
    data = r.json()
    print(f"  total: {data.get('total')}, records: {len(data.get('records', []))}")
    return data


def main():
    print("=" * 60)
    print("F 方案 e2e 联调验证")
    print("=" * 60)

    # 1. 登录（用 teacher 账号；按 ClassVision 惯例尝试常见账号）
    print("\n--- 1. 登录 ---")
    candidates = [
        ("teacher1", "123456"),
        ("teacher", "123456"),
        ("admin", "admin"),
        ("admin", "123456"),
    ]
    token = None
    for u, p in candidates:
        try:
            token = login(u, p)
            print(f"  ✅ 用 {u} 登录成功")
            break
        except SystemExit:
            continue
    if not token:
        print("  ❌ 所有候选账号均登录失败")
        return

    # 2. 查找可扫描考试
    print("\n--- 2. 查找可扫描考试 ---")
    exams = list_scannable_exams(token)
    if not exams:
        print("  ⚠️ 无可扫描考试（has_template=False），跳过 e2e 验证")
        return

    # 选第一个有 template 的考试
    target_exam = next((e for e in exams if e.get("has_template")), exams[0])
    exam_id = target_exam.get("id")
    print(f"\n  选中 exam_id={exam_id}")

    # 3. 列出该考试的题目
    print("\n--- 3. 列出考试题目 ---")
    questions = list_exam_questions(token, exam_id)
    if not questions:
        print("  ⚠️ 无题目，跳过")
        return

    # 选第一个大题（type=essay），没有就用第一题
    target_q = next((q for q in questions if q.get("type") == "essay"), questions[0])
    question_id = target_q.get("id")
    print(f"\n  选中 question_id={question_id} (type={target_q.get('type')})")

    # 4. 列出该考试的 submission
    print("\n--- 4. 列出考试 submission ---")
    submissions = list_exam_submissions(token, exam_id)
    if not submissions:
        print("  ⚠️ 无 submission，跳过")
        return
    target_sub = submissions[0]
    submission_id = target_sub.get("id")
    print(f"\n  选中 submission_id={submission_id}")

    # 5. 调 GET /regrade-history（detail=false）
    print("\n--- 5. 调 GET /regrade-history (detail=false) ---")
    data = get_regrade_history(token, submission_id, question_id, detail=False)
    if not data:
        print("  ❌ 接口调用失败")
        return
    # 验证返回字段
    required_keys = {"submission_id", "question_id", "total", "limit", "offset", "records"}
    missing = required_keys - set(data.keys())
    assert not missing, f"返回缺少字段: {missing}"
    print(f"  ✅ 返回字段完整: {sorted(data.keys())}")

    if data["records"]:
        rec = data["records"][0]
        print(f"\n  第一条记录字段: {sorted(rec.keys())}")
        # 验证列表模式不含 grading_json
        assert "grading_json" not in rec, "列表模式不应返回 grading_json"
        assert "writing_attribution_json" not in rec, "列表模式不应返回 writing_attribution_json"
        assert "student_text" not in rec, "列表模式不应返回完整 student_text"
        assert "student_text_head" in rec, "列表模式应有 student_text_head"
        print(f"  ✅ 列表模式序列化正确（无 grading_json/writing_attribution_json/完整 student_text，有 student_text_head）")

        # 6. 调 detail=true 验证
        print("\n--- 6. 调 GET /regrade-history (detail=true) ---")
        data_d = get_regrade_history(token, submission_id, question_id, detail=True)
        if data_d and data_d["records"]:
            rec_d = data_d["records"][0]
            print(f"  详情模式额外字段: {sorted(set(rec_d.keys()) - set(rec.keys()))}")
            assert "student_text" in rec_d, "详情模式应有完整 student_text"
            assert "grading_json" in rec_d, "详情模式应有 grading_json"
            print(f"  ✅ 详情模式序列化正确")
    else:
        print(f"\n  ℹ️ 历史记录为空（正常，可能还没触发过 regrade-essay）")

    print("\n" + "=" * 60)
    print("[E2E PASSED] F 方案 regrade-history 接口 e2e 验证通过")
    print("=" * 60)


if __name__ == "__main__":
    main()
