#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
from sqlalchemy import Column, String, Boolean

from model.base import BaseModel
from model.db import Model


class User(Model, BaseModel):
    __tablename__ = 'user'
    name = Column(String)
    phone = Column(String)
    id_num = Column(String)
    chinese_name = Column(String)
    email = Column(String)
    password = Column(String)
    is_inner_staff = Column(Boolean)
    location = Column(String)
    sh_location = Column(String)
