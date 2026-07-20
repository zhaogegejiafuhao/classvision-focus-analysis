"""测试 HyDE + Multi-Query 启用后的延迟"""
import time
import requests

TOKEN = open(r"C:\Users\15534\AppData\Local\Temp\cv_token.txt", encoding="utf-8-sig").read().strip()
BASE = "http://localhost:8000"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json; charset=utf-8",
}

def rag_query(question):
    t0 = time.time()
    resp = requests.post(
        f"{BASE}/api/rag/query",
        headers=headers,
        json={"question": question, "top_k": 5},
        timeout=300,
    )
    elapsed = time.time() - t0
    resp.raise_for_status()
    data = resp.json()
    answer = data.get("answer", "")
    sources = data.get("sources", [])
    return elapsed, answer, sources

print("=== HyDE + Multi-Query 启用后延迟测试 ===")
questions = [
    "注意力检测",                    # 5字 - HyDE only
    "课堂注意力分析的方法有哪些",     # 13字 - Multi-Query
    "如何检测学生的注意力是否集中",   # 14字 - Multi-Query
]

for q in questions:
    print(f"Testing: {q} ({len(q)}字)...")
    elapsed, answer, sources = rag_query(q)
    print(f"  耗时: {elapsed:.1f}s | 回答长度: {len(answer)} chars | sources: {len(sources)}")
    print(f"  回答: {answer[:150]}")
    print()