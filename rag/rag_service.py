"""RAG检索服务：混合检索(Dense+BM25+RRF) + Cross-Encoder 重排 + 生成回答"""

import logging
import time
from typing import List, Optional

from backend.core.config import settings
from backend.services.llm_client import get_llm, LLMError, _strip_think_tags
from rag.embedding_service import EmbeddingService
from rag.bm25_service import BM25Service
from rag.hybrid_search import rrf_fusion, rrf_fusion_multi
from rag.reranker_service import RerankerService
from rag.hyde_service import HyDEService
from rag.multi_query_service import MultiQueryService
from rag.query_router import route_query, RouteTier

logger = logging.getLogger("rag")


class RAGService:
    """RAG服务（混合检索 + Cross-Encoder 重排）"""

    # 混合检索候选数量（两路各取 candidate_k，融合后取 top_k 送入重排）
    CANDIDATE_K = 50

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.bm25_service = BM25Service(settings.RAG_INDEX_DIR)
        self.top_k = settings.RAG_TOP_K
        # 重排器懒加载（仅在启用时初始化，避免未使用时加载 2GB 模型）
        self._reranker: Optional[RerankerService] = None
        # HyDE 查询改写（仅在短 query 启用，每次多一轮 LLM 调用）
        self.hyde_service = HyDEService()
        # Multi-Query 查询扩展（中等长度 query 生成多个变体，多路检索后 RRF 融合）
        self.multi_query_service = MultiQueryService()

    def _get_reranker(self) -> Optional[RerankerService]:
        """懒加载重排器"""
        if not settings.RAG_RERANKER_ENABLED:
            return None
        if self._reranker is None:
            self._reranker = RerankerService(
                model_name=settings.RAG_RERANKER_MODEL,
                cache_dir=settings.RAG_CACHE_DIR,
                device=settings.RAG_RERANKER_DEVICE,
            )
        return self._reranker

    def _hybrid_search(
        self,
        question: str,
        top_k: int,
        tier: RouteTier = None,
        enable_hyde: bool = True,
        enable_multi_query: bool = True,
    ) -> List[dict]:
        """按路由分层检索

        - Tier2 BM25_ONLY：仅 Sparse 检索（标识符/编号类）
        - Tier3 DENSE_ONLY：仅 Dense 检索（概念/流程类，HyDE 改写后）
        - Tier4 HYBRID：Dense + BM25 并行 + RRF 融合（默认）
        - Tier1 LLM_ONLY：调用方应在 query() 中短路，不进入此方法

        HyDE 策略：短口语 query 时，Dense 用 LLM 生成的假答案文档检索，
        BM25 仍用原始 query（字面匹配，假答案会稀释关键词）。

        enable_hyde/enable_multi_query: 双模式控制（fast 模式强制关闭，deep 模式按全局配置）
        """
        if tier is None:
            tier = route_query(question) if settings.RAG_QUERY_ROUTER_ENABLED else RouteTier.TIER4_HYBRID

        candidate_k = max(self.CANDIDATE_K, top_k * 3)

        # Tier2: 仅 BM25（标识符/编号）
        if tier == RouteTier.TIER2_BM25_ONLY:
            sparse_results = self.bm25_service.search(question, candidate_k)
            logger.info(
                "hybrid_search tier=%s question=%r sparse=%d",
                tier.value, question, len(sparse_results),
            )
            return sparse_results[:top_k]

        # HyDE 改写：仅对短 query 启用，返回假答案或原 query
        # fast 模式下强制跳过（节省 ~22s LLM 调用）
        if enable_hyde:
            dense_query = self.hyde_service.rewrite(question)
        else:
            dense_query = question
        hyde_applied = dense_query != question

        # Tier3: 仅 Dense（概念/流程类）
        if tier == RouteTier.TIER3_DENSE_ONLY:
            # Multi-Query 扩展：生成多个变体，多路 Dense 检索后 RRF 融合
            if enable_multi_query and self.multi_query_service.should_apply(question):
                return self._multi_query_search_tier3(question, dense_query, candidate_k, top_k, hyde_applied)
            dense_results = self.embedding_service.search(dense_query, candidate_k)
            logger.info(
                "hybrid_search tier=%s question=%r hyde=%s mq=%s dense=%d",
                tier.value, question, hyde_applied, enable_multi_query, len(dense_results),
            )
            return dense_results[:top_k]

        # Tier4: Dense + BM25 + RRF 融合（默认）
        # Multi-Query 扩展：中等长度 query 生成多个变体，多路检索后 RRF 融合
        if enable_multi_query and self.multi_query_service.should_apply(question):
            return self._multi_query_search(question, dense_query, candidate_k, top_k, hyde_applied)

        dense_results = self.embedding_service.search(dense_query, candidate_k)
        sparse_results = self.bm25_service.search(question, candidate_k)

        # 如果 BM25 索引未建立（无数据），仅用 Dense 结果
        if not sparse_results:
            logger.info(
                "hybrid_search tier=%s question=%r hyde=%s mq=%s dense=%d sparse=0 fallback_dense",
                tier.value, question, hyde_applied, enable_multi_query, len(dense_results),
            )
            return dense_results[:top_k]

        fused = rrf_fusion(dense_results, sparse_results, k=60, top_k=candidate_k)
        logger.info(
            "hybrid_search tier=%s question=%r hyde=%s mq=%s dense=%d sparse=%d fused=%d",
            tier.value, question, hyde_applied, enable_multi_query,
            len(dense_results), len(sparse_results), len(fused),
        )
        return fused

    def _multi_query_search(
        self, question: str, dense_query: str, candidate_k: int, top_k: int, hyde_applied: bool,
    ) -> List[dict]:
        """Multi-Query 检索：生成多个查询变体，多路 Dense+BM25 检索后 RRF 融合

        - 原始 query 用 HyDE 改写后的 dense_query 做 Dense 检索
        - 原始 query 用 question 做 BM25 检索
        - 每个变体分别做 Dense + BM25 检索
        - 所有结果用 rrf_fusion_multi 融合
        """
        queries = self.multi_query_service.generate_queries(question)
        multi_applied = len(queries) > 1

        if not multi_applied:
            # LLM 生成失败，回退到单路混合检索
            dense_results = self.embedding_service.search(dense_query, candidate_k)
            sparse_results = self.bm25_service.search(question, candidate_k)
            if not sparse_results:
                return dense_results[:top_k]
            return rrf_fusion(dense_results, sparse_results, k=60, top_k=candidate_k)

        all_result_lists = []
        # 原始 query 的 Dense（用 HyDE 改写后的）+ BM25（用原始）
        all_result_lists.append(self.embedding_service.search(dense_query, candidate_k))
        all_result_lists.append(self.bm25_service.search(question, candidate_k))
        # 每个变体的 Dense + BM25
        for variant in queries[1:]:
            all_result_lists.append(self.embedding_service.search(variant, candidate_k))
            all_result_lists.append(self.bm25_service.search(variant, candidate_k))

        fused = rrf_fusion_multi(all_result_lists, k=60, top_k=candidate_k)
        logger.info(
            "multi_query_search question=%r hyde=%s variants=%d lists=%d fused=%d",
            question, hyde_applied, len(queries) - 1, len(all_result_lists), len(fused),
        )
        return fused

    def _multi_query_search_tier3(
        self, question: str, dense_query: str, candidate_k: int, top_k: int, hyde_applied: bool,
    ) -> List[dict]:
        """Multi-Query 检索（Tier3 仅 Dense 版本）：生成多个变体，多路 Dense 检索后 RRF 融合

        Tier3 不走 BM25，所以每个变体只做 Dense 检索。
        """
        queries = self.multi_query_service.generate_queries(question)
        multi_applied = len(queries) > 1

        if not multi_applied:
            dense_results = self.embedding_service.search(dense_query, candidate_k)
            return dense_results[:top_k]

        all_result_lists = []
        all_result_lists.append(self.embedding_service.search(dense_query, candidate_k))
        for variant in queries[1:]:
            all_result_lists.append(self.embedding_service.search(variant, candidate_k))

        fused = rrf_fusion_multi(all_result_lists, k=60, top_k=candidate_k)
        logger.info(
            "multi_query_search_tier3 question=%r hyde=%s variants=%d lists=%d fused=%d",
            question, hyde_applied, len(queries) - 1, len(all_result_lists), len(fused),
        )
        return fused

    def _rerank(self, question: str, candidates: List[dict]) -> List[dict]:
        """Cross-Encoder 重排：对混合检索候选精排，取 top_k 送入 LLM"""
        reranker = self._get_reranker()
        if reranker is None:
            # 未启用重排，直接截断到 top_k
            return candidates[:self.top_k]
        return reranker.rerank(
            question,
            candidates,
            top_k=settings.RAG_RERANKER_TOP_K,
            max_candidates=settings.RAG_RERANKER_MAX_CANDIDATES,
        )

    def query(self, question: str, top_k: int = None, visible_doc_ids: set = None) -> dict:
        """检索并生成回答。visible_doc_ids: 可见文档ID集合，不在其中的文档块会被过滤掉"""
        if top_k is None:
            top_k = self.top_k

        # 查询路由：Tier1 通用知识直接 LLM 回答，跳过检索节省算力
        tier = route_query(question) if settings.RAG_QUERY_ROUTER_ENABLED else RouteTier.TIER4_HYBRID
        if tier == RouteTier.TIER1_LLM_ONLY:
            t0 = time.time()
            answer = self._generate_answer_no_context(question)
            logger.info(
                "rag_query_tier1 question=%r generation_ms=%d answer_preview=%s",
                question, int((time.time() - t0) * 1000), answer[:80],
            )
            return {
                'answer': answer,
                'sources': [],
                'retrieved_chunks': [],
                'route_tier': tier.value,
            }

        t0 = time.time()
        # 按路由分层检索（Tier2/3/4）
        retrieved_chunks = self._hybrid_search(question, top_k, tier)
        t_retrieval = time.time() - t0

        # 按可见性过滤检索结果（在生成前过滤，防止私有文档内容泄露到 LLM 回答中）
        pre_filter_count = len(retrieved_chunks)
        if visible_doc_ids is not None:
            retrieved_chunks = [
                c for c in retrieved_chunks
                if c.get('document_id') is None or c.get('document_id') in visible_doc_ids
            ]
        filtered_out = pre_filter_count - len(retrieved_chunks)

        if not retrieved_chunks:
            logger.info(
                "rag_query_empty question=%r top_k=%d retrieval_ms=%d filtered_out=%d",
                question, top_k, int(t_retrieval * 1000), filtered_out,
            )
            return {
                'answer': '知识库中没有找到相关内容。',
                'sources': [],
                'retrieved_chunks': [],
            }

        # Cross-Encoder 重排（启用时）
        t1 = time.time()
        retrieved_chunks = self._rerank(question, retrieved_chunks)
        t_rerank = time.time() - t1

        # 构建上下文
        context = self._build_context(retrieved_chunks)

        # 调用 LLM 生成回答
        t2 = time.time()
        answer = self._generate_answer(question, context)
        t_generation = time.time() - t2

        # 结构化日志：query/retrieved_chunks/score/answer 全链路
        logger.info(
            "rag_query_ok question=%r top_k=%d hits=%d filtered_out=%d "
            "retrieval_ms=%d rerank_ms=%d generation_ms=%d scores=%s sources=%s answer_preview=%s",
            question,
            top_k,
            len(retrieved_chunks),
            filtered_out,
            int(t_retrieval * 1000),
            int(t_rerank * 1000),
            int(t_generation * 1000),
            [round(c.get('rerank_score', c.get('score', c.get('rrf_score', 0))), 4) for c in retrieved_chunks],
            [c.get('source', '') for c in retrieved_chunks],
            answer[:80],
        )

        return {
            'answer': answer,
            'sources': [r['source'] for r in retrieved_chunks],
            'retrieved_chunks': retrieved_chunks,
        }

    def retrieve_only(
        self,
        question: str,
        top_k: int = None,
        visible_doc_ids: set = None,
        mode: str = "fast",
    ) -> dict:
        """仅检索，不生成回答。供 chat 端点使用——调用方自行构建 prompt 并调用 LLM。

        避免重复 LLM 调用：query() 内部会调 _generate_answer() 生成回答，
        但 chat_routes 只需要 retrieved_chunks，那一次生成完全浪费。

        mode: "fast"=快速模式（关闭 HyDE/Multi-Query，延迟低 ~10-20s）
              "deep"=深度模式（启用 HyDE/Multi-Query，延迟高 ~40-84s 但检索质量好）
        """
        if top_k is None:
            top_k = self.top_k

        tier = route_query(question) if settings.RAG_QUERY_ROUTER_ENABLED else RouteTier.TIER4_HYBRID
        if tier == RouteTier.TIER1_LLM_ONLY:
            return {'retrieved_chunks': [], 'route_tier': tier.value}

        # 双模式控制：fast 模式强制关闭 HyDE/Multi-Query，deep 模式按全局配置
        enable_hyde = (mode == "deep") and settings.RAG_HYDE_ENABLED
        enable_multi_query = (mode == "deep") and settings.RAG_MULTI_QUERY_ENABLED

        t0 = time.time()
        retrieved_chunks = self._hybrid_search(
            question, top_k, tier,
            enable_hyde=enable_hyde,
            enable_multi_query=enable_multi_query,
        )
        t_retrieval = time.time() - t0

        pre_filter_count = len(retrieved_chunks)
        if visible_doc_ids is not None:
            retrieved_chunks = [
                c for c in retrieved_chunks
                if c.get('document_id') is None or c.get('document_id') in visible_doc_ids
            ]
        filtered_out = pre_filter_count - len(retrieved_chunks)

        if not retrieved_chunks:
            logger.info(
                "retrieve_only_empty question=%r mode=%s top_k=%d retrieval_ms=%d filtered_out=%d",
                question, mode, top_k, int(t_retrieval * 1000), filtered_out,
            )
            return {'retrieved_chunks': [], 'route_tier': tier.value}

        # reranker 只在 deep 模式启用（CPU 重排 20 候选约 3s，fast 模式延迟优先）
        t_rerank = 0
        if mode == "deep":
            retrieved_chunks = self._rerank(question, retrieved_chunks)
            t_rerank = time.time() - t0 - t_retrieval
        else:
            retrieved_chunks = retrieved_chunks[:top_k]

        logger.info(
            "retrieve_only_ok question=%r mode=%s tier=%s top_k=%d hits=%d filtered_out=%d "
            "retrieval_ms=%d rerank_ms=%d scores=%s sources=%s",
            question, mode, tier.value, top_k, len(retrieved_chunks), filtered_out,
            int(t_retrieval * 1000), int(t_rerank * 1000),
            [round(c.get('rerank_score', c.get('score', c.get('rrf_score', 0))), 4) for c in retrieved_chunks],
            [c.get('source', '') for c in retrieved_chunks],
        )
        return {'retrieved_chunks': retrieved_chunks, 'route_tier': tier.value}

    def query_with_context(
        self,
        question: str,
        history_messages: List[dict],
        is_followup_flag: bool = False,
        top_k: int = None,
        visible_doc_ids: set = None,
    ) -> dict:
        """多轮对话查询：支持上下文历史和追问识别

        Args:
            question: 当前问题
            history_messages: 历史对话消息 [{"role": "user/assistant", "content": "..."}]
            is_followup_flag: 是否为追问（追问不触发新检索，复用上文检索结果）
            top_k: 检索数量
            visible_doc_ids: 可见文档ID集合
        """
        if top_k is None:
            top_k = self.top_k

        # 追问模式：不检索，直接用历史上下文回答
        if is_followup_flag and history_messages:
            t0 = time.time()
            answer = self._generate_answer_with_history(question, history_messages, context=None)
            t_gen = time.time() - t0
            logger.info(
                "rag_followup question=%r history_turns=%d generation_ms=%d answer_preview=%s",
                question, len(history_messages) // 2, int(t_gen * 1000), answer[:80],
            )
            return {
                'answer': answer,
                'sources': [],
                'retrieved_chunks': [],
                'is_followup': True,
            }

        # 新问题：查询路由 + 按层检索 + 生成（带历史上下文）
        tier = route_query(question) if settings.RAG_QUERY_ROUTER_ENABLED else RouteTier.TIER4_HYBRID

        # Tier1: 通用知识，跳过检索，直接用历史上下文回答
        if tier == RouteTier.TIER1_LLM_ONLY:
            t0 = time.time()
            answer = self._generate_answer_with_history(question, history_messages, context=None)
            logger.info(
                "rag_query_with_context_tier1 question=%r history_turns=%d generation_ms=%d answer_preview=%s",
                question, len(history_messages) // 2, int((time.time() - t0) * 1000), answer[:80],
            )
            return {
                'answer': answer,
                'sources': [],
                'retrieved_chunks': [],
                'is_followup': False,
                'route_tier': tier.value,
            }

        # Tier2/3/4: 按路由分层检索
        t0 = time.time()
        retrieved_chunks = self._hybrid_search(question, top_k, tier)
        t_retrieval = time.time() - t0

        # 可见性过滤
        if visible_doc_ids is not None:
            retrieved_chunks = [
                c for c in retrieved_chunks
                if c.get('document_id') is None or c.get('document_id') in visible_doc_ids
            ]

        if not retrieved_chunks:
            return {
                'answer': '知识库中没有找到相关内容。',
                'sources': [],
                'retrieved_chunks': [],
                'is_followup': False,
                'route_tier': tier.value,
            }

        # 重排
        retrieved_chunks = self._rerank(question, retrieved_chunks)

        context = self._build_context(retrieved_chunks)
        t1 = time.time()
        answer = self._generate_answer_with_history(question, history_messages, context=context)
        t_gen = time.time() - t1

        logger.info(
            "rag_query_with_context question=%r tier=%s top_k=%d hits=%d history_turns=%d "
            "retrieval_ms=%d generation_ms=%d answer_preview=%s",
            question, tier.value, top_k, len(retrieved_chunks), len(history_messages) // 2,
            int(t_retrieval * 1000), int(t_gen * 1000), answer[:80],
        )

        return {
            'answer': answer,
            'sources': [r['source'] for r in retrieved_chunks],
            'retrieved_chunks': retrieved_chunks,
            'is_followup': False,
            'route_tier': tier.value,
        }

    def _generate_answer_with_history(
        self,
        question: str,
        history_messages: List[dict],
        context: str = None,
    ) -> str:
        """带历史上下文调用 LLM 生成回答"""
        system_prompt = """你是一个专业的教学分析助手。请根据提供的参考资料和对话历史回答用户的问题。

要求：
1. 回答要基于参考资料，不要编造内容
2. 如果参考资料不足以回答问题，请明确说明"参考资料中未提供此信息"
3. 回答要简洁、专业、有针对性
4. 可以引用参考资料的来源
5. 如果是追问，请结合对话历史上下文回答
6. 参考资料是辅助线索，对话历史中的数字不可作为事实依据"""

        # 构建 user 消息
        if context:
            user_content = f"""参考资料：
{context}

用户问题：{question}

请根据以上参考资料回答用户的问题。"""
        else:
            # 追问模式：无新参考资料，依赖历史上下文
            user_content = f"用户问题：{question}\n\n请根据对话历史上下文回答。"

        messages = [{"role": "system", "content": system_prompt}]
        # 加入历史对话（最近 N 轮）
        for msg in history_messages[-8:]:  # 最多8条历史
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": user_content})

        try:
            llm = get_llm("deep")
            result = llm.chat(messages, max_tokens=1024, think=False, temperature=0.7)
            return _strip_think_tags(result["content"])
        except LLMError:
            return "⚠️ LLM 服务不可用，请检查配置。"
        except Exception as e:
            return f"生成回答失败: {e}"

    def _build_context(self, chunks: List[dict]) -> str:
        """构建上下文（支持父子分块扩展）

        父子分块模式：子分块精准匹配 → 扩展到父分块完整上下文 → 去重
        单层模式：直接使用分块内容
        """
        if settings.RAG_PARENT_CHILD_ENABLED:
            # 父子分块：扩展到父分块
            seen_parent_ids = set()
            context_parts = []
            for i, chunk in enumerate(chunks):
                parent_id = chunk.get('parent_id')
                if parent_id is not None:
                    if parent_id in seen_parent_ids:
                        continue  # 去重：同一父分块只出现一次
                    seen_parent_ids.add(parent_id)
                    parent_content = self.embedding_service.get_parent_content(parent_id)
                    if parent_content:
                        context_parts.append(f"[参考{i + 1}] {parent_content}")
                    else:
                        # 父分块内容缺失，退回子分块
                        context_parts.append(f"[参考{i + 1}] {chunk['content']}")
                else:
                    # 无父分块引用（单层兼容），直接使用
                    context_parts.append(f"[参考{i + 1}] {chunk['content']}")
            return "\n\n".join(context_parts)
        else:
            # 单层模式
            context_parts = []
            for i, chunk in enumerate(chunks):
                context_parts.append(f"[参考{i + 1}] {chunk['content']}")
            return "\n\n".join(context_parts)

    def _generate_answer(self, question: str, context: str) -> str:
        """调用 LLM 生成回答"""
        system_prompt = """你是一个专业的教学分析助手。请根据提供的参考资料回答用户的问题。

要求：
1. 直接回答问题，不要描述思考过程（如"首先我需要..."、"让我分析..."）
2. 回答要基于参考资料，不要编造内容
3. 如果参考资料不足以回答问题，请明确说明"参考资料中未提供此信息"
4. 回答要简洁、专业、有针对性，控制在300字以内
5. 可以引用参考资料的来源
6. 参考资料是检索得到的辅助线索，不可作为绝对事实依据"""

        prompt = f"""参考资料：
{context}

用户问题：{question}

请根据以上参考资料回答用户的问题。"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

        try:
            llm = get_llm("deep")
            result = llm.chat(messages, max_tokens=1024, think=False, temperature=0.7)
            return _strip_think_tags(result["content"])
        except LLMError:
            return "⚠️ LLM 服务不可用，请检查配置。"
        except Exception as e:
            return f"生成回答失败: {e}"

    def _generate_answer_no_context(self, question: str) -> str:
        """Tier1 LLM-only：无参考资料，直接用模型内置知识回答（通用知识类问题）"""
        system_prompt = """你是一个专业的助手。请直接回答用户的问题。

