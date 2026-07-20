"""用有真实数据的课堂（ID=10）测试 fast/deep 模式回答质量"""
import json
import time
import requests

TOKEN = open(r"C:\Users\15534\AppData\Local\Temp\cv_token.txt", encoding="utf-8-sig").read().strip()
BASE = "http://localhost:8000"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json; charset=utf-8",
}

CLASSROOM_ID = 10  # 高等数学，5 学生，注意力 71.6，9 分钟

QUESTIONS = [
    ("注意力检测的方法有哪些", "通用知识问题"),
    ("当前课堂的平均注意力是多少", "课堂数据查询"),
    ("为什么学生的注意力会下降", "通用知识问题"),
    ("低头人次和转头人次分别是多少", "课堂数据查询"),
]

for mode in ["fast", "deep"]:
    print(f"\n{'='*60}")
    print(f"模式: {mode}")
    print(f"{'='*60}")

    for question, qtype in QUESTIONS:
        print(f"\n--- [{qtype}] {question} ---")
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
                    print(f"  耗时: {elapsed:.1f}s | 长度: {len(save_content)} chars")
                    print(f"  回答: {save_content}")
                    break
                if data.get("error"):
                    elapsed = time.time() - t0
                    print(f"  错误 ({elapsed:.1f}s): {data['error']}")
                    break
        except Exception as e:
            elapsed = time.time() - t0
            print(f"  失败 ({elapsed:.1f}s): {e}")
