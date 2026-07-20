"""测试 qwen3:4b 自言自语问题的不同根治方案

方案对比：
A. 当前方案：think:false + 简单 system prompt
B. 强化方案：think:false + few-shot 示例 system prompt
C. 后处理方案：think:false + 正则后处理
D. 组合方案：B + C
"""

import json
import re
import time
import requests

OLLAMA_HOST = "http://localhost:11434"
MODEL = "qwen3:4b"


def call_ollama(system_prompt, user_prompt, num_predict=300):
    """调用 Ollama API"""
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


def strip_monologue(text):
    """后处理：过滤自言自语开头"""
    # 常见自言自语前缀模式
    patterns = [
        r'^(首先|其次|然后|接下来|让我|我需要|我来|我会|我认为|我觉得|关键点|注意|需要|用户要求)[，,。:：\s]',
        r'^(好的|好的，|当然|当然，|明白了|了解)',
        r'^(分析|根据|基于|参考|查看|观察)',
    ]
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # 检查是否以自言自语前缀开头
        is_monologue = False
        for pattern in patterns:
            if re.match(pattern, line):
                is_monologue = True
                break
        if not is_monologue:
            cleaned.append(line)
    return '\n'.join(cleaned) if cleaned else text


# 测试用例
TEST_QUESTION = "如何检测学生的注意力是否集中"
TEST_CONTEXT = "注意力检测系统通过分析学生的头部姿态（pitch、yaw 角度）和眨眼频率来评估注意力水平。"

# 方案 A：当前 system prompt
PROMPT_A = f"""你是一个专业的教学分析助手。请根据提供的参考资料回答用户的问题。

要求：
1. 直接回答问题，不要描述思考过程（如"首先我需要..."、"让我分析..."）
2. 回答要基于参考资料，不要编造内容
3. 如果参考资料不足以回答问题，请明确说明"参考资料中未提供此信息"
4. 回答要简洁、专业、有针对性，控制在300字以内

参考资料：{TEST_CONTEXT}"""

# 方案 B：强化 system prompt + few-shot 示例
PROMPT_B = f"""你是教学分析助手。严格按格式回答，禁止描述思考过程。

【禁止出现的开头】"首先""让我""我需要""我来分析""关键点""根据参考""好的"
【正确示例】
用户：低头人次怎么计算？
助手：低头人次通过统计 pitch 角度绝对值超过 15 度的学生数量得到。

用户：平均注意力怎么算？
助手：平均注意力是所有学生注意力分数的算术平均值。

【参考资料】{TEST_CONTEXT}

现在回答用户问题，直接输出答案正文，不要任何前缀："""

# 方案 C：当前 prompt + 后处理
PROMPT_C = PROMPT_A


def test_scheme(name, system_prompt, post_process=None):
    """测试一个方案"""
    print(f"\n=== 方案 {name} ===")
    t0 = time.time()
    try:
        raw = call_ollama(system_prompt, TEST_QUESTION)
        elapsed = time.time() - t0
        print(f"耗时: {elapsed:.1f}s")
        print(f"原始输出 ({len(raw)} chars):")
        print(raw[:300])
        if post_process:
            cleaned = post_process(raw)
            print(f"\n后处理后 ({len(cleaned)} chars):")
            print(cleaned[:300])
            # 检查是否还有自言自语
            has_monologue = any(raw.strip().startswith(p) for p in ['首先', '让我', '我需要', '我来', '好的', '根据'])
            print(f"\n自言自语: {'有' if has_monologue else '无'}")
        else:
            has_monologue = any(raw.strip().startswith(p) for p in ['首先', '让我', '我需要', '我来', '好的', '根据'])
            print(f"\n自言自语: {'有' if has_monologue else '无'}")
    except Exception as e:
        print(f"失败: {e}")


print("=" * 60)
print("qwen3:4b 自言自语根治方案测试")
print(f"问题: {TEST_QUESTION}")
print("=" * 60)

# 方案 A：当前
test_scheme("A (当前)", PROMPT_A)

# 方案 B：强化 prompt + few-shot
test_scheme("B (强化 prompt)", PROMPT_B)

# 方案 C：当前 + 后处理
test_scheme("C (后处理)", PROMPT_C, post_process=strip_monologue)

# 方案 D：B + C
test_scheme("D (B + 后处理)", PROMPT_B, post_process=strip_monologue)

print("\n" + "=" * 60)
print("测试完成。选择自言自语最少且回答质量最好的方案。")
