from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.sql.expression import null
from common import deps
from schemas import response
from sqlalchemy.orm import Session
from service.curd_role import curd_role
router = APIRouter()


@router.get("/list", name="角色列表")
async def role_list(db: Session = Depends(deps.get_db),*, page: int = 1, page_size: int = 10) -> Any:
    roles = curd_role.get_multi(db, page=page, limit=page_size)
    total = curd_role.count(db)
    return response.success(data=roles, count=total)


@router.get("/user_lists", name="角色下所有成员")
async def role_user_lists(db: Session = Depends(deps.get_db),*,role_id: int) -> Any:
    
    return null
