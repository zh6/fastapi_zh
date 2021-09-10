#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:33
# @Author  : CoderCharm
# @File    : create_user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
初始化数据库角色


"""

from db.session import SessionLocal
from common.sys_casbin import get_casbin



def init_casbin():
    """
    初始化casbin的基本API数据

    把 api_v1_router 分组的所有路由都添加到 casbin里面
    :return:
    """
    e = get_casbin()
    # e.add_grouping_policy("1","3","1")
    # e.add_policy("3", "1","1", "GET")
    aa=e.get_grouping_policy()
    bb=e.get_named_policy("p")
    cc=e.get_filtered_grouping_policy(0,"1")
    dd=e.get_filtered_policy(3,"GET")
    print(bb)

db = SessionLocal()

init_casbin()


