from sqlalchemy import Column, Integer, VARCHAR
from db.base_class import Base
class SysRole(Base):
    name = Column(VARCHAR(32), comment="角色名")
    sys_id=Column(Integer,nullable=False,comment="系统id")
    __table_args__ = ({'comment': '用户角色表'})