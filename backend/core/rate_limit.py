"""轻量级内存速率限制器

基于滑动窗口算法，使用进程内存存储（单实例部署足够）。
对于多实例部署，应替换为 Redis 实现。

使用方式：
    from backend.core.rate_limit import rate_limit_dependency, llm_rate_limit

    # 在路由中作为依赖使用
    @router.post("/expensive")
    async def expensive_op(_rl: None = Depends(rate_limit_dependency("20/minute"))):
        ...

    # 或使用预设的 LLM 限制
    @router.post("/llm-call")
    async def llm_call(_rl: None = Depends(llm_rate_limit)):
        ...
"""

import time
from collections import defaultdict
from threading import Lock
from typing import Optional

from fastapi import HTTPException, Request, status


class SlidingWindowRateLimiter:
    """滑动窗口速率限制器（进程内存）"""

    def __init__(self):
        # key -> list of timestamps
        self._hits: dict[str, list[float]] = defaultdict(list)
        self._lock = Lock()

    def check(self, key: str, limit: int, window_seconds: int) -> tuple[bool, dict]:
        """检查是否允许请求。

        返回 (allowed, info)：
            allowed: True 如果允许
            info: {limit, remaining, reset_at}
        """
        now = time.time()
        cutoff = now - window_seconds

        with self._lock:
            # 清理过期记录
            hits = self._hits[key]
            # 保留窗口内的记录
            while hits and hits[0] < cutoff:
                hits.pop(0)

            current = len(hits)
            if current >= limit:
                # 计算最早记录何时过期
                reset_at = hits[0] + window_seconds if hits else now + window_seconds
                return False, {
                    "limit": limit,
                    "remaining": 0,
                    "reset_at": reset_at,
                    "retry_after": int(reset_at - now) + 1,
                }

            hits.append(now)
            return True, {
                "limit": limit,
                "remaining": limit - current - 1,
                "reset_at": now + window_seconds,
            }

    def cleanup(self, max_age: int = 3600):
        """清理超过 max_age 秒的记录，避免内存泄漏"""
        now = time.time()
        cutoff = now - max_age
        with self._lock:
            empty_keys = []
            for key, hits in self._hits.items():
                # 移除过期记录
                while hits and hits[0] < cutoff:
                    hits.pop(0)
                if not hits:
                    empty_keys.append(key)
            for key in empty_keys:
                del self._hits[key]


# 全局单例
_limiter = SlidingWindowRateLimiter()


def _parse_limit(limit_str: str) -> tuple[int, int]:
    """解析 '20/minute' -> (20, 60)"""
    parts = limit_str.strip().split("/")
    if len(parts) != 2:
        raise ValueError(f"Invalid limit format: {limit_str}")
    count = int(parts[0])
    unit = parts[1].lower()
    multipliers = {
        "second": 1,
        "seconds": 1,
        "minute": 60,
        "minutes": 60,
        "hour": 3600,
        "hours": 3600,
    }
    if unit not in multipliers:
        raise ValueError(f"Unknown time unit: {unit}")
    return count, multipliers[unit]


def _get_client_id(request: Request) -> str:
    """获取客户端标识：优先用认证用户 ID，否则用 IP"""
    # 尝试从 JWT 中获取用户 ID（不强制认证，仅用于限流键）
    auth = request.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        try:
            from backend.core.security import decode_access_token
            payload = decode_access_token(auth[7:])
            if payload and "sub" in payload:
                return f"user:{payload['sub']}"
        except Exception:
            pass

    # 回退到 IP（考虑代理转发）
    forwarded = request.headers.get("X-Forwarded-For", "")
    if forwarded:
        ip = forwarded.split(",")[0].strip()
    else:
        ip = request.client.host if request.client else "unknown"
    return f"ip:{ip}"


def rate_limit_dependency(limit_str: str, scope: Optional[str] = None):
    """创建速率限制依赖项。

    Args:
        limit_str: 限制字符串，如 "20/minute"
        scope: 限制范围，None=按路由路径分组，指定则全局共享
    """

    def _dependency(request: Request):
        from backend.core.config import settings

        if not settings.RATE_LIMIT_ENABLED:
            return None

        limit, window = _parse_limit(limit_str)
        client_id = _get_client_id(request)
        route_path = scope or request.url.path
        key = f"{client_id}:{route_path}"

        allowed, info = _limiter.check(key, limit, window)
        if not allowed:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f"请求过于频繁，请 {info['retry_after']} 秒后重试",
                headers={
                    "Retry-After": str(info["retry_after"]),
                    "X-RateLimit-Limit": str(info["limit"]),
                    "X-RateLimit-Remaining": "0",
                    "X-RateLimit-Reset": str(int(info["reset_at"])),
                },
            )
        return None

    return _dependency


# 预设的速率限制依赖
def llm_rate_limit(request: Request):
    """LLM 路由速率限制：默认 20/minute"""
    from backend.core.config import settings
    if not settings.RATE_LIMIT_ENABLED:
        return None
    limit, window = _parse_limit(settings.RATE_LIMIT_LLM)
    client_id = _get_client_id(request)
    key = f"{client_id}:llm"
    allowed, info = _limiter.check(key, limit, window)
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail=f"LLM 请求过于频繁，请 {info['retry_after']} 秒后重试",
            headers={"Retry-After": str(info["retry_after"])},
        )
    return None


def auth_rate_limit(request: Request):
    """认证路由速率限制：默认 10/minute（防暴力破解）"""
    from backend.core.config import settings
    if not settings.RATE_LIMIT_ENABLED:
        return None
    limit, window = _parse_limit(settings.RATE_LIMIT_AUTH)
    client_id = _get_client_id(request)
    key = f"{client_id}:auth"
    allowed, info = _limiter.check(key, limit, window)
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail="登录尝试过于频繁，请稍后重试",
            headers={"Retry-After": str(info["retry_after"])},
        )
    return None
