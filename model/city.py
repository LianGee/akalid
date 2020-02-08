#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : city.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :
from sqlalchemy import Column, String, BigInteger

from model.base import BaseModel
from model.db import Model


class City(Model, BaseModel):
    __tablename__ = 'city'
    city_name = Column(String)
    province_name = Column(String)
    date = Column(String)
    confirmed = Column(BigInteger, default=0)
    cured = Column(BigInteger, default=0)
    dead = Column(BigInteger, default=0)
    suspected = Column(BigInteger, default=0)
    location_id = Column(BigInteger, default=0)
