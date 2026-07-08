"""RAG检索服务：检索 + 生成回答"""

import json
import requests
from typing import List, Optional

from backend.core.config import settings
from rag.embedding_service import EmbeddingService


class RAGService:
    """RAG服务"""

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.ollama_host = settings.OLLAMA_HOST
        self.ollama_model = settings.OLLAMA_MODEL
        self.top_k = settings.RAG_TOP_K
        self._query_cache = {}  # 问题归一化 -> {content, sources, retrieved_chunks}

    def query(self, question: str, top_k: int = None) -> dict:
        """检索并生成回答"""
        if top_k is None:
            top_k = self.top_k

        # 检索相关内容
        retrieved_chunks = self.embedding_service.search(question, top_k)

        if not retrieved_chunks:
            return {
                'answer': '知识库中没有找到相关内容。',
                'sources': [],
                'retrieved_chunks': [],
            }

        # 构建上下文
        context = self._build_context(retrieved_chunks)

        # 调用Ollama生成回答
        answer = self._generate_answer(question, context)

        return {
            'answer': answer,
            'sources': [r['source'] for r in retrieved_chunks],
            'retrieved_chunks': retrieved_chunks,
        }

    def _build_context(self, chunks: List[dict]) -> str:
        """构建上下文"""
        context_parts = []
        for i, chunk in enumerate(chunks):
            context_parts.append(f"[参考{i + 1}] {chunk['content']}")
        return "\n\n".join(context_parts)

    def _generate_answer(self, question: str, context: str) -> str:
        """调用Ollama生成回答"""
        system_prompt = """你是一个专业的教学分析助手。请根据提供的参考资料回答用户的问题。

要求：
1. 回答要基于参考资料，不要编造内容
2. 如果参考资料不足以回答问题，请明确说明
3. 回答要简洁、专业、有针对性
4. 可以引用参考资料的来源"""

        prompt = f"""参考资料：
{context}

用户问题：{question}

请根据以上参考资料回答用户的问题。"""

        url = f"{self.ollama_host}/api/chat"
        payload = {
            "model": self.ollama_model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
        }

        try:
            resp = requests.post(url, json=payload, timeout=120)
            resp.raise_for_status()
            return resp.json()["message"]["content"]
        except Exception as e:
            return f"生成回答失败: {e}"

    def stream_query(self, question: str, top_k: int = None):
        """流式检索并生成回答，yield 事件字典。

        事件类型：
        - meta: 检索完成，带 sources / retrieved_chunks
        - delta: 文本增量
        - done: 流结束，带完整 content
        - error: 出错
        """
        if top_k is None:
            top_k = self.top_k

        # 缓存命中检查
        cache_key = question.strip().lower()
        if cache_key in self._query_cache:
            cached = self._query_cache[cache_key]
            yield {'type': 'meta', 'sources': cached['sources'], 'retrieved_chunks': cached['retrieved_chunks']}
            yield {'type': 'delta', 'delta': cached['content']}
            yield {'type': 'done', 'content': cached['content'], 'cached': True}
            return

        retrieved_chunks = self.embedding_service.search(question, top_k)
        sources = [r['source'] for r in retrieved_chunks]

        if not retrieved_chunks:
            yield {'type': 'meta', 'sources': [], 'retrieved_chunks': []}
            yield {'type': 'done', 'content': '知识库中没有找到相关内容。'}
            return

        # 先发检索元信息，前端可立即展示参考来源
        yield {'type': 'meta', 'sources': sources, 'retrieved_chunks': retrieved_chunks}

        context = self._build_context(retrieved_chunks)
        system_prompt = """你是一个专业的教学分析助手。请根据提供的参考资料回答用户的问题。

要求：
1. 回答要基于参考资料，不要编造内容
2. 如果参考资料不足以回答问题，请明确说明
3. 回答要简洁、专业、有针对性
4. 可以引用参考资料的来源"""
        prompt = f"""参考资料：
{context}

用户问题：{question}

请根据以上参考资料回答用户的问题。"""

        url = f"{self.ollama_host}/api/chat"
        payload = {
            "model": self.ollama_model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            "stream": True,
        }

        full = ""
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
                        full += delta
                        yield {'type': 'delta', 'delta': delta}
        except Exception as e:
            if isinstance(e, requests.exceptions.ConnectionError):
                err_msg = "Ollama 服务未启动，请先运行 ollama serve 并拉取模型（ollama pull qwen3:4b）"
            else:
                err_msg = str(e)
            yield {'type': 'error', 'error': err_msg}
            return

        # 存入缓存（上限 50 条，超出删最早）
        if len(self._query_cache) >= 50:
            self._query_cache.pop(next(iter(self._query_cache)))
        self._query_cache[cache_key] = {
            'content': full,
            'sources': sources,
            'retrieved_chunks': retrieved_chunks,
        }
        yield {'type': 'done', 'content': full}

    def add_knowledge(self, chunks: List[str], source: str, document_id: int = None):
        """添加知识到索引"""
        metadata = [
            {'content': chunk, 'source': source, 'document_id': document_id}
            for chunk in chunks
        ]
        self.embedding_service.add_chunks(chunks, metadata)
        self._query_cache.clear()

    def remove_document(self, document_id: int) -> int:
        """软删除指定文档的所有向量"""
        removed = self.embedding_service.remove_by_document(document_id)
        self._query_cache.clear()
        return removed

    def rebuild_index(self, db_session) -> dict:
        """从数据库重建索引"""
        result = self.embedding_service.rebuild_from_db(db_session)
        self._query_cache.clear()
        return result

    def get_status(self) -> dict:
        """获取RAG状态"""
        return self.embedding_service.get_index_status()