"""快速测试：只测 2 个问题验证 Multi-Query 关闭效果"""
import json
import time
import sys
import requests

TOKEN = open(r"C:\Users\15534\AppData\Local\Temp\cv_token.txt", encoding="utf-8-sig").read().strip()
BASE = "http://localhost:8000"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json; charset=utf-8",
}

CLASSROOM_ID = 10

# 只测 deep 模式的 2 个问题（deep 模式才会用 Multi-Query）
QUESTIONS = [
    ("当前课堂的平均注意力是多少", "课堂数据查询"),
    ("注意力检测的方法有哪些", "通用知识问题"),
]

mode = "deep"
print(f"模式: {mode}（Multi-Query 已关闭）", flush=True)

for question, qtype in QUESTIONS:
    print(f"\n--- [{qtype}] {question} ---", flush=True)
    t0 = time.time()
    try:
        resp = requests.post(
            f"{BASE}/api/classrooms/{CLASSROOM_ID}/chat/stream",
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
                print(f"  耗时: {elapsed:.1f}s | 长度: {len(save_content)} chars", flush=True)
                print(f"  回答: {save_content}", flush=True)
                break
            if data.get("error"):
                elapsed = time.time() - t0
                print(f"  错误 ({elapsed:.1f}s): {data['error']}", flush=True)
                break
    except Exception as e:
        elapsed = time.time() - t0
        print(f"  失败 ({elapsed:.1f}s): {e}", flush=True)

print("\n测试完成", flush=True)
