"""快速批改测试 - 验证优化后各场景"""
import requests, time

BASE_URL = "http://127.0.0.1:8000"

def get_headers():
    r = requests.post(f"{BASE_URL}/api/auth/login", json={"username":"teacher","password":"teacher123"})
    token = r.json()["access_token"]
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def test_math_correct():
    """测试：完全正确的计算题"""
    print("\n=== 测试1: 正确计算题 ===")
    data = {
        "question": "15 + 27 * 2 - 18 / 3",
        "standard_answer": "63",
        "total_score": 5,
        "subject_type": "math",
        "student_text": "15 + 54 - 6 = 69 - 6 = 63",
    }
    start = time.time()
    r = requests.post(f"{BASE_URL}/api/grading/grade", json=data, headers=get_headers(), timeout=300)
    elapsed = time.time() - start
    res = r.json()
    score = res["suggested_score"]
    max_s = res["max_score"]
    model = res["model_key"]
    steps = res["grading"]["steps"]
    print(f"  Score: {score}/{max_s}  Model: {model}  Steps: {len(steps)}  Time: {elapsed:.1f}s")
    for s in steps:
        mark = "V" if s["correct"] else "X"
        print(f"    [{mark}] {s['content'][:50]} score={s['score']}")
    return score == max_s

def test_math_error():
    """测试：计算错误的应用题"""
    print("\n=== 测试2: 计算错误应用题 ===")
    data = {
        "question": "某工厂原计划每天生产100个零件，实际每天多生产20个，提前5天完成。共有多少个零件？",
        "standard_answer": "x/100 - x/120 = 5, x = 3000",
        "total_score": 10,
        "subject_type": "math",
        "student_text": "设共x个。x/100 - x/120 = 5, 6x - 5x = 5, x = 5。答：共5个。",
    }
    start = time.time()
    r = requests.post(f"{BASE_URL}/api/grading/grade", json=data, headers=get_headers(), timeout=300)
    elapsed = time.time() - start
    res = r.json()
    score = res["suggested_score"]
    model = res["model_key"]
    err = res["error_cause"]
    steps = res["grading"]["steps"]
    print(f"  Score: {score}/{res['max_score']}  Model: {model}  Error: {err}  Steps: {len(steps)}  Time: {elapsed:.1f}s")
    for s in steps:
        mark = "V" if s["correct"] else "X"
        print(f"    [{mark}] {s['content'][:50]} score={s['score']}")
    return 3 <= score <= 9

def test_essay():
    """测试：作文批改"""
    print("\n=== 测试3: 作文批改 ===")
    data = {
        "question": "请以我的家乡为题写一篇记叙文",
        "standard_answer": "主题鲜明，情感真挚；结构完整；语言流畅",
        "total_score": 100,
        "subject_type": "essay",
        "student_text": "我的家乡是一个位于江南水乡的小镇，那里有小桥流水，有青砖黛瓦。清晨薄雾笼罩着小镇，河面上飘着轻纱般的雾气。春天桃花柳树如诗如画，夏天傍晚凉爽捉鱼摸螺，秋天桂花飘香做桂花糕，冬天银装素裹堆雪人。无论我走到哪里，家乡永远是我最温暖的港湾。",
    }
    start = time.time()
    r = requests.post(f"{BASE_URL}/api/grading/grade", json=data, headers=get_headers(), timeout=300)
    elapsed = time.time() - start
    res = r.json()
    score = res["suggested_score"]
    model = res["model_key"]
    dims = res["grading"]["dimensions"]
    print(f"  Score: {score}/100  Model: {model}  Time: {elapsed:.1f}s")
    for k, v in dims.items():
        print(f"    {k}: {v['score']}/{v['max_score']} - {v['error_cause']}")
    return 50 <= score <= 100

def test_empty():
    """测试：空答案"""
    print("\n=== 测试4: 空答案 ===")
    data = {
        "question": "计算 3+5",
        "standard_answer": "8",
        "total_score": 5,
        "subject_type": "math",
        "student_text": "",
    }
    start = time.time()
    r = requests.post(f"{BASE_URL}/api/grading/grade", json=data, headers=get_headers(), timeout=30)
    elapsed = time.time() - start
    res = r.json()
    score = res["suggested_score"]
    model = res["model_key"]
    print(f"  Score: {score}/{res['max_score']}  Model: {model}  Time: {elapsed:.1f}s")
    return score == 0 and model == "rule_based"

if __name__ == "__main__":
    results = {}
    for name, fn in [("计算题满分", test_math_correct), ("应用题计算错", test_math_error), ("作文批改", test_essay), ("空答案", test_empty)]:
        try:
            results[name] = fn()
        except Exception as e:
            print(f"  ERROR: {e}")
            results[name] = False
        time.sleep(2)

    print("\n" + "="*50)
    print("测试结果汇总:")
    for name, ok in results.items():
        mark = "PASS" if ok else "FAIL"
        print(f"  {mark} {name}")
    passed = sum(1 for v in results.values() if v)
    print(f"通过: {passed}/{len(results)}")