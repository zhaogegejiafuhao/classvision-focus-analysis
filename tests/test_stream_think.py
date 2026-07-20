"""测试流式模式下 think=True 的行为"""
import requests
import json
import time

OLLAMA_HOST = "http://127.0.0.1:11434"
MODEL = "qwen3:4b"

system_prompt = """你是资深教学分析专家。基于以下课堂数据进行对话分析。

【权威数据】
- 课堂名称：API Test Classroom
- 总人数：0
- 平均注意力：0分

【回答规则】
1. 直接回答问题
2. 控制在300字以内"""

question = "注意力检测的方法有哪些"

print("=== 流式 think=True ===")
payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ],
    "stream": True,
    "think": True,
    "options": {"num_predict": 2048, "num_ctx": 8192, "temperature": 0.7},
}

t0 = time.time()
full_content = ""
full_thinking = ""
chunk_count = 0
content_chunks = 0
thinking_chunks = 0

with requests.post(f"{OLLAMA_HOST}/api/chat", json=payload, stream=True, timeout=300) as resp:
    for line in resp.iter_lines():
        if not line:
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        if data.get("done"):
            break
        chunk_count += 1
        msg = data.get("message", {})
        content_delta = msg.get("content", "")
        thinking_delta = msg.get("thinking", "")
        if content_delta:
            content_chunks += 1
            full_content += content_delta
        if thinking_delta:
            thinking_chunks += 1
            full_thinking += thinking_delta

elapsed = time.time() - t0
print(f"耗时: {elapsed:.1f}s")
print(f"总 chunk 数: {chunk_count}")
print(f"content chunk 数: {content_chunks}")
print(f"thinking chunk 数: {thinking_chunks}")
print(f"回答长度: {len(full_content)} chars")
print(f"思考长度: {len(full_thinking)} chars")
print(f"回答: {full_content[:500]}")
print(f"思考 (前200): {full_thinking[:200]}")
