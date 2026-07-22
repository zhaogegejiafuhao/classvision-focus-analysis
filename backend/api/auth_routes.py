"""认证 API 路由（登录、获取当前用户）"""
import time
from collections import defaultdict
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import create_access_token, get_current_user, verify_password, hash_password
from backend.models.tables import RegisteredPerson
from backend.models.schemas import LoginRequest, LoginResponse, UserOut

router = APIRouter(prefix="/api/auth", tags=["auth"])

# ===== 简单内存限流 =====
_login_attempts: dict[str, list[float]] = defaultdict(list)
_register_attempts: dict[str, list[float]] = defaultdict(list)
RATE_LIMIT_WINDOW = 300  # 5 分钟
RATE_LIMIT_MAX_LOGIN = 10  # 每IP 5分钟最多10次登录
RATE_LIMIT_MAX_REGISTER = 5  # 每IP 5分钟最多5次注册


def _check_rate_limit(attempts_dict: dict, key: str, max_attempts: int):
    """检查请求频率限制"""
    now = time.time()
    attempts = attempts_dict[key]
    # 清理过期记录
    attempts_dict[key] = [t for t in attempts if now - t < RATE_LIMIT_WINDOW]
    if len(attempts_dict[key]) >= max_attempts:
        raise HTTPException(429, "请求过于频繁，请稍后再试")
    attempts_dict[key].append(now)


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
    client_ip = request.client.host if request.client else "unknown"
    _check_rate_limit(_login_attempts, client_ip, RATE_LIMIT_MAX_LOGIN)
    user = db.query(RegisteredPerson).filter(RegisteredPerson.username == req.username).first()
    if not user or not verify_password(req.password, user.password_hash):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    token = create_access_token({"sub": str(user.id), "role": user.role})
    return LoginResponse(access_token=token, user=UserOut.model_validate(user))


@router.post("/register", response_model=LoginResponse)
def register(req: RegisterRequest, request: Request, db: Session = Depends(get_db)):
    """用户自主注册（默认学生角色）"""
    client_ip = request.client.host if request.client else "unknown"
    _check_rate_limit(_register_attempts, client_ip, RATE_LIMIT_MAX_REGISTER)
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
