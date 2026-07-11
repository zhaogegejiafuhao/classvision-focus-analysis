"""JWT 认证与密码哈希工具"""
from datetime import datetime, timedelta, timezone
from typing import Iterable

import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from backend.core.config import settings
from backend.core.database import get_db
from backend.models.tables import RegisteredPerson

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not hashed_password:
        return False
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(hours=settings.JWT_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError:
        return {}


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> RegisteredPerson:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭据",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    user_id = payload.get("sub")
    if user_id is None:
        raise credentials_exception
    user = db.query(RegisteredPerson).filter(RegisteredPerson.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
    return user


def require_role(allowed_roles: Iterable[str]):
    """返回一个依赖，校验当前用户角色是否在 allowed_roles 中。

    用法:
        @router.post("/...", dependencies=[Depends(require_role(["teacher", "admin"]))])
        或作为参数依赖:
        current_user: RegisteredPerson = Depends(require_role(["teacher", "admin"]))
    """

    def _checker(current_user: RegisteredPerson = Depends(get_current_user)) -> RegisteredPerson:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"权限不足，需要角色: {', '.join(allowed_roles)}",
            )
        return current_user

    return _checker


def assert_owner_or_admin(owner_id: int | None, current_user: RegisteredPerson) -> None:
    """创建者或管理员才能通过，否则抛 403。

    用于删除操作：创建者可删除自己的资源，admin 可删除任何资源。
    """
    if current_user.role == "admin":
        return
    if owner_id is None or owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="仅创建者或管理员可执行此操作",
        )


def assert_teacher_or_admin(current_user: RegisteredPerson) -> None:
    """教师或管理员才能通过，否则抛 403。用于创建/编辑操作。"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="仅教师或管理员可执行此操作",
        )
