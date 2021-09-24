"""
管理员表的 字段model模型 验证  响应
"""

from typing import Optional, List

from pydantic import BaseModel, EmailStr, AnyHttpUrl

# 角色基础模型
class RoleBase(BaseModel):
    id:int
    name: str
    sys_id: int
# 用户基础模型
class UserBase(BaseModel):
    nickname:str
    email: EmailStr
    phone: Optional[int] = None
    avatar: Optional[str]=None
    is_active: Optional[bool] = True
    roles: List[RoleBase] = []


class UserAuth(BaseModel):
    password: str


# 邮箱登录认证 验证数据字段都叫username
class UserEmailAuth(UserAuth):
    username: EmailStr
    sys_id:str


# 手机号登录认证 验证数据字段都叫username
class UserPhoneAuth(UserAuth):
    username: int
    sys_id:str


# 创建账号需要验证的条件
class UserCreate(UserBase):
    nickname: str
    email: EmailStr
    password: str
    avatar: Optional[AnyHttpUrl] = None

