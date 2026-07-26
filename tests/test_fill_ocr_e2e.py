"""填空题 OCR 批改整合 - 真实端到端验证

不 mock OCR，真实调用 PaddleOCR 跑完整链路：
1. 用 PIL 生成含文字的图片（模拟填空题学生答案）
2. 调 ocr_service.recognize() 真实识别
3. 调 _grade_fill_question() 真实判分
4. 输出每步结果

验证目标：
- PaddleOCR 单引擎模式下 OCR 能跑通
- _grade_fill_question 全链路无 bug
- 规范化 + 精确匹配 + 模糊匹配逻辑符合预期
"""
import asyncio
import sys
import os
import io

# Windows 控制台 UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


def make_text_image(text: str, size=(400, 120), font_size=48) -> bytes:
    """用 PIL 生成含文字的图片（模拟填空题学生答案区域）"""
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new("RGB", size, color="white")
    draw = ImageDraw.Draw(img)

    # 尝试加载字体
    font = None
    font_candidates = [
        "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\consola.ttf",
        "C:\\Windows\\Fonts\\msyh.ttc",
    ]
    for fp in font_candidates:
        if os.path.exists(fp):
            try:
                font = ImageFont.truetype(fp, font_size)
                break
            except Exception:
                continue
    if font is None:
        font = ImageFont.load_default()

    # 居中绘制文字
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size[0] - tw) // 2 - bbox[0]
    y = (size[1] - th) // 2 - bbox[1]
    draw.text((x, y), text, fill="black", font=font)

    # 编码为 PNG
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def make_mock_question(answer: str, score: float = 5.0, content: str = "解方程"):
    """构造 mock Question"""
    from unittest.mock import MagicMock
    q = MagicMock()
    q.id = 9001
    q.type = "fill"
    q.content = content
    q.answer = answer
    q.score = score
    return q


def make_region(image_bytes: bytes):
    """构造 mock QuestionRegionImage"""
    from backend.services.paper_template import QuestionRegionImage
    return QuestionRegionImage(
        question_id=9001,
        region_type="fill",
        image_bytes=image_bytes,
        bbox=(0, 0, 400, 120),
    )


async def run_case(case_name: str, student_text: str, standard_answer: str,
                   expected_correct: bool, score: float = 5.0):
    """跑单个测试用例"""
    from backend.services.ocr import ocr_service
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    print(f"\n--- 用例: {case_name} ---")
    print(f"  学生手写: {student_text!r}")
    print(f"  标准答案: {standard_answer!r}")

    # 1. 生成图片
    img_bytes = make_text_image(student_text)
    print(f"  [图片] 生成 {len(img_bytes)} bytes PNG")

    # 2. 真实 OCR 识别
    try:
        ocr_result = await ocr_service.recognize(img_bytes)
        print(f"  [OCR] 识别文本: {ocr_result.text!r}")
        print(f"  [OCR] 置信度:   {ocr_result.confidence:.3f}")
        print(f"  [OCR] 引擎:     {ocr_result.engines_used}")
        if ocr_result.needs_manual_input:
            print(f"  [OCR] ⚠️ 标记 needs_manual_input=True")
    except Exception as e:
        print(f"  [OCR] ❌ 异常: {type(e).__name__}: {e}")
        return False

    # 3. 真实判分
    question = make_mock_question(standard_answer, score=score)
    region = make_region(img_bytes)
    orchestrator = AnswerSheetOrchestrator()
    try:
        result = await orchestrator._grade_fill_question(question, region)
    except Exception as e:
        print(f"  [判分] ❌ 异常: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False

    print(f"  [判分] student_answer: {result.student_answer!r}")
    print(f"  [判分] score:           {result.score}/{result.max_score}")
    print(f"  [判分] is_correct:      {result.is_correct}")
    print(f"  [判分] confidence:      {result.confidence:.3f}")
    print(f"  [判分] comment:         {result.comment}")
    if result.grading_detail:
        print(f"  [判分] detail:          {result.grading_detail}")
    if result.error:
        print(f"  [判分] ❌ error:        {result.error}")

    # 4. 期望比对
    if result.is_correct == expected_correct:
        print(f"  ✅ 期望 is_correct={expected_correct}，实际一致")
        return True
    else:
        print(f"  ⚠️ 期望 is_correct={expected_correct}，实际={result.is_correct}（OCR 噪声属正常）")
        return False


async def main():
    print("=" * 60)
    print("填空题 OCR 端到端验证（真实 PaddleOCR）")
    print("=" * 60)

    # 检查 PaddleOCR 可用性
    from backend.services.ocr import PADDLEOCR_AVAILABLE
    print(f"\n[PaddleOCR 可用]: {PADDLEOCR_AVAILABLE}")
    if not PADDLEOCR_AVAILABLE:
        print("❌ PaddleOCR 不可用，无法继续端到端测试")
        return

    # 检查百度 OCR 配置
    from backend.core.config import settings
    print(f"[百度 OCR API_KEY]: {'已配置' if settings.BAIDU_OCR_API_KEY else '未配置（仅 PaddleOCR 单引擎）'}")

    # 设计用例（注意：印刷体 OCR 置信度会很高，主要验证流程）
    cases = [
        # (case_name, student_text, standard_answer, expected_correct, score)
        ("完美匹配-数字方程", "x=5", "x=5", True, 5.0),
        ("完美匹配-单词",     "hello", "hello", True, 5.0),
        ("大小写差异",        "Hello", "hello", True, 5.0),  # 规范化统一小写
        ("尾部句号",          "42.", "42", True, 5.0),       # 规范化去标点
        ("明显错误",          "x=6", "x=5", False, 5.0),
    ]

    pass_count = 0
    fail_count = 0
    for case in cases:
        ok = await run_case(*case)
        if ok:
            pass_count += 1
        else:
            fail_count += 1

    print("\n" + "=" * 60)
    print(f"端到端结果: 通过 {pass_count}/{pass_count + fail_count}")
    if fail_count > 0:
        print(f"⚠️ {fail_count} 个用例结果与预期不一致（可能是 OCR 识别偏差，需要看具体输出）")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
