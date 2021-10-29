from typing import Optional
from sqlalchemy.orm import Session
from service.curd_base import CRUDBase
from models.sys_role import SysRole
from schemas.role import Create,Update
class CRUDRole(CRUDBase[SysRole, Create, Update]):

    def create(self, db: Session, obj_in: Create) -> SysRole:
        db_obj = SysRole(
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
    def update(self, db: Session, obj_in: Update) -> SysRole:
        db_obj = SysRole(
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

curd_role = CRUDRole(SysRole)
