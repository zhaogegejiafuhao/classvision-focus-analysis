"""测试双模式（fast/deep）chat 端点

验证：
1. fast 模式：用 qwen2.5:3b（如果已下载）或 qwen3:4b，关闭 HyDE/Multi-Query/reranker
2. deep 模式：用 qwen3:4b + HyDE + Multi-Query + reranker + 后处理提取答案
"""

import json
import time
import requests

TOKEN = open(r"C:\Users\15534\AppData\Local\Temp\cv_token.txt", encoding="utf-8-sig").read().strip()
BASE = "http://localhost:8000"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json; charset=utf-8",
}


def test_chat_mode(classroom_id, question, mode):
    """测试指定模式的 chat 请求"""
    print(f"\n--- mode={mode} | question={question!r} ---")
    t0 = time.time()
    try:
        resp = requests.post(
            f"{BASE}/api/classrooms/{classroom_id}/chat",
            headers=headers,
            json={"content": question, "mode": mode},
            timeout=300,
        )
        elapsed = time.time() - t0
        resp.raise_for_status()
        data = resp.json()
        content = data.get("content", "")
        print(f"  耗时: {elapsed:.1f}s | 回答长度: {len(content)} chars")
        print(f"  回答: {content[:200]}")
        return elapsed, content
    except Exception as e:
        elapsed = time.time() - t0
        print(f"  失败 ({elapsed:.1f}s): {e}")
        return elapsed, ""


def test_stream_mode(classroom_id, question, mode):
    """测试流式 chat 请求"""
    print(f"\n--- stream mode={mode} | question={question!r} ---")
    t0 = time.time()
    try:
        resp = requests.post(
            f"{BASE}/api/classrooms/{classroom_id}/chat/stream",
            headers=headers,
            json={"content": question, "mode": mode},
            stream=True,
            timeout=300,
        )
        resp.raise_for_status()
        full_content = ""
        for line in resp.iter_lines():
            if not line:
                continue
            line_str = line.decode("utf-8")
            if not line_str.startswith("data: "):
                continue
            try:
                data = json.loads(line_str[6:])
            except json.JSONDecodeError:
                continue
            if data.get("delta"):
                full_content += data["delta"]
            if data.get("done"):
                elapsed = time.time() - t0
                save_content = data.get("content", full_content)
                print(f"  耗时: {elapsed:.1f}s | 回答长度: {len(save_content)} chars")
                print(f"  回答: {save_content[:200]}")
                return elapsed, save_content
            if data.get("error"):
                elapsed = time.time() - t0
                print(f"  错误 ({elapsed:.1f}s): {data['error']}")
                return elapsed, ""
        elapsed = time.time() - t0
        print(f"  流结束 ({elapsed:.1f}s) | 回答长度: {len(full_content)} chars")
        print(f"  回答: {full_content[:200]}")
        return elapsed, full_content
    except Exception as e:
        elapsed = time.time() - t0
        print(f"  失败 ({elapsed:.1f}s): {e}")
        return elapsed, ""


# 查找可用的课堂 ID
print("=== 查找可用课堂 ===")
try:
    resp = requests.get(f"{BASE}/api/classrooms", headers=headers, timeout=10)
    resp.raise_for_status()
    classrooms = resp.json()
    if classrooms:
        classroom_id = classrooms[0]["id"]
        print(f"使用课堂 ID: {classroom_id} (名称: {classrooms[0].get('name', 'unknown')})")
    else:
        print("没有课堂，请先创建一个课堂")
        exit(1)
except Exception as e:
    print(f"查找课堂失败: {e}")
    exit(1)


# 测试问题
QUESTIONS = [
    "注意力检测的方法有哪些",
    "为什么疲劳人次这么高",
]

# 测试 deep 模式（fast 模式暂时也用 qwen3:4b，因为 qwen2.5:3b 还在下载）
print("\n" + "=" * 60)
print("双模式测试（deep 模式）")
print("=" * 60)

for q in QUESTIONS:
    test_stream_mode(classroom_id, q, "deep")

print("\n" + "=" * 60)
print("测试完成")
