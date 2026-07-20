"""测试 Phase 3: CPU 模式 Cross-Encoder 重排

验证：
1. bge-reranker-v2-m3 能在 CPU 上加载（首次需下载 ~2GB）
2. 重排延迟可接受（目标 < 2s for 50 candidates）
3. 重排后检索质量有改善
"""

import os
import sys
import time

# 设置环境变量
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# 添加项目根目录到 path
sys.path.insert(0, 'D:/ClassVision')

from rag.reranker_service import RerankerService
from rag.rag_service import RAGService


def test_reranker_directly():
    """直接测试 RerankerService"""
    print("\n=== 测试 1: 直接测试 RerankerService (CPU) ===")
    print("首次运行会下载 bge-reranker-v2-m3 (~2GB)，请耐心等待...")

    t0 = time.time()
    try:
        reranker = RerankerService(
            model_name="BAAI/bge-reranker-v2-m3",
            cache_dir="D:/models/sentence-transformers",
            device="cpu",
        )
        # 触发模型加载
        _ = reranker.model
        t_load = time.time() - t0
        print(f"模型加载耗时: {t_load:.1f}s")
        print(f"模型加载成功，device=cpu")
    except Exception as e:
        print(f"模型加载失败: {e}")
        return False

    # 构造测试数据
    query = "如何检测学生的注意力是否集中"
    candidates = [
        {'content': '注意力检测系统通过分析学生的头部姿态（pitch、yaw 角度）和眨眼频率来评估注意力水平。', 'source': 'doc1.pdf', 'score': 0.85},
        {'content': '课堂报告包含每个学生的平均注意力分数、低头次数、转头次数等指标。', 'source': 'doc2.pdf', 'score': 0.78},
        {'content': 'ClassVision 系统架构包括前端 Vue、后端 FastAPI、数据库 SQLite。', 'source': 'doc3.pdf', 'score': 0.72},
        {'content': '注意力检测算法使用 MediaPipe 提取面部关键点，计算 head pose 估计。', 'source': 'doc4.pdf', 'score': 0.88},
        {'content': 'Python 安装教程：从官网下载安装包，配置环境变量。', 'source': 'doc5.pdf', 'score': 0.65},
    ] * 10  # 扩展到 50 个候选

    print(f"\n测试重排: query={query!r}, candidates={len(candidates)}")

    t1 = time.time()
    result = reranker.rerank(query, candidates, top_k=3, max_candidates=50)
    t_rerank = time.time() - t1

    print(f"重排耗时: {t_rerank:.2f}s")
    print(f"重排结果 (top 3):")
    for i, item in enumerate(result):
        print(f"  [{i+1}] rerank_score={item.get('rerank_score', 0):.4f} source={item.get('source')} content={item['content'][:60]}...")

    return True


def test_rag_with_reranker():
    """测试完整 RAG 流程（含 reranker）"""
    print("\n=== 测试 2: 完整 RAG 查询（含 reranker）===")

    service = RAGService()

    queries = [
        "如何检测学生的注意力是否集中",
        "课堂注意力分析的方法有哪些",
        "注意力检测",
    ]

    for q in queries:
        print(f"\n--- Query: {q!r} ---")
        t0 = time.time()
        try:
            result = service.retrieve_only(q, top_k=3)
            t_total = time.time() - t0
            print(f"总延迟: {t_total:.1f}s")
            print(f"route_tier: {result.get('route_tier', 'unknown')}")
            chunks = result.get('retrieved_chunks', [])
            print(f"检索到 {len(chunks)} 个 chunk:")
            for i, c in enumerate(chunks):
                score = c.get('rerank_score', c.get('score', c.get('rrf_score', 0)))
                print(f"  [{i+1}] score={score:.4f} source={c.get('source')} content={c['content'][:60]}...")
        except Exception as e:
            print(f"查询失败: {e}")


if __name__ == "__main__":
    print("Phase 3 测试: CPU 模式 Cross-Encoder 重排")
    print("=" * 60)

    # 先测试 reranker 是否能加载
    if not test_reranker_directly():
        print("\nReranker 加载失败，请检查模型下载或依赖安装")
        sys.exit(1)

    # 测试完整 RAG 流程
    test_rag_with_reranker()

    print("\n" + "=" * 60)
    print("测试完成")
