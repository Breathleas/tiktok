# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 18:21
# @Author  : Wang Junling
# @Email   : wang_junling@yeah.net
# @File    : new_issue_porxy.py
# @Software: PyCharm
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
    if '/aweme/v1/aweme/post/?' in flow.request.url:
        # 发布详细信息
        # print(flow.response.text)
        for user in json.loads(flow.response.text)['aweme_list']:
            print(user)
            insert_sql = f"""
            insert into tiktok.tiktok_new_issue(user_id,issue_id,json_content,issue_date,present_time,flag) values (
                                {user.get('author_user_id')},{user.get('aweme_id')},
                                '{pymysql.escape_string(json.dumps(user, ensure_ascii=False))}',{user.get(
                'create_time')},{int(time.time())},0)"""
            try:
                cursor.execute(insert_sql)
                connect.commit()
            except Exception as err:
                logging.error(err)
