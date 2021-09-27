from sqlalchemy import Column, VARCHAR,Numeric,Integer
from db.base_class import Base

class Bill(Base):
    bill_method=Column(Integer,nullable=False,default=1,comment="账单类型（1：收款；2：转账）")
    bill_code= Column(VARCHAR(100),comment="账单编码")
    bill_name= Column(VARCHAR(100), comment="账单名称")
    member_id = Column(Integer,comment="商户id")
    member_name = Column(VARCHAR(128), comment="商户名称")
    total_amount=Column(Numeric(18,2),comment="账单金额")
    rate=Column(Numeric(18,2),comment="费率")
    rate_amount=Column(Numeric(18,2),comment="费率金额")
    payable_amount=Column(Numeric(18,2),comment="应付金额")
    real_amount=Column(Numeric(18,2),comment="实付金额")
    status=Column(Integer,nullable=False,default=0,comment="状态：0付款中，1交易成功 ")
    remark=Column(VARCHAR(100),comment="备注")
    __table_args__ = ({'comment': '账单表'})
