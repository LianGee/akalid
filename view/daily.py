#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : daily.py.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
from flask import Blueprint, g, request, send_from_directory

from common.login import login_required
from common.response import Response
from config import EXCEL_PATH
from service.impl.daily_info_service import DailyInfoService

daily_bp = Blueprint('daily', __name__)


@daily_bp.route('/info/has/done', methods=['GET'])
@login_required
def has_done():
    return Response.success(DailyInfoService.has_done(g.user.name))


@daily_bp.route('/info/save', methods=['POST'])
@login_required
def info_save():
    args = request.json
    return Response.success(DailyInfoService.save(args))


@daily_bp.route('/info/statistic', methods=['GET'])
@login_required
def daily_info_statistic():
    start = request.args.get('start')
    end = request.args.get('end')
    return Response.success(DailyInfoService.query(start, end))


@daily_bp.route('/info/download', methods=['GET'])
@login_required
def info_download():
    start = request.args.get('start')
    end = request.args.get('end')
    file_name = DailyInfoService.excel_download(start, end)
    return send_from_directory(EXCEL_PATH, file_name, as_attachment=True)
