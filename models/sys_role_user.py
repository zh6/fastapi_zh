from sqlalchemy import Column, Integer
from db.base_class import Base
class SysRoleUser(Base):
    user_id= Column(Integer , comment="用户id")
    role_id= Column(Integer,  comment="角色id")
    __table_args__ = ({'comment': '用户角色关联表'})