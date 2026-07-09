"""评分逻辑：客观题匹配 + 主观题 Ollama 评分。"""

import json
import re
import logging

import requests

from backend.core.config import settings

logger = logging.getLogger(__name__)


def _normalize_answer(text: str) -> str:
    """标准化答案文本：大写、去空白和标点。"""
    text = text.upper().strip()
    text = re.sub(r'[\s,，。、;；:：.（）()\[\]【】]', '', text)
    return text


def grade_objective(student_answer: str, standard_answer: str) -> dict:
    """客观题匹配评分。

    返回 {"correct": bool, "score": float, "match_type": str}

    三级匹配策略：
    1. 精确匹配：标准化后完全相等
    2. 模糊集合比较：提取所有 A/B/C/D 字母，排序后比较集合
    3. 单字母包含：标准答案为单字母时，检查是否包含在学生答案中
    """
    std = _normalize_answer(standard_answer)
    stu = _normalize_answer(student_answer)

    if not std:
        return {"correct": False, "score": 0, "match_type": "no_standard"}

    if not stu:
        return {"correct": False, "score": 0, "match_type": "empty"}

    # 精确匹配
    if stu == std:
        return {"correct": True, "score": 1, "match_type": "exact"}

    # 模糊集合比较：提取所有选项字母
    std_letters = sorted(set(c for c in std if c in 'ABCDEFG'))
    stu_letters = sorted(set(c for c in stu if c in 'ABCDEFG'))

    if std_letters and stu_letters:
        if std_letters == stu_letters:
            return {"correct": True, "score": 1, "match_type": "set_match"}
        # 单字母包含检查
        if len(std_letters) == 1 and std_letters[0] in stu_letters:
            return {"correct": True, "score": 1, "match_type": "contain_match"}

    return {"correct": False, "score": 0, "match_type": "no_match"}


def _build_subjective_prompt(question: str, standard: str, student: str, max_score: float) -> str:
    """构建主观题评分的 Ollama prompt。"""
    return f"""你是一位专业的阅卷老师。请根据以下信息对学生的主观题作答进行评分。

题目：{question}
标准答案：{standard}
学生作答：{student}
满分：{max_score}分

请严格按以下JSON格式输出（不要输出其他内容）：
{{"score": <得分>, "suggestion": "<评分理由，包括得分点和失分点分析>"}}

评分标准：
- 内容要点覆盖程度（40%）
- 逻辑清晰度（30%）
- 表达准确性（30%）
- 与标准答案的相符程度
- 学生答案为空或无关内容得0分
- score必须是0到{max_score}之间的数字"""


def grade_subjective(
    question: str,
    standard_answer: str,
    student_answer: str,
    max_score: float,
) -> dict:
    """调用 Ollama 评分主观题（非流式）。

    返回 {"score": float, "suggestion": str}
    """
    url = f"{settings.OLLAMA_HOST}/api/chat"
    prompt = _build_subjective_prompt(question, standard_answer, student_answer, max_score)
    payload = {
        "model": settings.OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }

    try:
        resp = requests.post(url, json=payload, timeout=120)
        resp.raise_for_status()
        content = resp.json()["message"]["content"]
    except Exception as e:
        logger.error(f"Ollama 主观题评分失败: {e}")
        return {"score": 0, "suggestion": f"AI评分失败: {e}"}

    # 解析 JSON 响应，正则回退
    score = 0.0
    suggestion = content

    try:
        match = re.search(r'\{[^}]*"score"[^}]*\}', content, re.DOTALL)
        if match:
            data = json.loads(match.group())
            score = float(data.get("score", 0))
            suggestion = data.get("suggestion", content)
    except (json.JSONDecodeError, ValueError):
        match = re.search(r'"score"\s*:\s*([\d.]+)', content)
        if match:
            score = float(match.group(1))

    score = max(0, min(score, max_score))
    return {"score": round(score, 1), "suggestion": suggestion}


def grade_subjective_stream(
    question: str,
    standard_answer: str,
    student_answer: str,
    max_score: float,
):
    """流式调用 Ollama 评分主观题。

    yield {"delta": str} 逐块输出，最后 yield {"done": True, "score": float, "suggestion": str}
    """
    url = f"{settings.OLLAMA_HOST}/api/chat"
    prompt = _build_subjective_prompt(question, standard_answer, student_answer, max_score)
    payload = {
        "model": settings.OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": True,
    }

    full_text = ""
    try:
        with requests.post(url, json=payload, stream=True, timeout=180) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                if not line:
                    continue
                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if data.get("done"):
                    break
                delta = data.get("message", {}).get("content", "")
                if delta:
                    full_text += delta
                    yield {"delta": delta}
    except Exception as e:
        yield {"error": str(e)}
        return

    # 解析最终分数
    score = 0.0
    try:
        match = re.search(r'\{[^}]*"score"[^}]*\}', full_text, re.DOTALL)
        if match:
            data = json.loads(match.group())
            score = float(data.get("score", 0))
        else:
            match = re.search(r'"score"\s*:\s*([\d.]+)', full_text)
            if match:
                score = float(match.group(1))
    except (json.JSONDecodeError, ValueError):
        pass

    score = max(0, min(score, max_score))
    yield {"done": True, "score": round(score, 1), "suggestion": full_text}
