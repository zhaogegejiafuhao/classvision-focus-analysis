"""混合检索：Dense (FAISS) + Sparse (BM25) + RRF 融合"""

from typing import List, Dict


def rrf_fusion(
    dense_results: List[dict],
    sparse_results: List[dict],
    k: int = 60,
    top_k: int = 50,
) -> List[dict]:
    """Reciprocal Rank Fusion 融合两路检索结果

    公式: score(doc) = 1/(k + dense_rank) + 1/(k + sparse_rank)
    - 仅依赖排名，不依赖原始分数值域
    - k=60 是经验值，平衡头部和尾部权重
    """
    return rrf_fusion_multi([dense_results, sparse_results], k=k, top_k=top_k)


def rrf_fusion_multi(
    result_lists: List[List[dict]],
    k: int = 60,
    top_k: int = 50,
) -> List[dict]:
    """Reciprocal Rank Fusion 融合多路检索结果（支持 Multi-Query 场景）

    公式: score(doc) = sum over all lists of 1/(k + rank_in_list)
    - 每个列表中的文档按排名贡献 1/(k+rank) 分数
    - 同一文档在多个列表中出现则分数累加
    """
    scores: Dict[str, float] = {}
    chunk_map: Dict[str, dict] = {}

    for result_list in result_lists:
        for rank, r in enumerate(result_list):
            key = _chunk_key(r)
            if key not in scores:
                scores[key] = 0.0
                chunk_map[key] = r
            scores[key] += 1.0 / (k + rank)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
    result = []
    for rank, (key, score) in enumerate(ranked):
        item = dict(chunk_map[key])
        item['rrf_score'] = round(score, 6)
        item['rank'] = rank
        result.append(item)
    return result


def _chunk_key(chunk: dict) -> str:
    """生成 chunk 的唯一标识，用于跨检索器去重"""
    # 优先用 document_id + chunk_index
    doc_id = chunk.get('document_id')
    chunk_idx = chunk.get('chunk_id') or chunk.get('chunk_index')
    if doc_id is not None and chunk_idx is not None:
        return f"doc{doc_id}_chunk{chunk_idx}"
    # 退化为 content 前 100 字符
    content = chunk.get('content', '')
    return content[:100]
