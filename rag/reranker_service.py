"""Cross-Encoder 重排服务：bge-reranker-v2-m3 精排"""

import logging
import os
from typing import List, Optional

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'  # 使用镜像站点

logger = logging.getLogger("rag")


class RerankerService:
    """Cross-Encoder 重排：对混合检索 top50 候选精排，输出 top_k 给 LLM"""

    def __init__(
        self,
        model_name: str = "BAAI/bge-reranker-v2-m3",
        cache_dir: str = None,
        device: str = "cpu",
    ):
        self.model_name = model_name
        self.cache_dir = cache_dir
        # device='cpu' 避免与 qwen3:4b 争抢 4GB 显存导致 OOM
        # CPU 重排 50 候选约 0.5-2s，可接受
        self.device = device
        self._model = None

    @property
    def model(self):
        """懒加载 Cross-Encoder 模型（首次调用时加载，约 2GB）"""
        if self._model is None:
            try:
                from sentence_transformers import CrossEncoder
                logger.info("loading_reranker model=%s device=%s", self.model_name, self.device)
                self._model = CrossEncoder(
                    self.model_name,
                    max_length=512,
                    device=self.device,
                )
                logger.info("reranker_loaded device=%s", self.device)
            except Exception as e:
                logger.error("reranker_load_failed error=%s", e)
                raise
        return self._model

    def rerank(
        self,
        query: str,
        candidates: List[dict],
        top_k: int = 3,
        max_candidates: int = 50,
    ) -> List[dict]:
        """对候选 chunk 重排

        Args:
            query: 用户查询
            candidates: 混合检索输出的候选列表
            top_k: 重排后返回的数量
            max_candidates: 最大候选数量限制（Cross-Encoder O(N) 复杂度，超限截断）

        Returns:
            重排后的 top_k chunk 列表，每个 chunk 增加 'rerank_score' 字段
        """
        if not candidates:
            return []

        # 截断候选数量，防止 O(N) 推理耗时过长
        candidates = candidates[:max_candidates]

        try:
            # 构建 query-document pairs
            pairs = [(query, c.get('content', '')) for c in candidates]
            scores = self.model.predict(pairs, show_progress_bar=False)

            # 按重排分数降序
            scored = list(zip(candidates, scores))
            scored.sort(key=lambda x: x[1], reverse=True)

            result = []
            for rank, (chunk, score) in enumerate(scored[:top_k]):
                item = dict(chunk)
                item['rerank_score'] = float(score)
                item['rank'] = rank
                result.append(item)

            logger.info(
                "rerank_ok query=%r candidates=%d top_k=%d top_score=%.4f",
                query, len(candidates), len(result),
                result[0]['rerank_score'] if result else 0,
            )
            return result

        except Exception as e:
            logger.error("rerank_failed error=%s, falling back to original order", e)
            # 失败时回退到原始顺序
            return candidates[:top_k]

    def get_status(self) -> dict:
        return {
            'model': self.model_name,
            'loaded': self._model is not None,
        }
