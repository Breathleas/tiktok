# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 下午12:21
# @Author  : Wang Junling
# @File    : doyin_api.py
# @Software: PyCharm

import time


def time_get(fun):
    def wrapper(*args, **kwargs):
        a = time.time()
        fun()
        print(time.time() - a)

    return wrapper


page = 0
params = {
    'cursor': page,
    'count': 20,
    'open_id': '78736b39-6a0f-4599-b2e8-eb166c9611cb',
    'access_token': 'act.2b75374a6f740ad4e34b2b01af9fa1e3pLhNT5fyVYR1ch8I1WPtCxfPULzn'
}
"""
{"access_token": "act.2b75374a6f740ad4e34b2b01af9fa1e3pLhNT5fyVYR1ch8I1WPtCxfPULzn", "refresh_token": "rft.a859cc0fe735c47993589de2c1e6074592BieSnESErUzfYERjqEfKG7hpAW", "open_id": "78736b39-6a0f-4599-b2e8-eb166c9611cb", "备注": "access_token用来获取用户数据，refresh_token用来刷新access_token"}
"""
import requests
import json


# import celery
# import redis
#
# backend = 'redis://127.0.0.1:6379/1'
# broker = 'redis://127.0.0.1:6379/2'
# cel = celery.Celery('doyin_api', broker=broker)
#

# @cel.task
def openDouyin(url: str, params: dict, ):
    rep = requests.get(url, params=params)
    return json.loads(rep.text)


page = 0
jisu = 1
# while 1:
count = 20
open_id = '78736b39-6a0f-4599-b2e8-eb166c9611cb'
access_token = 'act.2b75374a6f740ad4e34b2b01af9fa1e3pLhNT5fyVYR1ch8I1WPtCxfPULzn'

import asyncio
from aiohttp import ClientSession

url = fr'https://open.douyin.com/fans/list/?cursor={page}&count={count}&open_id={open_id}&access_token={access_token}'


async def hello(url):
    url = fr'https://open.douyin.com/fans/list/?cursor={page}&count={count}&open_id={open_id}&access_token={access_token}'
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
    return json.loads(response)

@time_get
def run():
    tasks = []
    for i in range(5):
        task = asyncio.ensure_future(hello(url.format(i)))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()


#     data=openDouyin(r'', params)
#     print(data)
#     page=data.get('data').get('cursor')
#     has_more=data.get('data').get('has_more')
#     if has_more:
#         jisu+=1
#     else:
#         break
#
# print(jisu)

# 获得网红基本信息
params = {'open_id': 'fd7953f6-a3ac-450c-b0b5-feae26cfc337',
          'access_token':'act.67b913f6cefe0bc54bca274f2d3f2790W9FxXuHNSXUsDYoBSJO8lXooLEfH'
          }
print(openDouyin(r'https://open.douyin.com/oauth/userinfo/',params))


# 获取粉丝信息
# params = {'cursor': 0,
#           'count': 20,
#           'open_id': 'fd7953f6-a3ac-450c-b0b5-feae26cfc337',
#           'access_token':'act.67b913f6cefe0bc54bca274f2d3f2790W9FxXuHNSXUsDYoBSJO8lXooLEfH'
#           }
#

#


# 获得关注
# params = {'cursor': 0,
#           'count': 20,
#           'open_id': 'fd7953f6-a3ac-450c-b0b5-feae26cfc337',
#           'access_token':'act.67b913f6cefe0bc54bca274f2d3f2790W9FxXuHNSXUsDYoBSJO8lXooLEfH'
#           }
# openDouyin(r'https://open.douyin.com/following/list/',params)

#
# params = {'cursor': 0,
#           'count': 20,
#           'open_id': 'fd7953f6-a3ac-450c-b0b5-feae26cfc337',
#           'access_token':'act.67b913f6cefe0bc54bca274f2d3f2790W9FxXuHNSXUsDYoBSJO8lXooLEfH'
#           }
# openDouyin(r'https://open.douyin.com/video/list/',params)


# 获取发布视频
@time_get
def aa():
    for _ in range(5):
        print(openDouyin(r'https://open.douyin.com/video/list/', params))


if __name__ == '__main__':
    aa()
