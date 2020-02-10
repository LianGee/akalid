#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : summary_service.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :
from datetime import datetime

from common.log import Logger
from model.app.china_summary import ChinaSummary
from model.city import City
from model.history import History
from model.province import Province
from model.world import World
from service.summary_service_api import SummaryServiceApi

log = Logger(__name__)


class SummaryService(SummaryServiceApi):

    @classmethod
    def history(cls):
        return History.select().order_by(History.date.asc()).all()

    @classmethod
    def overseas(cls, date):
        if date is None:
            date = datetime.now().strftime('%Y%m%d')
        words = World.select().filter(World.date == date).all()
        return words

    @classmethod
    def china_detail(cls, date):
        if date is None:
            date = datetime.now().strftime('%Y%m%d')
        provinces = Province.select().filter(Province.date == date).all()
        cities = City.select().filter(City.date == date).all()
        city_map = {}
        for city in cities:
            cs = city_map.get(city.province_name, [])
            if len(cs) == 0:
                city_map[city.province_name] = []
            city_map[city.province_name].append(city.get_json())
        result = []
        for province in provinces:
            res = province.get_json()
            res['cities'] = city_map.get(province.province_name)
            result.append(res)
        return result

    @classmethod
    def china_daily(cls, date):
        if date is None:
            date = datetime.now().strftime('%Y%m%d')
        world = World.select().filter(World.date == date, World.name == '中国').one()
        return world

    @classmethod
    def china_summary(cls, date):
        if date is None:
            date = datetime.now().strftime('%Y%m%d')
        provinces = Province.select() \
            .filter(Province.country == '中国', Province.date == date) \
            .order_by(Province.confirmed.asc()) \
            .all()
        province_names = [province.province_name for province in provinces]
        cities = City.select() \
            .filter(City.province_name.in_(province_names), City.date == date) \
            .order_by(City.confirmed.asc()) \
            .all()
        china_summary = ChinaSummary(
            cured=0,
            confirmed=0,
            dead=0,
            suspected=0,
            cities={},
            province_level={},
            provinces={}
        )
        city_map = {}
        for city in cities:
            if city.province_name in city_map.keys():
                city_map[city.province_name].append(city.get_json())
            else:
                city_map[city.province_name] = [
                    city.get_json()
                ]
        for province in provinces:
            china_summary.provinces[province.short_name] = {
                'cured': province.cured,
                'confirmed': province.confirmed,
                'dead': province.dead,
                'suspected': province.suspected
            }
            china_summary.cured += province.cured
            china_summary.confirmed += province.confirmed
            china_summary.dead += province.dead
            china_summary.suspected += province.suspected
            china_summary.province_level[province.short_name] = cls.summary_section(province.confirmed)
            log.info(f'{province.province_name} has {len(city_map.get(province.province_name, []))} cities')
        china_summary.cities = city_map
        log.info(f'total provinces {len(provinces)}')
        return china_summary

    @classmethod
    def summary_section(cls, num):
        if 1 <= num <= 9:
            return 0
        elif 10 <= num <= 99:
            return 1
        elif 100 <= num <= 499:
            return 2
        elif 500 <= num <= 999:
            return 3
        elif 1000 <= num <= 10000:
            return 4
        return 5
