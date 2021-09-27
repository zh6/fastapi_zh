
from sqlalchemy import Column, VARCHAR,Integer
from db.base_class import Base
class SysModule(Base):
    name = Column(VARCHAR(50), comment="模块名称")
    icon_cls= Column(VARCHAR(50), comment="图标")
    caption= Column(VARCHAR(50), comment="路由")
    sort= Column(Integer, comment="排序")
    parent_id=Column(Integer, comment="父级id")
    sys_id=Column(Integer, comment="所属系统")
    __table_args__ = ({'comment': '模块表'})
