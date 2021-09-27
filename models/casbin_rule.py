from sqlalchemy import Column, VARCHAR,Integer
from db.base_class import Base

class CasbinRule(Base):
    ptype = Column(VARCHAR(255))
    v0 = Column(VARCHAR(255))
    v1 = Column(VARCHAR(255))
    v2 = Column(VARCHAR(255))
    v3 = Column(VARCHAR(255))
    v4 = Column(VARCHAR(255))
    v5 = Column(VARCHAR(255))
    __table_args__ = ({'comment': 'casbin权限'})
