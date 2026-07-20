"""测试 Layer 3 LLM 兜底几何检测"""
import asyncio, sys, time
sys.path.insert(0, r"d:\ClassVision")

from backend.services.geometry_analyzer import (
    is_geometry_question,
    has_geometry_ambiguous_hints,
    detect_geometry_with_llm_fallback,
)

# 测试用例：(题目, 期望Layer1+2结果, 期望最终结果, 描述)
TEST_CASES = [
    # Layer 1+2 应直接命中（零延迟）
    ("已知：在△ABC中，AB=AC，D是BC的中点，DE⊥AB于E，DF⊥AC于F。求证：DE=DF",
     True, True, "几何证明题(△+⊥+求证)"),
    ("证明：三角形ABC全等于三角形DEF",
     True, True, "关键词命中(三角形+全等)"),
    ("计算 15 + 27 * 2 - 18 / 3",
     False, False, "纯算术(无模糊词)"),

    # 模糊词触发 LLM 兜底
    ("如图，将一张纸片折叠后得到如下图形，求折痕长度",
     False, None, "模糊词(如图)触发LLM——几何题"),
    ("小明有5个苹果，吃了2个，还剩几个？",
     False, False, "应用题(无模糊词)直接False"),
    ("如图所示的电路图，求电流大小",
     False, None, "模糊词(如图)触发LLM——非几何题(物理)"),
]

async def main():
    print("=" * 70)
    print("三层几何检测测试")
    print("=" * 70)
    for q, exp_sync, exp_final, desc in TEST_CASES:
        t0 = time.time()
        sync_result = is_geometry_question(q)
        amb = has_geometry_ambiguous_hints(q)
        t1 = time.time()
        final = await detect_geometry_with_llm_fallback(q)
        t2 = time.time()

        sync_mark = "OK" if sync_result == exp_sync else "XX"
        final_mark = "OK" if exp_final is None or final == exp_final else "XX"

        print(f"\n[{sync_mark}{final_mark}] {desc}")
        print(f"    题目: {q[:50]}")
        print(f"    Layer1+2 同步: {sync_result} (耗时 {(t1-t0)*1000:.1f}ms)")
        print(f"    模糊词: {amb}")
        print(f"    Layer3 最终: {final} (总耗时 {(t2-t0)*1000:.0f}ms)")
        if exp_final is not None:
            print(f"    期望最终: {exp_final}")

if __name__ == "__main__":
    asyncio.run(main())
