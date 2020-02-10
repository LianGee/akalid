#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : summary.py
# @Author: zaoshu
# @Date  : 2020-02-07
# @Desc  :

from flask import Blueprint, request

from common.login import login_required
from common.response import Response
from service.impl.summary_service import SummaryService

summary_bp = Blueprint('summary', __name__)


@summary_bp.route('/china', methods=['GET'])
@login_required
def summary_china():
    date = request.args.get('date')
    return Response.success(SummaryService.china_summary(date))


@summary_bp.route('/china/daily', methods=['GET'])
@login_required
def china_daily():
    date = request.args.get('date')
    return Response.success(SummaryService.china_daily(date))


@summary_bp.route('/china/detail', methods=['GET'])
@login_required
def china_detail():
    date = request.args.get('date')
    return Response.success(SummaryService.china_detail(date))


@summary_bp.route('/overseas', methods=['GET'])
@login_required
def overseas():
    date = request.args.get('date')
    return Response.success(SummaryService.overseas(date))


@summary_bp.route('/history', methods=['GET'])
@login_required
def history():
    return Response.success(SummaryService.history())
