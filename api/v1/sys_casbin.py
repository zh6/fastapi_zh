from fastapi import APIRouter

from common.sys_casbin import get_casbin
from schemas import casbin,response_code

router = APIRouter()


@router.post("/add/auth", summary="添加访问权限", name="添加访问权限", description="添加访问权限")
async def add_authority(
        authority_info: casbin.AuthCreate
):
    e = get_casbin()
    res = e.add_policy(authority_info.role_id,authority_info.sys_id, authority_info.path)
    if res:
        return response_code.resp_200()
    else:
        return response_code.resp_4001(message="添加失败，权限已存在")


@router.post("/del/auth", summary="删除访问权限")
async def del_authority(
        authority_info: casbin.AuthCreate
):
    e = get_casbin()
    res = e.remove_policy(authority_info.role_id,authority_info.sys_id,authority_info.path)
    if res:
        return response_code.resp_200()
    else:
        return response_code.resp_4001(message="删除失败，权限不存在")
