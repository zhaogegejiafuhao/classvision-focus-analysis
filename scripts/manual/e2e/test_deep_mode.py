"""测试 deep 模式（think=True + num_predict=2048 + HyDE + Multi-Query + reranker）"""
import json
import time
import requests

TOKEN = open(r"C:\Users\15534\AppData\Local\Temp\cv_token.txt", encoding="utf-8-sig").read().strip()
BASE = "http://localhost:8000"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json; charset=utf-8",
}

resp = requests.get(f"{BASE}/api/classrooms", headers=headers, timeout=10)
resp.raise_for_status()
classrooms = resp.json()
classroom_id = classrooms[0]["id"]
print(f"使用课堂 ID: {classroom_id}")

question = "注意力检测的方法有哪些"
print(f"\n=== deep stream | question={question!r} ===")
t0 = time.time()
try:
    resp = requests.post(
        f"{BASE}/api/classrooms/{classroom_id}/chat/stream",
        headers=headers,
        json={"content": question, "mode": "deep"},
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
            print(f"  回答: {save_content[:500]}")
            break
        if data.get("error"):
            elapsed = time.time() - t0
            print(f"  错误 ({elapsed:.1f}s): {data['error']}")
            break
except Exception as e:
    elapsed = time.time() - t0
    print(f"  失败 ({elapsed:.1f}s): {e}")
