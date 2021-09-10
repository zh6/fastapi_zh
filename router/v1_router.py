"""

版本路由区分

# 可以在这里添加所需要的依赖
https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi

fastapi 没有像flask那样 分组子路由没有 middleware("http") 但是有 dependencies

"""

from fastapi import APIRouter, Depends
from common.deps import check_authority
from common.deps import check_jwt_token
from api.v1.sys_user import router as user_router
from api.v1.sys_login import router as login_router
from api.v1.sys_casbin import router as sys_casbin_router

api_v1_router = APIRouter()
api_v1_router.include_router(login_router,tags=["登录"])
api_v1_router.include_router(user_router,tags=["用户"],dependencies=[Depends(check_authority)])
# check_authority 权限验证内部包含了 token 验证 如果不校验权限可直接 dependencies=[Depends(check_jwt_token)]
api_v1_router.include_router(sys_casbin_router, tags=["权限API管理"],  dependencies=[Depends(check_authority)])
