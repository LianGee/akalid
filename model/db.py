#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : db.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  :
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import config

engine = create_engine(config.DEFAULT_DATABASE_URL,
                       convert_unicode=True,
                       **config.DB_KWARGS)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Model = declarative_base()
Model.query = db_session.query_property()

