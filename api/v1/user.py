from typing import Any
from fastapi import APIRouter, Depends
from common import deps
from schemas import user,response
router = APIRouter()
@router.post("/info", summary="获取用户信息", name="获取用户信息", description="此API没有验证权限")
async def get_user_info(
        current_user: user.UserBase = Depends(deps.get_current_user)
) -> Any:
    """
    获取用户信息 这个路由分组没有验证权限
    :param current_user:
    :return:
    """
    return response.success(data={
        "nickname": current_user.nickname,
        "avatar": current_user.avatar
    })
