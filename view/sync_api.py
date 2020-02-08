#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sync_api.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :
from flask import Blueprint

from common.response import Response
from service.impl.sync_service import SyncService

sync_bp = Blueprint('sync', __name__)


@sync_bp.route('/')
def sync():
    SyncService.sync()
    return Response.success(True)
