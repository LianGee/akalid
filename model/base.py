#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : base.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  :
import math
from datetime import datetime

from sqlalchemy import Column, BigInteger

from model.db import db_session


class BaseModel:
    id = Column(BigInteger, primary_key=True)
    created_at = Column(BigInteger, index=True, default=math.floor(datetime.now().timestamp()))
    updated_at = Column(BigInteger, index=True, default=math.floor(datetime.now().timestamp()))

    @classmethod
    def get_session(cls):
        return db_session()

    @classmethod
    def select(cls):
        session = cls.get_session()
        try:
            return session.query(cls)
        finally:
            session.close()

    def update(self, *args, **kwargs):
        session = self.get_session()
        try:
            session.commit()
        finally:
            session.close()

    def insert(self):
        session = self.get_session()
        session.add(self)
        session.commit()
        session.close()

    def delete(self):
        session = self.get_session()
        session.delete(self)
        session.commit()
        session.close()

    @classmethod
    def bulk_insert(cls, lst: []):
        session = cls.get_session()
        session.bulk_insert_mappings(cls, [obj.__dict__ for obj in lst])
        session.commit()
        session.close()

    def get_json(self):
        result = self.__dict__
        result.pop('_sa_instance_state')
        return result
