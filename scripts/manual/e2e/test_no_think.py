"""测试 qwen3:4b 的 /no_think 指令是否能阻止自言自语"""
import requests
import json

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

print("=== 测试 1: /no_think 前缀 + think=False ===")
payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"/no_think {question}"},
    ],
    "stream": False,
    "think": False,
    "options": {"num_predict": 512, "num_ctx": 4096, "temperature": 0.7},
}
resp = requests.post(f"{OLLAMA_HOST}/api/chat", json=payload, timeout=120)
content = resp.json()["message"]["content"]
print(f"回答长度: {len(content)} chars")
print(f"回答: {content[:500]}")
print()

print("=== 测试 2: /no_think 前缀 + think=True ===")
payload2 = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"/no_think {question}"},
    ],
    "stream": False,
    "think": True,
    "options": {"num_predict": 512, "num_ctx": 4096, "temperature": 0.7},
}
resp2 = requests.post(f"{OLLAMA_HOST}/api/chat", json=payload2, timeout=120)
data2 = resp2.json()
content2 = data2["message"]["content"]
thinking2 = data2["message"].get("thinking", "")
print(f"回答长度: {len(content2)} chars")
print(f"思考长度: {len(thinking2)} chars")
print(f"回答: {content2[:500]}")
if thinking2:
    print(f"思考: {thinking2[:200]}")
print()

print("=== 测试 3: 无 /no_think + think=False（对照组）===")
payload3 = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ],
    "stream": False,
    "think": False,
    "options": {"num_predict": 512, "num_ctx": 4096, "temperature": 0.7},
}
resp3 = requests.post(f"{OLLAMA_HOST}/api/chat", json=payload3, timeout=120)
content3 = resp3.json()["message"]["content"]
print(f"回答长度: {len(content3)} chars")
print(f"回答: {content3[:500]}")
