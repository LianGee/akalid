#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : city_service_api.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :
from abc import ABCMeta, abstractmethod

from model.city import City


class CityServiceApi(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def delete_today(cls):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def bulk_insert(cls, cities: [City]):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def query_by_time(cls, start: int, end: int):
        raise NotImplementedError()
