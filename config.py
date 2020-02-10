#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  :
import os

APP_NAME = 'akalid'
SECRET_KEY = 'XKCWJC6KN99GRZPOYDJTALF45WG3RNQ9'
JSONIFY_PRETTYPRINT_REGULAR = True
JSON_AS_ASCII = False
DEBUG = True
FLASK_USE_RELOAD = True
BASE_DIR = os.path.abspath(os.getcwd())
EXCEL_PATH = BASE_DIR + '/data/excel/'
EXCEL_EXPORT = {
    'encoding': 'utf_8_sig',
}
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
