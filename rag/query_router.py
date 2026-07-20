"""规则查询路由器（Adaptive Query Routing - Rule-Based）

基于正则、关键词、长度规则将 query 分流到最优检索链路，避免单一检索方式的盲区。

四层分流（从简单到复杂）：
- Tier1 通用知识：无业务私有数据依赖（如「什么是 RAG」），跳过检索直接 LLM
- Tier2 精确标识符：订单号/SKU/编号/数字序列，仅走 BM25 关键词检索
- Tier3 纯语义模糊：概念/流程/方法类，仅走 Dense 向量检索
- Tier4 复杂混合：编号+语义或一般查询，Dense + BM25 + RRF 融合

工程取舍：规则路由零训练成本、可解释、低延迟，是中小项目标配。
规则随业务扩张需要持续维护，无法覆盖模糊边界 Query。
"""

import logging
import re
from enum import Enum

logger = logging.getLogger("rag")


class RouteTier(str, Enum):
    """查询路由分层"""
    TIER1_LLM_ONLY = "tier1_llm_only"        # 通用知识，跳过检索
    TIER2_BM25_ONLY = "tier2_bm25_only"      # 精确标识符，仅 BM25
    TIER3_DENSE_ONLY = "tier3_dense_only"    # 纯语义，仅 Dense
    TIER4_HYBRID = "tier4_hybrid"            # 混合查询，Dense + BM25 + RRF


# 通用知识意图词（无业务数据依赖，可直接由 LLM 回答）
GENERAL_KNOWLEDGE_PATTERNS = [
    r'^(什么是|什么叫|何为|什么是)',
    r'(的定义是|的含义是|是什么意思|是指什么)',
    r'^(如何|怎么)(安装|配置|使用|部署)[\w\s]*$',  # 通用工具操作，无业务上下文
    r'^(Python|Java|Git|Docker|SQL|HTML|CSS|JavaScript)[\s的]?',  # 通用技术名词开头
]

# 精确标识符模式：订单号、SKU、编号、学号、合同号等
IDENTIFIER_PATTERNS = [
    r'^[A-Za-z]{2,}[\-_]?\d[\d\-_]*$',   # ORD-2024-0891, SKU123, CV-2024-001
    r'^\d{4,}$',                          # 纯数字编号（>=4位）
    r'\b[A-Z]{2,}\d{4,}\b',               # 大写字母+数字（如 CV2024）
    r'^[A-Z]\d{6,}$',                     # 学号格式如 S2024001
]

# 业务术语（出现时不应走 Tier1 LLM-only，应该检索业务文档）
BUSINESS_TERMS = [
    '课堂', '注意力', '学生', '教师', '考试', '报告', 'ClassVision',
    '课堂数据', '低头', '转头', '疲劳', '眨眼', 'head', 'pitch', 'yaw',
    '知识库', '文档', 'RAG', '检索',
]

# 语义意图词（流程、概念咨询，适合 Dense 语义匹配）
SEMANTIC_INTENT_PATTERNS = [
    r'(怎么|如何|为什么|为何|流程|步骤|方法|策略|原理|机制|区别|对比|优劣|优缺点)',
    r'(建议|推荐|方案|措施|改进|优化|提升|降低|增加|减少)',
    r'(分析|评估|诊断|监测|识别|检测|预测)',
]


def route_query(question: str) -> RouteTier:
    """基于规则的查询路由

    Args:
        question: 用户查询（已 strip）

    Returns:
        RouteTier 分层决策
    """
    q = question.strip()
    if not q:
        return RouteTier.TIER4_HYBRID

    # Tier2: 纯标识符（订单号/SKU/编号）— 仅 BM25
    # 优先判断，因为标识符 query 不应走向量检索
    for pattern in IDENTIFIER_PATTERNS:
        if re.match(pattern, q) or re.search(pattern, q):
            logger.info("route tier2_bm25_only question=%r pattern=%s", q, pattern)
            return RouteTier.TIER2_BM25_ONLY

    # Tier1: 通用知识（无业务术语 + 通用意图词）— 跳过检索
    has_business_term = any(term in q for term in BUSINESS_TERMS)
    if not has_business_term:
        for pattern in GENERAL_KNOWLEDGE_PATTERNS:
            if re.search(pattern, q):
                logger.info("route tier1_llm_only question=%r pattern=%s", q, pattern)
                return RouteTier.TIER1_LLM_ONLY

    # Tier3: 纯语义（包含语义意图词且无标识符）— 仅 Dense
    has_identifier = any(re.search(p, q) for p in IDENTIFIER_PATTERNS)
    has_semantic_intent = any(re.search(p, q) for p in SEMANTIC_INTENT_PATTERNS)
    if has_semantic_intent and not has_identifier:
        logger.info("route tier3_dense_only question=%r", q)
        return RouteTier.TIER3_DENSE_ONLY

    # Tier4: 默认混合（Dense + BM25 + RRF）
    logger.info("route tier4_hybrid question=%r", q)
    return RouteTier.TIER4_HYBRID
