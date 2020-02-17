#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sync_api.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :
from flask import Blueprint

from common.login import login_required
from common.response import Response
from service.impl.crawler_service import CrawlerService
from service.impl.sync_service import SyncService

sync_bp = Blueprint('sync', __name__)


@sync_bp.route('/')
def sync():
    SyncService.sync()
    return Response.success(True)


@sync_bp.route('/crawler')
def crawler():
    CrawlerService.crawler()
    return Response.success(True)
