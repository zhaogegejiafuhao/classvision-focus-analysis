"""测试订正闭环：提交订正答案（含正确答案和空答案两种场景）"""
import requests, json, time
BASE_URL = "http://127.0.0.1:8000"

def login():
    r = requests.post(f"{BASE_URL}/api/auth/login", json={"username": "teacher", "password": "teacher123"}, timeout=10)
    return r.json().get("token") or r.json().get("access_token")

def headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def main():
    print("=" * 60)
    print("订正闭环测试")
    print("=" * 60)
    token = login()
    print(f"✓ 登录成功")

    # 找一个已批改的submission（场景2应用题：submission_id=43，原分5/10）
    # 订正答案：完整正确的解答
    print("\n--- 测试1: 提交正确订正答案（submission_id=43，应用题） ---")
    correct_correction = """解：设这批零件共有x个。
原计划需要的天数：x/100
实际需要的天数：x/(100+20) = x/120
根据题意：x/100 - x/120 = 5
通分：6x/600 - 5x/600 = 5
x/600 = 5
x = 3000
答：这批零件共有3000个。"""

    t0 = time.time()
    r = requests.post(
        f"{BASE_URL}/api/correction/submit",
        json={
            "submission_id": 43,
            "corrections": [{"question_id": "q1", "text": correct_correction}]
        },
        headers=headers(token),
        timeout=180,
    )
    elapsed = time.time() - t0
    print(f"  HTTP: {r.status_code}  耗时: {elapsed:.1f}s")
    if r.status_code == 200:
        data = r.json()
        print(f"  原始分数: {data.get('original_score')}")
        print(f"  订正分数: {data.get('correction_score')}")
        print(f"  是否进步: {data.get('improved')}")
        print(f"  correction_id: {data.get('correction_id')}")
        if data.get("improved"):
            print("  ✅ 订正成功，分数提升")
        else:
            print("  ⚠️ 订正未提升分数")
    else:
        print(f"  错误: {r.text[:300]}")

    # 测试2: 空答案快速短路
    print("\n--- 测试2: 提交空订正答案（应快速短路0分） ---")
    t0 = time.time()
    r = requests.post(
        f"{BASE_URL}/api/correction/submit",
        json={
            "submission_id": 43,
            "corrections": [{"question_id": "q1", "text": ""}]
        },
        headers=headers(token),
        timeout=30,
    )
    elapsed = time.time() - t0
    print(f"  HTTP: {r.status_code}  耗时: {elapsed:.1f}s")
    if r.status_code == 200:
        data = r.json()
        print(f"  原始分数: {data.get('original_score')}")
        print(f"  订正分数: {data.get('correction_score')}")
        print(f"  是否进步: {data.get('improved')}")
        print(f"  消息: {data.get('message', '-')}")
        if elapsed < 2:
            print("  ✅ 空答案快速短路工作正常")
        else:
            print(f"  ⚠️ 空答案响应过慢: {elapsed:.1f}s")

    # 测试3: 获取订正对比
    print("\n--- 测试3: 获取订正前后对比 ---")
    if r.status_code == 200:
        # 用测试1的correction_id
        r2 = requests.post(
            f"{BASE_URL}/api/correction/submit",
            json={
                "submission_id": 43,
                "corrections": [{"question_id": "q1", "text": correct_correction}]
            },
            headers=headers(token),
            timeout=180,
        )
        if r2.status_code == 200:
            cid = r2.json().get("correction_id")
            r3 = requests.get(f"{BASE_URL}/api/correction/comparison/{cid}", headers=headers(token), timeout=10)
            print(f"  HTTP: {r3.status_code}")
            if r3.status_code == 200:
                print(f"  对比数据: {json.dumps(r3.json(), ensure_ascii=False, indent=2)}")

    print("\n" + "=" * 60)
    print("订正闭环测试完成")
    print("=" * 60)

if __name__ == "__main__":
    main()
