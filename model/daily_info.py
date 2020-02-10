#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : daily.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
from sqlalchemy import Column, String, Boolean

from model.base import BaseModel
from model.db import Model


class DailyInfo(Model, BaseModel):
    __tablename__ = 'daily_info'
    name = Column(String)
    date = Column(String)
    in_sh = Column(Boolean)
    health = Column(Boolean)
    symptom = Column(String)
    contact_history = Column(Boolean)
    access_public = Column(Boolean)
    return_date = Column(String)
    note = Column(String)
