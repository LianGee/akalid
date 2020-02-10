#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : summary_service_api.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :
from abc import ABCMeta, abstractmethod


class SummaryServiceApi(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def china_summary(cls, date):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def china_daily(cls, date):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def china_detail(cls, date):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def overseas(cls, date):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def history(cls):
        raise NotImplementedError()
