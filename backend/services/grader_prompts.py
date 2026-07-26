"""批改层 Prompt 模板与降级常量（从 grader.py 抽取）

集中放置所有 LLM 提示词与 Level 0 降级用的兜底 rubric，
便于后续调优 / A-B 测试时只改一处。
"""

# ===== 数学批改 Prompt =====

RUBRIC_GENERATION_PROMPT = """你是一位资深的{subject}教师，请为以下题目推导步骤评分标准。

## 题目（{total_score}分）
{question}

## 标准答案
{standard_answer}

请推导评分标准，输出JSON：
1. 列出解题关键步骤（3-6步），每步描述应具体明确
2. 为每个步骤分配分值（总和={total_score}），前序步骤分值稍多、末尾步骤稍少
3. 标注 required（true=必须项，没写直接0分 / false=加分项）
4. 提供该步骤的关键词匹配列表和示例表达

【注意】至少生成3个步骤，确保评分粒度足够细。对于简单计算题，拆分为：列式→计算→结果三步。

严格输出以下JSON格式，不要输出其他内容：
{{"steps": [{{"step_id": "s1", "description": "...", "score": N, "required": true, "keywords": ["..."], "example": "..."}}]}}"""

MATH_GRADING_PROMPT = """你是一位专业的数学教师，请基于以下评分标准对学生解答进行逐步批改。

【重要】学生的解答文本是可正常阅读的，请仔细阅读后给出评分。不要说"无法辨识"——文本是清晰可读的。

## 题目
{question}

## 评分标准（Rubric）
{rubric_json}

## 标准答案
{standard_answer}

## 学生解答
{student_answer}
{geometry_section}

## 批改要求
请逐步骤判定：
1. 匹配每个rubric步骤，判断学生是否完成
2. 对每个步骤给出correct/partial/missing判定和得分
3. 评分锚点：
   - 完全正确：给该步骤满分
   - 部分正确（思路对但计算错）：给该步骤一半分数
   - 完全错误或缺失：给0分
4. 指出具体错误原因（如有）
5. 生成一句个性化评语（结合错因与知识薄弱点）
6. 对每个错误步骤标注错因标签（从以下6种选择：计算粗心、概念混淆、审题不清、辅助线缺失、逻辑跳步、知识缺失）
7. 如果学生答案与标准答案完全一致，所有步骤应标记为correct，error_cause填"none"

严格输出以下JSON格式，不要输出其他内容：
{{"steps": [{{"step_id": "s1", "content": "学生写的步骤内容", "correct": true, "score": N, "rubric_ref": "s1", "error_reason": null}}], "error_type": "calculation_error|concept_error|process_error|none", "error_cause": "计算粗心|概念混淆|审题不清|辅助线缺失|逻辑跳步|知识缺失|none", "knowledge_points": ["知识点1"], "comment": "个性化评语"}}"""

# 几何题辅助线评估指令（追加到MATH_GRADING_PROMPT的geometry_section占位符）
GEOMETRY_AUXILIARY_LINE_PROMPT_SECTION = """
## 几何辅助线评估提示
本题是几何证明/计算题，请特别关注以下方面：
- 学生是否画了辅助线（如虚线、延长线、连接线等）
- 辅助线是否正确（方向、位置是否合理）
- 是否缺失关键辅助线
- 辅助线使用情况应反映在错因标签中（如"辅助线缺失"）
- 评语中需包含辅助线相关的提示或建议
"""

COMMENT_GENERATION_PROMPT = """基于以下批改结果，生成一句简短个性化评语。

题目：{question}
学生得分：{score}/{max_score}
错误步骤：{error_steps}
错因类型：{error_type}
薄弱知识点：{knowledge_points}

要求：评语要具体指出问题并给出改进建议，不要空泛鼓励。"""


# ===== 作文批改 Prompt =====

ESSAY_OCR_LOW_CONFIDENCE_HINT = """**提示**：本次文本识别置信度较低（{confidence:.2f}），书写维度评分时适当关注，但其他维度仍以文本实际内容为准。"""

