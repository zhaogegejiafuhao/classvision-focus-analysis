import re
import logging

import ollama

from backend.core.config import settings

logger = logging.getLogger(__name__)


def _strip_think_tags(content: str) -> str:
    """过滤 LLM 输出中的 <think> 思考标签，处理闭合和未闭合两种情况"""
    if '</think>' in content:
        content = content.rsplit('</think>', 1)[-1]
    content = re.sub(r'<think>.*', '', content, flags=re.DOTALL)
    return content.strip()


def generate_report(stats: dict) -> str:
    prompt = f"""你是一位资深教学分析专家。请根据以下课堂注意力统计数据，生成一份结构化的课堂教学分析报告。

## 课堂基本信息
- 课程名称: {stats.get('classroom_name', '未知')}
- 课堂时长: {stats.get('duration', 0)} 分钟
- 参与学生数: {stats.get('total_students', 0)} 人
- 考场模式: {'是' if stats.get('exam_mode') else '否'}

## 注意力总体数据
- 平均注意力分数: {stats.get('avg_attention', 0)}%
- 注意力分布: 高(≥75%) {stats.get('high_attention_count', 0)}人, 中(50-75%) {stats.get('medium_attention_count', 0)}人, 低(<50%) {stats.get('low_attention_count', 0)}人

## 异常行为统计
- 低头人次: {stats.get('head_down_count', 0)} 人
- 转头人次: {stats.get('head_turn_count', 0)} 人
- 疲劳眨眼人次: {stats.get('fatigue_count', 0)} 人

## 学生注意力排行
### 注意力最高的5名学生
{stats.get('top_students', '暂无数据')}

### 注意力最低的5名学生
{stats.get('bottom_students', '暂无数据')}

## 注意力时间趋势
{stats.get('time_trend', '暂无数据')}

请按以下格式输出（使用 Markdown）:
1. 整体评价（对课堂整体注意力水平的综合评价）
2. 注意力分析（分布特点、时间趋势分析）
3. 主要问题（列出最突出的2-3个问题）
4. 教学改进建议（针对发现的问题给出具体可操作的建议）
5. 重点关注学生（对注意力偏低的学生给出个别化建议）"""

    try:
        response = ollama.chat(
            model=settings.OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}],
        )
        content = response["message"]["content"]
    except Exception as e:
        logger.error(f"Ollama 生成报告失败: {e}")
        return _fallback_report(stats)

    content = _strip_think_tags(content)
    if not content:
        return _fallback_report(stats)
    return content


def _fallback_report(stats: dict) -> str:
    avg = stats.get('avg_attention', 0)
    head_down = stats.get('head_down_count', 0)
    head_turn = stats.get('head_turn_count', 0)
    fatigue = stats.get('fatigue_count', 0)
    total = stats.get('total_students', 0)
    duration = stats.get('duration', 0)
    classroom_name = stats.get('classroom_name', '未知')
    high = stats.get('high_attention_count', 0)
    medium = stats.get('medium_attention_count', 0)
    low = stats.get('low_attention_count', 0)
    top_students = stats.get('top_students', '暂无数据')
    bottom_students = stats.get('bottom_students', '暂无数据')
    time_trend = stats.get('time_trend', '暂无数据')

    if avg >= 75:
        level = "良好"
    elif avg >= 50:
        level = "一般"
    else:
        level = "偏低"

    return f"""## 整体评价

**{classroom_name}** 课堂平均注意力分数为 **{avg}%**，整体注意力水平**{level}**。课堂时长 {duration} 分钟，参与学生 {total} 人。

## 注意力分析

### 注意力分布
- 高注意力（≥75%）：{high} 人
- 中注意力（50-75%）：{medium} 人
- 低注意力（<50%）：{low} 人

### 注意力时间趋势
{time_trend}

## 主要问题

- 低头人次：{head_down} 人
- 转头人次：{head_turn} 人
- 疲劳眨眼人次：{fatigue} 人

## 重点关注学生

### 注意力最高的5名学生
{top_students}

### 注意力最低的5名学生
{bottom_students}

## 教学改进建议

1. 针对低头较多的学生，建议增加课堂互动提问
2. 适当调整教学节奏，在注意力下降时段插入讨论环节
3. 关注疲劳学生，必要时安排短暂休息
4. 对注意力偏低的学生进行个别辅导和关注

> 注：此报告为基于统计数据的模板生成（AI 服务暂时不可用）"""
