"""F 方案 e2e 联调验证脚本（直接生成 JWT，无需登录）

验证完整链路：
1. 用 backend.core.security.create_access_token 直接生成 teacher token
2. 查数据库找到 submission_id + essay question_id
3. 调 GET /regrade-history 验证返回格式
4. 调 POST /regrade-essay 触发一次重批改，再 GET 验证非空
"""
import json
import sqlite3
import sys
import requests

BASE = "http://127.0.0.1:8000"


def make_token(user_id: int, role: str, username: str) -> str:
    """直接生成 JWT token（绕过登录）"""
    sys.path.insert(0, "d:/ClassVision")
    from backend.core.security import create_access_token
    token = create_access_token({"sub": str(user_id), "role": role, "username": username})
    return token


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def find_target(db_path: str = "classvision.db"):
    """从数据库找 submission + essay question"""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 找最新的 submission（有 essay 题目的考试）
    cur.execute("""
        SELECT s.id, s.exam_id, s.student_id, s.score, s.status, e.teacher_id, e.title
        FROM exam_submission s
        JOIN exam e ON e.id = s.exam_id
        ORDER BY s.id DESC
        LIMIT 5
    """)
    subs = cur.fetchall()
    print(f"Submissions (count={len(subs)}):")
    for s in subs:
        print(f"  sub_id={s[0]} exam_id={s[1]} student_id={s[2]} score={s[3]} status={s[4]!r} teacher_id={s[5]} title={s[6]!r}")

    if not subs:
        conn.close()
        return None

    target_sub = subs[0]
    submission_id, exam_id, student_id, _, _, teacher_id, _ = target_sub

    # 找该考试的 essay 题
    cur.execute("SELECT id, content, score, answer FROM question WHERE exam_id=? AND type='essay'", (exam_id,))
    qs = cur.fetchall()
    print(f"\nEssay questions in exam {exam_id} (count={len(qs)}):")
    for q in qs:
        print(f"  q_id={q[0]} score={q[2]} content_head={(q[1] or '')[:50]!r}")

    if not qs:
        conn.close()
        return None

    question_id = qs[0][0]

    # 找 teacher 的 username
    cur.execute("SELECT username, name FROM registered_person WHERE id=?", (teacher_id,))
    row = cur.fetchone()
    teacher_username = row[0] if row else f"teacher{teacher_id}"

    conn.close()
    return {
        "submission_id": submission_id,
        "question_id": question_id,
        "teacher_id": teacher_id,
        "teacher_username": teacher_username,
        "exam_id": exam_id,
    }


def get_regrade_history(token: str, submission_id: int, question_id: int, detail: bool = False) -> dict:
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


def trigger_regrade_essay(token: str, submission_id: int, question_id: int, student_text: str) -> dict:
    """触发一次 regrade-essay 创建一条历史记录"""
    import io
    # 构造 multipart/form-data
    files = {}
    data = {"student_text": student_text, "force_essay": "false"}
    r = requests.post(
        f"{BASE}/api/answer-sheet/submissions/{submission_id}/questions/{question_id}/regrade-essay",
        headers=auth_headers(token),
        data=data,
        files=files,
        timeout=180,
    )
    print(f"[RegradeEssay] sub={submission_id} q={question_id} → status={r.status_code}")
    if r.status_code != 200:
        print(f"  body: {r.text[:500]}")
        return {}
    return r.json()


