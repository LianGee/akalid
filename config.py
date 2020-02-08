#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  : 

APP_NAME = 'epidemic'
JSONIFY_PRETTYPRINT_REGULAR = True
JSON_AS_ASCII = False
DEBUG = True
FLASK_USE_RELOAD = True
DEFAULT_DATABASE_URL = 'mysql+mysqlconnector://root:123456@localhost:3306/epidemic?charset=utf8'
DB_KWARGS = {
    'pool_recycle': 360,
    'pool_size': 100,
    'max_overflow': 10,
    'logging_name': 'sqlalchemy',
}
DATABASES = {
    "default": DEFAULT_DATABASE_URL,
}
