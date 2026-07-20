"""测试 Ollama 不同参数对延迟的影响"""
import json
import time
import requests

BASE = "http://localhost:11434/api/chat"
MODEL = "qwen3:4b"

# 模拟课堂对话的系统提示词和问题
SYSTEM = "你是课堂分析助手。根据课堂数据回答问题。"
QUESTION = "注意力检测的方法有哪些"

tests = [
    ("think=True num_predict=1536 num_ctx=8192", {"think": True, "num_predict": 1536, "num_ctx": 8192}),
    ("think=True num_predict=1024 num_ctx=4096", {"think": True, "num_predict": 1024, "num_ctx": 4096}),
    ("think=True num_predict=1280 num_ctx=4096", {"think": True, "num_predict": 1280, "num_ctx": 4096}),
    ("think=False num_predict=512 num_ctx=4096", {"think": False, "num_predict": 512, "num_ctx": 4096}),
    ("think=False num_predict=1024 num_ctx=4096", {"think": False, "num_predict": 1024, "num_ctx": 4096}),
]

for name, opts in tests:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": QUESTION},
        ],
        "stream": False,
        "think": opts["think"],
        "options": {"num_predict": opts["num_predict"], "num_ctx": opts["num_ctx"], "temperature": 0.7},
    }
    t0 = time.time()
    try:
        resp = requests.post(BASE, json=payload, timeout=300)
        resp.raise_for_status()
        data = resp.json()
        elapsed = time.time() - t0
        msg = data.get("message", {})
        content = msg.get("content", "")
        thinking = msg.get("thinking", "")
        eval_tokens = data.get("eval_count", 0)
        eval_duration = data.get("eval_duration", 0) / 1e9
        print(f"\n[{name}]", flush=True)
        print(f"  耗时: {elapsed:.1f}s | content: {len(content)} chars | thinking: {len(thinking)} chars", flush=True)
        print(f"  eval_tokens: {eval_tokens} | eval_duration: {eval_duration:.1f}s", flush=True)
        print(f"  content预览: {content[:80]}...", flush=True)
    except Exception as e:
        elapsed = time.time() - t0
        print(f"\n[{name}] 失败 ({elapsed:.1f}s): {e}", flush=True)
