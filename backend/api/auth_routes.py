"""认证 API 路由（登录、获取当前用户）"""
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import create_access_token, get_current_user, verify_password, hash_password
from backend.core.rate_limit import _limiter
from backend.models.tables import RegisteredPerson
from backend.models.schemas import LoginRequest, LoginResponse, UserOut

router = APIRouter(prefix="/api/auth", tags=["auth"])

# 认证限流参数（5 分钟窗口，登录 10 次/注册 5 次，防暴力破解）
_AUTH_WINDOW = 300  # 5 分钟
_AUTH_LOGIN_MAX = 10  # 每IP 5分钟最多10次登录
_AUTH_REGISTER_MAX = 5  # 每IP 5分钟最多5次注册


def _check_auth_rate_limit(request: Request, action: str, max_attempts: int):
    """认证路由限流（复用框架 SlidingWindowRateLimiter，按 IP + 动作分组）"""
    forwarded = request.headers.get("X-Forwarded-For", "")
    if forwarded:
        ip = forwarded.split(",")[0].strip()
    else:
        ip = request.client.host if request.client else "unknown"
    key = f"ip:{ip}:auth_{action}"
    allowed, info = _limiter.check(key, max_attempts, _AUTH_WINDOW)
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail="请求过于频繁，请稍后再试",
            headers={"Retry-After": str(info["retry_after"])},
        )


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str


class RegisterRequest(BaseModel):
    name: str
    username: str
    password: str
    role: str = "student"


@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest, request: Request, db: Session = Depends(get_db)):
    """用户名/密码登录，返回 JWT token"""
    _check_auth_rate_limit(request, "login", _AUTH_LOGIN_MAX)
    user = db.query(RegisteredPerson).filter(RegisteredPerson.username == req.username).first()
    if not user or not verify_password(req.password, user.password_hash):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    token = create_access_token({"sub": str(user.id), "role": user.role})
    return LoginResponse(access_token=token, user=UserOut.model_validate(user))


@router.post("/register", response_model=LoginResponse)
def register(req: RegisterRequest, request: Request, db: Session = Depends(get_db)):
    """用户自主注册（默认学生角色）"""
    _check_auth_rate_limit(request, "register", _AUTH_REGISTER_MAX)
    if len(req.password) < 6:
        raise HTTPException(400, "密码至少6位")
    if req.role not in ("student", "teacher"):
        raise HTTPException(400, "只能注册学生或教师角色")

    existing = db.query(RegisteredPerson).filter(RegisteredPerson.username == req.username).first()
    if existing:
        raise HTTPException(400, "用户名已存在")

    person = RegisteredPerson(
        name=req.name,
        username=req.username,
        password_hash=hash_password(req.password),
        role=req.role,
        face_embedding="[]",
    )
    db.add(person)
    db.commit()
    db.refresh(person)

    token = create_access_token({"sub": str(person.id), "role": person.role})
    return LoginResponse(access_token=token, user=UserOut.model_validate(person))


@router.get("/me", response_model=UserOut)
def get_me(current_user: RegisteredPerson = Depends(get_current_user)):
    """获取当前登录用户信息"""
    return current_user


@router.post("/change-password")
def change_password(
    req: ChangePasswordRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """修改当前用户密码"""
    if not verify_password(req.old_password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="当前密码错误")
    if len(req.new_password) < 6:
        raise HTTPException(status_code=400, detail="新密码至少6位")
    current_user.password_hash = hash_password(req.new_password)
    db.commit()
    return {"message": "密码修改成功"}
