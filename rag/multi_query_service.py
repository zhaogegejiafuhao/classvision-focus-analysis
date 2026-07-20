"""Multi-Query / RAG-Fusion 查询扩展

核心思想：单个 query 视角有限，让 LLM 生成多个不同视角的查询变体，
分别检索后用 RRF 融合，能召回更多语义相关文档。

与 HyDE 的区别：
- HyDE：生成假答案文档 → 用假答案做 Dense 检索（解决短 query 语义模糊）
- Multi-Query：生成多个查询变体 → 多路检索后 RRF 融合（解决单视角召回盲区）

工程约束：
- 仅对中等长度 query 启用（短 query 交给 HyDE，长 query 已足够具体）
- 每次 multi_query_count 轮额外 LLM 调用，延迟成本高
- 仅在 Tier4 混合检索路径触发
"""

import logging
import re
import time
from typing import List, Optional

from backend.core.config import settings
from backend.services.llm_client import get_llm, LLMError, _strip_think_tags

logger = logging.getLogger("rag")


class MultiQueryService:
    """Multi-Query 查询扩展服务"""

    def __init__(
        self,
        ollama_host: Optional[str] = None,
        ollama_model: Optional[str] = None,
    ):
        # ollama_host / ollama_model 保留参数以兼容外部调用，实际由 llm_client 管理
        pass

    def should_apply(self, question: str) -> bool:
        """判断是否需要 Multi-Query 扩展

        规则：
        1. 全局开关 RAG_MULTI_QUERY_ENABLED 必须开启
        2. query 长度在 [MIN_LEN, MAX_LEN] 范围内（短 query 交给 HyDE）
        3. 跳过纯标识符查询
        """
        if not settings.RAG_MULTI_QUERY_ENABLED:
            return False
        q = question.strip()
        if len(q) < settings.RAG_MULTI_QUERY_MIN_LEN:
            return False
        if len(q) > settings.RAG_MULTI_QUERY_MAX_LEN:
            return False
        if re.match(r'^[A-Za-z0-9\-_]+$', q):
            return False
        return True

    def generate_queries(self, question: str) -> List[str]:
        """调用 LLM 生成多个查询变体

        Returns: 查询列表（包含原始 query）。失败时仅返回 [原始query]。
        """
        if not self.should_apply(question):
            return [question]

        count = settings.RAG_MULTI_QUERY_COUNT
        llm = get_llm("deep")
        messages = [
            {"role": "system", "content": f"查询改写器。输出{count}个改写查询，每行一个，无序号无解释无标点符号开头。直接输出查询内容。"},
            {"role": "user", "content": f"原查询：{question}\n\n输出{count}个不同视角的改写查询（每行一个，直接输出，不要任何前缀）："},
        ]

        t0 = time.time()
        try:
            result = llm.chat(messages, max_tokens=200, think=False, temperature=0.8)
            raw = result["content"].strip()
            if not raw:
                raw = (result.get("thinking") or "").strip()
            raw = _strip_think_tags(raw)

            variants = self._parse_variants(raw, count)
            if not variants:
                logger.warning("multi_query_empty question=%r raw_len=%d", question, len(raw))
                return [question]

            queries = [question] + variants
            logger.info(
                "multi_query_generated question=%r count=%d elapsed_ms=%d variants=%s",
                question, len(variants), int((time.time() - t0) * 1000), variants,
            )
            return queries
        except LLMError:
            logger.warning("multi_query_llm_unreachable question=%r", question)
            return [question]
        except Exception as e:
            logger.warning("multi_query_failed question=%r error=%s", question, e)
            return [question]

    def _parse_variants(self, raw: str, expected_count: int) -> List[str]:
        """从 LLM 输出中解析查询变体列表"""
        if not raw:
            return []

        lines = [line.strip() for line in raw.splitlines() if line.strip()]
        cleaned = []
        for line in lines:
            line = re.sub(r'^[\d]+[.、)]\s*', '', line)
            line = re.sub(r'^[-*]\s*', '', line)
            line = re.sub(r'^["""\']+', '', line).rstrip('"""\'')
            # 过滤自言自语行和 prompt 泄漏（安全网，think=True 后通常不需要）
            filter_prefixes = [
                '首先', '关键点', '只输出', '用户要求', '我需要', '让我', '注意：',
                '原查询', '无序号', '无解释', '所以输出', '不要任何', '输出时',
                '用户指定', '我注意到', '每个查询', '不同视角', '不同方面',
            ]
            if any(line.startswith(prefix) for prefix in filter_prefixes):
                continue
            if line and len(line) >= 2:
                cleaned.append(line)
        return cleaned[:expected_count]
