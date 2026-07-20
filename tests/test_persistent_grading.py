"""
ClassVision 持久化AI批改测试脚本

流程：
1. 登录获取token
2. 查询数据库，找到有学生提交记录的作业
3. 调用AI批改API（结果持久化到GradingResult表）
4. 打印批改结果

使用：.venv\Scripts\python.exe tests\test_persistent_grading.py
"""

import sys
import json
import time
import requests

BASE_URL = "http://localhost:8000"
TOKEN = None


def green(msg):
    print(f"\033[92m[OK] {msg}\033[0m")


def red(msg):
    print(f"\033[91m[FAIL] {msg}\033[0m")


def yellow(msg):
    print(f"\033[93m[WARN] {msg}\033[0m")


def blue(msg):
    print(f"\033[94m[INFO] {msg}\033[0m")


def section(msg):
    print(f"\n{'='*60}\n{msg}\n{'='*60}")


def headers():
    return {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


# ====== Step 1: 登录获取token ======
def login():
    global TOKEN
    section("Step 1: 登录获取token")
    try:
        r = requests.post(
            f"{BASE_URL}/api/auth/login",
            json={"username": "teacher", "password": "teacher123"},
            timeout=10,
        )
        if r.status_code == 200:
            data = r.json()
            # 兼容两种返回格式: {"token": ...} 或 {"access_token": ...}
            TOKEN = data.get("token") or data.get("access_token")
            if TOKEN:
                green(f"登录成功! Token: {TOKEN[:30]}...")
                return True
            else:
                red(f"登录响应中未找到token字段: {list(data.keys())}")
                return False
        else:
            red(f"登录失败: HTTP {r.status_code} - {r.text[:200]}")
            return False
    except requests.exceptions.ConnectionError:
        red("无法连接后端服务! 请确认 http://localhost:8000 是否正常运行")
        return False
    except Exception as e:
        red(f"登录异常: {type(e).__name__}: {e}")
        return False


# ====== Step 2: 查询数据库，找到有学生提交记录的作业 ======
def find_submission():
    """通过API查询作业列表，找到有提交记录的作业，返回一条submission_id"""
    section("Step 2: 查询有学生提交记录的作业")

    # 2a. 获取作业列表
    try:
        r = requests.get(f"{BASE_URL}/api/homework", headers=headers(), timeout=10)
        if r.status_code != 200:
            red(f"获取作业列表失败: HTTP {r.status_code} - {r.text[:200]}")
            return None

        homework_list = r.json()
        if isinstance(homework_list, dict):
            homework_list = homework_list.get("items", homework_list.get("data", []))
        if not homework_list:
            yellow("作业列表为空，尝试创建测试数据...")
            return _create_test_data()
    except Exception as e:
        red(f"获取作业列表异常: {type(e).__name__}: {e}")
        return None

    # 2b. 遍历作业，查找有提交记录的
    blue(f"共找到 {len(homework_list)} 个作业，查找有提交记录的...")
    for hw in homework_list:
        hw_id = hw.get("id")
        submission_count = hw.get("submission_count", 0)
        if submission_count > 0:
            blue(f"  作业 ID={hw_id} '{hw.get('title', '')}' 有 {submission_count} 条提交")
            # 获取该作业的提交列表
            try:
                r = requests.get(
                    f"{BASE_URL}/api/homework/{hw_id}/submissions",
                    headers=headers(),
                    timeout=10,
                )
                if r.status_code == 200:
                    submissions = r.json()
                    if submissions and len(submissions) > 0:
                        sub = submissions[0]
                        sub_id = sub.get("id")
                        student_name = sub.get("student_name", "未知")
                        content_preview = sub.get("content", "")[:50]
                        green(
                            f"找到提交记录! submission_id={sub_id}, "
                            f"学生={student_name}, 内容预览='{content_preview}'"
                        )
                        return sub_id
                else:
                    yellow(f"  获取作业 {hw_id} 的提交失败: HTTP {r.status_code}")
            except Exception as e:
                yellow(f"  获取作业 {hw_id} 的提交异常: {e}")

    # 2c. 没有找到有提交的作业，尝试创建测试数据
    yellow("未找到有提交记录的作业，尝试创建测试数据...")
    return _create_test_data()


def _create_test_data():
    """创建课堂+作业+提交，返回submission_id"""
    blue("正在创建测试数据...")

    # 创建课堂
    classroom_id = None
    try:
        r = requests.post(
            f"{BASE_URL}/api/classrooms",
            json={"name": "持久化批改测试班", "subject": "数学"},
            headers=headers(),
            timeout=10,
        )
        if r.status_code in (200, 201):
            classroom_id = r.json().get("id")
            green(f"创建课堂成功: ID={classroom_id}")
        else:
            yellow(f"创建课堂失败({r.status_code})，尝试使用已有课堂")
    except Exception as e:
        yellow(f"创建课堂异常: {e}")

    if not classroom_id:
        try:
            r = requests.get(f"{BASE_URL}/api/classrooms", headers=headers(), timeout=10)
            if r.status_code == 200:
                classes = r.json()
                if isinstance(classes, list) and classes:
                    classroom_id = classes[0].get("id")
                    yellow(f"使用已有课堂: ID={classroom_id}")
        except Exception:
            pass

    if not classroom_id:
        red("无法获取课堂ID，测试终止")
        return None

    # 创建作业
    homework_id = None
    try:
        r = requests.post(
            f"{BASE_URL}/api/homework",
            json={
                "classroom_id": classroom_id,
                "title": "解方程 2x+3=7",
                "description": "2x + 3 = 7\n2x = 7 - 3\n2x = 4\nx = 2",
                "total_score": 5,
                "deadline": "2026-12-31T23:59:59",
            },
            headers=headers(),
            timeout=10,
        )
        if r.status_code in (200, 201):
            homework_id = r.json().get("id")
            green(f"创建作业成功: ID={homework_id}")
        else:
            yellow(f"创建作业失败({r.status_code}): {r.text[:200]}")
    except Exception as e:
        yellow(f"创建作业异常: {e}")

    if not homework_id:
        red("无法创建作业，测试终止")
        return None

    # 创建提交（以学生身份）
    # 先用学生账号登录
    student_token = None
    try:
        r = requests.post(
            f"{BASE_URL}/api/auth/login",
            json={"username": "student", "password": "student123"},
            timeout=10,
        )
        if r.status_code == 200:
            data = r.json()
            student_token = data.get("token") or data.get("access_token")
    except Exception:
        pass

    submit_headers = (
        {"Authorization": f"Bearer {student_token}", "Content-Type": "application/json"}
        if student_token
        else headers()
    )

    submission_id = None
    try:
        r = requests.post(
            f"{BASE_URL}/api/homework/{homework_id}/submit",
            json={"content": "2x + 3 = 7\n2x = 7 + 3\n2x = 10\nx = 5"},
            headers=submit_headers,
            timeout=10,
        )
        if r.status_code in (200, 201):
            submission_id = r.json().get("id") or r.json().get("submission_id")
            green(f"创建提交成功: ID={submission_id}")
        else:
            yellow(f"创建提交失败({r.status_code}): {r.text[:200]}")
    except Exception as e:
        yellow(f"创建提交异常: {e}")

    if not submission_id:
        # 最后尝试从已有提交中获取
        try:
            r = requests.get(
                f"{BASE_URL}/api/homework/{homework_id}/submissions",
                headers=headers(),
                timeout=10,
            )
            if r.status_code == 200:
                subs = r.json()
                if subs:
                    submission_id = subs[0].get("id")
                    yellow(f"使用已有提交: ID={submission_id}")
        except Exception:
            pass

    return submission_id


# ====== Step 3: 调用AI批改API ======
def ai_grade(submission_id):
    """调用AI批改API，结果会持久化到GradingResult表"""
    section("Step 3: 调用AI批改API（结果持久化）")

    if not submission_id:
        red("无submission_id，无法批改")
        return None

    payload = {
        "submission_id": submission_id,
        "question": "解方程 2x+3=7",
        "standard_answer": "x=2",
        "total_score": 5,
        "subject_type": "math",
    }

    blue(f"发送AI批改请求 (submission_id={submission_id})...")
    blue("提示: AI批改可能需要15-60秒，请耐心等待...")

    start = time.time()
    try:
        r = requests.post(
            f"{BASE_URL}/api/grading/grade",
            json=payload,
            headers=headers(),
            timeout=180,
        )
        elapsed = time.time() - start

        if r.status_code == 200:
            data = r.json()
            green(f"批改成功! 耗时: {elapsed:.1f}s")
            return data
        else:
            red(f"批改失败: HTTP {r.status_code} - {r.text[:300]}")
            return None
    except requests.exceptions.Timeout:
        red("批改请求超时（超过180秒）")
        return None
    except Exception as e:
        red(f"批改异常: {type(e).__name__}: {e}")
        return None


# ====== Step 4: 打印批改结果 ======
def print_grading_result(data):
    """格式化打印批改结果"""
    section("Step 4: 批改结果详情")

    if not data:
        red("无批改结果数据")
        return

    print(f"  submission_id : {data.get('submission_id')}")
    print(f"  建议分数      : {data.get('suggested_score')} / {data.get('max_score')}")
    print(f"  模型          : {data.get('model_key')}")
    print(f"  置信度        : {data.get('confidence')}")
    print(f"  批改方法      : {data.get('grading_method')}")
    print(f"  错因类型      : {data.get('error_type')}")
    print(f"  错因          : {data.get('error_cause')}")
    print(f"  知识点        : {data.get('knowledge_points')}")
    print(f"  评语          : {data.get('comment', '')[:200]}")

    # 打印步骤详情
    grading = data.get("grading", {})
    steps = grading.get("steps", [])
    if steps:
        print(f"\n  步骤判定 ({len(steps)}步):")
        for i, step in enumerate(steps):
            status = "V" if step.get("correct") else "X"
            err = step.get("error_reason", "")
            score = step.get("score", 0)
            content = step.get("content", "")[:60]
            err_info = f" | 错因={err}" if err else ""
            print(f"    [{status}] step{i+1}: {content} 得分={score}{err_info}")

    # 打印rubric信息
    rubric = data.get("rubric", {})
    rubric_steps = rubric.get("steps", [])
    if rubric_steps:
        print(f"\n  评分标准 (Rubric, {len(rubric_steps)}步):")
        for rs in rubric_steps:
            required = "必填" if rs.get("required") else "加分"
            print(
                f"    {rs.get('step_id')}: {rs.get('description', '')[:40]} "
                f"({rs.get('score')}分, {required})"
            )

    # 验证持久化：查询GradingResult
    submission_id = data.get("submission_id")
    if submission_id:
        print(f"\n  正在验证持久化（查询GradingResult表）...")
        try:
            r = requests.get(
                f"{BASE_URL}/api/grading/result/{submission_id}",
                headers=headers(),
                timeout=10,
            )
            if r.status_code == 200:
                result = r.json()
                green(
                    f"持久化验证成功! GradingResult ID={result.get('id')}, "
                    f"score={result.get('score')}/{result.get('max_score')}, "
                    f"confirmed={result.get('confirmed')}"
                )
            else:
                yellow(
                    f"查询持久化结果失败: HTTP {r.status_code} - {r.text[:200]}"
                )
        except Exception as e:
            yellow(f"查询持久化结果异常: {type(e).__name__}: {e}")


# ====== 主流程 ======
if __name__ == "__main__":
    print("=" * 60)
    print("ClassVision 持久化AI批改测试")
    print("=" * 60)

    # Step 1: 登录
    if not login():
        red("登录失败，测试终止")
        sys.exit(1)

    # Step 2: 查找提交记录
    submission_id = find_submission()
    if not submission_id:
        red("未找到提交记录，测试终止")
        sys.exit(1)

    # Step 3: AI批改
    grading_data = ai_grade(submission_id)

    # Step 4: 打印结果
    print_grading_result(grading_data)

    # 汇总
    section("测试结果汇总")
    if grading_data:
        green("全部流程执行成功!")
        print(f"  - 登录: 成功")
        print(f"  - 查找提交: submission_id={submission_id}")
        print(f"  - AI批改: 成功 (分数={grading_data.get('suggested_score')}/{grading_data.get('max_score')})")
        print(f"  - 结果已持久化到GradingResult表")
    else:
        red("测试流程中存在失败项")
        print(f"  - 登录: 成功")
        print(f"  - 查找提交: submission_id={submission_id}")
        print(f"  - AI批改: 失败")