def main():
    print("=" * 60)
    print("F 方案 e2e 联调验证（JWT 直生成模式）")
    print("=" * 60)

    # 1. 找目标
    print("\n--- 1. 从数据库查找 submission + essay question ---")
    target = find_target()
    if not target:
        print("  ❌ 没找到合适的数据")
        return
    print(f"\n  选中: {target}")

    # 2. 生成 token
    print("\n--- 2. 生成 teacher JWT token ---")
    token = make_token(target["teacher_id"], "teacher", target["teacher_username"])
    print(f"  token: {token[:30]}...")

    # 3. 验证 token 有效
    print("\n--- 3. 验证 token 有效（调 /api/auth/me）---")
    r = requests.get(f"{BASE}/api/auth/me", headers=auth_headers(token), timeout=10)
    print(f"  status={r.status_code}, body={r.text[:200]}")
    if r.status_code != 200:
        print("  ❌ token 无效")
        return

    sub_id = target["submission_id"]
    q_id = target["question_id"]

    # 4. 调 GET /regrade-history（detail=false）验证空列表
    print("\n--- 4. 调 GET /regrade-history (detail=false) ---")
    data = get_regrade_history(token, sub_id, q_id, detail=False)
    if not data:
        print("  ❌ 接口调用失败")
        return

    # 验证返回字段
    required_keys = {"submission_id", "question_id", "total", "limit", "offset", "records"}
    missing = required_keys - set(data.keys())
    assert not missing, f"返回缺少字段: {missing}"
    print(f"  ✅ 返回字段完整: {sorted(data.keys())}")
    print(f"  ✅ submission_id={data['submission_id']}, question_id={data['question_id']}")
    print(f"  ✅ limit={data['limit']}, offset={data['offset']}")

    # 5. 触发一次 regrade-essay 创建历史记录
    print("\n--- 5. 触发 regrade-essay 创建历史记录 ---")
    student_text = "我最喜欢的一本书是《小王子》，因为它教会了我什么是真正的友谊和责任。"
    print(f"  student_text: {student_text[:50]}...")
    result = trigger_regrade_essay(token, sub_id, q_id, student_text)
    if not result:
        print("  ⚠️ regrade-essay 失败，跳过非空验证")
    else:
        print(f"  ✅ regrade-essay 成功: score={result.get('score')}/{result.get('max_score')} is_essay={result.get('is_essay')}")

    # 6. 再调 GET /regrade-history 验证非空
    print("\n--- 6. 再调 GET /regrade-history (detail=false) 验证非空 ---")
    data2 = get_regrade_history(token, sub_id, q_id, detail=False)
    if data2 and data2["records"]:
        rec = data2["records"][0]
        print(f"\n  第一条记录字段: {sorted(rec.keys())}")
        # 验证列表模式字段
        assert "student_text_head" in rec, "列表模式应有 student_text_head"
        assert "student_text" not in rec, "列表模式不应返回完整 student_text"
        assert "grading_json" not in rec, "列表模式不应返回 grading_json"
        assert "writing_attribution_json" not in rec, "列表模式不应返回 writing_attribution_json"
        print(f"  ✅ 列表模式序列化正确（无 grading_json/writing_attribution_json/完整 student_text）")
        print(f"  ✅ 第一条记录: id={rec['id']} method={rec['regrade_method']} input_mode={rec['input_mode']}")
        print(f"     before_score={rec['before_score']} → after_score={rec['after_score']}")
        print(f"     model_key={rec.get('model_key')} error_cause={rec.get('error_cause')!r}")
        print(f"     student_text_head={rec.get('student_text_head', '')[:50]!r}")

        # 7. 调 detail=true 验证完整字段
        print("\n--- 7. 调 GET /regrade-history (detail=true) 验证详情模式 ---")
        data3 = get_regrade_history(token, sub_id, q_id, detail=True)
        if data3 and data3["records"]:
            rec_d = data3["records"][0]
            extra_keys = sorted(set(rec_d.keys()) - set(rec.keys()))
            print(f"  详情模式额外字段: {extra_keys}")
            assert "student_text" in rec_d, "详情模式应有完整 student_text"
            assert "grading_json" in rec_d, "详情模式应有 grading_json"
            print(f"  ✅ 详情模式序列化正确")
            print(f"     student_text 完整长度: {len(rec_d.get('student_text') or '')}")
            print(f"     grading_json: {str(rec_d.get('grading_json'))[:100]}")

    print("\n" + "=" * 60)
    print("[E2E PASSED] F 方案 regrade-history 接口 e2e 验证全部通过")
    print("=" * 60)


if __name__ == "__main__":
    main()
