# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 上午11:36
# @Author  : Wang Junling
# @File    : douyin_main.py
# @Software: PyCharm
import asyncio

# from douyin_code.DouyinAPI import DouyinAPI
# CURSOR = 0
# COUNT = 20
# OPEN_ID = '78736b39-6a0f-4599-b2e8-eb166c9611cb'
# ACCESS_TOKEN = 'act.2b75374a6f740ad4e34b2b01af9fa1e3pLhNT5fyVYR1ch8I1WPtCxfPULzn'
#
# print(DouyinAPI.run_get_posts(1,open_id=OPEN_ID,access_token=ACCESS_TOKEN,count=COUNT,cursor=CURSOR))
# DOMAIN = "open.douyin.com"
# PROTOCOL = "https"
# print(douyin_api)

# for i in result:
#     print(i)


a = {"access_token": "act.2b75374a6f740ad4e34b2b01af9fa1e3pLhNT5fyVYR1ch8I1WPtCxfPULzn",
     "refresh_token": "rft.a859cc0fe735c47993589de2c1e6074592BieSnESErUzfYERjqEfKG7hpAW",
     "open_id": "78736b39-6a0f-4599-b2e8-eb166c9611cb",
     "备注": "access_token用来获取用户数据，refresh_token用来刷新access_token",
     'client_key':'awus2ha9snrpmf7c',
     'grant_type':'refresh_token'}


import requests
import json
def openDouyin(url: str, params: dict):
    rep = requests.get(url, params=params)
    return json.loads(rep.text)
'78736b39-6a0f-4599-b2e8-eb166c9611cb'
params = {'open_id': 'fd7953f6-a3ac-450c-b0b5-feae26cfc337',
          'access_token':'act.67b913f6cefe0bc54bca274f2d3f2790W9FxXuHNSXUsDYoBSJO8lXooLEfH'
          }
print(openDouyin(r'https://open.douyin.com/oauth/refresh_token/',a))
