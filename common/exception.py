#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : exception.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  : 


class ServerException(Exception):
    class ServerException(Exception):
        def __init__(self, code, msg):
            self.msg = msg
            self.code = code

        def __str__(self):
            return f'{self.msg}'
