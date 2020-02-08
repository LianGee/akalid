#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sync_service_api.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :
from abc import ABCMeta, abstractmethod


class SyncServiceApi(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def sync(cls):
        raise NotImplementedError()
