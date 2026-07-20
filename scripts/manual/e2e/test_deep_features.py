"""测试三个深度功能API是否可用"""
import requests, json, time

BASE_URL = "http://127.0.0.1:8000"

def login():
    r = requests.post(f"{BASE_URL}/api/auth/login", json={"username": "teacher", "password": "teacher123"}, timeout=10)
    return r.json().get("token") or r.json().get("access_token")

def headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def main():
    print("=" * 60)
    print("深度功能API可用性测试")
    print("=" * 60)

    token = login()
    print(f"✓ 登录成功, token={token[:20]}...")

    # 1. 知识归因分析（student_id=1）
    print("\n--- 测试1: 知识归因分析 /api/attribution/analyze ---")
    t0 = time.time()
    try:
        r = requests.post(
            f"{BASE_URL}/api/attribution/analyze",
            json={"student_id": 1, "analysis_type": "math"},
            headers=headers(token),
            timeout=60,
        )
        elapsed = time.time() - t0
        print(f"  HTTP: {r.status_code}  耗时: {elapsed:.1f}s")
        if r.status_code == 200:
            data = r.json()
            print(f"  radar维度数: {len(data.get('radar', {}))}")
            print(f"  weak_points数量: {len(data.get('weak_points', []))}")
            print(f"  correction_status: {data.get('correction_status')}")
            if data.get("weak_points"):
                print(f"  示例weak_point: {data['weak_points'][0]}")
        else:
            print(f"  错误: {r.text[:200]}")
    except Exception as e:
        print(f"  异常: {type(e).__name__}: {e}")

    # 2. 相似题生成
    print("\n--- 测试2: 相似题生成 /api/similar-questions/generate ---")
    t0 = time.time()
    try:
        r = requests.post(
            f"{BASE_URL}/api/similar-questions/generate",
            json={
                "question": "计算 15 + 27 * 2 - 18 / 3",
                "knowledge_points": ["四则混合运算"],
                "error_type": "计算粗心",
                "tier": "中等生",
                "count": 3,
                "standard_answer": "63"
            },
            headers=headers(token),
            timeout=120,
        )
        elapsed = time.time() - t0
        print(f"  HTTP: {r.status_code}  耗时: {elapsed:.1f}s")
        if r.status_code == 200:
            data = r.json()
            questions = data.get("questions", [])
            print(f"  生成题目数: {len(questions)}")
            for i, q in enumerate(questions[:2]):
                print(f"    题{i+1}: {str(q)[:100]}")
        else:
            print(f"  错误: {r.text[:200]}")
    except Exception as e:
        print(f"  异常: {type(e).__name__}: {e}")

    # 3. 订正提交
    print("\n--- 测试3: 订正提交 /api/correction/submit ---")
    t0 = time.time()
    try:
        # 先查一个已有的submission_id
        r = requests.post(
            f"{BASE_URL}/api/correction/submit",
            json={
                "submission_id": 42,
                "corrections": [
                    {"question_id": "q1", "image_base64": ""}
                ]
            },
            headers=headers(token),
            timeout=60,
        )
        elapsed = time.time() - t0
        print(f"  HTTP: {r.status_code}  耗时: {elapsed:.1f}s")
        if r.status_code == 200:
            data = r.json()
            print(f"  响应: {json.dumps(data, ensure_ascii=False)[:300]}")
        else:
            print(f"  错误: {r.text[:300]}")
    except Exception as e:
        print(f"  异常: {type(e).__name__}: {e}")

    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)

if __name__ == "__main__":
    main()
