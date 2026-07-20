"""异步LLM适配层

将 ClassVision 的同步 LLMProvider.chat() 包装为异步调用，
供 ZhiReviewPi 迁移的 grader/model_router 等异步服务使用。
"""
import asyncio
import logging
from typing import Optional

from backend.services.llm_client import get_llm, LLMProvider, LLMError
from backend.services.llm_utils import parse_llm_json

logger = logging.getLogger(__name__)


async def async_chat(
    messages: list[dict],
    model: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: int = 2048,
    mode: str = "deep",
) -> dict:
    """异步包装 LLMProvider.chat()

    Args:
        messages: OpenAI格式的消息列表
        model: 指定模型名（None则使用默认）
        temperature: 温度
        max_tokens: 最大token数
        mode: "deep"使用主模型, "fast"使用快速模型

    Returns:
        dict: {"content": str, "thinking": str | None}
    """
    llm = get_llm(mode=mode)
    return await asyncio.to_thread(
        llm.chat, messages, model, temperature, max_tokens, False
    )


async def async_chat_json(
    messages: list[dict],
    model: Optional[str] = None,
    temperature: float = 0.1,
    max_tokens: int = 2048,
    mode: str = "deep",
    fallback: Optional[dict] = None,
) -> dict:
    """异步调用LLM并自动解析JSON输出

    Args:
        messages: OpenAI格式的消息列表
        model: 指定模型名
        temperature: 温度（默认0.1，适合结构化输出）
        max_tokens: 最大token数
        mode: "deep"或"fast"
        fallback: JSON解析失败时的默认返回值

    Returns:
        dict: 解析后的JSON字典
    """
    result = await async_chat(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        mode=mode,
    )
    content = result.get("content", "")
    parsed = parse_llm_json(content, fallback=fallback)
    if not parsed or (not parsed.get("steps") and not parsed.get("error_cause") and not parsed.get("questions")):
        logger.warning(f"[async_chat_json] LLM JSON解析结果为空或不完整, 原文前200字: {content[:200]}")
    return parsed


async def async_chat_with_provider(
    provider_name: str,
    messages: list[dict],
    api_key: str,
    base_url: str,
    model: str,
    temperature: float = 0.1,
    max_tokens: int = 2048,
) -> dict:
    """使用指定Provider异步调用（用于多模态VL等特殊场景）

    Args:
        provider_name: Provider名称（仅用于日志）
        messages: 消息列表
        api_key: API密钥
        base_url: API基础URL
        model: 模型名
        temperature: 温度
        max_tokens: 最大token数

    Returns:
        dict: {"content": str, "thinking": str | None}
    """
    from backend.services.llm_client import OpenAICompatProvider

    provider = OpenAICompatProvider(
        base_url=base_url,
        api_key=api_key,
        model=model,
    )
    return await asyncio.to_thread(
        provider.chat, messages, None, temperature, max_tokens, False
    )


async def async_chat_json_with_provider(
    provider_name: str,
    messages: list[dict],
    api_key: str,
    base_url: str,
    model: str,
    temperature: float = 0.1,
    max_tokens: int = 2048,
) -> dict:
    """使用指定Provider异步调用并解析JSON"""
    result = await async_chat_with_provider(
        provider_name=provider_name,
        messages=messages,
        api_key=api_key,
        base_url=base_url,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    content = result.get("content", "")
    return parse_llm_json(content)
