from typing import Any
from fastapi import APIRouter, Depends
from common import deps
from sqlalchemy.orm import Session
from schemas import sys_module, response_code
from service.sys_module import curd_module
router = APIRouter()


@router.post("/sysModule/create", name="新增")
async def create(
        parms: sys_module.ModuleCreate,
        db: Session = Depends(deps.get_db),
) -> Any:
    module= curd_module.create(db,obj_in=parms)
    return response_code.resp_200(data=module)
