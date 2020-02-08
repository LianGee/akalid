#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : city_service.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :
import math
from datetime import datetime, timedelta

from model.city import City
from service.city_service_api import CityServiceApi


class CityService(CityServiceApi):

    @classmethod
    def query_by_time(cls, start: int, end: int):
        return City.select().filter(City.created_at.between(start, end)).all()

    @classmethod
    def delete_today(cls):
        now = datetime.now()
        current_time = math.floor(now.timestamp())
        now = now + timedelta(days=-1)
        start_time = math.floor(now.replace(hour=23, minute=59, second=59, microsecond=0).timestamp())
        City.select().filter(City.created_at.between(start_time, current_time)).delete(synchronize_session=False)

    @classmethod
    def bulk_insert(cls, cities: [City]):
        City.bulk_insert(cities)
