# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 17:22
# @Author  : Wang Junling
# @Email   : wang_junling@yeah.net
# @File    : mitm_comment.py
# @Software: PyCharm
import pymysql
import json
import logging
import time
import re
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
    if 'comment/list/?' in flow.request.url:
        # 发布详细信息
        # uid=re.findall("\?user_id=(.*?)&sec_user_id", flow.request.url)[0]
        for data in json.loads(flow.response.text)['comments']:
            try:

                use = data.get('user')
                sql = f"""insert into tiktok.tiktok_comment_tests(issue_id,user_id,comment_id,search_id,
                json_content,date,flag) values ('{data.get('aweme_id')}','{use.get('uid')}','{data.get('cid','')}',
                '{use.get('short_id') if use.get('short_id') else use.get(
                    'unique_id')}','{pymysql.escape_string(json.dumps(data, ensure_ascii=False))}','{data.get(
                    'create_time')}',0)"""
                '''
                评论入库：通过截取评论内容的数据包来分析每个字段，发布id,用户id，评论id,抖音号，json数据，创建时间。
                '''
                cursor.execute(sql)
                connect.commit()
            except Exception as err:
                print(err)
                logging.error(err)