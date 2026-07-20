"""测试 think=True + 大 num_predict，让模型思考完后给出简洁回答"""
import requests
import time

OLLAMA_HOST = "http://127.0.0.1:11434"
MODEL = "qwen3:4b"

system_prompt = """你是资深教学分析专家。基于以下课堂数据进行对话分析。

【权威数据】
- 课堂名称：API Test Classroom
- 总人数：0
- 平均注意力：0分
- 低头人次：0
- 转头人次：0
- 疲劳人次：0

【回答规则】
1. 直接回答问题，不要描述思考过程
2. 回答要专业、客观、有针对性，控制在300字以内"""

question = "注意力检测的方法有哪些"

print("=== 测试: think=True + num_predict=2048 ===")
payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ],
    "stream": False,
    "think": True,
    "options": {"num_predict": 2048, "num_ctx": 8192, "temperature": 0.7},
}
t0 = time.time()
resp = requests.post(f"{OLLAMA_HOST}/api/chat", json=payload, timeout=300)
elapsed = time.time() - t0
data = resp.json()
content = data["message"]["content"]
thinking = data["message"].get("thinking", "")
print(f"耗时: {elapsed:.1f}s")
print(f"回答长度: {len(content)} chars")
print(f"思考长度: {len(thinking)} chars")
print(f"回答: {content[:500]}")
if thinking:
    print(f"思考 (前300): {thinking[:300]}")
print()

print("=== 测试: think=True + num_predict=4096 ===")
payload2 = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ],
    "stream": False,
    "think": True,
    "options": {"num_predict": 4096, "num_ctx": 8192, "temperature": 0.7},
}
t0 = time.time()
resp2 = requests.post(f"{OLLAMA_HOST}/api/chat", json=payload2, timeout=300)
elapsed2 = time.time() - t0
data2 = resp2.json()
content2 = data2["message"]["content"]
thinking2 = data2["message"].get("thinking", "")
print(f"耗时: {elapsed2:.1f}s")
print(f"回答长度: {len(content2)} chars")
print(f"思考长度: {len(thinking2)} chars")
print(f"回答: {content2[:500]}")
if thinking2:
    print(f"思考 (前300): {thinking2[:300]}")
