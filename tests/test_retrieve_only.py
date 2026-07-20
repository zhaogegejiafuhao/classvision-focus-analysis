"""直接测试 RAGService.retrieve_only，排查 chat 端点中 RAG 是否工作"""
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")

from rag.rag_service import RAGService

svc = RAGService()

questions = [
    "注意力检测的方法有哪些",
    "为什么疲劳人次这么高",
]

for mode in ["fast", "deep"]:
    for q in questions:
        print(f"\n=== mode={mode} | question={q!r} ===")
        t0 = time.time()
        try:
            result = svc.retrieve_only(q, top_k=3, mode=mode)
            elapsed = time.time() - t0
            chunks = result.get("retrieved_chunks", [])
            print(f"  耗时: {elapsed:.1f}s | chunks: {len(chunks)} | tier: {result.get('route_tier', 'N/A')}")
            for i, c in enumerate(chunks, 1):
                score = c.get("rerank_score", c.get("score", c.get("rrf_score", 0)))
                print(f"    [{i}] score={score:.4f} source={c.get('source', '')} content={c.get('content', '')[:80]}")
        except Exception as e:
            elapsed = time.time() - t0
            print(f"  失败 ({elapsed:.1f}s): {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
