#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : world.py
# @Author: zaoshu
# @Date  : 2020-02-08
# @Desc  :
from sqlalchemy import Column, String, BigInteger

from model.base import BaseModel
from model.db import Model


class World(Model, BaseModel):
    __tablename__ = 'world'
    name = Column(String)
    date = Column(String)
    confirmed = Column(BigInteger, default=0)
    cured = Column(BigInteger, default=0)
    dead = Column(BigInteger, default=0)
    suspected = Column(BigInteger, default=0)
    add_dead = Column(BigInteger, default=0)
    add_confirmed = Column(BigInteger, default=0)
    add_cured = Column(BigInteger, default=0)
    add_suspected = Column(BigInteger, default=0)
