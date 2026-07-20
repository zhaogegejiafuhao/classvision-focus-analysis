"""验证multimodal调用方式问题"""
import asyncio, sys
sys.path.insert(0, r"d:\ClassVision")

from backend.services import async_llm
from backend.core.config import settings

async def test():
    # 测试1: 模拟grader.py第537行的调用方式（错误的方式）
    print("=" * 60)
    print("测试1: 通过 async_chat_json 调用 multimodal (走SiliconFlow API)")
    print("=" * 60)
    print(f"  model={settings.DOUBAO_ENDPOINT_ID}")
    try:
        result = await async_llm.async_chat_json(
            messages=[{"role": "user", "content": '请回复JSON: {"test": true}'}],
            model=settings.DOUBAO_ENDPOINT_ID,
            temperature=0.1,
            max_tokens=100,
            mode="deep",
        )
        print("  成功:", result)
    except Exception as e:
        print(f"  失败: {type(e).__name__}: {e}")

    print()
    print("=" * 60)
    print("测试2: 通过 async_chat_with_provider 调用豆包 (走火山引擎API)")
    print("=" * 60)
    try:
        resp = await async_llm.async_chat_with_provider(
            provider_name="volcengine",
            messages=[{"role": "user", "content": '请回复JSON: {"test": true}'}],
            api_key=settings.VOLCENGINE_API_KEY,
            base_url=settings.VOLCENGINE_BASE_URL,
            model=settings.DOUBAO_ENDPOINT_ID,
            temperature=0.1,
            max_tokens=100,
        )
        print("  成功:", resp)
    except Exception as e:
        print(f"  失败: {type(e).__name__}: {e}")

asyncio.run(test())
