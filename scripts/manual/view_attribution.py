"""查看 student_id=3 的完整归因分析数据"""
import requests, json
BASE_URL = "http://127.0.0.1:8000"
r = requests.post(f"{BASE_URL}/api/auth/login", json={"username": "teacher", "password": "teacher123"}, timeout=10)
token = r.json().get("token") or r.json().get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

r = requests.post(f"{BASE_URL}/api/attribution/analyze", json={"student_id": 3, "analysis_type": "math"}, headers=headers, timeout=30)
data = r.json()
print("=" * 60)
print("student_id=3 归因分析完整结果")
print("=" * 60)
print(f"\n【radar 雷达图维度】")
radar = data.get("radar", {})
for dim, val in radar.items():
    print(f"  {dim}: {val}")

print(f"\n【weak_points 薄弱点 ({len(data.get('weak_points', []))}个)】")
for i, wp in enumerate(data.get("weak_points", [])):
    print(f"\n  [{i+1}] {json.dumps(wp, ensure_ascii=False, indent=2)}")

print(f"\n【correction_status 订正状态】")
print(f"  {data.get('correction_status')}")
