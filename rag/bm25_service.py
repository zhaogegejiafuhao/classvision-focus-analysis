"""BM25 稀疏检索服务：jieba 分词 + BM25 算法"""

import logging
import pickle
import os
from typing import List, Optional

import jieba
from rank_bm25 import BM25Okapi

logger = logging.getLogger("rag")


class BM25Service:
    """BM25 稀疏检索，与 FAISS Dense 检索并行，结果通过 RRF 融合"""

    def __init__(self, index_dir: str):
        self.index_dir = index_dir
        self.bm25: Optional[BM25Okapi] = None
        self.corpus_chunks: List[str] = []  # 与 BM25 索引一一对应的原始文本
        self.corpus_metadata: List[dict] = []  # 与 FAISS chunk_metadata 对齐
        self._load_index()

    def _tokenize(self, text: str) -> List[str]:
        """jieba 中文分词，过滤空白和单字符标点"""
        tokens = [t.strip() for t in jieba.cut(text) if t.strip() and len(t.strip()) > 1]
        return tokens

    def _index_path(self):
        return os.path.join(self.index_dir, "bm25_index.pkl")

    def _load_index(self):
        """加载已有的 BM25 索引"""
        path = self._index_path()
        if os.path.exists(path):
            try:
                with open(path, 'rb') as f:
                    data = pickle.load(f)
                self.bm25 = data['bm25']
                self.corpus_chunks = data['corpus_chunks']
                self.corpus_metadata = data['corpus_metadata']
                logger.info("bm25_loaded chunks=%d", len(self.corpus_chunks))
            except Exception as e:
                logger.warning("bm25_load_failed error=%s", e)
                self.bm25 = None
                self.corpus_chunks = []
                self.corpus_metadata = []

    def _save_index(self):
        """保存 BM25 索引到磁盘"""
        path = self._index_path()
        with open(path, 'wb') as f:
            pickle.dump({
                'bm25': self.bm25,
                'corpus_chunks': self.corpus_chunks,
                'corpus_metadata': self.corpus_metadata,
            }, f)

    def add_chunks(self, chunks: List[str], metadata: List[dict]):
        """添加文本块到 BM25 索引（增量追加后重建）"""
        if not chunks:
            return
        self.corpus_chunks.extend(chunks)
        self.corpus_metadata.extend(metadata)
        # BM25 不支持增量更新，需全量重建
        tokenized_corpus = [self._tokenize(c) for c in self.corpus_chunks]
        self.bm25 = BM25Okapi(tokenized_corpus)
        self._save_index()
        logger.info("bm25_added new=%d total=%d", len(chunks), len(self.corpus_chunks))

    def search(self, query: str, top_k: int = 50) -> List[dict]:
        """检索相似文本，返回 top_k 结果（按 BM25 分数降序）"""
        if not self.bm25 or not self.corpus_chunks:
            return []
        tokenized_query = self._tokenize(query)
        if not tokenized_query:
            return []
        scores = self.bm25.get_scores(tokenized_query)
        # 取 top_k
        ranked_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        results = []
        for rank, idx in enumerate(ranked_indices):
            if scores[idx] <= 0:
                continue
            meta = self.corpus_metadata[idx] if idx < len(self.corpus_metadata) else {}
            results.append({
                'content': self.corpus_chunks[idx],
                'score': float(scores[idx]),
                'source': meta.get('source', ''),
                'chunk_id': meta.get('chunk_index', idx),
                'document_id': meta.get('document_id'),
                'page': meta.get('page'),
                'rank': rank,
            })
        return results

    def remove_by_document(self, document_id: int) -> int:
        """软删除指定文档的所有 chunk（标记 metadata）"""
        count = 0
        for meta in self.corpus_metadata:
            if meta.get('document_id') == document_id and not meta.get('is_deleted'):
                meta['is_deleted'] = True
                count += 1
        if count > 0:
            self._save_index()
        return count

    def rebuild_from_chunks(self, chunks: List[str], metadata: List[dict]):
        """从全量 chunk 重建 BM25 索引"""
        self.corpus_chunks = list(chunks)
        self.corpus_metadata = list(metadata)
        tokenized_corpus = [self._tokenize(c) for c in self.corpus_chunks]
        self.bm25 = BM25Okapi(tokenized_corpus) if tokenized_corpus else None
        self._save_index()
        logger.info("bm25_rebuilt total=%d", len(self.corpus_chunks))

    def get_status(self) -> dict:
        return {
            'total_chunks': len(self.corpus_chunks),
            'active': self.bm25 is not None,
        }
