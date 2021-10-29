from typing import Any
from fastapi import APIRouter, Depends
from common import deps
from sqlalchemy.orm import Session
from models.sys_module import SysModule
from schemas import module, response
router = APIRouter()

@router.get('/lists', name="菜单列表")
async def lists(db: Session = Depends(deps.get_db))-> Any:
    # 查询一级菜单
    module_list = []
    all_modules= db.query(SysModule).all()
    parent_modules = db.query(SysModule).filter(SysModule.parent_id == 0).all()
    all_parent_ids = [module.parent_id for module in db.query(SysModule.parent_id).distinct().all()]
    for parent_module in parent_modules:
        # 递归获得子菜单
        parent_module_dict = {"id": str(parent_module.id), "name": parent_module.name}
        if parent_module.id in all_parent_ids:
            parent_module_dict["children"] = get_menus(parent_module.id, all_modules, all_parent_ids)
        module_list.append(parent_module_dict)
    return response.success(data=module_list)
def get_menus(parent_id, all_modules, all_parent_ids)-> Any:
    child_modules = []
    child_modules_dicts = []
    for module in all_modules:
        if module.parent_id == parent_id:
            child_modules.append(module)
    for child_module in child_modules:
        # 判断有没有子菜单
        child_modules_dict = {"id": str(child_module.id), "name": child_module.name}
        if child_module.id in all_parent_ids:
            child_modules_dict["children"] = get_menus(child_module.id, all_modules, all_parent_ids)
        child_modules_dicts.append(child_modules_dict)
    if len(child_modules) == 0:
        return
    return child_modules_dicts
