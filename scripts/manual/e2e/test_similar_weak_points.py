"""验证相似题页面拉取薄弱点 - 检查API返回数据结构"""
import requests, json, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "http://127.0.0.1:8000"

def login():
    r = requests.post(f"{BASE_URL}/api/auth/login", json={"username": "teacher", "password": "teacher123"}, timeout=10)
    if r.status_code != 200:
        print(f"登录失败: {r.status_code} {r.text}")
        return None
    return r.json().get("token") or r.json().get("access_token")

def main():
    token = login()
    if not token:
        return
    print(f"登录成功 token={token[:24]}...")

    headers = {"Authorization": f"Bearer {token}"}
    r = requests.post(f"{BASE_URL}/api/attribution/analyze",
                      json={"student_id": 3, "analysis_type": "math"},
                      headers=headers, timeout=60)
    print(f"HTTP {r.status_code}")
    data = r.json()

    print("\n=== weak_points (top 3) ===")
    wps = data.get("weak_points", [])
    for i, wp in enumerate(wps[:3]):
        print(f"  [{i}] knowledge_name={wp.get('knowledge_name')}")
        print(f"      weakness_score={wp.get('weakness_score')}")
        print(f"      error_cause_distribution={wp.get('error_cause_distribution')}")

    print("\n=== correction_status ===")
    cs = data.get("correction_status", {})
    print(f"  total_errors={cs.get('total_errors')}")
    print(f"  corrected={cs.get('corrected')}")
    print(f"  correction_rate={cs.get('correction_rate')}")

    # 模拟前端的处理逻辑
    print("\n=== 模拟前端处理 ===")
    top_wps = sorted(wps, key=lambda x: x.get('weakness_score', 0), reverse=True)[:3]
    kp_names = [wp.get('knowledge_name') for wp in top_wps if wp.get('knowledge_name')]
    print(f"  knowledgePoints (将填入): {kp_names}")

    cause_counter = {}
    for wp in wps:
        dist = wp.get('error_cause_distribution') or {}
        for cause, count in dist.items():
            cause_counter[cause] = cause_counter.get(cause, 0) + count
    top_cause = sorted(cause_counter.items(), key=lambda x: x[1], reverse=True)[0] if cause_counter else None
    print(f"  errorType (将填入): {top_cause}")

    rate = cs.get('correction_rate', 0)
    if rate >= 0.8:
        tier = '优等生'
    elif rate >= 0.4:
        tier = '中等生'
    else:
        tier = '学困生'
    print(f"  tier (将填入): {tier} (订正率={rate})")

if __name__ == "__main__":
    main()
