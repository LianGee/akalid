#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
from flask import Blueprint, request, g

from common.log import Logger
from common.login import login_required
from common.response import Response
from model.user import User
from service.impl.user_service import UserService

user_bp = Blueprint('user', __name__)
log = Logger(__name__)


@user_bp.route('/login', methods=['POST'])
def login():
    args = request.json
    name = args.get('userName')
    password = args.get('password')
    data = UserService.login(name, password)
    status = 'ok' if data else 'error'
    return Response.success(status=status, data=data)


@user_bp.route('/register', methods=['POST'])
def register():
    args = request.json
    user = User(
        name=args['name'],
        chinese_name=args['chinese_name'],
        email=args['email'],
        password=args['password'],
        is_inner_staff=args['is_inner_staff'],
        location=args['location'],
        sh_location=args['sh_location']
    )
    return Response.success(UserService.register(user))


@user_bp.route('/current', methods=['GET'])
@login_required
def current():
    return Response.success(g.user)


