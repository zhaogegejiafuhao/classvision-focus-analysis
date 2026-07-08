"""向量嵌入服务"""

import os
import ssl
import pickle
from typing import List, Optional

# 禁用SSL验证（解决HuggingFace下载证书问题）
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['SSL_CERT_FILE'] = ''
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'  # 使用镜像站点
ssl._create_default_https_context = ssl._create_unverified_context

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from backend.core.config import settings


class EmbeddingService:
    """向量嵌入与FAISS索引管理"""

    def __init__(self):
        self.model_name = settings.RAG_EMBEDDING_MODEL
        self.cache_dir = settings.RAG_CACHE_DIR
        self.index_dir = settings.RAG_INDEX_DIR
        self.dimension = 384  # MiniLM模型维度

        # 确保目录存在
        os.makedirs(self.index_dir, exist_ok=True)
        os.makedirs(self.cache_dir, exist_ok=True)

        # 懒加载模型
        self._model = None

        # FAISS索引
        self.index: Optional[faiss.IndexFlatIP] = None
        self.chunk_metadata: List[dict] = []  # 存储每个向量的元数据

        # 加载已有索引（不需要模型）
        self._load_index()

    @property
    def model(self):
        """懒加载嵌入模型"""
        if self._model is None:
            print(f"加载嵌入模型: {self.model_name}")
            self._model = SentenceTransformer(
                self.model_name,
                cache_folder=self.cache_dir
            )
        return self._model

    def _load_index(self):
        """加载已有的FAISS索引"""
        index_path = os.path.join(self.index_dir, "faiss_index.bin")
        metadata_path = os.path.join(self.index_dir, "chunk_metadata.pkl")

        if os.path.exists(index_path) and os.path.exists(metadata_path):
            try:
                self.index = faiss.read_index(index_path)
                with open(metadata_path, 'rb') as f:
                    self.chunk_metadata = pickle.load(f)
                print(f"已加载索引，共 {self.index.ntotal} 个向量")
            except Exception as e:
                print(f"加载索引失败: {e}")
                self._create_new_index()
        else:
            self._create_new_index()

    def _create_new_index(self):
        """创建新的FAISS索引"""
        self.index = faiss.IndexFlatIP(self.dimension)  # 内积相似度
        self.chunk_metadata = []

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        """将文本转换为向量"""
        embeddings = self.model.encode(texts, show_progress_bar=False)
        return np.array(embeddings, dtype=np.float32)

    def add_chunks(self, chunks: List[str], metadata: List[dict]):
        """添加文本块到索引"""
        if not chunks:
            return

        # 生成向量
        embeddings = self.embed_texts(chunks)

        # 归一化向量（用于内积相似度）
        faiss.normalize_L2(embeddings)

        # 添加到索引
        self.index.add(embeddings)

        # 保存元数据
        for i, meta in enumerate(metadata):
            meta['chunk_index'] = len(self.chunk_metadata) + i
            self.chunk_metadata.append(meta)

        # 保存索引到磁盘
        self._save_index()

    def search(self, query: str, top_k: int = 5) -> List[dict]:
        """检索相似文本（自动过滤已软删除的向量）"""
        if self.index.ntotal == 0:
            return []

        # 生成查询向量
        query_embedding = self.embed_texts([query])
        faiss.normalize_L2(query_embedding)

        # 多取一些以补偿已删除的向量
        fetch_k = min(top_k * 3, self.index.ntotal)
        distances, indices = self.index.search(query_embedding, fetch_k)

        results = []
        for i, idx in enumerate(indices[0]):
            if idx < 0 or idx >= len(self.chunk_metadata):
                continue
            meta = self.chunk_metadata[idx]
            if meta.get('is_deleted'):
                continue
            result = {
                'content': meta.get('content', ''),
                'score': float(distances[0][i]),
                'source': meta.get('source', ''),
                'chunk_id': int(idx),
            }
            results.append(result)
            if len(results) >= top_k:
                break

        return results

    def remove_by_document(self, document_id: int) -> int:
        """软删除指定文档的所有向量（标记 metadata），返回删除数量。

        FAISS IndexFlatIP 不支持按 ID 删除，这里用软删除标记，
        检索时自动过滤。需要彻底清理时可调用 rebuild_from_db。
        """
        count = 0
        for meta in self.chunk_metadata:
            if meta.get('document_id') == document_id and not meta.get('is_deleted'):
                meta['is_deleted'] = True
                count += 1
        if count > 0:
            self._save_index()
        return count

    def rebuild_from_db(self, db_session) -> dict:
        """从原始文件重建索引：重新解析（应用最新 _clean_text）+ 补 document_id + 清理已删除向量。"""
        from backend.models.tables import KnowledgeDocument, KnowledgeChunk
        from rag.knowledge_base import get_knowledge_base
        kb = get_knowledge_base()
        self._create_new_index()
        docs = db_session.query(KnowledgeDocument).all()
        total = 0
        for doc in docs:
            chunks = None
            # 优先重新解析原始文件，应用最新的 _clean_text 规则
            if doc.file_path and os.path.exists(doc.file_path):
                chunks = kb.process_file(doc.file_path)
                # 同步更新 DB 中的 chunk 内容
                db_session.query(KnowledgeChunk).filter(
                    KnowledgeChunk.document_id == doc.id
                ).delete()
                for i, chunk in enumerate(chunks):
                    db_session.add(KnowledgeChunk(
                        document_id=doc.id,
                        chunk_index=i,
                        content=chunk,
                        embedding_stored=True,
                    ))
            # 文件不存在则用 DB 中已有的 chunk
            if not chunks:
                db_chunks = db_session.query(KnowledgeChunk).filter(
                    KnowledgeChunk.document_id == doc.id
                ).order_by(KnowledgeChunk.chunk_index).all()
                chunks = [c.content for c in db_chunks]
            if not chunks:
                continue
            metadata = [
                {'content': c, 'source': doc.filename, 'document_id': doc.id}
                for c in chunks
            ]
            self.add_chunks(chunks, metadata)
            total += len(chunks)
        db_session.commit()
        return {'documents': len(docs), 'chunks': total}

    def _save_index(self):
        """保存索引到磁盘"""
        index_path = os.path.join(self.index_dir, "faiss_index.bin")
        metadata_path = os.path.join(self.index_dir, "chunk_metadata.pkl")

        faiss.write_index(self.index, index_path)
        with open(metadata_path, 'wb') as f:
            pickle.dump(self.chunk_metadata, f)

    def get_index_status(self) -> dict:
        """获取索引状态"""
        return {
            'total_vectors': self.index.ntotal if self.index else 0,
            'dimension': self.dimension,
            'model': self.model_name,
            'index_dir': self.index_dir,
        }