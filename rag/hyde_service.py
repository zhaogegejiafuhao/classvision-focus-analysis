"""HyDE (Hypothetical Document Embeddings) 查询改写

核心思想：短口语 query 与文档书面文本存在语义鸿沟，向量检索效果差。
让 LLM 先生成一段「假答案文档」（即使内容不准，但术语和句式接近真实文档），
再用假答案做向量检索，语义距离远小于简短用户问句。

工程约束：仅对 <RAG_HYDE_MIN_QUERY_LEN 字的极短 query 启用，每次多一轮 LLM 调用，
长完整问句无需开启，避免翻倍接口延迟。
"""

import logging
import re
import time
from typing import Optional

from backend.core.config import settings
from backend.services.llm_client import get_llm, LLMError, _strip_think_tags

logger = logging.getLogger("rag")


class HyDEService:
    """HyDE 查询改写服务"""

    def __init__(
        self,
        ollama_host: Optional[str] = None,
        ollama_model: Optional[str] = None,
        max_tokens: Optional[int] = None,
    ):
        # ollama_host / ollama_model 保留参数以兼容外部调用，实际由 llm_client 管理
        self.max_tokens = max_tokens or settings.RAG_HYDE_MAX_TOKENS

    def should_apply(self, question: str) -> bool:
        """判断是否需要 HyDE 改写

        规则：
        1. 全局开关 RAG_HYDE_ENABLED 必须开启
        2. query 长度 < RAG_HYDE_MIN_QUERY_LEN 字（极短口语）
        3. 跳过纯标识符查询（订单号/SKU/编号类，交给 BM25 更合适）
        """
        if not settings.RAG_HYDE_ENABLED:
            return False
        q = question.strip()
        if len(q) >= settings.RAG_HYDE_MIN_QUERY_LEN:
            return False
        # 跳过纯编号/数字/字母数字混合串（交给 BM25）
        if re.match(r'^[A-Za-z0-9\-_]+$', q):
            return False
        return True

    def generate_hypothetical_answer(self, question: str) -> Optional[str]:
        """调用 LLM 生成假答案文档

        Returns: 假答案文本；失败时返回 None，调用方应回退到原 query
        """
        llm = get_llm("deep")
        messages = [
            {"role": "system", "content": "You are a technical writer. Output ONLY the answer text, no explanation, no preamble."},
            {"role": "user", "content": f"请用专业、书面化的语言回答以下问题，生成一段约 {self.max_tokens} 字的回答。使用领域专业术语和书面句式，内容不需要完全准确但要符合常见解答模式。直接输出答案正文。\n\n问题：{question}"},
        ]

        t0 = time.time()
        try:
            result = llm.chat(messages, max_tokens=300, think=False, temperature=0.7)
            content = result["content"].strip()
            # fallback: 如果 content 为空，尝试 thinking 字段
            if not content:
                content = (result.get("thinking") or "").strip()
            content = _strip_think_tags(content)

            if not content or len(content) < 5:
                logger.warning("hyde_empty question=%r", question)
                return None

            logger.info(
                "hyde_generated question=%r hypo_len=%d elapsed_ms=%d hypo_preview=%s",
                question, len(content), int((time.time() - t0) * 1000), content[:80],
            )
            return content
        except LLMError:
            logger.warning("hyde_llm_unreachable question=%r", question)
            return None
        except Exception as e:
            logger.warning("hyde_failed question=%r error=%s", question, e)
            return None

    def rewrite(self, question: str) -> str:
        """主入口：若需要改写返回假答案，否则原样返回 query

        调用方应在检索前调用此方法，把返回值作为新的检索 query。
        注意：重排和 LLM 生成仍应使用原始 question，而非假答案。
        """
        if not self.should_apply(question):
            return question
        hypo = self.generate_hypothetical_answer(question)
        if not hypo:
            return question
        return hypo
