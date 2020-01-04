# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 16:51
# @Author  : Wang Junling
# @Email   : wang_junling@yeah.net
# @File    : mitmprotyx.py
# @Software: PyCharm
import pymysql
import json
import logging
import time
# 这个地方必须这么写 函数名：response
LOGGING_FORMAT = '%(asctime)-15s:%(levelname)s: %(message)s'
logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO,
                    filename='mitmprotxy.log', filemode='a', )
connect = pymysql.connect(host='52.81.170.174',
                          user='wangjunling',
                          password='Wjl1314520.',
                          db='tiktok',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
cursor = connect.cursor()

def response(flow):
    # 通过抓包软包软件获取请求的接口
    # print(flow)
    # if 'aweme/v1/user/follower/list' in flow.request.url:
    #     # 数据的解析
    #     for user in json.loads(flow.response.text)['followers']:
    #
    #         print(user)
    if '/aweme/v1/aweme/post/?' in flow.request.url:
        # 发布详细信息
        # print(flow.response.text)
        for user in json.loads(flow.response.text)['aweme_list']:
            # print(user)
            sql = f"""insert into tiktok.tiktok_issue_test(user_id,issue_id,json_content,date,type,flag) values (
                                {user.get('author_user_id')},{user.get('aweme_id')},
                                '{pymysql.escape_string(json.dumps(user, ensure_ascii=False))}',{time.strftime("%Y%m%d", time.localtime())},0,0)"""
            """
            获取发数据包的信息，将每一条数据存入数据库，第一条为作者id,视频id和，json包，爬虫时间
            """
            try:
                cursor.execute(sql)
                connect.commit()
            except Exception as err:
                logging.error(err)
    # 用户详细信息插入
    if '/aweme/v1/user/?' in flow.request.url:
        if 'user_id = 962818056395822'not in flow.request.url:
            dd=json.loads(flow.response.text)['user']
            if int(dd.get('uid')) not in [55164137674,107697660200]:
                # print(dd)
                sql = f"""insert into tiktok.tiktok_user_test(id,`user_id`,`json_content`,`date`,`type`,`flag`) values (
                      0,{dd.get('uid')},'{pymysql.escape_string(flow.response.text)}',{time.strftime("%Y%m%d", time.localtime())},0,0)"""

                """
                将详细的用户数据插入数据库种。uid,json,爬取时间
                """
                try:
                    cursor.execute(sql)
                    connect.commit()
                except Exception as err:
                    logging.error(err)


