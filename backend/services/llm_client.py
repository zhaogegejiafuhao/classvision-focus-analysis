"""统一 LLM Provider 适配层

支持:
- Ollama（本地，/api/chat 协议）
- OpenAI 兼容 API（OpenRouter / DashScope / DeepSeek / 自定义，/chat/completions 协议）

所有调用方通过 get_llm() 获取 Provider 实例，无需关心底层协议差异。
"""

import json
import logging
import re
from abc import ABC, abstractmethod
from typing import Generator, Optional

import requests

from backend.core.config import settings

logger = logging.getLogger("llm")

# ── 预置厂商 Base URL ──────────────────────────────────────────
PROVIDER_BASE_URLS = {
    "ollama": "",
    "openrouter": "https://openrouter.ai/api/v1",
    "dashscope": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "deepseek": "https://api.deepseek.com/v1",
    "siliconflow": "https://api.siliconflow.cn/v1",
}


class LLMError(Exception):
    """LLM 调用统一异常"""
    pass


class LLMProvider(ABC):
    """LLM Provider 抽象基类"""

    @abstractmethod
    def chat(
        self,
        messages: list[dict],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        think: bool = False,
    ) -> dict:
        """同步调用 LLM

        Returns: {"content": str, "thinking": str | None}
        """
        ...

    @abstractmethod
    def stream(
        self,
        messages: list[dict],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        think: bool = False,
    ) -> Generator[dict, None, None]:
        """流式调用 LLM

        Yields: {"content": str, "thinking": str | None, "done": bool}
        """
        ...

    @abstractmethod
    def get_model(self, mode: str = "deep") -> str:
        """获取当前使用的模型名"""
        ...


class OllamaProvider(LLMProvider):
    """Ollama 本地模型 Provider（/api/chat 协议）"""

    def __init__(self, host: str, model: str, model_fast: str):
        self.host = host.rstrip("/")
        self.model = model
        self.model_fast = model_fast

    def get_model(self, mode: str = "deep") -> str:
        return self.model if mode == "deep" else self.model_fast

    def chat(
        self,
        messages: list[dict],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        think: bool = False,
    ) -> dict:
        url = f"{self.host}/api/chat"
        payload = {
            "model": model or self.model,
            "messages": messages,
            "stream": False,
            "think": think,
            "options": {"num_predict": max_tokens, "num_ctx": 4096, "temperature": temperature},
        }
        try:
            resp = requests.post(url, json=payload, timeout=300)
            resp.raise_for_status()
            data = resp.json()
            msg = data.get("message", {})
            content = msg.get("content", "")
            thinking = msg.get("thinking", None)
            # fallback: 如果 content 为空但 thinking 有内容
            if not content and thinking:
                content = thinking
                thinking = None
            return {"content": content, "thinking": thinking}
        except requests.exceptions.ConnectionError:
            raise LLMError("Ollama 服务未启动，请先运行 ollama serve 并拉取模型")
        except Exception as e:
            raise LLMError(f"Ollama 调用失败: {e}")

    def stream(
        self,
        messages: list[dict],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        think: bool = False,
    ) -> Generator[dict, None, None]:
        url = f"{self.host}/api/chat"
        payload = {
            "model": model or self.model,
            "messages": messages,
            "stream": True,
            "think": think,
            "options": {"num_predict": max_tokens, "num_ctx": 4096, "temperature": temperature},
        }
        try:
            with requests.post(url, json=payload, stream=True, timeout=300) as resp:
                resp.raise_for_status()
                for line in resp.iter_lines():
                    if not line:
                        continue
                    try:
                        data = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if data.get("done"):
                        yield {"content": "", "thinking": None, "done": True}
                        return
                    msg = data.get("message", {})
                    content = msg.get("content", "")
                    thinking = msg.get("thinking", None)
                    if content or thinking:
                        yield {"content": content, "thinking": thinking, "done": False}
        except requests.exceptions.ConnectionError:
            raise LLMError("Ollama 服务未启动，请先运行 ollama serve 并拉取模型")
        except Exception as e:
            raise LLMError(f"Ollama 流式调用失败: {e}")


