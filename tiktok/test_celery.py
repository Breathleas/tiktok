# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 上午11:45
# @Author  : Wang Junling
# @File    : test_celery.py
# @Software: PyCharm
import celery
import redis

backend='redis://127.0.0.1:6379/1'
broker='redis://127.0.0.1:6379/2'
cel=celery.Celery('test_celery',backend=backend,broker=broker)
@cel.task
def add(x,y):
    return x+y
