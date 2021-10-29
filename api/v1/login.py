from typing import Any
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from core import security
from common import deps, logger
from core.config import settings
from schemas import user, response
from service.curd_user import curd_user
router = APIRouter()


@router.post("/login", summary="用户登录认证", name="登录")
async def login(
        *,
        db: Session = Depends(deps.get_db),
        user_info: user.UserEmailAuth,
) -> Any:
    # 验证用户
    user = curd_user.authenticate(
        db, email=user_info.username, password=user_info.password)

    if not user:
        logger.info(
            f"用户邮箱认证错误: email{user_info.username} password:{user_info.password}")
        return response.error(message="username or password error")
    elif not curd_user.is_active(user):
        return response.error(message="User email not activated")
    # 获取模块
    
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    # 登录token 存储了user.id 和sys_id
    return response.success(data={
        "token": security.create_access_token(user.id, user_info.sys_id, expires_delta=access_token_expires),
        "user":user
    })