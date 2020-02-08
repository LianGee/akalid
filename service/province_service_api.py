#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : province_service_api.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  :
from abc import ABCMeta, abstractmethod

from model.province import Province


class ProvinceServiceApi(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def save(cls, province: Province):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def query_all(cls):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def query_today(cls):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def delete_today(cls):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def bulk_insert(cls, provinces: [Province]):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def query_with_time(cls, start: int, end: int):
        raise NotImplementedError()
