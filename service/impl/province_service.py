#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : province_service.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  :
import math
from datetime import datetime, timedelta

from model.province import Province
from service.province_service_api import ProvinceServiceApi


class ProvinceService(ProvinceServiceApi):
    @classmethod
    def query_with_time(cls, start: int, end: int):
        return Province.select().filter(Province.created_at.between(start, end)).all()

    @classmethod
    def delete_today(cls):
        now = datetime.now()
        current_time = math.floor(now.timestamp())
        now = now + timedelta(days=-1)
        start_time = math.floor(now.replace(hour=23, minute=59, second=59, microsecond=0).timestamp())
        Province.select().filter(Province.created_at.between(start_time, current_time)).delete(synchronize_session=False)

    @classmethod
    def query_today(cls):
        now = datetime.now()
        current_time = math.floor(now.timestamp())
        start_time = math.floor(now.replace(hour=0, minute=0, second=0, microsecond=0).timestamp())
        return Province.select().filter(Province.created_at.between(start_time, current_time)).all()

    @classmethod
    def bulk_insert(cls, provinces: [Province]):
        Province.bulk_insert(provinces)

    @classmethod
    def query_all(cls):
        return Province.select().all()

    @classmethod
    def save(cls, province: Province):
        if province.id is not None:
            province.update()
        else:
            province.insert()


