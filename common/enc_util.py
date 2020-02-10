#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : enc_util.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
import hashlib


def md5(s: str) -> str:
    m = hashlib.md5()
    m.update(s.encode('utf8'))
    return m.hexdigest()
