"""几何题批改诊断脚本 - 分步计时，找出真正的瓶颈"""
import asyncio, time, sys
sys.path.insert(0, r"d:\ClassVision")

from backend.services.grader import grading_service, RubricGenerator, MathGrader
from backend.services.model_router import model_router
from backend.services.geometry_analyzer import is_geometry_question

QUESTION = """已知：在△ABC中，AB=AC，D是BC的中点，DE⊥AB于E，DF⊥AC于F。
求证：DE=DF"""
STANDARD_ANSWER = """证明：因为AB=AC，所以∠B=∠C（等边对等角）
因为D是BC的中点，所以BD=DC
又因为DE⊥AB，DF⊥AC，所以∠DEB=∠DFC=90°
在△BDE和△CDF中：∠B=∠C，∠DEB=∠DFC，BD=DC
所以△BDE≌△CDF（AAS）
所以DE=DF"""
STUDENT_ANSWER = """证明：因为AB=AC，所以∠B=∠C
因为D是BC的中点，所以BD=DC
又因为DE⊥AB，DF⊥AC，所以∠DEB=∠DFC=90°
在△BDE和△CDF中：∠B=∠C，∠DEB=∠DFC，BD=DC
所以△BDE≌△CDF
所以DE=DF"""

async def diagnose():
    print("=" * 60)
    print("几何题批改诊断")
    print("=" * 60)

    t0 = time.time()
    is_geo = is_geometry_question(QUESTION)
    print(f"\n[Step 0] 几何题检测: {is_geo}  耗时: {time.time()-t0:.2f}s")

    print(f"\n[Step 1] Rubric生成...")
    t1 = time.time()
    rubric_gen = RubricGenerator()
    rubric = await rubric_gen.generate(
        question=QUESTION,
        standard_answer=STANDARD_ANSWER,
        total_score=10,
    )
    t_rubric = time.time() - t1
    print(f"  耗时: {t_rubric:.1f}s")
    print(f"  Rubric步骤数: {len(rubric.get('steps', []))}")
    for i, s in enumerate(rubric.get("steps", [])):
        print(f"    step{i+1}: {s.get('description', '')[:50]} (score={s.get('score')})")

    print(f"\n[Step 2] 模型路由...")
    t2 = time.time()
    model_key = model_router.route(
        question=QUESTION,
        confidence=0.85,
        is_geometry=is_geo,
    )
    print(f"  耗时: {time.time()-t2:.2f}s")
    print(f"  路由结果: model_key={model_key}")

    print(f"\n[Step 3] LLM批改（含降级链）...")
    t3 = time.time()
    math_grader = MathGrader()
    grading_result = await math_grader.grade(
        question=QUESTION,
        standard_answer=STANDARD_ANSWER,
        student_answer=STUDENT_ANSWER,
        rubric=rubric,
        is_geometry=is_geo,
        confidence=0.85,
    )
    t_grade = time.time() - t3
    print(f"  耗时: {t_grade:.1f}s")
    print(f"  模型: {grading_result.get('_model_key')}")
    steps = grading_result.get("steps", [])
    print(f"  返回步骤数: {len(steps)}")
    for i, s in enumerate(steps):
        mark = "V" if s.get("correct") else "X"
        print(f"    [{mark}] step{i+1}: {s.get('content', '')[:50]} score={s.get('score')}")
    print(f"  error_cause: {grading_result.get('error_cause')}")
    print(f"  total_score: {grading_result.get('total_score')}")

    print(f"\n{'='*60}")
    print(f"总耗时分析:")
    print(f"  Rubric生成: {t_rubric:.1f}s")
    print(f"  LLM批改:    {t_grade:.1f}s")
    print(f"  总计:       {t_rubric + t_grade:.1f}s")
    print(f"{'='*60}")

if __name__ == "__main__":
    asyncio.run(diagnose())
