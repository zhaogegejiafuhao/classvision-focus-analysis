import logging

from backend.services.llm_client import get_llm, LLMError

logger = logging.getLogger(__name__)


def generate_report(stats: dict) -> str:
    """生成课堂分析报告（使用统一 LLM Provider + think=True）"""
    prompt = _build_report_prompt(stats)
    
    try:
        result = get_llm().chat(
            messages=[{"role": "user", "content": prompt}],
            think=True,
            temperature=0.7,
            max_tokens=2048,
        )
        content = result.get("content", "")
        if not content:
            logger.warning("LLM 返回空 content，使用 fallback 报告")
            return _fallback_report(stats)
        
        return content.strip()
        
    except LLMError as e:
        logger.error(f"LLM 生成报告失败: {e}")
        return _fallback_report(stats)


def _build_report_prompt(stats: dict) -> str:
    """构建报告生成 prompt"""
    avg = stats.get('avg_attention', 0)
    head_down = stats.get('head_down_count', 0)
    head_turn = stats.get('head_turn_count', 0)
    fatigue = stats.get('fatigue_count', 0)
    total = stats.get('total_students', 0)
    duration = stats.get('duration', 0)
    classroom_name = stats.get('classroom_name', '未知')
    teacher_name = stats.get('teacher_name', '未知')
    exam_mode = stats.get('exam_mode', False)
    high = stats.get('high_attention_count', 0)
    medium = stats.get('medium_attention_count', 0)
    low = stats.get('low_attention_count', 0)
    top_students = stats.get('top_students', '暂无数据')
    bottom_students = stats.get('bottom_students', '暂无数据')
    time_trend = stats.get('time_trend', '暂无数据')
    
    return f"""你是一位资深教学分析专家。请根据以下课堂统计数据，生成一份专业、客观、可操作的课堂教学分析报告。

## 课堂基本信息
- 课程名称: {classroom_name}
- 授课教师: {teacher_name}
- 课堂时长: {duration} 分钟
- 参与学生数: {total} 人
- 考场模式: {'是' if exam_mode else '否'}

## 注意力总体数据
- 平均注意力分数: {avg}%
- 注意力分布: 高(≥75%) {high}人, 中(50-75%) {medium}人, 低(<50%) {low}人

## 异常行为统计
- 低头人次: {head_down} 人
- 转头人次: {head_turn} 人
- 疲劳眨眼人次: {fatigue} 人

## 学生注意力排行
### 注意力最高的5名学生
{top_students}

### 注意力最低的5名学生
{bottom_students}

## 注意力时间趋势
{time_trend}

请按以下格式输出 Markdown 格式的报告：

# 课堂教学分析报告

## 一、整体评价
（对课堂整体注意力水平的综合评价，包括整体等级判断）

## 二、注意力分析

### 2.1 分布特点
（分析高/中/低注意力学生的分布情况）

### 2.2 时间趋势
（分析注意力随时间的变化趋势，指出关键时段）

### 2.3 异常行为
（分析低头、转头、疲劳等异常行为的统计意义）

## 三、主要问题
（列出最突出的2-3个问题，每个问题附带具体数据支撑）

## 四、教学改进建议
（针对发现的问题给出具体可操作的建议，按优先级排序）

## 五、重点关注学生
（对注意力偏低的学生给出个别化建议）

---
*报告生成时间: {stats.get('generated_time', '自动生成')}*

要求：
1. 分析要基于数据，避免空泛描述
2. 建议要具体可操作，避免"加强关注"等泛泛之谈
3. 语言要专业但通俗易懂
4. 直接输出报告内容，不要有任何开场白或额外说明"""


def _fallback_report(stats: dict) -> str:
    """生成 fallback 报告（当 Ollama 不可用时）"""
    avg = stats.get('avg_attention', 0)
    head_down = stats.get('head_down_count', 0)
    head_turn = stats.get('head_turn_count', 0)
    fatigue = stats.get('fatigue_count', 0)
    total = stats.get('total_students', 0)
    duration = stats.get('duration', 0)
    classroom_name = stats.get('classroom_name', '未知')
    teacher_name = stats.get('teacher_name', '未知')
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

    return f"""# 课堂教学分析报告

## 一、整体评价

**{classroom_name}**（授课教师：{teacher_name}）课堂平均注意力分数为 **{avg}%**，整体注意力水平**{level}**。课堂时长 {duration} 分钟，参与学生 {total} 人。

## 二、注意力分析

### 2.1 分布特点
- 高注意力（≥75%）：{high} 人（{round(high/total*100, 1) if total else 0}%）
- 中注意力（50-75%）：{medium} 人（{round(medium/total*100, 1) if total else 0}%）
- 低注意力（<50%）：{low} 人（{round(low/total*100, 1) if total else 0}%）

### 2.2 时间趋势
{time_trend}

### 2.3 异常行为
- 低头人次：{head_down} 人
- 转头人次：{head_turn} 人
- 疲劳眨眼人次：{fatigue} 人

## 三、主要问题

1. 低头行为：{head_down} 人次出现低头行为，可能存在注意力分散
2. 转头行为：{head_turn} 人次出现转头行为，可能受到环境干扰
3. 疲劳表现：{fatigue} 人次出现疲劳眨眼，可能需要调整教学节奏

## 四、教学改进建议

1. **增加互动**：针对低头较多的学生，建议增加课堂互动提问频率
2. **调整节奏**：在注意力下降时段插入讨论环节或短暂休息
3. **环境优化**：减少教室环境干扰因素，保持良好光线和通风
4. **个别关注**：对注意力持续偏低的学生进行课后个别辅导

## 五、重点关注学生

### 注意力最高的5名学生
{top_students}

### 注意力最低的5名学生
{bottom_students}

建议对这些学生进行针对性关注和辅导。

---
*注：此报告为基于统计数据的模板生成（AI 服务暂时不可用）*
"""