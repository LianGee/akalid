#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : CrawlerService.py
# @Author: zaoshu
# @Date  : 2020-02-08
# @Desc  :
import json
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup

from common.http_util import HttpUtil
from common.log import Logger

log = Logger(__name__)


class CrawlerService:

    @classmethod
    def crawler(cls):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        url = 'https://www.zhihu.com/2019-nCoV/trends'
        http_util = HttpUtil(
            url,
            method=['GET'],
            headers={
                'user-agent': user_agent,
                'accept': accept
            }
        )
        raw_data = http_util.get()
        soup = BeautifulSoup(raw_data.content, features="html.parser")
        values = soup.find_all(name='script', attrs={'type': 'text/json'})
        now = datetime.now().strftime('%Y-%m-%d_%H')
        log.info(f"{'--' * 20}starting {now}{'--' * 20}")
        f = open(f"./data/{now}.json", 'w')
        f.write(values[1].contents[0])
        log.info(json.loads(values[1].contents[0]))
        log.info(f"{'--' * 20}{now} done{'--' * 20}")
