"""ClassVision 多场景批改测试 - 验证不同题型下的批改质量和降级机制

测试场景：
1. 几何证明题（含辅助线分析）
2. 应用题（long_context模型路由）
3. 作文批改（四维评分+雷达图）
4. 完全正确的解答（验证满分场景）
5. 空答案（验证降级机制）

使用：.venv\Scripts\python.exe test_multi_scenario.py
"""
import json, time, requests

BASE_URL = "http://127.0.0.1:8000"
TOKEN = None

def green(msg): print(f"\033[92m✅ {msg}\033[0m")
def red(msg):   print(f"\033[91m❌ {msg}\033[0m")
def yellow(msg): print(f"\033[93m⚠️  {msg}\033[0m")
def blue(msg):  print(f"\033[94m🔵 {msg}\033[0m")
def section(msg): print(f"\n{'='*70}\n📋 {msg}\n{'='*70}")

def headers():
    return {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

def login():
    global TOKEN
    r = requests.post(f"{BASE_URL}/api/auth/login", json={"username": "teacher", "password": "teacher123"})
    if r.status_code == 200:
        TOKEN = r.json().get("token") or r.json().get("access_token")
        green(f"教师登录成功")
        return True
    red(f"登录失败: {r.status_code}")
    return False

def create_homework_and_submission(title, description, student_answer, total_score=10):
    """创建作业+学生提交，返回submission_id"""
    r = requests.post(f"{BASE_URL}/api/homework", json={
        "classroom_id": 15,
        "title": title,
        "description": description,
        "total_score": total_score,
        "deadline": "2026-12-31T23:59:59"
    }, headers=headers(), timeout=10)
    hw_id = r.json().get("id")

    r = requests.post(f"{BASE_URL}/api/homework/{hw_id}/submit", json={
        "content": student_answer
    }, headers=headers(), timeout=10)
    sub_id = r.json().get("id") or r.json().get("submission_id")
    return hw_id, sub_id

def grade_math(submission_id, question, standard_answer, total_score, subject_type="math"):
    """调用AI数学批改"""
    payload = {
        "submission_id": submission_id,
        "question": question,
        "standard_answer": standard_answer,
        "total_score": total_score,
        "subject_type": subject_type
    }
    r = requests.post(f"{BASE_URL}/api/grading/grade", json=payload, headers=headers(), timeout=300)
    return r

def print_grading_result(data, scenario_name):
    """格式化打印批改结果"""
    print(f"\n  📊 {scenario_name} 批改结果:")
    print(f"    建议分数: {data.get('suggested_score')}/{data.get('max_score')}")
    print(f"    模型: {data.get('model_key')}")
    print(f"    置信度: {data.get('confidence')}")
    print(f"    错因类型: {data.get('error_type')}")
    print(f"    错因: {data.get('error_cause')}")
    print(f"    知识点: {data.get('knowledge_points')}")

    grading = data.get('grading', {})
    steps = grading.get('steps', [])
    if steps:
        print(f"    步骤判定 ({len(steps)}步):")
        for i, step in enumerate(steps):
            status = "✓" if step.get('correct') else "✗"
            err = step.get('error_reason', '')
            print(f"      [{status}] step{i+1}: {step.get('content','')[:40]} 得分={step.get('score')} {f'错因={err}' if err else ''}")

    comment = data.get('comment', '')
    if comment:
        print(f"    评语: {comment[:200]}")

    # 几何题辅助线分析
    if data.get('geometry_analysis'):
        ga = data['geometry_analysis']
        print(f"    🔺 辅助线分析: assessment={ga.get('assessment')}")
        if ga.get('hint'):
            print(f"       提示: {ga.get('hint')[:100]}")


# ===== 场景1: 几何证明题 =====
def test_geometry():
    section("场景1: 几何证明题（验证辅助线分析）")
    question = """已知：在△ABC中，AB=AC，D是BC的中点，DE⊥AB于E，DF⊥AC于F。
求证：DE=DF"""
    standard_answer = """证明：因为AB=AC，所以∠B=∠C（等边对等角）
因为D是BC的中点，所以BD=DC
又因为DE⊥AB，DF⊥AC，所以∠DEB=∠DFC=90°
在△BDE和△CDF中：
∠B=∠C，∠DEB=∠DFC，BD=DC
所以△BDE≌△CDF（AAS）
所以DE=DF"""
    # 学生答案：忘记写"等边对等角"的依据
    student_answer = """证明：因为AB=AC，所以∠B=∠C
因为D是BC的中点，所以BD=DC
又因为DE⊥AB，DF⊥AC，所以∠DEB=∠DFC=90°
在△BDE和△CDF中：∠B=∠C，∠DEB=∠DFC，BD=DC
所以△BDE≌△CDF
所以DE=DF"""

    hw_id, sub_id = create_homework_and_submission(question, standard_answer, student_answer, total_score=10)
    blue(f"几何题作业ID={hw_id} 提交ID={sub_id}")
    blue("发送批改请求（几何题会触发辅助线分析）...")

    start = time.time()
    r = grade_math(sub_id, question, standard_answer, total_score=10, subject_type="math")
    elapsed = time.time() - start

    print(f"    耗时: {elapsed:.1f}s HTTP: {r.status_code}")

    if r.status_code == 200:
        data = r.json()
        print_grading_result(data, "几何证明题")

        # 验证关键点
        if data.get('suggested_score', 0) > 0 and data.get('suggested_score', 10) < 10:
            green("几何题批改正常（部分得分）")
        elif data.get('suggested_score', 0) == 10:
            yellow("几何题给满分，可能过于宽松")
        else:
            red(f"几何题得分异常: {data.get('suggested_score')}")

        if data.get('knowledge_points'):
            green(f"知识点提取正常: {data['knowledge_points']}")
        return data
    else:
        red(f"几何题批改失败: {r.text[:300]}")
        return None


# ===== 场景2: 应用题（长文本） =====
def test_application():
    section("场景2: 应用题（验证long_context路由）")
    question = """某工厂计划生产一批零件，原计划每天生产100个，实际每天比原计划多生产20个，
结果提前5天完成任务。请问这批零件共有多少个？"""
    standard_answer = """解：设这批零件共有x个。
原计划需要的天数：x/100
实际需要的天数：x/(100+20) = x/120
根据题意：x/100 - x/120 = 5
通分：6x/600 - 5x/600 = 5
x/600 = 5
x = 3000
答：这批零件共有3000个。"""
    # 学生答案：方程列对但计算错误
    student_answer = """解：设这批零件共有x个。
原计划天数：x/100
实际天数：x/120
x/100 - x/120 = 5
6x - 5x = 5
x = 5
答：这批零件共有5个。"""

    hw_id, sub_id = create_homework_and_submission(question, standard_answer, student_answer, total_score=10)
    blue(f"应用题作业ID={hw_id} 提交ID={sub_id}")
    blue("发送批改请求（应用题应路由到long_context模型）...")

    start = time.time()
    r = grade_math(sub_id, question, standard_answer, total_score=10, subject_type="math")
    elapsed = time.time() - start

    print(f"    耗时: {elapsed:.1f}s HTTP: {r.status_code}")

    if r.status_code == 200:
        data = r.json()
        print_grading_result(data, "应用题")

        # 验证模型路由
        model_key = data.get('model_key')
        if model_key in ('long_context', 'standard'):
            green(f"模型路由正确: {model_key}")
        else:
            yellow(f"模型路由为: {model_key}（预期long_context/standard）")

        # 验证错因识别
        if data.get('error_cause') and data.get('error_cause') != 'none':
            green(f"错因识别: {data['error_cause']}")
        return data
    else:
        red(f"应用题批改失败: {r.text[:300]}")
        return None


# ===== 场景3: 作文批改 =====
def test_essay():
    section("场景3: 作文批改（验证四维评分+雷达图）")
    question = """题目：那一刻，我长大了
要求：以"那一刻，我长大了"为题，写一篇不少于600字的记叙文。
要求情感真实，叙事完整，有细节描写。"""
    standard_answer = """评分标准：
- 内容（40分）：主题明确，立意深刻，素材真实
- 结构（20分）：结构完整，过渡自然，详略得当
- 语言（25分）：用词准确，修辞恰当，句式多样
- 书写（15分）：字迹工整，卷面整洁，无错别字"""
    student_answer = """那一刻，我长大了

成长是一瞬间的事。那天晚上的经历，让我真正懂得了什么是责任。

那是一个寒冷的冬夜，妈妈突然发高烧。爸爸出差在外，家里只有我和妈妈。看着妈妈躺在床上，脸烧得通红，我心里既害怕又着急。

"妈妈，我带你去医院吧。"我颤抖着说。
妈妈摇摇头说："没事，睡一觉就好了。"

但我知道不行。我回忆着平时妈妈照顾我的样子，先找来体温计给妈妈量体温——39度5！我吓了一跳，赶紧去找退烧药。给妈妈倒了一杯温水，看着她吃下药。

然后我用湿毛巾给妈妈敷额头。一遍又一遍地换水，换毛巾。那晚我几乎没有睡觉，一直守在妈妈床边。第二天早上，妈妈的烧退了。她看着我红红的眼睛，温柔地说："孩子，你长大了。"

那一刻，我懂了。长大不是身高的增长，不是年龄的增加，而是当家人需要你时，你能挺身而出，承担起自己的责任。从那以后，我学会了照顾家人，学会了承担责任。我觉得，我真正长大了。"""

    hw_id, sub_id = create_homework_and_submission(question, standard_answer, student_answer, total_score=100)
    blue(f"作文作业ID={hw_id} 提交ID={sub_id}")
    blue("发送作文批改请求（四维评分）...")

    start = time.time()
    r = grade_math(sub_id, question, standard_answer, total_score=100, subject_type="essay")
    elapsed = time.time() - start

    print(f"    耗时: {elapsed:.1f}s HTTP: {r.status_code}")

    if r.status_code == 200:
        data = r.json()
        print_grading_result(data, "作文批改")

        # 验证四维评分
        grading = data.get('grading', {})
        dimensions = grading.get('dimensions', {})
        if dimensions:
            print(f"\n    📊 四维评分详情:")
            for dim_name, dim_data in dimensions.items():
                if isinstance(dim_data, dict):
                    score = dim_data.get('score', dim_data.get('dimension_score', 0))
                    max_s = dim_data.get('max_score', 0)
                    comment = dim_data.get('comment', dim_data.get('dimension_comment', ''))
                    print(f"      {dim_name}: {score}/{max_s} - {comment[:80]}")
            green("四维评分生成成功")
        else:
            yellow("未找到四维评分数据")

        # 作文错因验证
        if data.get('error_cause'):
            print(f"    作文错因: {data.get('error_cause')}")
        return data
    else:
        red(f"作文批改失败: {r.text[:300]}")
        return None


# ===== 场景4: 完全正确的解答（满分场景） =====
def test_correct_answer():
    section("场景4: 完全正确的解答（验证满分场景）")
    question = "计算：15 + 27 × 2 - 18 ÷ 3"
    standard_answer = """解：原式 = 15 + 54 - 6
= 69 - 6
= 63"""
    student_answer = """解：原式 = 15 + 54 - 6
= 69 - 6
= 63"""

    hw_id, sub_id = create_homework_and_submission(question, standard_answer, student_answer, total_score=5)
    blue(f"计算题作业ID={hw_id} 提交ID={sub_id}")

    start = time.time()
    r = grade_math(sub_id, question, standard_answer, total_score=5, subject_type="math")
    elapsed = time.time() - start
    print(f"    耗时: {elapsed:.1f}s HTTP: {r.status_code}")

    if r.status_code == 200:
        data = r.json()
        print_grading_result(data, "满分场景")

        if data.get('suggested_score') == data.get('max_score'):
            green(f"✓ 满分判定正确: {data.get('suggested_score')}/{data.get('max_score')}")
        else:
            yellow(f"得分: {data.get('suggested_score')}/{data.get('max_score')}（预期应为满分）")
        return data
    else:
        red(f"满分场景批改失败: {r.text[:300]}")
        return None


# ===== 场景5: 空答案（降级机制） =====
def test_empty_answer():
    section("场景5: 空答案/极短答案（验证降级机制）")
    question = "解方程：3x - 7 = 14"
    standard_answer = "3x = 21, x = 7"
    student_answer = ""  # 空答案

    hw_id, sub_id = create_homework_and_submission(question, standard_answer, student_answer, total_score=5)
    blue(f"空答案作业ID={hw_id} 提交ID={sub_id}")

    start = time.time()
    r = grade_math(sub_id, question, standard_answer, total_score=5, subject_type="math")
    elapsed = time.time() - start
    print(f"    耗时: {elapsed:.1f}s HTTP: {r.status_code}")

    if r.status_code == 200:
        data = r.json()
        print_grading_result(data, "空答案场景")

        if data.get('suggested_score', 5) == 0:
            green("空答案正确判0分")
        else:
            yellow(f"空答案得分: {data.get('suggested_score')}（预期0分）")

        # 验证降级链是否工作
        model_key = data.get('model_key')
        grading_method = data.get('grading_method')
        print(f"    最终模型: {model_key}  批改方法: {grading_method}")
        return data
    else:
        red(f"空答案场景失败: {r.text[:300]}")
        return None


if __name__ == "__main__":
    print("🚀 ClassVision 多场景批改测试")
    print("=" * 70)

    if not login():
        print("⚠️  登录失败，测试终止")
        exit(1)

    results = {}
    results["geometry"] = test_geometry()
    time.sleep(2)  # 场景之间间隔，避免连续请求导致API限流
    results["application"] = test_application()
    time.sleep(2)
    results["essay"] = test_essay()
    time.sleep(2)
    results["correct"] = test_correct_answer()
    time.sleep(2)
    results["empty"] = test_empty_answer()

    section("多场景测试结果汇总")
    for name, result in results.items():
        status = "✅" if result else "❌"
        score = result.get('suggested_score', 'N/A') if result else 'N/A'
        model = result.get('model_key', 'N/A') if result else 'N/A'
        print(f"  {status} {name:15s}  得分:{score}  模型:{model}")

    passed = sum(1 for v in results.values() if v)
    print(f"\n  通过: {passed}/{len(results)}")
    print("\n🎉 多场景测试完成!")
