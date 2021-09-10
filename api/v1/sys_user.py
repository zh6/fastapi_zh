#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 13:38
# @Author  : CoderCharm
# @File    : sys_user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from typing import Any
from datetime import timedelta

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from core import security
from models import sys_auth
from common import deps, logger
from core.config import settings
from schemas import sys_user,response_code
from service.sys_user import curd_user

router = APIRouter()

@router.get("/user/info", summary="获取用户信息", name="获取用户信息", description="此API没有验证权限")
async def get_user_info(
        *,
        current_user: sys_user.UserBase = Depends(deps.get_current_user)
) -> Any:
    """
    获取用户信息 这个路由分组没有验证权限
    :param current_user:
    :return:
    """
    return response_code.resp_200(data={
        "nickname": current_user.nickname,
        "avatar": current_user.avatar
    })
