#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : daily_info_service.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
import json
import os
from datetime import datetime

from flask import g
from sqlalchemy.orm.exc import NoResultFound

from common.constant import ErrorCode, Symptom
from common.exception import ServerException
from config import EXCEL_EXPORT, EXCEL_PATH
from model.daily_info import DailyInfo
from model.user import User
import pandas as pd


class DailyInfoService:

    @classmethod
    def save(cls, args: dict) -> bool:
        if cls.has_done(g.user.name):
            raise ServerException(msg='今天已经填过了', code=ErrorCode.FAILED)
        daily_info = DailyInfo(
            name=g.user.name,
            date=datetime.now().strftime('%Y%m%d'),
            in_sh=args.get('in_sh'),
            health=args.get('health'),
            symptom=json.dumps(args.get('symptom', [])),
            contact_history=args.get('contact_history'),
            access_public=args.get('access_public'),
            return_date=args.get('return_date'),
            note=args.get('note')
        )
        DailyInfo.insert(daily_info)
        return True

    @classmethod
    def has_done(cls, name: str):
        try:
            date = datetime.now().strftime('%Y%m%d')
            DailyInfo.select().filter(DailyInfo.name == name, DailyInfo.date == date).one()
        except NoResultFound:
            return False
        return True

    @classmethod
    def query(cls, start, end):
        if start is None or end is None:
            start = end = datetime.now().strftime('%Y%m%d')
        results = []
        daily_infos: [DailyInfo] = DailyInfo.select().filter(DailyInfo.date.between(start, end))\
            .order_by(DailyInfo.created_at.asc()).all()
        if len(daily_infos) == 0:
            return results
        names = [daily_info.name for daily_info in daily_infos]
        users = User.select().filter(User.name.in_(names)).all()
        user_map = {}
        for user in users:
            if user_map.get(user.name) is None:
                user_map[user.name] = user
        for daily_info in daily_infos:
            info = {
                'id': daily_info.id,
                'date': daily_info.date,
                'in_sh': '是' if daily_info.in_sh else '否', 'health': '健康' if daily_info.health else '异常',
                'symptom': ','.join([Symptom.CODE.get(symptom, '') for symptom in json.loads(daily_info.symptom)]),
                'chinese_name': user_map.get(daily_info.name).chinese_name,
                'is_inner_staff': '是' if user_map.get(daily_info.name).is_inner_staff else '否',
                'location': user_map.get(daily_info.name).location,
                'contact_history': '有' if daily_info.contact_history else '无',
                'access_public': '是' if daily_info.access_public else '否',
                'return_date': daily_info.return_date,
                'note': daily_info.note
            }
            results.append(info)
        return results

    @classmethod
    def excel_download(cls, start, end):
        results = cls.query(start, end)
        df = pd.DataFrame(results)
        order = [
            'id', 'date', 'chinese_name', 'is_inner_staff',
            'in_sh', 'location', 'health', 'symptom',
            'contact_history', 'access_public', 'return_date', 'note'
        ]
        df = df[order]
        header = [
            'id', '日期', '姓名', '是否在沪',
            '是否所内员工', '所在地', '身体状况', '症状',
            '接触史', '近期外出公共场所', '返沪日期', '备注'
        ]
        file_name = g.user.name + '_' + datetime.now().strftime("%Y%m%d_%H%M%S") + '.xlsx'
        path_name = EXCEL_PATH + file_name
        if os.path.exists(path_name):
            return file_name
        include_index = not isinstance(df.index, pd.RangeIndex)
        writer = pd.ExcelWriter(path_name, engine='xlsxwriter')
        df.to_excel(writer, index=include_index, header=header, **EXCEL_EXPORT)
        writer.save()
        return file_name
