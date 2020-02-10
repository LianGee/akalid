#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : constant.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  : 


class ErrorCode:
    SUCCESS = 0
    FAILED = 500


class HttpCode:
    HTTP_SUCCESS = [201, 200]


class Symptom:
    CODE = {
        0: '发热',
        1: '咳嗽',
        2: '验证',
        3: '其他',
        4: '疑似感染'
    }
