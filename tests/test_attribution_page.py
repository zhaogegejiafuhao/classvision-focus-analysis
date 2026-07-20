"""验证知识归因分析页面新增的后端接口"""
import requests, json, time

BASE_URL = "http://127.0.0.1:8000"

def login(username="teacher", password="teacher123"):
    r = requests.post(
        f"{BASE_URL}/api/auth/login",
        json={"username": username, "password": password},
        timeout=10,
    )
    if r.status_code != 200:
        # 尝试常见学生账号
        return None
    return r.json().get("token") or r.json().get("access_token")

def headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def main():
    section("知识归因分析页面 · 后端接口验证")

    # 1. 教师登录
    token = login()
    if not token:
        print("✗ 教师登录失败，请检查 /api/auth/login")
        return
    print(f"✓ 教师登录成功 token={token[:24]}...")

    # 2. GET /api/attribution/me/student-info （教师身份应该返回空 students）
    section("测试1: GET /api/attribution/me/student-info （教师视角）")
    t0 = time.time()
    try:
        r = requests.get(
            f"{BASE_URL}/api/attribution/me/student-info",
            headers=headers(token),
            timeout=10,
        )
        elapsed = time.time() - t0
        print(f"  HTTP: {r.status_code}  耗时: {elapsed:.2f}s")
        if r.status_code == 200:
            data = r.json()
            print(f"  user_id: {data.get('user_id')}")
            print(f"  role: {data.get('role')}")
            print(f"  students数量: {len(data.get('students', []))}")
            print(f"  ✓ 教师身份返回空 students 列表符合预期")
        else:
            print(f"  ✗ 错误: {r.text[:300]}")
    except Exception as e:
        print(f"  ✗ 异常: {type(e).__name__}: {e}")

    # 3. GET /api/attribution/classrooms/1/students-for-analysis （教师视角）
    section("测试2: GET /api/attribution/classrooms/1/students-for-analysis")
    t0 = time.time()
    try:
        r = requests.get(
            f"{BASE_URL}/api/attribution/classrooms/1/students-for-analysis",
            headers=headers(token),
            timeout=10,
        )
        elapsed = time.time() - t0
        print(f"  HTTP: {r.status_code}  耗时: {elapsed:.2f}s")
        if r.status_code == 200:
            data = r.json()
            print(f"  classroom_id: {data.get('classroom_id')}")
            print(f"  classroom_name: {data.get('classroom_name')}")
            students = data.get("students", [])
            print(f"  students数量: {len(students)}")
            if students:
                print(f"  示例: {students[0]}")
        else:
            print(f"  ✗ 错误: {r.text[:300]}")
    except Exception as e:
        print(f"  ✗ 异常: {type(e).__name__}: {e}")

    # 4. GET /api/attribution/graph?analysis_type=math （验证 to_dict 方法生效）
    section("测试3: GET /api/attribution/graph?analysis_type=math （验证 to_dict）")
    t0 = time.time()
    try:
        r = requests.get(
            f"{BASE_URL}/api/attribution/graph",
            params={"analysis_type": "math"},
            headers=headers(token),
            timeout=10,
        )
        elapsed = time.time() - t0
        print(f"  HTTP: {r.status_code}  耗时: {elapsed:.2f}s")
        if r.status_code == 200:
            data = r.json()
            graph = data.get("graph", {})
            nodes = graph.get("nodes", [])
            edges = graph.get("edges", [])
            print(f"  type: {data.get('type')}")
            print(f"  nodes数量: {len(nodes)}")
            print(f"  edges数量: {len(edges)}")
            if nodes:
                print(f"  示例节点: {nodes[0]}")
            if edges:
                print(f"  示例边: {edges[0]}")
            if len(nodes) > 0:
                print(f"  ✓ to_dict 方法生效！")
            else:
                print(f"  ✗ to_dict 返回空，可能未生效")
        else:
            print(f"  ✗ 错误: {r.text[:300]}")
    except Exception as e:
        print(f"  ✗ 异常: {type(e).__name__}: {e}")

    # 5. GET /api/attribution/graph?analysis_type=writing
    section("测试4: GET /api/attribution/graph?analysis_type=writing")
    try:
        r = requests.get(
            f"{BASE_URL}/api/attribution/graph",
            params={"analysis_type": "writing"},
            headers=headers(token),
            timeout=10,
        )
        print(f"  HTTP: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            graph = data.get("graph", {})
            print(f"  writing nodes: {len(graph.get('nodes', []))}")
            print(f"  writing edges: {len(graph.get('edges', []))}")
        else:
            print(f"  错误: {r.text[:300]}")
    except Exception as e:
        print(f"  异常: {type(e).__name__}: {e}")

    # 6. 重新触发归因分析并检查返回结构（用于验证前端字段匹配）
    section("测试5: POST /api/attribution/analyze （student_id=3 应有数据）")
    t0 = time.time()
    try:
        r = requests.post(
            f"{BASE_URL}/api/attribution/analyze",
            json={"student_id": 3, "analysis_type": "math"},
            headers=headers(token),
            timeout=60,
        )
        elapsed = time.time() - t0
        print(f"  HTTP: {r.status_code}  耗时: {elapsed:.2f}s")
        if r.status_code == 200:
            data = r.json()
            radar = data.get("radar", {})
            wps = data.get("weak_points", [])
            cs = data.get("correction_status", {}) or {}
            print(f"  radar: {json.dumps(radar, ensure_ascii=False)}")
            print(f"  weak_points数量: {len(wps)}")
            if wps:
                wp0 = wps[0]
                print(f"  示例weak_point字段: {list(wp0.keys())}")
                print(f"  示例值: knowledge_name={wp0.get('knowledge_name')}, weakness_score={wp0.get('weakness_score')}, error_count={wp0.get('error_count')}")
                print(f"           suggestion={wp0.get('suggestion', '')[:80]}")
                ecd = wp0.get("error_cause_distribution", {})
                print(f"           error_cause_distribution: {ecd}")
            print(f"  correction_status: {cs}")
        else:
            print(f"  ✗ 错误: {r.text[:300]}")
    except Exception as e:
        print(f"  ✗ 异常: {type(e).__name__}: {e}")

    section("验证完成")

if __name__ == "__main__":
    main()
