#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : history.py
# @Author: zaoshu
# @Date  : 2020-02-08
# @Desc  :
from sqlalchemy import String, Column, BigInteger

from model.base import BaseModel
from model.db import Model


class History(Model, BaseModel):
    __tablename__ = 'history'
    date = Column(String)
    confirmed = Column(BigInteger, default=0)
    cured = Column(BigInteger, default=0)
    dead = Column(BigInteger, default=0)
    suspected = Column(BigInteger, default=0)
