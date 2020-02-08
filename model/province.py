#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Province.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  :
from sqlalchemy import Column, String, BigInteger

from model.base import BaseModel
from model.db import Model


class Province(Model, BaseModel):
    __tablename__ = 'province'
    country = Column(String)
    province_name = Column(String)
    short_name = Column(String)
    date = Column(String)
    confirmed = Column(BigInteger, default=0)
    cured = Column(BigInteger, default=0)
    dead = Column(BigInteger, default=0)
    suspected = Column(BigInteger, default=0)
