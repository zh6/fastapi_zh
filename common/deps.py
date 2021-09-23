"""

一些通用的依赖功能

"""
from typing import Generator, Any, Union, Optional

from jose import jwt
from fastapi import Header, Depends, Request
from sqlalchemy.orm import Session,aliased
from pydantic import ValidationError
from db.session import SessionLocal
from common import custom_exc, sys_casbin
from models.sys_auth import SysRole, SysRoleUser, SysUser
from core.config import settings
from service.sys_user import curd_user
from sqlalchemy import func
from schemas import sys_user  
from collections import deque
def get_db() -> Generator:
    """
    获取sqlalchemy会话对象
    :return:
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def check_jwt_token(
        token: Optional[str] = Header(..., description="登录token")
) -> Union[str, Any]:
    """
    解析验证token  默认验证headers里面为token字段的数据
    可以给 headers 里面token替换别名, 以下示例为 X-Token
    token: Optional[str] = Header(None, alias="X-Token")
    :param token:
    :return:
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise custom_exc.TokenExpired()
    except (jwt.JWTError, ValidationError, AttributeError):
        raise custom_exc.TokenAuthError()


def get_current_user(
        db: Session = Depends(get_db),
        token: Optional[str] = Depends(check_jwt_token)
):
    """
    根据header中token 获取当前用户
    :param db:
    :param token:
    :return:
    """
    user_id=token.get("sub")
    sys_id=token.get("sys_id")
    roles=db.query(SysRole).join(SysRoleUser,SysRoleUser.role_id==SysRole.id).filter(
        SysRoleUser.user_id == user_id,SysRole.sys_id==sys_id).all()
    roles=[role for role in roles]
    user=db.query(SysUser).filter(SysUser.id == user_id, SysUser.is_delete == 0).first()
    user_dict = {"nickname": user.nickname, "email": user.email, "phone":user.phone,"avatar": user.avatar,"roles": [{"id": role.id,"sys_id": role.sys_id, "name": role.name}
                           for role in roles]}
    return sys_user.UserBase(**user_dict)


def check_authority(
        request: Request,
        user: sys_user.UserBase = Depends(get_current_user)
):
    """
    权限验证 依赖于 JWT token
    :param request:
    :param token:
    :return:
    """
    role_ids=[role.id for role in user.roles]
    sys_id=user.roles[0].sys_id
    path = request.url.path
    e = sys_casbin.get_casbin()
    a=[roleId for roleId in role_ids if e.enforce(str(roleId),str(sys_id), path)]
    if not a:
        raise custom_exc.AuthenticationError()
