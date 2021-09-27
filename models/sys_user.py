from sqlalchemy import Column, Integer, VARCHAR
from db.base_class import Base, gen_uuid
class SysUser(Base):
    email = Column(VARCHAR(128), unique=True, index=True, nullable=False, comment="邮箱")
    phone = Column(VARCHAR(16), unique=True, index=True, nullable=True, comment="手机号")
    nickname = Column(VARCHAR(128), comment="昵称")
    avatar = Column(VARCHAR(256), comment="头像")
    hashed_password = Column(VARCHAR(128), nullable=False, comment="密码")
    is_active = Column(Integer, default=False, comment="邮箱是否激活 0=未激活 1=激活", server_default="0")
    __table_args__ = ({'comment': '系统用户表'})