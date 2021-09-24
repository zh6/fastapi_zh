
from sqlalchemy import Column, VARCHAR,Integer
from db.base_class import Base
class SysApi(Base):
    name= Column(VARCHAR(50), comment="名称")
    zh_name= Column(VARCHAR(50), comment="中文名称")
    api = Column(VARCHAR(128), comment="API路径")
    module_id=Column(Integer, comment="模块id")
    __table_args__ = ({'comment': 'API管理表'})