要求：
1. 回答要简洁、专业、有针对性
2. 如果问题超出你的知识范围，请明确说明
3. 不要编造不确定的内容"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ]

        try:
            llm = get_llm("deep")
            result = llm.chat(messages, max_tokens=1024, think=False, temperature=0.7)
            return _strip_think_tags(result["content"])
        except LLMError:
            return "⚠️ LLM 服务不可用，请检查配置。"
        except Exception as e:
            return f"生成回答失败: {e}"

    def stream_query(self, question: str, top_k: int = None, visible_doc_ids: set = None):
        """流式检索并生成回答，yield 事件字典。visible_doc_ids: 可见文档ID集合，不在其中的文档块会在生成前被过滤掉。"""
        if top_k is None:
            top_k = self.top_k

        # 查询路由
        tier = route_query(question) if settings.RAG_QUERY_ROUTER_ENABLED else RouteTier.TIER4_HYBRID

        # Tier1: 通用知识，跳过检索，直接流式 LLM 回答
        if tier == RouteTier.TIER1_LLM_ONLY:
            yield {'type': 'meta', 'sources': [], 'retrieved_chunks': [], 'route_tier': tier.value}
            system_prompt = """你是一个专业的助手。请直接回答用户的问题。

要求：
1. 回答要简洁、专业、有针对性
2. 如果问题超出你的知识范围，请明确说明
3. 不要编造不确定的内容"""
            yield from self._stream_llm(system_prompt, question)
            return

        t0 = time.time()
        # 按路由分层检索（Tier2/3/4）
        retrieved_chunks = self._hybrid_search(question, top_k, tier)
        t_retrieval = time.time() - t0

        # 按可见性过滤检索结果（在生成前过滤，防止私有文档内容泄露到 LLM 回答中）
        pre_filter_count = len(retrieved_chunks)
        if visible_doc_ids is not None:
            retrieved_chunks = [
                c for c in retrieved_chunks
                if c.get('document_id') is None or c.get('document_id') in visible_doc_ids
            ]
        filtered_out = pre_filter_count - len(retrieved_chunks)

        if not retrieved_chunks:
            logger.info(
                "rag_stream_empty question=%r tier=%s top_k=%d retrieval_ms=%d filtered_out=%d",
                question, tier.value, top_k, int(t_retrieval * 1000), filtered_out,
            )
            yield {'type': 'meta', 'sources': [], 'retrieved_chunks': [], 'route_tier': tier.value}
            yield {'type': 'done', 'content': '知识库中没有找到相关内容。'}
            return

        # Cross-Encoder 重排（启用时）
        t1 = time.time()
        retrieved_chunks = self._rerank(question, retrieved_chunks)
        t_rerank = time.time() - t1

        logger.info(
            "rag_stream_start question=%r tier=%s top_k=%d hits=%d filtered_out=%d "
            "retrieval_ms=%d rerank_ms=%d scores=%s sources=%s",
            question,
            tier.value,
            top_k,
            len(retrieved_chunks),
            filtered_out,
            int(t_retrieval * 1000),
            int(t_rerank * 1000),
            [round(c.get('rerank_score', c.get('score', c.get('rrf_score', 0))), 4) for c in retrieved_chunks],
            [c.get('source', '') for c in retrieved_chunks],
        )

        # 先发检索元信息，前端可立即展示参考来源
        sources = [r['source'] for r in retrieved_chunks]
        yield {'type': 'meta', 'sources': sources, 'retrieved_chunks': retrieved_chunks, 'route_tier': tier.value}

        context = self._build_context(retrieved_chunks)
        system_prompt = """你是一个专业的教学分析助手。请根据提供的参考资料回答用户的问题。

要求：
1. 回答要基于参考资料，不要编造内容
2. 如果参考资料不足以回答问题，请明确说明"参考资料中未提供此信息"
3. 回答要简洁、专业、有针对性
4. 可以引用参考资料的来源
5. 参考资料是检索得到的辅助线索，不可作为绝对事实依据"""
        prompt = f"""参考资料：
{context}

用户问题：{question}

请根据以上参考资料回答用户的问题。"""

        yield from self._stream_llm(system_prompt, prompt)

    def _stream_llm(self, system_prompt: str, user_content: str):
        """流式调用 LLM，yield 事件字典"""
        llm = get_llm("deep")
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]
        full = ""
        try:
            for chunk in llm.stream(messages, max_tokens=512, think=False, temperature=0.7):
                if chunk["done"]:
                    break
                content = chunk.get("content", "")
                if not content:
                    continue
                full += content
                yield {'type': 'delta', 'delta': content}
        except LLMError as e:
            yield {'type': 'error', 'error': str(e)}
            return
        except Exception as e:
            yield {'type': 'error', 'error': str(e)}
            return
        full = _strip_think_tags(full)
        yield {'type': 'done', 'content': full}

    def add_knowledge(self, chunks, source: str, document_id: int = None):
        """添加知识到索引（FAISS Dense + BM25 Sparse 双索引同步）

        Args:
            chunks: List[str] 或 List[dict]（dict 含 content/page 字段，用于保留 PDF 页码元数据）
            source: 来源标识（如文件名）
            document_id: 所属文档 ID
        """
        # 统一为 List[dict] 格式
        normalized = []
        for c in chunks:
            if isinstance(c, dict):
                normalized.append({
                    'content': c.get('content', ''),
                    'page': c.get('page'),
                })
            else:
                normalized.append({'content': str(c), 'page': None})

        contents = [c['content'] for c in normalized]
        metadata = [
            {
                'content': c['content'],
                'source': source,
                'document_id': document_id,
                'page': c['page'],
            }
            for c in normalized
        ]
        self.embedding_service.add_chunks(contents, metadata)
        self.bm25_service.add_chunks(contents, metadata)

    def add_knowledge_parent_child(
        self,
        parents: list,
        children: list,
        source: str,
        document_id: int = None,
    ):
        """添加父子分块知识（子分块进 FAISS + BM25，父分块进 parent_store）

        Args:
            parents: [{'content': str, 'index': int}, ...]
            children: [{'content': str, 'parent_index': int, 'page': int|None}, ...]
            source: 来源标识（如文件名）
            document_id: 所属文档 ID
        """
        child_contents = [c['content'] for c in children]
        child_metadata = [
            {
                'content': c['content'],
                'source': source,
                'document_id': document_id,
                'page': c.get('page'),
                'parent_index': c['parent_index'],
            }
            for c in children
        ]
        parent_contents = [p['content'] for p in parents]

        # 子分块进 FAISS + parent_store
        self.embedding_service.add_parent_child_chunks(
            child_contents, child_metadata, parent_contents
        )
        # BM25 也索引子分块（用于 Sparse 检索）
        bm25_metadata = [
            {
                'content': c['content'],
                'source': source,
                'document_id': document_id,
                'page': c.get('page'),
            }
            for c in children
        ]
        self.bm25_service.add_chunks(child_contents, bm25_metadata)

    def remove_document(self, document_id: int) -> int:
        """软删除指定文档的所有向量（FAISS + BM25 双索引同步）"""
        removed = self.embedding_service.remove_by_document(document_id)
        self.bm25_service.remove_by_document(document_id)
        return removed

    def rebuild_index(self, db_session) -> dict:
        """从数据库重建索引（FAISS + BM25 双索引同步，保留页码元数据）"""
        result = self.embedding_service.rebuild_from_db(db_session)
        # 同步重建 BM25 索引：从 embedding_service 的 metadata 读取全量 chunk
        all_chunks = [m.get('content', '') for m in self.embedding_service.chunk_metadata]
        all_metadata = [
            {
                'content': m.get('content', ''),
                'source': m.get('source', ''),
                'document_id': m.get('document_id'),
                'page': m.get('page'),
                'chunk_index': m.get('chunk_index', i),
                'is_deleted': m.get('is_deleted', False),
            }
            for i, m in enumerate(self.embedding_service.chunk_metadata)
        ]
        # 过滤已软删除的 chunk
        active_chunks = [c for c, m in zip(all_chunks, all_metadata) if not m.get('is_deleted')]
        active_metadata = [m for m in all_metadata if not m.get('is_deleted')]
        self.bm25_service.rebuild_from_chunks(active_chunks, active_metadata)
        result['bm25_chunks'] = len(active_chunks)
        return result

    def get_status(self) -> dict:
        """获取RAG状态（Dense + Sparse + Reranker + Router + HyDE）"""
        dense_status = self.embedding_service.get_index_status()
        sparse_status = self.bm25_service.get_status()
        reranker_status = {
            'enabled': settings.RAG_RERANKER_ENABLED,
            'model': settings.RAG_RERANKER_MODEL if settings.RAG_RERANKER_ENABLED else None,
            'loaded': self._reranker is not None and self._reranker._model is not None,
        }
        return {
            **dense_status,
            'bm25_active': sparse_status['active'],
            'bm25_chunks': sparse_status['total_chunks'],
            'reranker': reranker_status,
            'query_router_enabled': settings.RAG_QUERY_ROUTER_ENABLED,
            'hyde_enabled': settings.RAG_HYDE_ENABLED,
            'multi_query_enabled': settings.RAG_MULTI_QUERY_ENABLED,
            'multi_query_count': settings.RAG_MULTI_QUERY_COUNT,
            'chunk_by_tokens': settings.RAG_CHUNK_BY_TOKENS,
            'chunk_size': settings.RAG_CHUNK_SIZE,
            'chunk_overlap': settings.RAG_CHUNK_OVERLAP,
            'chunk_strategy': settings.RAG_CHUNK_STRATEGY,
            'parent_child_enabled': settings.RAG_PARENT_CHILD_ENABLED,
            'parent_chunk_size': settings.RAG_PARENT_CHUNK_SIZE if settings.RAG_PARENT_CHILD_ENABLED else None,
            'child_chunk_size': settings.RAG_CHILD_CHUNK_SIZE if settings.RAG_PARENT_CHILD_ENABLED else None,
        }
