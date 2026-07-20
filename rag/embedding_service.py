"""向量嵌入服务（支持父子分块双索引）

- 子分块索引：FAISS 索引，用于精准向量匹配
- 父分块存储：parent_store 字典，用于 LLM 上下文扩展
"""

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
    """向量嵌入与FAISS索引管理（支持父子分块）"""

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

        # FAISS索引（仅存子分块用于检索匹配）
        self.index: Optional[faiss.IndexFlatIP] = None
        self.chunk_metadata: List[dict] = []  # 存储每个向量的元数据

        # 父分块存储：{parent_id: content}，用于 LLM 上下文扩展
        self.parent_store: dict = {}
        self._next_parent_id: int = 1

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
        parent_store_path = os.path.join(self.index_dir, "parent_store.pkl")

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

        # 加载父分块存储
        if os.path.exists(parent_store_path):
            try:
                with open(parent_store_path, 'rb') as f:
                    data = pickle.load(f)
                    self.parent_store = data.get('store', {})
                    self._next_parent_id = data.get('next_id', 1)
                print(f"已加载父分块存储，共 {len(self.parent_store)} 条")
            except Exception as e:
                print(f"加载父分块存储失败: {e}")
                self.parent_store = {}
                self._next_parent_id = 1

    def _create_new_index(self):
        """创建新的FAISS索引"""
        self.index = faiss.IndexFlatIP(self.dimension)  # 内积相似度
        self.chunk_metadata = []

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        """将文本转换为向量"""
        embeddings = self.model.encode(texts, show_progress_bar=False)
        return np.array(embeddings, dtype=np.float32)

    # ============================================================
    #  索引写入
    # ============================================================

    def add_chunks(self, chunks: List[str], metadata: List[dict]):
        """添加文本块到索引（单层模式，向后兼容）"""
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

    def add_parent_child_chunks(
        self,
        child_contents: List[str],
        child_metadata: List[dict],
        parent_contents: List[str],
    ) -> List[int]:
        """添加父子分块：子分块进 FAISS 索引，父分块进 parent_store

        Args:
            child_contents: 子分块文本列表
            child_metadata: 子分块元数据列表（需含 parent_index 字段）
            parent_contents: 父分块文本列表（按 parent_index 顺序）

        Returns:
            parent_ids: 分配给每个父分块的 ID 列表（与 parent_contents 顺序对应）
        """
        if not child_contents:
            return []

        # 1. 存储父分块到 parent_store，分配 parent_id
        parent_ids = []
        for p_content in parent_contents:
            pid = self._next_parent_id
            self.parent_store[pid] = p_content
            parent_ids.append(pid)
            self._next_parent_id += 1

        # 2. 为子分块元数据添加 parent_id 映射
        for meta in child_metadata:
            p_idx = meta.get('parent_index', 0)
            if p_idx < len(parent_ids):
                meta['parent_id'] = parent_ids[p_idx]
            else:
                meta['parent_id'] = None

        # 3. 子分块进 FAISS 索引
        embeddings = self.embed_texts(child_contents)
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)

        for i, meta in enumerate(child_metadata):
            meta['chunk_index'] = len(self.chunk_metadata) + i
            meta['is_child'] = True
            self.chunk_metadata.append(meta)

        self._save_index()
        return parent_ids

    def get_parent_content(self, parent_id: int) -> Optional[str]:
        """根据 parent_id 获取父分块内容"""
        return self.parent_store.get(parent_id)

    # ============================================================
    #  检索
    # ============================================================

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
                'page': meta.get('page'),
                'document_id': meta.get('document_id'),
                'parent_id': meta.get('parent_id'),  # 父子分块：子分块指向父分块
            }
            results.append(result)
            if len(results) >= top_k:
                break

        return results

    # ============================================================
    #  删除与重建
    # ============================================================

    def remove_by_document(self, document_id: int) -> int:
        """软删除指定文档的所有向量（标记 metadata），返回删除数量。

        FAISS IndexFlatIP 不支持按 ID 删除，这里用软删除标记，
        检索时自动过滤。需要彻底清理时可调用 rebuild_from_db。
        """
        count = 0
        parent_ids_to_remove = set()
        for meta in self.chunk_metadata:
            if meta.get('document_id') == document_id and not meta.get('is_deleted'):
                meta['is_deleted'] = True
                count += 1
                # 收集需要删除的 parent_id
                pid = meta.get('parent_id')
                if pid is not None:
                    parent_ids_to_remove.add(pid)
        # 清理 parent_store 中对应条目
        for pid in parent_ids_to_remove:
            self.parent_store.pop(pid, None)
        if count > 0:
            self._save_index()
        return count

    def rebuild_from_db(self, db_session) -> dict:
        """从原始文件重建索引：重新解析（应用最新分块策略 + 保留页码元数据 + 父子分块）。"""
        from backend.models.tables import KnowledgeDocument, KnowledgeChunk
        from rag.knowledge_base import get_knowledge_base
        kb = get_knowledge_base()
        self._create_new_index()
        self.parent_store = {}
        self._next_parent_id = 1

        docs = db_session.query(KnowledgeDocument).all()
        total_parents = 0
        total_children = 0

        for doc in docs:
            # 优先重新解析原始文件
            if doc.file_path and os.path.exists(doc.file_path):
                if settings.RAG_PARENT_CHILD_ENABLED:
                    # 父子分块模式
                    ext = os.path.splitext(doc.file_path)[1].lower()
                    full_text = None
                    if ext == '.pdf':
                        full_text = kb.parse_pdf(doc.file_path)
                    elif ext == '.txt':
                        full_text = kb.parse_txt(doc.file_path)
                    elif ext == '.md':
                        full_text = kb.parse_md(doc.file_path)
                    elif ext == '.docx':
                        full_text = kb.parse_docx(doc.file_path)
                    elif ext == '.pptx':
                        full_text = kb.parse_pptx(doc.file_path)

                    if full_text:
                        result = kb.split_into_parent_child(full_text)
                        parents = result['parents']
                        children = result['children']

                        # 存入数据库
                        db_session.query(KnowledgeChunk).filter(
                            KnowledgeChunk.document_id == doc.id
                        ).delete()

                        # 先存父分块，拿到 DB id
                        parent_db_ids = []
                        for p_idx, parent in enumerate(parents):
                            parent_record = KnowledgeChunk(
                                document_id=doc.id,
                                chunk_index=p_idx,
                                content=parent['content'],
                                embedding_stored=False,  # 父分块不进 FAISS
                                is_parent=True,
                            )
                            db_session.add(parent_record)
                            db_session.flush()
                            parent_db_ids.append(parent_record.id)

                        # 再存子分块
                        for c_idx, child in enumerate(children):
                            p_idx = child['parent_index']
                            parent_db_id = parent_db_ids[p_idx] if p_idx < len(parent_db_ids) else None
                            db_session.add(KnowledgeChunk(
                                document_id=doc.id,
                                chunk_index=len(parents) + c_idx,
                                content=child['content'],
                                embedding_stored=True,
                                is_parent=False,
                                parent_chunk_id=parent_db_id,
                            ))

                        # 子分块进 FAISS
                        child_contents = [c['content'] for c in children]
                        child_metadata = [
                            {
                                'content': c['content'],
                                'source': doc.filename,
                                'document_id': doc.id,
                                'page': c.get('page'),
                                'parent_index': c['parent_index'],
                            }
                            for c in children
                        ]
                        parent_contents = [p['content'] for p in parents]
                        self.add_parent_child_chunks(child_contents, child_metadata, parent_contents)

                        total_parents += len(parents)
                        total_children += len(children)
                    else:
                        # 文件解析失败，跳过
                        continue
                else:
                    # 单层分块模式
                    chunks_meta = kb.process_file_with_metadata(doc.file_path)
                    db_session.query(KnowledgeChunk).filter(
                        KnowledgeChunk.document_id == doc.id
                    ).delete()
                    for i, chunk in enumerate(chunks_meta):
                        db_session.add(KnowledgeChunk(
                            document_id=doc.id,
                            chunk_index=i,
                            content=chunk['content'],
                            embedding_stored=True,
                        ))
                    if not chunks_meta:
                        continue
                    contents = [c['content'] for c in chunks_meta]
                    metadata = [
                        {
                            'content': c['content'],
                            'source': doc.filename,
                            'document_id': doc.id,
                            'page': c.get('page'),
                        }
                        for c in chunks_meta
                    ]
                    self.add_chunks(contents, metadata)
                    total_children += len(chunks_meta)
            else:
                # 文件不存在，从 DB 中的 chunk 恢复
                db_chunks = db_session.query(KnowledgeChunk).filter(
                    KnowledgeChunk.document_id == doc.id
                ).order_by(KnowledgeChunk.chunk_index).all()
                if not db_chunks:
                    continue

                # 检查是否有父子分块
                parent_chunks = [c for c in db_chunks if c.is_parent]
                child_chunks = [c for c in db_chunks if not c.is_parent]

                if parent_chunks and child_chunks:
                    # 父子分块模式：从 DB 恢复
                    parent_contents = [c.content for c in parent_chunks]
                    parent_db_ids = {c.chunk_index: c.id for c in parent_chunks}

                    child_contents = [c.content for c in child_chunks]
                    child_metadata = []
                    for c in child_chunks:
                        # 找到该子分块对应的父分块索引
                        p_idx = 0
                        if c.parent_chunk_id:
                            for pi, pc in enumerate(parent_chunks):
                                if pc.id == c.parent_chunk_id:
                                    p_idx = pi
                                    break
                        child_metadata.append({
                            'content': c.content,
                            'source': doc.filename,
                            'document_id': doc.id,
                            'page': None,
                            'parent_index': p_idx,
                        })

                    self.add_parent_child_chunks(child_contents, child_metadata, parent_contents)
                    total_parents += len(parent_chunks)
                    total_children += len(child_chunks)
                else:
                    # 单层模式
                    chunks_meta = [{'content': c.content, 'page': None} for c in db_chunks]
                    contents = [c['content'] for c in chunks_meta]
                    metadata = [
                        {
                            'content': c['content'],
                            'source': doc.filename,
                            'document_id': doc.id,
                            'page': None,
                        }
                        for c in chunks_meta
                    ]
                    self.add_chunks(contents, metadata)
                    total_children += len(chunks_meta)

        db_session.commit()
        return {
            'documents': len(docs),
            'chunks': total_children,
            'parent_chunks': total_parents,
            'parent_store_size': len(self.parent_store),
        }

    # ============================================================
    #  持久化
    # ============================================================

    def _save_index(self):
        """保存索引到磁盘"""
        index_path = os.path.join(self.index_dir, "faiss_index.bin")
        metadata_path = os.path.join(self.index_dir, "chunk_metadata.pkl")
        parent_store_path = os.path.join(self.index_dir, "parent_store.pkl")

        faiss.write_index(self.index, index_path)
        with open(metadata_path, 'wb') as f:
            pickle.dump(self.chunk_metadata, f)
        with open(parent_store_path, 'wb') as f:
            pickle.dump({
                'store': self.parent_store,
                'next_id': self._next_parent_id,
            }, f)

    def get_index_status(self) -> dict:
        """获取索引状态"""
        return {
            'total_vectors': self.index.ntotal if self.index else 0,
            'dimension': self.dimension,
            'model': self.model_name,
            'index_dir': self.index_dir,
            'parent_child_enabled': settings.RAG_PARENT_CHILD_ENABLED,
            'parent_store_size': len(self.parent_store),
        }
