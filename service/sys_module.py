from typing import Optional
from sqlalchemy.orm import Session
from service.curd_base import CRUDBase
from models.sys_module import SysModule
from schemas import sys_module


class CRUDModule(CRUDBase[SysModule, sys_module.ModuleCreate, sys_module.ModuleUpdate]):

    def create(self, db: Session, obj_in: sys_module.ModuleCreate) -> SysModule:
        db_obj = SysModule(
            name=obj_in.name,
            icon_cls=obj_in.icon_cls,
            caption=obj_in.caption,
            sort=obj_in.sort,
            parent_id=obj_in.parent_id,
            sys_id=obj_in.sys_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    def update(self, db: Session, obj_in: sys_module.ModuleUpdate) -> SysModule:
        db_obj = SysModule(
            name=obj_in.name,
            icon_cls=obj_in.icon_cls,
            caption=obj_in.caption,
            sort=obj_in.sort,
            parent_id=obj_in.parent_id,
            sys_id=obj_in.sys_id
        )
        db.update(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

curd_module = CRUDModule(SysModule)
