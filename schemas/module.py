from pydantic import BaseModel
# 新增模块
class ModuleCreate(BaseModel):
    name = str
    icon_cls= str
    caption= str
    sort= int
    parent_id=int
    sys_id=int
class ModuleBase(BaseModel):
    name = str
    icon_cls= str
    caption= str
    sort= int
    parent_id=int
    sys_id=int
