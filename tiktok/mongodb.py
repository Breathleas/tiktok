# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 上午11:34
# @Author  : Wang Junling
# @File    : mongodb.py
# @Software: PyCharm


from pymongo import MongoClient
import urllib.parse
etcd_host = '54.223.192.102'
etcd_port = '27017'
etcd_username = 'douyin_scraper'
etcd_password = 'z32MH!c2l4XyxiwClkQ4'
etcd_db = 'DouyinDB'
etcd_tatle='posts'
username = urllib.parse.quote_plus(etcd_username)
password = urllib.parse.quote_plus(etcd_password)
client = MongoClient('mongodb://%s:%s@%s:%s/?authSource=DouyinDB&authMechanism=SCRAM-SHA-256'  % (username, password, etcd_host, etcd_port))
db = client[etcd_db]
table = db.posts

for i in table.find():
    print(i)

