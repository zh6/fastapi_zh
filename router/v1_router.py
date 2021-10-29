"""

版本路由区分

# 可以在这里添加所需要的依赖
https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi

fastapi 没有像flask那样 分组子路由没有 middleware("http") 但是有 dependencies

"""
# check_authority 权限验证内部包含了 token 验证 如果不校验权限可直接 dependencies=[Depends(check_jwt_token)]
from fastapi import APIRouter, Depends
from common.deps import check_authority
from common.deps import check_jwt_token
from api.v1.user import router as user
from api.v1.login import router as login
from api.v1.module import router as module
from api.v1.role import router as role
api_v1_router = APIRouter()
api_v1_router.include_router(login,tags=["登录"])
api_v1_router.include_router(user,prefix="/user", tags=["用户"],dependencies=[Depends(check_authority)])
api_v1_router.include_router(module,prefix="/module",  tags=["模块管理"])
api_v1_router.include_router(role,prefix="/role",  tags=["角色管理"])
