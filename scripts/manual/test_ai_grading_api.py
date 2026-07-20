"""
ClassVision AI智能批改 - 后端API联调测试脚本 v2

完整流程：
0. 健康检查
1. 认证登录
2. 创建课堂 + 作业 + 提交（数据准备）
3. AI数学批改
4. 获取批改结果
5. 确认批改
6. 知识归因分析
7. 相似题生成
8. 订正提交
9. OCR识别

使用：.venv\Scripts\python.exe test_ai_grading_api.py
"""
import sys, json, time, requests

BASE_URL = "http://127.0.0.1:8000"
TOKEN = None
CLASSROOM_ID = None
HOMEWORK_ID = None
SUBMISSION_ID = None
GRADING_RESULT_ID = None

def green(msg): print(f"\033[92m✅ {msg}\033[0m")
def red(msg):   print(f"\033[91m❌ {msg}\033[0m")
def yellow(msg): print(f"\033[93m⚠️  {msg}\033[0m")
def blue(msg):  print(f"\033[94m🔵 {msg}\033[0m")
def section(msg): print(f"\n{'='*60}\n📋 {msg}\n{'='*60}")

def headers():
    return {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

def test_health():
    section("0. 健康检查")
    try:
        r = requests.get(f"{BASE_URL}/api/health", timeout=5)
        if r.status_code == 200:
            green(f"后端服务正常: {r.json()}")
            return True
        red(f"异常: {r.status_code}")
        return False
    except requests.exceptions.ConnectionError:
        red("后端未启动! 运行: .venv\\Scripts\\python.exe -m uvicorn backend.main:app --reload")
        return False

def test_login():
    global TOKEN
    section("1. 认证登录（教师）")
    r = requests.post(f"{BASE_URL}/api/auth/login", json={"username": "teacher", "password": "teacher123"})
    if r.status_code == 200:
        TOKEN = r.json().get("token") or r.json().get("access_token")
        if TOKEN:
            green(f"教师登录成功! Token: {TOKEN[:30]}...")
            # 同时登录学生
            r2 = requests.post(f"{BASE_URL}/api/auth/login", json={"username": "student", "password": "student123"})
            if r2.status_code == 200:
                yellow(f"学生账号也可登录")
            return True
    red(f"登录失败: {r.status_code} - {r.text[:200]}")
    return False

def prepare_data():
    """准备测试数据：课堂 → 作业 → 提交"""
    global CLASSROOM_ID, HOMEWORK_ID, SUBMISSION_ID
    section("2. 准备测试数据（课堂+作业+提交）")
    
    # 2a. 创建课堂
    r = requests.post(f"{BASE_URL}/api/classrooms", json={"name": "AI批改测试班", "subject": "数学"}, headers=headers(), timeout=10)
    if r.status_code in (200, 201):
        CLASSROOM_ID = r.json().get("id")
        green(f"创建课堂成功: ID={CLASSROOM_ID}")
    else:
        yellow(f"创建课堂失败({r.status_code})，尝试使用已有课堂")
        r2 = requests.get(f"{BASE_URL}/api/classrooms", headers=headers(), timeout=10)
        if r2.status_code == 200 and r2.json():
            CLASSROOM_ID = r2.json()[0].get("id")
            yellow(f"使用已有课堂: ID={CLASSROOM_ID}")
    
    if not CLASSROOM_ID:
        red("无法获取课堂ID，后续测试可能失败")
        return False
    
    # 2b. 创建作业
    r = requests.post(f"{BASE_URL}/api/homework", json={
        "classroom_id": CLASSROOM_ID,
        "title": "解方程 2x + 3 = 7，求x的值",
        "description": "2x + 3 = 7\n2x = 7 - 3\n2x = 4\nx = 2",
        "total_score": 5,
        "deadline": "2026-12-31T23:59:59"
    }, headers=headers(), timeout=10)
    if r.status_code in (200, 201):
        HOMEWORK_ID = r.json().get("id")
        green(f"创建作业成功: ID={HOMEWORK_ID}")
    else:
        yellow(f"创建作业失败({r.status_code}): {r.text[:200]}")
        # 尝试获取已有作业
        r2 = requests.get(f"{BASE_URL}/api/homework?classroom_id={CLASSROOM_ID}", headers=headers(), timeout=10)
        if r2.status_code == 200 and r2.json():
            hw_list = r2.json() if isinstance(r2.json(), list) else r2.json().get("items", [])
            if hw_list:
                HOMEWORK_ID = hw_list[0].get("id")
                yellow(f"使用已有作业: ID={HOMEWORK_ID}")
    
    if not HOMEWORK_ID:
        red("无法获取作业ID")
        return False
    
    # 2c. 获取学生ID
    student_id = None
    r = requests.get(f"{BASE_URL}/api/persons?role=student", headers=headers(), timeout=10)
    if r.status_code == 200:
        persons = r.json() if isinstance(r.json(), list) else r.json().get("items", [])
        for p in persons:
            if p.get("username") == "student":
                student_id = p.get("id")
                break
        if not student_id and persons:
            student_id = persons[0].get("id")
    
    if not student_id:
        yellow("无法获取学生ID，将使用默认值1")
        student_id = 1
    
    # 2d. 创建提交
    r = requests.post(f"{BASE_URL}/api/homework/{HOMEWORK_ID}/submit", json={
        "content": "2x + 3 = 7\n2x = 7 + 3\n2x = 10\nx = 5"
    }, headers=headers(), timeout=10)
    if r.status_code in (200, 201):
        SUBMISSION_ID = r.json().get("id") or r.json().get("submission_id")
        green(f"创建提交成功: ID={SUBMISSION_ID}")
    else:
        yellow(f"创建提交失败({r.status_code}): {r.text[:200]}")
        # 尝试其他方式获取
        r2 = requests.get(f"{BASE_URL}/api/homework/{HOMEWORK_ID}/submissions", headers=headers(), timeout=10)
        if r2.status_code == 200:
            subs = r2.json() if isinstance(r2.json(), list) else r2.json().get("items", [])
            if subs:
                SUBMISSION_ID = subs[0].get("id")
                yellow(f"使用已有提交: ID={SUBMISSION_ID}")
    
    if not SUBMISSION_ID:
        red("无法获取提交ID，数学批改测试将失败")
        return False
    
    green(f"数据准备完成! 课堂={CLASSROOM_ID} 作业={HOMEWORK_ID} 提交={SUBMISSION_ID}")
    return True

def test_math_grading():
    global GRADING_RESULT_ID
    section("3. AI数学批改")
    
    if not SUBMISSION_ID:
        red("跳过：无提交数据")
        return None
    
    payload = {
        "submission_id": SUBMISSION_ID,
        "question": "解方程 2x + 3 = 7，求x的值",
        "standard_answer": "2x + 3 = 7\n2x = 7 - 3\n2x = 4\nx = 2",
        "total_score": 5,
        "subject_type": "math"
    }
    
    blue("发送AI批改请求 (Qwen2.5-14B, 约15-40秒)...")
    start = time.time()
    try:
        r = requests.post(f"{BASE_URL}/api/grading/grade", json=payload, headers=headers(), timeout=120)
        elapsed = time.time() - start
        if r.status_code == 200:
            data = r.json()
            green(f"批改成功! 耗时: {elapsed:.1f}s")
            print(f"  建议分数: {data.get('suggested_score')}/{data.get('max_score')}")
            print(f"  评语: {data.get('comment', '')[:150]}")
            print(f"  模型: {data.get('model_key')}")
            print(f"  置信度: {data.get('confidence')}")
            print(f"  错因: {data.get('error_cause')}")
            print(f"  知识点: {data.get('knowledge_points')}")
            return data
        else:
            red(f"批改失败: {r.status_code} - {r.text[:300]}")
            return None
    except Exception as e:
        red(f"异常: {type(e).__name__}: {e}")
        return None

def test_get_result():
    section("4. 获取批改结果")
    if not SUBMISSION_ID:
        red("跳过：无提交ID")
        return None
    try:
        r = requests.get(f"{BASE_URL}/api/grading/result/{SUBMISSION_ID}", headers=headers(), timeout=30)
        if r.status_code == 200:
            data = r.json()
            green(f"获取成功! 分数={data.get('score')}/{data.get('max_score')}")
            global GRADING_RESULT_ID
            GRADING_RESULT_ID = data.get("id")
            return data
        red(f"获取失败: {r.status_code} - {r.text[:200]}")
        return None
    except Exception as e:
        red(f"异常: {e}")
        return None

def test_confirm():
    section("5. 确认批改")
    if not GRADING_RESULT_ID:
        yellow("无批改结果ID，跳过确认")
        return None
    try:
        r = requests.post(f"{BASE_URL}/api/grading/confirm/{GRADING_RESULT_ID}", json={"confirmed_score": None}, headers=headers(), timeout=30)
        if r.status_code == 200:
            green(f"确认成功: {r.json()}")
            return True
        red(f"确认失败: {r.status_code} - {r.text[:200]}")
        return None
    except Exception as e:
        red(f"异常: {e}")
        return None

def test_attribution():
    section("6. 知识归因分析")
    blue("发送归因分析请求...")
    # 注意：测试脚本用教师账号提交作业，所以 student_id 实际是教师ID
    # 这里查询实际有批改记录的 student_id
    try:
        # 先查询有哪些批改记录
        r0 = requests.get(f"{BASE_URL}/api/attribution/report/3", headers=headers(), timeout=30)
        student_id_to_query = 3  # 教师ID（测试时提交作业的账号）
        r = requests.post(f"{BASE_URL}/api/attribution/analyze", json={"student_id": student_id_to_query, "analysis_type": "math"}, headers=headers(), timeout=120)
        if r.status_code == 200:
            data = r.json()
            radar = data.get('radar', {})
            weak_points = data.get('weak_points', [])
            green(f"归因分析成功! 雷达维度={len(radar.get('indicators',[]))} 薄弱点={len(weak_points)}")
            if weak_points:
                for wp in weak_points[:3]:
                    print(f"  薄弱点: {wp}")
            if radar:
                print(f"  雷达: {json.dumps(radar, ensure_ascii=False)[:200]}")
            return data
        red(f"失败: {r.status_code} - {r.text[:200]}")
        return None
    except Exception as e:
        red(f"异常: {e}")
        return None

def test_similar():
    section("7. 相似题生成")
    blue("发送相似题生成请求...")
    try:
        r = requests.post(f"{BASE_URL}/api/similar-questions/generate", json={
            "question": "解方程 2x + 3 = 7",
            "knowledge_points": ["一元一次方程", "等式性质"],
            "error_type": "计算粗心",
            "tier": "中等生",
            "count": 3,
            "standard_answer": "x = 2"
        }, headers=headers(), timeout=120)
        if r.status_code == 200:
            data = r.json()
            qs = data.get("questions", [])
            green(f"生成{len(qs)}道相似题!")
            for i, q in enumerate(qs[:3]):
                print(f"  题{i+1}: {q.get('question_text','')[:80]}")
                print(f"       答案: {q.get('standard_answer','')[:80]}")
                print(f"       难度: {q.get('difficulty','')}  类型: {q.get('variant_type','')}")
            return data
        red(f"失败: {r.status_code} - {r.text[:200]}")
        return None
    except Exception as e:
        red(f"异常: {e}")
        return None

def test_correction():
    section("8. 订正提交")
    if not SUBMISSION_ID:
        red("跳过：无提交ID")
        return None
    try:
        r = requests.post(f"{BASE_URL}/api/correction/submit", json={
            "submission_id": SUBMISSION_ID,
            "corrections": [{"question_id": "s1", "content": "订正：2x = 7-3 = 4, x = 2"}]
        }, headers=headers(), timeout=30)
        if r.status_code == 200:
            green(f"订正提交成功!")
            return r.json()
        red(f"订正失败: {r.status_code} - {r.text[:200]}")
        return None
    except Exception as e:
        red(f"异常: {e}")
        return None

def test_ocr():
    section("9. OCR识别 (PaddleOCR本地)")
    try:
        from PIL import Image, ImageDraw
        import io, base64
        img = Image.new('RGB', (300, 100), 'white')
        draw = ImageDraw.Draw(img)
        draw.text((30, 30), "2x+3=7", fill='black')
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        img_b64 = base64.b64encode(buf.getvalue()).decode()
        
        r = requests.post(f"{BASE_URL}/api/grading/ocr", json={"image_base64": img_b64}, headers=headers(), timeout=60)
        if r.status_code == 200:
            data = r.json()
            green(f"OCR成功! 文本='{data.get('text')}' 置信度={data.get('confidence')} 引擎={data.get('engine')}")
            return data
        red(f"OCR失败: {r.status_code} - {r.text[:200]}")
        return None
    except ImportError:
        yellow("Pillow未安装，跳过")
        return None
    except Exception as e:
        red(f"OCR异常: {type(e).__name__}: {e}")
        return None

if __name__ == "__main__":
    print("🚀 ClassVision AI智能批改 - 后端API联调测试 v2")
    
    results = {}
    if not test_health(): sys.exit(1)
    results["login"] = test_login()
    if not TOKEN:
        print("⚠️  无token，测试终止")
        sys.exit(1)
    
    results["prepare"] = prepare_data()
    results["math_grading"] = test_math_grading()
    results["get_result"] = test_get_result()
    results["confirm"] = test_confirm()
    results["attribution"] = test_attribution()
    results["similar"] = test_similar()
    results["correction"] = test_correction()
    results["ocr"] = test_ocr()
    
    section("测试结果汇总")
    for name, result in results.items():
        status = "✅" if result else "❌"
        print(f"  {status} {name}")
    passed = sum(1 for v in results.values() if v)
    print(f"\n  通过: {passed}/{len(results)}")
    print("\n🎉 联调测试完成!")