class OpenAICompatProvider(LLMProvider):
    """OpenAI 兼容 API Provider（/chat/completions 协议）

    适用于: OpenRouter / DashScope / DeepSeek / SiliconFlow / 自定义端点
    """

    def __init__(self, base_url: str, api_key: str, model: str, model_fast: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.model = model
        self.model_fast = model_fast or model

    def get_model(self, mode: str = "deep") -> str:
        return self.model if mode == "deep" else self.model_fast

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def _is_reasoning_model(model: str) -> bool:
        """判断是否为推理模型（reasoning model）"""
        reasoning_keywords = ["hy3", "r1", "reasoning", "deepseek-r1", "deepseek-prover"]
        return any(kw in model.lower() for kw in reasoning_keywords)

    def chat(
        self,
        messages: list[dict],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        think: bool = False,  # OpenAI 兼容 API 不支持 think
    ) -> dict:
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": model or self.get_model(),
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        # 推理模型（如 tencent/hy3）需要启用 reasoning 参数
        model_name = model or self.get_model()
        if self._is_reasoning_model(model_name):
            payload["reasoning"] = {"effort": "low", "exclude": False}
        try:
            resp = requests.post(url, json=payload, headers=self._headers(), timeout=300)
            resp.raise_for_status()
            data = resp.json()
            logger.debug("OpenAICompat response: %s", json.dumps(data, ensure_ascii=False)[:500])
            choice = data["choices"][0]
            msg = choice.get("message", {})
            content = msg.get("content") or ""
            # 某些厂商在 reasoning_content 字段返回思考过程
            thinking = msg.get("reasoning_content", None)
            # 推理模型可能 content 为空，实际回答在 reasoning_content 中
            if not content and thinking:
                content = thinking
                thinking = None
            return {"content": content, "thinking": thinking}
        except requests.exceptions.ConnectionError:
            raise LLMError(f"无法连接 {self.base_url}，请检查网络和 API 地址")
        except KeyError:
            raise LLMError(f"API 返回格式异常: {resp.text[:200]}")
        except Exception as e:
            raise LLMError(f"OpenAI 兼容 API 调用失败: {e}")

    def stream(
        self,
        messages: list[dict],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        think: bool = False,
    ) -> Generator[dict, None, None]:
        url = f"{self.base_url}/chat/completions"
        model_name = model or self.get_model()
        payload = {
            "model": model_name,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True,
        }
        # 推理模型需要启用 reasoning 参数
        if self._is_reasoning_model(model_name):
            payload["reasoning"] = {"effort": "low", "exclude": False}
        try:
            with requests.post(url, json=payload, headers=self._headers(), stream=True, timeout=300) as resp:
                resp.raise_for_status()
                for line in resp.iter_lines():
                    if not line:
                        continue
                    line = line.decode("utf-8", errors="replace")
                    if not line.startswith("data: "):
                        continue
                    data_str = line[6:]
                    if data_str.strip() == "[DONE]":
                        yield {"content": "", "thinking": None, "done": True}
                        return
                    try:
                        data = json.loads(data_str)
                    except json.JSONDecodeError:
                        continue
                    choice = data.get("choices", [{}])[0]
                    # 流式完成（stop 或 end_turn 等都视为结束）
                    if choice.get("finish_reason") in ("stop", "end_turn"):
                        yield {"content": "", "thinking": None, "done": True}
                        return
                    delta = choice.get("delta", {})
                    content = delta.get("content") or ""
                    reasoning = delta.get("reasoning_content", None)
                    # 推理模型 content 为空时，用 reasoning_content 作为输出
                    if not content and reasoning:
                        content = reasoning
                        reasoning = None
                    if content or reasoning:
                        yield {"content": content, "thinking": reasoning, "done": False}
        except requests.exceptions.ConnectionError:
            raise LLMError(f"无法连接 {self.base_url}，请检查网络和 API 地址")
        except Exception as e:
            raise LLMError(f"OpenAI 兼容 API 流式调用失败: {e}")


def _strip_think_tags(text: str) -> str:
    """移除 <think>...</think> 标签"""
    if '</think>' in text:
        text = text.rsplit('</think>', 1)[-1].strip()
    text = re.sub(r'<think>.*', '', text, flags=re.DOTALL).strip()
    return text


def get_llm(mode: str = "deep") -> LLMProvider:
    """获取当前配置的 LLM Provider 实例

    Args:
        mode: "deep" 使用主模型，"fast" 使用快速模型
    """
    provider_name = settings.LLM_PROVIDER.lower()

    if provider_name == "ollama":
        return OllamaProvider(
            host=settings.OLLAMA_HOST,
            model=settings.OLLAMA_MODEL,
            model_fast=settings.OLLAMA_MODEL_FAST,
        )
    else:
        # 所有云端厂商走 OpenAI 兼容协议
        base_url = settings.LLM_BASE_URL or PROVIDER_BASE_URLS.get(provider_name, "")
        if not base_url:
            raise LLMError(f"未知的 LLM Provider: {provider_name}，请配置 LLM_BASE_URL")

        api_key = settings.LLM_API_KEY
        if not api_key:
            raise LLMError(f"使用 {provider_name} 需要配置 LLM_API_KEY")

        model = settings.LLM_MODEL or ""
        model_fast = settings.LLM_MODEL_FAST or model

        if not model:
            raise LLMError(f"使用 {provider_name} 需要配置 LLM_MODEL")

        return OpenAICompatProvider(
            base_url=base_url,
            api_key=api_key,
            model=model,
            model_fast=model_fast,
        )
