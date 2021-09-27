from sqlalchemy import Column, Integer, VARCHAR,ForeignKey
from db.base_class import Base, gen_uuid
from sqlalchemy.orm import relationship

class SysUser(Base):
    email = Column(VARCHAR(128), unique=True, index=True, nullable=False, comment="邮箱")
    phone = Column(VARCHAR(16), unique=True, index=True, nullable=True, comment="手机号")
    nickname = Column(VARCHAR(128), comment="昵称")
    avatar = Column(VARCHAR(256), comment="头像")
    hashed_password = Column(VARCHAR(128), nullable=False, comment="密码")
    is_active = Column(Integer, default=False, comment="邮箱是否激活 0=未激活 1=激活", server_default="0")
    __table_args__ = ({'comment': '系统用户表'})


class SysRole(Base):
    name = Column(VARCHAR(32), comment="角色名")
    sys_id=Column(Integer,nullable=False,comment="系统id")
    __table_args__ = ({'comment': '用户角色表'})

class SysRoleUser(Base):
    user_id= Column(Integer , comment="用户id")
    role_id= Column(Integer,  comment="角色id")
    __table_args__ = ({'comment': '用户角色关联表'})


