#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ChinaSummary.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  : 


class ChinaSummary(object):
    def __init__(self, cured, confirmed, dead, suspected, cities, province_level, provinces):
        self.cured = cured
        self.confirmed = confirmed
        self.dead = dead
        self.suspected = suspected
        self.cities = cities
        self.province_level = province_level
        self.provinces = provinces