ESSAY_GRADING_PROMPT = """你是一位资深的语文作文阅卷老师，请按中考作文四维评分标准对以下学生作文进行评分。

【重要】下面的学生作文文本是完整的、可正常阅读的中文文本，请仔细阅读全文后给出评分。不要说"无法辨识"或"内容不可读"——文本内容是清晰可读的，你应当基于文本实际内容进行评分。

## 作文题目
{question}

## 写作要求（参考）
{standard_answer}

## 学生作文
{student_answer}

{ocr_confidence_hint}

## 评分标准（总分100分）
请按以下四个维度独立评分，评分要参考以下锚点：
- 内容：切题且素材丰富=28-40分；切题但素材一般=20-27分；偏题=10-19分；严重跑题=0-9分
- 结构：结构完整且层次清晰=14-20分；结构基本完整=10-13分；结构混乱=5-9分；无结构=0-4分
- 语言：流畅且有修辞=18-25分；通顺但平淡=12-17分；有语病=6-11分；不通顺=0-5分
- 书写：无错别字=12-15分；少量错别字=8-11分；较多错别字=4-7分；大量错别字=0-3分

1. **内容**（满分40分）：审题立意是否准确、主题是否明确、素材是否丰富贴切、思想感情是否真实健康
2. **结构**（满分20分）：篇章布局是否合理、段落过渡是否自然、开头结尾是否呼应、详略是否得当
3. **语言**（满分25分）：用词是否准确丰富、修辞是否恰当、句式是否有变化、是否通顺流畅
4. **书写**（满分15分）：是否有错别字、语句是否通顺（基于文本质量推断书写规范性）

## 评分要求
- 必须仔细阅读学生作文全文后再评分，评语要引用原文片段佐证
- 每个维度从以下5种错因中选1种最贴切的（无错填"none"）：素材匮乏、逻辑断层、修辞单一、偏题跑题、书写潦草
- 选出最主要的一个错因作为整体错因（primary_error_cause）
- 列出最薄弱的1-2个维度名称作为knowledge_points（从"内容/结构/语言/书写"中选）

严格输出以下JSON格式，不要输出其他内容：
{{"dimensions": {{"content": {{"score": N, "max_score": 40, "comment": "...", "error_cause": "偏题跑题|素材匮乏|none"}}, "structure": {{"score": N, "max_score": 20, "comment": "...", "error_cause": "逻辑断层|none"}}, "language": {{"score": N, "max_score": 25, "comment": "...", "error_cause": "修辞单一|none"}}, "handwriting": {{"score": N, "max_score": 15, "comment": "...", "error_cause": "书写潦草|none"}}}}, "primary_error_cause": "素材匮乏|逻辑断层|修辞单一|偏题跑题|书写潦草|none", "knowledge_points": ["薄弱维度1"], "overall_comment": "综合评语"}}"""

ESSAY_COMMENT_GENERATION_PROMPT = """基于以下作文四维批改结果，生成一段简短的个性化评语。

## 作文题目
{question}

## 总得分
{score}/{max_score}

## 四维详情
- 内容（{content_score}/{content_max}）：{content_comment}
- 结构（{structure_score}/{structure_max}）：{structure_comment}
- 语言（{language_score}/{language_max}）：{language_comment}
- 书写（{handwriting_score}/{handwriting_max}）：{handwriting_comment}

## 主要错因
{error_cause}

## 薄弱维度
{knowledge_points}

## 要求
1. 评语要贴合语文作文特性，避免出现"步骤评分""推理过程"等数学化术语
2. 先肯定优点，再指出最关键的1-2个改进方向
3. 不要超过100字，简洁有力，给出可操作的修改建议"""


# ===== Level 0 降级：兜底 rubric =====

# 数学题规则兜底评分标准（所有 LLM 失败时使用）
FALLBACK_RUBRIC = {
    "steps": [
        {"step_id": "s1", "description": "列式/建立方程", "score": 2, "required": True, "keywords": ["设", "令", "因为", "所以", "="], "example": ""},
        {"step_id": "s2", "description": "计算过程", "score": 2, "required": True, "keywords": ["代入", "化简", "解得", "计算"], "example": ""},
        {"step_id": "s3", "description": "最终答案", "score": 1, "required": True, "keywords": ["答", "故", "因此"], "example": ""},
    ]
}

# 作文四维占位 rubric（供题库存储使用）
FALLBACK_ESSAY_RUBRIC = {
    "type": "essay",
    "dimensions": [
        {"step_id": "dim_content", "description": "内容", "score": 40, "required": True, "keywords": [], "example": ""},
        {"step_id": "dim_structure", "description": "结构", "score": 20, "required": True, "keywords": [], "example": ""},
        {"step_id": "dim_language", "description": "语言", "score": 25, "required": True, "keywords": [], "example": ""},
        {"step_id": "dim_handwriting", "description": "书写", "score": 15, "required": True, "keywords": [], "example": ""},
    ],
}
