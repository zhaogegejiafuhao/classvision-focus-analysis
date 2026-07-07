import ollama

from backend.core.config import settings


def generate_report(stats: dict) -> str:
    prompt = f"""你是一位资深教学分析专家。请根据以下课堂注意力统计数据，生成一份结构化的课堂教学分析报告。

## 课堂统计数据
- 总人数: {stats.get('total_students', 0)}
- 平均注意力分数: {stats.get('avg_attention', 0)}
- 低头人次: {stats.get('head_down_count', 0)}
- 转头人次: {stats.get('head_turn_count', 0)}
- 疲劳人次: {stats.get('fatigue_count', 0)}
- 课堂时长: {stats.get('duration', 0)} 分钟

请按以下格式输出:
1. 整体评价
2. 主要问题
3. 教学改进建议"""

    response = ollama.chat(
        model=settings.OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]
