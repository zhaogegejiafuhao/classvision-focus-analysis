"""LLM Provider 配置 API"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

from backend.core.config import settings, Settings
from backend.core.security import get_current_user, assert_teacher_or_admin
from backend.core.rate_limit import llm_rate_limit
from backend.services.llm_client import get_llm, LLMError, PROVIDER_BASE_URLS

router = APIRouter(prefix="/api/llm", tags=["llm"])


class LLMConfigRequest(BaseModel):
    provider: str  # ollama / openrouter / dashscope / deepseek / siliconflow / custom
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    model: Optional[str] = None
    model_fast: Optional[str] = None
    # Ollama 专用
    ollama_host: Optional[str] = None
    ollama_model: Optional[str] = None
    ollama_model_fast: Optional[str] = None


class LLMConfigResponse(BaseModel):
    provider: str
    api_key_set: bool  # 不暴露实际 key，只显示是否已设置
    base_url: str
    model: str
    model_fast: str
    ollama_host: str
    ollama_model: str
    ollama_model_fast: str
    available_providers: list[dict]


class LLMTestResponse(BaseModel):
    success: bool
    message: str
    model: str


@router.get("/config", response_model=LLMConfigResponse)
def get_llm_config(current_user=Depends(get_current_user)):
    """获取当前 LLM 配置"""
    provider = settings.LLM_PROVIDER.lower()
    available = [
        {"value": k, "label": k.capitalize(), "base_url": v or "本地"}
        for k, v in PROVIDER_BASE_URLS.items()
    ]
    available.append({"value": "custom", "label": "自定义", "base_url": ""})

    return LLMConfigResponse(
        provider=provider,
        api_key_set=bool(settings.LLM_API_KEY),
        base_url=settings.LLM_BASE_URL or PROVIDER_BASE_URLS.get(provider, ""),
        model=settings.LLM_MODEL or settings.OLLAMA_MODEL,
        model_fast=settings.LLM_MODEL_FAST or settings.OLLAMA_MODEL_FAST,
        ollama_host=settings.OLLAMA_HOST,
        ollama_model=settings.OLLAMA_MODEL,
        ollama_model_fast=settings.OLLAMA_MODEL_FAST,
        available_providers=available,
    )


@router.put("/config", response_model=LLMConfigResponse)
def update_llm_config(req: LLMConfigRequest, current_user=Depends(get_current_user)):
    """更新 LLM 配置（写入 .env 文件）— 仅管理员/教师可操作"""
    assert_teacher_or_admin(current_user)
    env_path = ".env"
    
    # 读取现有 .env
    env_lines = []
    env_dict = {}
    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if "=" in line and not line.startswith("#"):
                    k, _, v = line.partition("=")
                    env_dict[k.strip()] = v.strip()
                env_lines.append(line)
    except FileNotFoundError:
        pass

    # 更新配置
    updates = {}
    updates["LLM_PROVIDER"] = req.provider

    if req.api_key is not None:
        updates["LLM_API_KEY"] = req.api_key
    if req.base_url is not None:
        updates["LLM_BASE_URL"] = req.base_url
    if req.model is not None:
        updates["LLM_MODEL"] = req.model
    if req.model_fast is not None:
        updates["LLM_MODEL_FAST"] = req.model_fast
    if req.ollama_host is not None:
        updates["OLLAMA_HOST"] = req.ollama_host
    if req.ollama_model is not None:
        updates["OLLAMA_MODEL"] = req.ollama_model
    if req.ollama_model_fast is not None:
        updates["OLLAMA_MODEL_FAST"] = req.ollama_model_fast

    env_dict.update(updates)

    # 写回 .env
    with open(env_path, "w", encoding="utf-8") as f:
        for k, v in env_dict.items():
            f.write(f"{k}={v}\n")

    # 重新加载 settings（pydantic Settings 字段名是大写的，如 LLM_PROVIDER）
    for key, value in updates.items():
        field_type = Settings.__annotations__.get(key, str)
        if field_type == bool:
            setattr(settings, key, str(value).lower() in ("true", "1", "yes"))
        elif field_type == int:
            setattr(settings, key, int(value))
        else:
            setattr(settings, key, value)

    return get_llm_config(current_user)


@router.post("/test", response_model=LLMTestResponse)
def test_llm_connection(current_user=Depends(get_current_user)):
    """测试 LLM 连接 — 仅管理员/教师可操作"""
    assert_teacher_or_admin(current_user)
    try:
        llm = get_llm()
        model = llm.get_model()
        result = llm.chat(
            messages=[{"role": "user", "content": "你好，请回复'连接成功'四个字"}],
            max_tokens=256,
            temperature=0.1,
        )
        content = result.get("content", "")
        if content:
            return LLMTestResponse(success=True, message=f"连接成功，模型响应: {content[:50]}", model=model)
        else:
            return LLMTestResponse(success=False, message="模型返回空内容", model=model)
    except LLMError as e:
        return LLMTestResponse(success=False, message=str(e), model=settings.LLM_PROVIDER)
    except Exception as e:
        return LLMTestResponse(success=False, message=f"连接失败: {e}", model=settings.LLM_PROVIDER)
