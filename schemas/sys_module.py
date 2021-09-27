from typing import Optional
from pydantic import BaseModel
# 新增


class ModuleCreate(BaseModel):
    name: Optional[str]
    icon_cls: str
    caption: Optional[str]
    sort: Optional[int]
    parent_id: Optional[int]=None
    sys_id: Optional[int]
# 修改


class ModuleUpdate(BaseModel):
    name: str
    icon_cls: str
    caption: str
    sort: int
    parent_id: int
    sys_id: int


class ModuleBase(BaseModel):
    name: str
    icon_cls: str
    caption: str
    sort: int
    parent_id: int
    sys_id: int
