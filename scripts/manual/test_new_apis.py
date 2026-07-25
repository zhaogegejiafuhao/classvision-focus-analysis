"""快速测试 AI 组卷、模板、报告 API"""
import requests
import json

BASE = "http://localhost:8000/api"

# 1. 登录
r = requests.post(f"{BASE}/auth/login", json={"username": "admin", "password": "admin123"})
token = r.json()["access_token"]
h = {"Authorization": f"Bearer {token}"}
print("1. 登录成功")

# 2. 获取模板列表
r = requests.get(f"{BASE}/exam-templates", headers=h)
templates = r.json()
print(f"2. 模板列表: {len(templates)} 个")
for t in templates:
    q_count = sum(s["count"] for s in t["structure"])
    print(f"   - {t['name']}: {q_count}题/{t['total_score']}分/{t['duration']}分钟")

# 3. 查看题库统计
r = requests.get(f"{BASE}/question-bank", headers=h, params={"page": 1, "page_size": 1})
qb = r.json()
print(f"3. 题库总量: {qb.get('total', '?')} 条")

# 4. 测试 AI 组卷
print("4. 测试 AI 智能组卷...")
r = requests.post(f"{BASE}/question-bank/ai-compose", headers=h, json={
    "prompt": "小学数学竞赛，10道单选题，覆盖计算和数论，难度中等偏难",
    "title": "AI组卷测试",
})
print(f"   状态码: {r.status_code}")
if r.status_code == 200:
    result = r.json()
    print(f"   考试ID: {result['exam_id']}")
    print(f"   题目数: {result['question_count']}")
    print(f"   总分: {result['total_score']}")
    for q in result["questions"][:5]:
        print(f"     Q{q['order']}: [{q['type']}] {q['content'][:50]}... ({q['score']}分, {q['source']})")
    if len(result["questions"]) > 5:
        print(f"     ... 还有 {len(result['questions'])-5} 题")
    exam_id = result["exam_id"]
else:
    print(f"   错误: {r.text[:300]}")
    exam_id = None

# 5. 测试考试报告
if exam_id:
    print("5. 测试考试报告...")
    r = requests.post(f"{BASE}/exams/{exam_id}/report", headers=h)
    print(f"   状态码: {r.status_code}")
    if r.status_code == 200:
        report = r.json()
        print(f"   考试: {report['exam_title']}")
        print(f"   参考人数: {report['total_count']}")
        print(f"   平均分: {report['avg_score']}")
        print(f"   及格率: {report['pass_rate']}%")
    else:
        print(f"   说明: {r.json().get('detail', r.text[:200])}")

print()
print("===== 测试完成 =====")
