#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sync_service.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :
import json
import os
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from common.log import Logger
from model.city import City
from model.history import History
from model.province import Province
from model.world import World
from service.impl.crawler_service import CrawlerService
from service.sync_service_api import SyncServiceApi

log = Logger(__name__)


class SyncService(SyncServiceApi):

    @classmethod
    def sync(cls):
        now = datetime.now().strftime('%Y-%m-%d_%H')
        log.info(f'begin sync {now}')
        file_name = f"./data/{now}.json"
        if not os.path.exists(file_name):
            CrawlerService.crawler()
        raw_data = json.load(open(file_name, 'r'))
        data = raw_data['initialState']['nCoV2019']['trends']
        date = datetime.now().strftime('%Y%m%d')
        world = World(
            date=date,
            name='中国',
            confirmed=data['totalConNum'],
            suspected=data['totalSusNum'],
            cured=data['totalCureNum'],
            dead=data['totalDeathNum'],
            add_confirmed=data['addCon'],
            add_cured=data['addCure'],
            add_dead=data['addDeath'],
            add_suspected=data['addSus']
        )
        history_list = data['historyList']
        histories = []
        for history in history_list:
            histories.append(History(
                date=history['date'],
                confirmed=history['conNum'],
                cured=history['cureNum'],
                dead=history['deathNum'],
                suspected=history['susNum']
            ))
        overseas_list = data['overseasList']
        worlds = []
        for overseas in overseas_list:
            worlds.append(
                World(
                    date=date,
                    confirmed=overseas['conNum'],
                    cured=overseas['cureNum'],
                    suspected=overseas['susNum'],
                    dead=overseas['deathNum'],
                    name=overseas['name']
                )
            )
        domestic_list = data['domesticList']
        provinces = []
        cities = []
        for domestic in domestic_list:
            provinces.append(
                Province(
                    date=date,
                    province_name=domestic['name'],
                    short_name=domestic['name'],
                    confirmed=domestic['conNum'],
                    dead=domestic['deathNum'],
                    suspected=domestic['susNum'],
                    cured=domestic['cureNum']
                )
            )
            city_list = domestic['cities']
            for city in city_list:
                cities.append(
                    City(
                        date=date,
                        province_name=domestic['name'],
                        city_name=city['name'],
                        confirmed=city['conNum'],
                        suspected=city['susNum'],
                        cured=city['cureNum'],
                        dead=city['deathNum']
                    )
                )
        History.select().delete()
        History.bulk_insert(histories)
        World.select().filter(World.date == date).delete()
        world.insert()
        World.bulk_insert(worlds)
        Province.select().filter(Province.date == date).delete()
        Province.bulk_insert(provinces)
        City.select().filter(City.date == date).delete()
        City.bulk_insert(cities)
        log.info(f'sync {now} done')


scheduler = BackgroundScheduler()
scheduler.add_job(SyncService.sync, trigger='interval', minutes=1, id='sync')
scheduler.start()
