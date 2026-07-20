"""测试 qwen3:4b 更激进的根治方案

方案 E. /api/generate + raw prompt（绕过 chat 模板）
方案 F. 强化后处理：提取最后一段答案
方案 G. 换 qwen2.5:3b 模型（需先下载）
"""

import json
import re
import time
import requests

OLLAMA_HOST = "http://localhost:11434"
MODEL = "qwen3:4b"

TEST_QUESTION = "如何检测学生的注意力是否集中"
TEST_CONTEXT = "注意力检测系统通过分析学生的头部姿态（pitch、yaw 角度）和眨眼频率来评估注意力水平。"


def call_generate(prompt, num_predict=300):
    """用 /api/generate 端点，raw prompt 格式"""
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"num_predict": num_predict, "num_ctx": 2048, "temperature": 0.7},
    }
    resp = requests.post(f"{OLLAMA_HOST}/api/generate", json=payload, timeout=90)
    resp.raise_for_status()
    return resp.json()["response"]


def call_chat(system_prompt, user_prompt, num_predict=300):
    """用 /api/chat 端点"""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
        "think": False,
        "options": {"num_predict": num_predict, "num_ctx": 2048, "temperature": 0.7},
    }
    resp = requests.post(f"{OLLAMA_HOST}/api/chat", json=payload, timeout=90)
    resp.raise_for_status()
    return resp.json()["message"]["content"]


def extract_answer(text):
    """强化后处理：提取最后一段答案

    qwen3 的思考过程通常是"首先...""关键点...""我的回答需要..."
    真正的答案通常在最后，以"答案："或直接陈述开始。
    """
    # 尝试找"答案："标记
    for marker in ['答案：', '答案:', '回答：', '回答:', '回复：', '回复:']:
        if marker in text:
            idx = text.rfind(marker)
            answer = text[idx + len(marker):].strip()
            if answer:
                return answer

    # 尝试找"所以，"或"因此，"等结论标记
    for marker in ['所以，', '因此，', '综上，', '最终回答：', '最终：']:
        if marker in text:
            idx = text.rfind(marker)
            answer = text[idx + len(marker):].strip()
            if answer:
                return answer

    # 退化方案：取最后一句话
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if lines:
        return lines[-1]
    return text


# 方案 E：/api/generate + raw prompt
# 用 raw prompt 绕过 chat 模板，可能减少思考行为
RAW_PROMPT = f"""参考资料：{TEST_CONTEXT}

问题：{TEST_QUESTION}

请直接给出答案，不要描述思考过程：

答案："""


# 方案 F：chat + 强化后处理
PROMPT_F = f"""你是教学分析助手。根据参考资料回答问题。

参考资料：{TEST_CONTEXT}

要求：
1. 直接回答，不要描述思考过程
2. 基于参考资料，不编造
3. 控制在 100 字以内
4. 输出格式：答案：xxx"""


# 方案 G：generate + 答案：前缀引导
RAW_PROMPT_G = f"""以下是一个关于教学分析的问题，请直接续写答案，不要输出任何思考过程。

参考资料：{TEST_CONTEXT}

问题：{TEST_QUESTION}

答案：注意力检测系统通过"""


def test_scheme(name, func, *args, post_process=None):
    print(f"\n=== 方案 {name} ===")
    t0 = time.time()
    try:
        raw = func(*args)
        elapsed = time.time() - t0
        print(f"耗时: {elapsed:.1f}s")
        print(f"原始输出 ({len(raw)} chars):")
        print(raw[:400])
        if post_process:
            cleaned = post_process(raw)
            print(f"\n后处理后 ({len(cleaned)} chars):")
            print(cleaned[:400])
        has_monologue = any(raw.strip().startswith(p) for p in ['首先', '让我', '我需要', '我来', '好的', '根据', '用户'])
        print(f"\n自言自语: {'有' if has_monologue else '无'}")
    except Exception as e:
        print(f"失败: {e}")


print("=" * 60)
print("qwen3:4b 激进根治方案测试")
print(f"问题: {TEST_QUESTION}")
print("=" * 60)

# 方案 E：generate + raw prompt
test_scheme("E (generate + raw)", call_generate, RAW_PROMPT)

# 方案 F：chat + 强化后处理
test_scheme("F (chat + 强化后处理)", call_chat, PROMPT_F, TEST_QUESTION, post_process=extract_answer)

# 方案 G：generate + 答案前缀引导（让模型续写答案）
test_scheme("G (generate + 前缀引导)", call_generate, RAW_PROMPT_G)

print("\n" + "=" * 60)
print("测试完成")
