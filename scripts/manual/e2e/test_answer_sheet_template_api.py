"""端到端验证答题卡扫描模板保存 API"""
import requests
import json
import sys

API_BASE = "http://localhost:8000/api"


def main():
    # 1. 登录
    login_resp = requests.post(
        f"{API_BASE}/auth/login",
        json={"username": "teacher", "password": "teacher123"},
    )
    login_resp.raise_for_status()
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    print(f"[1] Login OK, token: {token[:30]}...")

    # 2. 获取考试列表
    exams_resp = requests.get(f"{API_BASE}/answer-sheet/exams", headers=headers)
    exams_resp.raise_for_status()
    exams = exams_resp.json()
    print(f"[2] Got {len(exams)} exams")
    for e in exams:
        print(f"    exam id={e['id']} title={e['title']!r} q_count={e['question_count']} has_template={e['has_template']}")
    if not exams:
        print("[ERR] 没有考试，无法继续测试")
        sys.exit(1)

    exam_id = exams[0]["id"]
    print(f"    选定 exam_id={exam_id}")

    # 3. 获取题目
    q_resp = requests.get(f"{API_BASE}/answer-sheet/exams/{exam_id}/questions", headers=headers)
    q_resp.raise_for_status()
    questions = q_resp.json()
    print(f"[3] Got {len(questions)} questions")
    for q in questions:
        print(f"    Q{q['order']} [id={q['id']}] type={q['type']} content={q['content']!r}")

    # 4. 构造 regions
    regions = [
        {"question_id": questions[0]["id"], "region_type": "bubble", "bbox": {"x": 60, "y": 170, "w": 680, "h": 100}, "order": 1},
        {"question_id": questions[1]["id"], "region_type": "bubble", "bbox": {"x": 60, "y": 320, "w": 680, "h": 100}, "order": 2},
        {"question_id": questions[2]["id"], "region_type": "bubble", "bbox": {"x": 60, "y": 470, "w": 680, "h": 100}, "order": 3},
    ]

    # 5. 保存模板（multipart/form-data）
    with open("d:/ClassVision/test_blank_paper.png", "rb") as f:
        files = {"blank_file": ("blank.png", f, "image/png")}
        data = {
            "exam_id": str(exam_id),
            "regions_json": json.dumps(regions),
        }
        save_resp = requests.post(
            f"{API_BASE}/answer-sheet/templates",
            headers={"Authorization": f"Bearer {token}"},
            data=data,
            files=files,
        )
    print(f"[4] Save template status={save_resp.status_code}")
    if save_resp.status_code != 200:
        print(f"    ERROR: {save_resp.text}")
        sys.exit(1)
    save_data = save_resp.json()
    print(f"    template_id={save_data['template_id']} regions_count={save_data['regions_count']}")

    # 6. 获取模板验证
    get_resp = requests.get(f"{API_BASE}/answer-sheet/templates/{exam_id}", headers=headers)
    print(f"[5] Get template status={get_resp.status_code}")
    if get_resp.status_code == 200:
        t = get_resp.json()
        print(f"    id={t['id']} exam_id={t['exam_id']}")
        print(f"    blank_image_url={t['blank_image_url']}")
        print(f"    blank_image_size={t['blank_image_size']}")
        print(f"    regions count={len(t['regions'])}")
        for r in t["regions"]:
            print(f"      region id={r['id']} q_id={r['question_id']} type={r['region_type']} bbox={r['bbox']} order={r['order']}")

    # 7. 重新获取考试列表，验证 has_template=true
    exams2_resp = requests.get(f"{API_BASE}/answer-sheet/exams", headers=headers)
    exams2 = exams2_resp.json()
    print(f"[6] Re-check exams:")
    for e in exams2:
        print(f"    exam id={e['id']} has_template={e['has_template']}")

    print("\n=== ALL STEPS PASSED ===")


if __name__ == "__main__":
    main()
