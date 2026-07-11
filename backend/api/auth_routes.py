"""认证 API 路由（登录、获取当前用户）"""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import create_access_token, get_current_user, verify_password, hash_password
from backend.models.tables import RegisteredPerson
from backend.models.schemas import LoginRequest, LoginResponse, UserOut

router = APIRouter(prefix="/api/auth", tags=["auth"])


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str


@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest, db: Session = Depends(get_db)):
    """用户名/密码登录，返回 JWT token"""
    user = db.query(RegisteredPerson).filter(RegisteredPerson.username == req.username).first()
    if not user or not verify_password(req.password, user.password_hash):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    token = create_access_token({"sub": str(user.id), "role": user.role})
    return LoginResponse(access_token=token, user=UserOut.model_validate(user))


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
